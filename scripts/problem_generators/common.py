"""Shared helpers for the synthetic problem generators.

Every generator is a function ``gen(rng) -> dict`` registered with the
:func:`template` decorator. The returned dict is turned into a uniform record
by :func:`build`, so all generated problems share the same schema:

    id, field, subfield, topic, template, difficulty,
    question, solution, answer, values

``values`` holds the inputs and outputs (to 10 significant figures) so that the answers
can be re-checked programmatically (see tests/test_generators.py).
"""

import math
import re

# --- Physical constants (CODATA 2018 / SI 2019, rounded) -------------------
G = 6.674e-11          # gravitational constant, N m^2 / kg^2
C = 2.998e8            # speed of light, m/s
H = 6.626e-34          # Planck constant, J s
HBAR = 1.055e-34       # reduced Planck constant, J s
E_CHARGE = 1.602e-19   # elementary charge, C
M_E = 9.109e-31        # electron mass, kg
M_P = 1.673e-27        # proton mass, kg
K_B = 1.381e-23        # Boltzmann constant, J/K
N_A = 6.022e23         # Avogadro constant, 1/mol
R_GAS = 8.314          # gas constant, J/(mol K)
K_E = 8.988e9          # Coulomb constant, N m^2 / C^2
EPS0 = 8.854e-12       # vacuum permittivity, F/m
MU0 = 1.2566e-6        # vacuum permeability, T m / A
SIGMA_SB = 5.670e-8    # Stefan-Boltzmann constant, W/(m^2 K^4)
WIEN_B = 2.898e-3      # Wien displacement constant, m K
FARADAY = 96485.0      # Faraday constant, C/mol
G_EARTH = 9.81         # standard gravity used in problems, m/s^2
EV = 1.602e-19         # 1 eV in joules
HC_EV_NM = 1240.0      # hc in eV nm (handy approximation)
M_EARTH = 5.972e24
R_EARTH = 6.371e6
M_SUN = 1.989e30
L_SUN = 3.828e26
R_SUN = 6.957e8
T_SUN = 5772.0
AU = 1.496e11
LY = 9.461e15
PC = 3.086e16

REGISTRY = []


def template(name, field, subfield, topic, difficulty):
    """Register a generator function under a template name."""

    def deco(fn):
        REGISTRY.append(
            {
                "name": name,
                "field": field,
                "subfield": subfield,
                "topic": topic,
                "difficulty": difficulty,
                "fn": fn,
            }
        )
        return fn

    return deco


def fmt(x, sig=3):
    """Format a number with ``sig`` significant figures as LaTeX (no $)."""
    if isinstance(x, int) and abs(x) < 100000:
        return str(x)
    if x == 0:
        return "0"
    if not math.isfinite(x):
        raise ValueError(f"non-finite value {x!r}")
    exp = math.floor(math.log10(abs(x)))
    mant = round(x / 10 ** exp, sig - 1)
    if abs(mant) >= 10:
        exp += 1
        mant = round(x / 10 ** exp, sig - 1)
    if -3 <= exp < 5:
        decimals = max(sig - 1 - exp, 0)
        val = round(x, sig - 1 - exp)
        return f"{val:.{decimals}f}"
    return f"{mant:.{sig - 1}f} \\times 10^{{{exp}}}"


def sig(x, n=3):
    """Round to ``n`` significant figures, so stated data match what is displayed."""
    return float(f"{x:.{n}g}")


def q(x, unit="", sig=3):
    """Quantity: formatted number wrapped in $...$ followed by a unit."""
    s = f"${fmt(x, sig)}$"
    return f"{s} {unit}".rstrip() if unit else s


def nice(rng, lo, hi, step):
    """Random value from lo..hi (inclusive) in multiples of step."""
    n = int(round((hi - lo) / step))
    if all(isinstance(v, int) for v in (lo, hi, step)):
        return lo + step * rng.randint(0, n)
    val = lo + step * rng.randint(0, n)
    # avoid float noise like 0.30000000000000004
    digits = max(0, -int(math.floor(math.log10(step)))) if step < 1 else 0
    return round(val, digits + 2)


def pick(rng, items):
    return items[rng.randrange(len(items))]


_ARTICLE_RE = re.compile(r"(?<![\w\\])(An|an|A|a) (\$[^$]*\$|[A-Za-z][\w-]*)")
_NOT_A_NOUN = {"and", "or", "is", "are", "in", "of", "to", "has", "at", "as", "with", "allele"}


def _needs_an(token):
    """True/False if ``token`` starts with a vowel/consonant sound; None if unsure."""
    if token.startswith("$"):
        m = re.match(r"\$(\d+)", token)
        if not m:
            return None  # symbolic math: leave the author's choice alone
        digits = m.group(1)
        # "an 8...", "an 11", "an 18", "an 11 000", "an 18 000"
        return digits[0] == "8" or (len(digits) % 3 == 2 and digits[:2] in ("11", "18"))
    # initialisms and symbols are read letter by letter: "an X-linked", "an F₂ cross", "an NMR", "an SN2"
    if token[0].isupper() and (len(token) == 1 or not token[1].islower()):
        return token[0] in "AEFHILMNORSX"
    t = token.lower()
    if t.startswith(("uni", "use", "usu", "eu", "one", "ure")):
        return False
    if t.startswith(("hour", "honest", "honor")):
        return True
    return t[0] in "aeiou"


def fix_articles(text):
    """Choose "a" or "an" before words and numbers that sit outside math.

    A capital "A" is only treated as an article at the start of a sentence, so
    letters used as names ("allele A", "hemophilia A", "species A") are safe.
    """

    def repl(m):
        art, token = m.group(1), m.group(2)
        if text.count("$", 0, m.start()) % 2:  # article is inside math
            return m.group(0)
        if token.lower() in _NOT_A_NOUN:
            return m.group(0)
        if art[0] == "A" and text[:m.start()].rstrip(" (") and text[:m.start()].rstrip(" (")[-1] not in ".?!:\n":
            return m.group(0)
        an = _needs_an(token)
        if an is None:
            return m.group(0)
        new = "an" if an else "a"
        if art[0] == "A":
            new = new.capitalize()
        return f"{new} {token}"

    return _ARTICLE_RE.sub(repl, text)


def build(meta, data, index):
    """Assemble the final record from template metadata and generator output."""
    given = data.get("given") or []
    steps = data["steps"]
    parts = []
    if given:
        parts.append("**Given:** " + "; ".join(given))
    parts.append(
        "**Solution:**\n" + "\n".join(f"{i}. {s}" for i, s in enumerate(steps, 1))
    )
    parts.append(f"**Answer:** {data['answer']}")
    values = {}
    for k, v in data.get("values", {}).items():
        if isinstance(v, float):
            if not math.isfinite(v):
                raise ValueError(f"{meta['name']}: non-finite value for {k}")
            values[k] = float(f"{v:.10g}")
        else:
            values[k] = v
    return {
        "id": f"{meta['name']}-{index:05d}",
        "field": meta["field"],
        "subfield": meta["subfield"],
        "topic": meta["topic"],
        "template": meta["name"],
        "difficulty": data.get("difficulty", meta["difficulty"]),
        "question": fix_articles(data["question"]),
        "solution": fix_articles("\n\n".join(parts)),
        "answer": fix_articles(data["answer"]),
        "values": values,
    }
