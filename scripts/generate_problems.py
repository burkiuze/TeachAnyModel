#!/usr/bin/env python3
"""Generate synthetic, step-by-step science problems with verifiable answers.

Every template draws fresh numbers from a seeded random generator, so the
output is fully reproducible: the same seed always yields the same file.

Examples
--------
    python scripts/generate_problems.py                       # default: 50 per template
    python scripts/generate_problems.py --per-template 500 --seed 7 --out big.jsonl
    python scripts/generate_problems.py --fields Chemistry Biology
    python scripts/generate_problems.py --templates weak_acid_ph nernst_equation
    python scripts/generate_problems.py --list
"""

import argparse
import collections
import json
import os
import random
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from problem_generators import REGISTRY, build  # noqa: E402

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def generate(per_template=50, seed=42, fields=None, templates=None, max_attempts_factor=20):
    """Yield problem records, ``per_template`` unique questions per template (fewer if a template has fewer variants)."""
    for meta in REGISTRY:
        if fields and meta["field"] not in fields:
            continue
        if templates and meta["name"] not in templates:
            continue
        rng = random.Random(f"{seed}:{meta['name']}")
        seen = set()
        made = 0
        attempts = 0
        while made < per_template and attempts < per_template * max_attempts_factor:
            attempts += 1
            data = meta["fn"](rng)
            if data["question"] in seen:
                continue
            seen.add(data["question"])
            yield build(meta, data, made)
            made += 1


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--per-template", type=int, default=50, help="unique problems per template (default 50)")
    ap.add_argument("--seed", type=int, default=42, help="random seed (default 42)")
    ap.add_argument("--out", default=os.path.join(ROOT, "generated", "problems.jsonl"), help="output JSONL path")
    ap.add_argument("--fields", nargs="*", help="only these fields, e.g. Physics Chemistry")
    ap.add_argument("--templates", nargs="*", help="only these template names")
    ap.add_argument("--list", action="store_true", help="list the available templates and exit")
    args = ap.parse_args(argv)

    if args.list:
        for meta in REGISTRY:
            print(f"{meta['field']:12s} {meta['subfield']:28s} {meta['difficulty']:7s} {meta['name']}")
        print(f"\n{len(REGISTRY)} templates")
        return 0

    out_dir = os.path.dirname(os.path.abspath(args.out))
    os.makedirs(out_dir, exist_ok=True)
    by_field = collections.Counter()
    by_difficulty = collections.Counter()
    n = 0
    with open(args.out, "w", encoding="utf-8") as fh:
        for rec in generate(args.per_template, args.seed, args.fields, args.templates):
            fh.write(json.dumps(rec, ensure_ascii=False) + "\n")
            by_field[rec["field"]] += 1
            by_difficulty[rec["difficulty"]] += 1
            n += 1
    print(f"wrote {n} problems to {os.path.relpath(args.out)}")
    for field, count in sorted(by_field.items()):
        print(f"  {field:12s} {count}")
    print("  by difficulty: " + ", ".join(f"{k} {v}" for k, v in sorted(by_difficulty.items())))
    return 0


if __name__ == "__main__":
    sys.exit(main())
