#!/usr/bin/env python3
"""Stress-test problem templates while writing them.

For every selected template this renders many problems and reports:
  * exceptions raised by the generator,
  * how many unique questions it can produce,
  * text problems: unbalanced ``$``, Python e-notation or nan/None leaking into the text,
    solutions that do not end with the stated answer,
  * non-finite numbers in ``values``,
  * mismatches against the independent re-computation in ``tests/checks_*.py`` or
    ``tests/test_generators.py`` (relative tolerance 1e-6), and templates that have no check,
  * questions that display a *rounded* version of an input stored in ``values`` (the problem
    would then not state the data actually used).

Examples
    python scripts/check_templates.py                         # every template
    python scripts/check_templates.py --module chemistry      # templates defined in one module
    python scripts/check_templates.py --template weak_acid_ph --samples 1000
"""

import argparse
import glob
import importlib
import importlib.util
import math
import os
import random
import re
import sys

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from problem_generators import REGISTRY, build  # noqa: E402

NUM = re.compile(r"(-?\d+(?:\.\d+)?)(?:\s*\\times\s*10\^\{(-?\d+)\})?")


def load_checks():
    """Collect CHECKS dicts (and DEDICATED name sets) from tests/test_generators.py and tests/checks_*.py."""
    checks, dedicated = {}, set()
    paths = [os.path.join(ROOT, "tests", "test_generators.py")]
    paths += sorted(glob.glob(os.path.join(ROOT, "tests", "checks_*.py")))
    for path in paths:
        if not os.path.exists(path):
            continue
        name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(f"_checks_{name}", path)
        mod = importlib.util.module_from_spec(spec)
        try:
            spec.loader.exec_module(mod)
        except Exception as exc:  # report but keep going
            print(f"WARNING: could not import {os.path.relpath(path, ROOT)}: {exc!r}")
            continue
        checks.update(getattr(mod, "CHECKS", {}))
        dedicated |= set(getattr(mod, "DEDICATED", ()))
    return checks, dedicated


def numbers(text):
    out = []
    for m in NUM.finditer(text):
        v = float(m.group(1))
        if m.group(2):
            v *= 10 ** int(m.group(2))
        out.append(v)
    return out


def finite(obj):
    if isinstance(obj, float):
        return math.isfinite(obj)
    if isinstance(obj, dict):
        return all(finite(v) for v in obj.values())
    if isinstance(obj, (list, tuple)):
        return all(finite(v) for v in obj)
    return True


def check_template(meta, checks, dedicated, samples, inputs_only):
    problems = []
    rng = random.Random(f"check:{meta['name']}")
    questions = set()
    display = 0
    mismatches = 0
    for i in range(samples):
        try:
            rec = build(meta, meta["fn"](rng), i)
        except Exception as exc:
            problems.append(f"exception: {exc!r}")
            break
        questions.add(rec["question"])
        text = rec["question"] + "\n" + rec["solution"]
        if text.count("$") % 2:
            problems.append(f"unbalanced $ in {rec['id']}")
        if re.search(r"\d\.?\d*e[+-]\d", text):
            problems.append(f"Python e-notation in text of {rec['id']}")
        if re.search(r"\b(nan|inf|None)\b", text):
            problems.append(f"nan/inf/None in text of {rec['id']}")
        if not rec["solution"].rstrip().endswith(rec["answer"]):
            problems.append(f"solution does not end with the answer in {rec['id']}")
        if not finite(rec["values"]):
            problems.append(f"non-finite value in {rec['id']}")
        fn = checks.get(meta["name"])
        if fn is not None:
            try:
                for computed, stored in fn(rec["values"]):
                    if not math.isclose(computed, stored, rel_tol=1e-6, abs_tol=1e-9):
                        mismatches += 1
                        if mismatches <= 3:
                            problems.append(f"check mismatch in {rec['id']}: recomputed {computed!r} vs stored {stored!r}")
            except Exception as exc:
                problems.append(f"check raised for {rec['id']}: {exc!r}")
        nums = numbers(rec["question"])
        for k, v in rec["values"].items():
            if inputs_only and k not in inputs_only:
                continue
            if isinstance(v, bool) or not isinstance(v, (int, float)) or v == 0:
                continue
            close = [n for n in nums if abs(n - v) / abs(v) < 0.01]
            exact = [n for n in nums if abs(n - v) / abs(v) < 1e-6]
            if close and not exact:
                display += 1
                if display <= 3:
                    problems.append(f"possible rounded display of '{k}'={v} (question shows {close[0]}) in {rec['id']} "
                                    "— ignore if this value is an output")
        if len(problems) > 12:
            break
    if meta["name"] not in checks and meta["name"] not in dedicated:
        problems.append("no independent check in tests/ (add one to a CHECKS dict)")
    return len(questions), problems


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("--module", action="append", default=[],
                    help="problem_generators submodule to import and check (repeatable)")
    ap.add_argument("--template", action="append", default=[], help="template name (repeatable)")
    ap.add_argument("--samples", type=int, default=300)
    args = ap.parse_args(argv)

    for m in args.module:
        importlib.import_module(f"problem_generators.{m}")
    selected = REGISTRY
    if args.module:
        mods = {f"problem_generators.{m}" for m in args.module}
        selected = [t for t in selected if t["fn"].__module__ in mods]
    if args.template:
        selected = [t for t in selected if t["name"] in args.template]
    names = [t["name"] for t in REGISTRY]
    dupes = sorted({n for n in names if names.count(n) > 1})
    checks, dedicated = load_checks()

    n_bad = 0
    if dupes:
        print(f"DUPLICATE template names: {dupes}")
        n_bad += 1
    for meta in selected:
        unique, problems = check_template(meta, checks, dedicated, args.samples, None)
        hard = [p for p in problems if not p.startswith("possible rounded display")]
        status = "OK " if not hard else "ERR"
        print(f"[{status}] {meta['name']:40s} unique questions: {unique}/{args.samples}")
        for p in problems:
            print(f"        - {p}")
        n_bad += bool(hard)
    print(f"\n{len(selected)} templates checked, {n_bad} with errors")
    return 1 if n_bad else 0


if __name__ == "__main__":
    sys.exit(main())
