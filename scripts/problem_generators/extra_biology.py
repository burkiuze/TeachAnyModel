"""Additional Biology templates: genetics, molecular and cell biology, physiology, epidemiology,
biochemistry and ecology.

Genetics: ABO/Rh blood-group crosses (multiple alleles, codominance), carrier risk of an unaffected
sibling of an affected child, polygenic additive traits and test crosses with independent assortment.
Molecular and cell biology / microbiology: genome replication time with many origins, hemocytometer counts
with dye-exclusion viability, cell density from OD600 calibration.
Physiology: osmolarity and tonicity, Fick's law of diffusion, minute and alveolar ventilation, renal clearance
and GFR, Kleiber scaling of metabolic rate, repeated drug dosing to steady state.
Epidemiology: herd-immunity threshold and vaccine coverage, SIR epidemic growth, peak and final size.
Biochemistry: reversible enzyme inhibition (apparent Km and Vmax), Lineweaver–Burk analysis and the ATP yield
of fatty-acid beta-oxidation.
Ecology: Lotka–Volterra predator–prey and competition models, cohort life tables.
"""

import math
from fractions import Fraction

from .chemistry import molar_mass
from .common import fmt, nice, pick, template

BIO = "Biology"


# ---------------------------------------------------------------------------
# Formatting helpers
# ---------------------------------------------------------------------------


def ex(x, min_sig=1):
    """Format ``x`` with the fewest significant figures (at least ``min_sig``) that show it exactly."""
    if isinstance(x, int) and abs(x) < 100000:
        return str(x)
    x = float(x)
    if x == 0:
        return "0"
    for s in range(min_sig, 12):
        if math.isclose(float(f"{x:.{s}g}"), x, rel_tol=1e-12):
            return fmt(x, s)
    return fmt(x, 12)


def qx(x, unit="", min_sig=1):
    """Exact quantity ``$x$ unit`` with ``x`` shown to as many figures as it has."""
    s = f"${ex(x, min_sig)}$"
    return f"{s} {unit}" if unit else s


def clean(x):
    """Strip float noise from products of displayed numbers (e.g. 0.235 * 2.5)."""
    return float(f"{x:.12g}")


def cap(s):
    return s[0].upper() + s[1:]


def ftex(fr):
    fr = Fraction(fr)
    return str(fr.numerator) if fr.denominator == 1 else f"\\frac{{{fr.numerator}}}{{{fr.denominator}}}"


def fslash(fr):
    fr = Fraction(fr)
    return str(fr.numerator) if fr.denominator == 1 else f"{fr.numerator}/{fr.denominator}"


def prob_tex(fr, max_den=5000):
    """A probability as an exact fraction (when short) followed by its decimal value (TeX, no $)."""
    fr = Fraction(fr)
    if fr.denominator == 1:
        return str(fr.numerator)
    x = float(fr)
    dec = None
    for s in range(1, 5):
        if math.isclose(float(f"{x:.{s}g}"), x, rel_tol=1e-12):
            dec = f"= {fmt(x, s)}"
            break
    if dec is None:
        dec = f"\\approx {fmt(x, 3)}"
    if fr.denominator <= max_den:
        return f"{ftex(fr)} {dec}"
    return dec[2:] if dec.startswith("= ") else fmt(x, 3)


def pc(x, s=3):
    """Percentage (TeX, no $)."""
    return f"{fmt(100 * x, s)}\\%"


def _punnett(g1, g2, key):
    """Offspring distribution for a one-gene cross; ``key`` maps two alleles to an outcome label."""
    out = {}
    for a in g1:
        for b in g2:
            k = key(a, b)
            out[k] = out.get(k, Fraction(0)) + Fraction(1, 4)
    return out


# ---------------------------------------------------------------------------
# Genetics: ABO and Rh blood groups
# ---------------------------------------------------------------------------

ABO_TEX = {"A": "I^A", "B": "I^B", "O": "i"}
ABO_TYPES = ("A", "B", "AB", "O")


def _abo_genotype(a, b):
    return "".join(sorted(a + b, key="ABO".index))


def _abo_type(g):
    if "A" in g and "B" in g:
        return "AB"
    for t in "AB":
        if t in g:
            return t
    return "O"


def _abo_tex(g):
    return "".join(ABO_TEX[ch] for ch in g)


def _gametes_text(g, tex):
    alleles = sorted(set(g), key=g.index)
    if len(alleles) == 1:
        return f"only ${tex(alleles[0])}$ gametes"
    return f"${tex(alleles[0])}$ and ${tex(alleles[1])}$ gametes, each with probability $\\frac{{1}}{{2}}$"


# genotype -> [(description used in the question, reasoning used in the solution)]
ABO_DESC = {
    "AA": [("has type A blood and has been shown by genotyping to be homozygous",
            "genotyping shows that {p} is homozygous, so {p} is $I^AI^A$."),
           ("has type A blood, and both of {pos} parents have type AB blood",
            "both of {pos} parents are $I^AI^B$, so {p} received either $I^A$ or $I^B$ from each of them; the only "
            "way to be type A is $I^AI^A$.")],
    "AO": [("has type A blood and a type O mother",
            "{pos} type O mother ($ii$) could only pass on $i$, so {p} is $I^Ai$."),
           ("has type A blood and a type O father",
            "{pos} type O father ($ii$) could only pass on $i$, so {p} is $I^Ai$."),
           ("has type A blood and already has a type O child from an earlier relationship",
            "a type O child ($ii$) receives $i$ from each parent, so {p} must carry $i$: $I^Ai$.")],
    "BB": [("has type B blood and has been shown by genotyping to be homozygous",
            "genotyping shows that {p} is homozygous, so {p} is $I^BI^B$."),
           ("has type B blood, and both of {pos} parents have type AB blood",
            "both of {pos} parents are $I^AI^B$, so {p} received either $I^A$ or $I^B$ from each of them; the only "
            "way to be type B is $I^BI^B$.")],
    "BO": [("has type B blood and a type O mother",
            "{pos} type O mother ($ii$) could only pass on $i$, so {p} is $I^Bi$."),
           ("has type B blood and a type O father",
            "{pos} type O father ($ii$) could only pass on $i$, so {p} is $I^Bi$."),
           ("has type B blood and already has a type O child from an earlier relationship",
            "a type O child ($ii$) receives $i$ from each parent, so {p} must carry $i$: $I^Bi$.")],
    "AB": [("has type AB blood",
            "because $I^A$ and $I^B$ are codominant, type AB has only one possible genotype, $I^AI^B$.")],
    "OO": [("has type O blood", "type O is the recessive phenotype, so the genotype is $ii$.")],
}

RH_DESC = {
    "dd": [("is Rh-negative", "is Rh-negative, so $dd$")],
    "Dd": [("is Rh-positive, although {pos} mother is Rh-negative",
            "is Rh-positive but received $d$ from {pos} Rh-negative ($dd$) mother, so $Dd$"),
           ("is Rh-positive and known to be heterozygous", "is a known heterozygote, $Dd$")],
    "DD": [("is Rh-positive and known to be homozygous", "is a known homozygote, $DD$")],
}


@template("abo_rh_blood_group_cross", BIO, "Genetics", "Multiple alleles and codominance: ABO and Rh blood groups",
          "medium")
def abo_rh_blood_group_cross(rng):
    genotypes = ["AA", "AO", "BB", "BO", "AB", "OO"]
    g1, g2 = pick(rng, genotypes), pick(rng, genotypes)
    she, he = {"p": "she", "pos": "her"}, {"p": "he", "pos": "his"}
    desc1, why1 = pick(rng, ABO_DESC[g1])
    desc2, why2 = pick(rng, ABO_DESC[g2])
    use_rh = rng.random() < 0.45
    abo = _punnett(g1, g2, lambda a, b: _abo_type(a + b))
    geno = _punnett(g1, g2, _abo_genotype)
    p = {t: abo.get(t, Fraction(0)) for t in ABO_TYPES}
    rh1 = rh2 = None
    p_neg = Fraction(0)
    if use_rh:
        rh1, rh2 = pick(rng, ["DD", "Dd", "Dd", "dd"]), pick(rng, ["DD", "Dd", "Dd", "dd"])
        rdesc1, rwhy1 = pick(rng, RH_DESC[rh1])
        rdesc2, rwhy2 = pick(rng, RH_DESC[rh2])
        rh_geno = _punnett(rh1, rh2, lambda a, b: "".join(sorted(a + b)))
        p_neg = rh_geno.get("dd", Fraction(0))
    mode = pick(rng, ["single", "single", "both", "at_least", "exactly"])
    impossible = [t for t in ABO_TYPES if p[t] == 0]
    if mode == "single" and impossible and rng.random() < 0.2:
        target = pick(rng, impossible)
    else:
        target = pick(rng, [t for t in ABO_TYPES if p[t] > 0])
    target_rh, p_rh = None, Fraction(1)
    if use_rh:
        target_rh = pick(rng, [s for s, pr in (("+", 1 - p_neg), ("-", p_neg)) if pr > 0])
        p_rh = p_neg if target_rh == "-" else 1 - p_neg
    p_child = p[target] * p_rh
    if p_child == 1:
        mode = "single"
    n = k = None
    if mode == "single":
        p_ans = p_child
    elif mode == "both":
        n = 2
        p_ans = p_child ** 2
    elif mode == "at_least":
        n = rng.randint(2, 4)
        p_ans = 1 - (1 - p_child) ** n
    else:
        n = rng.randint(3, 5)
        k = rng.randint(1, n - 1)
        p_ans = math.comb(n, k) * p_child ** k * (1 - p_child) ** (n - k)

    rh_word = "" if not use_rh else (", Rh-positive" if target_rh == "+" else ", Rh-negative")
    phrase = f"type {target}{rh_word} blood"
    ask = {"single": f"their first child will have {phrase}",
           "both": f"their first two children will both have {phrase}",
           "at_least": f"at least one of their {n} children will have {phrase}",
           "exactly": f"exactly {k} of their {n} children will have {phrase}"}[mode]
    intro = ("In the ABO blood-group system the alleles $I^A$ and $I^B$ are codominant, and both are completely "
             "dominant over $i$.")
    if use_rh:
        intro += (" The Rh(D) blood group is controlled by a gene on a different chromosome, with $D$ (Rh-positive) "
                  "completely dominant over $d$ (Rh-negative).")
    woman = "A woman " + desc1.format(**she) + (f", and she {rdesc1.format(**she)}" if use_rh else "") + "."
    man = "Her partner " + desc2.format(**he) + (f", and he {rdesc2.format(**he)}" if use_rh else "") + "."
    question = (f"{intro} {woman} {man} Ignore rare variants such as the Bombay phenotype. (a) What is the probability "
                f"of each ABO blood type for a child of this couple? (b) What is the probability that {ask}?")

    order = {"AA": 0, "AB": 1, "AO": 2, "BB": 3, "BO": 4, "OO": 5}
    if impossible:
        note = (f" This couple cannot have a type {' or '.join(impossible)} child — the kind of exclusion used in "
                "disputed-parentage cases.")
    else:
        note = " All four ABO types are possible."
    steps = [
        f"Woman: {why1.format(**she)}",
        f"Partner: {why2.format(**he)}",
        f"Gametes (law of segregation): the woman (${_abo_tex(g1)}$) produces {_gametes_text(g1, ABO_TEX.get)}; her "
        f"partner (${_abo_tex(g2)}$) produces {_gametes_text(g2, ABO_TEX.get)}.",
        "Punnett square (four equally likely gamete combinations): "
        + ", ".join(f"${_abo_tex(g)}$: ${ftex(pr)}$" for g, pr in sorted(geno.items(), key=lambda kv: order[kv[0]]))
        + ".",
        "ABO phenotypes ($I^A$ and $I^B$ are both expressed when present together; $i$ shows only as $ii$): "
        + ", ".join(f"type {t}: ${ftex(p[t])}$" for t in ABO_TYPES) + "." + note,
    ]
    if use_rh:
        rh_order = {"DD": 0, "Dd": 1, "dd": 2}
        steps += [
            f"Rh genotypes: the woman {rwhy1.format(**she)}; her partner {rwhy2.format(**he)}.",
            f"Rh cross ${rh1} \\times {rh2}$: "
            + ", ".join(f"${g}$: ${ftex(pr)}$" for g, pr in sorted(rh_geno.items(), key=lambda kv: rh_order[kv[0]]))
            + f", so $P(\\text{{Rh-negative}}) = {ftex(p_neg)}$ and $P(\\text{{Rh-positive}}) = {ftex(1 - p_neg)}$.",
            "The ABO gene (chromosome 9) and the RhD gene (chromosome 1) assort independently, so the probabilities "
            "multiply (product rule).",
            f"For one child: $P(\\text{{type {target}}}) \\times P(\\text{{Rh-{'positive' if target_rh == '+' else 'negative'}}})"
            f" = {ftex(p[target])} \\times {ftex(p_rh)} = {ftex(p_child)}$.",
        ]
    else:
        steps.append(f"For one child: $P(\\text{{type {target}}}) = {ftex(p_child)}$.")
    if mode == "single":
        if p_child == 0:
            steps.append("The requested blood type cannot arise from these parents, so the probability is 0.")
    elif mode == "both":
        steps.append("Given the parents' genotypes, each child is an independent event, so multiply: "
                     f"$P = ({ftex(p_child)})^2 = {prob_tex(p_ans)}$.")
    elif mode == "at_least":
        steps.append("Use the complement (no child of that type) and independence between children: "
                     f"$P = 1 - (1 - p)^{{{n}}} = 1 - ({ftex(1 - p_child)})^{{{n}}} = {prob_tex(p_ans)}$.")
    else:
        steps.append("Binomial probability (independent children, $p$ per child): $P = \\binom{n}{k}p^k(1-p)^{n-k} = "
                     f"\\binom{{{n}}}{{{k}}}({ftex(p_child)})^{{{k}}}({ftex(1 - p_child)})^{{{n - k}}} = {prob_tex(p_ans)}$.")
    part_a = ", ".join(f"type {t}: {fslash(p[t])}" for t in ABO_TYPES)
    answer = f"(a) {part_a}; (b) $P = {prob_tex(p_ans)}$"
    values = {"woman": g1, "partner": g2, "rh_woman": rh1, "rh_partner": rh2,
              "p_A": float(p["A"]), "p_B": float(p["B"]), "p_AB": float(p["AB"]), "p_O": float(p["O"]),
              "target": target, "target_rh": target_rh, "p_child": float(p_child), "mode": mode, "n": n, "k": k,
              "p_answer": float(p_ans)}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Genetics: carrier risk in an autosomal recessive pedigree
# ---------------------------------------------------------------------------

AR_DISORDERS = [  # disorder, incidences (1 in N, perfect squares so that q = 1/sqrt(N) is exact)
    ("cystic fibrosis", [2500, 3600]),
    ("phenylketonuria (PKU)", [10000, 12100, 14400]),
    ("Tay–Sachs disease", [2500, 3600]),
    ("spinal muscular atrophy", [6400, 8100, 10000]),
    ("sickle-cell disease", [400, 625, 900]),
    ("oculocutaneous albinism", [10000, 14400, 19600]),
]


@template("recessive_carrier_risk_pedigree", BIO, "Genetics", "Carrier risk for autosomal recessive disorders",
          "medium")
def recessive_carrier_risk_pedigree(rng):
    disease, incidences = pick(rng, AR_DISORDERS)
    person = pick(rng, ["woman", "man"])
    pos = "her" if person == "woman" else "his"
    sib = pick(rng, ["brother", "sister"])
    kind = pick(rng, ["population", "population", "sibling", "carrier", "screen"])
    Px = Fraction(2, 3)
    N = root = det = qa = None
    steps = [
        f"The {person} and both parents are unaffected, but the {sib} is affected ($aa$) and must have received $a$ "
        "from each parent. So both parents are heterozygous carriers ($Aa$).",
        "$Aa \\times Aa$ gives $AA : Aa : aa = \\frac{1}{4} : \\frac{1}{2} : \\frac{1}{4}$. We already know that the "
        f"{person} is unaffected, which rules out $aa$, so $P(\\text{{carrier}}) = \\frac{{1/2}}{{3/4}} = \\frac{{2}}{{3}}$.",
    ]
    if kind in ("population", "screen"):
        N = pick(rng, incidences)
        root = math.isqrt(N)
        qa = Fraction(1, root)
        prior = 2 * qa / (1 + qa)
        partner_txt = (f"The partner is unaffected, has no family history of the disorder and comes from a population "
                       f"in which {disease} affects 1 in {N} births (assume Hardy–Weinberg equilibrium)")
        steps.append(
            f"Partner (Hardy–Weinberg): $q^2 = \\frac{{1}}{{{N}}}$, so $q = \\frac{{1}}{{{root}}} = {fmt(float(qa), 3)}$ "
            f"and the carrier frequency is $2pq = 2({fmt(1 - float(qa), 4)})({fmt(float(qa), 3)}) = "
            f"{fmt(float(2 * qa * (1 - qa)), 3)}$. Because the partner is unaffected, condition on not being $aa$: "
            f"$P_0 = \\frac{{2pq}}{{1 - q^2}} = \\frac{{2q}}{{1 + q}} = \\frac{{2}}{{{root + 1}}} = {fmt(float(prior), 3)}$ "
            "(practically equal to $2pq$ for a rare allele).")
        if kind == "screen":
            det = pick(rng, [80, 85, 90, 95, 98])
            S = Fraction(det, 100)
            Pp = prior * (1 - S) / (prior * (1 - S) + (1 - prior))
            partner_txt += (f", and has just tested negative on a carrier screen that detects {det}% of carriers "
                            "and gives no false positives")
            steps.append(
                "Update for the negative screen with Bayes' theorem. A carrier tests negative with probability "
                f"$1 - {fmt(det / 100, 2)} = {fmt(1 - det / 100, 2)}$, a non-carrier always tests negative: "
                f"$P = \\frac{{P_0(1 - S)}}{{P_0(1 - S) + (1 - P_0)}} = \\frac{{{fmt(float(prior), 4)} \\times "
                f"{fmt(1 - det / 100, 2)}}}{{{fmt(float(prior), 4)} \\times {fmt(1 - det / 100, 2)} + "
                f"{fmt(float(1 - prior), 4)}}} = {fmt(float(Pp), 3)}$ — the residual risk after a negative test.")
        else:
            Pp = prior
    elif kind == "sibling":
        Pp = Fraction(2, 3)
        partner_txt = ("The partner is also unaffected and has unaffected parents, but has a sibling with the "
                       "disorder")
        steps.append("Partner: by exactly the same reasoning (unaffected, unaffected parents, affected sibling), "
                     "$P = \\frac{2}{3}$.")
    else:
        Pp = Fraction(1)
        partner_txt = "The partner has been tested and is a known heterozygous carrier"
        steps.append("Partner: a known carrier, so $P = 1$.")
    P1 = Px * Pp / 4
    pp_tex = ftex(Pp) if Pp.denominator <= 5000 else fmt(float(Pp), 4)
    steps.append(
        "A child can only be affected if both parents are carriers, and then has a $\\frac{1}{4}$ chance of being "
        f"$aa$: $P = \\frac{{2}}{{3}} \\times {pp_tex} \\times \\frac{{1}}{{4}} = {prob_tex(P1)}$.")
    n = P_any = None
    if rng.random() < 0.5:
        n = rng.randint(2, 4)
        Pboth = Px * Pp
        P_any = Pboth * (1 - Fraction(3, 4) ** n)
        naive = 1 - (1 - P1) ** n
        steps.append(
            f"For {n} children the outcomes are not independent, because they all depend on whether both parents are "
            "carriers. Condition on that event: $P(\\ge 1 \\text{ affected}) = P(\\text{both carriers})"
            f"\\left[1 - \\left(\\tfrac{{3}}{{4}}\\right)^{{{n}}}\\right] = {fmt(float(Pboth), 4)} \\times "
            f"{fmt(1 - 0.75 ** n, 4)} = {fmt(float(P_any), 3)}$. (The naive $1 - (1 - P_1)^{{{n}}} = "
            f"{fmt(float(naive), 3)}$ ignores this dependence.)")
    question = (
        f"{cap(disease)} is an autosomal recessive disorder. A {person} is unaffected, as are both of {pos} parents, "
        f"but {pos} {sib} has {disease}. {partner_txt}. Assume complete penetrance and no new mutations. (a) What is "
        f"the probability that the {person} is a carrier? (b) What is the probability that the partner is a carrier? "
        f"(c) What is the probability that the couple's first child will have {disease}?"
        + (f" (d) If they have {n} children, what is the probability that at least one of them is affected?" if n else "")
    )
    answer = (f"(a) $\\frac{{2}}{{3}}$; (b) ${prob_tex(Pp)}$; (c) ${prob_tex(P1)}$"
              + (f"; (d) ${fmt(float(P_any), 3)}$" if n else ""))
    values = {"partner": kind, "N": N, "q": float(qa) if qa is not None else None,
              "detection": det / 100 if det is not None else None, "P_person": float(Px), "P_partner": float(Pp),
              "P_child": float(P1), "n": n, "P_any": float(P_any) if P_any is not None else None}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Genetics: polygenic (additive) inheritance
# ---------------------------------------------------------------------------

POLY_TRAITS = [  # trait, unit, organism, base range, increment range, (high word, low word)
    ("plant height", "cm", "a crop plant", (20, 60, 2), (2, 10, 1), ("tall", "short")),
    ("ear length", "cm", "maize", (6, 10, 1), (1, 3, 0.5), ("long", "short")),
    ("fruit mass", "g", "a squash species", (100, 300, 10), (10, 50, 5), ("heavy", "light")),
    ("seed mass", "mg", "a bean species", (200, 400, 10), (20, 60, 5), ("heavy", "light")),
]
POLY_LETTERS = "ABCD"


def _poly_genotype(counts):
    """[2, 1, 0] -> 'AABbcc'."""
    return "".join(L * c + L.lower() * (2 - c) for L, c in zip(POLY_LETTERS, counts))


def _locus_dist(x, y):
    """Distribution of contributing alleles (0, 1, 2) in offspring of parents carrying x and y of them."""
    p1, p2 = Fraction(x, 2), Fraction(y, 2)
    return [(1 - p1) * (1 - p2), p1 * (1 - p2) + (1 - p1) * p2, p1 * p2]


def _convolve(a, b):
    out = [Fraction(0)] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            out[i + j] += x * y
    return out


@template("polygenic_additive_trait", BIO, "Genetics", "Polygenic inheritance (additive model)", "medium")
def polygenic_additive_trait(rng):
    trait, unit, org, base_rng, inc_rng, (hi_w, lo_w) = pick(rng, POLY_TRAITS)
    low = nice(rng, *base_rng)
    inc = nice(rng, *inc_rng)
    mode = pick(rng, ["f2", "f2", "infer", "cross"])
    model = ("each contributing allele (capital letter) adds the same amount, alleles act additively (no dominance or "
             "epistasis), and environmental effects are negligible")
    if mode in ("f2", "infer"):
        n = pick(rng, [2, 3, 3, 4])
        high = clean(low + 2 * n * inc)
        dist = [Fraction(math.comb(2 * n, j), 4 ** n) for j in range(2 * n + 1)]
        classes = [clean(low + j * inc) for j in range(2 * n + 1)]
        F1 = clean(low + n * inc)
        k = rng.randint(0, 2 * n)
        frac = dist[k]
        lows, highs = POLY_LETTERS[:n].lower() * 1, POLY_LETTERS[:n]
        g_low = "".join(ch * 2 for ch in lows)
        g_high = "".join(ch * 2 for ch in highs)
        coeffs = " : ".join(str(math.comb(2 * n, j)) for j in range(2 * n + 1))
        if mode == "f2":
            k2 = rng.randint(n + 1, 2 * n)
            frac_ge = sum(dist[k2:], Fraction(0))
            question = (
                f"{cap(trait)} in {org} is controlled by {n} unlinked genes ({', '.join(highs)}), each with two alleles; "
                f"{model}. A true-breeding line ${g_low}$ has a {trait} of {qx(low, unit)} and a true-breeding line "
                f"${g_high}$ has {qx(high, unit)}. The two lines are crossed and the F₁ are intercrossed to produce an "
                f"F₂. (a) How much does each contributing allele add? (b) What is the {trait} of the F₁? (c) How many "
                f"phenotypic classes appear in the F₂? (d) What fraction of the F₂ has a {trait} of exactly "
                f"{qx(classes[k], unit)}? (e) What fraction of the F₂ has a {trait} of at least {qx(classes[k2], unit)}?"
            )
            steps = [
                f"The {hi_w} line carries $2n = {2 * n}$ contributing alleles and the {lo_w} line none, so each allele adds "
                f"$\\frac{{{ex(high)} - {ex(low)}}}{{{2 * n}}} = {ex(inc)}$ {unit}.",
            ]
        else:
            question = (
                f"Two true-breeding lines of {org} differ in {trait}: the {lo_w} line has {qx(low, unit)} and the "
                f"{hi_w} line {qx(high, unit)}. The difference is due to several unlinked genes with two alleles each; "
                f"{model}. The lines are crossed and the F₁ intercrossed. In a large F₂, a fraction "
                f"$\\frac{{1}}{{{4 ** n}}}$ of the individuals are as {lo_w} as the {lo_w} parent, and the same fraction "
                f"are as {hi_w} as the {hi_w} parent. (a) How many genes are involved? (b) How much does each contributing "
                f"allele add? (c) How many phenotypic classes appear in the F₂? (d) What fraction of the F₂ has a {trait} "
                f"of exactly {qx(classes[k], unit)}?"
            )
            steps = [
                "An F₂ individual is as extreme as one parent only if it received no contributing allele (or only "
                "contributing alleles) at all $2n$ allele positions, each with probability $\\frac{1}{2}$: "
                "$P = (\\frac{1}{2})^{2n} = (\\frac{1}{4})^n$.",
                f"$(\\frac{{1}}{{4}})^n = \\frac{{1}}{{{4 ** n}}}$ gives $n = \\frac{{\\ln {4 ** n}}}{{\\ln 4}} = {n}$ genes.",
                f"Each of the $2n = {2 * n}$ contributing alleles adds $\\frac{{{ex(high)} - {ex(low)}}}{{{2 * n}}} = "
                f"{ex(inc)}$ {unit}.",
            ]
        steps += [
            f"The F₁ is heterozygous at every locus (${''.join(L + L.lower() for L in highs)}$), with {n} contributing "
            f"alleles: {trait} $= {ex(low)} + {n} \\times {ex(inc)} = {ex(F1)}$ {unit}, exactly the mid-parent value.",
            f"Each F₁ gamete carries a contributing allele at each locus with probability $\\frac{{1}}{{2}}$, so the number "
            f"$k$ of contributing alleles in an F₂ individual is binomial with $2n = {2 * n}$ trials and $p = \\frac{{1}}{{2}}$: "
            f"$P(k) = \\binom{{{2 * n}}}{{k}}/{4 ** n}$. There are $2n + 1 = {2 * n + 1}$ phenotypic classes "
            f"({', '.join(ex(c) for c in classes)} {unit}) in the ratio {coeffs}.",
            f"{cap(trait)} {qx(classes[k], unit)} means $k = \\frac{{{ex(classes[k])} - {ex(low)}}}{{{ex(inc)}}} = {k}$: "
            f"$P = \\binom{{{2 * n}}}{{{k}}}/{4 ** n} = {prob_tex(frac)}$.",
        ]
        values = {"mode": mode, "n": n, "low": low, "inc": inc, "high": high, "F1": F1, "n_classes": 2 * n + 1,
                  "k": k, "value": classes[k], "frac": float(frac)}
        answer_parts = []
        if mode == "f2":
            steps.append(
                f"At least {qx(classes[k2], unit)} means $k \\ge {k2}$: $P = \\frac{{"
                + " + ".join(str(math.comb(2 * n, j)) for j in range(k2, 2 * n + 1))
                + f"}}{{{4 ** n}}} = {prob_tex(frac_ge)}$.")
            values.update({"k2": k2, "value2": classes[k2], "frac_ge": float(frac_ge)})
            answer = (f"(a) ${ex(inc)}$ {unit} per allele; (b) ${ex(F1)}$ {unit}; (c) {2 * n + 1} classes; "
                      f"(d) ${prob_tex(frac)}$; (e) ${prob_tex(frac_ge)}$")
        else:
            answer = (f"(a) {n} genes; (b) ${ex(inc)}$ {unit} per allele; (c) {2 * n + 1} classes; "
                      f"(d) ${prob_tex(frac)}$")
        steps.append("With more genes the classes become more numerous and closer together, and together with "
                     "environmental variation they blend into the continuous, bell-shaped distribution typical of "
                     "quantitative traits.")
        del answer_parts
        return {"question": question, "steps": steps, "answer": answer, "values": values}

    # mode == "cross": two specified genotypes at three loci
    n = 3
    for _ in range(1000):
        c1 = [rng.randint(0, 2) for _ in range(n)]
        c2 = [rng.randint(0, 2) for _ in range(n)]
        if sum(1 for a, b in zip(c1, c2) if a == 1 or b == 1) >= 2:
            break
    g1, g2 = _poly_genotype(c1), _poly_genotype(c2)
    v1, v2 = clean(low + sum(c1) * inc), clean(low + sum(c2) * inc)
    dist = [Fraction(1)]
    locus_txt = []
    for L, a, b in zip(POLY_LETTERS, c1, c2):
        d = _locus_dist(a, b)
        dist = _convolve(dist, d)
        locus_txt.append(f"locus {L} (${g1[POLY_LETTERS.index(L) * 2:POLY_LETTERS.index(L) * 2 + 2]} \\times "
                         f"{g2[POLY_LETTERS.index(L) * 2:POLY_LETTERS.index(L) * 2 + 2]}$): "
                         + ", ".join(f"{j}: ${ftex(x)}$" for j, x in enumerate(d) if x > 0))
    possible = [j for j, x in enumerate(dist) if x > 0]
    k = pick(rng, possible)
    value = clean(low + k * inc)
    frac = dist[k]
    mean_k = sum(j * x for j, x in enumerate(dist))
    mean = clean(low + float(mean_k) * inc)
    question = (
        f"{cap(trait)} in {org} is controlled by three unlinked genes (A, B, C), each with two alleles; {model}. The "
        f"genotype $aabbcc$ has a {trait} of {qx(low, unit)} and each contributing allele adds {qx(inc, unit)}. A plant "
        f"of genotype ${g1}$ is crossed with one of genotype ${g2}$. (a) What are the phenotypes of the two parents? "
        f"(b) What is the probability that an offspring has a {trait} of {qx(value, unit)}? (c) What is the expected "
        f"(mean) {trait} of the offspring?"
    )
    steps = [
        f"Parents: ${g1}$ has {sum(c1)} contributing alleles, so ${ex(low)} + {sum(c1)} \\times {ex(inc)} = {ex(v1)}$ "
        f"{unit}; ${g2}$ has {sum(c2)}, so ${ex(low)} + {sum(c2)} \\times {ex(inc)} = {ex(v2)}$ {unit}.",
        "Treat each locus separately (unlinked genes assort independently). Number of contributing alleles an "
        "offspring receives at each locus — " + "; ".join(locus_txt) + ".",
        "Add the counts over the three loci (multiply the probabilities of every combination that gives the same "
        "total): " + ", ".join(f"$k = {j}$: ${ftex(x)}$" for j, x in enumerate(dist) if x > 0) + ".",
        f"{cap(trait)} {qx(value, unit)} requires $k = \\frac{{{ex(value)} - {ex(low)}}}{{{ex(inc)}}} = {k}$ "
        f"contributing alleles: $P = {prob_tex(frac)}$.",
        f"Mean: $E[k] = \\sum k P(k) = {ex(float(mean_k))}$, so the mean {trait} is ${ex(low)} + {ex(float(mean_k))} "
        f"\\times {ex(inc)} = {ex(mean)}$ {unit} — the mid-parent value $\\frac{{{ex(v1)} + {ex(v2)}}}{{2}}$, as "
        "expected for purely additive genes.",
    ]
    answer = (f"(a) ${ex(v1)}$ {unit} and ${ex(v2)}$ {unit}; (b) $P = {prob_tex(frac)}$; (c) mean ${ex(mean)}$ {unit}")
    values = {"mode": mode, "g1": g1, "g2": g2, "low": low, "inc": inc, "v1": v1, "v2": v2, "k": k, "value": value,
              "frac": float(frac), "mean": mean, "dist": [float(x) for x in dist]}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Genetics: test crosses with independent assortment
# ---------------------------------------------------------------------------

TESTCROSS_SETS = [  # organism, offspring noun, [(letter, dominant phenotype, recessive phenotype)]
    ("a species of flowering plant", "plants",
     [("T", "tall", "dwarf"), ("P", "purple flowers", "white flowers"), ("S", "smooth seeds", "wrinkled seeds")]),
    ("guinea pigs", "pups",
     [("B", "black fur", "brown fur"), ("R", "rough coat", "smooth coat"), ("L", "short hair", "long hair")]),
    ("a species of beetle", "beetles",
     [("G", "green body", "brown body"), ("L", "long antennae", "short antennae"),
      ("S", "spotted wing covers", "plain wing covers")]),
]


def _multinomial_equal(rng, n, m):
    counts = [0] * m
    for _ in range(n):
        counts[rng.randrange(m)] += 1
    return counts


@template("testcross_independent_assortment", BIO, "Genetics", "Test crosses and independent assortment", "easy")
def testcross_independent_assortment(rng):
    org, noun, genes = pick(rng, TESTCROSS_SETS)
    mode = pick(rng, ["predict", "predict", "infer"])
    nl = 3 if mode == "infer" else pick(rng, [2, 3, 3])
    genes = genes[:nl]
    while True:
        het = [rng.random() < 0.6 for _ in range(nl)]
        if any(het):
            break
    letters = [g[0] for g in genes]
    genotype = "".join(L + (L.lower() if h else L) for L, h in zip(letters, het))
    tester = "".join(L.lower() * 2 for L in letters)
    h = sum(het)
    relations = ", ".join(f"{d} ({L}) is dominant to {r} ({L.lower()})" for L, d, r in genes)
    gam_tester = "".join(L.lower() for L in letters)
    # gametes of the tested parent
    gametes = [""]
    for L, hh in zip(letters, het):
        gametes = [g + a for g in gametes for a in ((L, L.lower()) if hh else (L,))]
    steps = [
        f"The tester ${tester}$ produces only ${gam_tester}$ gametes, so each offspring's phenotype directly shows "
        "which alleles it received from the tested parent.",
    ]
    if mode == "predict":
        target = [pick(rng, ["D", "R"]) for _ in range(nl)]
        if rng.random() < 0.85:  # usually ask for a class that can occur
            target = [t if hh else "D" for t, hh in zip(target, het)]
        p_t = Fraction(1)
        for t, hh in zip(target, het):
            p_t *= Fraction(1, 2) if hh else (Fraction(1) if t == "D" else Fraction(0))
        N = 8 * rng.randint(10, 100)
        expected = N * p_t
        p_same = Fraction(1, 2 ** h)
        label = ", ".join(d if t == "D" else r for (L, d, r), t in zip(genes, target))
        question = (
            f"In {org}, {relations}. The genes are on different chromosomes and assort independently. An individual of "
            f"genotype ${genotype}$ is test-crossed to a ${tester}$ individual, producing {N} offspring. (a) How many "
            f"phenotypic classes are expected among the offspring, and in what ratio? (b) How many of the {N} {noun} are "
            f"expected to show the phenotype “{label}”? (c) What fraction of the offspring is expected to show the "
            "same phenotype as the tested parent?"
        )
        het_loci = [L for L, hh in zip(letters, het) if hh]
        hom_loci = [L for L, hh in zip(letters, het) if not hh]
        steps.append(
            f"The tested parent is heterozygous at {h} {'locus' if h == 1 else 'loci'} ({', '.join(het_loci)})"
            + (f" and homozygous dominant at {', '.join(hom_loci)}" if hom_loci else "")
            + f". By independent assortment it makes $2^{{{h}}} = {2 ** h}$ kinds of gametes with equal frequency: "
            + ", ".join(f"${g}$" for g in gametes) + ".")
        steps.append(
            f"So the offspring fall into {2 ** h} phenotypic classes in a "
            + ":".join(["1"] * (2 ** h)) + " ratio (each $\\frac{1}{" + str(2 ** h) + "}$)"
            + ("; every offspring shows the dominant phenotype at the homozygous locus" if len(hom_loci) == 1 else
               ("; every offspring shows the dominant phenotype at the homozygous loci" if hom_loci else "")) + ".")
        parts = []
        for (L, d, r), t, hh in zip(genes, target, het):
            pr = Fraction(1, 2) if hh else (Fraction(1) if t == "D" else Fraction(0))
            parts.append(f"P({d if t == 'D' else r}) $= {ftex(pr)}$")
        steps.append(
            "Product rule for the requested class: " + " × ".join(parts) + f", so $P = {ftex(p_t)}$ and the expected "
            f"number is ${N} \\times {ftex(p_t)} = {ex(expected)}$" + (" — this class cannot occur, because the tested "
                                                                        "parent carries no recessive allele at that "
                                                                        "locus." if p_t == 0 else "."))
        steps.append(
            "The tested parent shows every dominant phenotype. An offspring matches it only if it receives the "
            f"dominant allele at each heterozygous locus: $P = (\\frac{{1}}{{2}})^{{{h}}} = {ftex(p_same)}$.")
        answer = (f"(a) {2 ** h} classes in a " + ":".join(["1"] * (2 ** h)) + f" ratio; (b) ${ex(expected)}$ {noun}; "
                  f"(c) ${ftex(p_same)}$")
        values = {"mode": mode, "genotype": genotype, "het": het, "N": N, "target": "".join(target),
                  "p_target": float(p_t), "expected": float(expected), "n_classes": 2 ** h, "p_same": float(p_same)}
        return {"question": question, "steps": steps, "answer": answer, "values": values}

    # infer: deduce the genotype of a dominant-phenotype parent from the test-cross offspring
    N = rng.randint(120, 400)
    codes = [""]
    for hh in het:
        codes = [c + a for c in codes for a in (("D", "R") if hh else ("D",))]
    counts = _multinomial_equal(rng, N, len(codes))
    labels = [", ".join(d if c == "D" else r for (L, d, r), c in zip(genes, code)) for code in codes]
    data = "; ".join(f"{lab}: {cnt}" for lab, cnt in zip(labels, counts))
    dom_pheno = ", ".join(d for L, d, r in genes)
    question = (
        f"In {org}, {relations}; the three genes assort independently. An individual with the phenotype “{dom_pheno}” "
        f"is test-crossed to a ${tester}$ individual. The {N} offspring are: {data}. (a) What is the genotype of the "
        "tested individual? (b) In what ratio would you expect these phenotypic classes to occur?"
    )
    for (L, d, r), hh in zip(genes, het):
        i = letters.index(L)
        n_rec = sum(cnt for code, cnt in zip(codes, counts) if code[i] == "R")
        n_dom = N - n_rec
        if hh:
            steps.append(f"Gene {L}: {n_dom} offspring {d}, {n_rec} {r} — roughly 1:1, and recessive {r} offspring can only "
                         f"arise if the tested parent passed on ${L.lower()}$. So it is ${L}{L.lower()}$.")
        else:
            steps.append(f"Gene {L}: all {N} offspring are {d}; with this many offspring a hidden ${L.lower()}$ allele would "
                         f"have produced about half {r} offspring, so the tested parent is ${L}{L}$.")
    steps.append(
        f"Genotype ${genotype}$: heterozygous at {h} {'locus' if h == 1 else 'loci'}, so it makes $2^{{{h}}} = {2 ** h}$ "
        f"gamete types in equal proportions and the test cross should give {2 ** h} classes in a "
        + ":".join(["1"] * (2 ** h)) + " ratio, matching the data within sampling error.")
    answer = f"(a) ${genotype}$; (b) {2 ** h} classes in a " + ":".join(["1"] * (2 ** h)) + " ratio"
    values = {"mode": mode, "genotype": genotype, "letters": letters, "N": N, "classes": codes, "counts": counts,
              "n_classes": 2 ** h}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Molecular biology: replication time
# ---------------------------------------------------------------------------

REPLICONS = [
    # name, kind, genome size (bp), what is replicated, origins range, fork speed spec, S phase (lo, hi, step, unit)
    ("Escherichia coli", "bacterium", 4.64e6, "its single circular chromosome", None, ("bp/s", 600, 1000, 50), None),
    ("Bacillus subtilis", "bacterium", 4.22e6, "its single circular chromosome", None, ("bp/s", 500, 900, 50), None),
    ("the budding yeast Saccharomyces cerevisiae", "eukaryote", 1.21e7, "its haploid nuclear genome", (250, 400, 10),
     ("kb/min", 1.5, 3.0, 0.1), (20, 40, 5, "min")),
    ("a human diploid cell", "eukaryote", 6.2e9, "its diploid nuclear genome", (20000, 50000, 1000),
     ("kb/min", 1.0, 3.0, 0.1), (6, 10, 1, "h")),
    ("a mouse diploid cell", "eukaryote", 5.4e9, "its diploid nuclear genome", (20000, 50000, 1000),
     ("kb/min", 1.0, 3.0, 0.1), (6, 10, 1, "h")),
]


@template("genome_replication_time_origins", BIO, "Molecular Biology", "DNA replication: forks and origins", "medium")
def genome_replication_time_origins(rng):
    name, kind, G, what, orig_rng, (v_unit, v_lo, v_hi, v_step), s_spec = pick(rng, REPLICONS)
    v_in = nice(rng, v_lo, v_hi, v_step)
    v = v_in if v_unit == "bp/s" else v_in * 1000 / 60  # bp/s
    conv = "" if v_unit == "bp/s" else (f"Fork speed: ${ex(v_in)}$ kb/min $= \\frac{{{ex(v_in)} \\times 1000}}{{60}} = "
                                         f"{fmt(v, 4)}$ bp/s.")
    if kind == "bacterium":
        mode = pick(rng, ["time", "time", "speed"])
        if mode == "time":
            t = G / (2 * v)
            question = (
                f"The genome of {name} is {qx(G, 'bp')} long. Replication of {what} starts at a single origin (oriC) and "
                f"proceeds bidirectionally, with each replication fork moving at {qx(v_in, v_unit)}. Assuming constant "
                "fork speed, how long does it take to replicate the whole chromosome?"
            )
            steps = [
                "Two forks leave oriC in opposite directions and meet in the terminus region on the other side of the "
                "circle, so each fork copies half of the chromosome.",
                f"$t = \\frac{{G/2}}{{v}} = \\frac{{{ex(G)}/2}}{{{ex(v_in)}}} = {fmt(t, 4)}$ s $= {fmt(t / 60, 3)}$ min.",
                f"Check: in rich medium {name.split()[0]} cells can divide every 20–25 min, faster than one round of "
                "replication. This works because new rounds start at oriC before earlier rounds finish (multifork "
                "replication).",
            ]
            answer = f"$t = {fmt(t, 4)}$ s $\\approx {fmt(t / 60, 3)}$ min"
            values = {"mode": mode, "G": G, "n_origins": 1, "v_bp_s": v, "t_s": t, "t_min": t / 60}
        else:
            C = nice(rng, 35, 70, 1)
            v_need = G / (2 * C * 60)
            question = (
                f"The genome of {name} ({qx(G, 'bp')}) is replicated bidirectionally from a single origin. In a slowly "
                f"growing culture the replication period (C period) is measured as {qx(C, 'min')}. What average speed "
                "must each replication fork have, in nucleotides per second?"
            )
            steps = [
                "With one origin and two forks moving in opposite directions, each fork copies $G/2$ base pairs during "
                "the C period.",
                f"$v = \\frac{{G/2}}{{C}} = \\frac{{{ex(G)}/2}}{{{C} \\times 60\\ \\text{{s}}}} = {fmt(v_need, 3)}$ bp/s "
                "(nucleotides per second on each strand).",
                "Check: this is the right order of magnitude for bacterial DNA polymerase III holoenzyme (several hundred "
                "to about 1000 nucleotides per second).",
            ]
            answer = f"$v \\approx {fmt(v_need, 3)}$ nucleotides/s"
            values = {"mode": mode, "G": G, "C_min": C, "v_bp_s": v_need}
        return {"question": question, "steps": steps, "answer": answer, "values": values}

    mode = pick(rng, ["time", "origins"])
    if mode == "time":
        n_or = nice(rng, *orig_rng)
        t = G / (2 * n_or * v)
        question = (
            f"In {name}, {what} contains {qx(G, 'bp')}. Suppose {n_or} replication origins are evenly spaced and all fire "
            f"at the start of S phase, each giving two forks that move apart at {qx(v_in, v_unit)}. How long would "
            "replication take? Compare with the observed length of S phase."
        )
        S_lo, S_hi, _, S_unit = s_spec
        steps = [
            conv,
            f"With evenly spaced origins each replicon is $G/n = {ex(G)}/{n_or} = {fmt(G / n_or, 4)}$ bp long and is "
            "copied by two forks moving in opposite directions.",
            f"$t = \\frac{{G}}{{2nv}} = \\frac{{{ex(G)}}}{{2 \\times {n_or} \\times {fmt(v, 4)}}} = {fmt(t, 4)}$ s "
            f"$= {fmt(t / 60, 3)}$ min.",
            f"The observed S phase lasts about {S_lo}–{S_hi} {S_unit}, longer than this estimate, because origins fire "
            "at different times during S phase (early- and late-replicating regions), are unevenly spaced, and forks "
            "sometimes stall.",
        ]
        answer = f"$t \\approx {fmt(t / 60, 3)}$ min"
        values = {"mode": mode, "G": G, "n_origins": n_or, "v_kb_min": v_in, "v_bp_s": v, "t_s": t, "t_min": t / 60}
    else:
        S_lo, S_hi, S_step, S_unit = s_spec
        T = nice(rng, S_lo, S_hi, S_step)
        T_s = T * (60 if S_unit == "min" else 3600)
        n_exact = G / (2 * v * T_s)
        n_min = math.ceil(n_exact - 1e-9)
        spacing_kb = 2 * v * T_s / 1000
        question = (
            f"In {name}, {what} contains {qx(G, 'bp')} and S phase lasts {T} {S_unit}. Replication forks move at "
            f"{qx(v_in, v_unit)}. If all origins fire at the start of S phase, are evenly spaced and replicate "
            "bidirectionally, what is the minimum number of origins needed, and what is the maximum spacing between "
            "neighboring origins?"
        )
        steps = [
            conv,
            f"S phase: ${T}$ {S_unit} $= {ex(T_s)}$ s.",
            "Two forks leave each origin, so one origin can replicate at most $2vT$ base pairs during S phase: "
            f"$2vT = 2 \\times {fmt(v, 4)} \\times {ex(T_s)} = {fmt(2 * v * T_s, 4)}$ bp, i.e. a maximum origin "
            f"spacing of ${fmt(spacing_kb, 4)}$ kb.",
            f"$n_{{min}} = \\frac{{G}}{{2vT}} = \\frac{{{ex(G)}}}{{{fmt(2 * v * T_s, 4)}}} = {fmt(n_exact, 4)}$, "
            f"so at least {n_min} origins are needed.",
            "Real genomes use considerably more origins than this minimum, because origins fire throughout S phase "
            "rather than all at once and are not evenly spaced.",
        ]
        answer = f"at least {n_min} origins, spaced at most ${fmt(spacing_kb, 4)}$ kb apart"
        values = {"mode": mode, "G": G, "v_kb_min": v_in, "v_bp_s": v, "T_s": T_s, "n_exact": n_exact,
                  "n_min": n_min, "spacing_kb": spacing_kb}
    steps = [s for s in steps if s]
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Cell biology / microbiology: hemocytometer and optical density
# ---------------------------------------------------------------------------

HEMO_CELLS = [
    ("HeLa cells", "trypan blue"), ("CHO cells", "trypan blue"), ("HEK293 cells", "trypan blue"),
    ("Jurkat T cells", "trypan blue"), ("baker's yeast (Saccharomyces cerevisiae) cells", "methylene blue"),
]
HEMO_MIX = [  # sample µL, stain µL, prior dilution in buffer
    (10, 10, 1), (20, 20, 1), (50, 50, 1), (25, 75, 1), (20, 80, 1), (50, 50, 5), (10, 10, 10),
]


@template("hemocytometer_viable_count", BIO, "Cell Biology", "Cell counting with a hemocytometer", "easy")
def hemocytometer_viable_count(rng):
    cells, stain = pick(rng, HEMO_CELLS)
    s_ul, d_ul, pre = pick(rng, HEMO_MIX)
    DF = pre * (s_ul + d_ul) // s_ul
    n_sq = pick(rng, [4, 4, 5])
    mean_t = rng.randint(25, 110)
    via_t = rng.uniform(0.70, 0.98)
    live = [max(8, mean_t + rng.randint(-12, 12)) for _ in range(n_sq)]
    dead = [max(0, round(x * (1 - via_t) / via_t) + rng.randint(-2, 2)) for x in live]
    L, D = sum(live), sum(dead)
    mean_live = L / n_sq
    conc = mean_live * DF * 1e4
    viab = L / (L + D)
    V = nice(rng, 5, 50, 1)
    total = conc * V
    mode = pick(rng, ["seed", "prepare"])
    where = "the four large corner squares" if n_sq == 4 else "the four large corner squares and the central large square"
    if pre == 1:
        mix = f"{s_ul} µL of the suspension was mixed with {d_ul} µL of {stain} solution"
    else:
        mix = (f"the suspension was first diluted 1:{pre} in buffer, and {s_ul} µL of the diluted suspension was mixed "
               f"with {d_ul} µL of {stain} solution")
    if mode == "seed":
        target = pick(rng, [5e4, 1e5, 2e5, 2.5e5, 5e5])
        while target / conc * 1000 > 1000:
            target /= 2
        vol_ul = target / conc * 1000
        ask = (f"(d) What volume of the suspension contains {qx(target)} viable cells for seeding one culture well?")
        last_step = (f"Volume for {qx(target)} viable cells: $\\frac{{{ex(target)}}}{{{fmt(conc, 4)}\\ "
                     f"\\text{{mL}}^{{-1}}}} = {fmt(vol_ul / 1000, 3)}$ mL $= {fmt(vol_ul, 3)}$ µL.")
        ans_d = f"(d) ${fmt(vol_ul, 3)}$ µL"
        extra = {"target_cells": target, "vol_uL": vol_ul}
    else:
        Vp = pick(rng, [10, 20, 25, 50])
        Cp = pick(rng, [x for x in (1e4, 2e4, 5e4, 1e5, 2e5, 5e5) if x * Vp < 0.5 * total and x < conc / 2] or [1e4])
        vol_ml = Cp * Vp / conc
        ask = (f"(d) How would you prepare {Vp} mL of suspension containing {qx(Cp)} viable cells/mL?")
        last_step = (f"Dilution ($C_1V_1 = C_2V_2$): $V_1 = \\frac{{{ex(Cp)} \\times {Vp}}}{{{fmt(conc, 4)}}} = "
                     f"{fmt(vol_ml, 3)}$ mL of suspension, made up to {Vp} mL with ${fmt(Vp - vol_ml, 3)}$ mL of medium.")
        ans_d = f"(d) ${fmt(vol_ml, 3)}$ mL of suspension + ${fmt(Vp - vol_ml, 3)}$ mL of medium"
        extra = {"Vp_mL": Vp, "Cp": Cp, "vol_mL": vol_ml}
    question = (
        f"A {ex(V)} mL suspension of {cells} is counted with an improved Neubauer hemocytometer (each large square is "
        f"1 mm × 1 mm and the chamber is 0.1 mm deep). For the count, {mix}. In {where}, the numbers of unstained "
        f"(live) cells were {', '.join(map(str, live))} and the numbers of blue-stained (dead) cells were "
        f"{', '.join(map(str, dead))}. (a) What is the concentration of viable cells in the original suspension? "
        f"(b) What is the percentage viability? (c) How many viable cells are in the whole suspension? {ask}"
    )
    steps = [
        f"Volume over one large square: $1 \\times 1 \\times 0.1 = 0.1$ mm³ $= 1 \\times 10^{{-4}}$ mL, so cells/mL "
        "$=$ (mean count per square) × dilution factor × $10^4$.",
        f"Dilution factor: " + (f"$\\frac{{{s_ul} + {d_ul}}}{{{s_ul}}} = {DF}$" if pre == 1 else
                                f"${pre} \\times \\frac{{{s_ul} + {d_ul}}}{{{s_ul}}} = {DF}$") + ".",
        f"Live cells: total ${L}$ in {n_sq} squares, mean ${ex(mean_live)}$ per square. Concentration: "
        f"${ex(mean_live)} \\times {DF} \\times 10^4 = {fmt(conc, 4)}$ viable cells/mL.",
        f"Viability: dead cells take up {stain} because their membranes are damaged; live cells exclude it. "
        f"$\\frac{{{L}}}{{{L} + {D}}} = {pc(viab)}$.",
        f"Total viable cells: ${fmt(conc, 4)} \\times {ex(V)} = {fmt(total, 3)}$.",
        last_step,
        f"Precision: about {L} cells were counted, so the Poisson counting error is roughly $1/\\sqrt{{{L}}} \\approx "
        f"{pc(1 / math.sqrt(L), 2)}$. (Cells touching the top and left boundary lines are counted; those touching the "
        "bottom and right lines are not.)",
    ]
    answer = (f"(a) ${fmt(conc, 4)}$ viable cells/mL; (b) {fmt(100 * viab, 3)}% viable; (c) ${fmt(total, 3)}$ viable "
              f"cells; {ans_d}")
    values = {"live": live, "dead": dead, "n_squares": n_sq, "DF": DF, "conc": conc, "viability": viab, "V_mL": V,
              "total_viable": total, "mode": mode, **extra}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


OD_ORGS = [  # organism, calibration mantissa range (lo, hi, step), exponent, medium, doubling-time range (min)
    ("Escherichia coli", (6.0, 10.0, 0.5), 8, "LB medium at 37 °C", (20, 35, 1)),
    ("Saccharomyces cerevisiae", (1.0, 3.0, 0.1), 7, "YPD medium at 30 °C", (85, 120, 5)),
    ("Bacillus subtilis", (2.0, 5.0, 0.5), 8, "LB medium at 37 °C", (25, 40, 1)),
]


@template("od600_cell_density_inoculum", BIO, "Microbiology", "Optical density and culture growth", "easy")
def od600_cell_density_inoculum(rng):
    org, (c_lo, c_hi, c_st), c_exp, medium, (td_lo, td_hi) = pick(rng, OD_ORGS)
    cal = clean(nice(rng, c_lo, c_hi, c_st) * 10 ** c_exp)
    k = pick(rng, [2, 5, 10, 20])
    od_m = nice(rng, 0.100, 0.450, 0.001)
    od = clean(od_m * k)
    density = od * cal
    V_new = pick(rng, [25, 50, 100, 200, 250, 500])
    od0 = pick(rng, [x for x in (0.02, 0.05, 0.1) if x < od / 4] or [0.02])
    V_in = od0 * V_new / od
    td = rng.randint(td_lo, td_hi)
    od_t = pick(rng, [0.4, 0.5, 0.6, 0.8])
    t = td * math.log2(od_t / od0)
    question = (
        f"An overnight culture of {org} in {medium} is diluted 1:{k} in fresh medium, and the OD₆₀₀ of the dilution, "
        f"measured in a 1 cm cuvette against a medium blank, is {qx(od_m, min_sig=3)}. For this spectrophotometer, "
        f"OD₆₀₀ = 1.0 corresponds to {qx(cal)} cells/mL in the linear range. (a) What are the OD₆₀₀ and the cell "
        f"density of the undiluted culture? (b) What volume of the overnight culture is needed to start {V_new} mL "
        f"(final volume) of a new culture at OD₆₀₀ = {ex(od0)}? (c) If the cells grow exponentially without a lag "
        f"with a doubling time of {td} min, how long will the new culture take to reach OD₆₀₀ = {ex(od_t)}?"
    )
    steps = [
        "OD₆₀₀ of a cell suspension is mostly light scattering; it is proportional to cell density only at low values "
        "(below roughly 0.4–0.5), which is why dense cultures are diluted before reading.",
        f"Undiluted culture: $\\text{{OD}} = {ex(od_m, 3)} \\times {k} = {ex(od)}$.",
        f"Cell density: ${ex(od)} \\times {ex(cal)} = {fmt(density, 3)}$ cells/mL.",
        f"Inoculum ($C_1V_1 = C_2V_2$ in OD units): $V_1 = \\frac{{{ex(od0)} \\times {V_new}}}{{{ex(od)}}} = "
        f"{fmt(V_in, 3)}$ mL of culture, plus ${fmt(V_new - V_in, 4)}$ mL of fresh medium.",
        f"Exponential growth: $\\text{{OD}}(t) = \\text{{OD}}_0 \\, 2^{{t/t_d}}$, so $t = t_d \\log_2\\frac{{{ex(od_t)}}}"
        f"{{{ex(od0)}}} = {td} \\times {fmt(math.log2(od_t / od0), 4)} = {fmt(t, 3)}$ min "
        f"(${fmt(t / 60, 3)}$ h).",
    ]
    answer = (f"(a) OD₆₀₀ $= {ex(od)}$, ${fmt(density, 3)}$ cells/mL; (b) ${fmt(V_in, 3)}$ mL; "
              f"(c) ${fmt(t, 3)}$ min")
    values = {"k": k, "od_measured": od_m, "od_culture": od, "cal": cal, "density": density, "V_new": V_new,
              "od0": od0, "V_inoculum": V_in, "td": td, "od_target": od_t, "t_min": t}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Physiology: osmolarity and tonicity
# ---------------------------------------------------------------------------

SOLUTES = {  # key: (display name, particles per formula unit, crosses the membrane?)
    "NaCl": ("NaCl", 2, False),
    "KCl": ("KCl", 2, False),
    "CaCl2": ("CaCl₂", 3, False),
    "sucrose": ("sucrose", 1, False),
    "mannitol": ("mannitol", 1, False),
    "urea": ("urea", 1, True),
    "glycerol": ("glycerol", 1, True),
}


@template("osmolarity_tonicity_cell_volume", BIO, "Physiology", "Osmolarity, tonicity and cell volume", "medium")
def osmolarity_tonicity_cell_volume(rng):
    C_in = pick(rng, [280, 290, 300])
    cell = pick(rng, ["rbc", "cultured"])
    design = pick(rng, ["iso", "hypo", "hyper", "hypo", "hyper"])
    sol = []
    if design == "iso":
        choice = pick(rng, ["NaCl", "mix", "sucrose", "KClmix"])
        if choice == "NaCl":
            sol = [("NaCl", C_in / 2)]
        elif choice == "sucrose":
            sol = [(pick(rng, ["sucrose", "mannitol"]), C_in)]
        else:
            salt = "NaCl" if choice == "mix" else "KCl"
            c1 = nice(rng, 50, C_in // 2 - 25, 5)
            sol = [(salt, c1), (pick(rng, ["sucrose", "mannitol"]), C_in - 2 * c1)]
    else:
        for _ in range(1000):
            names = pick(rng, [["NaCl"], ["NaCl", "sucrose"], ["NaCl", "mannitol"], ["KCl", "sucrose"], ["CaCl2"],
                               ["NaCl", "CaCl2"], ["mannitol"], ["sucrose"]])
            sol = []
            for nm in names:
                i = SOLUTES[nm][1]
                hi = 400 if i == 1 else (250 if i == 2 else 150)
                sol.append((nm, nice(rng, 10, hi, 5)))
            E = sum(SOLUTES[nm][1] * c for nm, c in sol)
            if design == "hypo" and 0.35 * C_in <= E <= 0.9 * C_in:
                break
            if design == "hyper" and 1.1 * C_in <= E <= 2.2 * C_in:
                break
    if rng.random() < 0.55:
        sol.append((pick(rng, ["urea", "glycerol"]), nice(rng, 50, 400, 10)))
    osm_total = sum(SOLUTES[nm][1] * c for nm, c in sol)
    osm_eff = sum(SOLUTES[nm][1] * c for nm, c in sol if not SOLUTES[nm][2])
    b = pick(rng, [0.0, 0.0, 0.3, 0.4])
    if cell == "rbc":
        V0 = pick(rng, [85, 88, 90, 92, 95])
        vunit = "fL"
        cell_txt = "A human red blood cell"
    else:
        V0 = nice(rng, 1.5, 3.0, 0.1)
        vunit = "pL"
        cell_txt = "A cultured mammalian cell"
    V_eq = V0 * (b + (1 - b) * C_in / osm_eff)

    def cls(x, a, b_, c):
        return a if x > C_in else (b_ if x < C_in else c)

    osmotic = cls(osm_total, "hyperosmotic", "hypo-osmotic", "isosmotic")
    tonicity = cls(osm_eff, "hypertonic", "hypotonic", "isotonic")
    sol_txt = " and ".join(f"{qx(c, 'mM')} {SOLUTES[nm][0]}" for nm, c in sol)
    b_txt = ("Treat the cell as an ideal osmometer whose whole volume is osmotically active" if b == 0 else
             f"Assume {round(100 * b)}% of the initial cell volume is osmotically inactive (proteins and other solids)")
    pen = [SOLUTES[nm][0] for nm, c in sol if SOLUTES[nm][2]]
    question = (
        f"{cell_txt} with a volume of {qx(V0, vunit)} contains nonpenetrating solutes at a total osmolarity of "
        f"{C_in} mOsm/L. It is placed in a large volume of a solution containing {sol_txt}. Assume salts dissociate "
        "completely, the solutions behave ideally, the membrane is impermeable to ions, sucrose and mannitol but freely "
        f"permeable to urea and glycerol. {b_txt}. (a) What is the osmolarity of the solution, and is it hyperosmotic, "
        "hypo-osmotic or isosmotic to the cell? (b) Is the solution hypertonic, hypotonic or isotonic? (c) What is the "
        "cell volume once it reaches its new equilibrium?"
    )
    terms = " + ".join(f"{SOLUTES[nm][1]}({ex(c)})" for nm, c in sol)
    steps = [
        "Osmolarity $= \\sum i c$, where $i$ is the number of particles per formula unit (NaCl and KCl give 2, CaCl₂ "
        "gives 3, molecules such as sucrose, mannitol, urea and glycerol give 1).",
        f"Solution: ${terms} = {ex(osm_total)}$ mOsm/L, compared with {C_in} mOsm/L inside the cell, so the solution "
        f"is {osmotic}.",
        ("Tonicity is set only by the nonpenetrating solutes: "
         + (f"{' and '.join(pen)} cross{'es' if len(pen) == 1 else ''} the membrane and equilibrate"
            ", so in the end"
            if pen else "here all solutes are nonpenetrating, so")
         + f" the effective osmolarity is ${ex(osm_eff)}$ mOsm/L."),
        f"${ex(osm_eff)}$ mOsm/L " + {"hypertonic": f"> {C_in}$: the solution is hypertonic and water leaves the cell, "
                                                    "which shrinks (crenation, for a red blood cell).",
                                      "hypotonic": f"< {C_in}$: the solution is hypotonic and water enters the cell, "
                                                   "which swells (and may lyse if the swelling is large).",
                                      "isotonic": f"= {C_in}$: the solution is isotonic and the cell keeps its volume "
                                                  "at equilibrium."}[tonicity].replace("$", "", 0),
    ]
    # fix the math delimiters of the comparison step
    steps[-1] = f"${ex(osm_eff)}" + steps[-1][len(ex(osm_eff)) + 1:].replace(" mOsm/L ", "", 1)
    steps[-1] = steps[-1].replace("$", " $", 0)
    steps.append(
        "The amount of nonpenetrating solute inside is fixed, so at equilibrium "
        "$(V - V_b)\\,C_{out} = (V_0 - V_b)\\,C_{in}$ (Boyle–van 't Hoff), where $V_b$ is the osmotically inactive "
        "volume: $V = V_0\\left[b + (1 - b)\\frac{C_{in}}{C_{out}}\\right]$.")
    steps.append(
        f"$V = {ex(V0)}\\left[{ex(b)} + {ex(1 - b)} \\times \\frac{{{C_in}}}{{{ex(osm_eff)}}}\\right] = {fmt(V_eq, 3)}$ "
        f"{vunit} (${fmt(V_eq / V0, 3)}$ times the initial volume).")
    if pen and osmotic != tonicity.replace("tonic", "osmotic").replace("hypo-osmotic", "hypo-osmotic"):
        steps.append(f"Note that osmolarity and tonicity differ here: the penetrating {' and '.join(pen)} raise the "
                     "osmolarity but cannot hold water out of the cell, because they enter it until their "
                     "concentrations are equal on both sides.")
    answer = (f"(a) ${ex(osm_total)}$ mOsm/L, {osmotic}; (b) {tonicity}; (c) $V = {fmt(V_eq, 3)}$ {vunit}")
    values = {"solutes": [nm for nm, c in sol], "conc": [c for nm, c in sol], "C_in": C_in, "osm_total": osm_total,
              "osm_eff": osm_eff, "b": b, "V0": V0, "V_eq": V_eq, "osmotic": osmotic, "tonicity": tonicity}
    return {"question": question, "steps": steps, "answer": answer, "values": values}
