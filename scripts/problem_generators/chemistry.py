"""Chemistry problem templates (general, physical and analytical chemistry)."""

import math
import re

from .common import FARADAY, N_A, R_GAS, fmt, nice, pick, q, sig, template

CHEM = "Chemistry"
GEN = "General Chemistry"
PCHEM = "Physical Chemistry"
R_LATM = 0.08206  # L atm / (mol K)
KW = 1.0e-14

# ---------------------------------------------------------------------------
# Formula utilities
# ---------------------------------------------------------------------------

ATOMIC_MASS = {
    "H": 1.008, "He": 4.003, "Li": 6.94, "Be": 9.012, "B": 10.81, "C": 12.011,
    "N": 14.007, "O": 15.999, "F": 18.998, "Ne": 20.180, "Na": 22.990,
    "Mg": 24.305, "Al": 26.982, "Si": 28.085, "P": 30.974, "S": 32.06,
    "Cl": 35.45, "Ar": 39.948, "K": 39.098, "Ca": 40.078, "Ti": 47.867,
    "Cr": 51.996, "Mn": 54.938, "Fe": 55.845, "Co": 58.933, "Ni": 58.693,
    "Cu": 63.546, "Zn": 65.38, "Br": 79.904, "Sr": 87.62, "Ag": 107.868,
    "Cd": 112.41, "Sn": 118.71, "I": 126.904, "Ba": 137.327, "Au": 196.967,
    "Hg": 200.59, "Pb": 207.2,
}

_TOKEN = re.compile(r"[A-Z][a-z]?|\(|\)|\d+")
_SUB = str.maketrans("0123456789", "₀₁₂₃₄₅₆₇₈₉")


def parse_formula(formula):
    """Return ``{element: count}`` for formulas like ``Ca(OH)2`` or ``CuSO4·5H2O``."""
    total = {}
    for part in formula.split("·"):
        mult = 1
        m = re.match(r"(\d+)(.*)", part)
        if m:
            mult, part = int(m.group(1)), m.group(2)
        tokens = _TOKEN.findall(part)
        if "".join(tokens) != part:
            raise ValueError(f"cannot parse formula {formula!r}")
        stack = [{}]
        i = 0
        while i < len(tokens):
            tok = tokens[i]
            has_count = i + 1 < len(tokens) and tokens[i + 1].isdigit()
            n = int(tokens[i + 1]) if has_count else 1
            if tok == "(":
                stack.append({})
                i += 1
                continue
            if tok.isdigit():
                raise ValueError(f"unexpected number in {formula!r}")
            if tok == ")":
                for el, c in stack.pop().items():
                    stack[-1][el] = stack[-1].get(el, 0) + c * n
            else:
                stack[-1][tok] = stack[-1].get(tok, 0) + n
            i += 2 if has_count else 1
        if len(stack) != 1:
            raise ValueError(f"unbalanced parentheses in {formula!r}")
        for el, c in stack[0].items():
            total[el] = total.get(el, 0) + c * mult
    return total


def molar_mass(formula):
    return sum(ATOMIC_MASS[el] * n for el, n in parse_formula(formula).items())


def pretty(formula):
    """Unicode subscripts: ``Ca(OH)2`` -> ``Ca(OH)₂``; hydrate coefficients stay normal."""
    out = []
    for part in formula.split("·"):
        lead = ""
        m = re.match(r"(\d+)(.*)", part)
        if m:
            lead, part = m.group(1), m.group(2)
        part = re.sub(r"(?<=[A-Za-z)])(\d+)", lambda mm: mm.group(1).translate(_SUB), part)
        out.append(lead + part)
    return "·".join(out)


def mm_line(formula):
    """Molar-mass working, e.g. ``M(H₂O) = 2(1.008) + 15.999 = 18.02 g/mol``."""
    terms = []
    for el, n in parse_formula(formula).items():
        a = ATOMIC_MASS[el]
        terms.append(f"{n}({a})" if n > 1 else f"{a}")
    return f"$M = {' + '.join(terms)} = {molar_mass(formula):.2f}$ g/mol"


def equation(reactants, products, arrow="→"):
    def side(items):
        return " + ".join((f"{c} " if c != 1 else "") + pretty(f) for c, f in items)

    return f"{side(reactants)} {arrow} {side(products)}"


def ph_str(x):
    return f"{x:.2f}"


COMPOUNDS = [
    ("H2O", "water", "molecules"), ("CO2", "carbon dioxide", "molecules"),
    ("NaCl", "sodium chloride", "formula units"), ("C6H12O6", "glucose", "molecules"),
    ("H2SO4", "sulfuric acid", "molecules"), ("CaCO3", "calcium carbonate", "formula units"),
    ("NH3", "ammonia", "molecules"), ("C2H5OH", "ethanol", "molecules"),
    ("NaHCO3", "sodium bicarbonate", "formula units"), ("KMnO4", "potassium permanganate", "formula units"),
    ("Ca(OH)2", "calcium hydroxide", "formula units"), ("Al2(SO4)3", "aluminum sulfate", "formula units"),
    ("Mg3(PO4)2", "magnesium phosphate", "formula units"), ("C12H22O11", "sucrose", "molecules"),
    ("Fe2O3", "iron(III) oxide", "formula units"), ("CuSO4·5H2O", "copper(II) sulfate pentahydrate", "formula units"),
    ("(NH4)2SO4", "ammonium sulfate", "formula units"), ("C8H18", "octane", "molecules"),
    ("C9H8O4", "aspirin", "molecules"), ("C8H10N4O2", "caffeine", "molecules"),
    ("HNO3", "nitric acid", "molecules"), ("K2Cr2O7", "potassium dichromate", "formula units"),
    ("Ba(NO3)2", "barium nitrate", "formula units"), ("CH3COOH", "acetic acid", "molecules"),
]

# ---------------------------------------------------------------------------
# Moles, composition, formulas
# ---------------------------------------------------------------------------


@template("moles_and_particles", CHEM, GEN, "The mole", "easy")
def moles_and_particles(rng):
    f, name, unit = pick(rng, COMPOUNDS)
    m = nice(rng, 1.0, 250.0, 0.5)
    M = molar_mass(f)
    n = m / M
    counts = parse_formula(f)
    el = pick(rng, sorted(counts))
    particles = n * N_A
    atoms = particles * counts[el]
    question = (
        f"How many moles of {name} ({pretty(f)}) are in {q(m, 'g', 4)}? How many {unit} is that, and how many "
        f"{el} atoms does the sample contain?"
    )
    steps = [
        f"Molar mass of {pretty(f)}: {mm_line(f)}.",
        f"Moles: $n = m/M = {fmt(m, 4)}/{M:.2f} = {fmt(n, 4)}$ mol.",
        f"{unit.capitalize()}: $N = nN_A = ({fmt(n, 4)})(6.022\\times10^{{23}}) = {fmt(particles, 4)}$.",
        f"Each {unit[:-1]} contains {counts[el]} {el} atom{'s' if counts[el] > 1 else ''}, so the sample holds "
        f"${counts[el]} \\times {fmt(particles, 4)} = {fmt(atoms, 4)}$ {el} atoms.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$n = {fmt(n, 4)}$ mol; ${fmt(particles, 4)}$ {unit}; ${fmt(atoms, 4)}$ {el} atoms",
            "values": {"formula": f, "mass": m, "M": M, "n": n, "particles": particles, "element": el,
                       "atoms": atoms}}


@template("percent_composition", CHEM, GEN, "Percent composition", "easy")
def percent_composition(rng):
    f, name, _ = pick(rng, COMPOUNDS)
    M = molar_mass(f)
    counts = parse_formula(f)
    steps = [f"Molar mass of {pretty(f)}: {mm_line(f)}."]
    values = {"formula": f, "M": M}
    parts = []
    for el, n in counts.items():
        pct = 100 * n * ATOMIC_MASS[el] / M
        steps.append(
            f"{el}: $\\frac{{{n} \\times {ATOMIC_MASS[el]}}}{{{M:.2f}}} \\times 100\\% = {pct:.2f}\\%$"
        )
        parts.append(f"{el} {pct:.2f}%")
        values[f"pct_{el}"] = pct
    steps.append("Check: the percentages add up to 100% (within rounding).")
    question = f"Calculate the percent composition by mass of {name} ({pretty(f)})."
    return {"question": question, "steps": steps, "answer": ", ".join(parts), "values": values}


EMPIRICAL_CASES = [
    ("C6H12O6", "glucose"), ("C6H6", "benzene"), ("C2H4O2", "acetic acid"), ("N2H4", "hydrazine"),
    ("H2O2", "hydrogen peroxide"), ("C4H10", "butane"), ("Fe2O3", "an iron oxide"),
    ("P4O10", "a phosphorus oxide"), ("C8H8", "styrene"), ("C2H2", "acetylene"), ("N2O4", "a nitrogen oxide"),
    ("C3H6O3", "lactic acid"), ("C10H8", "naphthalene"), ("C6H8O7", "citric acid"),
    ("C8H10N4O2", "caffeine"), ("C4H8O2", "ethyl acetate"), ("C2H6O2", "ethylene glycol"),
    ("C5H10O5", "ribose"), ("B2H6", "diborane"), ("C6H4Cl2", "dichlorobenzene"),
]


def _formula_from_counts(counts):
    return "".join(el + (str(n) if n > 1 else "") for el, n in counts.items())


@template("empirical_and_molecular_formula", CHEM, GEN, "Empirical formulas", "medium")
def empirical_and_molecular_formula(rng):
    f, name = pick(rng, EMPIRICAL_CASES)
    counts = parse_formula(f)
    M = molar_mass(f)
    pcts = {el: round(100 * n * ATOMIC_MASS[el] / M, 2) for el, n in counts.items()}
    moles = {el: p / ATOMIC_MASS[el] for el, p in pcts.items()}
    small = min(moles.values())
    ratios = {el: v / small for el, v in moles.items()}
    k = next(k for k in range(1, 9) if all(abs(r * k - round(r * k)) < 0.08 for r in ratios.values()))
    emp = {el: round(r * k) for el, r in ratios.items()}
    g = 0
    for n in counts.values():
        g = math.gcd(g, n)
    if emp != {el: n // g for el, n in counts.items()}:
        raise ValueError(f"empirical formula mismatch for {f}")
    emp_f = _formula_from_counts(emp)
    M_emp = molar_mass(emp_f)
    mult = round(M / M_emp)
    composition = ", ".join(f"{p:.2f}% {el}" for el, p in pcts.items())
    question = (
        f"A sample of {name} is found to contain {composition} by mass. Its molar mass is about "
        f"{q(round(M, 1), 'g/mol', 4)}. Determine its empirical and molecular formulas."
    )
    steps = ["Assume a 100 g sample, so each percentage becomes a mass in grams."]
    steps.append("Convert to moles: " + "; ".join(
        f"{el}: ${pcts[el]:.2f}/{ATOMIC_MASS[el]} = {moles[el]:.3f}$ mol" for el in pcts) + ".")
    steps.append(f"Divide by the smallest ({small:.3f} mol): " + ", ".join(
        f"{el} {ratios[el]:.2f}" for el in pcts) + ".")
    if k > 1:
        steps.append(f"The ratios are not all whole numbers; multiply by {k}: " + ", ".join(
            f"{el} {ratios[el] * k:.2f} ≈ {emp[el]}" for el in pcts) + ".")
    else:
        steps.append("Round to whole numbers: " + ", ".join(f"{el} {emp[el]}" for el in pcts) + ".")
    steps.append(f"Empirical formula: **{pretty(emp_f)}**, with formula mass ${M_emp:.2f}$ g/mol.")
    steps.append(f"Multiplier: ${M:.1f}/{M_emp:.2f} = {M / M_emp:.2f} \\approx {mult}$, so the molecular formula is "
                 f"**{pretty(f)}**.")
    return {"question": question, "steps": steps,
            "answer": f"empirical formula {pretty(emp_f)}; molecular formula {pretty(f)}",
            "values": {"formula": f, "empirical": emp_f, "multiplier": mult, "M": M}}


@template("hydrate_formula", CHEM, GEN, "Hydrates", "easy")
def hydrate_formula(rng):
    anh, x, name = pick(rng, [
        ("CuSO4", 5, "copper(II) sulfate"), ("MgSO4", 7, "magnesium sulfate"), ("BaCl2", 2, "barium chloride"),
        ("Na2CO3", 10, "sodium carbonate"), ("CoCl2", 6, "cobalt(II) chloride"), ("CaSO4", 2, "calcium sulfate"),
        ("Na2SO4", 10, "sodium sulfate"), ("FeSO4", 7, "iron(II) sulfate"), ("ZnSO4", 7, "zinc sulfate"),
    ])
    m_h = nice(rng, 1.00, 9.00, 0.01)
    M_anh = molar_mass(anh)
    M_w = molar_mass("H2O")
    m_anh = round(m_h * M_anh / (M_anh + x * M_w), 3)
    m_w = m_h - m_anh
    n_anh = m_anh / M_anh
    n_w = m_w / M_w
    ratio = n_w / n_anh
    question = (
        f"A {q(m_h, 'g', 3)} sample of hydrated {name}, {pretty(anh)}·xH₂O, is heated until all the water is driven "
        f"off. The anhydrous residue has a mass of ${m_anh:.3f}$ g. Find x."
    )
    steps = [
        f"Mass of water lost: ${m_h:.2f} - {m_anh:.3f} = {m_w:.3f}$ g.",
        f"Moles of water: ${m_w:.3f}/{M_w:.2f} = {n_w:.4f}$ mol.",
        f"Moles of anhydrous {pretty(anh)} ($M = {M_anh:.2f}$ g/mol): ${m_anh:.3f}/{M_anh:.2f} = {n_anh:.4f}$ mol.",
        f"Ratio: $x = {n_w:.4f}/{n_anh:.4f} = {ratio:.2f} \\approx {x}$.",
    ]
    return {"question": question, "steps": steps, "answer": f"$x = {x}$, i.e. {pretty(anh)}·{x}H₂O",
            "values": {"m_hydrate": m_h, "m_anhydrous": m_anh, "x": x}}


ELEMENTS = [
    "H", "He", "Li", "Be", "B", "C", "N", "O", "F", "Ne", "Na", "Mg", "Al", "Si", "P", "S", "Cl", "Ar",
    "K", "Ca", "Sc", "Ti", "V", "Cr", "Mn", "Fe", "Co", "Ni", "Cu", "Zn", "Ga", "Ge", "As", "Se", "Br", "Kr",
]
ELEMENT_NAMES = [
    "hydrogen", "helium", "lithium", "beryllium", "boron", "carbon", "nitrogen", "oxygen", "fluorine", "neon",
    "sodium", "magnesium", "aluminum", "silicon", "phosphorus", "sulfur", "chlorine", "argon", "potassium",
    "calcium", "scandium", "titanium", "vanadium", "chromium", "manganese", "iron", "cobalt", "nickel",
    "copper", "zinc", "gallium", "germanium", "arsenic", "selenium", "bromine", "krypton",
]
AUFBAU = [("1s", 2), ("2s", 2), ("2p", 6), ("3s", 2), ("3p", 6), ("4s", 2), ("3d", 10), ("4p", 6)]
_SUP = str.maketrans("0123456789", "⁰¹²³⁴⁵⁶⁷⁸⁹")


def electron_configuration(Z):
    config = []
    left = Z
    for sub, cap in AUFBAU:
        if left <= 0:
            break
        e = min(cap, left)
        config.append([sub, e])
        left -= e
    exceptions = {24: (4, 5), 29: (1, 10)}  # Cr: 4s1 3d5, Cu: 4s1 3d10
    if Z in exceptions:
        d = dict((s, i) for i, (s, _) in enumerate(config))
        config[d["4s"]][1] = 1
        config[d["3d"]][1] = exceptions[Z][1]
    return config


def unpaired(config):
    total = 0
    for sub, e in config:
        orbitals = {"s": 1, "p": 3, "d": 5}[sub[1]]
        total += e if e <= orbitals else 2 * orbitals - e
    return total


@template("electron_configuration", CHEM, GEN, "Electron configuration", "easy")
def electron_configuration_problem(rng):
    Z = rng.randint(3, 36)
    sym, name = ELEMENTS[Z - 1], ELEMENT_NAMES[Z - 1]
    config = electron_configuration(Z)
    # write in order of n for the final answer (3d before 4s), as most textbooks do
    order = sorted(config, key=lambda c: (int(c[0][0]), "spdf".index(c[0][1])))
    full = " ".join(f"{s}{str(e).translate(_SUP)}" for s, e in order)
    noble = {2: "He", 10: "Ne", 18: "Ar"}
    core_Z = max(z for z in (0, 2, 10, 18) if z < Z)
    core = electron_configuration(core_Z) if core_Z else []
    core_subs = {s for s, _ in core}
    short_parts = [f"{s}{str(e).translate(_SUP)}" for s, e in order if s not in core_subs]
    short = (f"[{noble[core_Z]}] " if core_Z else "") + " ".join(short_parts)
    n_unp = unpaired(config)
    last = config[-1][0]
    block = last[1] if Z not in (24, 29) else "d"
    steps = [
        f"{name.capitalize()} has $Z = {Z}$, so a neutral atom has {Z} electrons.",
        "Fill subshells in Aufbau order (1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p), at most 2 electrons per orbital.",
    ]
    if Z in (24, 29):
        steps.append(
            f"{name.capitalize()} is an exception: one 4s electron moves into 3d to give a "
            f"{'half-filled' if Z == 24 else 'completely filled'} 3d subshell, which is lower in energy."
        )
    steps += [
        f"Full configuration: {full}.",
        f"Noble-gas shorthand: {short}.",
        f"Hund's rule (fill degenerate orbitals singly first) gives {n_unp} unpaired electron"
        f"{'s' if n_unp != 1 else ''}, so the atom is {'paramagnetic' if n_unp else 'diamagnetic'}.",
        f"The highest-energy electrons occupy a {block} subshell: {sym} is a {block}-block element.",
    ]
    question = (
        f"Write the ground-state electron configuration of {name} ({sym}), both in full and in noble-gas shorthand. "
        "How many unpaired electrons does the atom have, and to which block of the periodic table does it belong?"
    )
    return {"question": question, "steps": steps,
            "answer": f"{full} = {short}; {n_unp} unpaired electron{'s' if n_unp != 1 else ''}; {block}-block",
            "values": {"Z": Z, "symbol": sym, "unpaired": n_unp, "block": block}}


# ---------------------------------------------------------------------------
# Solutions and stoichiometry
# ---------------------------------------------------------------------------


@template("solution_preparation", CHEM, GEN, "Molarity", "easy")
def solution_preparation(rng):
    f, name = pick(rng, [
        ("NaCl", "sodium chloride"), ("KCl", "potassium chloride"), ("NaOH", "sodium hydroxide"),
        ("CuSO4·5H2O", "copper(II) sulfate pentahydrate"), ("C6H12O6", "glucose"),
        ("KMnO4", "potassium permanganate"), ("AgNO3", "silver nitrate"), ("Na2CO3", "sodium carbonate"),
        ("KNO3", "potassium nitrate"), ("NH4Cl", "ammonium chloride"), ("K2Cr2O7", "potassium dichromate"),
    ])
    V = pick(rng, [50, 100, 250, 500, 1000, 2000])
    c = nice(rng, 0.05, 2.00, 0.01)
    M = molar_mass(f)
    n = c * V / 1000
    m = n * M
    question = (
        f"How many grams of {name} ({pretty(f)}) are needed to prepare {q(V, 'mL')} of a {q(c, 'M')} solution? "
        "Briefly describe how the solution is made."
    )
    steps = [
        f"Moles needed: $n = cV = ({fmt(c)})({fmt(V / 1000, 3)}\\text{{ L}}) = {fmt(n)}$ mol.",
        f"Molar mass: {mm_line(f)}.",
        f"Mass: $m = nM = ({fmt(n)})({M:.2f}) = {fmt(m)}$ g.",
        f"Weigh the solid, dissolve it in less than {V} mL of water in a {V} mL volumetric flask, then add water to the mark and mix.",
    ]
    return {"question": question, "steps": steps, "answer": f"${fmt(m)}$ g of {pretty(f)}",
            "values": {"formula": f, "V_mL": V, "c": c, "M": M, "mass": m}}


@template("dilution", CHEM, GEN, "Dilution", "easy")
def dilution(rng):
    name, c1 = pick(rng, [("hydrochloric acid", 12.0), ("sulfuric acid", 18.0), ("nitric acid", 15.8),
                          ("sodium hydroxide", 6.00), ("sodium chloride", 5.00), ("acetic acid", 17.4),
                          ("ammonia", 14.8)])
    c2 = nice(rng, 0.05, 3.00, 0.05)
    V2 = pick(rng, [100, 250, 500, 1000, 2000])
    V1 = c2 * V2 / c1
    acid = "acid" in name
    question = (
        f"What volume of {q(c1, 'M')} {name} is needed to prepare {q(V2, 'mL')} of {q(c2, 'M')} solution?"
    )
    steps = [
        "The moles of solute do not change on dilution: $c_1V_1 = c_2V_2$.",
        f"$V_1 = \\frac{{c_2V_2}}{{c_1}} = \\frac{{({fmt(c2)})({V2})}}{{{fmt(c1)}}} = {fmt(V1)}$ mL.",
        f"Dilute {fmt(V1)} mL of stock to a total volume of {V2} mL (about {fmt(V2 - V1)} mL of water).",
    ]
    if acid:
        steps.append("Safety: always add concentrated acid to water, never water to acid, because dilution releases heat.")
    return {"question": question, "steps": steps, "answer": f"$V_1 = {fmt(V1)}$ mL",
            "values": {"c1": c1, "c2": c2, "V2": V2, "V1": V1}}


REACTIONS_2 = [
    # reactants, products, product index of interest
    ([(2, "H2"), (1, "O2")], [(2, "H2O")], 0),
    ([(1, "N2"), (3, "H2")], [(2, "NH3")], 0),
    ([(4, "Fe"), (3, "O2")], [(2, "Fe2O3")], 0),
    ([(2, "Al"), (3, "Cl2")], [(2, "AlCl3")], 0),
    ([(1, "CH4"), (2, "O2")], [(1, "CO2"), (2, "H2O")], 0),
    ([(2, "Na"), (1, "Cl2")], [(2, "NaCl")], 0),
    ([(1, "C3H8"), (5, "O2")], [(3, "CO2"), (4, "H2O")], 1),
    ([(1, "Zn"), (2, "HCl")], [(1, "ZnCl2"), (1, "H2")], 0),
    ([(2, "Al"), (1, "Fe2O3")], [(1, "Al2O3"), (2, "Fe")], 1),
    ([(1, "P4"), (6, "Cl2")], [(4, "PCl3")], 0),
    ([(2, "NH3"), (1, "CO2")], [(1, "CO(NH2)2"), (1, "H2O")], 0),
    ([(1, "SiO2"), (3, "C")], [(1, "SiC"), (2, "CO")], 0),
    ([(1, "CaO"), (1, "H2O")], [(1, "Ca(OH)2")], 0),
    ([(2, "C2H6"), (7, "O2")], [(4, "CO2"), (6, "H2O")], 0),
]


@template("limiting_reactant", CHEM, GEN, "Stoichiometry", "medium")
def limiting_reactant(rng):
    reacts, prods, pi = pick(rng, REACTIONS_2)
    (ca, fa), (cb, fb) = reacts
    cp, fp = prods[pi]
    ma = nice(rng, 2.0, 100.0, 0.5)
    mb = nice(rng, 2.0, 100.0, 0.5)
    Ma, Mb, Mp = molar_mass(fa), molar_mass(fb), molar_mass(fp)
    na, nb = ma / Ma, mb / Mb
    if abs(na / ca - nb / cb) / max(na / ca, nb / cb) < 0.03:
        mb = round(mb * 1.5, 1)
        nb = mb / Mb
    if na / ca < nb / cb:
        lim, ex, nlim, nex, clim, cex, Mex = fa, fb, na, nb, ca, cb, Mb
    else:
        lim, ex, nlim, nex, clim, cex, Mex = fb, fa, nb, na, cb, ca, Ma
    n_prod = nlim * cp / clim
    m_prod = n_prod * Mp
    n_left = nex - nlim * cex / clim
    m_left = n_left * Mex
    yield_frac = nice(rng, 0.60, 0.97, 0.01)
    actual = sig(m_prod * yield_frac, 3)
    pct = 100 * actual / m_prod
    eq = equation(reacts, prods)
    question = (
        f"For the reaction {eq}, {q(ma, 'g')} of {pretty(fa)} is mixed with {q(mb, 'g')} of {pretty(fb)}. "
        f"(a) Which reactant is limiting? (b) What is the theoretical yield of {pretty(fp)}? "
        f"(c) How much of the excess reactant remains? (d) If {q(actual, 'g')} of {pretty(fp)} is actually obtained, "
        "what is the percent yield?"
    )
    steps = [
        f"Molar masses: {pretty(fa)} {Ma:.2f}, {pretty(fb)} {Mb:.2f}, {pretty(fp)} {Mp:.2f} g/mol.",
        f"Moles: $n(\\text{{{pretty(fa)}}}) = {fmt(ma)}/{Ma:.2f} = {fmt(na, 4)}$ mol; $n(\\text{{{pretty(fb)}}}) = {fmt(mb)}/{Mb:.2f} = {fmt(nb, 4)}$ mol.",
        f"Divide by the coefficients: {pretty(fa)} ${fmt(na, 4)}/{ca} = {fmt(na / ca, 4)}$; {pretty(fb)} ${fmt(nb, 4)}/{cb} = {fmt(nb / cb, 4)}$. "
        f"The smaller value identifies the limiting reactant: **{pretty(lim)}**.",
        f"Theoretical yield: $n(\\text{{{pretty(fp)}}}) = {fmt(nlim, 4)} \\times \\frac{{{cp}}}{{{clim}}} = {fmt(n_prod, 4)}$ mol, "
        f"i.e. ${fmt(n_prod, 4)} \\times {Mp:.2f} = {fmt(m_prod)}$ g.",
        f"Excess {pretty(ex)} consumed: ${fmt(nlim, 4)} \\times \\frac{{{cex}}}{{{clim}}} = {fmt(nlim * cex / clim, 4)}$ mol; "
        f"remaining ${fmt(n_left, 3)}$ mol $= {fmt(m_left)}$ g.",
        f"Percent yield: $\\frac{{{fmt(actual, 4)}}}{{{fmt(m_prod, 4)}}} \\times 100\\% = {pct:.1f}\\%$.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"(a) {pretty(lim)}; (b) ${fmt(m_prod)}$ g {pretty(fp)}; (c) ${fmt(m_left)}$ g {pretty(ex)} left; "
                      f"(d) {pct:.1f}%",
            "values": {"m_a": ma, "m_b": mb, "limiting": lim, "theoretical_g": m_prod, "excess_left_g": m_left,
                       "actual_g": actual, "percent_yield": pct}}


@template("gas_stoichiometry", CHEM, GEN, "Gas stoichiometry", "medium")
def gas_stoichiometry(rng):
    reacts, prods, gas_i, context = pick(rng, [
        ([(1, "CaCO3")], [(1, "CaO"), (1, "CO2")], 1, "Limestone is decomposed by strong heating"),
        ([(2, "KClO3")], [(2, "KCl"), (3, "O2")], 1, "Potassium chlorate is decomposed with a MnO₂ catalyst"),
        ([(2, "NaN3")], [(2, "Na"), (3, "N2")], 1, "An airbag inflates when sodium azide decomposes"),
        ([(1, "Zn"), (2, "HCl")], [(1, "ZnCl2"), (1, "H2")], 1, "Zinc reacts with excess hydrochloric acid"),
        ([(2, "H2O2")], [(2, "H2O"), (1, "O2")], 1, "Hydrogen peroxide decomposes"),
        ([(1, "Mg"), (2, "HCl")], [(1, "MgCl2"), (1, "H2")], 1, "Magnesium reacts with excess hydrochloric acid"),
        ([(1, "NH4NO3")], [(1, "N2O"), (2, "H2O")], 0, "Ammonium nitrate is gently heated"),
        ([(1, "NaHCO3"), (1, "HCl")], [(1, "NaCl"), (1, "H2O"), (1, "CO2")], 2, "Baking soda reacts with excess acid"),
    ])
    cr, fr = reacts[0]
    cg, fg = prods[gas_i]
    m = nice(rng, 0.5, 80.0, 0.5)
    TC = nice(rng, 0, 40, 1)
    P = nice(rng, 0.85, 1.10, 0.01)
    Mr = molar_mass(fr)
    nr = m / Mr
    ng = nr * cg / cr
    T = TC + 273.15
    V = ng * R_LATM * T / P
    question = (
        f"{context}: {equation(reacts, prods)}. What volume of {pretty(fg)} gas is produced from {q(m, 'g')} of "
        f"{pretty(fr)} at {q(TC, '°C')} and {q(P, 'atm')}?"
    )
    steps = [
        f"Moles of {pretty(fr)} ($M = {Mr:.2f}$ g/mol): $n = {fmt(m)}/{Mr:.2f} = {fmt(nr, 4)}$ mol.",
        f"Mole ratio from the balanced equation: ${cg}$ {pretty(fg)} : ${cr}$ {pretty(fr)}, so "
        f"$n(\\text{{{pretty(fg)}}}) = {fmt(nr, 4)} \\times \\frac{{{cg}}}{{{cr}}} = {fmt(ng, 4)}$ mol.",
        f"Ideal gas law with $T = {fmt(T, 5)}$ K: $V = \\frac{{nRT}}{{P}} = \\frac{{({fmt(ng, 4)})(0.08206)({fmt(T, 5)})}}{{{fmt(P)}}} = {fmt(V)}$ L.",
    ]
    return {"question": question, "steps": steps, "answer": f"$V = {fmt(V)}$ L of {pretty(fg)}",
            "values": {"mass": m, "M": Mr, "n_gas": ng, "T_C": TC, "P_atm": P, "V_L": V}}


@template("titration_strong", CHEM, GEN, "Acid-base titration", "easy")
def titration_strong(rng):
    acid, a_h = pick(rng, [("HCl", 1), ("HNO3", 1), ("H2SO4", 2)])
    base, b_oh = pick(rng, [("NaOH", 1), ("KOH", 1), ("Ba(OH)2", 2)])
    Va = pick(rng, [10.0, 20.0, 25.0, 50.0])
    Cb = nice(rng, 0.050, 0.500, 0.005)
    Vb_r = nice(rng, 8.00, 45.00, 0.05)
    Ca_found = Cb * Vb_r * b_oh / (Va * a_h)
    acid_ion = "two H⁺ ions" if a_h == 2 else "one H⁺ ion"
    base_ion = "two OH⁻ ions" if b_oh == 2 else "one OH⁻ ion"
    question = (
        f"A {q(Va, 'mL', 3)} sample of {pretty(acid)} solution of unknown concentration is titrated with "
        f"{q(Cb, 'M')} {pretty(base)}. The equivalence point is reached after {q(Vb_r, 'mL', 4)} of base. "
        f"What is the concentration of the acid?"
    )
    steps = [
        f"Each {pretty(acid)} supplies {acid_ion}; each {pretty(base)} supplies {base_ion}.",
        f"Moles of OH⁻ added: ${b_oh} \\times ({fmt(Cb)})({fmt(Vb_r / 1000, 4)}\\text{{ L}}) = {fmt(b_oh * Cb * Vb_r / 1000, 4)}$ mol.",
        f"At equivalence, moles H⁺ = moles OH⁻, so $n(\\text{{{pretty(acid)}}}) = {fmt(b_oh * Cb * Vb_r / 1000, 4)}/{a_h} = "
        f"{fmt(b_oh * Cb * Vb_r / 1000 / a_h, 4)}$ mol.",
        f"Concentration: $c = n/V = {fmt(b_oh * Cb * Vb_r / 1000 / a_h, 4)}/{fmt(Va / 1000, 3)} = {fmt(Ca_found, 4)}$ M.",
    ]
    return {"question": question, "steps": steps, "answer": f"$c(\\text{{{pretty(acid)}}}) = {fmt(Ca_found, 4)}$ M",
            "values": {"Va_mL": Va, "Cb": Cb, "Vb_mL": Vb_r, "acid_H": a_h, "base_OH": b_oh, "Ca": Ca_found}}


# ---------------------------------------------------------------------------
# Gases and colligative properties
# ---------------------------------------------------------------------------

GASES = [("N2", "nitrogen"), ("O2", "oxygen"), ("CO2", "carbon dioxide"), ("CH4", "methane"), ("Ar", "argon"),
         ("SO2", "sulfur dioxide"), ("C3H8", "propane"), ("Cl2", "chlorine"), ("NH3", "ammonia"),
         ("He", "helium"), ("Ne", "neon"), ("C4H10", "butane"), ("H2S", "hydrogen sulfide")]


@template("gas_molar_mass_from_density", CHEM, GEN, "Gas laws", "medium")
def gas_molar_mass_from_density(rng):
    f, name = pick(rng, GASES)
    M = molar_mass(f)
    TC = nice(rng, 0, 100, 1)
    P = nice(rng, 0.500, 2.000, 0.010)
    T = TC + 273.15
    d = sig(P * M / (R_LATM * T), 4)
    M_calc = d * R_LATM * T / P
    question = (
        f"An unknown gas has a density of {q(d, 'g/L', 4)} at {q(TC, '°C')} and {q(P, 'atm')}. "
        "Find its molar mass and suggest which common gas it could be."
    )
    steps = [
        "Combine $PV = nRT$ with $n = m/M$ and $d = m/V$: $M = \\frac{dRT}{P}$.",
        f"$M = \\frac{{({fmt(d, 4)})(0.08206)({fmt(T, 5)})}}{{{fmt(P)}}} = {fmt(M_calc, 4)}$ g/mol.",
        f"This matches {name} ({pretty(f)}, $M = {M:.2f}$ g/mol).",
    ]
    return {"question": question, "steps": steps, "answer": f"$M \\approx {fmt(M_calc, 4)}$ g/mol — {name} ({pretty(f)})",
            "values": {"d": d, "T_C": TC, "P_atm": P, "M": M_calc, "formula": f}}


@template("graham_effusion", CHEM, GEN, "Kinetic molecular theory", "easy")
def graham_effusion(rng):
    (f1, n1), (f2, n2) = rng.sample(GASES, 2)
    M1, M2 = molar_mass(f1), molar_mass(f2)
    ratio = math.sqrt(M2 / M1)
    t2 = nice(rng, 20, 300, 1)
    t1 = t2 / ratio
    question = (
        f"Under identical conditions, how much faster does {n1} ({pretty(f1)}) effuse than {n2} "
        f"({pretty(f2)})? If a sample of {pretty(f2)} takes {q(t2, 's')} to effuse through a pinhole, how long does "
        f"the same amount of {pretty(f1)} take?"
    )
    steps = [
        "Graham's law: $\\frac{r_1}{r_2} = \\sqrt{\\frac{M_2}{M_1}}$ (lighter molecules move faster on average).",
        f"$\\frac{{r(\\text{{{pretty(f1)}}})}}{{r(\\text{{{pretty(f2)}}})}} = \\sqrt{{\\frac{{{M2:.2f}}}{{{M1:.2f}}}}} = {fmt(ratio, 4)}$.",
        f"Time is inversely proportional to rate: $t_1 = t_2/{fmt(ratio, 4)} = {fmt(t1)}$ s.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"rate ratio ${fmt(ratio, 4)}$; $t = {fmt(t1)}$ s",
            "values": {"M1": M1, "M2": M2, "rate_ratio": ratio, "t2": t2, "t1": t1}}


@template("colligative_bp_fp", CHEM, GEN, "Colligative properties", "medium")
def colligative_bp_fp(rng):
    solvent = pick(rng, ["water", "water", "water", "benzene"])
    if solvent == "water":
        Kb, Kf, Tb, Tf = 0.512, 1.86, 100.00, 0.00
        f, name, i = pick(rng, [
            ("C6H12O6", "glucose", 1), ("C12H22O11", "sucrose", 1), ("CO(NH2)2", "urea", 1),
            ("C2H6O2", "ethylene glycol", 1), ("NaCl", "sodium chloride", 2), ("CaCl2", "calcium chloride", 3),
            ("KBr", "potassium bromide", 2), ("MgSO4", "magnesium sulfate", 2), ("C3H8O3", "glycerol", 1),
        ])
    else:
        Kb, Kf, Tb, Tf = 2.53, 5.12, 80.1, 5.5
        f, name, i = pick(rng, [("C10H8", "naphthalene", 1), ("C14H10", "anthracene", 1), ("C6H5COOH", "benzoic acid", 1)])
    m_solute = nice(rng, 1.0, 60.0, 0.5)
    m_solv = pick(rng, [100, 150, 200, 250, 500, 1000])
    M = molar_mass(f)
    molality = m_solute / M / (m_solv / 1000)
    dTb = i * Kb * molality
    dTf = i * Kf * molality
    note = (f"{name.capitalize()} dissociates into {i} ions, so the ideal van 't Hoff factor is $i = {i}$ "
            "(real values are slightly lower because of ion pairing)." if i > 1 else
            f"{name.capitalize()} does not dissociate, so $i = 1$.")
    question = (
        f"{q(m_solute, 'g')} of {name} ({pretty(f)}) is dissolved in {q(m_solv, 'g')} of {solvent}. "
        f"Estimate the boiling point and freezing point of the solution. "
        f"({solvent.capitalize()}: $K_b = {Kb}$ °C·kg/mol, $K_f = {Kf}$ °C·kg/mol, normal bp {Tb} °C, fp {Tf} °C.)"
    )
    steps = [
        f"Moles of solute: ${fmt(m_solute)}/{M:.2f} = {fmt(m_solute / M, 4)}$ mol.",
        f"Molality: $b = {fmt(m_solute / M, 4)}\\text{{ mol}}/{fmt(m_solv / 1000, 3)}\\text{{ kg}} = {fmt(molality, 4)}$ mol/kg.",
        note,
        f"$\\Delta T_b = iK_bb = ({i})({Kb})({fmt(molality, 4)}) = {fmt(dTb)}$ °C → bp $= {Tb + dTb:.2f}$ °C.",
        f"$\\Delta T_f = iK_fb = ({i})({Kf})({fmt(molality, 4)}) = {fmt(dTf)}$ °C → fp $= {Tf - dTf:.2f}$ °C.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"bp ≈ {Tb + dTb:.2f} °C; fp ≈ {Tf - dTf:.2f} °C",
            "values": {"m_solute": m_solute, "M": M, "m_solvent_g": m_solv, "i": i, "Kb": Kb, "Kf": Kf,
                       "molality": molality, "dTb": dTb, "dTf": dTf}}


@template("osmotic_pressure_molar_mass", CHEM, GEN, "Colligative properties", "hard")
def osmotic_pressure_molar_mass(rng):
    M_true = nice(rng, 8000, 200000, 500)
    m_mg = nice(rng, 20, 800, 5)
    V_mL = pick(rng, [10.0, 25.0, 50.0, 100.0])
    T = 298.15
    pi_atm = (m_mg / 1000 / M_true) / (V_mL / 1000) * R_LATM * T
    pi_mmHg = sig(pi_atm * 760, 3)
    pi_atm_r = pi_mmHg / 760
    M = (m_mg / 1000) * R_LATM * T / (pi_atm_r * V_mL / 1000)
    c = pi_atm_r / (R_LATM * T)
    dTf = 1.86 * c
    question = (
        f"A solution of {q(m_mg, 'mg')} of a protein in enough water to make {q(V_mL, 'mL', 3)} of solution has an "
        f"osmotic pressure of {q(pi_mmHg, 'mmHg')} at 25.0 °C. Estimate the molar mass of the protein. Why is "
        "osmometry preferred to freezing-point depression for such molecules?"
    )
    steps = [
        f"Convert the pressure: $\\Pi = {fmt(pi_mmHg)}/760 = {fmt(pi_atm_r)}$ atm.",
        f"Van 't Hoff equation $\\Pi = cRT$: $c = \\frac{{\\Pi}}{{RT}} = \\frac{{{fmt(pi_atm_r)}}}{{(0.08206)(298.15)}} = {fmt(c)}$ mol/L.",
        f"Moles of protein: $n = cV = ({fmt(c)})({fmt(V_mL / 1000, 3)}) = {fmt(c * V_mL / 1000)}$ mol.",
        f"Molar mass: $M = \\frac{{{fmt(m_mg / 1000)}\\text{{ g}}}}{{{fmt(c * V_mL / 1000)}\\text{{ mol}}}} = {fmt(M)}$ g/mol.",
        f"For comparison, the freezing-point depression would be only about $1.86 \\times {fmt(c)} = {fmt(dTf)}$ °C — "
        "far too small to measure accurately, whereas a few mmHg of osmotic pressure is easy to measure.",
    ]
    return {"question": question, "steps": steps, "answer": f"$M \\approx {fmt(M)}$ g/mol",
            "values": {"m_mg": m_mg, "V_mL": V_mL, "pi_mmHg": pi_mmHg, "M": M}}


@template("clausius_clapeyron", CHEM, PCHEM, "Vapor pressure", "medium")
def clausius_clapeyron(rng):
    name, dH, Tb = pick(rng, [("water", 40.7, 373.15), ("ethanol", 38.6, 351.4), ("benzene", 30.7, 353.2),
                              ("diethyl ether", 26.5, 307.6), ("acetone", 29.1, 329.2), ("methanol", 35.2, 337.8)])
    if rng.random() < 0.5:
        T2 = round(Tb - nice(rng, 10, 60, 1), 2)
        P2 = 760 * math.exp(-dH * 1000 / R_GAS * (1 / T2 - 1 / Tb))
        question = (
            f"The normal boiling point of {name} is {q(Tb, 'K', 5)} and its enthalpy of vaporization is "
            f"{q(dH, 'kJ/mol')}. Estimate its vapor pressure at {q(T2, 'K', 5)} ({T2 - 273.15:.1f} °C)."
        )
        steps = [
            "At the normal boiling point the vapor pressure is 760 mmHg.",
            "Clausius–Clapeyron: $\\ln\\frac{P_2}{P_1} = -\\frac{\\Delta H_{vap}}{R}\\left(\\frac{1}{T_2} - \\frac{1}{T_1}\\right)$.",
            f"$\\ln\\frac{{P_2}}{{760}} = -\\frac{{{fmt(dH * 1000)}}}{{8.314}}\\left(\\frac{{1}}{{{fmt(T2, 5)}}} - \\frac{{1}}{{{fmt(Tb, 5)}}}\\right) = {math.log(P2 / 760):.3f}$.",
            f"$P_2 = 760\\,e^{{{math.log(P2 / 760):.3f}}} = {fmt(P2)}$ mmHg.",
        ]
        answer = f"$P \\approx {fmt(P2)}$ mmHg"
        values = {"dH_kJ": dH, "Tb": Tb, "T2": T2, "P2_mmHg": P2}
    else:
        P2 = nice(rng, 400, 720, 5)
        T2 = 1 / (1 / Tb - R_GAS * math.log(P2 / 760) / (dH * 1000))
        question = (
            f"{name.capitalize()} boils at {q(Tb, 'K', 5)} at 760 mmHg ($\\Delta H_{{vap}} = {fmt(dH)}$ kJ/mol). "
            f"At what temperature does it boil where the atmospheric pressure is only {q(P2, 'mmHg')}, as on a high mountain?"
        )
        steps = [
            "A liquid boils when its vapor pressure equals the external pressure.",
            "Rearrange Clausius–Clapeyron: $\\frac{1}{T_2} = \\frac{1}{T_1} - \\frac{R}{\\Delta H_{vap}}\\ln\\frac{P_2}{P_1}$.",
            f"$\\frac{{1}}{{T_2}} = \\frac{{1}}{{{fmt(Tb, 5)}}} - \\frac{{8.314}}{{{fmt(dH * 1000)}}}\\ln\\frac{{{P2}}}{{760}} = {1 / T2:.6f}$ K⁻¹.",
            f"$T_2 = {T2:.1f}$ K $= {T2 - 273.15:.1f}$ °C — lower pressure means a lower boiling point.",
        ]
        answer = f"$T_b \\approx {T2:.1f}$ K ({T2 - 273.15:.1f} °C)"
        values = {"dH_kJ": dH, "Tb": Tb, "P2_mmHg": P2, "T2": T2}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Thermochemistry and thermodynamics
# ---------------------------------------------------------------------------

FUELS = [  # formula, name, standard enthalpy of formation (kJ/mol), phase
    ("CH4", "methane", -74.8, "g"), ("C2H6", "ethane", -84.0, "g"), ("C3H8", "propane", -103.8, "g"),
    ("C4H10", "butane", -125.6, "g"), ("C2H5OH", "ethanol", -277.6, "l"), ("CH3OH", "methanol", -238.6, "l"),
    ("C6H12O6", "glucose", -1273.3, "s"), ("C8H18", "octane", -250.1, "l"), ("C2H2", "acetylene", 226.7, "g"),
    ("C6H6", "benzene", 49.0, "l"),
]


def _dec(x):
    """Stoichiometric coefficient as text; a coefficient of 1 is omitted."""
    if x == 1:
        return ""
    return (str(int(x)) if float(x).is_integer() else f"{x:g}") + " "


@template("enthalpy_from_formation", CHEM, PCHEM, "Thermochemistry", "medium")
def enthalpy_from_formation(rng):
    f, name, dHf, phase = pick(rng, FUELS)
    c = parse_formula(f)
    x, y, z = c.get("C", 0), c.get("H", 0), c.get("O", 0)
    o2 = x + y / 4 - z / 2
    dHc = x * -393.5 + (y / 2) * -285.8 - dHf
    m = nice(rng, 1, 500, 1)
    M = molar_mass(f)
    n = m / M
    heat = -dHc * n
    eqn = f"{pretty(f)}({phase}) + {_dec(o2)}O₂(g) → {_dec(x)}CO₂(g) + {_dec(y / 2)}H₂O(l)"
    question = (
        f"Using standard enthalpies of formation — $\\Delta H_f^\\circ$[{pretty(f)}({phase})] $= {dHf}$ kJ/mol, "
        f"$\\Delta H_f^\\circ$[CO₂(g)] $= -393.5$ kJ/mol, $\\Delta H_f^\\circ$[H₂O(l)] $= -285.8$ kJ/mol — calculate the "
        f"standard enthalpy of combustion of {name}, and the heat released when {q(m, 'g')} of it burns completely."
    )
    steps = [
        f"Balanced equation per mole of fuel: {eqn}.",
        "$\\Delta H^\\circ_{rxn} = \\sum n\\Delta H_f^\\circ(\\text{products}) - \\sum n\\Delta H_f^\\circ(\\text{reactants})$; "
        "$\\Delta H_f^\\circ$ of an element in its standard state (O₂) is zero.",
        f"$\\Delta H_c^\\circ = [{x}(-393.5) + {y / 2:g}(-285.8)] - [{dHf}] = {dHc:.1f}$ kJ/mol.",
        f"Moles burned: ${fmt(m)}/{M:.2f} = {fmt(n, 4)}$ mol.",
        f"Heat released: $q = {fmt(n, 4)} \\times {-dHc:.1f} = {fmt(heat)}$ kJ.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$\\Delta H_c^\\circ = {dHc:.1f}$ kJ/mol; ${fmt(heat)}$ kJ released",
            "values": {"formula": f, "dHf": dHf, "dHc": dHc, "mass": m, "heat_kJ": heat}}


@template("neutralization_calorimetry", CHEM, PCHEM, "Calorimetry", "medium")
def neutralization_calorimetry(rng):
    V = pick(rng, [25.0, 50.0, 75.0, 100.0])
    ca = nice(rng, 0.50, 2.00, 0.05)
    cb = nice(rng, 0.50, 2.00, 0.05)
    T0 = nice(rng, 19.0, 25.0, 0.1)
    n_water = min(ca, cb) * V / 1000
    mass = 2 * V
    lim = "HCl" if ca <= cb else "NaOH"
    if rng.random() < 0.5:
        dH = -57.1
        dT = n_water * -dH * 1000 / (mass * 4.18)
        question = (
            f"In a coffee-cup calorimeter, {q(V, 'mL', 3)} of {q(ca, 'M')} HCl and {q(V, 'mL', 3)} of {q(cb, 'M')} NaOH, "
            f"both at {q(T0, '°C')}, are mixed. Taking $\\Delta H_{{neut}} = -57.1$ kJ per mole of water formed, a solution "
            "density of 1.00 g/mL and a specific heat of 4.18 J/(g·°C), predict the final temperature."
        )
        steps = [
            f"Moles: HCl ${fmt(ca * V / 1000)}$ mol, NaOH ${fmt(cb * V / 1000)}$ mol; "
            + ("they are equal." if ca == cb else f"{lim} is limiting.")
            + f" Water formed: ${fmt(n_water)}$ mol.",
            f"Heat released: $q = ({fmt(n_water)})(57.1\\times10^3) = {fmt(n_water * 57100)}$ J.",
            f"Total solution mass: ${fmt(mass, 3)}$ g; $\\Delta T = \\frac{{q}}{{mc}} = \\frac{{{fmt(n_water * 57100)}}}{{({fmt(mass, 3)})(4.18)}} = {dT:.2f}$ °C.",
            f"Final temperature: ${T0:.1f} + {dT:.2f} = {T0 + dT:.1f}$ °C.",
        ]
        answer = f"$T_f \\approx {T0 + dT:.1f}$ °C"
    else:
        dT = round(n_water * 57100 / (mass * 4.18) * rng.uniform(0.96, 1.03), 2)
        dH = -(mass * 4.18 * dT) / n_water / 1000
        question = (
            f"{q(V, 'mL', 3)} of {q(ca, 'M')} HCl and {q(V, 'mL', 3)} of {q(cb, 'M')} NaOH, both at {q(T0, '°C')}, are mixed "
            f"in a coffee-cup calorimeter and the temperature rises to {q(round(T0 + dT, 2), '°C', 4)}. Assuming a density of "
            "1.00 g/mL and a specific heat of 4.18 J/(g·°C), calculate $\\Delta H$ of neutralization per mole of water formed."
        )
        steps = [
            f"$\\Delta T = {T0 + dT:.2f} - {T0:.1f} = {dT:.2f}$ °C; mass of solution $= {fmt(mass, 3)}$ g.",
            f"Heat absorbed by the solution: $q = mc\\Delta T = ({fmt(mass, 3)})(4.18)({dT:.2f}) = {fmt(mass * 4.18 * dT)}$ J.",
            f"Water formed (limited by {'either' if ca == cb else lim}): ${fmt(n_water)}$ mol.",
            f"The reaction releases this heat, so $\\Delta H = -\\frac{{{fmt(mass * 4.18 * dT)}}}{{{fmt(n_water)}}} = {dH:.1f}$ kJ/mol "
            "(the accepted value for strong acid + strong base is about −56 to −57 kJ/mol).",
        ]
        answer = f"$\\Delta H_{{neut}} \\approx {dH:.1f}$ kJ/mol"
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"V_mL": V, "c_acid": ca, "c_base": cb, "n_water": n_water, "dT": dT, "dH_kJ": dH}}


BONDS = {"H–H": 436, "Cl–Cl": 243, "H–Cl": 431, "C–H": 413, "O=O": 498, "C=O (CO₂)": 799, "O–H": 463,
         "C=C": 614, "C–C": 348, "N≡N": 945, "N–H": 391, "C–Cl": 328, "Br–Br": 193, "C–Br": 276, "H–Br": 366}

BOND_REACTIONS = [
    ("CH₄(g) + 2 O₂(g) → CO₂(g) + 2 H₂O(g)", "CH4", 1, {"C–H": 4, "O=O": 2}, {"C=O (CO₂)": 2, "O–H": 4}),
    ("H₂(g) + Cl₂(g) → 2 HCl(g)", "H2", 1, {"H–H": 1, "Cl–Cl": 1}, {"H–Cl": 2}),
    ("C₂H₄(g) + H₂(g) → C₂H₆(g)", "C2H4", 1, {"C=C": 1, "C–H": 4, "H–H": 1}, {"C–C": 1, "C–H": 6}),
    ("N₂(g) + 3 H₂(g) → 2 NH₃(g)", "N2", 1, {"N≡N": 1, "H–H": 3}, {"N–H": 6}),
    ("2 H₂(g) + O₂(g) → 2 H₂O(g)", "H2", 2, {"H–H": 2, "O=O": 1}, {"O–H": 4}),
    ("CH₄(g) + Cl₂(g) → CH₃Cl(g) + HCl(g)", "CH4", 1, {"C–H": 4, "Cl–Cl": 1}, {"C–H": 3, "C–Cl": 1, "H–Cl": 1}),
    ("C₂H₄(g) + Br₂(g) → C₂H₄Br₂(g)", "C2H4", 1, {"C=C": 1, "Br–Br": 1}, {"C–C": 1, "C–Br": 2}),
    ("H₂(g) + Br₂(g) → 2 HBr(g)", "H2", 1, {"H–H": 1, "Br–Br": 1}, {"H–Br": 2}),
]


@template("bond_enthalpy_estimate", CHEM, PCHEM, "Bond enthalpies", "medium")
def bond_enthalpy_estimate(rng):
    eqn, key, kcoef, broken, formed = pick(rng, BOND_REACTIONS)
    Hb = sum(BONDS[b] * n for b, n in broken.items())
    Hf = sum(BONDS[b] * n for b, n in formed.items())
    dH = Hb - Hf
    m = nice(rng, 1.0, 100.0, 0.5)
    n = m / molar_mass(key)
    heat = -dH * n / kcoef
    table = ", ".join(f"{b} {BONDS[b]}" for b in dict.fromkeys(list(broken) + list(formed)))
    question = (
        f"Use average bond enthalpies (kJ/mol: {table}) to estimate $\\Delta H$ for {eqn}. "
        f"Roughly how much heat is released or absorbed when {q(m, 'g')} of {pretty(key)} reacts?"
    )
    steps = [
        "$\\Delta H \\approx \\sum(\\text{bonds broken}) - \\sum(\\text{bonds formed})$: breaking bonds costs energy, forming them releases it.",
        "Bonds broken: " + " + ".join(f"{n}({BONDS[b]})" for b, n in broken.items()) + f" $= {Hb}$ kJ.",
        "Bonds formed: " + " + ".join(f"{n}({BONDS[b]})" for b, n in formed.items()) + f" $= {Hf}$ kJ.",
        f"$\\Delta H \\approx {Hb} - {Hf} = {dH}$ kJ per mole of reaction as written "
        f"({'exothermic' if dH < 0 else 'endothermic'}).",
        f"Moles of {pretty(key)}: ${fmt(n, 4)}$ mol $\\Rightarrow$ ${fmt(n, 4)}/{kcoef}$ mol of reaction; "
        f"heat {'released' if dH < 0 else 'absorbed'} $\\approx {fmt(abs(heat))}$ kJ.",
        "Average bond enthalpies ignore the molecular environment, so the estimate typically differs from "
        "values computed with enthalpies of formation by a few percent.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$\\Delta H \\approx {dH}$ kJ; about ${fmt(abs(heat))}$ kJ {'released' if dH < 0 else 'absorbed'}",
            "values": {"dH_kJ": dH, "mass": m, "heat_released_kJ": heat}}


GIBBS_REACTIONS = [
    ("CaCO₃(s) → CaO(s) + CO₂(g)", 178.3, 160.5),
    ("N₂(g) + 3 H₂(g) → 2 NH₃(g)", -92.2, -198.7),
    ("2 SO₂(g) + O₂(g) → 2 SO₃(g)", -197.8, -187.9),
    ("H₂O(l) → H₂O(g)", 44.0, 118.9),
    ("N₂O₄(g) → 2 NO₂(g)", 57.2, 175.8),
    ("NH₄NO₃(s) → NH₄⁺(aq) + NO₃⁻(aq)", 25.7, 108.7),
    ("2 H₂O₂(l) → 2 H₂O(l) + O₂(g)", -196.0, 125.8),
    ("C(graphite) → C(diamond)", 1.9, -3.36),
    ("PCl₅(g) → PCl₃(g) + Cl₂(g)", 87.9, 170.2),
    ("2 NO(g) + O₂(g) → 2 NO₂(g)", -114.1, -146.5),
]


@template("gibbs_spontaneity", CHEM, PCHEM, "Gibbs free energy", "medium")
def gibbs_spontaneity(rng):
    eqn, dH, dS = pick(rng, GIBBS_REACTIONS)
    T = nice(rng, 200, 1500, 25)
    dG = dH - T * dS / 1000
    if dH < 0 and dS > 0:
        regime = "spontaneous at all temperatures ($\\Delta H < 0$, $\\Delta S > 0$)"
        Tc = None
    elif dH > 0 and dS < 0:
        regime = "non-spontaneous at all temperatures ($\\Delta H > 0$, $\\Delta S < 0$)"
        Tc = None
    else:
        Tc = dH * 1000 / dS
        kind = "above" if dH > 0 else "below"
        regime = f"spontaneous {kind} $T = \\Delta H/\\Delta S = {fmt(Tc)}$ K"
    question = (
        f"For {eqn}, $\\Delta H^\\circ = {dH}$ kJ/mol and $\\Delta S^\\circ = {dS}$ J/(mol·K). Assuming these are "
        f"independent of temperature, calculate $\\Delta G^\\circ$ at {q(T, 'K')} and state the temperature range over "
        "which the reaction is spontaneous under standard conditions."
    )
    steps = [
        "$\\Delta G^\\circ = \\Delta H^\\circ - T\\Delta S^\\circ$ (convert $\\Delta S$ to kJ).",
        f"$\\Delta G^\\circ = {dH} - ({T})({dS / 1000:.4f}) = {dG:.1f}$ kJ/mol → "
        f"{'spontaneous' if dG < 0 else 'non-spontaneous'} at {T} K.",
        f"Sign analysis: the reaction is {regime}.",
    ]
    if Tc is not None:
        steps.append("At the crossover temperature $\\Delta G^\\circ = 0$ and the system is at equilibrium under standard conditions.")
    return {"question": question, "steps": steps,
            "answer": f"$\\Delta G^\\circ = {dG:.1f}$ kJ/mol at {T} K; {regime}",
            "values": {"dH": dH, "dS": dS, "T": T, "dG": dG, "T_crossover": Tc}}


@template("equilibrium_constant_gibbs", CHEM, PCHEM, "Chemical equilibrium", "medium")
def equilibrium_constant_gibbs(rng):
    T = pick(rng, [298.15, 298.15, 350.0, 400.0, 500.0, 700.0])
    if rng.random() < 0.5:
        dG = nice(rng, -60.0, 40.0, 0.5)
        if dG == 0:
            dG = -5.0
        K = math.exp(-dG * 1000 / (R_GAS * T))
        question = (
            f"A reaction has $\\Delta G^\\circ = {fmt(dG, 3)}$ kJ/mol at ${T:g}$ K. Calculate its equilibrium constant "
            "and say whether products or reactants are favored at equilibrium."
        )
        steps = [
            "$\\Delta G^\\circ = -RT\\ln K \\Rightarrow K = e^{-\\Delta G^\\circ/RT}$.",
            f"$\\frac{{-\\Delta G^\\circ}}{{RT}} = \\frac{{{fmt(-dG * 1000, 4)}}}{{(8.314)({fmt(T, 5)})}} = {-dG * 1000 / (R_GAS * T):.3f}$.",
            f"$K = e^{{{-dG * 1000 / (R_GAS * T):.3f}}} = {fmt(K)}$.",
            f"Since $K {'>' if K > 1 else '<'} 1$, {'products' if K > 1 else 'reactants'} are favored at equilibrium.",
        ]
        answer = f"$K = {fmt(K)}$ ({'products' if K > 1 else 'reactants'} favored)"
    else:
        exp = rng.randint(-12, 12)
        K = round(rng.uniform(1.0, 9.9), 1) * 10.0 ** exp
        dG = -R_GAS * T * math.log(K) / 1000
        question = (
            f"The equilibrium constant of a reaction is $K = {fmt(K, 2)}$ at ${T:g}$ K. Calculate $\\Delta G^\\circ$."
        )
        steps = [
            "$\\Delta G^\\circ = -RT\\ln K$.",
            f"$\\ln K = \\ln({fmt(K, 2)}) = {math.log(K):.3f}$.",
            f"$\\Delta G^\\circ = -(8.314)({fmt(T, 5)})({math.log(K):.3f}) = {fmt(dG * 1000, 4)}$ J/mol $= {dG:.2f}$ kJ/mol.",
            f"A {'negative' if dG < 0 else 'positive'} $\\Delta G^\\circ$ corresponds to $K {'>' if dG < 0 else '<'} 1$. ✓",
        ]
        answer = f"$\\Delta G^\\circ = {dG:.2f}$ kJ/mol"
    return {"question": question, "steps": steps, "answer": answer, "values": {"T": T, "dG_kJ": dG, "K": K}}


# ---------------------------------------------------------------------------
# Equilibrium
# ---------------------------------------------------------------------------


@template("equilibrium_ice_hi", CHEM, PCHEM, "Chemical equilibrium", "hard")
def equilibrium_ice_hi(rng):
    K = 50.5
    a = nice(rng, 0.10, 2.00, 0.05)
    b = nice(rng, 0.10, 2.00, 0.05)
    # K(a-x)(b-x) = 4x^2  ->  (K-4)x^2 - K(a+b)x + Kab = 0
    A, B, Cq = K - 4, -K * (a + b), K * a * b
    disc = B * B - 4 * A * Cq
    roots = [(-B - math.sqrt(disc)) / (2 * A), (-B + math.sqrt(disc)) / (2 * A)]
    x = next(r for r in roots if 0 < r < min(a, b))
    question = (
        f"At 448 °C, $K_c = 50.5$ for H₂(g) + I₂(g) ⇌ 2 HI(g). If a flask initially contains [H₂] = {q(a, 'M')} and "
        f"[I₂] = {q(b, 'M')} with no HI, find all equilibrium concentrations."
    )
    steps = [
        f"ICE table: H₂ ${fmt(a)} - x$, I₂ ${fmt(b)} - x$, HI $2x$.",
        f"$K_c = \\frac{{(2x)^2}}{{({fmt(a)} - x)({fmt(b)} - x)}} = 50.5$.",
        f"Expand: $46.5x^2 - {fmt(K * (a + b), 4)}x + {fmt(K * a * b, 4)} = 0$.",
        f"Quadratic formula: roots ${fmt(roots[0], 4)}$ and ${fmt(roots[1], 4)}$; only $x = {fmt(x, 4)}$ M keeps every "
        "concentration positive.",
        f"[H₂] $= {fmt(a - x, 3)}$ M, [I₂] $= {fmt(b - x, 3)}$ M, [HI] $= {fmt(2 * x, 3)}$ M.",
        f"Check: $\\frac{{({fmt(2 * x, 4)})^2}}{{({fmt(a - x, 4)})({fmt(b - x, 4)})}} = {fmt((2 * x) ** 2 / ((a - x) * (b - x)), 3)}$ ✓",
    ]
    return {"question": question, "steps": steps,
            "answer": f"[H₂] = {fmt(a - x, 3)} M, [I₂] = {fmt(b - x, 3)} M, [HI] = {fmt(2 * x, 3)} M",
            "values": {"K": K, "H2_0": a, "I2_0": b, "x": x, "H2": a - x, "I2": b - x, "HI": 2 * x}}


@template("equilibrium_dissociation", CHEM, PCHEM, "Chemical equilibrium", "hard")
def equilibrium_dissociation(rng):
    eqn, K, temp, nu = pick(rng, [
        ("N₂O₄(g) ⇌ 2 NO₂(g)", 4.64e-3, "25 °C", 2),
        ("PCl₅(g) ⇌ PCl₃(g) + Cl₂(g)", 4.19e-2, "250 °C", 1),
    ])
    c0 = nice(rng, 0.020, 1.000, 0.005)
    if nu == 2:  # 4x^2 = K(c0 - x)
        x = (-K + math.sqrt(K * K + 16 * K * c0)) / 8
        expr = "\\frac{(2x)^2}{c_0 - x}"
        quad = f"$4x^2 + {fmt(K)}x - {fmt(K * c0)} = 0$"
        prods = f"[NO₂] $= 2x = {fmt(2 * x)}$ M"
        reac = "N₂O₄"
    else:  # x^2 = K(c0 - x)
        x = (-K + math.sqrt(K * K + 4 * K * c0)) / 2
        expr = "\\frac{x^2}{c_0 - x}"
        quad = f"$x^2 + {fmt(K)}x - {fmt(K * c0)} = 0$"
        prods = f"[PCl₃] = [Cl₂] $= {fmt(x)}$ M"
        reac = "PCl₅"
    alpha = x / c0
    question = (
        f"For {eqn}, $K_c = {fmt(K)}$ at {temp}. If {reac} is placed in an empty flask at an initial concentration of "
        f"{q(c0, 'M')}, find the equilibrium concentrations and the fraction of {reac} that dissociates."
    )
    steps = [
        f"Let $x$ = mol/L of {reac} that dissociates; $K_c = {expr}$ with $c_0 = {fmt(c0)}$ M.",
        f"Rearranged: {quad}.",
        f"Positive root: $x = {fmt(x)}$ M.",
        f"[{reac}] $= {fmt(c0 - x)}$ M; {prods}.",
        f"Fraction dissociated: $\\alpha = x/c_0 = {fmt(alpha)}$ ({100 * alpha:.1f}%). Diluting the gas (lower $c_0$) increases $\\alpha$ "
        "— Le Châtelier's principle favors the side with more moles of gas.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"[{reac}] = {fmt(c0 - x)} M, {prods.replace('$', '')}; {100 * alpha:.1f}% dissociated",
            "values": {"K": K, "c0": c0, "nu": nu, "x": x, "alpha": alpha}}


KSP_SALTS = [  # formula, name, Ksp, cations per formula unit, anions per formula unit
    ("AgCl", "silver chloride", 1.8e-10, 1, 1), ("BaSO4", "barium sulfate", 1.1e-10, 1, 1),
    ("AgBr", "silver bromide", 5.0e-13, 1, 1), ("CaCO3", "calcium carbonate", 3.4e-9, 1, 1),
    ("CaF2", "calcium fluoride", 3.9e-11, 1, 2), ("PbI2", "lead(II) iodide", 9.8e-9, 1, 2),
    ("Mg(OH)2", "magnesium hydroxide", 5.6e-12, 1, 2), ("Ag2CrO4", "silver chromate", 1.1e-12, 2, 1),
    ("Ag2CO3", "silver carbonate", 8.5e-12, 2, 1), ("PbCl2", "lead(II) chloride", 1.7e-5, 1, 2),
    ("Ca3(PO4)2", "calcium phosphate", 2.1e-33, 3, 2),
]


@template("ksp_solubility", CHEM, PCHEM, "Solubility equilibria", "medium")
def ksp_solubility(rng):
    f, name, Ksp, a, b = pick(rng, KSP_SALTS)
    M = molar_mass(f)
    coef = (a ** a) * (b ** b)
    s = (Ksp / coef) ** (1 / (a + b))
    coef_s = "" if coef == 1 else str(coef)
    ion_terms = ("s" if a == 1 else f"({a}s)^{a}") + " \\cdot " + ("s" if b == 1 else f"({b}s)^{b}")
    question = (
        f"The solubility product of {name} ({pretty(f)}) is $K_{{sp}} = {fmt(Ksp, 2)}$ at 25 °C. Calculate its molar "
        "solubility in pure water and its solubility in g/L."
    )
    steps = [
        f"Dissolution produces {a} cation{'s' if a > 1 else ''} and {b} anion{'s' if b > 1 else ''} per formula unit; "
        f"if $s$ mol/L dissolves, the ion concentrations are ${a if a > 1 else ''}s$ and ${b if b > 1 else ''}s$.",
        f"$K_{{sp}} = {ion_terms} = {coef_s}s^{{{a + b}}}$.",
        f"$s = \\left(\\frac{{{fmt(Ksp, 2)}}}{{{coef}}}\\right)^{{1/{a + b}}} = {fmt(s)}$ mol/L.",
        f"Solubility in g/L: $({fmt(s)})({M:.2f}) = {fmt(s * M)}$ g/L.",
    ]
    if a + b > 2:
        steps.append("Note: salts with different ion ratios cannot be compared by $K_{sp}$ alone — compare molar solubilities.")
    return {"question": question, "steps": steps, "answer": f"$s = {fmt(s)}$ mol/L $= {fmt(s * M)}$ g/L",
            "values": {"formula": f, "Ksp": Ksp, "a": a, "b": b, "s": s, "g_per_L": s * M}}


@template("common_ion_solubility", CHEM, PCHEM, "Solubility equilibria", "medium")
def common_ion_solubility(rng):
    f, name, Ksp, salt, ion = pick(rng, [
        ("AgCl", "silver chloride", 1.8e-10, "NaCl", "Cl⁻"), ("BaSO4", "barium sulfate", 1.1e-10, "Na₂SO₄", "SO₄²⁻"),
        ("AgBr", "silver bromide", 5.0e-13, "KBr", "Br⁻"), ("CaCO3", "calcium carbonate", 3.4e-9, "Na₂CO₃", "CO₃²⁻"),
    ])
    c = pick(rng, [0.0010, 0.0050, 0.010, 0.050, 0.10, 0.20, 0.50])
    s0 = math.sqrt(Ksp)
    s = 2 * Ksp / (c + math.sqrt(c * c + 4 * Ksp))  # numerically stable root of s^2 + cs - Ksp = 0
    s_approx = Ksp / c
    question = (
        f"Compare the molar solubility of {name} ($K_{{sp}} = {fmt(Ksp, 2)}$) in pure water with its solubility in "
        f"{q(c, 'M', 2)} {salt}."
    )
    steps = [
        f"Pure water: $K_{{sp}} = s^2 \\Rightarrow s_0 = \\sqrt{{{fmt(Ksp, 2)}}} = {fmt(s0)}$ M.",
        f"In {fmt(c, 2)} M {salt} the common ion {ion} is already present: $K_{{sp}} = s(s + {fmt(c, 2)})$.",
        f"Because $s \\ll {fmt(c, 2)}$, $s \\approx K_{{sp}}/{fmt(c, 2)} = {fmt(s_approx)}$ M; solving the quadratic "
        f"$s^2 + {fmt(c, 2)}s - K_{{sp}} = 0$ exactly gives $s = {fmt(s)}$ M.",
        f"The solubility drops by a factor of ${fmt(s0 / s)}$ — the common-ion effect predicted by Le Châtelier's principle.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"pure water ${fmt(s0)}$ M; in {salt} ${fmt(s)}$ M (≈{fmt(s0 / s)}× lower)",
            "values": {"Ksp": Ksp, "c_common": c, "s_water": s0, "s_common": s}}


# ---------------------------------------------------------------------------
# Acids and bases
# ---------------------------------------------------------------------------


@template("strong_acid_base_ph", CHEM, PCHEM, "pH", "easy")
def strong_acid_base_ph(rng):
    f, name, kind, nion = pick(rng, [
        ("HCl", "hydrochloric acid", "acid", 1), ("HNO3", "nitric acid", "acid", 1),
        ("HClO4", "perchloric acid", "acid", 1), ("NaOH", "sodium hydroxide", "base", 1),
        ("KOH", "potassium hydroxide", "base", 1), ("Ba(OH)2", "barium hydroxide", "base", 2),
    ])
    c = round(rng.uniform(1.0, 9.9), 1) * 10.0 ** -rng.randint(1, 4)
    ion = c * nion
    if kind == "acid":
        pH = -math.log10(ion)
        steps = [
            f"{name.capitalize()} is a strong acid and ionizes completely: [H₃O⁺] $= {fmt(ion, 2)}$ M.",
            f"pH $= -\\log_{{10}}({fmt(ion, 2)}) = {ph_str(pH)}$.",
            f"pOH $= 14.00 - {ph_str(pH)} = {ph_str(14 - pH)}$; [OH⁻] $= 10^{{-14}}/{fmt(ion, 2)} = {fmt(KW / ion, 2)}$ M.",
        ]
    else:
        pOH = -math.log10(ion)
        pH = 14 - pOH
        steps = [
            f"{name.capitalize()} is a strong base and dissociates completely"
            + (f", releasing 2 OH⁻ per formula unit: [OH⁻] $= 2 \\times {fmt(c, 2)} = {fmt(ion, 2)}$ M." if nion == 2
               else f": [OH⁻] $= {fmt(ion, 2)}$ M."),
            f"pOH $= -\\log_{{10}}({fmt(ion, 2)}) = {ph_str(pOH)}$.",
            f"At 25 °C, pH $= 14.00 - {ph_str(pOH)} = {ph_str(pH)}$; [H₃O⁺] $= {fmt(KW / ion, 2)}$ M.",
        ]
    question = f"What is the pH of a {q(c, 'M', 2)} solution of {name} ({pretty(f)}) at 25 °C?"
    return {"question": question, "steps": steps, "answer": f"pH = {ph_str(pH)}",
            "values": {"formula": f, "c": c, "n_ion": nion, "kind": kind, "pH": pH}}


WEAK_ACIDS = [("acetic acid", "CH₃COOH", 1.8e-5), ("formic acid", "HCOOH", 1.8e-4), ("hydrofluoric acid", "HF", 6.8e-4),
              ("hydrocyanic acid", "HCN", 6.2e-10), ("hypochlorous acid", "HOCl", 3.0e-8),
              ("benzoic acid", "C₆H₅COOH", 6.3e-5), ("nitrous acid", "HNO₂", 4.5e-4), ("lactic acid", "C₃H₆O₃", 1.4e-4)]
WEAK_BASES = [("ammonia", "NH₃", 1.8e-5), ("methylamine", "CH₃NH₂", 4.4e-4), ("pyridine", "C₅H₅N", 1.7e-9),
              ("aniline", "C₆H₅NH₂", 4.3e-10), ("trimethylamine", "(CH₃)₃N", 6.4e-5), ("hydrazine", "N₂H₄", 1.3e-6)]


def _weak(K, c):
    return (-K + math.sqrt(K * K + 4 * K * c)) / 2


@template("weak_acid_ph", CHEM, PCHEM, "Weak acids", "medium")
def weak_acid_ph(rng):
    name, f, Ka = pick(rng, WEAK_ACIDS)
    c = round(rng.uniform(1.0, 9.9), 1) * 10.0 ** -rng.randint(1, 3)
    x = _weak(Ka, c)
    pH = -math.log10(x)
    xa = math.sqrt(Ka * c)
    pct = 100 * x / c
    question = (
        f"Calculate the pH and the percent ionization of a {q(c, 'M', 2)} solution of {name} ({f}), "
        f"$K_a = {fmt(Ka, 2)}$."
    )
    steps = [
        f"{f} + H₂O ⇌ H₃O⁺ + A⁻. ICE: [HA] $= {fmt(c, 2)} - x$, [H₃O⁺] = [A⁻] $= x$.",
        f"$K_a = \\frac{{x^2}}{{{fmt(c, 2)} - x}} = {fmt(Ka, 2)} \\Rightarrow x^2 + {fmt(Ka, 2)}x - {fmt(Ka * c)} = 0$.",
        f"Exact solution: $x = \\frac{{-K_a + \\sqrt{{K_a^2 + 4K_ac}}}}{{2}} = {fmt(x)}$ M = [H₃O⁺].",
        f"pH $= -\\log({fmt(x)}) = {ph_str(pH)}$; percent ionization $= {fmt(x)}/{fmt(c, 2)} \\times 100\\% = {pct:.2g}\\%$.",
        f"Shortcut check: $x \\approx \\sqrt{{K_ac}} = {fmt(xa)}$ M (pH {ph_str(-math.log10(xa))}); "
        + ("the 5% rule holds, so the approximation is fine." if pct < 5 else
           "ionization exceeds 5%, so the approximation is not valid here and the quadratic is required."),
    ]
    return {"question": question, "steps": steps,
            "answer": f"pH = {ph_str(pH)}; {pct:.2g}% ionized",
            "values": {"Ka": Ka, "c": c, "H3O": x, "pH": pH, "percent_ionization": pct}}


@template("weak_base_ph", CHEM, PCHEM, "Weak bases", "medium")
def weak_base_ph(rng):
    name, f, Kb = pick(rng, WEAK_BASES)
    c = round(rng.uniform(1.0, 9.9), 1) * 10.0 ** -rng.randint(1, 3)
    x = _weak(Kb, c)
    pOH = -math.log10(x)
    pH = 14 - pOH
    question = f"Calculate the pH of a {q(c, 'M', 2)} solution of {name} ({f}), $K_b = {fmt(Kb, 2)}$, at 25 °C."
    steps = [
        f"B + H₂O ⇌ BH⁺ + OH⁻. ICE: [B] $= {fmt(c, 2)} - x$, [BH⁺] = [OH⁻] $= x$.",
        f"$K_b = \\frac{{x^2}}{{{fmt(c, 2)} - x}} \\Rightarrow x^2 + {fmt(Kb, 2)}x - {fmt(Kb * c)} = 0$.",
        f"$x = [\\text{{OH}}^-] = {fmt(x)}$ M.",
        f"pOH $= {ph_str(pOH)}$, so pH $= 14.00 - {ph_str(pOH)} = {ph_str(pH)}$.",
        f"Percent protonated: ${100 * x / c:.2g}\\%$.",
    ]
    return {"question": question, "steps": steps, "answer": f"pH = {ph_str(pH)}",
            "values": {"Kb": Kb, "c": c, "OH": x, "pH": pH}}


BUFFERS = [  # acid form, conjugate base form, Ka of the acid form
    ("acetic acid (CH₃COOH)", "sodium acetate (CH₃COONa)", 1.8e-5),
    ("ammonium chloride (NH₄Cl)", "ammonia (NH₃)", 5.6e-10),
    ("sodium dihydrogen phosphate (NaH₂PO₄)", "sodium hydrogen phosphate (Na₂HPO₄)", 6.2e-8),
    ("carbonic acid (H₂CO₃)", "sodium bicarbonate (NaHCO₃)", 4.5e-7),
    ("formic acid (HCOOH)", "sodium formate (HCOONa)", 1.8e-4),
    ("hydrofluoric acid (HF)", "sodium fluoride (NaF)", 6.8e-4),
]


@template("buffer_ph", CHEM, PCHEM, "Buffers", "medium")
def buffer_ph(rng):
    acid, base, Ka = pick(rng, BUFFERS)
    pKa = -math.log10(Ka)
    V = pick(rng, [0.500, 1.00])
    ca = nice(rng, 0.10, 1.00, 0.05)
    cb = nice(rng, 0.10, 1.00, 0.05)
    na, nb = ca * V, cb * V
    add = pick(rng, ["HCl", "NaOH"])
    n_add = round(rng.uniform(0.05, 0.6) * min(na, nb), 3)
    pH0 = pKa + math.log10(nb / na)
    if add == "HCl":
        na2, nb2 = na + n_add, nb - n_add
        rxn = "H₃O⁺ + A⁻ → HA + H₂O: the base component consumes the added acid"
        pH_water = -math.log10(n_add / V)
    else:
        na2, nb2 = na - n_add, nb + n_add
        rxn = "OH⁻ + HA → A⁻ + H₂O: the acid component consumes the added base"
        pH_water = 14 + math.log10(n_add / V)
    pH1 = pKa + math.log10(nb2 / na2)
    question = (
        f"A buffer is made with {q(ca, 'M')} {acid} and {q(cb, 'M')} {base} in {q(V, 'L', 3)} of solution "
        f"($K_a = {fmt(Ka, 2)}$ for the acid form). Calculate its pH, then the pH after adding {q(n_add, 'mol')} of "
        f"{add} (ignore the volume change). Compare with adding the same amount to {fmt(V, 3)} L of pure water."
    )
    steps = [
        f"$\\mathrm{{p}}K_a = -\\log({fmt(Ka, 2)}) = {pKa:.2f}$.",
        f"Henderson–Hasselbalch: pH $= \\mathrm{{p}}K_a + \\log\\frac{{[\\text{{A}}^-]}}{{[\\text{{HA}}]}} = {pKa:.2f} + "
        f"\\log\\frac{{{fmt(nb)}}}{{{fmt(na)}}} = {ph_str(pH0)}$.",
        f"Added {add}: {rxn}. New amounts: HA ${fmt(na2)}$ mol, A⁻ ${fmt(nb2)}$ mol.",
        f"New pH $= {pKa:.2f} + \\log\\frac{{{fmt(nb2)}}}{{{fmt(na2)}}} = {ph_str(pH1)}$ (change of {pH1 - pH0:+.2f}).",
        f"In pure water the same {add} would give pH $= {ph_str(pH_water)}$ — a change of {pH_water - 7:+.2f} units, "
        "showing how strongly the buffer resists pH changes.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"initial pH = {ph_str(pH0)}; after {add}: pH = {ph_str(pH1)} (pure water: {ph_str(pH_water)})",
            "values": {"Ka": Ka, "ca": ca, "cb": cb, "V": V, "added": add, "n_add": n_add, "pH0": pH0, "pH1": pH1}}


@template("weak_acid_titration", CHEM, PCHEM, "Acid-base titration", "hard")
def weak_acid_titration(rng):
    name, f, Ka = pick(rng, WEAK_ACIDS)
    Va = pick(rng, [25.0, 50.0])
    Ca = nice(rng, 0.050, 0.200, 0.010)
    Cb = nice(rng, 0.050, 0.200, 0.010)
    Veq = Ca * Va / Cb
    pKa = -math.log10(Ka)
    x0 = _weak(Ka, Ca)
    pH_init = -math.log10(x0)
    cA = Ca * Va / (Va + Veq)
    Kb = KW / Ka
    oh = _weak(Kb, cA)
    pH_eq = 14 + math.log10(oh)
    Vx = Veq + 10.0
    oh_ex = Cb * 10.0 / (Va + Vx)
    pH_ex = 14 + math.log10(oh_ex)
    question = (
        f"{q(Va, 'mL', 3)} of {q(Ca, 'M')} {name} ($K_a = {fmt(Ka, 2)}$) is titrated with {q(Cb, 'M')} NaOH. Find (a) the "
        "equivalence-point volume, and the pH (b) before any base is added, (c) at the half-equivalence point, "
        f"(d) at the equivalence point, and (e) after {q(Vx, 'mL', 3)} of base has been added."
    )
    steps = [
        f"(a) $V_{{eq}} = \\frac{{C_aV_a}}{{C_b}} = \\frac{{({fmt(Ca)})({fmt(Va, 3)})}}{{{fmt(Cb)}}} = {fmt(Veq)}$ mL.",
        f"(b) Weak acid alone: solve $x^2/({fmt(Ca)} - x) = K_a$ → [H₃O⁺] $= {fmt(x0)}$ M, pH $= {ph_str(pH_init)}$.",
        f"(c) At half-equivalence [HA] = [A⁻], so pH = p$K_a$ $= {ph_str(pKa)}$.",
        f"(d) At equivalence all HA has become A⁻: [A⁻] $= \\frac{{({fmt(Ca)})({fmt(Va, 3)})}}{{{fmt(Va, 3)} + {fmt(Veq)}}} = {fmt(cA)}$ M. "
        f"A⁻ is a weak base with $K_b = K_w/K_a = {fmt(Kb)}$; [OH⁻] $= {fmt(oh)}$ M, so pH $= {ph_str(pH_eq)}$ (basic, as expected "
        "for a weak acid–strong base titration).",
        f"(e) Excess OH⁻: $({fmt(Cb)})(10.0\\text{{ mL}})/({fmt(Va, 3)} + {fmt(Vx)}\\text{{ mL}}) = {fmt(oh_ex)}$ M → pH $= {ph_str(pH_ex)}$.",
        "A good indicator changes color near the equivalence pH — phenolphthalein (pH 8.2–10) is the usual choice.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"(a) {fmt(Veq)} mL; (b) {ph_str(pH_init)}; (c) {ph_str(pKa)}; (d) {ph_str(pH_eq)}; (e) {ph_str(pH_ex)}",
            "values": {"Ka": Ka, "Va": Va, "Ca": Ca, "Cb": Cb, "Veq": Veq, "pH_initial": pH_init, "pH_half": pKa,
                       "pH_eq": pH_eq, "pH_excess": pH_ex}}


# ---------------------------------------------------------------------------
# Kinetics
# ---------------------------------------------------------------------------


@template("first_order_kinetics", CHEM, PCHEM, "Chemical kinetics", "medium")
def first_order_kinetics(rng):
    unit = pick(rng, ["s", "min", "h"])
    t_half = nice(rng, 5, 400, 1)
    k = math.log(2) / t_half
    A0 = nice(rng, 0.10, 2.00, 0.05)
    t = sig(t_half * rng.uniform(0.3, 4.0), 3)
    A = A0 * math.exp(-k * t)
    pct_target = pick(rng, [10, 20, 25, 1, 5, 50, 90])
    t_target = math.log(100 / pct_target) / k
    context = pick(rng, [
        "A compound decomposes by first-order kinetics",
        "A drug is eliminated from the bloodstream by first-order kinetics",
        "A pesticide degrades in soil by first-order kinetics",
        "An organic peroxide decomposes in solution by first-order kinetics",
    ])
    question = (
        f"{context} with a half-life of {q(t_half, unit)}. If the initial concentration is {q(A0, 'M')}, find the rate "
        f"constant, the concentration after {q(t, unit)}, and the time needed for the concentration to fall to "
        f"{pct_target}% of its initial value."
    )
    steps = [
        f"For first-order kinetics $t_{{1/2}} = \\ln2/k$, so $k = 0.6931/{t_half} = {fmt(k)}$ {unit}⁻¹ (independent of concentration).",
        f"Integrated rate law: $[A] = [A]_0e^{{-kt}} = {fmt(A0)}\\,e^{{-({fmt(k)})({fmt(t, 4)})}} = {fmt(A)}$ M.",
        f"Time to reach {pct_target}%: $t = \\frac{{\\ln([A]_0/[A])}}{{k}} = \\frac{{\\ln({fmt(100 / pct_target, 3)})}}{{{fmt(k)}}} = {fmt(t_target)}$ {unit}.",
        f"Check: that is ${fmt(t_target / t_half)}$ half-lives, and $(1/2)^{{{fmt(t_target / t_half)}}} = {fmt(0.5 ** (t_target / t_half))}$. ✓",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$k = {fmt(k)}$ {unit}⁻¹; $[A] = {fmt(A)}$ M; $t = {fmt(t_target)}$ {unit}",
            "values": {"t_half": t_half, "k": k, "A0": A0, "t": t, "A": A, "pct_target": pct_target,
                       "t_target": t_target}}


@template("second_order_kinetics", CHEM, PCHEM, "Chemical kinetics", "medium")
def second_order_kinetics(rng):
    k = round(rng.uniform(1.0, 9.9), 2) * 10.0 ** rng.randint(-3, 0)
    A0 = nice(rng, 0.050, 1.500, 0.010)
    t = nice(rng, 10, 2000, 10)
    A = 1 / (1 / A0 + k * t)
    th1 = 1 / (k * A0)
    th2 = 1 / (k * A0 / 2)
    question = (
        f"The reaction 2A → products is second order in A with $k = {fmt(k)}$ M⁻¹s⁻¹. Starting from "
        f"[A]$_0$ = {q(A0, 'M')}, find [A] after {q(t, 's')}, the first half-life and the second half-life."
    )
    steps = [
        "Second-order integrated rate law: $\\frac{1}{[A]} = \\frac{1}{[A]_0} + kt$.",
        f"$\\frac{{1}}{{[A]}} = \\frac{{1}}{{{fmt(A0)}}} + ({fmt(k)})({t}) = {fmt(1 / A, 4)}$ M⁻¹ → $[A] = {fmt(A)}$ M.",
        f"Half-life $t_{{1/2}} = \\frac{{1}}{{k[A]_0}} = {fmt(th1)}$ s.",
        f"The second half-life starts from $[A]_0/2$: $t_{{1/2}}' = \\frac{{1}}{{k([A]_0/2)}} = {fmt(th2)}$ s — twice as long. "
        "A growing half-life is the signature of second-order kinetics (first-order half-lives are constant).",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$[A] = {fmt(A)}$ M; $t_{{1/2}} = {fmt(th1)}$ s, then ${fmt(th2)}$ s",
            "values": {"k": k, "A0": A0, "t": t, "A": A, "t_half_1": th1, "t_half_2": th2}}


@template("arrhenius_activation_energy", CHEM, PCHEM, "Chemical kinetics", "medium")
def arrhenius_activation_energy(rng):
    Ea = nice(rng, 40, 200, 1)  # kJ/mol
    T1 = nice(rng, 280, 400, 5)
    T2 = T1 + nice(rng, 10, 60, 5)
    k1 = round(rng.uniform(1.0, 9.9), 2) * 10.0 ** rng.randint(-5, -1)
    ratio = math.exp(Ea * 1000 / R_GAS * (1 / T1 - 1 / T2))
    k2 = sig(k1 * ratio)
    Ea_calc = R_GAS * math.log(k2 / k1) / (1 / T1 - 1 / T2) / 1000
    r10 = math.exp(Ea_calc * 1000 / R_GAS * (1 / 298.15 - 1 / 308.15))
    question = (
        f"The rate constant of a reaction is {q(k1)} s⁻¹ at {q(T1, 'K')} and {q(k2)} s⁻¹ at {q(T2, 'K')}. Calculate the "
        "activation energy. By what factor does the rate increase between 25 °C and 35 °C?"
    )
    steps = [
        "Two-point Arrhenius equation: $\\ln\\frac{k_2}{k_1} = \\frac{E_a}{R}\\left(\\frac{1}{T_1} - \\frac{1}{T_2}\\right)$.",
        f"$\\ln\\frac{{{fmt(k2)}}}{{{fmt(k1)}}} = {math.log(k2 / k1):.4f}$; $\\frac{{1}}{{{T1}}} - \\frac{{1}}{{{T2}}} = {fmt(1 / T1 - 1 / T2, 5)}$ K⁻¹.",
        f"$E_a = \\frac{{(8.314)({math.log(k2 / k1):.4f})}}{{{fmt(1 / T1 - 1 / T2, 5)}}} = {fmt(Ea_calc * 1000)}$ J/mol $= {fmt(Ea_calc)}$ kJ/mol.",
        f"From 298.15 K to 308.15 K: $\\frac{{k_{{35}}}}{{k_{{25}}}} = \\exp\\left[\\frac{{E_a}}{{R}}\\left(\\frac{{1}}{{298.15}} - \\frac{{1}}{{308.15}}\\right)\\right] = {fmt(r10)}$.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$E_a \\approx {fmt(Ea_calc)}$ kJ/mol; rate increases ≈{fmt(r10)}× from 25 to 35 °C",
            "values": {"k1": k1, "T1": T1, "k2": k2, "T2": T2, "Ea_kJ": Ea_calc, "ratio_25_35": r10}}


@template("initial_rates_rate_law", CHEM, PCHEM, "Chemical kinetics", "hard")
def initial_rates_rate_law(rng):
    m = rng.randint(0, 2)
    n = rng.randint(0, 2)
    if m == 0 and n == 0:
        m = 1
    k_mant = round(rng.uniform(1.0, 9.9), 2)
    k = k_mant * 10.0 ** rng.randint(-3, 1)
    a1 = pick(rng, [0.010, 0.020, 0.050, 0.10, 0.15, 0.20])
    b1 = pick(rng, [0.010, 0.020, 0.050, 0.10, 0.15, 0.20])
    fa = pick(rng, [2, 3])
    fb = pick(rng, [2, 3, 4])
    exps = [(a1, b1), (a1 * fa, b1), (a1, b1 * fb)]
    rates = [float(f"{k * a ** m * b ** n:.3g}") for a, b in exps]
    ra = rates[1] / rates[0]
    rb = rates[2] / rates[0]
    m_calc = round(math.log(ra) / math.log(fa))
    n_calc = round(math.log(rb) / math.log(fb))
    k_calc = rates[0] / (a1 ** m_calc * b1 ** n_calc)
    units_exp = m + n - 1
    k_unit = "s⁻¹" if units_exp == 0 else f"M⁻{str(units_exp).translate(_SUP) if units_exp > 1 else '¹'}s⁻¹"
    table = "; ".join(
        f"Exp {i + 1}: [A] = {fmt(a, 2)} M, [B] = {fmt(b, 2)} M, rate = {fmt(r)} M/s"
        for i, ((a, b), r) in enumerate(zip(exps, rates))
    )
    order_word = {0: "zero", 1: "first", 2: "second"}
    law = "k" + "".join(f"[{sp}]" + (f"^{e}" if e > 1 else "") for sp, e in (("A", m_calc), ("B", n_calc)) if e)
    question = (
        f"For A + B → products, the following initial rates were measured — {table}. Determine the rate law, "
        "the overall order and the rate constant."
    )
    steps = [
        "Assume rate $= k[A]^m[B]^n$ and compare experiments in which only one concentration changes.",
        f"Exp 2 vs 1: [A] ×{fa}, rate ×{fmt(ra, 3)} → ${fa}^m = {fmt(ra, 3)}$, so $m = {m_calc}$ ({order_word[m_calc]} order in A).",
        f"Exp 3 vs 1: [B] ×{fb}, rate ×{fmt(rb, 3)} → ${fb}^n = {fmt(rb, 3)}$, so $n = {n_calc}$ ({order_word[n_calc]} order in B).",
        f"Rate law: rate $= {law}$ (a zero-order reactant drops out); overall order {m_calc + n_calc}.",
        f"From Exp 1: $k = \\frac{{{fmt(rates[0])}}}{{({fmt(a1, 2)})^{{{m_calc}}}({fmt(b1, 2)})^{{{n_calc}}}}} = {fmt(k_calc)}$ {k_unit}.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"rate $= {law}$ (overall order {m_calc + n_calc}); $k = {fmt(k_calc)}$ {k_unit}",
            "values": {"m": m_calc, "n": n_calc, "k": k_calc, "rates": rates,
                       "A": [e[0] for e in exps], "B": [e[1] for e in exps]}}


# ---------------------------------------------------------------------------
# Electrochemistry
# ---------------------------------------------------------------------------

HALF_CELLS = [  # metal, ion label, n, E° (V)
    ("Mg", "Mg²⁺", 2, -2.37), ("Al", "Al³⁺", 3, -1.66), ("Zn", "Zn²⁺", 2, -0.76), ("Cr", "Cr³⁺", 3, -0.74),
    ("Fe", "Fe²⁺", 2, -0.44), ("Cd", "Cd²⁺", 2, -0.40), ("Ni", "Ni²⁺", 2, -0.26), ("Sn", "Sn²⁺", 2, -0.14),
    ("Pb", "Pb²⁺", 2, -0.13), ("Cu", "Cu²⁺", 2, 0.34), ("Ag", "Ag⁺", 1, 0.80), ("Au", "Au³⁺", 3, 1.50),
]


def _cell(rng):
    while True:
        h1, h2 = rng.sample(HALF_CELLS, 2)
        if abs(h1[3] - h2[3]) >= 0.1:
            break
    an, cat = (h1, h2) if h1[3] < h2[3] else (h2, h1)
    n = an[2] * cat[2] // math.gcd(an[2], cat[2])
    return an, cat, n


def _coef(c):
    return "" if c == 1 else f"{c} "


@template("galvanic_cell_potential", CHEM, PCHEM, "Electrochemistry", "medium")
def galvanic_cell_potential(rng):
    an, cat, n = _cell(rng)
    E = cat[3] - an[3]
    dG = -n * FARADAY * E / 1000
    logK = n * E / 0.05916
    ca, cc = n // an[2], n // cat[2]
    overall = f"{_coef(ca)}{an[0]}(s) + {_coef(cc)}{cat[1]}(aq) → {_coef(ca)}{an[1]}(aq) + {_coef(cc)}{cat[0]}(s)"
    question = (
        f"A galvanic cell is built from a {an[0]}/{an[1]} half-cell ($E^\\circ = {an[3]:+.2f}$ V) and a {cat[0]}/{cat[1]} "
        f"half-cell ($E^\\circ = {cat[3]:+.2f}$ V). Identify the anode and cathode, write the overall reaction and cell "
        "notation, and calculate $E^\\circ_{cell}$, $\\Delta G^\\circ$ and $K$ at 25 °C."
    )
    steps = [
        f"The half-cell with the higher reduction potential is reduced: cathode = {cat[0]} ({cat[3]:+.2f} V); "
        f"anode = {an[0]} ({an[3]:+.2f} V), which is oxidized.",
        f"Half-reactions: anode {an[0]} → {an[1]} + {an[2]}e⁻; cathode {cat[1]} + {cat[2]}e⁻ → {cat[0]}. "
        f"Electrons transferred: $n = {n}$.",
        f"Overall: {overall}. Cell notation: {an[0]}(s) | {an[1]}(aq) ‖ {cat[1]}(aq) | {cat[0]}(s).",
        f"$E^\\circ_{{cell}} = E^\\circ_{{cathode}} - E^\\circ_{{anode}} = {cat[3]:+.2f} - ({an[3]:+.2f}) = {E:.2f}$ V "
        "(potentials are not multiplied by stoichiometric coefficients).",
        f"$\\Delta G^\\circ = -nFE^\\circ = -({n})(96485)({E:.2f}) = {fmt(dG * 1000)}$ J $= {dG:.0f}$ kJ.",
        f"$\\log_{{10}}K = \\frac{{nE^\\circ}}{{0.05916}} = {logK:.1f}$, so $K \\approx 10^{{{logK:.1f}}}$ — the reaction goes essentially to completion.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"anode {an[0]}, cathode {cat[0]}; $E^\\circ = {E:.2f}$ V; $\\Delta G^\\circ = {dG:.0f}$ kJ; $K \\approx 10^{{{logK:.1f}}}$",
            "values": {"anode": an[0], "cathode": cat[0], "n": n, "E_cell": E, "dG_kJ": dG, "log10K": logK}}


@template("nernst_equation", CHEM, PCHEM, "Electrochemistry", "hard")
def nernst_equation(rng):
    an, cat, n = _cell(rng)
    E0 = cat[3] - an[3]
    ca, cc = n // an[2], n // cat[2]
    c_an = pick(rng, [0.0010, 0.010, 0.050, 0.10, 0.50, 1.0, 2.0])
    c_cat = pick(rng, [0.0010, 0.010, 0.050, 0.10, 0.50, 1.0, 2.0])
    Q = c_an ** ca / c_cat ** cc
    E = E0 - 0.05916 / n * math.log10(Q)
    question = (
        f"Calculate the potential at 25 °C of the cell {an[0]}(s) | {an[1]}({fmt(c_an, 2)} M) ‖ {cat[1]}({fmt(c_cat, 2)} M) | "
        f"{cat[0]}(s). Standard reduction potentials: {an[1]}/{an[0]} {an[3]:+.2f} V, {cat[1]}/{cat[0]} {cat[3]:+.2f} V."
    )
    steps = [
        f"$E^\\circ_{{cell}} = {cat[3]:+.2f} - ({an[3]:+.2f}) = {E0:.2f}$ V.",
        f"Overall reaction: {_coef(ca)}{an[0]} + {_coef(cc)}{cat[1]} → {_coef(ca)}{an[1]} + {_coef(cc)}{cat[0]}, with $n = {n}$.",
        f"Reaction quotient (solids omitted): $Q = \\frac{{[\\text{{{an[1]}}}]^{{{ca}}}}}{{[\\text{{{cat[1]}}}]^{{{cc}}}}} = {fmt(Q)}$.",
        f"Nernst equation: $E = E^\\circ - \\frac{{0.05916}}{{n}}\\log Q = {E0:.2f} - \\frac{{0.05916}}{{{n}}}\\log({fmt(Q)}) = {E:.3f}$ V.",
        "Increasing the cathode-ion concentration or decreasing the anode-ion concentration raises the cell potential.",
    ]
    return {"question": question, "steps": steps, "answer": f"$E = {E:.3f}$ V",
            "values": {"E0": E0, "n": n, "c_anode_ion": c_an, "c_cathode_ion": c_cat, "Q": Q, "E": E}}


@template("electrolysis_faraday", CHEM, PCHEM, "Electrochemistry", "medium")
def electrolysis_faraday(rng):
    metal, ion, nz, context = pick(rng, [
        ("Cu", "Cu²⁺", 2, "copper is electroplated from a CuSO₄ bath"),
        ("Ag", "Ag⁺", 1, "silver is plated from a silver nitrate solution"),
        ("Ni", "Ni²⁺", 2, "nickel is plated from a NiSO₄ solution"),
        ("Zn", "Zn²⁺", 2, "zinc is deposited during galvanizing"),
        ("Cr", "Cr³⁺", 3, "chromium is plated from a Cr³⁺ bath"),
        ("Au", "Au³⁺", 3, "gold is plated from an Au³⁺ solution"),
        ("Al", "Al³⁺", 3, "aluminum is produced from molten Al₂O₃ (Hall–Héroult process)"),
    ])
    M = ATOMIC_MASS[metal]
    if rng.random() < 0.5:
        I = nice(rng, 0.5, 20.0, 0.5)
        t_min = nice(rng, 10, 240, 5)
        Q = I * t_min * 60
        m = Q / FARADAY / nz * M
        question = f"When {context}, a current of {q(I, 'A')} flows for {q(t_min, 'min')}. What mass of {metal} is deposited?"
        steps = [
            f"Charge: $Q = It = ({fmt(I)})({t_min} \\times 60\\text{{ s}}) = {fmt(Q)}$ C.",
            f"Moles of electrons: $Q/F = {fmt(Q)}/96485 = {fmt(Q / FARADAY)}$ mol.",
            f"{ion} + {nz}e⁻ → {metal}, so moles of {metal} $= {fmt(Q / FARADAY)}/{nz} = {fmt(Q / FARADAY / nz)}$ mol.",
            f"Mass: $({fmt(Q / FARADAY / nz)})({M}) = {fmt(m)}$ g.",
        ]
        answer = f"${fmt(m)}$ g of {metal}"
        values = {"I": I, "t_s": t_min * 60, "n": nz, "M": M, "mass": m}
    else:
        m = nice(rng, 0.5, 50.0, 0.5)
        I = nice(rng, 1.0, 25.0, 0.5)
        t = m / M * nz * FARADAY / I
        question = f"When {context}, how long (in minutes) must a current of {q(I, 'A')} flow to deposit {q(m, 'g')} of {metal}?"
        steps = [
            f"Moles of {metal}: ${fmt(m)}/{M} = {fmt(m / M)}$ mol.",
            f"Each {ion} needs {nz} electron{'s' if nz > 1 else ''}: moles e⁻ $= {fmt(m / M * nz)}$ mol.",
            f"Charge: $Q = nF = {fmt(m / M * nz)} \\times 96485 = {fmt(m / M * nz * FARADAY)}$ C.",
            f"Time: $t = Q/I = {fmt(t)}$ s $= {fmt(t / 60)}$ min.",
        ]
        answer = f"$t = {fmt(t / 60)}$ min"
        values = {"I": I, "t_s": t, "n": nz, "M": M, "mass": m}
    return {"question": question, "steps": steps, "answer": answer, "values": values}
