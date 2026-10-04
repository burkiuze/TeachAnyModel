"""Mathematics for science: calculus, linear algebra, ODEs, probability, statistics, numerics."""

import math
from fractions import Fraction

from .common import fmt, nice, pick, q, sig, template

MATH = "Mathematics"

# ---------------------------------------------------------------------------
# Helpers
# ---------------------------------------------------------------------------


def poly_str(coeffs, var="x"):
    """LaTeX for a polynomial given coefficients from the highest power down."""
    n = len(coeffs) - 1
    terms = []
    for i, c in enumerate(coeffs):
        p = n - i
        if c == 0:
            continue
        cs = _num(abs(c))
        if p == 0:
            body = cs
        else:
            coef = "" if abs(c) == 1 else cs
            body = coef + (var if p == 1 else f"{var}^{{{p}}}")
        sign = "-" if c < 0 else "+"
        terms.append((sign, body))
    if not terms:
        return "0"
    first_sign, first = terms[0]
    out = ("-" if first_sign == "-" else "") + first
    for sign, body in terms[1:]:
        out += f" {sign} {body}"
    return out


def _num(x):
    if isinstance(x, Fraction):
        if x.denominator == 1:
            return str(x.numerator)
        return ("-" if x < 0 else "") + f"\\tfrac{{{abs(x.numerator)}}}{{{x.denominator}}}"
    if isinstance(x, float) and x.is_integer():
        return str(int(x))
    return str(x)


def poly_eval(coeffs, x):
    total = 0
    for c in coeffs:
        total = total * x + c
    return total


def phi(z):
    """Standard normal CDF."""
    return 0.5 * (1 + math.erf(z / math.sqrt(2)))


def det3(m):
    return (m[0][0] * (m[1][1] * m[2][2] - m[1][2] * m[2][1])
            - m[0][1] * (m[1][0] * m[2][2] - m[1][2] * m[2][0])
            + m[0][2] * (m[1][0] * m[2][1] - m[1][1] * m[2][0]))


def _exp(r, var="t"):
    """e^{rt} with tidy coefficients: e^{-t}, e^{-3t}."""
    coef = "" if r == 1 else "-" if r == -1 else str(r)
    return f"e^{{{coef}{var}}}"


def _signed(c, s, first=False):
    if c == 0:
        return ""
    mag = "" if abs(c) == 1 else str(abs(c))
    if first:
        return ("-" if c < 0 else "") + mag + s
    return (" - " if c < 0 else " + ") + mag + s


# ---------------------------------------------------------------------------
# Calculus
# ---------------------------------------------------------------------------


@template("derivative_tangent_line", MATH, "Calculus", "Derivatives", "easy")
def derivative_tangent_line(rng):
    deg = rng.randint(2, 4)
    coeffs = [rng.randint(-6, 6) for _ in range(deg + 1)]
    if coeffs[0] == 0:
        coeffs[0] = pick(rng, [1, 2, 3, -1, -2])
    d = [c * (deg - i) for i, c in enumerate(coeffs[:-1])]
    x0 = rng.randint(-3, 3)
    y0 = poly_eval(coeffs, x0)
    m = poly_eval(d, x0)
    b = y0 - m * x0
    question = (
        f"Let $f(x) = {poly_str(coeffs)}$. Find $f'(x)$, and the equation of the tangent line to the curve at $x = {x0}$."
    )
    steps = [
        "Power rule term by term: $\\frac{d}{dx}x^n = nx^{n-1}$, and the derivative of a constant is 0.",
        f"$f'(x) = {poly_str(d)}$.",
        f"Point of tangency: $f({x0}) = {y0}$. Slope: $f'({x0}) = {m}$.",
        (f"Tangent line: $y = f({x0}) + f'({x0})(x - ({x0})) = {poly_str([m, b])}$." if m != 0 else
         f"Tangent line: $f'({x0}) = 0$, so it is horizontal, $y = {y0}$ (a stationary point)."),
    ]
    return {"question": question, "steps": steps,
            "answer": f"$f'(x) = {poly_str(d)}$; tangent: $y = {poly_str([m, b]) if m != 0 else y0}$",
            "values": {"coeffs": coeffs, "derivative": d, "x0": x0, "slope": m, "intercept": b}}


@template("definite_integral_polynomial", MATH, "Calculus", "Integrals", "easy")
def definite_integral_polynomial(rng):
    deg = rng.randint(1, 3)
    coeffs = [rng.randint(-5, 5) for _ in range(deg + 1)]
    if coeffs[0] == 0:
        coeffs[0] = pick(rng, [1, 2, 3, -1])
    a = rng.randint(-2, 1)
    b = a + rng.randint(1, 4)
    anti = [Fraction(c, deg - i + 1) for i, c in enumerate(coeffs)] + [Fraction(0)]
    Fb = poly_eval(anti, Fraction(b))
    Fa = poly_eval(anti, Fraction(a))
    val = Fb - Fa
    context = pick(rng, [
        "", f" Interpret the result if the integrand is a velocity in m/s and $x$ is time in s.",
    ])
    question = f"Evaluate $\\int_{{{a}}}^{{{b}}} \\left({poly_str(coeffs)}\\right)dx$.{context}"
    steps = [
        "Antiderivative term by term: $\\int x^n\\,dx = \\frac{x^{n+1}}{n+1}$.",
        f"$F(x) = {poly_str(anti)}$.",
        f"$F({b}) = {_num(Fb)}$, $F({a}) = {_num(Fa)}$.",
        f"Fundamental theorem of calculus: $\\int_{{{a}}}^{{{b}}} f\\,dx = F({b}) - F({a}) = {_num(val)}$"
        + (f" $\\approx {fmt(float(val), 4)}$." if val.denominator != 1 else "."),
    ]
    if context:
        steps.append(f"The integral of velocity is the displacement: ${fmt(float(val), 4)}$ m between $t = {a}$ s and "
                     f"$t = {b}$ s (a negative value means net motion in the negative direction).")
    return {"question": question, "steps": steps,
            "answer": f"${_num(val)}$" + (f" $\\approx {fmt(float(val), 4)}$" if val.denominator != 1 else ""),
            "values": {"coeffs": coeffs, "a": a, "b": b, "integral": float(val)}}


TAYLOR = [
    ("\\sin x", "x - \\frac{x^3}{6}", lambda x: math.sin(x), lambda x: x - x ** 3 / 6, "the small-angle approximation for a pendulum"),
    ("e^x", "1 + x + \\frac{x^2}{2}", math.exp, lambda x: 1 + x + x * x / 2, "growth and decay over short times"),
    ("\\sqrt{1 + x}", "1 + \\frac{x}{2} - \\frac{x^2}{8}", lambda x: math.sqrt(1 + x),
     lambda x: 1 + x / 2 - x * x / 8, "small corrections in relativity and optics"),
    ("\\ln(1 + x)", "x - \\frac{x^2}{2}", lambda x: math.log(1 + x), lambda x: x - x * x / 2, "small relative changes"),
    ("\\frac{1}{1 - x}", "1 + x + x^2", lambda x: 1 / (1 - x), lambda x: 1 + x + x * x, "geometric series"),
    ("\\cos x", "1 - \\frac{x^2}{2}", math.cos, lambda x: 1 - x * x / 2, "small oscillations"),
]


@template("taylor_approximation", MATH, "Calculus", "Taylor series", "medium")
def taylor_approximation(rng):
    f_tex, approx_tex, f, g, use = pick(rng, TAYLOR)
    x = pick(rng, [0.05, 0.1, 0.15, 0.2, 0.3, 0.5, -0.1, -0.2])
    exact = f(x)
    approx = g(x)
    rel = abs(approx - exact) / abs(exact)
    question = (
        f"Use the Taylor (Maclaurin) polynomial ${f_tex} \\approx {approx_tex}$ to approximate the function at $x = {x}$. "
        "Compare with the exact value and give the relative error."
    )
    steps = [
        f"The polynomial keeps the first terms of the series expansion about $x = 0$; it is accurate when $|x| \\ll 1$ "
        f"(useful for {use}).",
        f"Approximation: ${approx_tex.replace('x', f'({x})')} = {approx:.6f}$.",
        f"Exact value: ${f_tex.replace('x', f'({x})')} = {exact:.6f}$.",
        f"Relative error: $\\frac{{|{approx:.6f} - {exact:.6f}|}}{{{abs(exact):.6f}}} = {fmt(rel)}$ "
        f"({fmt(100 * rel)}%). The error is roughly the size of the first omitted term and shrinks rapidly as $x \\to 0$.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"approx ${approx:.6f}$, exact ${exact:.6f}$, relative error ${fmt(rel)}$",
            "values": {"x": x, "approx": approx, "exact": exact, "rel_error": rel}}


# ---------------------------------------------------------------------------
# Differential equations
# ---------------------------------------------------------------------------


@template("newton_cooling", MATH, "Differential Equations", "First-order ODEs", "medium")
def newton_cooling(rng):
    obj = pick(rng, ["a cup of coffee", "a bowl of soup", "a metal casting", "a cooked turkey", "a forensic sample"])
    Ts = nice(rng, 15, 25, 1)
    T0 = nice(rng, 60, 95, 1) if obj != "a metal casting" else nice(rng, 300, 600, 10)
    t1 = nice(rng, 2, 20, 1)
    k_true = rng.uniform(0.02, min(0.2, 2.0 / t1))
    T1 = round(Ts + (T0 - Ts) * math.exp(-k_true * t1), 1)
    k = math.log((T0 - Ts) / (T1 - Ts)) / t1
    Tx = Ts + max(2, round((T1 - Ts) * pick(rng, [0.2, 0.3, 0.4, 0.5])))
    tx = math.log((T0 - Ts) / (Tx - Ts)) / k
    question = (
        f"{obj[0].upper() + obj[1:]} at {T0} °C is placed in a room at {Ts} °C. After {t1} min its temperature is {T1} °C. "
        f"Assuming Newton's law of cooling, find the cooling constant and the time at which it reaches {Tx} °C."
    )
    steps = [
        "Newton's law of cooling: $\\frac{dT}{dt} = -k(T - T_s)$. Separating variables gives "
        "$T(t) = T_s + (T_0 - T_s)e^{-kt}$.",
        f"Use the measurement: ${T1} = {Ts} + ({T0} - {Ts})e^{{-{t1}k}} \\Rightarrow k = \\frac{{1}}{{{t1}}}\\ln\\frac{{{T0 - Ts}}}{{{T1 - Ts:.1f}}} = {fmt(k)}$ min⁻¹.",
        f"Solve ${Tx} = {Ts} + {T0 - Ts}e^{{-kt}}$: $t = \\frac{{1}}{{k}}\\ln\\frac{{{T0 - Ts}}}{{{Tx - Ts}}} = {fmt(tx)}$ min.",
        "The temperature difference decays exponentially: the object approaches room temperature but never quite reaches it.",
    ]
    return {"question": question, "steps": steps, "answer": f"$k = {fmt(k)}$ min⁻¹; $t \\approx {fmt(tx)}$ min",
            "values": {"T0": T0, "Ts": Ts, "t1": t1, "T1": T1, "k": k, "Tx": Tx, "tx": tx}}


@template("second_order_linear_ode", MATH, "Differential Equations", "Second-order linear ODEs", "hard")
def second_order_linear_ode(rng):
    kind = pick(rng, ["over", "critical", "under"])
    if kind == "over":
        r1, r2 = sorted(rng.sample(range(-6, 0), 2))
        b, c = -(r1 + r2), r1 * r2
    elif kind == "critical":
        r1 = r2 = rng.randint(-5, -1)
        b, c = -2 * r1, r1 * r1
    else:
        al, be = rng.randint(-3, -1), rng.randint(1, 4)
        b, c = -2 * al, al * al + be * be
    y0 = rng.randint(-3, 4) or 1
    v0 = rng.randint(-5, 5)
    eq = "y''" + _signed(b, "y'") + _signed(c, "y") + " = 0"
    char_eq = "r^2" + _signed(b, "r") + (f" + {c}" if c > 0 else "")
    disc = b * b - 4 * c
    steps = [
        f"Try $y = e^{{rt}}$: characteristic equation ${char_eq} = 0$, discriminant $b^2 - 4c = {disc}$.",
    ]
    if kind == "over":
        C2 = Fraction(v0 - r1 * y0, r2 - r1)
        C1 = y0 - C2
        sol = f"y(t) = {_num(C1)}{_exp(r1)} + {_num(C2)}{_exp(r2)}".replace("+ -", "- ")
        steps += [
            f"Two distinct real roots: $r_1 = {r1}$, $r_2 = {r2}$ → $y = C_1{_exp(r1)} + C_2{_exp(r2)}$ (overdamped).",
            f"Initial conditions: $C_1 + C_2 = {y0}$ and $({r1})C_1 + ({r2})C_2 = {v0}$ → $C_1 = {_num(C1)}$, $C_2 = {_num(C2)}$.",
        ]
        values = {"C1": float(C1), "C2": float(C2), "r1": r1, "r2": r2}
    elif kind == "critical":
        C1 = y0
        C2 = v0 - r1 * y0
        sol = f"y(t) = ({poly_str([C2, C1], 't') if C2 else C1}){_exp(r1)}"
        steps += [
            f"Repeated root $r = {r1}$ → $y = (C_1 + C_2t){_exp(r1)}$ (critically damped: the fastest return without oscillation).",
            f"$y(0) = C_1 = {y0}$; $y'(0) = C_2 + ({r1})C_1 = {v0}$ → $C_2 = {C2}$.",
        ]
        values = {"C1": C1, "C2": C2, "r": r1}
    else:
        A = y0
        B = Fraction(v0 - al * y0, be)
        bt = "t" if be == 1 else f"{be}t"
        trig = (_signed(A, f"\\cos {bt}", first=True) + _signed(B, f"\\sin {bt}", first=not A)) if B.denominator == 1 \
            else _signed(A, f"\\cos {bt}", first=True) + (" - " if B < 0 else " + ") + f"{_num(abs(B))}\\sin {bt}"
        sol = f"y(t) = {_exp(al)}\\left({trig}\\right)"
        steps += [
            f"Complex roots $r = {al} \\pm {be if be != 1 else ''}i$ → $y = {_exp(al)}(A\\cos {bt} + B\\sin {bt})$ "
            "(underdamped: decaying oscillation).",
            f"$y(0) = A = {y0}$; $y'(0) = ({al})A + ({be})B = {v0}$ → $B = {_num(B)}$.",
        ]
        values = {"A": A, "B": float(B), "alpha": al, "beta": be}
    steps.append(f"Solution: ${sol}$. All terms decay because the real parts of the roots are negative — like a damped "
                 "spring–mass system $m\\ddot x + c\\dot x + kx = 0$.")
    question = f"Solve the initial-value problem ${eq}$, $y(0) = {y0}$, $y'(0) = {v0}$, and classify the damping."
    values.update({"b": b, "c": c, "y0": y0, "v0": v0, "damping": kind})
    label = {"over": "overdamped", "critical": "critically damped", "under": "underdamped"}[kind]
    return {"question": question, "steps": steps, "answer": f"${sol}$ ({label})",
            "values": values}


# ---------------------------------------------------------------------------
# Linear algebra
# ---------------------------------------------------------------------------


@template("eigenvalues_2x2", MATH, "Linear Algebra", "Eigenvalues and eigenvectors", "medium")
def eigenvalues_2x2(rng):
    l1, l2 = rng.sample(range(-4, 7), 2)
    a = rng.randint(-3, 3)
    # A = P diag(l1, l2) P^-1 with P = [[1, 1], [a, a+1]] (det P = 1 keeps A integer)
    A11 = l1 * (a + 1) - l2 * a
    A12 = l2 - l1
    A21 = a * (a + 1) * (l1 - l2)
    A22 = -l1 * a + l2 * (a + 1)
    tr, det = A11 + A22, A11 * A22 - A12 * A21

    def lam_minus(v):
        return "\\lambda" if v == 0 else (f"\\lambda - {v}" if v > 0 else f"\\lambda + {-v}")

    def a_minus(v):
        mag = "" if abs(v) == 1 else str(abs(v))
        return "A" if v == 0 else (f"A - {mag}I" if v > 0 else f"A + {mag}I")

    char_poly = "\\lambda^2" + _signed(-tr, "\\lambda") + (f" + {det}" if det > 0 else f" - {-det}" if det < 0 else "")
    question = (
        f"Find the eigenvalues and eigenvectors of $A = \\begin{{pmatrix}} {A11} & {A12} \\\\ {A21} & {A22} \\end{{pmatrix}}$."
    )
    steps = [
        "Eigenvalues solve $\\det(A - \\lambda I) = 0$, i.e. $\\lambda^2 - (\\operatorname{tr}A)\\lambda + \\det A = 0$.",
        f"$\\operatorname{{tr}}A = {tr}$, $\\det A = ({A11})({A22}) - ({A12})({A21}) = {det}$: ${char_poly} = 0$.",
        f"Factor: $({lam_minus(l1)})({lam_minus(l2)}) = 0$ → $\\lambda_1 = {l1}$, $\\lambda_2 = {l2}$.",
        f"For $\\lambda_1 = {l1}$: $({a_minus(l1)})\\mathbf v = 0$ gives $\\mathbf v_1 = (1, {a})^T$.",
        f"For $\\lambda_2 = {l2}$: $({a_minus(l2)})\\mathbf v = 0$ gives $\\mathbf v_2 = (1, {a + 1})^T$.",
        f"Checks: $\\lambda_1 + \\lambda_2 = {l1 + l2} = \\operatorname{{tr}}A$ and $\\lambda_1\\lambda_2 = {l1 * l2} = \\det A$. ✓",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$\\lambda_1 = {l1}$, $\\mathbf v_1 = (1, {a})^T$; $\\lambda_2 = {l2}$, $\\mathbf v_2 = (1, {a + 1})^T$",
            "values": {"A": [[A11, A12], [A21, A22]], "eigenvalues": [l1, l2], "v1": [1, a], "v2": [1, a + 1]}}


@template("linear_system_cramer", MATH, "Linear Algebra", "Linear systems", "medium")
def linear_system_cramer(rng):
    while True:
        M = [[rng.randint(-4, 5) for _ in range(3)] for _ in range(3)]
        D = det3(M)
        if D != 0 and all(any(r) for r in M):
            break
    sol = [rng.randint(-5, 5) for _ in range(3)]
    rhs = [sum(M[i][j] * sol[j] for j in range(3)) for i in range(3)]
    names = ["x", "y", "z"]
    eqs = []
    for i in range(3):
        s = ""
        for j in range(3):
            s += _signed(M[i][j], names[j], first=(s == ""))
        eqs.append(f"{s or '0'} = {rhs[i]}")
    dets = []
    for j in range(3):
        Mj = [row[:] for row in M]
        for i in range(3):
            Mj[i][j] = rhs[i]
        dets.append(det3(Mj))
    question = "Solve the system using Cramer's rule: $" + "$, $".join(eqs) + "$."
    steps = [
        f"Coefficient determinant: $D = {D}$ (non-zero, so there is a unique solution).",
        f"Replace each column by the right-hand side: $D_x = {dets[0]}$, $D_y = {dets[1]}$, $D_z = {dets[2]}$.",
        f"$x = D_x/D = {sol[0]}$, $y = D_y/D = {sol[1]}$, $z = D_z/D = {sol[2]}$.",
        "Check by substituting into the first equation: "
        f"${M[0][0]}({sol[0]}) + ({M[0][1]})({sol[1]}) + ({M[0][2]})({sol[2]}) = {rhs[0]}$. ✓",
    ]
    return {"question": question, "steps": steps, "answer": f"$x = {sol[0]}$, $y = {sol[1]}$, $z = {sol[2]}$",
            "values": {"matrix": M, "rhs": rhs, "solution": sol, "det": D}}


@template("vector_operations", MATH, "Linear Algebra", "Vectors", "easy")
def vector_operations(rng):
    u = [rng.randint(-5, 5) for _ in range(3)]
    v = [rng.randint(-5, 5) for _ in range(3)]
    if not any(u):
        u[0] = 1
    if not any(v):
        v[1] = 2
    dot = sum(a * b for a, b in zip(u, v))
    nu, nv = math.sqrt(sum(a * a for a in u)), math.sqrt(sum(b * b for b in v))
    cos = dot / (nu * nv)
    ang = math.degrees(math.acos(max(-1.0, min(1.0, cos))))
    cr = [u[1] * v[2] - u[2] * v[1], u[2] * v[0] - u[0] * v[2], u[0] * v[1] - u[1] * v[0]]
    area = math.sqrt(sum(c * c for c in cr))
    question = (
        f"For $\\mathbf u = ({u[0]}, {u[1]}, {u[2]})$ and $\\mathbf v = ({v[0]}, {v[1]}, {v[2]})$, find "
        "$\\mathbf u\\cdot\\mathbf v$, the angle between them, $\\mathbf u\\times\\mathbf v$, and the area of the "
        "parallelogram they span."
    )
    steps = [
        f"Dot product: $({u[0]})({v[0]}) + ({u[1]})({v[1]}) + ({u[2]})({v[2]}) = {dot}$.",
        f"Magnitudes: $|\\mathbf u| = \\sqrt{{{sum(a * a for a in u)}}} = {fmt(nu)}$, $|\\mathbf v| = \\sqrt{{{sum(b * b for b in v)}}} = {fmt(nv)}$.",
        f"$\\cos\\theta = \\frac{{{dot}}}{{({fmt(nu)})({fmt(nv)})}} = {fmt(cos)}$ → $\\theta = {ang:.1f}°$"
        + (" (perpendicular)." if dot == 0 else "."),
        f"Cross product: $\\mathbf u\\times\\mathbf v = ({cr[0]}, {cr[1]}, {cr[2]})$ — perpendicular to both "
        f"(check: $\\mathbf u\\cdot(\\mathbf u\\times\\mathbf v) = {sum(a * c for a, c in zip(u, cr))}$).",
        f"Parallelogram area $= |\\mathbf u\\times\\mathbf v| = \\sqrt{{{sum(c * c for c in cr)}}} = {fmt(area)}$.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$\\mathbf u\\cdot\\mathbf v = {dot}$; $\\theta = {ang:.1f}°$; $\\mathbf u\\times\\mathbf v = ({cr[0]}, {cr[1]}, {cr[2]})$; area ${fmt(area)}$",
            "values": {"u": u, "v": v, "dot": dot, "angle_deg": ang, "cross": cr, "area": area}}


# ---------------------------------------------------------------------------
# Probability
# ---------------------------------------------------------------------------


@template("bayes_diagnostic_test", MATH, "Probability", "Bayes' theorem", "medium")
def bayes_diagnostic_test(rng):
    disease = pick(rng, ["a rare disease", "a genetic condition", "an infection", "a type of cancer",
                         "a metabolic disorder"])
    prev = pick(rng, [0.001, 0.002, 0.005, 0.01, 0.02, 0.05, 0.1, 0.2])
    sens = pick(rng, [0.80, 0.90, 0.95, 0.98, 0.99, 0.999])
    spec = pick(rng, [0.90, 0.95, 0.97, 0.99, 0.995, 0.999])
    N = 100000
    sick = prev * N
    tp = sens * sick
    fp = (1 - spec) * (N - sick)
    tn = spec * (N - sick)
    fn = sick - tp
    ppv = tp / (tp + fp)
    npv = tn / (tn + fn)
    question = (
        f"{disease[0].upper() + disease[1:]} affects {100 * prev:g}% of a population. A test has sensitivity "
        f"{100 * sens:g}% and specificity {100 * spec:g}%. If a randomly chosen person tests positive, "
        "what is the probability that they have the condition? What if they test negative?"
    )
    steps = [
        f"Natural frequencies for {N:,} people: {fmt(sick, 4)} have the condition, {fmt(N - sick, 5)} do not.",
        f"True positives $= {fmt(sens, 4)} \\times {fmt(sick, 4)} = {fmt(tp, 4)}$; false positives $= {fmt(1 - spec, 3)} \\times "
        f"{fmt(N - sick, 5)} = {fmt(fp, 4)}$.",
        f"Bayes' theorem: $P(D\\mid +) = \\frac{{TP}}{{TP + FP}} = \\frac{{{fmt(tp, 4)}}}{{{fmt(tp, 4)} + {fmt(fp, 4)}}} = {fmt(ppv)}$ "
        f"({fmt(100 * ppv)}%).",
        f"Negative predictive value: $P(\\text{{no }}D\\mid -) = \\frac{{TN}}{{TN + FN}} = \\frac{{{fmt(tn, 5)}}}{{{fmt(tn, 5)} + {fmt(fn, 3)}}} = {fmt(npv, 5)}$.",
        "When a condition is rare, even an accurate test produces many false positives relative to true positives — "
        "the base-rate effect.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$P(D\\mid +) = {fmt(ppv)}$; $P(\\text{{healthy}}\\mid -) = {fmt(npv, 5)}$",
            "values": {"prevalence": prev, "sensitivity": sens, "specificity": spec, "ppv": ppv, "npv": npv}}


@template("binomial_distribution", MATH, "Probability", "Binomial distribution", "medium")
def binomial_distribution(rng):
    ctx, verb, p = pick(rng, [
        ("A drug cures {pct}% of patients. Among {n} treated patients", "are cured", None),
        ("Each offspring of an Aa × Aa cross has probability 1/4 of showing the recessive trait. Among {n} offspring",
         "show the trait", 0.25),
        ("A component fails a quality test with probability {p}. In a batch of {n} components", "fail", None),
        ("A seed germinates with probability {p}. If {n} seeds are planted", "germinate", None),
    ])
    if p is None:
        p = pick(rng, [0.05, 0.1, 0.2, 0.3, 0.6, 0.7, 0.8, 0.9])
    n = rng.randint(5, 20)
    k = rng.randint(0, n)
    pk = math.comb(n, k) * p ** k * (1 - p) ** (n - k)
    p_atleast1 = 1 - (1 - p) ** n
    mean, sd = n * p, math.sqrt(n * p * (1 - p))
    question = (
        ctx.format(p=fmt(p, 2), pct=f"{100 * p:g}", n=n) + f", what is the probability that "
        f"{'none of them' if k == 0 else f'exactly {k}'} {verb}, and "
        f"that at least one does? Give the mean and standard deviation of the number that {verb}."
    )
    steps = [
        f"$X \\sim \\text{{Binomial}}(n = {n}, p = {fmt(p, 2)})$: independent trials with constant success probability.",
        f"$P(X = {k}) = \\binom{{{n}}}{{{k}}}p^{{{k}}}(1-p)^{{{n - k}}} = {math.comb(n, k)} \\times {fmt(p, 2)}^{{{k}}} \\times "
        f"{fmt(1 - p, 2)}^{{{n - k}}} = {fmt(pk)}$.",
        f"$P(X \\ge 1) = 1 - P(X = 0) = 1 - {fmt(1 - p, 2)}^{{{n}}} = {fmt(p_atleast1, 4)}$.",
        f"Mean $np = {fmt(mean)}$; standard deviation $\\sqrt{{np(1-p)}} = {fmt(sd)}$.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$P(X = {k}) = {fmt(pk)}$; $P(X \\ge 1) = {fmt(p_atleast1, 4)}$; mean ${fmt(mean)}$, sd ${fmt(sd)}$",
            "values": {"n": n, "p": p, "k": k, "p_k": pk, "p_at_least_1": p_atleast1, "mean": mean, "sd": sd}}


@template("poisson_distribution", MATH, "Probability", "Poisson distribution", "medium")
def poisson_distribution(rng):
    ctx = pick(rng, [
        "A Geiger counter near a weak source records an average of {lam} counts per second.",
        "A genome accumulates on average {lam} new mutations per generation in a given region.",
        "On average {lam} cars pass a checkpoint per minute.",
        "A faint star delivers on average {lam} photons per millisecond to a detector.",
        "A hospital ward admits on average {lam} emergency patients per night.",
    ])
    lam = pick(rng, [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 4.0, 5.0, 6.5, 8.0])
    k = rng.randint(0, int(lam + 3))
    pk = math.exp(-lam) * lam ** k / math.factorial(k)
    cdf = sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(k + 1))
    question = (
        ctx.format(lam=fmt(lam, 2)) + f" Assuming a Poisson process, what is the probability of exactly {k} "
        f"event{'' if k == 1 else 's'} in one "
        f"interval, and of at most {k}?"
    )
    steps = [
        f"$P(X = k) = \\frac{{e^{{-\\lambda}}\\lambda^k}}{{k!}}$ with $\\lambda = {fmt(lam, 2)}$ (mean = variance = λ).",
        f"$P(X = {k}) = \\frac{{e^{{-{fmt(lam, 2)}}}({fmt(lam, 2)})^{{{k}}}}}{{{k}!}} = {fmt(pk)}$.",
        f"$P(X \\le {k}) = \\sum_{{i=0}}^{{{k}}} P(X = i) = {fmt(cdf)}$.",
        f"Standard deviation $\\sqrt{{\\lambda}} = {fmt(math.sqrt(lam))}$ — counting statistics have relative uncertainty $1/\\sqrt{{\\lambda}}$.",
    ]
    return {"question": question, "steps": steps, "answer": f"$P(X = {k}) = {fmt(pk)}$; $P(X \\le {k}) = {fmt(cdf)}$",
            "values": {"lambda": lam, "k": k, "p_k": pk, "cdf": cdf}}


@template("normal_distribution", MATH, "Statistics", "Normal distribution", "medium")
def normal_distribution(rng):
    name, mu, sd, unit = pick(rng, [
        ("adult heights in a population", 170.0, 8.0, "cm"), ("IQ scores", 100.0, 15.0, "points"),
        ("systolic blood pressure", 120.0, 12.0, "mmHg"), ("the mass of manufactured 500 g packages", 500.0, 4.0, "g"),
        ("repeated measurements of g", 9.81, 0.05, "m/s²"), ("birth weights", 3.4, 0.5, "kg"),
    ])
    za, zb = sorted(rng.sample([-2.5, -2.0, -1.5, -1.2, -1.0, -0.5, 0.0, 0.5, 0.8, 1.0, 1.5, 2.0, 2.5], 2))
    a, b = round(mu + za * sd, 3), round(mu + zb * sd, 3)
    pa = phi(za)
    pab = phi(zb) - phi(za)
    question = (
        f"Assume {name} are normally distributed with mean {fmt(mu, 4)} {unit} and standard deviation {fmt(sd, 3)} {unit}. "
        f"What fraction lies below {fmt(a, 4)} {unit}, and what fraction lies between {fmt(a, 4)} and {fmt(b, 4)} {unit}?"
    )
    steps = [
        "Standardize: $z = (x - \\mu)/\\sigma$.",
        f"$z_1 = ({fmt(a, 4)} - {fmt(mu, 4)})/{fmt(sd, 3)} = {za}$; $z_2 = ({fmt(b, 4)} - {fmt(mu, 4)})/{fmt(sd, 3)} = {zb}$.",
        f"$P(X < {fmt(a, 4)}) = \\Phi({za}) = {pa:.4f}$.",
        f"$P({fmt(a, 4)} < X < {fmt(b, 4)}) = \\Phi({zb}) - \\Phi({za}) = {phi(zb):.4f} - {pa:.4f} = {pab:.4f}$.",
        "Rule of thumb: about 68%, 95% and 99.7% of values lie within 1, 2 and 3 standard deviations of the mean.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"below: {100 * pa:.2f}%; between: {100 * pab:.2f}%",
            "values": {"mu": mu, "sd": sd, "a": a, "b": b, "p_below_a": pa, "p_between": pab}}


@template("counting_combinatorics", MATH, "Probability", "Counting", "easy")
def counting_combinatorics(rng):
    kind = pick(rng, ["committee", "arrangement", "sequence", "birthday"])
    if kind == "committee":
        n, k = rng.randint(6, 20), rng.randint(2, 5)
        ans = math.comb(n, k)
        question = f"In how many ways can a {k}-person committee be chosen from {n} researchers?"
        steps = ["Order does not matter, so count combinations: $\\binom{n}{k} = \\frac{n!}{k!(n-k)!}$.",
                 f"$\\binom{{{n}}}{{{k}}} = \\frac{{{n}!}}{{{k}!\\,{n - k}!}} = {ans}$."]
        answer = f"${ans}$"
    elif kind == "arrangement":
        n, k = rng.randint(5, 12), rng.randint(2, 4)
        ans = math.perm(n, k)
        question = (f"{n} samples are available but only {k} slots in an instrument's ordered queue. How many different "
                    "ordered queues are possible?")
        steps = ["Order matters, so count permutations: $P(n, k) = \\frac{n!}{(n-k)!}$.",
                 f"$P({n}, {k}) = " + " \\times ".join(str(n - i) for i in range(k)) + f" = {ans}$."]
        answer = f"${ans}$"
    elif kind == "sequence":
        L = rng.randint(3, 12)
        alphabet, size, what = pick(rng, [("DNA", 4, "nucleotides"), ("peptide", 20, "amino acids"),
                                          ("RNA", 4, "nucleotides")])
        ans = size ** L
        question = (f"How many different {alphabet} sequences of length {L} can be built from the {size} standard {what}? "
                    f"How many {alphabet} sequences of length {L} contain no repeats of the same residue next to each other?")
        no_rep = size * (size - 1) ** (L - 1)
        steps = [f"Each of the {L} positions can independently be any of {size} residues: ${size}^{{{L}}} = {fmt(ans)}$.",
                 f"Without identical neighbors: {size} choices for the first position, then {size - 1} for each later one: "
                 f"${size} \\times {size - 1}^{{{L - 1}}} = {fmt(no_rep)}$."]
        answer = f"${fmt(ans)}$ sequences; ${fmt(no_rep)}$ without adjacent repeats"
        ans = float(ans)
    else:
        n = rng.randint(10, 60)
        p_no = 1.0
        for i in range(n):
            p_no *= (365 - i) / 365
        ans = 1 - p_no
        question = (f"In a group of {n} people, what is the probability that at least two share a birthday? "
                    "(Ignore leap years and assume all 365 birthdays are equally likely.)")
        steps = ["Compute the complement — all birthdays different: $P = \\frac{365}{365}\\cdot\\frac{364}{365}\\cdots"
                 f"\\frac{{{365 - n + 1}}}{{365}}$.",
                 f"$P(\\text{{all different}}) = {fmt(p_no)}$.",
                 f"$P(\\text{{at least one shared}}) = 1 - {fmt(p_no)} = {fmt(ans)}$. (It already exceeds 50% for 23 people "
                 "because the number of pairs grows like $n^2/2$.)"]
        answer = f"$P \\approx {fmt(ans)}$"
    return {"question": question, "steps": steps, "answer": answer, "values": {"kind": kind, "result": ans}}


# ---------------------------------------------------------------------------
# Statistics and data analysis
# ---------------------------------------------------------------------------

T_CRIT_95 = {4: 2.776, 5: 2.571, 6: 2.447, 7: 2.365, 8: 2.306, 9: 2.262, 10: 2.228, 11: 2.201}


@template("descriptive_statistics", MATH, "Statistics", "Descriptive statistics and confidence intervals", "easy")
def descriptive_statistics(rng):
    name, mu, sd, unit, dec = pick(rng, [
        ("the boiling point of a liquid", 78.4, 0.3, "°C", 1), ("the period of a pendulum", 2.01, 0.02, "s", 2),
        ("the mass of a reaction product", 4.85, 0.12, "g", 2), ("a titration volume", 24.6, 0.15, "mL", 2),
        ("plant height after four weeks", 32.0, 4.0, "cm", 1), ("resting heart rate", 68.0, 6.0, "bpm", 0),
    ])
    n = rng.randint(5, 12)
    data = [round(rng.gauss(mu, sd), dec) for _ in range(n)]
    if dec == 0:
        data = [int(x) for x in data]
    mean = sum(data) / n
    s = sorted(data)
    median = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
    var = sum((x - mean) ** 2 for x in data) / (n - 1)
    sdev = math.sqrt(var)
    se = sdev / math.sqrt(n)
    t = T_CRIT_95[n - 1]
    question = (
        f"Repeated measurements of {name} gave ({unit}): " + ", ".join(str(x) for x in data)
        + ". Compute the mean, median, sample standard deviation, standard error of the mean, and a 95% confidence "
        "interval for the true mean."
    )
    steps = [
        f"Mean: $\\bar x = \\frac{{\\sum x_i}}{{n}} = \\frac{{{fmt(sum(data), 5)}}}{{{n}}} = {fmt(mean, 4)}$ {unit}.",
        f"Median (middle of the sorted data {', '.join(str(x) for x in s)}): {fmt(median, 4)} {unit}.",
        f"Sample standard deviation: $s = \\sqrt{{\\frac{{\\sum (x_i - \\bar x)^2}}{{n - 1}}}} = {fmt(sdev)}$ {unit} "
        "(dividing by $n - 1$ corrects the bias from using $\\bar x$).",
        f"Standard error: $s/\\sqrt n = {fmt(sdev)}/\\sqrt{{{n}}} = {fmt(se)}$ {unit}.",
        f"95% CI with Student's t ($df = {n - 1}$, $t = {t}$): ${fmt(mean, 4)} \\pm {t} \\times {fmt(se)} = "
        f"[{fmt(mean - t * se, 4)}, {fmt(mean + t * se, 4)}]$ {unit}.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"mean {fmt(mean, 4)}, median {fmt(median, 4)}, s = {fmt(sdev)}, SE = {fmt(se)}; 95% CI "
                      f"[{fmt(mean - t * se, 4)}, {fmt(mean + t * se, 4)}] {unit}",
            "values": {"data": data, "mean": mean, "median": median, "sd": sdev, "se": se, "t_crit": t}}


@template("linear_regression", MATH, "Statistics", "Least-squares regression", "hard")
def linear_regression(rng):
    ctx = pick(rng, [
        ("A spring is stretched by x (cm) and the restoring force F (N) is measured", "x", "F",
         "spring constant (N/cm)", [1, 2, 3, 4, 5, 6], rng.uniform(1.5, 8.0), 0.0),
        ("A Beer–Lambert calibration gives absorbance A at concentrations c (mM)", "c", "A",
         "slope (absorbance per mM)", [0.1, 0.2, 0.3, 0.4, 0.5], rng.uniform(0.8, 2.5), 0.01),
        ("The voltage V (V) across a resistor is measured at currents I (A)", "I", "V", "resistance (Ω)",
         [0.1, 0.2, 0.3, 0.4, 0.5, 0.6], rng.uniform(5, 50), 0.0),
        ("A heated sample's temperature T (°C) is recorded at times t (min)", "t", "T", "heating rate (°C/min)",
         [0, 2, 4, 6, 8, 10], rng.uniform(0.5, 3.0), 20.0),
    ])
    label, xl, yl, slope_name, xs, m_true, b_true = ctx
    n = len(xs)
    noise = 0.03 * m_true * max(xs)
    ys = [round(m_true * x + b_true + rng.gauss(0, noise), 3 if m_true * max(xs) < 10 else 2) for x in xs]
    xm, ym = sum(xs) / n, sum(ys) / n
    Sxx = sum((x - xm) ** 2 for x in xs)
    Syy = sum((y - ym) ** 2 for y in ys)
    Sxy = sum((x - xm) * (y - ym) for x, y in zip(xs, ys))
    m = Sxy / Sxx
    b = ym - m * xm
    r = Sxy / math.sqrt(Sxx * Syy)
    pairs = "; ".join(f"({x}, {y})" for x, y in zip(xs, ys))
    question = (
        f"{label}: ({xl}, {yl}) = {pairs}. Fit a least-squares straight line, report the {slope_name} and the "
        "intercept, and give the correlation coefficient $r$."
    )
    steps = [
        f"Means: $\\bar x = {fmt(xm, 4)}$, $\\bar y = {fmt(ym, 4)}$.",
        f"$S_{{xx}} = \\sum(x - \\bar x)^2 = {fmt(Sxx, 4)}$; $S_{{xy}} = \\sum(x - \\bar x)(y - \\bar y) = {fmt(Sxy, 4)}$; "
        f"$S_{{yy}} = {fmt(Syy, 4)}$.",
        f"Slope $m = S_{{xy}}/S_{{xx}} = {fmt(m, 4)}$; intercept $b = \\bar y - m\\bar x = {fmt(b, 3)}$.",
        f"$r = \\frac{{S_{{xy}}}}{{\\sqrt{{S_{{xx}}S_{{yy}}}}}} = {r:.4f}$ — "
        + ("a very strong linear relationship." if abs(r) > 0.99 else "a strong linear relationship." if abs(r) > 0.95
           else "a moderate linear relationship."),
        f"Best-fit line: $y = {fmt(m, 4)}x {'+' if b >= 0 else '-'} {fmt(abs(b), 3)}$.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"slope ${fmt(m, 4)}$, intercept ${fmt(b, 3)}$, $r = {r:.4f}$",
            "values": {"x": xs, "y": ys, "slope": m, "intercept": b, "r": r}}


@template("error_propagation", MATH, "Statistics", "Uncertainty propagation", "medium")
def error_propagation(rng):
    case = pick(rng, ["density", "pendulum_g", "kinetic_energy"])
    if case == "density":
        m, dm = nice(rng, 10.0, 200.0, 0.1), pick(rng, [0.1, 0.2, 0.5])
        V, dV = nice(rng, 5.0, 80.0, 0.5), pick(rng, [0.1, 0.2, 0.5])
        val = m / V
        rel = math.sqrt((dm / m) ** 2 + (dV / V) ** 2)
        question = (f"A sample has mass $m = {fmt(m, 4)} \\pm {dm}$ g and volume $V = {fmt(V, 3)} \\pm {dV}$ cm³. Find its "
                    "density and the uncertainty, assuming independent random errors.")
        steps = [f"$\\rho = m/V = {fmt(m, 4)}/{fmt(V, 3)} = {fmt(val, 4)}$ g/cm³.",
                 "For products and quotients, relative uncertainties add in quadrature: "
                 "$\\frac{\\delta\\rho}{\\rho} = \\sqrt{\\left(\\frac{\\delta m}{m}\\right)^2 + \\left(\\frac{\\delta V}{V}\\right)^2}$.",
                 f"$= \\sqrt{{({fmt(dm / m)})^2 + ({fmt(dV / V)})^2}} = {fmt(rel)}$."]
        unit = "g/cm³"
    elif case == "pendulum_g":
        L, dL = nice(rng, 0.300, 2.000, 0.005), pick(rng, [0.001, 0.002, 0.005])
        T_true = 2 * math.pi * math.sqrt(L / 9.81)
        T, dT = round(T_true * rng.uniform(0.995, 1.005), 3), pick(rng, [0.002, 0.005, 0.01])
        val = 4 * math.pi ** 2 * L / T ** 2
        rel = math.sqrt((dL / L) ** 2 + (2 * dT / T) ** 2)
        question = (f"A pendulum of length $L = {fmt(L, 4)} \\pm {dL}$ m has a measured period $T = {T:.3f} \\pm {dT}$ s. "
                    "Calculate $g = 4\\pi^2L/T^2$ and its uncertainty.")
        steps = [f"$g = 4\\pi^2({fmt(L, 4)})/({T:.3f})^2 = {fmt(val, 4)}$ m/s².",
                 "Powers multiply relative uncertainties: $\\frac{\\delta g}{g} = \\sqrt{\\left(\\frac{\\delta L}{L}\\right)^2 + "
                 "\\left(2\\frac{\\delta T}{T}\\right)^2}$.",
                 f"$= \\sqrt{{({fmt(dL / L)})^2 + (2 \\times {fmt(dT / T)})^2}} = {fmt(rel)}$ — the period term dominates "
                 "because it is squared." if 2 * dT / T > dL / L else
                 f"$= \\sqrt{{({fmt(dL / L)})^2 + (2 \\times {fmt(dT / T)})^2}} = {fmt(rel)}$."]
        unit = "m/s²"
    else:
        m, dm = nice(rng, 0.100, 5.000, 0.005), pick(rng, [0.001, 0.005, 0.01])
        v, dv = nice(rng, 1.0, 30.0, 0.1), pick(rng, [0.05, 0.1, 0.2])
        val = 0.5 * m * v ** 2
        rel = math.sqrt((dm / m) ** 2 + (2 * dv / v) ** 2)
        question = (f"A cart of mass $m = {fmt(m, 4)} \\pm {dm}$ kg moves at $v = {fmt(v, 3)} \\pm {dv}$ m/s. Find its kinetic "
                    "energy and the uncertainty.")
        steps = [f"$K = \\tfrac12mv^2 = \\tfrac12({fmt(m, 4)})({fmt(v, 3)})^2 = {fmt(val, 4)}$ J.",
                 "$\\frac{\\delta K}{K} = \\sqrt{\\left(\\frac{\\delta m}{m}\\right)^2 + \\left(2\\frac{\\delta v}{v}\\right)^2}$.",
                 f"$= \\sqrt{{({fmt(dm / m)})^2 + (2 \\times {fmt(dv / v)})^2}} = {fmt(rel)}$."]
        unit = "J"
    abs_unc = rel * val
    unc_r = float(f"{abs_unc:.1g}")
    decimals = max(0, -int(math.floor(math.log10(unc_r))))
    steps.append(f"Absolute uncertainty: ${fmt(rel)} \\times {fmt(val, 4)} = {fmt(abs_unc, 2)}$ {unit}; round it to one "
                 f"significant figure and the value to match: ${val:.{decimals}f} \\pm {unc_r:.{decimals}f}$ {unit}.")
    return {"question": question, "steps": steps, "answer": f"${val:.{decimals}f} \\pm {unc_r:.{decimals}f}$ {unit}",
            "values": {"case": case, "value": val, "rel_uncertainty": rel, "abs_uncertainty": abs_unc}}


# ---------------------------------------------------------------------------
# Numerical methods and units
# ---------------------------------------------------------------------------


@template("newtons_method", MATH, "Numerical Methods", "Root finding", "medium")
def newtons_method(rng):
    case = pick(rng, ["sqrt", "cbrt", "cos"])
    if case == "sqrt":
        a = pick(rng, [2, 3, 5, 6, 7, 10, 11, 13, 17, 19, 20])
        f_tex, df_tex = f"x^2 - {a}", "2x"
        f, df = (lambda x: x * x - a), (lambda x: 2 * x)
        x0 = float(round(math.sqrt(a)))
        exact = math.sqrt(a)
        goal = f"$\\sqrt{{{a}}}$"
    elif case == "cbrt":
        a = pick(rng, [2, 3, 5, 7, 10, 20, 30, 50, 100])
        f_tex, df_tex = f"x^3 - {a}", "3x^2"
        f, df = (lambda x: x ** 3 - a), (lambda x: 3 * x * x)
        x0 = float(round(a ** (1 / 3)))
        exact = a ** (1 / 3)
        goal = f"$\\sqrt[3]{{{a}}}$"
    else:
        f_tex, df_tex = "x - \\cos x", "1 + \\sin x"
        f, df = (lambda x: x - math.cos(x)), (lambda x: 1 + math.sin(x))
        x0 = pick(rng, [0.5, 1.0, 0.0])
        exact = 0.7390851332151607
        goal = "the solution of $x = \\cos x$"
    xs = [x0]
    for _ in range(4):
        x = xs[-1]
        xs.append(x - f(x) / df(x))
    question = (
        f"Use Newton's method on $f(x) = {f_tex}$, starting from $x_0 = {fmt(x0, 2) if x0 else 0}$, to approximate {goal}. "
        "Perform four iterations."
    )
    steps = [f"Newton's iteration: $x_{{n+1}} = x_n - \\frac{{f(x_n)}}{{f'(x_n)}}$ with $f'(x) = {df_tex}$."]
    for i in range(1, 5):
        steps.append(f"$x_{i} = {xs[i]:.10f}$")
    err = abs(xs[4] - exact)
    err_txt = "below $10^{-12}$ (the limit of double-precision arithmetic)" if err < 1e-12 else f"${fmt(err, 2)}$"
    steps.append(f"True value: ${exact:.10f}$; error after four steps: {err_txt}. "
                 "Newton's method converges quadratically: the number of correct digits roughly doubles each step.")
    return {"question": question, "steps": steps, "answer": f"$x_4 = {xs[4]:.10f}$",
            "values": {"case": case, "x0": x0, "iterates": xs, "exact": exact}}


INTEGRANDS = [
    ("\\sin x", math.sin, lambda b: 1 - math.cos(b), 0.0, [1.0, 1.5, 2.0, math.pi]),
    ("e^x", math.exp, lambda b: math.exp(b) - 1, 0.0, [0.5, 1.0, 1.5, 2.0]),
    ("\\frac{1}{x}", lambda x: 1 / x, math.log, 1.0, [2.0, 3.0, 4.0, 5.0]),
    ("x^3", lambda x: x ** 3, lambda b: b ** 4 / 4, 0.0, [1.0, 2.0, 3.0]),
    ("\\sqrt{x}", math.sqrt, lambda b: 2 / 3 * b ** 1.5, 0.0, [1.0, 4.0, 9.0]),
]


@template("numerical_integration", MATH, "Numerical Methods", "Numerical integration", "medium")
def numerical_integration(rng):
    f_tex, f, F, a, bs = pick(rng, INTEGRANDS)
    b = pick(rng, bs)
    n = pick(rng, [4, 6, 8])
    h = (b - a) / n
    ys = [f(a + i * h) for i in range(n + 1)]
    trap = h * (ys[0] / 2 + sum(ys[1:-1]) + ys[-1] / 2)
    simp = h / 3 * (ys[0] + ys[-1] + 4 * sum(ys[1:-1:2]) + 2 * sum(ys[2:-1:2]))
    exact = F(b) - F(a)
    b_tex = "\\pi" if b == math.pi else fmt(b, 3)
    question = (
        f"Approximate $\\int_{{{fmt(a, 2) if a else 0}}}^{{{b_tex}}} {f_tex}\\,dx$ with the trapezoidal rule and Simpson's rule "
        f"using $n = {n}$ subintervals, and compare with the exact value."
    )
    steps = [
        f"$h = (b - a)/n = {fmt(h, 4)}$; sample values $f(x_i)$: " + ", ".join(f"{y:.4f}" for y in ys) + ".",
        f"Trapezoidal: $T = h\\left[\\tfrac12f_0 + f_1 + \\dots + f_{{n-1}} + \\tfrac12f_n\\right] = {trap:.6f}$.",
        f"Simpson: $S = \\frac{{h}}{{3}}\\left[f_0 + 4(f_1 + f_3 + \\dots) + 2(f_2 + f_4 + \\dots) + f_n\\right] = {simp:.6f}$.",
        f"Exact: ${exact:.6f}$. Errors: trapezoid ${fmt(abs(trap - exact), 2)}$, Simpson "
        f"${fmt(abs(simp - exact), 2) if abs(simp - exact) > 1e-12 else 0}$"
        + (" (Simpson's rule is exact for cubics)." if f_tex == "x^3" else
           " — Simpson's error falls as $h^4$ versus $h^2$ for the trapezoid rule."),
    ]
    return {"question": question, "steps": steps,
            "answer": f"$T = {trap:.6f}$, $S = {simp:.6f}$, exact ${exact:.6f}$",
            "values": {"a": a, "b": b, "n": n, "trapezoid": trap, "simpson": simp, "exact": exact}}


CONVERSIONS = [  # quantity, from unit, to unit, factor, value range, chain explanation
    ("speed", "mph", "m/s", 0.44704, (5, 120), "1 mi = 1609.344 m and 1 h = 3600 s"),
    ("speed", "km/h", "m/s", 1 / 3.6, (10, 300), "1 km = 1000 m and 1 h = 3600 s"),
    ("pressure", "psi", "kPa", 6.894757, (5, 3000), "1 psi = 6.894757 kPa"),
    ("pressure", "mmHg", "kPa", 0.1333224, (50, 800), "760 mmHg = 101.325 kPa"),
    ("energy", "kWh", "J", 3.6e6, (0.1, 500), "1 kWh = 1000 W × 3600 s"),
    ("energy", "kcal (food Calories)", "kJ", 4.184, (50, 3000), "1 kcal = 4.184 kJ"),
    ("energy", "eV", "J", 1.602177e-19, (0.5, 1e6), "1 eV = 1.602×10⁻¹⁹ J"),
    ("density", "g/cm³", "kg/m³", 1000.0, (0.5, 22), "1 g = 10⁻³ kg and 1 cm³ = 10⁻⁶ m³"),
    ("volume", "US gallons", "L", 3.785412, (1, 500), "1 US gallon = 3.785412 L"),
    ("length", "light-years", "km", 9.4607e12, (1, 1000), "1 ly = (2.998×10⁵ km/s)(3.156×10⁷ s)"),
    ("length", "inches", "cm", 2.54, (1, 500), "1 in = 2.54 cm exactly"),
    ("power", "horsepower", "kW", 0.745700, (1, 1000), "1 hp = 745.7 W"),
]


@template("unit_conversion", MATH, "Measurement", "Unit conversion", "easy")
def unit_conversion(rng):
    if rng.random() < 0.2:
        F = nice(rng, -40, 450, 1)
        Cc = (F - 32) * 5 / 9
        question = f"Convert {F} °F to degrees Celsius and to kelvin."
        steps = ["Temperature scales are offset as well as scaled: $T_C = (T_F - 32) \\times 5/9$.",
                 f"$T_C = ({F} - 32) \\times 5/9 = {Cc:.2f}$ °C.",
                 f"$T_K = T_C + 273.15 = {Cc + 273.15:.2f}$ K."]
        return {"question": question, "steps": steps, "answer": f"{Cc:.2f} °C = {Cc + 273.15:.2f} K",
                "values": {"F": F, "C": Cc, "K": Cc + 273.15}}
    qty, u1, u2, fac, (lo, hi), why = pick(rng, CONVERSIONS)
    x = sig(10 ** rng.uniform(math.log10(lo), math.log10(hi)), 3)
    y = x * fac
    question = f"Convert {q(x)} {u1} to {u2}."
    steps = [
        f"Conversion factor: {why}, so 1 {u1} $= {fmt(fac, 7)}$ {u2}.",
        f"Multiply by the factor written as a ratio equal to 1: ${fmt(x)}\\text{{ {u1.split(' ')[0]}}} \\times "
        f"\\frac{{{fmt(fac, 7)}\\text{{ {u2}}}}}{{1\\text{{ {u1.split(' ')[0]}}}}} = {fmt(y)}$ {u2}.",
        "Check the units cancel and the size of the answer makes sense.",
    ]
    return {"question": question, "steps": steps, "answer": f"{q(y)} {u2}",
            "values": {"x": x, "factor": fac, "y": y}}
