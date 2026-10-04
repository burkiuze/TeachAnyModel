"""Biology problem templates (genetics, molecular biology, physiology, ecology)."""

import itertools
import math
from fractions import Fraction

from .common import FARADAY, R_GAS, fmt, nice, pick, q, sig, template

BIO = "Biology"

# ---------------------------------------------------------------------------
# Population genetics
# ---------------------------------------------------------------------------

RECESSIVE_TRAITS = [
    ("cystic fibrosis", "an autosomal recessive disorder"),
    ("albinism (oculocutaneous type 1)", "an autosomal recessive trait"),
    ("phenylketonuria (PKU)", "an autosomal recessive disorder"),
    ("sickle-cell disease", "an autosomal recessive disorder"),
    ("Tay–Sachs disease", "an autosomal recessive disorder"),
    ("a recessive coat-color phenotype in a population of mice", "a recessive trait"),
    ("white flowers in a population of wild plants", "a recessive trait"),
]


@template("hardy_weinberg", BIO, "Population Genetics", "Hardy–Weinberg equilibrium", "medium")
def hardy_weinberg(rng):
    trait, kind = pick(rng, RECESSIVE_TRAITS)
    denom = pick(rng, [25, 100, 400, 1000, 2500, 3600, 10000])
    q2 = 1 / denom
    qa = math.sqrt(q2)
    p = 1 - qa
    het = 2 * p * qa
    N = pick(rng, [10000, 50000, 100000, 1000000])
    question = (
        f"{trait[0].upper() + trait[1:]} is {kind}. In a randomly mating population, 1 in {denom:,} individuals shows the "
        "recessive phenotype. Assuming Hardy–Weinberg equilibrium, find the frequencies of both alleles, the fraction "
        f"of heterozygous carriers, and the expected number of carriers in a population of {N:,}."
    )
    steps = [
        f"Affected individuals are homozygous recessive: $q^2 = 1/{denom} = {fmt(q2)}$.",
        f"Recessive allele frequency: $q = \\sqrt{{{fmt(q2)}}} = {fmt(qa)}$; dominant allele: $p = 1 - q = {fmt(p)}$.",
        f"Carriers (heterozygotes): $2pq = 2({fmt(p)})({fmt(qa)}) = {fmt(het)}$, i.e. about 1 in {round(1 / het)}.",
        f"Expected carriers among {N:,}: ${fmt(het)} \\times {N} \\approx {round(het * N)}$.",
        f"Note that carriers outnumber affected individuals by a factor of ${fmt(het / q2)}$ — most copies of a rare "
        "recessive allele are hidden in heterozygotes.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$q = {fmt(qa)}$, $p = {fmt(p)}$; carriers $2pq = {fmt(het)}$ (≈{round(het * N):,} of {N:,})",
            "values": {"q2": q2, "q": qa, "p": p, "carrier_freq": het, "N": N, "carriers": het * N}}


def _multinomial(rng, n, probs):
    counts = [0] * len(probs)
    cum = list(itertools.accumulate(probs))
    for _ in range(n):
        u = rng.random()
        for i, c in enumerate(cum):
            if u < c:
                counts[i] += 1
                break
        else:
            counts[-1] += 1
    return counts


@template("hardy_weinberg_chi_square", BIO, "Population Genetics", "Testing Hardy–Weinberg equilibrium", "hard")
def hardy_weinberg_chi_square(rng):
    N = nice(rng, 100, 1000, 10)
    p_true = nice(rng, 0.20, 0.80, 0.01)
    # optionally simulate a heterozygote deficit (e.g. inbreeding or population structure)
    F = pick(rng, [0.0, 0.0, 0.0, 0.15, 0.3])
    q_true = 1 - p_true
    probs = [p_true ** 2 + F * p_true * q_true, 2 * p_true * q_true * (1 - F), q_true ** 2 + F * p_true * q_true]
    AA, Aa, aa = _multinomial(rng, N, probs)
    p_hat = (2 * AA + Aa) / (2 * N)
    q_hat = 1 - p_hat
    exp = [p_hat ** 2 * N, 2 * p_hat * q_hat * N, q_hat ** 2 * N]
    obs = [AA, Aa, aa]
    chi = sum((o - e) ** 2 / e for o, e in zip(obs, exp))
    reject = chi > 3.841
    question = (
        f"A sample of {N} individuals is genotyped at a locus with two alleles: AA = {AA}, Aa = {Aa}, aa = {aa}. "
        "Use a chi-square test (α = 0.05) to decide whether the population is in Hardy–Weinberg equilibrium."
    )
    steps = [
        f"Allele frequencies from the data: $p = \\frac{{2({AA}) + {Aa}}}{{2({N})}} = {fmt(p_hat, 4)}$, $q = {fmt(q_hat, 4)}$.",
        f"Expected counts: AA $= p^2N = {exp[0]:.1f}$, Aa $= 2pqN = {exp[1]:.1f}$, aa $= q^2N = {exp[2]:.1f}$.",
        "$\\chi^2 = \\sum\\frac{(O - E)^2}{E} = " + " + ".join(
            f"\\frac{{({o} - {e:.1f})^2}}{{{e:.1f}}}" for o, e in zip(obs, exp)) + f" = {chi:.2f}$.",
        "Degrees of freedom: 3 genotype classes − 1 − 1 estimated allele frequency = 1; critical value 3.841.",
        (f"Since ${chi:.2f} > 3.841$, reject the null hypothesis: the genotype frequencies deviate significantly from "
         "Hardy–Weinberg expectations" + (" (here, a deficit of heterozygotes, as caused by inbreeding or population "
                                         "subdivision)." if Aa < exp[1] else ".")) if reject else
        (f"Since ${chi:.2f} < 3.841$, we fail to reject the null hypothesis: the data are consistent with "
         "Hardy–Weinberg equilibrium."),
    ]
    return {"question": question, "steps": steps,
            "answer": f"$\\chi^2 = {chi:.2f}$ (df = 1); " + ("not in HWE (p < 0.05)" if reject else "consistent with HWE"),
            "values": {"AA": AA, "Aa": Aa, "aa": aa, "p": p_hat, "chi2": chi, "reject": reject}}


@template("selection_against_recessive", BIO, "Evolution", "Natural selection", "hard")
def selection_against_recessive(rng):
    q0 = nice(rng, 0.05, 0.90, 0.01)
    s = nice(rng, 0.05, 1.00, 0.05)
    p0 = 1 - q0
    wbar = 1 - s * q0 ** 2
    q1 = q0 * (1 - s * q0) / wbar
    question = (
        f"In a large randomly mating population the frequency of a recessive allele $a$ is {fmt(q0, 2)}. Homozygous "
        f"$aa$ individuals have relative fitness $1 - s$ with $s = {fmt(s, 2)}$, while AA and Aa have fitness 1. What is "
        "the allele frequency after one generation of selection?"
    )
    steps = [
        f"Genotype frequencies before selection: AA $p^2 = {fmt(p0 ** 2)}$, Aa $2pq = {fmt(2 * p0 * q0)}$, aa $q^2 = {fmt(q0 ** 2)}$.",
        f"Mean fitness: $\\bar w = 1 - sq^2 = 1 - ({fmt(s, 2)})({fmt(q0 ** 2)}) = {fmt(wbar, 4)}$.",
        "After selection, $q' = \\frac{pq + q^2(1 - s)}{\\bar w} = \\frac{q(1 - sq)}{1 - sq^2}$.",
        f"$q' = \\frac{{{fmt(q0, 2)}(1 - {fmt(s, 2)} \\times {fmt(q0, 2)})}}{{{fmt(wbar, 4)}}} = {fmt(q1, 4)}$ "
        f"($\\Delta q = {fmt(q1 - q0, 3)}$).",
        "Selection against a recessive allele slows dramatically as $q$ becomes small, because most copies then sit in "
        "heterozygotes where they are invisible to selection.",
    ]
    return {"question": question, "steps": steps, "answer": f"$q' = {fmt(q1, 4)}$",
            "values": {"q0": q0, "s": s, "q1": q1, "w_bar": wbar}}


# ---------------------------------------------------------------------------
# Mendelian genetics
# ---------------------------------------------------------------------------

MONO_TRAITS = [  # letter, dominant phenotype, recessive phenotype, organism
    ("P", "purple flowers", "white flowers", "pea plants"),
    ("T", "tall stems", "dwarf stems", "pea plants"),
    ("R", "round seeds", "wrinkled seeds", "pea plants"),
    ("Y", "yellow seeds", "green seeds", "pea plants"),
    ("B", "black fur", "brown fur", "guinea pigs"),
    ("F", "unaffected", "cystic fibrosis", "humans"),
    ("A", "normal pigmentation", "albinism", "humans"),
]


def _offspring(g1, g2):
    """Genotype probabilities for a single-gene cross, e.g. 'Aa' x 'aa'."""
    out = {}
    for a in g1:
        for b in g2:
            geno = "".join(sorted(a + b, key=lambda ch: (ch.islower(), ch)))
            out[geno] = out.get(geno, Fraction(0)) + Fraction(1, 4)
    return out


def _frac(fr):
    return f"{fr.numerator}/{fr.denominator}" if fr.denominator != 1 else str(fr.numerator)


def _ratio_text(dist):
    """'all Aa' for a single outcome, otherwise 'AA 1/4, Aa 1/2, aa 1/4'."""
    items = sorted((k, v) for k, v in dist.items() if v > 0)
    if len(items) == 1:
        return f"all {items[0][0]}"
    return ", ".join(f"{k} {_frac(v)}" for k, v in items)


@template("monohybrid_cross", BIO, "Genetics", "Mendelian inheritance", "easy")
def monohybrid_cross(rng):
    L, dom, rec, org = pick(rng, MONO_TRAITS)
    l = L.lower()
    genos = [L + L, L + l, l + l]
    g1, g2 = pick(rng, [(genos[1], genos[1]), (genos[1], genos[2]), (genos[0], genos[2]), (genos[1], genos[0]),
                        (genos[1], genos[1])])
    off = _offspring(g1, g2)
    p_rec = off.get(l + l, Fraction(0))
    p_dom = 1 - p_rec
    n = rng.randint(3, 6)
    uniform = p_rec == 0
    k = n if uniform else rng.randint(1, n)
    target_rec = rng.random() < 0.5 and not uniform
    p_t = float(p_rec if target_rec else p_dom)
    prob = math.comb(n, k) * p_t ** k * (1 - p_t) ** (n - k)
    target = rec if target_rec else dom
    geno_txt = _ratio_text(off)
    phen_txt = f"all {dom}" if uniform else f"{dom} {_frac(p_dom)}, {rec} {_frac(p_rec)}"
    exactly = f"all {n}" if uniform else f"exactly {k}"
    question = (
        f"In {org}, the allele for {dom} ({L}) is completely dominant over the allele for {rec} ({l}). An individual "
        f"with genotype {g1} is crossed with one with genotype {g2}. (a) What are the expected genotype and phenotype "
        f"ratios among the offspring? (b) If the cross produces {n} offspring, what is the probability that {exactly} "
        f"of them have {target}?"
    )
    steps = [
        f"Gametes: {g1} produces {' and '.join(sorted(set(g1)))}; {g2} produces {' and '.join(sorted(set(g2)))} "
        "(each allele with equal probability, by Mendel's law of segregation).",
        f"Punnett square genotypes: {geno_txt}.",
        f"Phenotypes: {phen_txt}.",
    ]
    if uniform:
        steps.append(f"Every offspring carries at least one {L} allele, so each shows {dom} with certainty: $P = 1$.")
    else:
        steps += [
            f"Each offspring independently has probability $p = {_frac(p_rec if target_rec else p_dom)}$ of showing {target}.",
            f"Binomial probability: $P = \\binom{{{n}}}{{{k}}}p^{{{k}}}(1-p)^{{{n - k}}} = {math.comb(n, k)} \\times "
            f"({fmt(p_t, 3)})^{{{k}}}({fmt(1 - p_t, 3)})^{{{n - k}}} = {fmt(prob)}$.",
        ]
    return {"question": question, "steps": steps,
            "answer": f"(a) {geno_txt}; phenotypes {phen_txt}; (b) $P = {fmt(prob)}$",
            "values": {"parent1": g1, "parent2": g2, "p_recessive": float(p_rec), "n": n, "k": k,
                       "target_recessive": target_rec, "probability": prob}}


DI_GENES = [("Y", "yellow", "green", "seed color"), ("R", "round", "wrinkled", "seed shape")]


@template("dihybrid_cross", BIO, "Genetics", "Independent assortment", "medium")
def dihybrid_cross(rng):
    (A, a_dom, a_rec, _), (B, b_dom, b_rec, _) = DI_GENES
    a, b = A.lower(), B.lower()
    options = [A + A, A + a, a + a]
    options_b = [B + B, B + b, b + b]
    p1 = (pick(rng, options[:2]), pick(rng, options_b[:2]))
    p2 = (pick(rng, options), pick(rng, options_b))
    if rng.random() < 0.4:
        p1, p2 = (A + a, B + b), (A + a, B + b)
    off_a = _offspring(p1[0], p2[0])
    off_b = _offspring(p1[1], p2[1])
    pa_rec = off_a.get(a + a, Fraction(0))
    pb_rec = off_b.get(b + b, Fraction(0))
    phen = {
        f"{a_dom} and {b_dom}": (1 - pa_rec) * (1 - pb_rec),
        f"{a_dom} and {b_rec}": (1 - pa_rec) * pb_rec,
        f"{a_rec} and {b_dom}": pa_rec * (1 - pb_rec),
        f"{a_rec} and {b_rec}": pa_rec * pb_rec,
    }
    nonzero = [k for k, v in phen.items() if v > 0]
    target = pick(rng, nonzero)
    g_target = (pick(rng, sorted(off_a)), pick(rng, sorted(off_b)))
    pg = off_a[g_target[0]] * off_b[g_target[1]]
    s1, s2 = p1[0] + p1[1], p2[0] + p2[1]
    question = (
        f"In pea plants, yellow seeds ({A}) are dominant to green ({a}) and round seeds ({B}) are dominant to wrinkled "
        f"({b}); the two genes assort independently. For the cross {s1} × {s2}, find (a) the expected phenotype "
        f"ratio, (b) the probability that an offspring has {target} seeds, and (c) the probability that an offspring "
        f"has genotype {g_target[0] + g_target[1]}."
    )
    steps = [
        "Independent assortment lets us treat each gene separately and multiply probabilities (product rule).",
        f"Seed color, {p1[0]} × {p2[0]}: {_ratio_text(off_a)} → "
        + _ratio_text({a_dom: 1 - pa_rec, a_rec: pa_rec}) + ".",
        f"Seed shape, {p1[1]} × {p2[1]}: {_ratio_text(off_b)} → "
        + _ratio_text({b_dom: 1 - pb_rec, b_rec: pb_rec}) + ".",
        "(a) Phenotypes: " + "; ".join(f"{k} {_frac(v)}" for k, v in phen.items() if v > 0) + ".",
        f"(b) $P$({target}) $= {_frac(phen[target])}$ $= {fmt(float(phen[target]))}$.",
        f"(c) $P$({g_target[0] + g_target[1]}) $= P({g_target[0]}) \\times P({g_target[1]}) = "
        f"{_frac(off_a[g_target[0]])} \\times {_frac(off_b[g_target[1]])} = {_frac(pg)}$.",
    ]
    return {"question": question, "steps": steps,
            "answer": "(a) " + "; ".join(f"{k} {_frac(v)}" for k, v in phen.items() if v > 0)
                      + f"; (b) {_frac(phen[target])}; (c) {_frac(pg)}",
            "values": {"parent1": s1, "parent2": s2, "p_target_phenotype": float(phen[target]),
                       "target_genotype": g_target[0] + g_target[1], "p_target_genotype": float(pg)}}


@template("x_linked_cross", BIO, "Genetics", "Sex-linked inheritance", "medium")
def x_linked_cross(rng):
    disorder, letter = pick(rng, [("hemophilia A", "h"), ("red–green color blindness", "b"),
                                  ("Duchenne muscular dystrophy", "d")])
    D, d = letter.upper(), letter
    mother = pick(rng, [(D, d), (D, d), (D, D), (d, d)])
    father = pick(rng, [D, D, d]) if disorder != "Duchenne muscular dystrophy" else D
    if mother == (D, D) and father == D:
        mother = (D, d)
    sons = {x: Fraction(1, 2) for x in set(mother)} if mother[0] != mother[1] else {mother[0]: Fraction(1)}
    p_son_aff = sons.get(d, Fraction(0))
    p_dau_aff = p_son_aff if father == d else Fraction(0)
    p_dau_car = (1 - p_son_aff) if father == d else p_son_aff
    p_child_aff = (p_son_aff + p_dau_aff) / 2
    mtxt = f"X^{{{mother[0]}}}X^{{{mother[1]}}}"
    ftxt = f"X^{{{father}}}Y"
    m_word = {(D, D): "a non-carrier woman", (D, d): "a carrier woman", (d, d): "an affected woman"}[mother]
    f_word = "an unaffected man" if father == D else "an affected man"
    question = (
        f"{disorder[0].upper() + disorder[1:]} is an X-linked recessive disorder. {m_word[0].upper() + m_word[1:]} "
        f"(${mtxt}$) and {f_word} (${ftxt}$) have children. What is the probability that (a) a son is affected, "
        "(b) a daughter is affected, (c) a daughter is a carrier, and (d) a child of unknown sex is affected?"
    )
    steps = [
        "Sons receive their X from the mother and Y from the father; daughters receive one X from each parent.",
        f"Mother's gametes: $X^{{{mother[0]}}}$ and $X^{{{mother[1]}}}$ (1/2 each); father's: $X^{{{father}}}$ "
        "(to daughters) or $Y$ (to sons).",
        f"(a) A son is affected if he inherits $X^{{{d}}}$ from his mother: $P = {_frac(p_son_aff)}$.",
        f"(b) A daughter needs $X^{{{d}}}$ from both parents: $P = {_frac(p_dau_aff)}$.",
        f"(c) Carrier daughters ($X^{{{D}}}X^{{{d}}}$): $P = {_frac(p_dau_car)}$.",
        f"(d) Averaging over sex (1/2 each): $P = \\tfrac12({_frac(p_son_aff)}) + \\tfrac12({_frac(p_dau_aff)}) = {_frac(p_child_aff)}$.",
        "X-linked recessive traits are far more common in males because a single recessive allele is expressed in a "
        "hemizygous male.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"(a) {_frac(p_son_aff)}; (b) {_frac(p_dau_aff)}; (c) {_frac(p_dau_car)}; (d) {_frac(p_child_aff)}",
            "values": {"mother": "".join(mother), "father": father, "p_son_affected": float(p_son_aff),
                       "p_daughter_affected": float(p_dau_aff), "p_daughter_carrier": float(p_dau_car),
                       "p_child_affected": float(p_child_aff)}}


CHI_CRIT = {1: 3.841, 2: 5.991, 3: 7.815}


@template("chi_square_mendelian", BIO, "Genetics", "Chi-square goodness of fit", "hard")
def chi_square_mendelian(rng):
    case = pick(rng, [
        ("an F₂ monohybrid cross (Aa × Aa)", ["dominant", "recessive"], [3, 1]),
        ("an F₂ dihybrid cross (AaBb × AaBb)", ["dominant–dominant", "dominant–recessive", "recessive–dominant",
                                                "recessive–recessive"], [9, 3, 3, 1]),
        ("a test cross (Aa × aa)", ["dominant", "recessive"], [1, 1]),
        ("an F₂ cross with incomplete dominance (Rr × Rr)", ["red", "pink", "white"], [1, 2, 1]),
    ])
    label, classes, ratio = case
    N = nice(rng, 80, 800, 4)
    tot = sum(ratio)
    true = [r / tot for r in ratio]
    if rng.random() < 0.3:  # simulate a real deviation
        true = [t * (1 + rng.uniform(-0.35, 0.35)) for t in true]
        s = sum(true)
        true = [t / s for t in true]
    obs = _multinomial(rng, N, true)
    exp = [N * r / tot for r in ratio]
    chi = sum((o - e) ** 2 / e for o, e in zip(obs, exp))
    df = len(classes) - 1
    crit = CHI_CRIT[df]
    reject = chi > crit
    obs_txt = ", ".join(f"{c} {o}" for c, o in zip(classes, obs))
    question = (
        f"In {label} the expected phenotype ratio is {':'.join(map(str, ratio))}. Among {N} offspring the observed "
        f"counts were: {obs_txt}. Do the data fit the expected ratio (chi-square test, α = 0.05)?"
    )
    steps = [
        "Expected counts: " + ", ".join(f"{c} ${N} \\times {r}/{tot} = {e:.1f}$" for c, r, e in zip(classes, ratio, exp)) + ".",
        "$\\chi^2 = \\sum\\frac{(O-E)^2}{E} = " + " + ".join(
            f"\\frac{{({o} - {e:.1f})^2}}{{{e:.1f}}}" for o, e in zip(obs, exp)) + f" = {chi:.2f}$.",
        f"Degrees of freedom $= {len(classes)} - 1 = {df}$; critical value at α = 0.05 is {crit}.",
        (f"${chi:.2f} > {crit}$: reject the null hypothesis — the deviation is unlikely to be due to chance alone "
         "(consider linkage, lethality or mis-scoring)." if reject else
         f"${chi:.2f} < {crit}$: fail to reject the null hypothesis — the data are consistent with the "
         f"{':'.join(map(str, ratio))} ratio."),
    ]
    return {"question": question, "steps": steps,
            "answer": f"$\\chi^2 = {chi:.2f}$, df = {df}; " + ("does not fit" if reject else "consistent with") +
                      f" the {':'.join(map(str, ratio))} ratio",
            "values": {"observed": obs, "expected_ratio": ratio, "chi2": chi, "df": df, "reject": reject}}


@template("linkage_map_distance", BIO, "Genetics", "Linkage and recombination", "medium")
def linkage_map_distance(rng):
    N = nice(rng, 200, 2000, 10)
    rf = nice(rng, 0.02, 0.40, 0.01)
    R = round(N * rf)
    r1 = R // 2 + rng.randint(-min(5, R // 4), min(5, R // 4))
    r2 = R - r1
    P = N - R
    p1 = P // 2 + rng.randint(-10, 10)
    p2 = P - p1
    rf_obs = R / N
    question = (
        f"A dihybrid fruit fly with genotype $AB/ab$ (alleles in coupling) is test-crossed to an $ab/ab$ fly. The "
        f"offspring are: AB {p1}, ab {p2}, Ab {r1}, aB {r2}. Calculate the recombination frequency and the map distance "
        "between the two genes."
    )
    steps = [
        "Parental (non-recombinant) classes are the two most frequent: AB and ab. Recombinant classes: Ab and aB.",
        f"Recombinants: ${r1} + {r2} = {R}$ of ${N}$ offspring.",
        f"Recombination frequency $= {R}/{N} = {fmt(rf_obs, 3)}$ ({100 * rf_obs:.1f}%).",
        f"Map distance ≈ {100 * rf_obs:.1f} map units (centimorgans), since 1% recombination = 1 cM.",
        "Because recombination frequency is well below 50%, the genes are linked on the same chromosome."
        + (" (For distances above ~20 cM, double crossovers make the observed frequency underestimate the true "
           "distance.)" if rf_obs > 0.2 else ""),
    ]
    return {"question": question, "steps": steps,
            "answer": f"RF = {100 * rf_obs:.1f}% → {100 * rf_obs:.1f} cM",
            "values": {"N": N, "recombinants": R, "rf": rf_obs}}


# ---------------------------------------------------------------------------
# Molecular biology
# ---------------------------------------------------------------------------

_BASES = "TCAG"
_AA = "FFLLSSSSYY**CC*WLLLLPPPPHHQQRRRRIIIMTTTTNNKKSSRRVVVVAAAADDEEGGGG"
CODON_TABLE = {a + b + c: _AA[16 * i + 4 * j + k]
               for i, a in enumerate(_BASES) for j, b in enumerate(_BASES) for k, c in enumerate(_BASES)}
THREE = {"A": "Ala", "R": "Arg", "N": "Asn", "D": "Asp", "C": "Cys", "Q": "Gln", "E": "Glu", "G": "Gly",
         "H": "His", "I": "Ile", "L": "Leu", "K": "Lys", "M": "Met", "F": "Phe", "P": "Pro", "S": "Ser",
         "T": "Thr", "W": "Trp", "Y": "Tyr", "V": "Val", "*": "Stop"}
COMP = {"A": "T", "T": "A", "G": "C", "C": "G"}
SENSE = [c for c, aa in CODON_TABLE.items() if aa != "*"]
STOPS = ["TAA", "TAG", "TGA"]


def translate(dna):
    return [CODON_TABLE[dna[i:i + 3]] for i in range(0, len(dna) - 2, 3)]


@template("transcription_translation", BIO, "Molecular Biology", "Gene expression", "medium")
def transcription_translation(rng):
    n = rng.randint(4, 9)
    coding = "ATG" + "".join(pick(rng, SENSE) for _ in range(n)) + pick(rng, STOPS)
    template_strand = "".join(COMP[b] for b in coding)  # written 3'->5', aligned with coding strand
    mrna = coding.replace("T", "U")
    aas = translate(coding)
    protein = "-".join(THREE[a] for a in aas[:-1])
    codons = " ".join(mrna[i:i + 3] for i in range(0, len(mrna), 3))
    mutate = rng.random() < 0.6
    question = (
        f"The template (non-coding) strand of a short gene reads 3′-{template_strand}-5′. Write the mRNA "
        "sequence and the encoded peptide."
    )
    steps = [
        "RNA polymerase reads the template strand 3′→5′ and builds mRNA 5′→3′, pairing A–U, T–A, G–C, C–G.",
        f"mRNA: 5′-{mrna}-3′ (identical to the coding strand 5′-{coding}-3′ with U in place of T).",
        f"Split into codons from the start codon AUG: {codons}.",
        "Translate with the genetic code: " + ", ".join(
            f"{mrna[3 * i:3 * i + 3]}→{THREE[a]}" for i, a in enumerate(aas)) + ".",
        f"Peptide (N→C): {protein} ({len(aas) - 1} amino acids; the stop codon {mrna[-3:]} is not translated).",
    ]
    answer = f"mRNA 5′-{mrna}-3′; peptide {protein}"
    values = {"coding_strand": coding, "mrna": mrna, "protein": "".join(aas[:-1])}
    if mutate:
        ci = rng.randint(1, n)  # codon index (skip start and stop codons)
        pos = rng.randint(0, 2)
        old = coding[3 * ci + pos]
        new = pick(rng, [b for b in "ACGT" if b != old])
        mut = coding[:3 * ci + pos] + new + coding[3 * ci + pos + 1:]
        old_c, new_c = coding[3 * ci:3 * ci + 3], mut[3 * ci:3 * ci + 3]
        old_aa, new_aa = CODON_TABLE[old_c], CODON_TABLE[new_c]
        kind = "silent" if old_aa == new_aa else ("nonsense" if new_aa == "*" else "missense")
        effect = {
            "silent": f"both codons encode {THREE[old_aa]}, so the protein is unchanged (degeneracy of the code, often at the third position)",
            "nonsense": f"{new_c.replace('T', 'U')} is a stop codon, so translation terminates early and the peptide is truncated after {ci} amino acids",
            "missense": f"{THREE[old_aa]} is replaced by {THREE[new_aa]}",
        }[kind]
        question += (
            f" A point mutation changes nucleotide {3 * ci + pos + 1} of the coding strand from {old} to {new}. "
            "What kind of mutation is this?"
        )
        steps.append(
            f"Mutation: codon {ci + 1} changes from {old_c.replace('T', 'U')} to {new_c.replace('T', 'U')}; {effect}. "
            f"This is a **{kind}** mutation."
        )
        answer += f"; the point mutation is {kind}"
        values.update({"mutation_position": 3 * ci + pos + 1, "mutation_type": kind})
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("chargaff_rule", BIO, "Molecular Biology", "DNA structure", "easy")
def chargaff_rule(rng):
    org = pick(rng, ["a bacterium", "a plant", "a mammal", "a virus with double-stranded DNA"])
    base = pick(rng, ["A", "T", "G", "C"])
    pct = nice(rng, 15.0, 35.0, 0.5)
    pairs = {"A": "T", "T": "A", "G": "C", "C": "G"}
    comp = {base: pct, pairs[base]: pct}
    other = (100 - 2 * pct) / 2
    for b in "ATGC":
        comp.setdefault(b, other)
    gc_content = comp["G"] + comp["C"]
    question = (
        f"Double-stranded DNA from {org} contains {fmt(pct, 3)}% {base}. What are the percentages of the other three "
        "bases, and what is its GC content?"
    )
    steps = [
        "Chargaff's rules for double-stranded DNA: A pairs with T and G pairs with C, so %A = %T and %G = %C.",
        f"%{pairs[base]} = %{base} = {fmt(pct, 3)}%.",
        f"The remaining $100 - 2({fmt(pct, 3)}) = {fmt(100 - 2 * pct, 3)}$% is split equally between the other pair: "
        f"{fmt(other, 3)}% each.",
        f"GC content = %G + %C = {fmt(gc_content, 3)}%. Higher GC content means more hydrogen bonds (3 per G–C vs 2 per "
        "A–T) and stronger base stacking, hence a higher melting temperature.",
    ]
    return {"question": question, "steps": steps,
            "answer": ", ".join(f"{b} {fmt(comp[b], 3)}%" for b in "ATGC") + f"; GC content {fmt(gc_content, 3)}%",
            "values": {"A": comp["A"], "T": comp["T"], "G": comp["G"], "C": comp["C"], "GC": gc_content}}


@template("primer_melting_temperature", BIO, "Molecular Biology", "PCR primers", "easy")
def primer_melting_temperature(rng):
    n = rng.randint(12, 20)
    gcp = rng.uniform(0.3, 0.7)
    seq = "".join(pick(rng, "GC") if rng.random() < gcp else pick(rng, "AT") for _ in range(n))
    nA, nT, nG, nC = (seq.count(b) for b in "ATGC")
    gc = (nG + nC) / n * 100
    tm = 2 * (nA + nT) + 4 * (nG + nC)
    hb = 2 * (nA + nT) + 3 * (nG + nC)
    comp = "".join(COMP[b] for b in reversed(seq))
    cycles = rng.randint(20, 35)
    question = (
        f"A PCR primer has the sequence 5′-{seq}-3′. Find (a) its GC content, (b) its approximate melting "
        "temperature by the Wallace rule, (c) the number of hydrogen bonds it forms with its fully complementary target, "
        f"and (d) the sequence of that target strand (5′→3′). (e) Ideally, how many copies of a single target "
        f"molecule exist after {cycles} PCR cycles?"
    )
    steps = [
        f"Base counts: A {nA}, T {nT}, G {nG}, C {nC} (length {n}).",
        f"(a) GC content $= ({nG} + {nC})/{n} = {gc:.1f}\\%$.",
        f"(b) Wallace rule (short oligos): $T_m \\approx 2(A + T) + 4(G + C) = 2({nA + nT}) + 4({nG + nC}) = {tm}$ °C.",
        f"(c) Hydrogen bonds: 2 per A–T pair, 3 per G–C pair: $2({nA + nT}) + 3({nG + nC}) = {hb}$.",
        f"(d) The complementary strand is antiparallel, so read the complement backwards: 5′-{comp}-3′.",
        f"(e) Each cycle at most doubles the number of copies: $2^{{{cycles}}} = {fmt(2 ** cycles)}$ copies.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"(a) {gc:.1f}%; (b) {tm} °C; (c) {hb}; (d) 5′-{comp}-3′; (e) ${fmt(2 ** cycles)}$",
            "values": {"sequence": seq, "gc_percent": gc, "tm": tm, "h_bonds": hb, "complement": comp,
                       "cycles": cycles, "copies": 2 ** cycles}}


@template("michaelis_menten", BIO, "Biochemistry", "Enzyme kinetics", "medium")
def michaelis_menten(rng):
    Km = sig(rng.uniform(0.05, 20.0), 3)
    Vmax = nice(rng, 5, 500, 5)
    enzyme = pick(rng, ["an enzyme", "hexokinase", "an esterase", "a protease", "lactate dehydrogenase",
                        "a purified kinase"])
    if rng.random() < 0.5:
        S = sig(Km * rng.uniform(0.1, 10), 3)
        v = Vmax * S / (Km + S)
        question = (
            f"{enzyme[0].upper() + enzyme[1:]} follows Michaelis–Menten kinetics with $K_m = {fmt(Km)}$ mM and "
            f"$V_{{max}} = {Vmax}$ μmol/min. What is the reaction rate at a substrate concentration of {q(S, 'mM')}, "
            "and what fraction of $V_{max}$ is this?"
        )
        steps = [
            "$v = \\frac{V_{max}[S]}{K_m + [S]}$.",
            f"$v = \\frac{{({Vmax})({fmt(S)})}}{{{fmt(Km)} + {fmt(S)}}} = {fmt(v)}$ μmol/min.",
            f"Fraction of $V_{{max}}$: ${fmt(v / Vmax)}$ ({100 * v / Vmax:.0f}%). "
            + ("[S] < $K_m$, so the enzyme is far from saturated." if S < Km else
               "[S] > $K_m$, so the enzyme is approaching saturation."),
        ]
        answer = f"$v = {fmt(v)}$ μmol/min ({100 * v / Vmax:.0f}% of $V_{{max}}$)"
        values = {"Km": Km, "Vmax": Vmax, "S": S, "v": v}
    else:
        f = pick(rng, [0.1, 0.25, 0.5, 0.75, 0.8, 0.9, 0.95, 0.99])
        S = f * Km / (1 - f)
        question = (
            f"{enzyme[0].upper() + enzyme[1:]} has $K_m = {fmt(Km)}$ mM. What substrate concentration is required for the "
            f"enzyme to work at {round(100 * f)}% of its maximum rate?"
        )
        steps = [
            f"Set $v = {f}V_{{max}}$ in $v = \\frac{{V_{{max}}[S]}}{{K_m + [S]}}$: ${f} = \\frac{{[S]}}{{K_m + [S]}}$.",
            f"Solve: $[S] = \\frac{{{f}}}{{1 - {f}}}K_m = {fmt(f / (1 - f))} \\times {fmt(Km)} = {fmt(S)}$ mM.",
            "Each further step toward $V_{max}$ costs disproportionately more substrate — the hyperbola only approaches "
            "$V_{max}$ asymptotically. (At 50%, $[S] = K_m$, which is the definition of $K_m$.)",
        ]
        answer = f"$[S] = {fmt(S)}$ mM"
        values = {"Km": Km, "fraction": f, "S": S}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Physiology
# ---------------------------------------------------------------------------

RT_F_37 = R_GAS * 310.15 / FARADAY  # volts


@template("nernst_membrane_potential", BIO, "Physiology", "Membrane potential", "medium")
def nernst_membrane_potential(rng):
    ion, z, out_lo, out_hi, in_lo, in_hi = pick(rng, [
        ("K⁺", 1, 3.5, 5.5, 120, 155), ("Na⁺", 1, 135, 150, 5, 20), ("Cl⁻", -1, 100, 120, 4, 30),
        ("Ca²⁺", 2, 1.0, 2.5, 0.0001, 0.0001),
    ])
    co = nice(rng, out_lo, out_hi, 0.5 if out_hi < 10 else 1)
    ci = in_lo if in_lo == in_hi else nice(rng, in_lo, in_hi, 1)
    E = RT_F_37 / z * math.log(co / ci) * 1000
    slope = 61.5 / z
    question = (
        f"In a mammalian cell at 37 °C the {ion} concentration is {q(co, 'mM')} outside and {q(ci, 'mM')} inside. "
        f"Calculate the equilibrium (Nernst) potential for {ion}."
    )
    steps = [
        "Nernst equation: $E_{ion} = \\frac{RT}{zF}\\ln\\frac{[\\text{ion}]_{out}}{[\\text{ion}]_{in}}$; at 37 °C, "
        "$RT/F = 26.7$ mV, so $E \\approx \\frac{61.5\\text{ mV}}{z}\\log_{10}\\frac{[\\text{out}]}{[\\text{in}]}$.",
        f"$E = \\frac{{61.5}}{{{z}}}\\log_{{10}}\\frac{{{fmt(co)}}}{{{fmt(ci)}}} = ({fmt(slope)})({math.log10(co / ci):.3f}) = {E:.0f}$ mV.",
        f"Interpretation: at {E:.0f} mV (inside relative to outside) the electrical force on {ion} exactly balances its "
        "concentration gradient, so there is no net flux.",
    ]
    return {"question": question, "steps": steps, "answer": f"$E_{{ion}} \\approx {E:.0f}$ mV",
            "values": {"z": z, "c_out": co, "c_in": ci, "E_mV": E}}


@template("goldman_resting_potential", BIO, "Physiology", "Membrane potential", "hard")
def goldman_resting_potential(rng):
    Ko, Ki = nice(rng, 3.5, 6.0, 0.5), nice(rng, 130, 150, 5)
    Nao, Nai = nice(rng, 135, 150, 5), nice(rng, 10, 18, 1)
    Clo, Cli = nice(rng, 100, 120, 5), nice(rng, 5, 12, 1)
    pNa = pick(rng, [0.01, 0.02, 0.04, 0.05, 0.1])
    pCl = pick(rng, [0.0, 0.1, 0.2, 0.45])
    num = Ko + pNa * Nao + pCl * Cli
    den = Ki + pNa * Nai + pCl * Clo
    V = 61.5 * math.log10(num / den)
    EK = 61.5 * math.log10(Ko / Ki)
    question = (
        f"A neuron at 37 °C has [K⁺] = {Ko} mM out / {Ki} mM in, [Na⁺] = {Nao} out / {Nai} in, and [Cl⁻] = {Clo} out / "
        f"{Cli} in. The relative permeabilities are $P_K : P_{{Na}} : P_{{Cl}} = 1 : {pNa} : {pCl}$. Use the Goldman–"
        "Hodgkin–Katz equation to estimate the resting membrane potential, and compare it with $E_K$."
    )
    steps = [
        "GHK: $V_m = 61.5\\log_{10}\\frac{P_K[K]_o + P_{Na}[Na]_o + P_{Cl}[Cl]_i}{P_K[K]_i + P_{Na}[Na]_i + P_{Cl}[Cl]_o}$ mV "
        "(the anion's inside and outside concentrations swap places because of its negative charge).",
        f"Numerator: ${Ko} + {pNa}({Nao}) + {pCl}({Cli}) = {fmt(num, 4)}$.",
        f"Denominator: ${Ki} + {pNa}({Nai}) + {pCl}({Clo}) = {fmt(den, 4)}$.",
        f"$V_m = 61.5\\log_{{10}}({fmt(num / den)}) = {V:.1f}$ mV.",
        f"$E_K = 61.5\\log_{{10}}({Ko}/{Ki}) = {EK:.1f}$ mV. The resting potential lies close to $E_K$ because K⁺ "
        "permeability dominates, but the small Na⁺ leak pulls it a little toward $E_{Na}$ (positive).",
    ]
    return {"question": question, "steps": steps, "answer": f"$V_m \\approx {V:.1f}$ mV ($E_K = {EK:.1f}$ mV)",
            "values": {"Ko": Ko, "Ki": Ki, "Nao": Nao, "Nai": Nai, "Clo": Clo, "Cli": Cli, "pNa": pNa, "pCl": pCl,
                       "Vm_mV": V, "EK_mV": EK}}


@template("cardiac_output", BIO, "Physiology", "Cardiovascular physiology", "easy")
def cardiac_output(rng):
    if rng.random() < 0.6:
        HR = nice(rng, 50, 180, 2)
        SV = nice(rng, 50, 120, 5)
        CO = HR * SV / 1000
        blood = nice(rng, 4.5, 6.0, 0.5)
        question = (
            f"A person's heart rate is {HR} beats/min and the stroke volume is {SV} mL. Calculate the cardiac output and "
            f"estimate how long it takes to pump a volume equal to the total blood volume ({fmt(blood)} L)."
        )
        steps = [
            "Cardiac output = heart rate × stroke volume.",
            f"$CO = ({HR})({SV}\\text{{ mL}}) = {HR * SV}$ mL/min $= {fmt(CO)}$ L/min.",
            f"Time to pump the whole blood volume: ${fmt(blood)}/{fmt(CO)} = {fmt(blood / CO)}$ min ($\\approx {fmt(60 * blood / CO)}$ s).",
        ]
        answer = f"$CO = {fmt(CO)}$ L/min; about {fmt(60 * blood / CO)} s per full circulation"
        values = {"HR": HR, "SV": SV, "CO": CO, "blood_L": blood}
    else:
        VO2 = nice(rng, 200, 3000, 50)
        Ca = nice(rng, 180, 210, 1)
        Cv = nice(rng, 60, 160, 1)
        CO = VO2 / (Ca - Cv)
        question = (
            f"During exercise a person consumes {VO2} mL O₂/min. Arterial blood contains {Ca} mL O₂ per liter and mixed "
            f"venous blood {Cv} mL O₂ per liter. Use the Fick principle to calculate the cardiac output."
        )
        steps = [
            "Fick principle: oxygen uptake = blood flow × arteriovenous O₂ difference, so $CO = \\frac{\\dot V_{O_2}}{C_a - C_v}$.",
            f"$C_a - C_v = {Ca} - {Cv} = {Ca - Cv}$ mL O₂/L.",
            f"$CO = {VO2}/{Ca - Cv} = {fmt(CO)}$ L/min.",
            "During exercise both cardiac output and O₂ extraction (a wider a–v difference) increase.",
        ]
        answer = f"$CO = {fmt(CO)}$ L/min"
        values = {"VO2": VO2, "Ca": Ca, "Cv": Cv, "CO": CO}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("water_potential", BIO, "Physiology", "Water potential", "medium")
def water_potential(rng):
    solute, i = pick(rng, [("sucrose", 1), ("sucrose", 1), ("NaCl", 2), ("glucose", 1)])
    C = nice(rng, 0.05, 0.80, 0.05)
    TC = nice(rng, 15, 30, 1)
    T = TC + 273.15
    psi_s = -i * C * 0.0831 * T
    psi_p = nice(rng, 0.0, 0.8, 0.1)
    psi_cell = psi_s + psi_p
    C_out = nice(rng, 0.0, 0.8, 0.05)
    psi_out = -C_out * 0.0831 * T  # surrounding sucrose solution, open beaker
    direction = ("into the cell" if psi_out > psi_cell else "out of the cell" if psi_out < psi_cell else
                 "in neither direction (net)")
    question = (
        f"A plant cell's contents behave like a {q(C, 'M')} {solute} solution at {TC} °C, and the cell's pressure potential "
        f"is {q(psi_p, 'bar')}. The cell is placed in an open beaker of {q(C_out, 'M')} sucrose. Calculate the water "
        "potential of the cell and of the solution, and state the direction of net water movement."
    )
    steps = [
        "Solute potential: $\\psi_s = -iCRT$ with $R = 0.0831$ L·bar/(mol·K).",
        f"Cell: $\\psi_s = -({i})({fmt(C)})(0.0831)({fmt(T, 5)}) = {psi_s:.2f}$ bar; $\\psi = \\psi_s + \\psi_p = "
        f"{psi_s:.2f} + {fmt(psi_p)} = {psi_cell:.2f}$ bar.",
        f"Solution (open beaker, $\\psi_p = 0$): $\\psi = -(1)({fmt(C_out)})(0.0831)({fmt(T, 5)}) = {psi_out:.2f}$ bar.",
        f"Water moves from higher (less negative) to lower water potential: net movement {direction}.",
    ]
    if solute == "NaCl":
        steps.insert(1, "NaCl dissociates into two ions, so $i = 2$.")
    return {"question": question, "steps": steps,
            "answer": f"$\\psi_{{cell}} = {psi_cell:.2f}$ bar, $\\psi_{{solution}} = {psi_out:.2f}$ bar; water moves {direction}",
            "values": {"i": i, "C": C, "T": T, "psi_p": psi_p, "psi_cell": psi_cell, "C_out": C_out, "psi_out": psi_out}}


@template("q10_temperature_coefficient", BIO, "Physiology", "Temperature and metabolic rate", "easy")
def q10_temperature_coefficient(rng):
    organism = pick(rng, ["a lizard", "a frog", "an insect", "a goldfish", "an isolated enzyme preparation",
                          "a crab"])
    T1 = nice(rng, 5, 25, 1)
    T2 = T1 + nice(rng, 4, 15, 1)
    R1 = nice(rng, 10, 200, 1)
    Q10_true = nice(rng, 1.5, 3.5, 0.1)
    R2 = sig(R1 * Q10_true ** ((T2 - T1) / 10), 3)
    Q10 = (R2 / R1) ** (10 / (T2 - T1))
    question = (
        f"The oxygen consumption of {organism} is {R1} μL O₂/(g·h) at {T1} °C and {fmt(R2)} μL O₂/(g·h) at {T2} °C. "
        "Calculate the $Q_{10}$ temperature coefficient."
    )
    steps = [
        "$Q_{10} = \\left(\\frac{R_2}{R_1}\\right)^{10/(T_2 - T_1)}$.",
        f"$\\frac{{R_2}}{{R_1}} = {fmt(R2)}/{R1} = {fmt(R2 / R1)}$; exponent $10/({T2} - {T1}) = {fmt(10 / (T2 - T1))}$.",
        f"$Q_{{10}} = ({fmt(R2 / R1)})^{{{fmt(10 / (T2 - T1))}}} = {fmt(Q10)}$.",
        "Most biological rates have $Q_{10}$ between 2 and 3: they roughly double or triple for every 10 °C rise.",
    ]
    return {"question": question, "steps": steps, "answer": f"$Q_{{10}} = {fmt(Q10)}$",
            "values": {"R1": R1, "T1": T1, "R2": R2, "T2": T2, "Q10": Q10}}


# ---------------------------------------------------------------------------
# Cell biology and microbiology
# ---------------------------------------------------------------------------


@template("microscope_magnification", BIO, "Cell Biology", "Microscopy", "easy")
def microscope_magnification(rng):
    cell, real_um = pick(rng, [("red blood cell", 7.5), ("human cheek cell", 60.0), ("E. coli bacterium", 2.0),
                               ("yeast cell", 5.0), ("onion epidermal cell", 250.0), ("chloroplast", 5.0),
                               ("mitochondrion", 1.0), ("Paramecium", 200.0)])
    real = sig(real_um * rng.uniform(0.8, 1.25), 2)
    if real_um < 10:
        mag = pick(rng, [1000, 2000, 5000, 10000, 20000])  # micrograph from an electron or oil-immersion image
    else:
        mag = pick(rng, [40, 100, 200, 400])
    image_mm = real * mag / 1000
    question = (
        f"In a micrograph taken at a magnification of ×{mag:,}, a {cell} measures {q(image_mm, 'mm')} across. "
        "What is its actual size in micrometers?"
    )
    steps = [
        "Actual size = image size ÷ magnification.",
        f"Convert the image size: {fmt(image_mm)} mm $= {fmt(image_mm * 1000)}$ μm.",
        f"Actual size $= {fmt(image_mm * 1000)}/{mag} = {fmt(real)}$ μm.",
    ]
    return {"question": question, "steps": steps, "answer": f"about ${fmt(real)}$ μm",
            "values": {"magnification": mag, "image_mm": image_mm, "actual_um": real}}


@template("surface_area_volume", BIO, "Cell Biology", "Cell size", "easy")
def surface_area_volume(rng):
    r1 = nice(rng, 1, 10, 1)
    r2 = r1 * pick(rng, [2, 3, 4, 5, 10])
    rows = []
    for r in (r1, r2):
        SA = 4 * math.pi * r ** 2
        V = 4 / 3 * math.pi * r ** 3
        rows.append((r, SA, V, SA / V))
    question = (
        f"Model two cells as spheres of radius {r1} μm and {r2} μm. Calculate the surface area, volume and surface-area-"
        "to-volume ratio of each, and explain why cells are generally small."
    )
    steps = ["For a sphere, $A = 4\\pi r^2$, $V = \\tfrac43\\pi r^3$, so $A/V = 3/r$."]
    for r, SA, V, ratio in rows:
        steps.append(f"$r = {r}$ μm: $A = {fmt(SA)}$ μm², $V = {fmt(V)}$ μm³, $A/V = {fmt(ratio)}$ μm⁻¹.")
    steps.append(
        f"Making the cell {r2 // r1}× wider multiplies its volume (metabolic demand) by {(r2 // r1) ** 3} but its surface "
        f"(exchange capacity) only by {(r2 // r1) ** 2}, so $A/V$ falls {r2 // r1}-fold. Small cells exchange materials "
        "with their surroundings fast enough by diffusion; large cells cannot."
    )
    return {"question": question, "steps": steps,
            "answer": f"A/V = {fmt(rows[0][3])} μm⁻¹ vs {fmt(rows[1][3])} μm⁻¹ — the smaller cell has {r2 // r1}× more "
                      "surface per unit volume",
            "values": {"r1": r1, "r2": r2, "ratio1": rows[0][3], "ratio2": rows[1][3]}}


@template("bacterial_growth", BIO, "Microbiology", "Bacterial growth", "easy")
def bacterial_growth(rng):
    species, td = pick(rng, [("Escherichia coli", 20), ("Escherichia coli", 30), ("Bacillus subtilis", 25),
                             ("Staphylococcus aureus", 30), ("Vibrio natriegens", 10),
                             ("Mycobacterium tuberculosis", 1080), ("a soil bacterium", 60)])
    N0 = nice(rng, 1, 9, 1) * 10 ** rng.randint(1, 4)
    gens = rng.randint(4, 20)
    t = gens * td
    N = N0 * 2 ** gens
    target = N0 * 10 ** rng.randint(3, 6)
    t_target = td * math.log2(target / N0)
    unit = "min"
    question = (
        f"A culture of {species} with a doubling time of {td} min starts with {N0:,} cells in exponential phase. "
        f"(a) How many cells are present after {fmt(t / 60, 3)} h? (b) How long until the population reaches {target:,} "
        "cells (assuming growth stays exponential)?"
    )
    steps = [
        f"(a) Number of generations: $n = t/t_d = {t}/{td} = {gens}$; $N = N_0 2^n = {N0} \\times 2^{{{gens}}} = {fmt(N)}$ cells.",
        f"(b) $t = t_d\\log_2(N/N_0) = {td}\\log_2({fmt(target / N0)}) = {td} \\times {fmt(math.log2(target / N0))} = "
        f"{fmt(t_target)}$ {unit} $= {fmt(t_target / 60)}$ h.",
        "In reality, nutrient depletion and waste accumulation end exponential growth (stationary phase).",
    ]
    return {"question": question, "steps": steps,
            "answer": f"(a) ${fmt(N)}$ cells; (b) ${fmt(t_target / 60)}$ h",
            "values": {"N0": N0, "td_min": td, "t_min": t, "N": N, "target": target, "t_target_min": t_target}}


@template("serial_dilution_plate_count", BIO, "Microbiology", "Viable counts", "medium")
def serial_dilution_plate_count(rng):
    k = rng.randint(4, 8)
    vol = pick(rng, [0.1, 0.1, 1.0])
    colonies = rng.randint(30, 300)
    cfu = colonies / (vol * 10 ** -k)
    question = (
        f"A bacterial culture is serially diluted tenfold to $10^{{-{k}}}$, and {q(vol, 'mL', 1)} of that dilution is "
        f"spread on an agar plate. After incubation the plate has {colonies} colonies. What was the concentration of "
        "viable cells in the original culture?"
    )
    steps = [
        f"Colonies per mL of the plated dilution: ${colonies}/{fmt(vol, 1)} = {fmt(colonies / vol)}$ CFU/mL.",
        f"Correct for dilution: multiply by $10^{{{k}}}$: ${fmt(colonies / vol)} \\times 10^{{{k}}} = {fmt(cfu)}$ CFU/mL.",
        "The count is reliable because it falls in the statistically acceptable 30–300 colony range. Each colony is "
        "assumed to arise from one viable cell (hence 'colony-forming units').",
    ]
    return {"question": question, "steps": steps, "answer": f"${fmt(cfu)}$ CFU/mL",
            "values": {"dilution_exp": k, "volume_mL": vol, "colonies": colonies, "cfu_per_mL": cfu}}


# ---------------------------------------------------------------------------
# Ecology
# ---------------------------------------------------------------------------


@template("trophic_energy_transfer", BIO, "Ecology", "Energy flow", "easy")
def trophic_energy_transfer(rng):
    E0 = nice(rng, 1, 9, 1) * 10 ** rng.randint(3, 6)
    eff = pick(rng, [0.10, 0.10, 0.05, 0.15, 0.20])
    chain = pick(rng, [["phytoplankton", "zooplankton", "small fish", "tuna", "orca"],
                       ["grass", "grasshoppers", "frogs", "snakes", "hawks"],
                       ["oak leaves", "caterpillars", "songbirds", "weasels", "owls"],
                       ["algae", "snails", "crayfish", "raccoons", "coyotes"]])
    lvl = rng.randint(2, 4)
    levels = [E0 * eff ** i for i in range(lvl + 1)]
    question = (
        f"In a food chain {' → '.join(chain[:lvl + 1])}, the producers capture {E0:,} kJ/m²/yr of energy. Assuming "
        f"{round(eff * 100)}% of the energy is transferred from each trophic level to the next, how much energy reaches "
        f"the {chain[lvl]}? What happens to the rest?"
    )
    steps = [f"Energy at each level is {round(eff * 100)}% of the level below: $E_n = E_0 \\times {eff}^n$."]
    for i in range(1, lvl + 1):
        steps.append(f"{chain[i].capitalize()} (level {i + 1}): ${fmt(levels[i - 1])} \\times {eff} = {fmt(levels[i])}$ kJ/m²/yr.")
    steps.append(
        "The other energy at each step is lost mainly as heat from cellular respiration, and as material that is not "
        "eaten, digested or absorbed — which is why food chains rarely exceed 4–5 levels."
    )
    return {"question": question, "steps": steps, "answer": f"${fmt(levels[-1])}$ kJ/m²/yr reaches the {chain[lvl]}",
            "values": {"E0": E0, "efficiency": eff, "levels": lvl, "E_top": levels[-1]}}


@template("mark_recapture", BIO, "Ecology", "Population size estimation", "easy")
def mark_recapture(rng):
    animal = pick(rng, ["field mice", "trout", "butterflies", "turtles", "snails", "lizards", "grasshoppers"])
    N_true = nice(rng, 200, 5000, 50)
    M = rng.randint(30, min(300, N_true // 3))
    C = rng.randint(30, min(400, N_true // 2))
    R = max(1, round(C * M / N_true + rng.uniform(-2, 2)))
    R = min(R, C, M)
    N = M * C / R
    question = (
        f"Ecologists capture, mark and release {M} {animal}. A week later they capture {C} {animal}, of which {R} are "
        "marked. Estimate the population size, and state two assumptions of the method."
    )
    steps = [
        "Lincoln–Petersen index: the marked fraction in the second sample estimates the marked fraction of the whole "
        "population, $R/C = M/N$.",
        f"$N = \\frac{{MC}}{{R}} = \\frac{{({M})({C})}}{{{R}}} = {fmt(N, 4)} \\approx {round(N)}$ individuals.",
        "Assumptions: the population is closed (no births, deaths or migration between samples); marks are not lost and "
        "do not affect survival or catchability; marked animals mix randomly with unmarked ones.",
    ]
    return {"question": question, "steps": steps, "answer": f"$N \\approx {round(N)}$ {animal}",
            "values": {"M": M, "C": C, "R": R, "N": N}}


@template("population_growth_models", BIO, "Ecology", "Population growth", "medium")
def population_growth_models(rng):
    r = nice(rng, 0.02, 0.80, 0.01)
    K = nice(rng, 500, 20000, 100)
    N0 = nice(rng, 10, max(20, K // 10), 5)
    t = nice(rng, 2, 20, 1)
    N_exp = N0 * math.exp(r * t)
    N_log = K / (1 + (K - N0) / N0 * math.exp(-r * t))
    N_now = nice(rng, K // 10, K - K // 10, 10)
    dNdt = r * N_now * (1 - N_now / K)
    question = (
        f"A population has intrinsic growth rate $r = {fmt(r)}$ per year, carrying capacity $K = {K}$ and initial size "
        f"$N_0 = {N0}$. (a) Predict its size after {t} years using the exponential and logistic models. (b) What is "
        f"the logistic growth rate when $N = {N_now}$, and what is the maximum possible growth rate? (c) What is the "
        "doubling time while the population is still small?"
    )
    steps = [
        f"(a) Exponential: $N = N_0e^{{rt}} = {N0}e^{{({fmt(r)})({t})}} = {fmt(N_exp)}$.",
        f"Logistic: $N = \\frac{{K}}{{1 + \\frac{{K - N_0}}{{N_0}}e^{{-rt}}}} = \\frac{{{K}}}{{1 + {fmt((K - N0) / N0)}e^{{-{fmt(r * t)}}}}} = {fmt(N_log)}$.",
        f"(b) $\\frac{{dN}}{{dt}} = rN\\left(1 - \\frac{{N}}{{K}}\\right) = ({fmt(r)})({N_now})\\left(1 - \\frac{{{N_now}}}{{{K}}}\\right) = {fmt(dNdt)}$ per year.",
        f"The maximum occurs at $N = K/2 = {fmt(K / 2)}$: $(dN/dt)_{{max}} = rK/4 = {fmt(r * K / 4)}$ per year.",
        f"(c) Doubling time $= \\ln 2/r = {fmt(math.log(2) / r)}$ years (≈ 70/(100r), the 'rule of 70').",
    ]
    return {"question": question, "steps": steps,
            "answer": f"(a) exponential ${fmt(N_exp)}$, logistic ${fmt(N_log)}$; (b) ${fmt(dNdt)}$/yr, max ${fmt(r * K / 4)}$/yr; "
                      f"(c) ${fmt(math.log(2) / r)}$ yr",
            "values": {"r": r, "K": K, "N0": N0, "t": t, "N_exp": N_exp, "N_log": N_log, "N_now": N_now,
                       "dNdt": dNdt, "doubling_time": math.log(2) / r}}


@template("species_diversity", BIO, "Ecology", "Biodiversity indices", "medium")
def species_diversity(rng):
    S = rng.randint(3, 6)
    names = rng.sample(["oak", "maple", "birch", "pine", "beech", "ash", "hickory", "spruce"], S)
    counts = [rng.randint(2, 60) for _ in range(S)]
    N = sum(counts)
    D = 1 - sum(n * (n - 1) for n in counts) / (N * (N - 1))
    ps = [n / N for n in counts]
    Hs = -sum(p * math.log(p) for p in ps)
    E = Hs / math.log(S)
    question = (
        "A forest plot contains the following numbers of trees: " + ", ".join(f"{s} {n}" for s, n in zip(names, counts))
        + ". Calculate Simpson's diversity index ($1 - D$), the Shannon index $H'$ and Shannon evenness."
    )
    steps = [
        f"Total individuals $N = {N}$, species richness $S = {S}$.",
        "Simpson: $1 - \\frac{\\sum n(n-1)}{N(N-1)} = 1 - \\frac{" + " + ".join(f"{n}({n - 1})" for n in counts)
        + f"}}{{{N}({N - 1})}} = {D:.3f}$ (probability that two randomly chosen trees belong to different species).",
        "Shannon: $H' = -\\sum p_i\\ln p_i$ with $p_i = n_i/N$: " + ", ".join(f"{p:.3f}" for p in ps)
        + f" → $H' = {Hs:.3f}$.",
        f"Evenness: $E = H'/\\ln S = {Hs:.3f}/{math.log(S):.3f} = {E:.3f}$ (1 = all species equally abundant).",
    ]
    return {"question": question, "steps": steps,
            "answer": f"Simpson $1 - D = {D:.3f}$; $H' = {Hs:.3f}$; evenness ${E:.3f}$",
            "values": {"counts": counts, "simpson": D, "shannon": Hs, "evenness": E}}
