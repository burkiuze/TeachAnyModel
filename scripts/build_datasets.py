#!/usr/bin/env python3
"""Export the repository's data into ready-to-train formats.

Sources
    corpus/**/*.md          long-form reference documents (Markdown + YAML front matter)
    qa/*.jsonl              hand-written conceptual question/answer pairs
    generated/*.jsonl       synthetic step-by-step problems (scripts/generate_problems.py)

Outputs (written to --out, default ``dist/``; each SFT file also gets a train/validation split)
    pretrain.jsonl          {"text", "source"}: one document per line for continued pretraining
    rag_chunks.jsonl        {"id", "title", "section", "field", "text"}: section-level chunks for retrieval
    sft_alpaca.jsonl        {"instruction", "input", "output"}
    sft_sharegpt.jsonl      {"conversations": [{"from": "human"|"gpt", "value"}]}
    sft_chat.jsonl          {"messages": [{"role": "system"|"user"|"assistant", "content"}]}  (OpenAI / HF chat format)

Examples
    python scripts/build_datasets.py
    python scripts/build_datasets.py --out /tmp/science --val-fraction 0.02 --system-prompt "You are a physics tutor."
    python scripts/build_datasets.py --no-generated          # only hand-written material
"""

import argparse
import glob
import hashlib
import json
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DEFAULT_SYSTEM = (
    "You are a knowledgeable science tutor. Explain concepts accurately and show your reasoning step by step, "
    "using LaTeX for mathematics."
)


# ---------------------------------------------------------------------------
# Readers
# ---------------------------------------------------------------------------


def parse_front_matter(text):
    """Split ``---``-delimited YAML front matter (simple ``key: value`` / ``[a, b]`` subset) from the body."""
    meta = {}
    if not text.startswith("---\n"):
        return meta, text
    end = text.index("\n---", 4)
    for line in text[4:end].splitlines():
        if ":" not in line:
            continue
        key, val = line.split(":", 1)
        val = val.strip()
        if val.startswith("[") and val.endswith("]"):
            meta[key.strip()] = [v.strip().strip("'\"") for v in val[1:-1].split(",") if v.strip()]
        else:
            meta[key.strip()] = val.strip("'\"")
    body = text[end + 4:].lstrip("\n")
    return meta, body


def read_corpus(root):
    docs = []
    for path in sorted(glob.glob(os.path.join(root, "corpus", "**", "*.md"), recursive=True)):
        with open(path, encoding="utf-8") as fh:
            meta, body = parse_front_matter(fh.read())
        docs.append({"path": os.path.relpath(path, root), "meta": meta, "body": body.strip()})
    return docs


def read_jsonl(pattern):
    rows = []
    for path in sorted(glob.glob(pattern)):
        with open(path, encoding="utf-8") as fh:
            for line in fh:
                line = line.strip()
                if line:
                    rows.append(json.loads(line))
    return rows


# ---------------------------------------------------------------------------
# Transformations
# ---------------------------------------------------------------------------


def chunk_document(doc, max_chars=4000):
    """Split a document at ``##`` headings; long sections are split further at ``###`` or paragraphs."""
    title = doc["meta"].get("title", os.path.basename(doc["path"]))
    sections = re.split(r"(?m)^(?=## )", doc["body"])
    chunks = []
    for sec in sections:
        sec = sec.strip()
        if not sec:
            continue
        heading = sec.splitlines()[0].lstrip("# ").strip() if sec.startswith("#") else title
        pieces = [sec]
        if len(sec) > max_chars:
            pieces = [p for p in re.split(r"(?m)^(?=### )", sec) if p.strip()]
        for piece in pieces:
            while len(piece) > max_chars:
                cut = piece.rfind("\n\n", 0, max_chars)
                cut = cut if cut > max_chars // 4 else max_chars
                chunks.append((heading, piece[:cut].strip()))
                piece = piece[cut:]
            if piece.strip():
                chunks.append((heading, piece.strip()))
    out = []
    for i, (heading, text) in enumerate(chunks):
        out.append({
            "id": f"{doc['path'][:-3].replace(os.sep, '/')}#{i:03d}",
            "title": title,
            "section": heading,
            "field": doc["meta"].get("field", ""),
            "text": f"# {title}\n\n{text}" if not text.startswith("# ") else text,
        })
    return out


def sft_pairs(qa_rows, problems):
    """Yield (id, prompt, response) triples from the Q&A files and the generated problems."""
    for row in qa_rows:
        yield row["id"], row["question"], row["answer"]
    for rec in problems:
        yield rec["id"], rec["question"], rec["solution"]


def is_validation(key, fraction):
    """Deterministic split: hash the record id so the split is stable across runs and machines."""
    if fraction <= 0:
        return False
    h = int(hashlib.sha256(key.encode("utf-8")).hexdigest()[:8], 16)
    return h / 0xFFFFFFFF < fraction


def write_jsonl(path, rows):
    with open(path, "w", encoding="utf-8") as fh:
        for row in rows:
            fh.write(json.dumps(row, ensure_ascii=False) + "\n")
    return len(rows)


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--out", default=os.path.join(ROOT, "dist"), help="output directory (default dist/)")
    ap.add_argument("--val-fraction", type=float, default=0.05, help="fraction of SFT pairs held out (default 0.05)")
    ap.add_argument("--system-prompt", default=DEFAULT_SYSTEM, help="system message for sft_chat.jsonl ('' for none)")
    ap.add_argument("--no-generated", action="store_true", help="skip generated/*.jsonl")
    ap.add_argument("--no-qa", action="store_true", help="skip qa/*.jsonl")
    ap.add_argument("--chunk-chars", type=int, default=4000, help="maximum characters per RAG chunk")
    args = ap.parse_args(argv)

    os.makedirs(args.out, exist_ok=True)
    docs = read_corpus(ROOT)
    qa_rows = [] if args.no_qa else read_jsonl(os.path.join(ROOT, "qa", "*.jsonl"))
    problems = [] if args.no_generated else read_jsonl(os.path.join(ROOT, "generated", "*.jsonl"))

    # pretraining text: documents, then Q&A and worked problems rendered as plain text
    pretrain = [{"text": d["body"], "source": d["path"]} for d in docs]
    pretrain += [{"text": f"Question: {r['question']}\n\nAnswer: {r['answer']}", "source": f"qa:{r['id']}"}
                 for r in qa_rows]
    pretrain += [{"text": f"Problem: {p['question']}\n\n{p['solution']}", "source": f"generated:{p['id']}"}
                 for p in problems]
    counts = {"pretrain.jsonl": write_jsonl(os.path.join(args.out, "pretrain.jsonl"), pretrain)}

    chunks = [c for d in docs for c in chunk_document(d, args.chunk_chars)]
    counts["rag_chunks.jsonl"] = write_jsonl(os.path.join(args.out, "rag_chunks.jsonl"), chunks)

    splits = {"train": {"alpaca": [], "sharegpt": [], "chat": []}, "validation": {"alpaca": [], "sharegpt": [], "chat": []}}
    for key, prompt, response in sft_pairs(qa_rows, problems):
        split = "validation" if is_validation(key, args.val_fraction) else "train"
        splits[split]["alpaca"].append({"instruction": prompt, "input": "", "output": response})
        splits[split]["sharegpt"].append({"conversations": [{"from": "human", "value": prompt},
                                                            {"from": "gpt", "value": response}]})
        msgs = [{"role": "system", "content": args.system_prompt}] if args.system_prompt else []
        msgs += [{"role": "user", "content": prompt}, {"role": "assistant", "content": response}]
        splits[split]["chat"].append({"messages": msgs})
    for split, by_fmt in splits.items():
        suffix = "" if split == "train" else ".validation"
        for fmt_name, rows in by_fmt.items():
            name = f"sft_{fmt_name}{suffix}.jsonl"
            counts[name] = write_jsonl(os.path.join(args.out, name), rows)

    print(f"sources: {len(docs)} corpus documents, {len(qa_rows)} Q&A pairs, {len(problems)} generated problems")
    for name, n in counts.items():
        print(f"  {os.path.join(os.path.relpath(args.out, ROOT), name)}: {n} rows")
    return 0


if __name__ == "__main__":
    sys.exit(main())
