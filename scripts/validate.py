#!/usr/bin/env python3
"""Check the dataset for structural problems before training or committing.

Checks
    corpus/   front matter present with required keys; a level-1 title; balanced ``$`` math delimiters;
              no raw ``|`` inside math in Markdown table rows (it breaks the table — use ``\\vert``)
    qa/       valid JSON lines; required keys; unique ids; non-empty question/answer; balanced ``$``
    generated/ valid JSON lines; required keys; unique ids; finite numeric values; balanced ``$``

Exit status is 1 if any error is found.
"""

import glob
import json
import math
import os
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from build_datasets import parse_front_matter  # noqa: E402

CORPUS_KEYS = {"title", "field", "subfield", "level", "keywords"}
QA_KEYS = {"id", "field", "subfield", "difficulty", "question", "answer"}
PROBLEM_KEYS = {"id", "field", "subfield", "topic", "template", "difficulty", "question", "solution", "answer", "values"}
DIFFICULTIES = {"easy", "medium", "hard"}


def strip_code(text):
    """Remove fenced and inline code, where ``$`` and ``|`` carry no math meaning."""
    text = re.sub(r"```.*?```", "", text, flags=re.S)
    return re.sub(r"`[^`\n]*`", "", text)


def unbalanced_dollars(text):
    """Return the line numbers of paragraphs with an odd number of unescaped ``$``."""
    bad = []
    line_no = 1
    for para in re.split(r"\n\s*\n", strip_code(text)):
        if len(re.findall(r"(?<!\\)\$", para)) % 2:
            bad.append(line_no)
        line_no += para.count("\n") + 2
    return bad


def pipes_in_table_math(text):
    bad = []
    for i, line in enumerate(strip_code(text).splitlines(), 1):
        if not line.lstrip().startswith("|"):
            continue
        for seg in re.findall(r"(?<!\\)\$(.+?)(?<!\\)\$", line):
            if "|" in seg.replace("\\|", ""):
                bad.append(i)
                break
    return bad


def finite_values(obj):
    if isinstance(obj, float):
        return math.isfinite(obj)
    if isinstance(obj, dict):
        return all(finite_values(v) for v in obj.values())
    if isinstance(obj, list):
        return all(finite_values(v) for v in obj)
    return True


def check_corpus(errors):
    paths = sorted(glob.glob(os.path.join(ROOT, "corpus", "**", "*.md"), recursive=True))
    words = 0
    for path in paths:
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            text = fh.read()
        meta, body = parse_front_matter(text)
        missing = CORPUS_KEYS - set(meta)
        if missing:
            errors.append(f"{rel}: front matter missing {sorted(missing)}")
        if not re.search(r"(?m)^# \S", body):
            errors.append(f"{rel}: no level-1 title")
        for ln in unbalanced_dollars(body):
            errors.append(f"{rel}: unbalanced $ in paragraph starting near body line {ln}")
        for ln in pipes_in_table_math(body):
            errors.append(f"{rel}: raw | inside math in a table row (body line {ln}); use \\vert")
        words += len(body.split())
    return len(paths), words


def check_jsonl(pattern, required, errors, kind):
    ids = set()
    n = 0
    for path in sorted(glob.glob(pattern)):
        rel = os.path.relpath(path, ROOT)
        with open(path, encoding="utf-8") as fh:
            for ln, line in enumerate(fh, 1):
                if not line.strip():
                    continue
                n += 1
                try:
                    row = json.loads(line)
                except json.JSONDecodeError as exc:
                    errors.append(f"{rel}:{ln}: invalid JSON ({exc})")
                    continue
                missing = required - set(row)
                if missing:
                    errors.append(f"{rel}:{ln}: missing keys {sorted(missing)}")
                    continue
                if row["id"] in ids:
                    errors.append(f"{rel}:{ln}: duplicate id {row['id']}")
                ids.add(row["id"])
                if row["difficulty"] not in DIFFICULTIES:
                    errors.append(f"{rel}:{ln}: difficulty must be one of {sorted(DIFFICULTIES)}")
                text_fields = ["question", "answer"] + (["solution"] if kind == "generated" else [])
                for key in text_fields:
                    if not str(row[key]).strip():
                        errors.append(f"{rel}:{ln}: empty {key}")
                    elif unbalanced_dollars(str(row[key])):
                        errors.append(f"{rel}:{ln}: unbalanced $ in {key}")
                if kind == "generated" and not finite_values(row["values"]):
                    errors.append(f"{rel}:{ln}: non-finite number in values")
    return n


def main():
    errors = []
    n_docs, n_words = check_corpus(errors)
    n_qa = check_jsonl(os.path.join(ROOT, "qa", "*.jsonl"), QA_KEYS, errors, "qa")
    n_gen = check_jsonl(os.path.join(ROOT, "generated", "*.jsonl"), PROBLEM_KEYS, errors, "generated")
    print(f"corpus: {n_docs} documents, {n_words:,} words")
    print(f"qa: {n_qa} pairs")
    print(f"generated: {n_gen} problems")
    if errors:
        print(f"\n{len(errors)} problem(s):")
        for e in errors[:200]:
            print("  " + e)
        return 1
    print("OK — no problems found")
    return 0


if __name__ == "__main__":
    sys.exit(main())
