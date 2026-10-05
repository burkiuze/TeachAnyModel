"""Additional Chemistry templates: thermochemistry, equilibrium, acids and bases, solutions, gases,
solids, kinetics, electrochemistry and instrumental analysis.

General chemistry: Hess's law, the reaction quotient, hydrolysis of salts, precipitation on mixing,
Dalton's law (gas collected over water, gas mixtures), concentration units and the density of cubic
crystals.

Physical chemistry: bomb calorimetry, Kp/Kc interconversion, the van 't Hoff equation, diprotic acids,
zero-order kinetics, Raoult's law, the van der Waals equation, battery capacity and concentration
cells.

Analytical chemistry: buffer preparation, trace (ppm/ppb) analysis of drinking water, Beer–Lambert
calibration and the method of standard additions.
"""

import math
import re
from fractions import Fraction as Fr

from .chemistry import ATOMIC_MASS, parse_formula, pretty
from .common import FARADAY, N_A, R_GAS, fmt, nice, pick, sig, template

CHEM = "Chemistry"
GEN = "General Chemistry"
PCHEM = "Physical Chemistry"
ANALYT = "Analytical Chemistry"

R_LATM = 0.08206          # gas constant, L atm / (mol K)
KW = 1.0e-14              # ion product of water at 25 °C
T_STD = 298.15            # K
TORR_PER_ATM = 760.0
M_WATER = 18.015          # g/mol

# Atomic masses (g/mol) for elements that the chemistry module does not list
MASSES = dict(ATOMIC_MASS)
MASSES.update({"Po": 209.0, "Mo": 95.95, "W": 183.84, "V": 50.942, "Cs": 132.905, "Pt": 195.08,
               "Pd": 106.42, "As": 74.922, "Se": 78.971, "U": 238.03, "Xe": 131.29})


def mm(formula):
    """Molar mass from the formula, including hydrates (``CH3COONa·3H2O``)."""
    return sum(MASSES[el] * n for el, n in parse_formula(formula).items())


def ex(x, min_sig=3):
    """Shortest display (at least ``min_sig`` significant figures) that shows ``x`` exactly."""
    if isinstance(x, int) and abs(x) < 100000:
        return str(x)
    x = float(x)
    if x == 0:
        return "0"
    for s in range(min_sig, 11):
        if math.isclose(float(f"{x:.{s}g}"), x, rel_tol=1e-12):
            return fmt(x, s)
    return fmt(x, 10)


def qx(x, unit="", min_sig=3):
    """Exact quantity: ``$x$ unit`` with ``x`` shown to as many figures as it has."""
    s = f"${ex(x, min_sig)}$"
    return f"{s} {unit}" if unit else s


def mant(rng, lo_exp, hi_exp, digits=2):
    """Random value d.d × 10^e with ``digits`` significant figures."""
    return sig(rng.uniform(1.0, 9.9) * 10.0 ** rng.randint(lo_exp, hi_exp), digits)


def ph(x):
    return f"{x:.2f}"


def kj(x):
    """Enthalpy in kJ with one decimal (two if needed)."""
    return f"{x:.1f}" if abs(round(x, 1) - x) < 1e-9 else f"{x:.2f}"


def tex(formula, charge=""):
    """``NH3`` -> ``\\text{NH}_{3}`` for use inside $...$."""
    out = "".join(f"\\text{{{a}}}" + (f"_{{{d}}}" if d else "") for a, d in re.findall(r"([A-Za-z()]+)(\d*)", formula))
    return out + (f"^{{{charge}}}" if charge else "")


def lsq(xs, ys):
    """Least-squares slope, intercept and r²."""
    n = len(xs)
    xb, yb = sum(xs) / n, sum(ys) / n
    sxx = sum((x - xb) ** 2 for x in xs)
    sxy = sum((x - xb) * (y - yb) for x, y in zip(xs, ys))
    syy = sum((y - yb) ** 2 for y in ys)
    m = sxy / sxx
    return m, yb - m * xb, sxy * sxy / (sxx * syy)


# ---------------------------------------------------------------------------
# Reaction utilities
# ---------------------------------------------------------------------------


def parse_rxn(text):
    """``"C(graphite) + 1/2 O2(g) -> CO(g)"`` -> ([(coef, formula, phase), ...], [...])."""
    def side(s):
        out = []
        for term in s.split(" + "):
            parts = term.strip().split(" ")
            coef = Fr(parts[0]) if len(parts) == 2 else Fr(1)
            m = re.match(r"^(.+)\(([a-z]+)\)$", parts[-1])
            out.append((coef, m.group(1), m.group(2)))
        return out

    left, right = text.split("->")
    return side(left), side(right)


def coef_txt(c):
    c = Fr(c)
    if c == 1:
        return ""
    if c.denominator == 1:
        return f"{c.numerator} "
    return f"{c.numerator}/{c.denominator} "


def frac_txt(c):
    """Exact rational as text: 2, -1, 1/2, -5/2."""
    c = Fr(c)
    return str(c.numerator) if c.denominator == 1 else f"{c.numerator}/{c.denominator}"


def species_txt(formula, phase):
    return f"{pretty(formula)}({phase})"


def rxn_txt(rxn, scale=Fr(1), arrow="→"):
    left, right = rxn
    scale = Fr(scale)
    if scale < 0:
        left, right, scale = right, left, -scale

    def side(items):
        return " + ".join(f"{coef_txt(c * scale)}{species_txt(f, p)}" for c, f, p in items)

    return f"{side(left)} {arrow} {side(right)}"


def rxn_vec(rxn):
    vec = {}
    for sign, items in ((-1, rxn[0]), (1, rxn[1])):
        for c, f, p in items:
            key = f"{f}({p})"
            vec[key] = vec.get(key, Fr(0)) + sign * c
    return vec


def dn_gas(rxn):
    return sum(c for c, f, p in rxn[1] if p == "g") - sum(c for c, f, p in rxn[0] if p == "g")


def solve_combination(vectors, target):
    """Exact multipliers c_i with sum c_i * vectors[i] == target (Gauss–Jordan on fractions)."""
    species = sorted(set(target).union(*vectors))
    n = len(vectors)
    rows = [[v.get(s, Fr(0)) for v in vectors] + [target.get(s, Fr(0))] for s in species]
    r = 0
    for c in range(n):
        p = next((i for i in range(r, len(rows)) if rows[i][c] != 0), None)
        if p is None:
            raise ValueError("reactions are not independent")
        rows[r], rows[p] = rows[p], rows[r]
        pv = rows[r][c]
        rows[r] = [x / pv for x in rows[r]]
        for i in range(len(rows)):
            if i != r and rows[i][c] != 0:
                f = rows[i][c]
                rows[i] = [a - f * b for a, b in zip(rows[i], rows[r])]
        r += 1
    if any(rows[i][n] != 0 for i in range(r, len(rows))):
        raise ValueError("target cannot be obtained from the given reactions")
    return [rows[i][n] for i in range(n)]


# ---------------------------------------------------------------------------
# Thermochemistry
# ---------------------------------------------------------------------------

HESS_SYSTEMS = [
    ("C(graphite) + 2 H2(g) -> CH4(g)",
     [("C(graphite) + O2(g) -> CO2(g)", -393.5), ("H2(g) + 1/2 O2(g) -> H2O(l)", -285.8),
      ("CH4(g) + 2 O2(g) -> CO2(g) + 2 H2O(l)", -890.3)]),
    ("2 C(graphite) + H2(g) -> C2H2(g)",
     [("C(graphite) + O2(g) -> CO2(g)", -393.5), ("H2(g) + 1/2 O2(g) -> H2O(l)", -285.8),
      ("2 C2H2(g) + 5 O2(g) -> 4 CO2(g) + 2 H2O(l)", -2598.8)]),
    ("C(graphite) + 1/2 O2(g) -> CO(g)",
     [("C(graphite) + O2(g) -> CO2(g)", -393.5), ("CO(g) + 1/2 O2(g) -> CO2(g)", -283.0)]),
    ("N2(g) + 2 O2(g) -> 2 NO2(g)",
     [("N2(g) + O2(g) -> 2 NO(g)", 180.6), ("2 NO(g) + O2(g) -> 2 NO2(g)", -114.1)]),
    ("2 S(s) + 3 O2(g) -> 2 SO3(g)",
     [("S(s) + O2(g) -> SO2(g)", -296.8), ("2 SO2(g) + O2(g) -> 2 SO3(g)", -197.8)]),
    ("C2H4(g) + H2(g) -> C2H6(g)",
     [("C2H4(g) + 3 O2(g) -> 2 CO2(g) + 2 H2O(l)", -1411.0), ("H2(g) + 1/2 O2(g) -> H2O(l)", -285.8),
      ("2 C2H6(g) + 7 O2(g) -> 4 CO2(g) + 6 H2O(l)", -3119.6)]),
    ("3 C(graphite) + 4 H2(g) -> C3H8(g)",
     [("C(graphite) + O2(g) -> CO2(g)", -393.5), ("H2(g) + 1/2 O2(g) -> H2O(l)", -285.8),
      ("C3H8(g) + 5 O2(g) -> 3 CO2(g) + 4 H2O(l)", -2219.9)]),
    ("C(graphite) -> C(diamond)",
     [("C(graphite) + O2(g) -> CO2(g)", -393.5), ("C(diamond) + O2(g) -> CO2(g)", -395.4)]),
    ("2 H2O2(l) -> 2 H2O(l) + O2(g)",
     [("H2(g) + O2(g) -> H2O2(l)", -187.8), ("H2(g) + 1/2 O2(g) -> H2O(l)", -285.8)]),
    ("CaO(s) + CO2(g) -> CaCO3(s)",
     [("Ca(s) + 1/2 O2(g) -> CaO(s)", -635.1), ("C(graphite) + O2(g) -> CO2(g)", -393.5),
      ("Ca(s) + C(graphite) + 3/2 O2(g) -> CaCO3(s)", -1206.9)]),
    ("N2H4(l) + O2(g) -> N2(g) + 2 H2O(l)",
     [("N2(g) + 2 H2(g) -> N2H4(l)", 50.6), ("H2(g) + 1/2 O2(g) -> H2O(l)", -285.8)]),
    ("C2H4(g) + H2O(l) -> C2H5OH(l)",
     [("C2H4(g) + 3 O2(g) -> 2 CO2(g) + 2 H2O(l)", -1411.0),
      ("C2H5OH(l) + 3 O2(g) -> 2 CO2(g) + 3 H2O(l)", -1366.8)]),
    ("C(graphite) + H2O(g) -> CO(g) + H2(g)",
     [("C(graphite) + O2(g) -> CO2(g)", -393.5), ("2 CO(g) + O2(g) -> 2 CO2(g)", -566.0),
      ("2 H2(g) + O2(g) -> 2 H2O(g)", -483.6)]),
    ("6 C(graphite) + 3 H2(g) -> C6H6(l)",
     [("C(graphite) + O2(g) -> CO2(g)", -393.5), ("H2(g) + 1/2 O2(g) -> H2O(l)", -285.8),
      ("2 C6H6(l) + 15 O2(g) -> 12 CO2(g) + 6 H2O(l)", -6534.8)]),
    ("P4(s) + 10 Cl2(g) -> 4 PCl5(s)",
     [("P4(s) + 6 Cl2(g) -> 4 PCl3(l)", -1279.0), ("PCl3(l) + Cl2(g) -> PCl5(s)", -123.8)]),
]


def _signed_pairs(vec):
    return [[k, float(v)] for k, v in sorted(vec.items()) if v != 0]


@template("hess_law_combine_reactions", CHEM, GEN, "Hess's law", "medium")
def hess_law_combine_reactions(rng):
    target_txt, given = pick(rng, HESS_SYSTEMS)
    given = list(given)
    rng.shuffle(given)
    target = parse_rxn(target_txt)
    rxns = [parse_rxn(t) for t, _ in given]
    dHs = [dh for _, dh in given]
    vecs = [rxn_vec(r) for r in rxns]
    tvec = rxn_vec(target)
    mults = solve_combination(vecs, tvec)
    if any(c == 0 for c in mults):
        raise ValueError("unused reaction in Hess system")
    terms = [float(c) * dh for c, dh in zip(mults, dHs)]
    dH = sum(terms)

    # quantity part: a species of the target equation
    side_name, (coef, f, p) = pick(rng, [("reactant", it) for it in target[0]] + [("product", it) for it in target[1]])
    M = mm(f)
    m = nice(rng, 1.0, 200.0, 0.5)
    n_rxn = m / M / float(coef)
    heat = dH * n_rxn
    verb = "is formed" if side_name == "product" else "reacts"

    listing = "; ".join(f"({i}) {rxn_txt(r)}, $\\Delta H^\\circ = {kj(dh)}$ kJ" for i, (r, dh) in enumerate(zip(rxns, dHs), 1))
    question = (
        f"Use Hess's law and the thermochemical equations {listing} to calculate $\\Delta H^\\circ$ for "
        f"{rxn_txt(target)}. How much heat is released or absorbed when {qx(m, 'g')} of {species_txt(f, p)} {verb} "
        "according to this equation?"
    )
    steps = [
        "Enthalpy is a state function, so the given equations may be reversed and scaled until they add up to the "
        "target equation: reversing an equation changes the sign of $\\Delta H^\\circ$, and multiplying it by a factor "
        "multiplies $\\Delta H^\\circ$ by the same factor."
    ]
    others = [set(k for k, v in vec.items() if v != 0) for vec in vecs]
    for i, (r, c, dh, term) in enumerate(zip(rxns, mults, dHs, terms), 1):
        mine = set(k for k, v in vecs[i - 1].items() if v != 0)
        unique = [k for k in mine if k in tvec and all(k not in o for j, o in enumerate(others) if j != i - 1)]
        if c == 1:
            how = "is used as written"
        elif c == -1:
            how = "is reversed"
        elif c > 0:
            how = f"is multiplied by {coef_txt(c).strip()}"
        else:
            how = f"is reversed and multiplied by {coef_txt(-c).strip()}"
        if unique:
            key = sorted(unique)[0]
            kf, kp = re.match(r"^(.+)\(([a-z]+)\)$", key).groups()
            need = tvec[key]
            where = "product" if need > 0 else "reactant"
            why = f" so that {species_txt(kf, kp)} appears as a {where}" + (
                f" with coefficient {coef_txt(abs(need)).strip()}" if abs(need) != 1 else "")
        else:
            why = " so that the intermediate species cancel"
        dh_txt = f"{kj(dh)}" if c == 1 else f"({frac_txt(c)})({kj(dh)}) = {kj(term)}"
        steps.append(f"Equation ({i}) {how}{why}: {rxn_txt(r, c)}, $\\Delta H^\\circ = {dh_txt}$ kJ.")
    total = {}
    for c, vec in zip(mults, vecs):
        for k, v in vec.items():
            total[k] = total.get(k, Fr(0)) + c * v
    cancelled = sorted({k for vec in vecs for k in vec} - {k for k, v in tvec.items() if v != 0})
    if any(total.get(k, 0) != tvec.get(k, 0) for k in set(total) | set(tvec)):
        raise ValueError("Hess combination failed")
    canc_txt = ", ".join(species_txt(*re.match(r"^(.+)\(([a-z]+)\)$", k).groups()) for k in cancelled)
    steps.append(
        f"Adding the manipulated equations, {canc_txt} cancel{'s' if len(cancelled) == 1 else ''} between the two sides "
        f"and what remains is the target equation, {rxn_txt(target)}."
        if cancelled else f"Adding the manipulated equations gives the target equation, {rxn_txt(target)}."
    )
    steps.append(
        "$\\Delta H^\\circ = " + " + ".join(f"({kj(t)})" for t in terms) + f" = {kj(dH)}$ kJ, so the reaction is "
        + ("exothermic." if dH < 0 else "endothermic.")
    )
    steps.append(
        f"Moles of {pretty(f)}: $n = {ex(m)}/{M:.2f} = {fmt(m / M, 4)}$ mol; the equation involves "
        f"{coef_txt(coef).strip() or '1'} mol of it, i.e. ${fmt(n_rxn, 4)}$ mol of reaction as written."
    )
    steps.append(
        f"Heat: $q = ({fmt(n_rxn, 4)})({kj(dH)}\\text{{ kJ}}) = {fmt(heat)}$ kJ — "
        + (f"${fmt(-heat)}$ kJ of heat is released." if heat < 0 else f"${fmt(heat)}$ kJ of heat is absorbed.")
    )
    answer = (f"$\\Delta H^\\circ = {kj(dH)}$ kJ; ${fmt(abs(heat))}$ kJ "
              f"{'released' if heat < 0 else 'absorbed'} for {ex(m)} g of {pretty(f)}")
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"target_rxn": _signed_pairs(tvec), "given_rxns": [_signed_pairs(v) for v in vecs],
                       "dH_given": dHs, "multipliers": [float(c) for c in mults], "dH": dH,
                       "species": f"{f}({p})", "formula": f, "coef": float(coef), "mass": m, "M": M,
                       "heat_kJ": heat}}


BOMB_FUELS = [  # formula, name, phase, tabulated ΔcH° (kJ/mol, 298 K, H2O(l))
    ("C10H8", "naphthalene", "s", -5156.3), ("C12H22O11", "sucrose", "s", -5643.4),
    ("C6H12O6", "glucose", "s", -2803.0), ("C2H5OH", "ethanol", "l", -1366.8),
    ("C14H10", "anthracene", "s", -7061.0), ("C6H5OH", "phenol", "s", -3053.5),
    ("C7H6O3", "salicylic acid", "s", -3022.2), ("C8H18", "octane", "l", -5470.0),
    ("C6H12", "cyclohexane", "l", -3919.6), ("C7H6O2", "benzoic acid", "s", -3226.9),
    ("C6H14", "hexane", "l", -4163.2),
]
BENZOIC_KJ_PER_G = 26.43   # energy released per gram of benzoic acid burned in a bomb
RT_KJ = 8.314e-3 * T_STD


@template("bomb_calorimetry_combustion", CHEM, PCHEM, "Bomb calorimetry", "hard")
def bomb_calorimetry_combustion(rng):
    f, name, phase, dHc_lit = pick(rng, BOMB_FUELS)
    calibrate = f != "C7H6O2" and rng.random() < 0.55
    counts = parse_formula(f)
    x, y, z = counts.get("C", 0), counts.get("H", 0), counts.get("O", 0)
    o2 = Fr(x) + Fr(y, 4) - Fr(z, 2)
    dn = Fr(z, 2) - Fr(y, 4)
    M = mm(f)
    dU_lit = dHc_lit - float(dn) * RT_KJ
    C_true = nice(rng, 8.50, 11.50, 0.01)
    m = nice(rng, 0.5000, 1.1000, 0.0001)
    dT = round(-dU_lit * m / M / C_true, 3)
    steps = []
    if calibrate:
        mb = nice(rng, 0.8000, 1.2000, 0.0001)
        dTb = round(BENZOIC_KJ_PER_G * mb / C_true, 3)
        C = BENZOIC_KJ_PER_G * mb / dTb
        calib_q = (
            f"The calorimeter is first calibrated by burning ${mb:.4f}$ g of benzoic acid (which releases "
            f"{BENZOIC_KJ_PER_G} kJ per gram under bomb conditions); the temperature rises by ${dTb:.3f}$ °C. "
        )
        steps.append(
            f"Calibration: heat released by the benzoic acid $= ({BENZOIC_KJ_PER_G}\\text{{ kJ/g}})({mb:.4f}\\text{{ g}}) = "
            f"{fmt(BENZOIC_KJ_PER_G * mb, 4)}$ kJ, so $C_{{cal}} = \\frac{{{fmt(BENZOIC_KJ_PER_G * mb, 4)}}}{{{dTb:.3f}}} = "
            f"{fmt(C, 4)}$ kJ/°C."
        )
        values_extra = {"m_benzoic": mb, "dT_benzoic": dTb}
    else:
        C = C_true
        calib_q = f"The heat capacity of the calorimeter (bomb plus water) is {qx(C, 'kJ/°C')}. "
        values_extra = {"m_benzoic": None, "dT_benzoic": None}
    q_cal = C * dT
    dU_g = -q_cal / m
    dU = dU_g * M
    dH = dU + float(dn) * RT_KJ
    eqn = (f"{pretty(f)}({phase}) + {coef_txt(o2)}O₂(g) → {coef_txt(x)}CO₂(g) + {coef_txt(Fr(y, 2))}H₂O(l)")
    question = (
        f"{calib_q}Then ${m:.4f}$ g of {name} ({pretty(f)}, {'solid' if phase == 's' else 'liquid'}) is burned in excess "
        f"oxygen in the same bomb calorimeter and the temperature rises by ${dT:.3f}$ °C. Calculate the energy of "
        f"combustion $\\Delta_c U$ of {name} in kJ/g and kJ/mol, and convert it to the enthalpy of combustion "
        "$\\Delta_c H$ at about 298 K. Neglect the heat from the ignition wire and assume the water formed is liquid."
    )
    steps += [
        f"Heat absorbed by the calorimeter: $q_{{cal}} = C_{{cal}}\\Delta T = ({fmt(C, 4)})({dT:.3f}) = {fmt(q_cal, 4)}$ kJ. "
        "The bomb is sealed, so the reaction occurs at constant volume and the heat it releases equals $-\\Delta U$: "
        "$q_{rxn} = -q_{cal}$.",
        f"Per gram: $\\Delta_c U = -\\frac{{{fmt(q_cal, 4)}\\text{{ kJ}}}}{{{m:.4f}\\text{{ g}}}} = {fmt(dU_g, 4)}$ kJ/g.",
        f"Molar mass of {pretty(f)}: ${M:.2f}$ g/mol, so $\\Delta_c U = ({fmt(dU_g, 4)})({M:.2f}) = {fmt(dU, 4)}$ kJ/mol.",
        f"Balanced equation: {eqn}. Gas moles change by $\\Delta n_{{gas}} = {x} - {frac_txt(o2)} = "
        f"{frac_txt(dn)}$ (the {'solid' if phase == 's' else 'liquid'} fuel and "
        "liquid water do not count).",
        f"$\\Delta_c H = \\Delta_c U + \\Delta n_{{gas}}RT = {fmt(dU, 4)} + ({float(dn):g})(8.314\\times10^{{-3}})(298.15) = "
        f"{fmt(dH, 4)}$ kJ/mol.",
        f"Check: the tabulated $\\Delta_c H^\\circ$ of {name} is about ${kj(dHc_lit)}$ kJ/mol, in good agreement. "
        + ("Because $\\Delta n_{gas} = 0$, $\\Delta H$ and $\\Delta U$ are equal here." if dn == 0 else
           "The $\\Delta n_{gas}RT$ correction is small (a few kJ/mol) compared with $\\Delta_c U$."),
    ]
    answer = (f"$\\Delta_c U = {fmt(dU_g, 4)}$ kJ/g $= {fmt(dU, 4)}$ kJ/mol; $\\Delta_c H = {fmt(dH, 4)}$ kJ/mol")
    values = {"formula": f, "mass": m, "dT": dT, "C_cal": C, "calibrated": calibrate, "M": M,
              "dU_per_g": dU_g, "dU_molar": dU, "dn_gas": float(dn), "dH_molar": dH}
    values.update(values_extra)
    return {"question": question, "steps": steps, "answer": answer, "values": values,
            "difficulty": "hard" if calibrate else "medium"}


# ---------------------------------------------------------------------------
# Equilibrium
# ---------------------------------------------------------------------------

EQUILIBRIA = {  # equation, ΔH° (kJ/mol), ΔS° (J/(mol K)) from standard thermodynamic tables
    "ammonia": ("N2(g) + 3 H2(g) -> 2 NH3(g)", -92.2, -198.7),
    "sulfur_trioxide": ("2 SO2(g) + O2(g) -> 2 SO3(g)", -197.8, -187.9),
    "dinitrogen_tetroxide": ("N2O4(g) -> 2 NO2(g)", 57.2, 175.8),
    "phosphorus_pentachloride": ("PCl5(g) -> PCl3(g) + Cl2(g)", 87.9, 170.2),
    "nitric_oxide": ("2 NO(g) + O2(g) -> 2 NO2(g)", -114.1, -146.5),
    "hydrogen_iodide": ("H2(g) + I2(g) -> 2 HI(g)", -9.4, 21.8),
    "methanol": ("CO(g) + 2 H2(g) -> CH3OH(g)", -90.5, -219.2),
    "boudouard": ("C(s) + CO2(g) -> 2 CO(g)", 172.5, 175.9),
    "ammonium_chloride": ("NH4Cl(s) -> NH3(g) + HCl(g)", 176.2, 285.1),
    "nitrosyl_chloride": ("2 NOCl(g) -> 2 NO(g) + Cl2(g)", 77.2, 121.3),
    "steam_reforming": ("CH4(g) + H2O(g) -> CO(g) + 3 H2(g)", 206.1, 214.7),
    "water_gas_shift": ("CO(g) + H2O(g) -> CO2(g) + H2(g)", -41.2, -42.0),
    "calcium_carbonate": ("CaCO3(s) -> CaO(s) + CO2(g)", 178.3, 160.5),
}


def k_model(key, T):
    """Thermodynamic K (pressures in bar ≈ atm) assuming ΔH° and ΔS° independent of T."""
    _, dH, dS = EQUILIBRIA[key]
    return math.exp(-(dH * 1000 - T * dS) / (R_GAS * T))


def solids_note(rxn):
    solids = [species_txt(f, p) for side in rxn for c, f, p in side if p in ("s", "l")]
    return solids


KPKC_CASES = [
    ("ammonia", (500, 800, 10)), ("sulfur_trioxide", (700, 1100, 10)), ("dinitrogen_tetroxide", (280, 400, 5)),
    ("phosphorus_pentachloride", (400, 600, 10)), ("nitric_oxide", (500, 900, 10)), ("hydrogen_iodide", (500, 800, 10)),
    ("methanol", (400, 600, 10)), ("boudouard", (900, 1300, 10)), ("ammonium_chloride", (520, 680, 10)),
    ("nitrosyl_chloride", (400, 700, 10)), ("steam_reforming", (850, 1200, 10)), ("water_gas_shift", (600, 1000, 10)),
    ("calcium_carbonate", (900, 1300, 10)),
]


@template("kp_kc_interconversion", CHEM, PCHEM, "Chemical equilibrium", "easy")
def kp_kc_interconversion(rng):
    key, (lo, hi, step) = pick(rng, KPKC_CASES)
    rxn = parse_rxn(EQUILIBRIA[key][0])
    dn = int(dn_gas(rxn))
    T = nice(rng, lo, hi, step)
    RT = R_LATM * T
    Kp_true = k_model(key, T)
    if rng.random() < 0.5:
        given, want = "K_c", "K_p"
        Kc = sig(Kp_true * RT ** (-dn), 3)
        Kp = Kc * RT ** dn
        K_given, K_res = Kc, Kp
    else:
        given, want = "K_p", "K_c"
        Kp = sig(Kp_true, 3)
        Kc = Kp * RT ** (-dn)
        K_given, K_res = Kp, Kc
    variant = pick(rng, ["none", "none", "reverse", "double", "half"])
    power = {"none": None, "reverse": -1, "double": 2, "half": 0.5}[variant]
    eq = rxn_txt(rxn, arrow="⇌")
    extra_q = ""
    if variant != "none":
        scale = {"reverse": Fr(-1), "double": Fr(2), "half": Fr(1, 2)}[variant]
        var_eq = rxn_txt(rxn, scale, arrow="⇌")
        extra_q = f" Also give ${want}$ at this temperature for the equation written as {var_eq}."
    question = (
        f"For the equilibrium {eq}, ${given} = {fmt(K_given, 3)}$ at {qx(T, 'K')}. Calculate ${want}$ at the same "
        f"temperature, with pressures in atm and concentrations in mol/L.{extra_q}"
    )
    gp = sum(c for c, f, p in rxn[1] if p == "g")
    gr = sum(c for c, f, p in rxn[0] if p == "g")
    solids = solids_note(rxn)
    steps = [
        "For an ideal-gas equilibrium $P_i = [i]RT$, which gives $K_p = K_c(RT)^{\\Delta n}$ with "
        "$\\Delta n$ = (moles of gaseous products) − (moles of gaseous reactants) and $R = 0.08206$ L·atm/(mol·K).",
        f"$\\Delta n = {gp} - {gr} = {dn}$"
        + (f" (the condensed phase{'s' if len(solids) > 1 else ''} {', '.join(solids)} "
           f"{'do' if len(solids) > 1 else 'does'} not appear in $K$ and {'are' if len(solids) > 1 else 'is'} not counted)."
           if solids else "."),
    ]
    if dn == 0:
        steps.append(f"Because $\\Delta n = 0$, $(RT)^0 = 1$ and ${want} = {given} = {fmt(K_res, 3)}$.")
    else:
        steps.append(f"$RT = (0.08206)({ex(T)}) = {fmt(RT, 4)}$.")
        if given == "K_c":
            steps.append(f"$K_p = K_c(RT)^{{{dn}}} = ({fmt(Kc, 3)})({fmt(RT, 4)})^{{{dn}}} = {fmt(Kp, 3)}$.")
        else:
            steps.append(f"$K_c = K_p(RT)^{{{-dn}}} = ({fmt(Kp, 3)})({fmt(RT, 4)})^{{{-dn}}} = {fmt(Kc, 3)}$.")
        steps.append(
            f"Check: $RT > 1$ and $\\Delta n {'>' if dn > 0 else '<'} 0$, so $K_p$ must be "
            f"{'larger' if dn > 0 else 'smaller'} than $K_c$ — it is."
        )
    K_var = None
    if power is not None:
        K_var = K_res ** power
        rule = {"reverse": f"reversing an equation inverts $K$: ${want}' = 1/{fmt(K_res, 3)} = {fmt(K_var, 3)}$",
                "double": f"doubling every coefficient squares $K$: ${want}' = ({fmt(K_res, 3)})^2 = {fmt(K_var, 3)}$",
                "half": f"halving every coefficient takes the square root of $K$: ${want}' = \\sqrt{{{fmt(K_res, 3)}}} = "
                        f"{fmt(K_var, 3)}$"}[variant]
        steps.append(f"For the modified equation, {rule}.")
    answer = f"${want} = {fmt(K_res, 3)}$" + (f"; modified equation: ${want}' = {fmt(K_var, 3)}$" if K_var is not None else "")
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"reaction": key, "T": T, "dn": dn, "given": given, "K_given": K_given, "Kc": Kc, "Kp": Kp,
                       "variant": variant, "power": power, "K_variant": K_var}}


QK_CASES = [
    ("ammonia", (600, 800, 10)), ("sulfur_trioxide", (900, 1100, 10)), ("dinitrogen_tetroxide", (300, 380, 5)),
    ("phosphorus_pentachloride", (450, 550, 10)), ("hydrogen_iodide", (600, 800, 10)), ("water_gas_shift", (700, 1000, 10)),
    ("methanol", (450, 550, 10)), ("boudouard", (950, 1150, 10)), ("nitrosyl_chloride", (450, 600, 10)),
    ("steam_reforming", (900, 1100, 10)),
]


@template("reaction_quotient_direction", CHEM, GEN, "Reaction quotient", "medium")
def reaction_quotient_direction(rng):
    key, (lo, hi, step) = pick(rng, QK_CASES)
    rxn = parse_rxn(EQUILIBRIA[key][0])
    dn = int(dn_gas(rxn))
    gases = [(f, -c) for c, f, p in rxn[0] if p == "g"] + [(f, c) for c, f, p in rxn[1] if p == "g"]
    T = nice(rng, lo, hi, step)
    mode = pick(rng, ["conc", "moles", "pressure"])
    Kp_true = k_model(key, T)
    K = sig(Kp_true, 3) if mode == "pressure" else sig(Kp_true * (R_LATM * T) ** (-dn), 3)
    V = nice(rng, 1.00, 10.00, 0.50) if mode == "moles" else None

    def val(a):
        return a / V if mode == "moles" else a

    for _ in range(1000):
        amounts = []
        for _f, _nu in gases:
            if mode == "pressure":
                amounts.append(nice(rng, 0.10, 5.00, 0.05))
            elif mode == "moles":
                amounts.append(nice(rng, 0.050, 2.500, 0.025))
            else:
                amounts.append(nice(rng, 0.020, 1.500, 0.005))
        free = rng.randrange(len(gases))
        u = rng.choice([-1, 1]) * rng.uniform(0.2, 1.3)
        rest = 1.0
        for i, (a, (_f, nu)) in enumerate(zip(amounts, gases)):
            if i != free:
                rest *= val(a) ** float(nu)
        nu_f = float(gases[free][1])
        v_free = (K * 10 ** u / rest) ** (1 / nu_f)
        a_free = sig(v_free * V if mode == "moles" else v_free, 3)
        if not 0.010 <= a_free <= 20.0:
            continue
        amounts[free] = a_free
        Q = 1.0
        for a, (_f, nu) in zip(amounts, gases):
            Q *= val(a) ** float(nu)
        if abs(math.log10(Q / K)) >= 0.1:
            break
    else:
        raise RuntimeError("no suitable Q/K mixture")
    forward = Q < K
    eq = rxn_txt(rxn, arrow="⇌")
    kname = "K_p" if mode == "pressure" else "K_c"
    qname = "Q_p" if mode == "pressure" else "Q_c"

    def term(f, nu, inner):
        e = abs(nu)
        return inner + (f"^{{{e}}}" if e != 1 else "")

    def sym(f):
        return f"P_{{{tex(f)}}}" if mode == "pressure" else f"[{tex(f)}]"

    num = " ".join(term(f, nu, sym(f)) for f, nu in gases if nu > 0) or "1"
    den = " ".join(term(f, nu, sym(f)) for f, nu in gases if nu < 0) or "1"
    unit = "atm" if mode == "pressure" else ("mol" if mode == "moles" else "M")
    listing = ", ".join(f"{qx(a, unit)} {pretty(f)}" for a, (f, nu) in zip(amounts, gases))
    solids = solids_note(rxn)
    if mode == "pressure":
        setup = f"a reaction vessel at {qx(T, 'K')} contains the gases at partial pressures of {listing}"
    elif mode == "moles":
        setup = f"a {qx(V, 'L')} reaction vessel at {qx(T, 'K')} contains {listing}"
    else:
        setup = f"a mixture at {qx(T, 'K')} has the concentrations {listing}"
    solid_txt = f" (with some {' and '.join(solids)} present)" if solids else ""
    question = (
        f"For {eq}, ${kname} = {fmt(K, 3)}$ at {qx(T, 'K')}. At one moment {setup}{solid_txt}. Calculate the reaction "
        f"quotient ${qname}$, decide whether the system is at equilibrium, and predict the direction of net reaction."
    )
    steps = [f"${qname}$ has the same form as ${kname}$ but uses the current {'partial pressures' if mode == 'pressure' else 'concentrations'}"
             + (f"; the solid {', '.join(solids)} is left out" if solids else "")
             + f": ${qname} = \\frac{{{num}}}{{{den}}}$."]
    if mode == "moles":
        steps.append("Concentrations $c = n/V$: " + "; ".join(
            f"[{pretty(f)}] $= {ex(a)}/{ex(V)} = {fmt(a / V, 4)}$ M" for a, (f, nu) in zip(amounts, gases)) + ".")

    def sub(f, nu, a):
        e = abs(nu)
        return f"({fmt(val(a), 4)})" + (f"^{{{e}}}" if e != 1 else "")

    num_s = "".join(sub(f, nu, a) for a, (f, nu) in zip(amounts, gases) if nu > 0) or "1"
    den_s = "".join(sub(f, nu, a) for a, (f, nu) in zip(amounts, gases) if nu < 0) or "1"
    steps.append(f"${qname} = \\frac{{{num_s}}}{{{den_s}}} = {fmt(Q, 3)}$.")
    if forward:
        steps.append(
            f"${qname} = {fmt(Q, 3)} < {kname} = {fmt(K, 3)}$: the mixture has too few products relative to equilibrium, so it "
            "is not at equilibrium and the net reaction proceeds forward (to the right)."
        )
        steps.append("Products are formed and reactants consumed until $Q$ rises to $K$.")
        answer = f"${qname} = {fmt(Q, 3)} < {kname}$; not at equilibrium — the reaction proceeds forward (toward products)"
    else:
        steps.append(
            f"${qname} = {fmt(Q, 3)} > {kname} = {fmt(K, 3)}$: the mixture has too many products relative to equilibrium, so it "
            "is not at equilibrium and the net reaction proceeds in reverse (to the left)."
        )
        steps.append("Reactants are re-formed from the products until $Q$ falls to $K$.")
        answer = f"${qname} = {fmt(Q, 3)} > {kname}$; not at equilibrium — the reaction proceeds in reverse (toward reactants)"
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"reaction": key, "T": T, "mode": mode, "K": K, "V": V, "amounts": amounts,
                       "nu": [float(nu) for _f, nu in gases], "Q": Q, "forward": forward}}


VH_CASES = [
    ("ammonia", (450, 800, 25)), ("sulfur_trioxide", (700, 1100, 25)), ("dinitrogen_tetroxide", (275, 400, 5)),
    ("phosphorus_pentachloride", (400, 600, 10)), ("calcium_carbonate", (900, 1300, 10)), ("methanol", (400, 650, 10)),
    ("boudouard", (850, 1300, 10)), ("water_gas_shift", (500, 1100, 25)), ("nitric_oxide", (500, 900, 10)),
    ("steam_reforming", (850, 1200, 10)),
]
DH_WATER_IONIZATION = 55.8   # kJ/mol for 2 H2O(l) ⇌ H3O+(aq) + OH-(aq)


@template("vant_hoff_k_temperature", CHEM, PCHEM, "Temperature dependence of K", "medium")
def vant_hoff_k_temperature(rng):
    r = rng.random()
    if r < 0.2:
        mode = "water"
        T1 = T_STD
        K1 = KW
        dH = DH_WATER_IONIZATION
        tC = pick(rng, [0, 5, 10, 15, 20, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80])
        T2 = tC + 273.15
        K2 = K1 * math.exp(-dH * 1000 / R_GAS * (1 / T2 - 1 / T1))
        pH_n = -0.5 * math.log10(K2)
        question = (
            f"The autoionization of water, 2 H₂O(l) ⇌ H₃O⁺(aq) + OH⁻(aq), has $K_w = 1.0 \\times 10^{{-14}}$ at 25 °C and "
            f"$\\Delta H^\\circ = +{dH}$ kJ/mol. Assuming $\\Delta H^\\circ$ is constant, estimate $K_w$ at {tC} °C and the "
            "pH of pure (neutral) water at that temperature."
        )
        x = -dH * 1000 / R_GAS * (1 / T2 - 1 / T1)
        steps = [
            "van 't Hoff equation: $\\ln\\frac{K_2}{K_1} = -\\frac{\\Delta H^\\circ}{R}\\left(\\frac{1}{T_2} - \\frac{1}{T_1}\\right)$.",
            f"$T_1 = 298.15$ K, $T_2 = {tC} + 273.15 = {fmt(T2, 5)}$ K; "
            f"$\\frac{{1}}{{T_2}} - \\frac{{1}}{{T_1}} = {fmt(1 / T2 - 1 / T1, 4)}$ K⁻¹.",
            f"$\\ln\\frac{{K_2}}{{K_1}} = -\\frac{{{dH}\\times10^3}}{{8.314}}({fmt(1 / T2 - 1 / T1, 4)}) = {x:.4f}$.",
            f"$K_w = (1.0\\times10^{{-14}})e^{{{x:.4f}}} = {fmt(K2, 3)}$.",
            f"In pure water $[\\text{{H}}_3\\text{{O}}^+] = [\\text{{OH}}^-] = \\sqrt{{K_w}} = {fmt(math.sqrt(K2), 3)}$ M, so "
            f"pH $= {ph(pH_n)}$.",
            ("Ionization is endothermic, so $K_w$ grows with temperature and neutral pH falls below 7; the water is still "
             "neutral because $[\\text{H}_3\\text{O}^+] = [\\text{OH}^-]$." if T2 > T1 else
             "Ionization is endothermic, so $K_w$ is smaller at lower temperature and neutral pH is above 7; the water is "
             "still neutral because $[\\text{H}_3\\text{O}^+] = [\\text{OH}^-]$."),
        ]
        answer = f"$K_w = {fmt(K2, 3)}$ at {tC} °C; neutral pH = {ph(pH_n)}"
        return {"question": question, "steps": steps, "answer": answer,
                "values": {"mode": mode, "T1": T1, "T2": T2, "K1": K1, "K2": K2, "dH_kJ": dH, "pH_neutral": pH_n,
                           "dS": None}}
    key, (lo, hi, step) = pick(rng, VH_CASES)
    rxn = parse_rxn(EQUILIBRIA[key][0])
    dH_tab = EQUILIBRIA[key][1]
    while True:
        T1 = nice(rng, lo, hi, step)
        T2 = nice(rng, lo, hi, step)
        if abs(T2 - T1) >= 3 * step and abs(T2 - T1) >= 25:
            break
    eq = rxn_txt(rxn, arrow="⇌")
    K1 = sig(k_model(key, T1), 3)
    inv = 1 / T2 - 1 / T1
    if r < 0.6:
        mode = "find_K2"
        dH = dH_tab
        x = -dH * 1000 / R_GAS * inv
        K2 = K1 * math.exp(x)
        question = (
            f"For {eq}, $K_p = {fmt(K1, 3)}$ at {qx(T1, 'K')} and $\\Delta H^\\circ = {kj(dH)}$ kJ/mol. Assuming "
            f"$\\Delta H^\\circ$ does not change with temperature, estimate $K_p$ at {qx(T2, 'K')}."
        )
        steps = [
            "van 't Hoff equation: $\\ln\\frac{K_2}{K_1} = -\\frac{\\Delta H^\\circ}{R}\\left(\\frac{1}{T_2} - \\frac{1}{T_1}\\right)$.",
            f"$\\frac{{1}}{{T_2}} - \\frac{{1}}{{T_1}} = \\frac{{1}}{{{ex(T2)}}} - \\frac{{1}}{{{ex(T1)}}} = {fmt(inv, 4)}$ K⁻¹.",
            f"$\\ln\\frac{{K_2}}{{K_1}} = -\\frac{{{fmt(dH * 1000, 4)}}}{{8.314}}({fmt(inv, 4)}) = {x:.4f}$.",
            f"$K_2 = ({fmt(K1, 3)})e^{{{x:.4f}}} = {fmt(K2, 3)}$.",
            f"Consistency: the reaction is {'exothermic' if dH < 0 else 'endothermic'}, so raising the temperature "
            f"{'lowers' if dH < 0 else 'raises'} $K$ (Le Châtelier); here $T$ {'rises' if T2 > T1 else 'falls'} and $K$ "
            f"{'increases' if K2 > K1 else 'decreases'}, as expected.",
        ]
        answer = f"$K_p \\approx {fmt(K2, 3)}$ at {ex(T2)} K"
        values = {"mode": mode, "reaction": key, "T1": T1, "T2": T2, "K1": K1, "K2": K2, "dH_kJ": dH, "dS": None,
                  "pH_neutral": None}
    else:
        mode = "find_dH"
        K2 = sig(k_model(key, T2), 3)
        lnr = math.log(K2 / K1)
        dH = -R_GAS * lnr / inv / 1000
        dG1 = -R_GAS * T1 * math.log(K1) / 1000
        dS = (dH - dG1) * 1000 / T1
        question = (
            f"For {eq}, $K_p = {fmt(K1, 3)}$ at {qx(T1, 'K')} and $K_p = {fmt(K2, 3)}$ at {qx(T2, 'K')}. Use the "
            "van 't Hoff equation to find $\\Delta H^\\circ$ (assumed constant over this range), then find $\\Delta S^\\circ$ "
            f"from $\\Delta G^\\circ$ at {qx(T1, 'K')}."
        )
        steps = [
            "van 't Hoff equation: $\\Delta H^\\circ = -\\frac{R\\ln(K_2/K_1)}{1/T_2 - 1/T_1}$.",
            f"$\\ln\\frac{{{fmt(K2, 3)}}}{{{fmt(K1, 3)}}} = {lnr:.4f}$; $\\frac{{1}}{{{ex(T2)}}} - \\frac{{1}}{{{ex(T1)}}} = "
            f"{fmt(inv, 4)}$ K⁻¹.",
            f"$\\Delta H^\\circ = -\\frac{{(8.314)({lnr:.4f})}}{{{fmt(inv, 4)}}} = {fmt(dH * 1000, 4)}$ J/mol "
            f"$= {fmt(dH, 4)}$ kJ/mol ({'exothermic' if dH < 0 else 'endothermic'}).",
            f"$\\Delta G^\\circ({ex(T1)}\\text{{ K}}) = -RT_1\\ln K_1 = -(8.314)({ex(T1)})\\ln({fmt(K1, 3)}) = {fmt(dG1, 4)}$ kJ/mol.",
            f"$\\Delta S^\\circ = \\frac{{\\Delta H^\\circ - \\Delta G^\\circ}}{{T_1}} = \\frac{{({fmt(dH, 4)} - ({fmt(dG1, 4)}))\\times10^3}}{{{ex(T1)}}} = "
            f"{fmt(dS, 4)}$ J/(mol·K).",
        steps[-1] = (
            f"Interpretation: an {'endothermic' if dH > 0 else 'exothermic'} reaction has a $K$ that "
            f"{'rises' if dH > 0 else 'falls'} with temperature, as the data show; $\\Delta S^\\circ$ is "
            f"{'positive' if dS > 0 else 'negative'}, consistent with the reaction {'increasing' if dS > 0 else 'decreasing'} "
            "the number of moles of gas."
            ),
        ]
        answer = f"$\\Delta H^\\circ \\approx {fmt(dH, 3)}$ kJ/mol; $\\Delta S^\\circ \\approx {fmt(dS, 3)}$ J/(mol·K)"
        values = {"mode": mode, "reaction": key, "T1": T1, "T2": T2, "K1": K1, "K2": K2, "dH_kJ": dH, "dS": dS,
                  "pH_neutral": None}
    return {"question": question, "steps": steps, "answer": answer, "values": values,
            "difficulty": "hard" if mode == "find_dH" else "medium"}


# ---------------------------------------------------------------------------
# Acids, bases and buffers
# ---------------------------------------------------------------------------

HYDROLYSIS_SALTS = [  # salt, name, hydrolyzing ion, spectator ion, conjugate partner, K of partner, ion behaves as
    ("NaF", "sodium fluoride", "F⁻", "Na⁺", "HF", 6.8e-4, "base"),
    ("CH3COONa", "sodium acetate", "CH₃COO⁻", "Na⁺", "CH₃COOH", 1.8e-5, "base"),
    ("NaNO2", "sodium nitrite", "NO₂⁻", "Na⁺", "HNO₂", 4.5e-4, "base"),
    ("KNO2", "potassium nitrite", "NO₂⁻", "K⁺", "HNO₂", 4.5e-4, "base"),
    ("NaCN", "sodium cyanide", "CN⁻", "Na⁺", "HCN", 6.2e-10, "base"),
    ("NaOCl", "sodium hypochlorite", "OCl⁻", "Na⁺", "HOCl", 3.0e-8, "base"),
    ("HCOONa", "sodium formate", "HCOO⁻", "Na⁺", "HCOOH", 1.8e-4, "base"),
    ("C6H5COONa", "sodium benzoate", "C₆H₅COO⁻", "Na⁺", "C₆H₅COOH", 6.3e-5, "base"),
    ("NH4Cl", "ammonium chloride", "NH₄⁺", "Cl⁻", "NH₃", 1.8e-5, "acid"),
    ("NH4NO3", "ammonium nitrate", "NH₄⁺", "NO₃⁻", "NH₃", 1.8e-5, "acid"),
    ("CH3NH3Cl", "methylammonium chloride", "CH₃NH₃⁺", "Cl⁻", "CH₃NH₂", 4.4e-4, "acid"),
    ("C5H5NHCl", "pyridinium chloride", "C₅H₅NH⁺", "Cl⁻", "C₅H₅N", 1.7e-9, "acid"),
    ("C6H5NH3Cl", "anilinium chloride", "C₆H₅NH₃⁺", "Cl⁻", "C₆H₅NH₂", 4.3e-10, "acid"),
]


@template("salt_hydrolysis_ph", CHEM, GEN, "Acid-base properties of salts", "medium")
def salt_hydrolysis_ph(rng):
    salt, name, ion, spect, partner, Kp, kind = pick(rng, HYDROLYSIS_SALTS)
    K = KW / Kp
    M = mm(salt)
    by_mass = rng.random() < 0.45
    for _ in range(1000):
        if by_mass:
            mass = nice(rng, 0.50, 30.00, 0.05)
            V = nice(rng, 100, 1000, 50)
            c = mass / M / (V / 1000)
        else:
            c = sig(rng.uniform(1.0, 9.9) * 10.0 ** -rng.randint(1, 2), 2)
        if K * c >= 1e-12 and c <= 1.0:
            break
    else:
        raise RuntimeError("no valid concentration")
    x = (-K + math.sqrt(K * K + 4 * K * c)) / 2
    if kind == "base":
        pOH = -math.log10(x)
        pH = 14 - pOH
        hyd = f"{ion} + H₂O ⇌ {partner} + OH⁻"
        kname, pname = "K_b", "K_a"
    else:
        pH = -math.log10(x)
        hyd = f"{ion} + H₂O ⇌ {partner} + H₃O⁺"
        kname, pname = "K_a", "K_b"
    cation, anion = (spect, ion) if kind == "base" else (ion, spect)
    amount = (f"{qx(mass, 'g')} of {name} ({pretty(salt)}) is dissolved in water to make {qx(V, 'mL')} of solution"
              if by_mass else f"a {qx(c, 'M', 2)} solution of {name} ({pretty(salt)}) is prepared")
    question = (
        f"At 25 °C, {amount}. Given {pname}({partner}) $= {fmt(Kp, 2)}$, calculate the pH of the solution and the "
        "percentage of the ion that reacts with water."
    )
    steps = []
    if by_mass:
        steps.append(f"Concentration: $M({pretty(salt)}) = {M:.2f}$ g/mol, so $c = \\frac{{{ex(mass)}/{M:.2f}}}"
                     f"{{{fmt(V / 1000, 3)}\\text{{ L}}}} = {fmt(c, 4)}$ M.")
    strong = "base" if kind == "base" else "acid"
    steps.append(
        f"The salt dissociates completely into {cation} and {anion}. {spect} comes from a strong {strong} and does not "
        f"react with water, but {ion} is the conjugate {kind} of the weak {'acid' if kind == 'base' else 'base'} "
        f"{partner}, so the solution is {'basic' if kind == 'base' else 'acidic'}."
    )
    steps.append(
        f"Hydrolysis: {hyd}, with ${kname} = \\frac{{K_w}}{{{pname}}} = \\frac{{1.0\\times10^{{-14}}}}{{{fmt(Kp, 2)}}} = "
        f"{fmt(K, 3)}$."
    )
    prod = "OH⁻" if kind == "base" else "H₃O⁺"
    steps.append(
        f"ICE: [{ion}] $= {fmt(c, 4)} - x$, [{partner}] = [{prod}] $= x$; $\\frac{{x^2}}{{{fmt(c, 4)} - x}} = {fmt(K, 3)}$, "
        f"so $x = \\frac{{-K + \\sqrt{{K^2 + 4Kc}}}}{{2}} = {fmt(x, 3)}$ M (the $\\sqrt{{Kc}}$ shortcut gives the same "
        "value because $x \\ll c$)."
    )
    if kind == "base":
        steps.append(f"pOH $= -\\log({fmt(x, 3)}) = {ph(pOH)}$, so pH $= 14.00 - {ph(pOH)} = {ph(pH)}$ (basic).")
    else:
        steps.append(f"pH $= -\\log({fmt(x, 3)}) = {ph(pH)}$ (acidic).")
    pct = 100 * x / c
    steps.append(f"Fraction hydrolyzed: $\\frac{{{fmt(x, 3)}}}{{{fmt(c, 4)}}} \\times 100\\% = {fmt(pct, 2)}\\%$ — only a "
                 "small fraction of the ions react with water.")
    values = {"salt": salt, "kind": kind, "K_partner": Kp, "K_ion": K, "c": c, "x": x, "pH": pH, "percent": pct,
              "mass": mass if by_mass else None, "V_mL": V if by_mass else None, "M": M}
    return {"question": question, "steps": steps, "answer": f"pH = {ph(pH)}; {fmt(pct, 2)}% hydrolyzed",
            "values": values}


DIPROTIC = [  # name, H2A, HA-, A2-, Ka1, Ka2
    ("carbonic acid", "H₂CO₃", "HCO₃⁻", "CO₃²⁻", 4.5e-7, 4.7e-11),
    ("hydrosulfuric acid", "H₂S", "HS⁻", "S²⁻", 9.5e-8, 1.0e-19),
    ("oxalic acid", "H₂C₂O₄", "HC₂O₄⁻", "C₂O₄²⁻", 5.9e-2, 6.4e-5),
    ("sulfurous acid", "H₂SO₃", "HSO₃⁻", "SO₃²⁻", 1.7e-2, 6.4e-8),
    ("ascorbic acid", "H₂C₆H₆O₆", "HC₆H₆O₆⁻", "C₆H₆O₆²⁻", 8.0e-5, 1.6e-12),
    ("malonic acid", "H₂C₃H₂O₄", "HC₃H₂O₄⁻", "C₃H₂O₄²⁻", 1.5e-3, 2.0e-6),
    ("phthalic acid", "H₂C₈H₄O₄", "HC₈H₄O₄⁻", "C₈H₄O₄²⁻", 1.1e-3, 3.9e-6),
    ("tartaric acid", "H₂C₄H₄O₆", "HC₄H₄O₆⁻", "C₄H₄O₆²⁻", 1.0e-3, 4.6e-5),
]


@template("diprotic_acid_ph_species", CHEM, PCHEM, "Polyprotic acids", "hard")
def diprotic_acid_ph_species(rng):
    name, h2a, ha, a2, Ka1, Ka2 = pick(rng, DIPROTIC)
    for _ in range(1000):
        c = sig(rng.uniform(1.0, 9.9) * 10.0 ** -rng.randint(1, 3), 2)
        x = (-Ka1 + math.sqrt(Ka1 * Ka1 + 4 * Ka1 * c)) / 2
        if Ka2 / x <= 0.05 and x >= 1e-6:
            break
    else:
        raise RuntimeError("no valid diprotic concentration")
    pH = -math.log10(x)
    h2a_eq = c - x
    question = (
        f"Calculate the pH of a {qx(c, 'M', 2)} solution of {name} ({h2a}; $K_{{a1}} = {fmt(Ka1, 2)}$, "
        f"$K_{{a2}} = {fmt(Ka2, 2)}$) at 25 °C, and the equilibrium concentrations of {h2a}, {ha} and {a2}."
    )
    approx_ok = x / c < 0.05
    steps = [
        f"$K_{{a1}}/K_{{a2}} = {fmt(Ka1 / Ka2, 2)}$, so the first ionization, {h2a} + H₂O ⇌ H₃O⁺ + {ha}, supplies "
        "essentially all of the H₃O⁺; treat the acid as monoprotic first.",
        f"ICE: [{h2a}] $= {fmt(c, 2)} - x$, [H₃O⁺] = [{ha}] $= x$; $\\frac{{x^2}}{{{fmt(c, 2)} - x}} = {fmt(Ka1, 2)}$.",
        f"Solving $x^2 + {fmt(Ka1, 2)}x - {fmt(Ka1 * c, 3)} = 0$: $x = {fmt(x, 3)}$ M"
        + (" (here the $\\sqrt{K_{a1}c}$ shortcut would also work, since ionization is below 5%)." if approx_ok else
           f" — {fmt(100 * x / c, 2)}% ionization, so the quadratic is required rather than the $\\sqrt{{K_{{a1}}c}}$ shortcut."),
        f"pH $= -\\log({fmt(x, 3)}) = {ph(pH)}$; [{h2a}] $= {fmt(c, 2)} - {fmt(x, 3)} = {fmt(h2a_eq, 3)}$ M, "
        f"[{ha}] $\\approx {fmt(x, 3)}$ M.",
        f"Second ionization: $K_{{a2}} = \\frac{{[\\text{{H}}_3\\text{{O}}^+][\\text{{A}}^{{2-}}]}}{{[\\text{{HA}}^-]}}$ and "
        f"[H₃O⁺] ≈ [{ha}], so [{a2}] $\\approx K_{{a2}} = {fmt(Ka2, 2)}$ M, independent of the acid concentration.",
        f"Check: the second step adds at most ${fmt(Ka2, 2)}$ M of H₃O⁺, only {fmt(100 * Ka2 / x, 2)}% of ${fmt(x, 3)}$ M, so "
        "neglecting it is justified.",
    ]
    answer = (f"pH = {ph(pH)}; [{h2a}] = {fmt(h2a_eq, 3)} M, [{ha}] = {fmt(x, 3)} M, [{a2}] = {fmt(Ka2, 2)} M")
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"Ka1": Ka1, "Ka2": Ka2, "c": c, "H3O": x, "pH": pH, "H2A": h2a_eq, "HA": x, "A2": Ka2}}


BUFFER_PREP = [  # weak species name, its label, conjugate label, type of weak species, salt formula, salt name, K, K label
    ("acetic acid", "CH₃COOH", "CH₃COO⁻", "acid", "CH3COONa", "sodium acetate", 1.8e-5, "K_a"),
    ("acetic acid", "CH₃COOH", "CH₃COO⁻", "acid", "CH3COONa·3H2O", "sodium acetate trihydrate", 1.8e-5, "K_a"),
    ("formic acid", "HCOOH", "HCOO⁻", "acid", "HCOONa", "sodium formate", 1.8e-4, "K_a"),
    ("benzoic acid", "C₆H₅COOH", "C₆H₅COO⁻", "acid", "C6H5COONa", "sodium benzoate", 6.3e-5, "K_a"),
    ("lactic acid", "HC₃H₅O₃", "C₃H₅O₃⁻", "acid", "NaC3H5O3", "sodium lactate", 1.4e-4, "K_a"),
    ("sodium dihydrogen phosphate", "H₂PO₄⁻", "HPO₄²⁻", "acid", "Na2HPO4", "disodium hydrogen phosphate", 6.2e-8,
     "K_{a2}"),
    ("sodium hydrogen carbonate", "HCO₃⁻", "CO₃²⁻", "acid", "Na2CO3", "sodium carbonate", 4.7e-11, "K_{a2}"),
    ("hypochlorous acid", "HOCl", "OCl⁻", "acid", "NaOCl", "sodium hypochlorite", 3.0e-8, "K_a"),
    ("ammonia", "NH₃", "NH₄⁺", "base", "NH4Cl", "ammonium chloride", 1.8e-5, "K_b"),
    ("methylamine", "CH₃NH₂", "CH₃NH₃⁺", "base", "CH3NH3Cl", "methylammonium chloride", 4.4e-4, "K_b"),
]


@template("buffer_preparation_target_ph", CHEM, ANALYT, "Buffer preparation", "medium")
def buffer_preparation_target_ph(rng):
    wname, wlab, clab, wtype, salt, sname, K, klab = pick(rng, BUFFER_PREP)
    pKa = -math.log10(K) if wtype == "acid" else 14 + math.log10(K)
    acid_lab, base_lab = (wlab, clab) if wtype == "acid" else (clab, wlab)
    while True:
        pH = round(pKa + rng.uniform(-0.75, 0.75), 2)
        if abs(pH - pKa) >= 0.05:
            break
    c = nice(rng, 0.050, 0.500, 0.010)
    V = pick(rng, [100.0, 250.0, 500.0, 1000.0])
    n_w = c * V / 1000
    ratio = 10 ** (pH - pKa)   # [base]/[acid]
    mode = "salt" if rng.random() < 0.55 else "titrant"
    k_txt = f"${klab} = {fmt(K, 2)}$" + (" for " + wlab if klab == "K_{a2}" else "")
    steps = []
    if wtype == "acid":
        steps.append(f"$\\mathrm{{p}}K_a = -\\log({fmt(K, 2)}) = {pKa:.3f}$.")
    else:
        steps.append(f"For the conjugate acid {clab}: $\\mathrm{{p}}K_a = 14.00 - \\mathrm{{p}}K_b = 14.00 + \\log({fmt(K, 2)}) = "
                     f"{pKa:.3f}$.")
    steps.append(
        f"Henderson–Hasselbalch: pH $= \\mathrm{{p}}K_a + \\log\\frac{{[\\text{{base}}]}}{{[\\text{{acid}}]}}$, so "
        f"$\\frac{{[{base_lab}]}}{{[{acid_lab}]}} = 10^{{{ph(pH)} - {pKa:.3f}}} = {fmt(ratio, 3)}$. Both species share the "
        "same volume, so this is also the mole ratio."
    )
    steps.append(f"Moles of {wlab} present: $({ex(c)}\\text{{ M}})({fmt(V / 1000, 3)}\\text{{ L}}) = {fmt(n_w, 3)}$ mol.")
    values = {"K": K, "weak_type": wtype, "pKa": pKa, "pH": pH, "c_weak": c, "V_mL": V, "ratio": ratio, "mode": mode}
    if mode == "salt":
        Ms = mm(salt)
        n_salt = n_w * ratio if wtype == "acid" else n_w / ratio
        mass = n_salt * Ms
        question = (
            f"What mass of {sname} ({pretty(salt)}) must be dissolved in {qx(V, 'mL')} of {qx(c, 'M')} {wname} "
            f"({k_txt}) to make a buffer with pH {ph(pH)}? Assume the volume does not change."
        )
        if wtype == "acid":
            steps.append(f"Moles of {clab} needed: $n = {fmt(ratio, 3)} \\times {fmt(n_w, 3)} = {fmt(n_salt, 3)}$ mol, "
                         f"supplied by {sname}.")
        else:
            steps.append(f"Moles of {clab} needed: $n = \\frac{{{fmt(n_w, 3)}}}{{{fmt(ratio, 3)}}} = {fmt(n_salt, 3)}$ mol, "
                         f"supplied by {sname}.")
        steps.append(f"Molar mass of {pretty(salt)}: ${Ms:.2f}$ g/mol, so $m = ({fmt(n_salt, 3)})({Ms:.2f}) = {fmt(mass, 3)}$ g.")
        steps.append(f"Check: $\\mathrm{{p}}K_a + \\log\\frac{{n_{{base}}}}{{n_{{acid}}}} = {pKa:.3f} + "
                     f"\\log({fmt(ratio, 3)}) = {ph(pH)}$ ✓; the ratio lies between 0.1 and 10, so the buffer is effective.")
        answer = f"${fmt(mass, 3)}$ g of {sname}"
        values.update({"salt": salt, "M_salt": Ms, "n_add": n_salt, "mass": mass, "c_titrant": None, "V_titrant": None})
    else:
        titrant = "NaOH" if wtype == "acid" else "HCl"
        if wtype == "acid":
            n_add = n_w * ratio / (1 + ratio)
        else:
            n_add = n_w / (1 + ratio)
        for _ in range(100):
            ct = pick(rng, [0.100, 0.200, 0.250, 0.500, 1.00, 2.00])
            Vt = n_add / ct * 1000
            if 2.0 <= Vt <= V:
                break
        else:
            ct = 1.00
            Vt = n_add / ct * 1000
        question = (
            f"A buffer of pH {ph(pH)} is to be made by adding {qx(ct, 'M')} {titrant} to {qx(V, 'mL')} of {qx(c, 'M')} "
            f"{wname} ({k_txt}). What volume of {titrant} is required?"
        )
        if wtype == "acid":
            steps.append(
                f"OH⁻ converts {wlab} into {clab} (1:1). If $y$ mol NaOH is added, $n({clab}) = y$ and "
                f"$n({wlab}) = {fmt(n_w, 3)} - y$; setting $\\frac{{y}}{{{fmt(n_w, 3)} - y}} = {fmt(ratio, 3)}$ gives "
                f"$y = \\frac{{({fmt(ratio, 3)})({fmt(n_w, 3)})}}{{1 + {fmt(ratio, 3)}}} = {fmt(n_add, 3)}$ mol."
            )
        else:
            steps.append(
                f"H₃O⁺ converts {wlab} into {clab} (1:1). If $y$ mol HCl is added, $n({clab}) = y$ and "
                f"$n({wlab}) = {fmt(n_w, 3)} - y$; setting $\\frac{{{fmt(n_w, 3)} - y}}{{y}} = {fmt(ratio, 3)}$ gives "
                f"$y = \\frac{{{fmt(n_w, 3)}}}{{1 + {fmt(ratio, 3)}}} = {fmt(n_add, 3)}$ mol."
            )
        steps.append(f"Volume of {ex(ct)} M {titrant}: $V = \\frac{{{fmt(n_add, 3)}}}{{{ex(ct)}}} = {fmt(Vt / 1000, 3)}$ L "
                     f"$= {fmt(Vt, 3)}$ mL. Dilution by the added solution changes both amounts equally, so the pH is unaffected.")
        answer = f"${fmt(Vt, 3)}$ mL of {ex(ct)} M {titrant}"
        values.update({"salt": None, "M_salt": None, "n_add": n_add, "mass": None, "c_titrant": ct, "V_titrant": Vt})
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Solubility
# ---------------------------------------------------------------------------

PRECIP = [  # precipitate, name, Ksp, cations, anions per formula unit, cation, anion, cation source, anion source
    ("AgCl", "silver chloride", 1.8e-10, 1, 1, "Ag⁺", "Cl⁻", "AgNO₃", "NaCl"),
    ("AgBr", "silver bromide", 5.0e-13, 1, 1, "Ag⁺", "Br⁻", "AgNO₃", "KBr"),
    ("BaSO4", "barium sulfate", 1.1e-10, 1, 1, "Ba²⁺", "SO₄²⁻", "BaCl₂", "Na₂SO₄"),
    ("CaSO4", "calcium sulfate", 4.9e-5, 1, 1, "Ca²⁺", "SO₄²⁻", "CaCl₂", "Na₂SO₄"),
    ("SrSO4", "strontium sulfate", 3.4e-7, 1, 1, "Sr²⁺", "SO₄²⁻", "Sr(NO₃)₂", "Na₂SO₄"),
    ("PbSO4", "lead(II) sulfate", 2.5e-8, 1, 1, "Pb²⁺", "SO₄²⁻", "Pb(NO₃)₂", "Na₂SO₄"),
    ("CaCO3", "calcium carbonate", 3.4e-9, 1, 1, "Ca²⁺", "CO₃²⁻", "CaCl₂", "Na₂CO₃"),
    ("PbI2", "lead(II) iodide", 9.8e-9, 1, 2, "Pb²⁺", "I⁻", "Pb(NO₃)₂", "KI"),
    ("PbCl2", "lead(II) chloride", 1.7e-5, 1, 2, "Pb²⁺", "Cl⁻", "Pb(NO₃)₂", "NaCl"),
    ("CaF2", "calcium fluoride", 3.9e-11, 1, 2, "Ca²⁺", "F⁻", "Ca(NO₃)₂", "NaF"),
    ("Mg(OH)2", "magnesium hydroxide", 5.6e-12, 1, 2, "Mg²⁺", "OH⁻", "MgCl₂", "NaOH"),
    ("Ag2CrO4", "silver chromate", 1.1e-12, 2, 1, "Ag⁺", "CrO₄²⁻", "AgNO₃", "K₂CrO₄"),
    ("Ag2SO4", "silver sulfate", 1.2e-5, 2, 1, "Ag⁺", "SO₄²⁻", "AgNO₃", "Na₂SO₄"),
]


@template("precipitation_on_mixing_ksp", CHEM, GEN, "Precipitation", "medium")
def precipitation_on_mixing_ksp(rng):
    ppt, pname, Ksp, a, b, cat, an, csrc, asrc = pick(rng, PRECIP)
    for _ in range(2000):
        c1 = mant(rng, -4, -1)
        V1 = nice(rng, 10.0, 250.0, 5.0)
        V2 = nice(rng, 10.0, 250.0, 5.0)
        Vt = V1 + V2
        cat_c = c1 * V1 / Vt
        u = rng.choice([-1, 1]) * rng.uniform(0.2, 2.5)
        an_need = (Ksp * 10 ** u / cat_c ** a) ** (1 / b)
        c2 = sig(an_need * Vt / V2, 2)
        if not 1e-5 <= c2 <= 1.0:
            continue
        an_c = c2 * V2 / Vt
        Q = cat_c ** a * an_c ** b
        if abs(math.log10(Q / Ksp)) >= 0.15:
            break
    else:
        raise RuntimeError("no valid mixture")
    forms = Q > Ksp
    an_min = (Ksp / cat_c ** a) ** (1 / b)
    sol1 = f"{qx(V1, 'mL')} of {qx(c1, 'M', 2)} {csrc}"
    sol2 = f"{qx(V2, 'mL')} of {qx(c2, 'M', 2)} {asrc}"
    first, second = (sol1, sol2) if rng.random() < 0.5 else (sol2, sol1)
    question = (
        f"At 25 °C, {first} is mixed with {second}. "
        f"Will {pname} ({pretty(ppt)}, $K_{{sp}} = {fmt(Ksp, 2)}$) precipitate? Also find the {an} concentration at which "
        f"precipitation would just begin for the {cat} concentration in the mixture. Assume the volumes are additive."
    )
    kexp = (f"[\\text{{{cat}}}]" + (f"^{a}" if a > 1 else "") + f"[\\text{{{an}}}]" + (f"^{b}" if b > 1 else ""))
    steps = [
        f"Total volume: ${ex(V1)} + {ex(V2)} = {ex(Vt)}$ mL. Both salts are soluble strong electrolytes, so each ion is "
        "simply diluted by mixing.",
        f"[{cat}] $= \\frac{{({fmt(c1, 2)})({ex(V1)})}}{{{ex(Vt)}}} = {fmt(cat_c, 3)}$ M; "
        f"[{an}] $= \\frac{{({fmt(c2, 2)})({ex(V2)})}}{{{ex(Vt)}}} = {fmt(an_c, 3)}$ M.",
        f"{pretty(ppt)}(s) ⇌ {coef_txt(a)}{cat}(aq) + {coef_txt(b)}{an}(aq); ion product "
        f"$Q = {kexp} = ({fmt(cat_c, 3)})" + (f"^{a}" if a > 1 else "") + f"({fmt(an_c, 3)})" + (f"^{b}" if b > 1 else "")
        + f" = {fmt(Q, 3)}$.",
    ]
    if forms:
        steps.append(f"$Q = {fmt(Q, 3)} > K_{{sp}} = {fmt(Ksp, 2)}$: the solution is supersaturated, so {pretty(ppt)} "
                     "precipitates until the ion product falls to $K_{sp}$.")
    else:
        steps.append(f"$Q = {fmt(Q, 3)} < K_{{sp}} = {fmt(Ksp, 2)}$: the solution is unsaturated, so no precipitate forms.")
    root = "" if b == 1 else f"^{{1/{b}}}"
    steps.append(
        f"Onset of precipitation: $[\\text{{{an}}}]_{{min}} = \\left(\\frac{{K_{{sp}}}}{{[\\text{{{cat}}}]"
        + (f"^{a}" if a > 1 else "") + f"}}\\right){root} = \\left(\\frac{{{fmt(Ksp, 2)}}}{{({fmt(cat_c, 3)})"
        + (f"^{a}" if a > 1 else "") + f"}}\\right){root} = {fmt(an_min, 3)}$ M "
        f"(the mixture has {fmt(an_c, 3)} M, {'above' if forms else 'below'} this threshold)."
    )
    answer = (f"$Q = {fmt(Q, 3)}$ {'>' if forms else '<'} $K_{{sp}}$: "
              + (f"{pretty(ppt)} precipitates" if forms else "no precipitate forms")
              + f"; precipitation begins at [{an}] = {fmt(an_min, 3)} M")
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"Ksp": Ksp, "a": a, "b": b, "c_cation_source": c1, "V1_mL": V1, "c_anion_source": c2,
                       "V2_mL": V2, "cation": cat_c, "anion": an_c, "Q": Q, "precipitates": forms,
                       "anion_threshold": an_min}}


# ---------------------------------------------------------------------------
# Kinetics
# ---------------------------------------------------------------------------

ZERO_ORDER_CASES = [
    {"intro": "Ammonia decomposes on a hot tungsten wire, 2 NH₃(g) → N₂(g) + 3 H₂(g). The metal surface is saturated "
              "with adsorbed NH₃, so ammonia is consumed at a constant rate (zero-order kinetics)",
     "qty": "the NH₃ concentration", "sym": "[\\text{NH}_3]", "unit": "mM", "tu": "s",
     "A0": (2.00, 8.00, 0.05), "k": (0.0100, 0.0400, 0.0005), "limit": None},
    {"intro": "Dinitrogen monoxide decomposes on a hot platinum surface, 2 N₂O(g) → 2 N₂(g) + O₂(g), with "
              "zero-order kinetics because the surface is saturated",
     "qty": "the N₂O concentration", "sym": "[\\text{N}_2\\text{O}]", "unit": "M", "tu": "min",
     "A0": (0.100, 0.500, 0.005), "k": (0.0010, 0.0080, 0.0001), "limit": None},
    {"intro": "Hydrogen iodide decomposes on a gold surface, 2 HI(g) → H₂(g) + I₂(g), with zero-order kinetics",
     "qty": "the HI concentration", "sym": "[\\text{HI}]", "unit": "M", "tu": "s",
     "A0": (0.050, 0.300, 0.005), "k": (1.0e-4, 5.0e-4, 1.0e-5), "limit": None},
    {"intro": "Ethanol is removed from the blood mainly by liver alcohol dehydrogenase, which is saturated at typical "
              "blood-alcohol levels, so the blood-alcohol concentration (BAC) falls at a constant rate (zero-order "
              "kinetics)",
     "qty": "the BAC", "sym": "\\text{BAC}", "unit": "g/L", "tu": "h",
     "A0": (0.80, 2.00, 0.05), "k": (0.10, 0.20, 0.01), "limit": (0.50, "the legal driving limit in many countries")},
    {"intro": "A transdermal patch releases its drug at a constant rate (zero-order kinetics) as long as drug remains "
              "in the reservoir",
     "qty": "the amount of drug left in the patch", "sym": "m", "unit": "mg", "tu": "h",
     "A0": (20.0, 120.0, 0.5), "k": (0.50, 2.50, 0.05), "limit": None},
    {"intro": "An enzyme-catalyzed reaction is run with the enzyme saturated by substrate S, so S is consumed at a "
              "constant rate (zero order in S) until it runs low",
     "qty": "[S]", "sym": "[\\text{S}]", "unit": "mM", "tu": "min",
     "A0": (5.0, 50.0, 0.5), "k": (0.20, 2.00, 0.05), "limit": None},
]


@template("zero_order_integrated_rate", CHEM, PCHEM, "Chemical kinetics", "easy")
def zero_order_integrated_rate(rng):
    case = pick(rng, ZERO_ORDER_CASES)
    unit, tu, sym = case["unit"], case["tu"], case["sym"]
    ku = f"{unit}/{tu}"
    if rng.random() < 0.55:
        mode = "forward"
        A0 = nice(rng, *case["A0"])
        k = nice(rng, *case["k"])
        t_end = A0 / k
        t = sig(rng.uniform(0.1, 0.9) * t_end, 2)
        At = A0 - k * t
        t_half = A0 / (2 * k)
        lim = case["limit"]
        if lim is not None and A0 > lim[0] + 0.05:
            target = lim[0]
            target_txt = f"{qx(target, unit, 2)} ({lim[1]})"
            pct = None
        else:
            pct = pick(rng, [10, 20, 25, 40, 75])
            target = A0 * pct / 100
            target_txt = f"{pct}% of its initial value"
        t_target = (A0 - target) / k
        question = (
            f"{case['intro']}. Initially {case['qty']} is {qx(A0, unit)}, and it decreases with a zero-order rate constant "
            f"$k = {ex(k, 2)}$ {ku}. Find {case['qty']} after {qx(t, tu, 2)}, the half-life, the time needed to fall to "
            f"{target_txt}, and the time at which it would be used up completely."
        )
        steps = [
            f"Zero order: rate $= -\\frac{{d{sym}}}{{dt}} = k$, so ${sym} = {sym}_0 - kt$ — a straight line of slope $-k$.",
            f"After {ex(t, 2)} {tu}: ${sym} = {ex(A0)} - ({ex(k, 2)})({ex(t, 2)}) = {fmt(At, 3)}$ {unit}.",
            f"Half-life: $t_{{1/2}} = \\frac{{{sym}_0}}{{2k}} = \\frac{{{ex(A0)}}}{{2({ex(k, 2)})}} = {fmt(t_half, 3)}$ {tu} — "
            "it is proportional to the starting amount, unlike a first-order half-life.",
            f"Time to reach {fmt(target, 3)} {unit}: $t = \\frac{{{sym}_0 - {sym}}}{{k}} = \\frac{{{ex(A0)} - {fmt(target, 3)}}}"
            f"{{{ex(k, 2)}}} = {fmt(t_target, 3)}$ {tu}.",
            f"Used up when ${sym} = 0$: $t = {sym}_0/k = {fmt(t_end, 3)}$ {tu}; in practice the rate drops below the "
            "zero-order value near the end, once the surface or enzyme is no longer saturated.",
        ]
        answer = (f"{fmt(At, 3)} {unit} after {ex(t, 2)} {tu}; $t_{{1/2}} = {fmt(t_half, 3)}$ {tu}; "
                  f"{fmt(t_target, 3)} {tu} to reach {fmt(target, 3)} {unit}; gone after {fmt(t_end, 3)} {tu}")
        values = {"mode": mode, "A0": A0, "k": k, "t": t, "A_t": At, "t_half": t_half, "pct": pct, "target": target,
                  "t_target": t_target, "t_end": t_end, "t1": None, "A1": None, "t2": None, "A2": None}
    else:
        mode = "data"
        A0_true = nice(rng, *case["A0"])
        k_true = nice(rng, *case["k"])
        t_end_true = A0_true / k_true
        f1 = rng.uniform(0.1, 0.4)
        f2 = f1 + rng.uniform(0.2, 0.45)
        t1 = sig(f1 * t_end_true, 2)
        t2 = sig(f2 * t_end_true, 2)
        A1 = sig(A0_true - k_true * t1, 3)
        A2 = sig(A0_true - k_true * t2, 3)
        k = (A1 - A2) / (t2 - t1)
        A0 = A1 + k * t1
        t_half = A0 / (2 * k)
        t_end = A0 / k
        question = (
            f"{case['intro']}. {case['qty'][0].upper() + case['qty'][1:]} is measured as {qx(A1, unit)} at "
            f"$t = {ex(t1, 2)}$ {tu} and {qx(A2, unit)} at $t = {ex(t2, 2)}$ {tu}. Find the rate constant, the initial "
            "value, the half-life and the time at which it is used up completely."
        )
        steps = [
            f"Zero order: ${sym} = {sym}_0 - kt$, so the data lie on a straight line of slope $-k$.",
            f"$k = -\\frac{{\\Delta {sym}}}{{\\Delta t}} = \\frac{{{ex(A1)} - {ex(A2)}}}{{{ex(t2, 2)} - {ex(t1, 2)}}} = "
            f"{fmt(k, 3)}$ {ku}.",
            f"Back-extrapolate: ${sym}_0 = {ex(A1)} + ({fmt(k, 3)})({ex(t1, 2)}) = {fmt(A0, 3)}$ {unit}.",
            f"Half-life: $t_{{1/2}} = \\frac{{{sym}_0}}{{2k}} = {fmt(t_half, 3)}$ {tu}.",
            f"Used up at $t = {sym}_0/k = {fmt(t_end, 3)}$ {tu} (assuming the rate stays zero order to the end).",
        ]
        answer = (f"$k = {fmt(k, 3)}$ {ku}; initial value {fmt(A0, 3)} {unit}; $t_{{1/2}} = {fmt(t_half, 3)}$ {tu}; "
                  f"used up after {fmt(t_end, 3)} {tu}")
        values = {"mode": mode, "A0": A0, "k": k, "t": None, "A_t": None, "t_half": t_half, "pct": None, "target": None,
                  "t_target": None, "t_end": t_end, "t1": t1, "A1": A1, "t2": t2, "A2": A2}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Solutions and gases
# ---------------------------------------------------------------------------

WATER_VP_RAOULT = {20: 17.54, 25: 23.76, 30: 31.82, 40: 55.32, 50: 92.51, 60: 149.4, 70: 233.7, 80: 355.1}  # torr
NONVOLATILE = [  # solute, name, solvent
    ("C12H22O11", "sucrose", "water"), ("C6H12O6", "glucose", "water"), ("CO(NH2)2", "urea", "water"),
    ("C3H8O3", "glycerol", "water"), ("C2H6O2", "ethylene glycol", "water"),
    ("C10H8", "naphthalene", "benzene"), ("C12H10", "biphenyl", "benzene"),
]
SOLVENTS = {"water": ("H2O", None), "benzene": ("C6H6", 95.1)}
VOLATILE_PAIRS = [  # (name, formula, P° at 25 °C in torr) for the more volatile and the less volatile liquid
    (("benzene", "C6H6", 95.1), ("toluene", "C7H8", 28.4)),
    (("hexane", "C6H14", 151.0), ("heptane", "C7H16", 45.7)),
    (("pentane", "C5H12", 512.0), ("hexane", "C6H14", 151.0)),
    (("methanol", "CH3OH", 127.0), ("ethanol", "C2H5OH", 59.0)),
]


@template("raoult_law_vapor_pressure", CHEM, PCHEM, "Raoult's law", "medium")
def raoult_law_vapor_pressure(rng):
    if rng.random() < 0.5:
        mode = "nonvolatile"
        f, name, solv = pick(rng, NONVOLATILE)
        sf, P0 = SOLVENTS[solv]
        tC = 25
        if solv == "water":
            tC = pick(rng, sorted(WATER_VP_RAOULT))
            P0 = WATER_VP_RAOULT[tC]
        m_solute = nice(rng, 5.0, 150.0, 0.5)
        m_solv = nice(rng, 100, 500, 5)
        M2, M1 = mm(f), mm(sf)
        n2, n1 = m_solute / M2, m_solv / M1
        x1 = n1 / (n1 + n2)
        P = x1 * P0
        dP = P0 - P
        question = (
            f"{qx(m_solute, 'g')} of {name} ({pretty(f)}), a nonvolatile nonelectrolyte, is dissolved in "
            f"{qx(m_solv, 'g')} of {solv}. The vapor pressure of pure {solv} at {tC} °C is {qx(P0, 'torr')}. Assuming "
            "ideal behavior, find the vapor pressure of the solution and the vapor-pressure lowering."
        )
        steps = [
            "Raoult's law: only the solvent contributes to the vapor, $P = \\chi_{solvent}P^\\circ_{solvent}$.",
            f"Moles: {pretty(f)} ${ex(m_solute)}/{M2:.2f} = {fmt(n2, 4)}$ mol; {solv} ${ex(m_solv)}/{M1:.2f} = {fmt(n1, 4)}$ mol.",
            f"$\\chi_{{solvent}} = \\frac{{{fmt(n1, 4)}}}{{{fmt(n1, 4)} + {fmt(n2, 4)}}} = {fmt(x1, 4)}$.",
            f"$P = ({fmt(x1, 4)})({ex(P0)}) = {fmt(P, 4)}$ torr.",
            f"Lowering: $\\Delta P = \\chi_{{solute}}P^\\circ = ({fmt(1 - x1, 3)})({ex(P0)}) = {fmt(dP, 3)}$ torr — a "
            "colligative property that depends on the number of solute particles, not on their identity.",
        ]
        answer = f"$P = {fmt(P, 4)}$ torr; lowered by ${fmt(dP, 3)}$ torr"
        values = {"mode": mode, "P0": P0, "m_solute": m_solute, "M_solute": M2, "m_solvent": m_solv, "M_solvent": M1,
                  "x_solvent": x1, "P": P, "dP": dP, "x_A": None, "y_A": None, "P0_B": None}
    else:
        mode = "binary"
        (na, fa, pa), (nb, fb, pb) = pick(rng, VOLATILE_PAIRS)
        if rng.random() < 0.5:
            ma = nice(rng, 10.0, 100.0, 0.5)
            mb = nice(rng, 10.0, 100.0, 0.5)
            Ma, Mb = mm(fa), mm(fb)
            xa = (ma / Ma) / (ma / Ma + mb / Mb)
            comp = f"{qx(ma, 'g')} of {na} ({pretty(fa)}) and {qx(mb, 'g')} of {nb} ({pretty(fb)})"
            pre = [f"Moles: {na} ${ex(ma)}/{Ma:.2f} = {fmt(ma / Ma, 4)}$ mol, {nb} ${ex(mb)}/{Mb:.2f} = {fmt(mb / Mb, 4)}$ mol; "
                   f"$\\chi_{{{na}}} = {fmt(xa, 4)}$, $\\chi_{{{nb}}} = {fmt(1 - xa, 4)}$."]
        else:
            ma = mb = None
            xa = nice(rng, 0.10, 0.90, 0.01)
            comp = f"{na} and {nb} with a {na} mole fraction of {qx(xa, '', 2)}"
            pre = [f"$\\chi_{{{nb}}} = 1 - {ex(xa, 2)} = {ex(1 - xa, 2)}$."]
        Pa, Pb = xa * pa, (1 - xa) * pb
        P = Pa + Pb
        ya = Pa / P
        question = (
            f"At 25 °C the vapor pressures of pure {na} and {nb} are {qx(pa, 'torr')} and {qx(pb, 'torr')}. A solution "
            f"contains {comp}. Treating it as an ideal solution, find the partial pressures, the total vapor pressure "
            f"and the mole fraction of {na} in the vapor."
        )
        steps = ["For an ideal solution of two volatile liquids each component obeys Raoult's law, "
                 "$P_i = \\chi_iP_i^\\circ$, and Dalton's law gives $P = P_A + P_B$."] + pre + [
            f"$P_{{{na}}} = ({fmt(xa, 4)})({ex(pa)}) = {fmt(Pa, 4)}$ torr; $P_{{{nb}}} = ({fmt(1 - xa, 4)})({ex(pb)}) = "
            f"{fmt(Pb, 4)}$ torr.",
            f"$P = {fmt(Pa, 4)} + {fmt(Pb, 4)} = {fmt(P, 4)}$ torr.",
            f"Vapor: $y_{{{na}}} = P_{{{na}}}/P = {fmt(ya, 3)}$, larger than its liquid mole fraction ({fmt(xa, 3)}) — the vapor "
            "is enriched in the more volatile component, the basis of fractional distillation.",
        ]
        answer = (f"$P_{{{na}}} = {fmt(Pa, 4)}$ torr, $P_{{{nb}}} = {fmt(Pb, 4)}$ torr, $P = {fmt(P, 4)}$ torr; "
                  f"$y_{{{na}}} = {fmt(ya, 3)}$")
        values = {"mode": mode, "P0": pa, "P0_B": pb, "m_solute": ma, "M_solute": mm(fa), "m_solvent": mb,
                  "M_solvent": mm(fb), "x_A": xa, "P": P, "y_A": ya, "x_solvent": None, "dP": None}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


WATER_VP_TORR = {15: 12.8, 16: 13.6, 17: 14.5, 18: 15.5, 19: 16.5, 20: 17.5, 21: 18.7, 22: 19.8, 23: 21.1,
                 24: 22.4, 25: 23.8, 26: 25.2, 27: 26.7, 28: 28.3, 29: 30.0, 30: 31.8}
COLLECTED_GASES = [  # equation, gas, reactant formula, reactant name, mol reactant per mol gas, how it is made
    ("2 KClO₃(s) → 2 KCl(s) + 3 O₂(g)", "O2", "KClO3", "potassium chlorate", Fr(2, 3),
     "Oxygen is prepared by heating potassium chlorate with a little MnO₂ catalyst"),
    ("Zn(s) + 2 HCl(aq) → ZnCl₂(aq) + H₂(g)", "H2", "Zn", "zinc", Fr(1),
     "Hydrogen is prepared by reacting zinc with excess hydrochloric acid"),
    ("Mg(s) + 2 HCl(aq) → MgCl₂(aq) + H₂(g)", "H2", "Mg", "magnesium", Fr(1),
     "Hydrogen is prepared by reacting magnesium ribbon with excess hydrochloric acid"),
    ("2 Al(s) + 6 HCl(aq) → 2 AlCl₃(aq) + 3 H₂(g)", "H2", "Al", "aluminum", Fr(2, 3),
     "Hydrogen is prepared by reacting aluminum foil with excess hydrochloric acid"),
    ("2 H₂O₂(aq) → 2 H₂O(l) + O₂(g)", "O2", "H2O2", "hydrogen peroxide", Fr(2),
     "Oxygen is prepared by decomposing hydrogen peroxide over a catalyst"),
    ("NH₄NO₂(s) → N₂(g) + 2 H₂O(l)", "N2", "NH4NO2", "ammonium nitrite", Fr(1),
     "Nitrogen is prepared by gently heating ammonium nitrite"),
]
MIX_GASES = [("He", "helium"), ("Ne", "neon"), ("Ar", "argon"), ("N2", "nitrogen"), ("O2", "oxygen"),
             ("CO2", "carbon dioxide"), ("CH4", "methane"), ("H2", "hydrogen")]


@template("dalton_partial_pressures", CHEM, GEN, "Partial pressures", "medium")
def dalton_partial_pressures(rng):
    if rng.random() < 0.55:
        mode = "over_water"
        eqn, gas, rf, rname, ratio, how = pick(rng, COLLECTED_GASES)
        V = nice(rng, 50.0, 450.0, 0.5)
        tC = pick(rng, sorted(WATER_VP_TORR))
        Pw = WATER_VP_TORR[tC]
        Pbar = nice(rng, 735, 775, 1)
        Pg = Pbar - Pw
        T = tC + 273.15
        n = (Pg / TORR_PER_ATM) * (V / 1000) / (R_LATM * T)
        Mr = mm(rf)
        mass = n * float(ratio) * Mr
        question = (
            f"{how} ({eqn}). The gas is collected over water at {tC} °C in an inverted bottle until it occupies "
            f"{qx(V, 'mL')}, with the water levels inside and outside equalized; the barometric pressure is "
            f"{qx(Pbar, 'torr')} and the vapor pressure of water at {tC} °C is {qx(Pw, 'torr')}. Find the partial pressure "
            f"of the dry {pretty(gas)}, the moles collected and the mass of {rname} that reacted."
        )
        steps = [
            f"Dalton's law: the bottle contains {pretty(gas)} saturated with water vapor, and with the levels equal the total "
            f"pressure equals the barometric pressure: $P_{{gas}} = P_{{bar}} - P_{{H_2O}} = {ex(Pbar)} - {ex(Pw)} = {ex(Pg)}$ torr "
            f"$= {fmt(Pg / TORR_PER_ATM, 4)}$ atm.",
            f"Ideal gas law with $T = {tC} + 273.15 = {fmt(T, 5)}$ K and $V = {fmt(V / 1000, 4)}$ L: "
            f"$n = \\frac{{PV}}{{RT}} = \\frac{{({fmt(Pg / TORR_PER_ATM, 4)})({fmt(V / 1000, 4)})}}{{(0.08206)({fmt(T, 5)})}} = "
            f"{fmt(n, 4)}$ mol {pretty(gas)}.",
            f"Stoichiometry: {coef_txt(ratio).strip() or '1'} mol {pretty(rf)} per mol {pretty(gas)}, so "
            f"$n({pretty(rf)}) = {fmt(n * float(ratio), 4)}$ mol; $m = ({fmt(n * float(ratio), 4)})({Mr:.2f}) = {fmt(mass, 3)}$ g.",
            "Ignoring the water vapor would overestimate the gas by "
            f"{fmt(100 * Pw / Pg, 2)}%.",
        ]
        answer = f"$P_{{{tex(gas)}}} = {ex(Pg)}$ torr; $n = {fmt(n, 3)}$ mol; ${fmt(mass, 3)}$ g of {rname}"
        values = {"mode": mode, "V_mL": V, "T_C": tC, "P_bar": Pbar, "P_water": Pw, "P_gas": Pg, "n": n,
                  "ratio": float(ratio), "M": Mr, "mass": mass, "masses": None, "Ms": None, "V_L": None, "T_K": None,
                  "partials": None, "P_total": None, "fractions": None}
    else:
        mode = "mixture"
        k = pick(rng, [2, 3])
        gases = rng.sample(MIX_GASES, k)
        masses = [nice(rng, 0.50, 20.00, 0.05) for _ in gases]
        V = nice(rng, 2.0, 25.0, 0.5)
        T = nice(rng, 273, 400, 1)
        Ms = [mm(f) for f, _ in gases]
        ns = [m / M for m, M in zip(masses, Ms)]
        ntot = sum(ns)
        xs = [n / ntot for n in ns]
        Ps = [n * R_LATM * T / V for n in ns]
        Ptot = sum(Ps)
        listing = ", ".join(f"{qx(m, 'g')} of {nm} ({pretty(f)})" for m, (f, nm) in zip(masses, gases))
        question = (
            f"A {qx(V, 'L')} steel tank at {qx(T, 'K')} contains {listing}. Assuming ideal behavior, find the mole fraction "
            "and partial pressure of each gas and the total pressure."
        )
        steps = ["Each gas behaves as if alone in the tank (Dalton's law): $P_i = n_iRT/V$, $P = \\sum P_i$ and $P_i = \\chi_iP$.",
                 "Moles: " + "; ".join(f"{pretty(f)} ${ex(m)}/{M:.2f} = {fmt(n, 4)}$ mol" for m, M, n, (f, _) in
                                      zip(masses, Ms, ns, gases)) + f"; total ${fmt(ntot, 4)}$ mol.",
                 "Mole fractions: " + ", ".join(f"$\\chi_{{{tex(f)}}} = {fmt(x, 3)}$" for x, (f, _) in zip(xs, gases)) + ".",
                 f"$\\frac{{RT}}{{V}} = \\frac{{(0.08206)({ex(T)})}}{{{ex(V)}}} = {fmt(R_LATM * T / V, 4)}$ atm/mol, so "
                 + ", ".join(f"$P_{{{tex(f)}}} = {fmt(p, 3)}$ atm" for p, (f, _) in zip(Ps, gases)) + ".",
                 f"Total: $P = {fmt(Ptot, 3)}$ atm; check: $\\chi_iP$ reproduces each partial pressure."]
        answer = "; ".join(f"{pretty(f)}: $\\chi = {fmt(x, 3)}$, ${fmt(p, 3)}$ atm" for x, p, (f, _) in zip(xs, Ps, gases)) \
            + f"; total ${fmt(Ptot, 3)}$ atm"
        values = {"mode": mode, "masses": masses, "Ms": Ms, "V_L": V, "T_K": T, "partials": Ps, "P_total": Ptot,
                  "fractions": xs, "V_mL": None, "T_C": None, "P_bar": None, "P_water": None, "P_gas": None, "n": None,
                  "ratio": None, "M": None, "mass": None}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


VDW_GASES = [  # formula, name, a (L² atm/mol²), b (L/mol)
    ("He", "helium", 0.0341, 0.0237), ("H2", "hydrogen", 0.244, 0.0266), ("N2", "nitrogen", 1.39, 0.0391),
    ("O2", "oxygen", 1.36, 0.0318), ("Ar", "argon", 1.34, 0.0322), ("CH4", "methane", 2.25, 0.0428),
    ("CO2", "carbon dioxide", 3.59, 0.0427), ("NH3", "ammonia", 4.17, 0.0371), ("Cl2", "chlorine", 6.49, 0.0562),
    ("Xe", "xenon", 4.19, 0.0510),
]


@template("van_der_waals_real_gas", CHEM, PCHEM, "Real gases", "medium")
def van_der_waals_real_gas(rng):
    f, name, a, b = pick(rng, VDW_GASES)
    Tc = 8 * a / (27 * R_LATM * b)
    M = mm(f)
    by_mass = rng.random() < 0.5
    for _ in range(2000):
        if by_mass:
            mass = nice(rng, 5.0, 500.0, 0.5)
            n = mass / M
        else:
            n = nice(rng, 0.50, 10.00, 0.05)
        V = nice(rng, 0.50, 10.00, 0.05)
        T = nice(rng, 250, 600, 5)
        Pid = n * R_LATM * T / V
        if T >= 1.3 * Tc and V / n >= 5 * b and 5 <= Pid <= 250:
            break
    else:
        raise RuntimeError("no valid van der Waals conditions")
    rep = n * R_LATM * T / (V - n * b)
    att = a * n * n / (V * V)
    P = rep - att
    Z = P / Pid
    dev = 100 * (P - Pid) / Pid
    amount = f"{qx(mass, 'g')} of {name} ({pretty(f)})" if by_mass else f"{qx(n, 'mol')} of {name}"
    question = (
        f"A {qx(V, 'L')} cylinder holds {amount} at {qx(T, 'K')}. Calculate the pressure predicted by the ideal gas law "
        f"and by the van der Waals equation ($a = {ex(a, 3)}$ L²·atm/mol², $b = {ex(b, 3)}$ L/mol), and the compressibility "
        "factor $Z = P_{vdW}V/(nRT)$."
    )
    steps = []
    if by_mass:
        steps.append(f"Moles: $n = {ex(mass)}/{M:.2f} = {fmt(n, 4)}$ mol.")
    steps += [
        f"Ideal gas: $P = \\frac{{nRT}}{{V}} = \\frac{{({fmt(n, 4)})(0.08206)({ex(T)})}}{{{ex(V)}}} = {fmt(Pid, 4)}$ atm.",
        "van der Waals: $P = \\frac{nRT}{V - nb} - \\frac{an^2}{V^2}$; $nb$ corrects for the volume of the molecules and "
        "$an^2/V^2$ for their mutual attraction.",
        f"Repulsive term: $\\frac{{({fmt(n, 4)})(0.08206)({ex(T)})}}{{{ex(V)} - ({fmt(n, 4)})({ex(b, 3)})}} = {fmt(rep, 4)}$ atm; "
        f"attractive term: $\\frac{{({ex(a, 3)})({fmt(n, 4)})^2}}{{({ex(V)})^2}} = {fmt(att, 4)}$ atm.",
        f"$P_{{vdW}} = {fmt(rep, 4)} - {fmt(att, 4)} = {fmt(P, 4)}$ atm, i.e. {fmt(abs(dev), 2)}% "
        f"{'below' if dev < 0 else 'above'} the ideal value.",
        f"$Z = P_{{vdW}}/P_{{ideal}} = {fmt(Z, 4)}$: "
        + ("$Z < 1$, so intermolecular attractions dominate under these conditions." if Z < 1 else
           "$Z > 1$, so the finite size of the molecules (repulsion) dominates under these conditions."),
    ]
    answer = f"$P_{{ideal}} = {fmt(Pid, 4)}$ atm; $P_{{vdW}} = {fmt(P, 4)}$ atm; $Z = {fmt(Z, 4)}$"
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"formula": f, "a": a, "b": b, "n": n, "mass": mass if by_mass else None, "M": M, "V": V, "T": T,
                       "P_ideal": Pid, "P_vdw": P, "Z": Z}}


SOLUTION_DATA = [  # formula, name, [(mass percent, density in g/mL at 20 °C)]
    ("NaCl", "sodium chloride", [(4, 1.0268), (6, 1.0413), (8, 1.0559), (10, 1.0707), (12, 1.0857), (14, 1.1009),
                                 (16, 1.1162), (18, 1.1319), (20, 1.1478), (22, 1.1640), (24, 1.1804), (26, 1.1972)]),
    ("C12H22O11", "sucrose", [(10, 1.0381), (20, 1.0810), (30, 1.1270), (40, 1.1765), (50, 1.2296), (60, 1.2865)]),
    ("H2SO4", "sulfuric acid", [(10, 1.0661), (20, 1.1394), (30, 1.2185), (40, 1.3028), (50, 1.3951), (60, 1.4983),
                                (70, 1.6105), (80, 1.7272), (96, 1.8355)]),
    ("NaOH", "sodium hydroxide", [(10, 1.1089), (20, 1.2191), (30, 1.3279), (40, 1.4300), (50, 1.5253)]),
    ("HNO3", "nitric acid", [(10, 1.0543), (20, 1.1150), (30, 1.1801), (40, 1.2463), (50, 1.3100), (60, 1.3667),
                             (70, 1.4134)]),
    ("HCl", "hydrochloric acid", [(10, 1.0474), (20, 1.0980), (30, 1.1492), (36, 1.1789)]),
    ("C2H5OH", "ethanol", [(10, 0.9819), (20, 0.9686), (30, 0.9538), (40, 0.9352), (50, 0.9138), (60, 0.8911)]),
]


@template("solution_concentration_units", CHEM, GEN, "Concentration units", "medium")
def solution_concentration_units(rng):
    f, name, table = pick(rng, SOLUTION_DATA)
    w, rho = pick(rng, table)
    M = mm(f)
    n = w / M                        # mol solute per 100 g of solution
    Vsol = 100 / rho                 # mL per 100 g of solution
    molarity = n / (Vsol / 1000)
    molality = n / ((100 - w) / 1000)
    chi = n / (n + (100 - w) / M_WATER)
    extra = pick(rng, ["mass", "dilute", "none"])
    steps = [
        f"Take exactly 100 g of solution: it contains {w} g of {pretty(f)} and {100 - w} g of water.",
        f"Moles of solute: ${w}/{M:.2f} = {fmt(n, 4)}$ mol; volume of the 100 g: $100/{ex(rho, 4)} = {fmt(Vsol, 4)}$ mL.",
        f"Molarity: $\\frac{{{fmt(n, 4)}\\text{{ mol}}}}{{{fmt(Vsol / 1000, 4)}\\text{{ L}}}} = {fmt(molarity, 4)}$ M.",
        f"Molality: $\\frac{{{fmt(n, 4)}\\text{{ mol}}}}{{{fmt((100 - w) / 1000, 3)}\\text{{ kg water}}}} = "
        f"{fmt(molality, 4)}$ mol/kg.",
        f"Mole fraction: water ${100 - w}/{M_WATER} = {fmt((100 - w) / M_WATER, 4)}$ mol, so "
        f"$\\chi = \\frac{{{fmt(n, 4)}}}{{{fmt(n, 4)} + {fmt((100 - w) / M_WATER, 4)}}} = {fmt(chi, 4)}$.",
    ]
    values = {"formula": f, "w": w, "rho": rho, "M": M, "molarity": molarity, "molality": molality, "chi": chi,
              "extra": extra, "V_mL": None, "m_solute": None, "c2": None, "V2_mL": None, "V_needed_mL": None}
    extra_q = ""
    answer = f"{fmt(molarity, 4)} M; {fmt(molality, 4)} mol/kg; $\\chi = {fmt(chi, 4)}$"
    if extra == "mass":
        V = nice(rng, 25, 500, 5)
        ms = V * rho * w / 100
        extra_q = f" What mass of {name} is contained in {qx(V, 'mL')} of the solution?"
        steps.append(f"Mass of solute in {ex(V)} mL: $m = V\\rho w = ({ex(V)})({ex(rho, 4)})({fmt(w / 100, 2)}) = {fmt(ms, 4)}$ g "
                     f"(check: ${fmt(molarity, 4)}\\text{{ M}} \\times {fmt(V / 1000, 3)}\\text{{ L}} \\times {M:.2f} = "
                     f"{fmt(molarity * V / 1000 * M, 4)}$ g).")
        answer += f"; {fmt(ms, 4)} g in {ex(V)} mL"
        values.update({"V_mL": V, "m_solute": ms})
    elif extra == "dilute":
        for c2 in rng.sample([0.100, 0.200, 0.250, 0.500, 1.00], 5):
            if c2 < molarity / 2:
                break
        V2 = pick(rng, [100.0, 250.0, 500.0, 1000.0])
        Vn = c2 * V2 / molarity
        extra_q = f" What volume of it is needed to prepare {qx(V2, 'mL')} of {qx(c2, 'M')} {name}?"
        steps.append(f"Dilution: $c_1V_1 = c_2V_2 \\Rightarrow V_1 = \\frac{{({ex(c2)})({ex(V2)})}}{{{fmt(molarity, 4)}}} = "
                     f"{fmt(Vn, 3)}$ mL, made up to {ex(V2)} mL with water.")
        answer += f"; {fmt(Vn, 3)} mL needed"
        values.update({"c2": c2, "V2_mL": V2, "V_needed_mL": Vn})
    question = (
        f"An aqueous {name} ({pretty(f)}) solution is {w}% {name} by mass and has a density of {qx(rho, 'g/mL', 4)} at "
        f"20 °C. Calculate its molarity, molality and the mole fraction of {name}.{extra_q}"
    )
    return {"question": question, "steps": steps, "answer": answer, "values": values}


TRACE_LIMITS = [  # species label, name, molar mass, limit (mg/L), source of limit
    ("Pb", "lead", 207.2, 0.015, "the U.S. EPA action level for lead"),
    ("As", "arsenic", 74.922, 0.010, "the U.S. EPA maximum contaminant level (MCL) for arsenic"),
    ("Cu", "copper", 63.546, 1.3, "the U.S. EPA action level for copper"),
    ("Hg", "mercury", 200.59, 0.002, "the U.S. EPA MCL for inorganic mercury"),
    ("Cd", "cadmium", 112.41, 0.005, "the U.S. EPA MCL for cadmium"),
    ("F⁻", "fluoride", 18.998, 4.0, "the U.S. EPA MCL for fluoride"),
    ("NO₃⁻", "nitrate", 62.004, 50.0, "the WHO guideline value for nitrate (as NO₃⁻)"),
    ("U", "uranium", 238.03, 0.030, "the U.S. EPA MCL for uranium"),
    ("Se", "selenium", 78.971, 0.050, "the U.S. EPA MCL for selenium"),
    ("Ba", "barium", 137.33, 2.0, "the U.S. EPA MCL for barium"),
    ("Cr", "chromium", 51.996, 0.10, "the U.S. EPA MCL for total chromium"),
]


@template("trace_contaminant_ppm_ppb", CHEM, ANALYT, "Trace concentrations", "easy")
def trace_contaminant_ppm_ppb(rng):
    sp, name, M, limit, source = pick(rng, TRACE_LIMITS)
    V = pick(rng, [100.0, 250.0, 500.0, 1000.0])
    while True:
        c_true = limit * 10 ** rng.uniform(-0.8, 0.8)
        m_ug = sig(c_true * V, 3)          # mg/L × mL = µg
        ppm = m_ug / V                      # µg/mL = mg/L = ppm
        if abs(math.log10(ppm / limit)) >= 0.02:
            break
    ppb = ppm * 1000
    molar = ppm / 1000 / M
    exceeds = ppm > limit
    L_day = pick(rng, [1.5, 2.0, 2.5, 3.0])
    intake = ppm * L_day * 1000            # µg per day
    mass_txt = qx(m_ug / 1000, "mg") if m_ug >= 1000 else qx(m_ug, "µg")
    question = (
        f"Analysis of a {qx(V, 'mL')} drinking-water sample finds {mass_txt} of {name} ({sp}). Express the concentration "
        f"in ppm, ppb and mol/L, compare it with {source} ({ex(limit, 1)} mg/L), and find how much {name} a person drinking "
        f"{qx(L_day, 'L', 2)} of this water per day would take in. Assume the density of the dilute solution is "
        "1.00 g/mL."
    )
    steps = [
        "For dilute aqueous solutions 1 L has a mass of 1000 g, so 1 ppm = 1 mg/kg = 1 mg/L and 1 ppb = 1 µg/L.",
        f"Concentration: $\\frac{{{fmt(m_ug, 3)}\\text{{ µg}}}}{{{fmt(V / 1000, 3)}\\text{{ L}}}} = {fmt(ppb, 3)}$ µg/L "
        f"$= {fmt(ppb, 3)}$ ppb $= {fmt(ppm, 3)}$ ppm.",
        f"Molarity: $\\frac{{{fmt(ppm / 1000, 3)}\\text{{ g/L}}}}{{{M}\\text{{ g/mol}}}} = {fmt(molar, 3)}$ M.",
        f"Limit: {ex(limit, 1)} mg/L $= {fmt(limit * 1000, 3)}$ ppb; the sample is "
        f"{fmt(ppm / limit, 3)} times the limit, so it {'exceeds' if exceeds else 'is below'} it.",
        f"Daily intake: $({fmt(ppb, 3)}\\text{{ µg/L}})({ex(L_day, 2)}\\text{{ L}}) = {fmt(intake, 3)}$ µg per day.",
    ]
    answer = (f"{fmt(ppm, 3)} ppm = {fmt(ppb, 3)} ppb = ${fmt(molar, 3)}$ M; "
              f"{'exceeds' if exceeds else 'below'} the {ex(limit, 1)} mg/L limit; {fmt(intake, 3)} µg/day")
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"m_ug": m_ug, "V_mL": V, "ppm": ppm, "ppb": ppb, "M": M, "molarity": molar, "limit_mg_L": limit,
                       "exceeds": exceeds, "L_per_day": L_day, "intake_ug": intake}}


# ---------------------------------------------------------------------------
# Solid state
# ---------------------------------------------------------------------------

CUBIC_SOLIDS = [  # formula, name, structure, a (pm)
    ("Po", "polonium (α form)", "sc", 335.2),
    ("Li", "lithium", "bcc", 351.0), ("Na", "sodium", "bcc", 429.1), ("K", "potassium", "bcc", 532.8),
    ("Cr", "chromium", "bcc", 288.5), ("Fe", "iron (α form)", "bcc", 286.6), ("Mo", "molybdenum", "bcc", 314.7),
    ("W", "tungsten", "bcc", 316.5), ("V", "vanadium", "bcc", 302.4), ("Ba", "barium", "bcc", 502.8),
    ("Cs", "cesium", "bcc", 614.1),
    ("Al", "aluminum", "fcc", 404.9), ("Cu", "copper", "fcc", 361.5), ("Ni", "nickel", "fcc", 352.4),
    ("Ag", "silver", "fcc", 408.6), ("Au", "gold", "fcc", 407.8), ("Pt", "platinum", "fcc", 392.4),
    ("Pb", "lead", "fcc", 495.0), ("Ca", "calcium", "fcc", 558.8), ("Pd", "palladium", "fcc", 389.0),
    ("NaCl", "sodium chloride", "rocksalt", 564.0), ("KCl", "potassium chloride", "rocksalt", 629.2),
    ("LiF", "lithium fluoride", "rocksalt", 402.7), ("MgO", "magnesium oxide", "rocksalt", 421.2),
    ("CsCl", "cesium chloride", "cscl", 412.3),
]
STRUCTURES = {
    "sc": (1, "simple cubic", "8 corners × 1/8 = 1 atom", "edge", "a = 2r", 0.5, 52),
    "bcc": (2, "body-centered cubic", "8 corners × 1/8 + 1 body center = 2 atoms", "body diagonal",
            "\\sqrt{3}a = 4r", math.sqrt(3) / 4, 68),
    "fcc": (4, "face-centered cubic", "8 corners × 1/8 + 6 faces × 1/2 = 4 atoms", "face diagonal",
            "\\sqrt{2}a = 4r", math.sqrt(2) / 4, 74),
    "rocksalt": (4, "rock-salt (NaCl-type)", "4 cations + 4 anions = 4 formula units", "cell edge",
                 "a = 2(r_+ + r_-)", 0.5, None),
    "cscl": (1, "cesium chloride-type", "1 cation + 8 × 1/8 anions = 1 formula unit", "body diagonal",
             "\\sqrt{3}a = 2(r_+ + r_-)", math.sqrt(3) / 2, None),
}


@template("cubic_unit_cell_density", CHEM, GEN, "Crystal structure", "medium")
def cubic_unit_cell_density(rng):
    f, name, st, a_tab = pick(rng, CUBIC_SOLIDS)
    Z, sname, count_txt, contact, contact_eq, rfac, pack = STRUCTURES[st]
    metal = st in ("sc", "bcc", "fcc")
    M = mm(f)
    rho_tab = Z * M / (N_A * (a_tab * 1e-10) ** 3)
    modes = ["density", "edge", "identify"] if metal and st != "sc" else ["density", "edge"]
    mode = pick(rng, modes)
    unit_name = "atoms" if metal else "formula units"
    rlabel = "atomic radius" if metal else "sum of the cation and anion radii"
    if mode == "density":
        a = a_tab
        rho = Z * M / (N_A * (a * 1e-10) ** 3)
        question = (
            f"{name.capitalize()} ({pretty(f)}) crystallizes in a {sname} lattice with a unit-cell edge of {qx(a, 'pm', 4)}. "
            f"Calculate its density and the {rlabel}."
        )
        steps = [
            f"Atoms per cell: {count_txt}, so $Z = {Z}$ {unit_name}.",
            f"Mass of one cell: $\\frac{{ZM}}{{N_A}} = \\frac{{({Z})({M:.3f})}}{{6.022\\times10^{{23}}}} = {fmt(Z * M / N_A, 4)}$ g.",
            f"Volume: $a^3 = ({ex(a, 4)}\\times10^{{-10}}\\text{{ cm}})^3 = {fmt((a * 1e-10) ** 3, 4)}$ cm³.",
            f"Density: $\\rho = {fmt(Z * M / N_A, 4)}/{fmt((a * 1e-10) ** 3, 4)} = {fmt(rho, 4)}$ g/cm³.",
        ]
    elif mode == "edge":
        rho = sig(rho_tab, 4)
        a = (Z * M / (N_A * rho)) ** (1 / 3) * 1e10
        question = (
            f"{name.capitalize()} ({pretty(f)}) has a density of {qx(rho, 'g/cm³', 4)} and crystallizes in a {sname} "
            f"lattice. Calculate the unit-cell edge length and the {rlabel}."
        )
        steps = [
            f"Atoms per cell: {count_txt}, so $Z = {Z}$ {unit_name}.",
            f"$\\rho = \\frac{{ZM}}{{N_Aa^3}} \\Rightarrow a^3 = \\frac{{ZM}}{{N_A\\rho}} = "
            f"\\frac{{({Z})({M:.3f})}}{{(6.022\\times10^{{23}})({ex(rho, 4)})}} = {fmt((a * 1e-10) ** 3, 4)}$ cm³.",
            f"$a = {fmt(a * 1e-10, 4)}$ cm $= {fmt(a, 4)}$ pm.",
        ]
    else:
        a = a_tab
        rho = sig(rho_tab, 4)
        z_calc = rho * N_A * (a * 1e-10) ** 3 / M
        question = (
            f"{name.capitalize()} ({pretty(f)}) has a cubic unit cell with edge {qx(a, 'pm', 4)} and a density of "
            f"{qx(rho, 'g/cm³', 4)}. How many atoms are in each unit cell, and is the lattice simple cubic, body-centered "
            f"or face-centered cubic? Also find the {rlabel}."
        )
        steps = [
            f"$Z = \\frac{{\\rho N_Aa^3}}{{M}} = \\frac{{({ex(rho, 4)})(6.022\\times10^{{23}})({ex(a, 4)}\\times10^{{-10}})^3}}"
            f"{{{M:.3f}}} = {fmt(z_calc, 3)} \\approx {Z}$.",
            f"$Z = {Z}$ corresponds to a {sname} cell ({count_txt}).",
        ]
    r = rfac * a
    if metal:
        steps.append(f"In a {sname} metal the atoms touch along the {contact}: ${contact_eq}$, so "
                     f"$r = {fmt(rfac, 4)}a = {fmt(r, 4)}$ pm.")
        steps.append(f"About {pack}% of the cell volume is occupied by atoms in this structure.")
    else:
        steps.append(f"Cations and anions touch along the {contact}: ${contact_eq}$, so "
                     f"$r_+ + r_- = {fmt(rfac, 4)}a = {fmt(r, 4)}$ pm.")
    if mode == "density":
        answer = f"$\\rho = {fmt(rho, 4)}$ g/cm³; $r = {fmt(r, 4)}$ pm" if metal else \
            f"$\\rho = {fmt(rho, 4)}$ g/cm³; $r_+ + r_- = {fmt(r, 4)}$ pm"
    elif mode == "edge":
        answer = f"$a = {fmt(a, 4)}$ pm; " + (f"$r = {fmt(r, 4)}$ pm" if metal else f"$r_+ + r_- = {fmt(r, 4)}$ pm")
    else:
        answer = f"$Z = {Z}$ ({sname}); $r = {fmt(r, 4)}$ pm"
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"formula": f, "structure": st, "mode": mode, "Z": Z, "M": M, "a_pm": a, "rho": rho, "r_pm": r}}


# ---------------------------------------------------------------------------
# Electrochemistry
# ---------------------------------------------------------------------------

CELLS = [  # name, nominal voltage, capacity spec, capacity unit, electrode reaction, species, species name, e- per unit,
    #        cells in series, current spec (in the capacity's current unit)
    ("lithium-ion smartphone battery", 3.85, (3000, 5000, 50), "mAh", "LiC₆ → C₆ + Li⁺ + e⁻ (anode)", "Li",
     "lithium shuttled out of the graphite anode", 1, 1, (150, 800, 10)),
    ("CR2032 lithium coin cell", 3.0, (210, 240, 5), "mAh", "Li → Li⁺ + e⁻ (anode)", "Li", "lithium metal", 1, 1,
     (0.10, 2.00, 0.05)),
    ("alkaline AA cell", 1.5, (1800, 2800, 50), "mAh", "Zn + 2 OH⁻ → ZnO + H₂O + 2 e⁻ (anode)", "Zn", "zinc", 2, 1,
     (50, 500, 10)),
    ("NiMH AA rechargeable cell", 1.2, (1900, 2600, 50), "mAh",
     "NiOOH + H₂O + e⁻ → Ni(OH)₂ + OH⁻ (cathode)", "NiOOH", "nickel oxyhydroxide", 1, 1, (100, 1000, 10)),
    ("zinc–air hearing-aid cell", 1.4, (160, 620, 10), "mAh", "Zn + 2 OH⁻ → ZnO + H₂O + 2 e⁻ (anode)", "Zn", "zinc",
     2, 1, (0.5, 3.0, 0.1)),
    ("12 V lead–acid car battery (six 2.1 V cells in series)", 12.6, (40, 90, 5), "Ah",
     "Pb + HSO₄⁻ → PbSO₄ + H⁺ + 2 e⁻ (anode of each cell)", "Pb", "lead", 2, 6, (2.0, 20.0, 0.5)),
]


@template("battery_capacity_electrons", CHEM, PCHEM, "Batteries", "easy")
def battery_capacity_electrons(rng):
    name, Vnom, cap_spec, cu, rxn, sp, sp_name, z, ncell, I_spec = pick(rng, CELLS)
    cap = nice(rng, *cap_spec)
    I = nice(rng, *I_spec)
    cap_Ah = cap / 1000 if cu == "mAh" else cap
    iu = "mA" if cu == "mAh" else "A"
    I_A = I / 1000 if iu == "mA" else I
    Q = cap_Ah * 3600
    n_e = Q / FARADAY
    M = mm(sp)
    mass = n_e / z * M * ncell
    E_Wh = cap_Ah * Vnom
    E_kJ = E_Wh * 3.6
    hours = cap_Ah / I_A
    question = (
        f"A {name} has a rated capacity of {qx(cap, cu, 2)} at a nominal {qx(Vnom, 'V', 2)}. The electrode reaction is "
        f"{rxn}. Find the charge it can deliver in coulombs, the moles of electrons transferred, the mass of {sp_name} "
        f"({pretty(sp)}) that reacts during a full discharge, the stored energy in Wh and kJ, and how long it can supply "
        f"a steady {qx(I, iu, 2)}."
    )
    steps = [
        f"Charge: 1 Ah = 3600 C, so $Q = ({fmt(cap_Ah, 4)}\\text{{ Ah}})(3600\\text{{ C/Ah}}) = {fmt(Q, 4)}$ C.",
        f"Electrons: $n_{{e^-}} = Q/F = {fmt(Q, 4)}/96485 = {fmt(n_e, 4)}$ mol.",
    ]
    if ncell > 1:
        steps.append(
            f"The six cells are in series, so the same charge passes through each; each cell consumes "
            f"${fmt(n_e, 4)}/{z} = {fmt(n_e / z, 4)}$ mol {pretty(sp)}, and the battery "
            f"$6 \\times {fmt(n_e / z, 4)} \\times {M:.2f} = {fmt(mass, 4)}$ g."
        )
    else:
        steps.append(
            f"{coef_txt(z).strip() or '1'} electron{'s' if z > 1 else ''} per {pretty(sp)}: "
            f"$n = {fmt(n_e, 4)}/{z} = {fmt(n_e / z, 4)}$ mol, so $m = ({fmt(n_e / z, 4)})({M:.2f}) = {fmt(mass, 4)}$ g."
        )
    steps += [
        f"Energy: $E = QV = ({fmt(cap_Ah, 4)}\\text{{ Ah}})({ex(Vnom, 2)}\\text{{ V}}) = {fmt(E_Wh, 4)}$ Wh "
        f"$= {fmt(E_kJ, 4)}$ kJ (1 Wh = 3.6 kJ).",
        f"Run time: $t = \\frac{{\\text{{capacity}}}}{{I}} = \\frac{{{ex(cap, 2)}\\text{{ {cu}}}}}{{{ex(I, 2)}\\text{{ {iu}}}}} = "
        f"{fmt(hours, 3)}$ h (real cells deliver somewhat less at high currents).",
    ]
    answer = (f"$Q = {fmt(Q, 4)}$ C; ${fmt(n_e, 4)}$ mol e⁻; ${fmt(mass, 4)}$ g {pretty(sp)}; ${fmt(E_Wh, 4)}$ Wh "
              f"$= {fmt(E_kJ, 4)}$ kJ; ${fmt(hours, 3)}$ h")
    return {"question": question, "steps": steps, "answer": answer,
            "values": {"capacity_Ah": cap_Ah, "V_nominal": Vnom, "Q_C": Q, "n_e": n_e, "z": z, "cells": ncell,
                       "M": M, "mass_g": mass, "E_Wh": E_Wh, "E_kJ": E_kJ, "I_A": I_A, "hours": hours}}


CONC_CELL_IONS = [("Cu", "Cu²⁺", 2), ("Ag", "Ag⁺", 1), ("Zn", "Zn²⁺", 2), ("Ni", "Ni²⁺", 2), ("Pb", "Pb²⁺", 2),
                  ("Fe", "Fe²⁺", 2)]
CONC_VALUES = [0.0010, 0.0020, 0.0050, 0.010, 0.020, 0.050, 0.10, 0.20, 0.50, 1.0, 1.5, 2.0]
SILVER_HALIDES = [("AgCl", "silver chloride", "Cl⁻", "KCl", 1.8e-10), ("AgBr", "silver bromide", "Br⁻", "KBr", 5.0e-13),
                  ("AgI", "silver iodide", "I⁻", "KI", 8.3e-17)]


@template("concentration_cell_emf", CHEM, PCHEM, "Electrochemistry", "medium")
def concentration_cell_emf(rng):
    r = rng.random()
    if r < 0.45:
        mode = "emf"
        metal, ion, n = pick(rng, CONC_CELL_IONS)
        while True:
            c1, c2 = rng.sample(CONC_VALUES, 2)
            if max(c1, c2) / min(c1, c2) >= 2:
                break
        c_dil, c_con = min(c1, c2), max(c1, c2)
        tC = 25 if rng.random() < 0.6 else pick(rng, [5, 10, 15, 20, 30, 35, 40, 45, 50, 60])
        T = tC + 273.15
        E = R_GAS * T / (n * FARADAY) * math.log(c_con / c_dil)
        question = (
            f"A concentration cell is built from two {metal} electrodes, one in {qx(c1, 'M', 2)} {ion} and the other in "
            f"{qx(c2, 'M', 2)} {ion}, joined by a salt bridge. At {tC} °C, which electrode is the anode, what is the cell "
            "potential, and in which direction do electrons flow in the external circuit?"
        )
        steps = [
            f"Both half-cells are {ion}/{metal}, so $E^\\circ_{{cell}} = 0$; any voltage comes from the concentration "
            "difference alone.",
            f"The cell runs so as to equalize the concentrations: {metal} is oxidized in the dilute ({fmt(c_dil, 2)} M) "
            f"compartment (anode, [{ion}] rises) and {ion} is reduced in the concentrated ({fmt(c_con, 2)} M) one "
            f"(cathode, [{ion}] falls).",
            f"Nernst equation with $Q = \\frac{{[\\text{{{ion}}}]_{{anode}}}}{{[\\text{{{ion}}}]_{{cathode}}}}$: "
            f"$E = -\\frac{{RT}}{{nF}}\\ln Q = \\frac{{(8.314)({fmt(T, 5)})}}{{({n})(96485)}}"
            f"\\ln\\frac{{{fmt(c_con, 2)}}}{{{fmt(c_dil, 2)}}} = {fmt(E, 3)}$ V.",
            f"Electrons leave the anode (dilute side) and travel through the wire to the cathode (concentrated side); "
            "the voltage falls to zero when the two concentrations become equal.",
        ]
        if tC == 25:
            steps.insert(3, f"At 25 °C this is the familiar $E = \\frac{{0.05916}}{{{n}}}\\log\\frac{{{fmt(c_con, 2)}}}"
                            f"{{{fmt(c_dil, 2)}}}$ V.")
        answer = f"anode: {metal} in {fmt(c_dil, 2)} M {ion}; $E = {fmt(E, 3)}$ V; electrons flow from the dilute to the concentrated side"
        values = {"mode": mode, "n": n, "T": T, "c_dilute": c_dil, "c_conc": c_con, "E": E, "Ksp": None, "c_X": None}
    elif r < 0.75:
        mode = "unknown"
        metal, ion, n = pick(rng, CONC_CELL_IONS)
        c_con = pick(rng, [0.10, 0.20, 0.50, 1.0])
        T = T_STD
        c_true = c_con * 10 ** -rng.uniform(0.5, 4.0)
        E = round(R_GAS * T / (n * FARADAY) * math.log(c_con / c_true), 4)
        c_dil = c_con * math.exp(-n * FARADAY * E / (R_GAS * T))
        question = (
            f"The potential of the cell {metal}(s) | {ion}(unknown) ‖ {ion}({fmt(c_con, 2)} M) | {metal}(s) is "
            f"{qx(E, 'V', 3)} at 25 °C. What is the {ion} concentration in the anode compartment?"
        )
        steps = [
            f"Concentration cell: $E^\\circ = 0$ and $E = \\frac{{RT}}{{nF}}\\ln\\frac{{c_{{cathode}}}}{{c_{{anode}}}}$ "
            f"with $n = {n}$.",
            f"$\\ln\\frac{{{fmt(c_con, 2)}}}{{c_{{anode}}}} = \\frac{{nFE}}{{RT}} = \\frac{{({n})(96485)({ex(E, 3)})}}"
            f"{{(8.314)(298.15)}} = {fmt(n * FARADAY * E / (R_GAS * T), 4)}$.",
            f"$c_{{anode}} = {fmt(c_con, 2)}\\,e^{{-{fmt(n * FARADAY * E / (R_GAS * T), 4)}}} = {fmt(c_dil, 3)}$ M.",
            "The positive potential confirms that the anode side is the more dilute one; this is how ion-selective "
            "and pH electrodes turn a measured voltage into a concentration.",
        ]
        answer = f"[{ion}] = ${fmt(c_dil, 3)}$ M"
        values = {"mode": mode, "n": n, "T": T, "c_dilute": c_dil, "c_conc": c_con, "E": E, "Ksp": None, "c_X": None}
    else:
        mode = "ksp"
        salt, sname, X, KX, Ksp_true = pick(rng, SILVER_HALIDES)
        c_ref = pick(rng, [0.010, 0.050, 0.10, 0.20])
        cX = pick(rng, [0.010, 0.020, 0.050, 0.10, 0.50, 1.0])
        T = T_STD
        E = round(R_GAS * T / FARADAY * math.log(c_ref * cX / Ksp_true), 3)
        ag = c_ref * math.exp(-FARADAY * E / (R_GAS * T))
        Ksp = ag * cX
        question = (
            f"To measure the $K_{{sp}}$ of {sname}, a cell is built from two silver electrodes: the cathode dips into "
            f"{qx(c_ref, 'M', 2)} AgNO₃, and the anode into {qx(cX, 'M', 2)} {KX} saturated with {pretty(salt)}. The cell "
            f"potential at 25 °C is {qx(E, 'V', 3)}. Find [Ag⁺] in the anode compartment and $K_{{sp}}$ of {pretty(salt)}."
        )
        steps = [
            "Both electrodes are Ag⁺/Ag, so this is a concentration cell: "
            "$E = \\frac{RT}{F}\\ln\\frac{[\\text{Ag}^+]_{cathode}}{[\\text{Ag}^+]_{anode}}$ ($n = 1$).",
            f"$\\ln\\frac{{{fmt(c_ref, 2)}}}{{[\\text{{Ag}}^+]}} = \\frac{{FE}}{{RT}} = \\frac{{(96485)({ex(E, 3)})}}{{(8.314)(298.15)}} = "
            f"{fmt(FARADAY * E / (R_GAS * T), 4)}$.",
            f"$[\\text{{Ag}}^+]_{{anode}} = {fmt(c_ref, 2)}\\,e^{{-{fmt(FARADAY * E / (R_GAS * T), 4)}}} = {fmt(ag, 3)}$ M.",
            f"In the anode compartment [{X}] = {fmt(cX, 2)} M (the tiny amount from the dissolved salt is negligible), so "
            f"$K_{{sp}} = [\\text{{Ag}}^+][\\text{{{X}}}] = ({fmt(ag, 3)})({fmt(cX, 2)}) = {fmt(Ksp, 2)}$.",
            "A measurable voltage gives access to concentrations far too small to titrate.",
        ]
        answer = f"[Ag⁺] = ${fmt(ag, 3)}$ M; $K_{{sp}} = {fmt(Ksp, 2)}$"
        values = {"mode": mode, "n": 1, "T": T, "c_dilute": ag, "c_conc": c_ref, "E": E, "Ksp": Ksp, "c_X": cX}
    return {"question": question, "steps": steps, "answer": answer, "values": values,
            "difficulty": "hard" if mode == "ksp" else "medium"}


# ---------------------------------------------------------------------------
# Instrumental analysis
# ---------------------------------------------------------------------------

BL_ANALYTES = [  # description, λ (nm), ε (L mol⁻¹ cm⁻¹), formula for mg/L, standard step (µM) spec
    ("the red iron(II)–1,10-phenanthroline complex (reported as iron, Fe)", 510, 1.11e4, "Fe", (10.0, 18.0, 1.0)),
    ("permanganate ion (MnO₄⁻)", 525, 2.45e3, "MnO4", (40.0, 80.0, 5.0)),
    ("NADH", 340, 6.22e3, "C21H29N7O14P2", (16.0, 32.0, 2.0)),
    ("4-nitrophenol (measured as the yellow 4-nitrophenolate ion in basic solution)", 405, 1.83e4, "C6H5NO3",
     (5.5, 10.5, 0.5)),
    ("crystal violet (C₂₅H₃₀N₃Cl)", 590, 8.7e4, "C25H30N3Cl", (1.2, 2.2, 0.1)),
]
DILUTIONS = [None, (5.00, 25.00), (10.00, 50.00), (2.00, 10.00), (1.00, 10.00), (10.00, 25.00)]


@template("beer_lambert_calibration", CHEM, ANALYT, "Spectrophotometry", "medium")
def beer_lambert_calibration(rng):
    desc, lam, eps, formula, step_spec = pick(rng, BL_ANALYTES)
    if rng.random() < 0.6:
        mode = "calibration"
        s = nice(rng, *step_spec)
        concs = [round(s * i, 4) for i in range(1, 6)]
        blank = rng.uniform(0.0, 0.010)
        absb = [round(blank + eps * 1e-6 * c + rng.uniform(-0.004, 0.004), 3) for c in concs]
        A_u = round(rng.uniform(0.15, 0.9) * absb[-1], 3)
        dil = pick(rng, DILUTIONS)
        m, b, r2 = lsq(concs, absb)
        c_meas = (A_u - b) / m
        DF = dil[1] / dil[0] if dil else 1.0
        c_orig = c_meas * DF
        eps_est = m * 1e6
        table = ", ".join(f"{ex(c)} µM: {a:.3f}" for c, a in zip(concs, absb))
        dil_txt = (f" The unknown was prepared by diluting {qx(dil[0], 'mL')} of the original sample to {qx(dil[1], 'mL')}."
                   if dil else "")
        question = (
            f"Standards of {desc} measured at {lam} nm in a 1.00 cm cell gave these absorbances (blank-corrected readings "
            f"may still show a small intercept): {table}. An unknown solution has an absorbance of ${A_u:.3f}$.{dil_txt} "
            "Use a least-squares calibration line to find the concentration of the unknown"
            + (" and of the original sample" if dil else "") + ", and estimate the molar absorptivity."
        )
        n = len(concs)
        xb = sum(concs) / n
        yb = sum(absb) / n
        steps = [
            "Beer–Lambert law: $A = \\varepsilon bc$, so absorbance is linear in concentration; fit $A = mc + b_0$ by least "
            "squares.",
            f"Means: $\\bar c = {fmt(xb, 4)}$ µM, $\\bar A = {fmt(yb, 4)}$; "
            f"$m = \\frac{{\\sum(c_i - \\bar c)(A_i - \\bar A)}}{{\\sum(c_i - \\bar c)^2}} = {fmt(m, 4)}$ µM⁻¹, "
            f"$b_0 = \\bar A - m\\bar c = {fmt(b, 3) if abs(b) >= 1e-4 else '0.0000'}$ ($r^2 = {r2:.5f}$).",
            f"Unknown: $c = \\frac{{A - b_0}}{{m}} = \\frac{{{A_u:.3f} - ({fmt(b, 3) if abs(b) >= 1e-4 else '0'})}}{{{fmt(m, 4)}}} = "
            f"{fmt(c_meas, 4)}$ µM.",
        ]
        if dil:
            steps.append(f"Dilution factor ${ex(dil[1])}/{ex(dil[0])} = {fmt(DF, 3)}$, so the original sample contains "
                         f"$({fmt(c_meas, 4)})({fmt(DF, 3)}) = {fmt(c_orig, 4)}$ µM.")
        steps.append(f"Molar absorptivity: $\\varepsilon = \\frac{{m}}{{b}} = \\frac{{{fmt(m, 4)}\\times10^{{6}}\\text{{ M}}^{{-1}}}}"
                     f"{{1.00\\text{{ cm}}}} = {fmt(eps_est, 3)}$ L·mol⁻¹·cm⁻¹, close to the literature value "
                     f"${ex(eps, 3)}$.")
        answer = (f"$c = {fmt(c_meas, 4)}$ µM" + (f" in the measured solution, ${fmt(c_orig, 4)}$ µM in the original sample"
                                                  if dil else "") + f"; $\\varepsilon \\approx {fmt(eps_est, 3)}$ L·mol⁻¹·cm⁻¹")
        values = {"mode": mode, "concs": concs, "absorbances": absb, "slope": m, "intercept": b, "r2": r2,
                  "A_unknown": A_u, "dilution_factor": DF, "c_meas": c_meas, "c_orig": c_orig, "eps_est": eps_est,
                  "eps": None, "path": None, "T_pct": None, "A": None, "c_M": None, "M": None, "mg_L": None}
    else:
        mode = "single"
        path = pick(rng, [1.00, 1.00, 0.500, 2.00])
        T_pct = nice(rng, 10.0, 85.0, 0.1)
        A = 2 - math.log10(T_pct)
        c = A / (eps * path)
        M = mm(formula)
        mgL = c * M * 1000
        question = (
            f"A solution of {desc} transmits {qx(T_pct, '%')} of the incident light at {lam} nm in a {qx(path, 'cm')} "
            f"cell. Given $\\varepsilon = {ex(eps, 3)}$ L·mol⁻¹·cm⁻¹ at this wavelength, find the absorbance, the molar "
            f"concentration and the concentration in mg/L ($M = {M:.2f}$ g/mol)."
        )
        steps = [
            f"Absorbance from percent transmittance: $A = -\\log T = 2 - \\log(\\%T) = 2 - \\log({ex(T_pct)}) = {A:.4f}$.",
            f"Beer–Lambert law: $c = \\frac{{A}}{{\\varepsilon b}} = \\frac{{{A:.4f}}}{{({ex(eps, 3)})({ex(path)})}} = "
            f"{fmt(c, 4)}$ M.",
            f"Mass concentration: $({fmt(c, 4)}\\text{{ mol/L}})({M:.2f}\\text{{ g/mol}})(1000\\text{{ mg/g}}) = {fmt(mgL, 4)}$ mg/L.",
            "Absorbances between about 0.1 and 1 give the most reliable results; "
            + ("this one is in that range." if 0.1 <= A <= 1.0 else "this one is outside it, so diluting or changing the "
               "path length would improve precision."),
        ]
        answer = f"$A = {A:.4f}$; $c = {fmt(c, 4)}$ M $= {fmt(mgL, 4)}$ mg/L"
        values = {"mode": mode, "eps": eps, "path": path, "T_pct": T_pct, "A": A, "c_M": c, "M": M, "mg_L": mgL,
                  "concs": None, "absorbances": None, "slope": None, "intercept": None, "r2": None, "A_unknown": None,
                  "dilution_factor": None, "c_meas": None, "c_orig": None, "eps_est": None}
    return {"question": question, "steps": steps, "answer": answer, "values": values,
            "difficulty": "hard" if mode == "calibration" else "easy"}


STD_ADD_CASES = [  # analyte, sample, technique, signal, unit, conc unit, standard concentrations, signal range, decimals
    ("copper", "an electroplating rinse-water sample", "flame atomic absorption at 324.8 nm", "absorbance", "",
     "mg/L", [20.0, 25.0, 50.0], (0.25, 0.70), 3),
    ("zinc", "a digested dietary-supplement solution", "flame atomic absorption at 213.9 nm", "absorbance", "",
     "mg/L", [10.0, 20.0, 25.0], (0.25, 0.70), 3),
    ("calcium", "a mineral-water sample", "flame atomic absorption at 422.7 nm", "absorbance", "",
     "mg/L", [50.0, 100.0, 200.0], (0.25, 0.70), 3),
    ("sodium", "a diluted blood-serum sample", "flame atomic emission at 589 nm", "emission intensity",
     "(arbitrary units)", "mg/L", [50.0, 100.0, 200.0], (40.0, 300.0), 1),
    ("lead", "a river-water sample", "anodic stripping voltammetry", "peak current", "nA",
     "µg/L", [50.0, 100.0, 200.0], (20.0, 150.0), 1),
]


@template("standard_addition_method", CHEM, ANALYT, "Standard addition", "hard")
def standard_addition_method(rng):
    analyte, sample, tech, sig_name, sunit, cu, cs_opts, (smin, smax), dec = pick(rng, STD_ADD_CASES)
    cs = pick(rng, cs_opts)

    def rd(x):
        return round(x, dec)

    def show(x):
        return f"{x:.{dec}f}"

    su = f" {sunit}" if sunit else ""
    if rng.random() < 0.6:
        mode = "multiple"
        Vx = pick(rng, [5.00, 10.00, 20.00, 25.00])
        Vtot = pick(rng, [50.00, 100.00])
        if Vx > Vtot / 2:
            Vtot = 100.00
        step = pick(rng, [0.50, 1.00, 2.00])
        Vs = [round(step * i, 2) for i in range(5)]
        delta = cs * step / Vtot
        c_d = delta * rng.uniform(0.6, 2.5)
        kf = rng.uniform(smin, smax) / (c_d + 4 * delta)
        S = [rd(kf * (c_d + i * delta) * (1 + rng.uniform(-0.01, 0.01))) for i in range(5)]
        x = [cs * v / Vtot for v in Vs]
        m, b, r2 = lsq(x, S)
        c_flask = b / m
        cx = c_flask * Vtot / Vx
        table = "; ".join(f"{ex(v, 3)} mL: {show(s_)}" for v, s_ in zip(Vs, S))
        question = (
            f"The {analyte} content of {sample} is determined by {tech} using standard additions. Into each of five "
            f"{qx(Vtot, 'mL', 4)} volumetric flasks, {qx(Vx, 'mL', 3)} of the sample is pipetted, followed by increasing "
            f"volumes of a {qx(cs, cu)} {analyte} standard; each flask is then diluted to the mark. Volume of standard "
            f"added and {sig_name}{su}: {table}. Find the {analyte} concentration in the original sample."
        )
        steps = [
            "Standard additions compensate for matrix effects: every flask has the same matrix, and the signal is "
            "$S = k(c_{x,flask} + c_{added})$.",
            f"Added concentration in each flask: $c_{{added}} = c_sV_s/V_{{flask}}$ = "
            + ", ".join(fmt(v, 3) for v in x) + f" {cu}.",
            f"Least-squares line of $S$ against $c_{{added}}$: slope $m = {fmt(m, 4)}$, intercept $b = {fmt(b, 4)}$ "
            f"($r^2 = {r2:.4f}$).",
            f"The x-intercept is at $c_{{added}} = -b/m = -{fmt(c_flask, 4)}$ {cu}, so the diluted sample in each flask "
            f"contains ${fmt(c_flask, 4)}$ {cu} of {analyte}.",
            f"Correct for the dilution of the sample: $c_x = {fmt(c_flask, 4)} \\times \\frac{{{ex(Vtot, 4)}}}{{{ex(Vx, 3)}}} = "
            f"{fmt(cx, 3)}$ {cu}.",
        ]
        answer = f"${fmt(cx, 3)}$ {cu} {analyte} in the original sample"
        values = {"mode": mode, "Vx": Vx, "Vtot": Vtot, "cs": cs, "Vs": Vs, "signals": S, "slope": m, "intercept": b,
                  "cx": cx, "S1": None, "S2": None, "Vs_single": None}
    else:
        mode = "single"
        Vx = pick(rng, [10.00, 20.00, 25.00, 50.00])
        Vs1 = pick(rng, [0.100, 0.200, 0.250, 0.500, 1.00])
        cx_true = cs * Vs1 / Vx / rng.uniform(0.5, 2.0)
        kf = rng.uniform(smin, smax) / ((cx_true * Vx + cs * Vs1) / (Vx + Vs1))
        S1 = rd(kf * cx_true * (1 + rng.uniform(-0.01, 0.01)))
        S2 = rd(kf * (cx_true * Vx + cs * Vs1) / (Vx + Vs1) * (1 + rng.uniform(-0.01, 0.01)))
        if S2 <= S1 * Vx / (Vx + Vs1) * 1.05:
            S2 = rd(S1 * 1.5)
        cx = S1 * cs * Vs1 / (S2 * (Vx + Vs1) - S1 * Vx)
        question = (
            f"The {analyte} content of {sample} is determined by {tech}. A {qx(Vx, 'mL', 3)} portion gives a "
            f"{sig_name} of {show(S1)}{su}. After {qx(Vs1, 'mL', 3)} of a {qx(cs, cu)} {analyte} standard is added to "
            f"this portion, the {sig_name} rises to {show(S2)}{su}. Assuming the signal is proportional to concentration, "
            f"find the {analyte} concentration in the sample."
        )
        steps = [
            "Signal proportional to concentration: before the spike $S_1 = kc_x$; after it "
            "$S_2 = k\\frac{c_xV_x + c_sV_s}{V_x + V_s}$ (the spike also dilutes the sample slightly).",
            "Dividing eliminates $k$: $\\frac{S_2}{S_1} = \\frac{c_xV_x + c_sV_s}{c_x(V_x + V_s)}$, so "
            "$c_x = \\frac{S_1c_sV_s}{S_2(V_x + V_s) - S_1V_x}$.",
            f"$c_x = \\frac{{({show(S1)})({ex(cs)})({ex(Vs1, 3)})}}{{({show(S2)})({ex(Vx, 3)} + {ex(Vs1, 3)}) - "
            f"({show(S1)})({ex(Vx, 3)})}} = {fmt(cx, 3)}$ {cu}.",
            f"Check: the spike adds ${fmt(cs * Vs1 / (Vx + Vs1), 3)}$ {cu} to a sample of ${fmt(cx * Vx / (Vx + Vs1), 3)}$ {cu} "
            f"(after dilution), and the signal ratio ${fmt(S2 / S1, 4)}$ matches "
            f"$\\frac{{{fmt(cx * Vx / (Vx + Vs1) + cs * Vs1 / (Vx + Vs1), 4)}}}{{{fmt(cx, 4)}}} = "
            f"{fmt((cx * Vx / (Vx + Vs1) + cs * Vs1 / (Vx + Vs1)) / cx, 4)}$.",
        ]
        answer = f"${fmt(cx, 3)}$ {cu} {analyte}"
        values = {"mode": mode, "Vx": Vx, "Vtot": None, "cs": cs, "Vs": None, "signals": None, "slope": None,
                  "intercept": None, "cx": cx, "S1": S1, "S2": S2, "Vs_single": Vs1}
    return {"question": question, "steps": steps, "answer": answer, "values": values}
