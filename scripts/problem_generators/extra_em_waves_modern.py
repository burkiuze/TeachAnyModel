"""Extra physics templates: circuits and fields, waves and optics, and modern physics.

Electromagnetism: capacitor networks, two-loop Kirchhoff circuits, Wheatstone and meter bridges, RL transients,
series RLC circuits, power-factor correction, the Hall effect, mass spectrometry and radiation pressure.
Waves and optics: Malus's law, Brewster's angle, thin films, single-slit diffraction, the Rayleigh criterion,
air columns and beats.
Modern physics: Compton scattering, hydrogen-like ions, relativistic velocity addition and Doppler shift,
muon time dilation, nuclear reaction Q-values, activity of a radioisotope sample and fission energy.
"""

import math

from .common import C, E_CHARGE, EPS0, EV, H, M_E, N_A, fmt, nice, pick, q, sig, template

PHYS = "Physics"
U_KG = 1.66054e-27                    # atomic mass unit, kg
U_MEV = 931.494                       # energy equivalent of 1 u, MeV
MEV_J = 1.0e6 * EV                    # 1 MeV in joules
YEAR_S = 3.15576e7                    # Julian year, s
HC_KEV_PM = H * C / EV / 1e3 / 1e-12  # hc in keV·pm (about 1240)
ME_C2_KEV = M_E * C ** 2 / EV / 1e3   # electron rest energy, keV (about 511)
LAMBDA_C = H / (M_E * C)              # Compton wavelength of the electron, m
SOLAR_CONSTANT = 1361.0               # solar irradiance at 1 AU, W/m^2
TAU_MUON = 2.197e-6                   # muon mean lifetime at rest, s
MUON_MC2_MEV = 105.66                 # muon rest energy, MeV
A0_NM = 0.0529                        # Bohr radius, nm


# ---------------------------------------------------------------------------
# Small helpers
# ---------------------------------------------------------------------------


def _deg(x, s=3):
    """Angle in degrees as LaTeX (no $)."""
    return f"{fmt(x, s)}^\\circ"


def _and(items):
    items = list(items)
    return items[0] if len(items) == 1 else ", ".join(items[:-1]) + " and " + items[-1]


def _fixed(x, decimals):
    """fmt() with a fixed number of decimal places (for 1 <= |x| < 100000)."""
    return fmt(x, int(math.floor(math.log10(abs(x)))) + 1 + decimals)


def _exact(x):
    """fmt() with just enough significant figures to reproduce a short decimal literal exactly."""
    digits = f"{abs(x):.10g}".split("e")[0].replace(".", "").lstrip("0")
    return fmt(x, max(len(digits), 1))


def _cos2(angle_deg):
    """cos^2 of an angle in degrees; exactly 0 for odd multiples of 90 degrees."""
    if angle_deg % 180 == 90:
        return 0.0
    return math.cos(math.radians(angle_deg)) ** 2


def _region(lam_nm):
    """Name of the spectral region / visible color of a vacuum wavelength in nm."""
    if lam_nm < 10:
        return "soft X-ray"
    if lam_nm < 121:
        return "extreme ultraviolet"
    if lam_nm < 380:
        return "ultraviolet"
    for limit, name in ((450, "violet"), (495, "blue"), (570, "green"), (590, "yellow"), (620, "orange")):
        if lam_nm < limit:
            return name
    return "red" if lam_nm <= 750 else "infrared"


def _energy(U):
    """Display an energy in J (mJ when below 1 J), as LaTeX number plus unit outside math."""
    return f"{fmt(U * 1000)}$ mJ" if U < 1 else f"{fmt(U)}$ J"


def _voltage(v_uV):
    """Display a voltage given in microvolts (3 significant figures) in a convenient unit."""
    if v_uV >= 1e6:
        return q(v_uV / 1e6, "V")
    if v_uV >= 1e3:
        return q(v_uV / 1e3, "mV")
    return q(v_uV, "μV")


# ---------------------------------------------------------------------------
# Electromagnetism: DC circuits
# ---------------------------------------------------------------------------


@template("capacitor_network_charge_energy", PHYS, "Electromagnetism", "Capacitor networks", "medium")
def capacitor_network_charge_energy(rng):
    C1, C2, C3 = nice(rng, 1, 60, 1), nice(rng, 1, 60, 1), nice(rng, 1, 60, 1)
    V = nice(rng, 6, 240, 3)
    config = pick(rng, ["series_with_parallel_pair", "series_pair_parallel_with_C3"])
    if config == "series_with_parallel_pair":
        C23 = C2 + C3
        Ceq = C1 * C23 / (C1 + C23)
        Q = Ceq * V
        Q1, V1 = Q, Q / C1
        V2 = V3 = Q / C23
        Q2, Q3 = C2 * V2, C3 * V3
        layout = (f"Capacitor $C_1 = {C1}$ μF is connected in series with the parallel combination of $C_2 = {C2}$ μF "
                  f"and $C_3 = {C3}$ μF")
        steps = [
            f"$C_2$ and $C_3$ are in parallel (same voltage), so their capacitances add: "
            f"$C_{{23}} = C_2 + C_3 = {C2} + {C3} = {C23}$ μF.",
            f"$C_1$ is in series with $C_{{23}}$ (same charge), so $\\frac{{1}}{{C_{{eq}}}} = \\frac{{1}}{{C_1}} + \\frac{{1}}{{C_{{23}}}}$: "
            f"$C_{{eq}} = \\frac{{C_1C_{{23}}}}{{C_1 + C_{{23}}}} = \\frac{{({C1})({C23})}}{{{C1 + C23}}} = {fmt(Ceq)}$ μF.",
            f"Charge delivered by the battery: $Q = C_{{eq}}V = ({fmt(Ceq)})({V}) = {fmt(Q)}$ μC. Series elements carry the same "
            f"charge, so $Q_1 = {fmt(Q1)}$ μC, and the parallel pair holds ${fmt(Q)}$ μC in total.",
            f"Voltages: $V_1 = Q_1/C_1 = {fmt(Q1)}/{C1} = {fmt(V1)}$ V and $V_2 = V_3 = Q/C_{{23}} = {fmt(Q)}/{C23} = {fmt(V2)}$ V. "
            f"Check: $V_1 + V_2 = {fmt(V1 + V2)}$ V $= V$ ✓.",
            f"Charges on the parallel pair: $Q_2 = C_2V_2 = ({C2})({fmt(V2)}) = {fmt(Q2)}$ μC and "
            f"$Q_3 = C_3V_3 = ({C3})({fmt(V3)}) = {fmt(Q3)}$ μC; $Q_2 + Q_3 = {fmt(Q2 + Q3)}$ μC $= Q$ ✓.",
        ]
    else:
        C12 = C1 * C2 / (C1 + C2)
        Ceq = C12 + C3
        Q1 = Q2 = C12 * V
        V1, V2 = Q1 / C1, Q2 / C2
        V3, Q3 = V, C3 * V
        Q = Q1 + Q3
        layout = (f"Capacitors $C_1 = {C1}$ μF and $C_2 = {C2}$ μF are connected in series, and this pair is connected in "
                  f"parallel with $C_3 = {C3}$ μF")
        steps = [
            f"$C_1$ and $C_2$ are in series (same charge): "
            f"$C_{{12}} = \\frac{{C_1C_2}}{{C_1 + C_2}} = \\frac{{({C1})({C2})}}{{{C1 + C2}}} = {fmt(C12)}$ μF.",
            f"$C_{{12}}$ is in parallel with $C_3$ (same voltage): $C_{{eq}} = C_{{12}} + C_3 = {fmt(C12)} + {C3} = {fmt(Ceq)}$ μF.",
            f"Each branch has the full battery voltage across it. Branch with $C_3$: $V_3 = {V}$ V and "
            f"$Q_3 = C_3V = ({C3})({V}) = {fmt(Q3)}$ μC.",
            f"Series branch: $Q_1 = Q_2 = C_{{12}}V = ({fmt(C12)})({V}) = {fmt(Q1)}$ μC, so $V_1 = Q_1/C_1 = {fmt(V1)}$ V and "
            f"$V_2 = Q_2/C_2 = {fmt(V2)}$ V. Check: $V_1 + V_2 = {fmt(V1 + V2)}$ V $= V$ ✓.",
            f"Total charge from the battery: $Q = Q_1 + Q_3 = {fmt(Q)}$ μC, which equals $C_{{eq}}V = ({fmt(Ceq)})({V})$ μC ✓.",
        ]
    U1, U2, U3 = (0.5 * Qi * Vi / 1000 for Qi, Vi in ((Q1, V1), (Q2, V2), (Q3, V3)))
    U = 0.5 * Ceq * 1e-6 * V ** 2 * 1000  # mJ
    steps += [
        f"Stored energies from $U = \\tfrac12QV$ (μC × V = μJ): $U_1 = {fmt(U1)}$ mJ, $U_2 = {fmt(U2)}$ mJ, $U_3 = {fmt(U3)}$ mJ.",
        f"Total: $U = \\tfrac12C_{{eq}}V^2 = \\tfrac12({fmt(Ceq)}\\times10^{{-6}}\\text{{ F}})({V}\\text{{ V}})^2 = {fmt(U / 1000)}$ J "
        f"$= {fmt(U)}$ mJ, equal to $U_1 + U_2 + U_3 = {fmt(U1 + U2 + U3)}$ mJ ✓.",
        "In a series connection the voltage divides in inverse proportion to capacitance, so the smaller series capacitor "
        "takes the larger share of the voltage.",
    ]
    question = (f"{layout}. The network is connected across an ideal {q(V, 'V')} battery. Find the equivalent capacitance, "
                "the charge on and voltage across each capacitor, and the total energy stored.")
    answer = (f"$C_{{eq}} = {fmt(Ceq)}$ μF; $Q_1 = {fmt(Q1)}$ μC, $Q_2 = {fmt(Q2)}$ μC, $Q_3 = {fmt(Q3)}$ μC; "
              f"$V_1 = {fmt(V1)}$ V, $V_2 = {fmt(V2)}$ V, $V_3 = {fmt(V3)}$ V; $U = {fmt(U)}$ mJ")
    return {
        "question": question,
        "steps": steps,
        "answer": answer,
        "values": {"C1_uF": C1, "C2_uF": C2, "C3_uF": C3, "V": V, "config": config, "C_eq_uF": Ceq, "Q_total_uC": Q,
                   "Q1_uC": Q1, "Q2_uC": Q2, "Q3_uC": Q3, "V1": V1, "V2": V2, "V3": V3, "U_total_mJ": U},
    }


@template("kirchhoff_two_loop_circuit", PHYS, "Electromagnetism", "Kirchhoff's rules", "hard")
def kirchhoff_two_loop_circuit(rng):
    while True:
        E1, E2 = nice(rng, 2, 24, 1), nice(rng, 2, 24, 1)
        R1, R2, R3 = nice(rng, 1, 40, 1), nice(rng, 1, 40, 1), nice(rng, 1, 40, 1)
        s2 = pick(rng, [1, 1, -1])
        e2 = s2 * E2
        D = R1 * R2 + R1 * R3 + R2 * R3
        I1 = (E1 * (R2 + R3) - e2 * R3) / D
        I2 = (e2 * (R1 + R3) - E1 * R3) / D
        I3 = I1 + I2
        if min(abs(I1), abs(I2), abs(I3)) >= 0.005:
            break
    Vab = I3 * R3
    P1, P2 = E1 * I1, e2 * I2
    P_out = I1 ** 2 * R1 + I2 ** 2 * R2 + I3 ** 2 * R3
    sgn = "+" if s2 > 0 else "-"
    question = (
        "Three branches connect the same two junctions, a (top) and b (bottom). The left branch is an ideal battery of EMF "
        f"$\\mathcal{{E}}_1 = {E1}$ V (positive terminal toward a) in series with $R_1 = {R1}$ Ω. The right branch is an ideal "
        f"battery of EMF $\\mathcal{{E}}_2 = {E2}$ V (positive terminal toward {'a' if s2 > 0 else 'b'}) in series with "
        f"$R_2 = {R2}$ Ω. The middle branch is a single resistor $R_3 = {R3}$ Ω. Use Kirchhoff's rules to find the current in "
        "each branch (size and direction) and the potential difference $V_a - V_b$, and check that energy is conserved."
    )
    steps = [
        "Choose directions: $I_1$ upward (b → a) in the left branch, $I_2$ upward (b → a) in the right branch and $I_3$ "
        "downward (a → b) through $R_3$. A negative result simply means the current flows the other way.",
        "Junction rule at a (current in = current out): $I_1 + I_2 = I_3$.",
        f"Loop rule, left loop (b → $\\mathcal{{E}}_1$ → $R_1$ → a → $R_3$ → b): $+\\mathcal{{E}}_1 - I_1R_1 - I_3R_3 = 0$, "
        f"i.e. ${E1} = {R1}I_1 + {R3}I_3$.",
        "Loop rule, right loop (b → $\\mathcal{E}_2$ → $R_2$ → a → $R_3$ → b): going upward through $\\mathcal{E}_2$ "
        + ("from its − to its + terminal gains" if s2 > 0 else "from its + to its − terminal loses")
        + f" {E2} V, so ${sgn}{E2} - I_2R_2 - I_3R_3 = 0$, i.e. ${e2} = {R2}I_2 + {R3}I_3$.",
        f"Substitute $I_3 = I_1 + I_2$: ${E1} = {R1 + R3}I_1 + {R3}I_2$ and ${e2} = {R3}I_1 + {R2 + R3}I_2$.",
        f"Solve with Cramer's rule. Determinant: $D = ({R1 + R3})({R2 + R3}) - ({R3})^2 = {D}$ Ω².",
        f"$I_1 = \\frac{{({E1})({R2 + R3}) - ({e2})({R3})}}{{{D}}} = {fmt(I1)}$ A and "
        f"$I_2 = \\frac{{({e2})({R1 + R3}) - ({E1})({R3})}}{{{D}}} = {fmt(I2)}$ A.",
        f"Then $I_3 = I_1 + I_2 = {fmt(I3)}$ A, and $V_a - V_b = I_3R_3 = ({fmt(I3)})({R3}) = {fmt(Vab)}$ V.",
    ]
    notes = []
    if I1 < 0:
        notes.append("$I_1 < 0$: the current in the left branch actually flows downward (a → b)")
    if I2 < 0:
        notes.append("$I_2 < 0$: the current in the right branch actually flows downward (a → b)")
    if I3 < 0:
        notes.append("$I_3 < 0$: the current in $R_3$ actually flows upward, so b is at the higher potential")
    if notes:
        steps.append("Interpret the signs: " + "; ".join(notes) + ".")

    def role(P):
        return f"delivers {fmt(abs(P))} W" if P > 0 else f"absorbs {fmt(abs(P))} W (it is being charged)"

    steps += [
        f"Battery 1 {role(P1)} and battery 2 {role(P2)}.",
        f"Energy check: net power from the batteries $\\mathcal{{E}}_1I_1 {sgn} \\mathcal{{E}}_2I_2 = {fmt(P1 + P2)}$ W; power "
        f"dissipated $I_1^2R_1 + I_2^2R_2 + I_3^2R_3 = {fmt(P_out)}$ W ✓.",
    ]

    def way(I, up):
        return ("b → a" if I > 0 else "a → b") if up else ("a → b" if I > 0 else "b → a")

    answer = (f"left branch {fmt(abs(I1))} A ({way(I1, True)}); right branch {fmt(abs(I2))} A ({way(I2, True)}); "
              f"middle branch {fmt(abs(I3))} A ({way(I3, False)}); $V_a - V_b = {fmt(Vab)}$ V")
    return {
        "question": question,
        "steps": steps,
        "answer": answer,
        "values": {"E1": E1, "E2": E2, "orient2": s2, "R1": R1, "R2": R2, "R3": R3, "I1": I1, "I2": I2, "I3": I3,
                   "V_ab": Vab, "P_dissipated": P_out},
    }


@template("wheatstone_bridge_balance", PHYS, "Electromagnetism", "DC circuits", "medium")
def wheatstone_bridge_balance(rng):
    if rng.random() < 0.6:
        R1, R2 = pick(rng, [(10, 10), (100, 100), (1000, 1000), (10, 100), (100, 10), (100, 1000), (1000, 100)])
        R3 = nice(rng, 1, 9999, 1)
        V = nice(rng, 1.5, 12.0, 0.5)
        Rx = R2 * R3 / R1
        Ia, Ib = V / (R1 + R2), V / (R3 + Rx)
        I = Ia + Ib
        Px = Ib ** 2 * Rx
        question = (
            f"In a Wheatstone bridge the ratio arms are $R_1 = {R1}$ Ω (between A and B) and $R_2 = {R2}$ Ω (between B and C). "
            "A decade resistance box $R_3$ (between A and D) and an unknown resistor $R_x$ (between D and C) form the other side. "
            f"A {q(V, 'V')} battery with negligible internal resistance is connected across A and C, and a galvanometer "
            f"between B and D. The galvanometer reads zero when $R_3 = {R3}$ Ω. Find $R_x$, the current drawn from the "
            "battery and the power dissipated in $R_x$."
        )
        steps = [
            "Zero galvanometer current means B and D are at the same potential. Then $R_1$ and $R_2$ carry the same current "
            "$I_a$, and $R_3$ and $R_x$ carry the same current $I_b$.",
            "Equal potential drops: $I_aR_1 = I_bR_3$ and $I_aR_2 = I_bR_x$. Dividing: $\\frac{R_1}{R_2} = \\frac{R_3}{R_x}$.",
            f"$R_x = \\frac{{R_2R_3}}{{R_1}} = \\frac{{({R2})({R3})}}{{{R1}}} = {fmt(Rx, 4)}$ Ω.",
            f"The galvanometer branch carries no current, so it can be removed: two parallel paths of "
            f"$R_1 + R_2 = {R1 + R2}$ Ω and $R_3 + R_x = {fmt(R3 + Rx, 4)}$ Ω.",
            f"$I_a = \\frac{{{fmt(V)}}}{{{R1 + R2}}} = {fmt(Ia * 1000)}$ mA and $I_b = \\frac{{{fmt(V)}}}{{{fmt(R3 + Rx, 4)}}} = "
            f"{fmt(Ib * 1000)}$ mA, so the battery supplies $I = I_a + I_b = {fmt(I * 1000)}$ mA.",
            f"Power in $R_x$: $P = I_b^2R_x = ({fmt(Ib)})^2({fmt(Rx, 4)}) = {fmt(Px * 1000)}$ mW.",
            f"Check: B and D are both ${fmt(Ia * R2)}$ V above C ($I_aR_2 = I_bR_x$) ✓. The balance condition does not "
            "depend on the battery voltage, which is why the bridge measures resistance so precisely.",
        ]
        answer = f"$R_x = {fmt(Rx, 4)}$ Ω; $I = {fmt(I * 1000)}$ mA; $P_x = {fmt(Px * 1000)}$ mW"
        values = {"variant": "wheatstone", "R1": R1, "R2": R2, "R3": R3, "V": V, "Rx": Rx, "I_total_mA": I * 1000,
                  "P_x_mW": Px * 1000}
    else:
        R = nice(rng, 1.0, 20.0, 0.5)
        l = nice(rng, 20.0, 80.0, 0.1)
        S = nice(rng, 1, 20, 1)
        Rx = R * l / (100 - l)
        l_new = 100 * (Rx + S) / (Rx + S + R)
        question = (
            "A meter bridge has a uniform resistance wire 100 cm long. An unknown resistor $R_x$ is in the left gap and a "
            f"standard resistor $R = {fmt(R)}$ Ω is in the right gap. The galvanometer shows no deflection when the sliding "
            f"contact is {q(l, 'cm')} from the left end of the wire. Find $R_x$. A {q(S, 'Ω')} resistor is then connected in "
            "series with $R_x$; where is the new balance point?"
        )
        steps = [
            "The wire is uniform, so the resistance of each segment is proportional to its length. At balance the bridge "
            "condition gives $\\frac{R_x}{R} = \\frac{l}{100 - l}$ (lengths in cm).",
            f"$R_x = R\\frac{{l}}{{100 - l}} = ({fmt(R)})\\frac{{{fmt(l)}}}{{{fmt(100 - l)}}} = {fmt(Rx)}$ Ω.",
            f"With the extra resistor the left gap holds $R_x + {S} = {fmt(Rx + S)}$ Ω. New balance: "
            f"$\\frac{{l'}}{{100 - l'}} = \\frac{{R_x + {S}}}{{R}} \\Rightarrow l' = \\frac{{100(R_x + {S})}}{{R_x + {S} + R}} = "
            f"{fmt(l_new)}$ cm from the left end.",
            f"Check: $\\frac{{{fmt(l_new)}}}{{{fmt(100 - l_new)}}} = {fmt(l_new / (100 - l_new))}$ and "
            f"$\\frac{{{fmt(Rx + S)}}}{{{fmt(R)}}} = {fmt((Rx + S) / R)}$ ✓. The balance point moves toward the larger "
            "resistance; balance points near the middle of the wire give the most precise results.",
        ]
        answer = f"$R_x = {fmt(Rx)}$ Ω; new balance point {q(l_new, 'cm')} from the left end"
        values = {"variant": "meter_bridge", "R_known": R, "l_cm": l, "S": S, "Rx": Rx, "l_new_cm": l_new}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Electromagnetism: transients and AC circuits
# ---------------------------------------------------------------------------


@template("rl_circuit_current_growth", PHYS, "Electromagnetism", "RL circuits", "medium")
def rl_circuit_current_growth(rng):
    L_mH = nice(rng, 10, 900, 10)
    R = nice(rng, 2, 100, 1)
    emf = nice(rng, 3, 48, 1)
    L = L_mH / 1000
    tau = L / R
    I_inf = emf / R
    coil = pick(rng, ["an inductor", "a large solenoid", "an electromagnet coil", "a choke coil"])
    setup = (f"{coil[0].upper() + coil[1:]} with inductance {q(L_mH, 'mH')} is connected in series with a resistor so that "
             f"the total resistance of the circuit is {q(R, 'Ω')}, and the combination is switched across an ideal "
             f"{q(emf, 'V')} battery at $t = 0$.")
    steps = [
        "Loop rule: $\\mathcal{E} - IR - L\\frac{dI}{dt} = 0$. With $I(0) = 0$ the solution is "
        "$I(t) = \\frac{\\mathcal{E}}{R}\\left(1 - e^{-t/\\tau}\\right)$ with time constant $\\tau = L/R$.",
        f"Time constant: $\\tau = \\frac{{L}}{{R}} = \\frac{{{fmt(L)}\\text{{ H}}}}{{{R}\\,\\Omega}} = {fmt(tau * 1000)}$ ms.",
        f"Final current (once the current is steady the inductor acts like a plain wire): "
        f"$I_\\infty = \\mathcal{{E}}/R = {emf}/{R} = {fmt(I_inf)}$ A. The initial rate of rise is "
        f"$\\frac{{dI}}{{dt}}\\big|_0 = \\mathcal{{E}}/L = {fmt(emf / L)}$ A/s.",
    ]
    if rng.random() < 0.55:
        t_ms = sig(tau * 1000 * nice(rng, 0.2, 4.0, 0.1), 3)
        t = t_ms / 1000
        x = t / tau
        I = I_inf * (1 - math.exp(-x))
        VL = emf * math.exp(-x)
        U = 0.5 * L * I ** 2
        question = (setup + f" Find the time constant, the final current, and, at $t = {fmt(t_ms)}$ ms, the current, the "
                    "voltage across the inductor and the energy stored in its magnetic field.")
        steps += [
            f"At $t = {fmt(t_ms)}$ ms: $t/\\tau = {fmt(x)}$, so $I = {fmt(I_inf)}\\left(1 - e^{{-{fmt(x)}}}\\right) = {fmt(I)}$ A "
            f"({fmt(100 * I / I_inf)}% of the final value).",
            f"Inductor voltage: $V_L = L\\frac{{dI}}{{dt}} = \\mathcal{{E}}e^{{-t/\\tau}} = {emf}e^{{-{fmt(x)}}} = {fmt(VL)}$ V "
            f"(check: $IR + V_L = {fmt(I * R + VL)}$ V $= \\mathcal{{E}}$ ✓).",
            f"Stored energy: $U = \\tfrac12LI^2 = \\tfrac12({fmt(L)})({fmt(I)})^2 = {_energy(U)}.",
        ]
        answer = (f"$\\tau = {fmt(tau * 1000)}$ ms; $I_\\infty = {fmt(I_inf)}$ A; at {q(t_ms, 'ms')}: $I = {fmt(I)}$ A, "
                  f"$V_L = {fmt(VL)}$ V, $U = {_energy(U)}")
        values = {"variant": "at_time", "L": L, "R": R, "emf": emf, "tau": tau, "I_final": I_inf, "t": t, "I_t": I,
                  "V_L": VL, "U_t": U}
    else:
        pct = nice(rng, 10, 99, 1)
        t = -tau * math.log(1 - pct / 100)
        U_inf = 0.5 * L * I_inf ** 2
        question = (setup + f" Find the time constant and the final current. How long after the switch is closed does the "
                    f"current reach {pct}% of its final value, and how much energy is stored in the inductor once the "
                    "current is steady?")
        steps += [
            f"Set $I = {fmt(pct / 100, 2)}I_\\infty$: $1 - e^{{-t/\\tau}} = {fmt(pct / 100, 2)} \\Rightarrow "
            f"t = -\\tau\\ln(1 - {fmt(pct / 100, 2)}) = ({fmt(tau * 1000)}\\text{{ ms}})({fmt(-math.log(1 - pct / 100))}) = "
            f"{fmt(t * 1000)}$ ms.",
            f"Steady-state energy: $U = \\tfrac12LI_\\infty^2 = \\tfrac12({fmt(L)})({fmt(I_inf)})^2 = {_energy(U_inf)}.",
            "Rule of thumb: the current reaches 63% of its final value after one time constant and more than 99% after "
            "five.",
        ]
        answer = (f"$\\tau = {fmt(tau * 1000)}$ ms; $I_\\infty = {fmt(I_inf)}$ A; {pct}% reached after {q(t * 1000, 'ms')}; "
                  f"$U_\\infty = {_energy(U_inf)}")
        values = {"variant": "time_to_fraction", "L": L, "R": R, "emf": emf, "tau": tau, "I_final": I_inf, "percent": pct,
                  "t": t, "U_final": U_inf}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("series_rlc_phase_power", PHYS, "Electromagnetism", "AC circuits", "hard")
def series_rlc_phase_power(rng):
    R = nice(rng, 10, 300, 5)
    L_mH = nice(rng, 10, 500, 10)
    C_uF = nice(rng, 1, 100, 1)
    if rng.random() < 0.5:
        V, f = pick(rng, [(120, 60), (230, 50), (240, 50), (220, 60)])
        source = "AC mains supply"
    else:
        V, f = nice(rng, 5, 50, 1), nice(rng, 100, 2000, 50)
        source = "signal generator"
    L, Cap = L_mH / 1000, C_uF * 1e-6
    w = 2 * math.pi * f
    XL, XC = w * L, 1 / (w * Cap)
    X = XL - XC
    Z = math.hypot(R, X)
    I = V / Z
    phi = math.degrees(math.atan2(X, R))
    pf = R / Z
    P = I ** 2 * R
    VR, VLv, VCv = I * R, I * XL, I * XC
    f0 = 1 / (2 * math.pi * math.sqrt(L * Cap))
    if X > 0:
        rel, nature = "lags", "inductive (above resonance)"
    else:
        rel, nature = "leads", "capacitive (below resonance)"
    question = (
        f"A {q(R, 'Ω')} resistor, a {q(L_mH, 'mH')} inductor and a {q(C_uF, 'μF')} capacitor are connected in series to a "
        f"{q(V, 'V')} (rms), {q(f, 'Hz')} {source}. Find the reactances, the impedance, the rms current, the phase angle "
        "between the current and the source voltage, the power factor and the average power delivered."
    )
    steps = [
        f"Angular frequency: $\\omega = 2\\pi f = 2\\pi({f}) = {fmt(w, 4)}$ rad/s.",
        f"Reactances: $X_L = \\omega L = ({fmt(w, 4)})({fmt(L)}) = {fmt(XL)}$ Ω; "
        f"$X_C = \\frac{{1}}{{\\omega C}} = \\frac{{1}}{{({fmt(w, 4)})({fmt(Cap)})}} = {fmt(XC)}$ Ω.",
        f"Impedance: $Z = \\sqrt{{R^2 + (X_L - X_C)^2}} = \\sqrt{{{R}^2 + ({fmt(X)})^2}} = {fmt(Z)}$ Ω.",
        f"Current: $I_{{rms}} = V_{{rms}}/Z = {V}/{fmt(Z)} = {fmt(I)}$ A.",
        f"Phase angle: $\\tan\\phi = \\frac{{X_L - X_C}}{{R}} = \\frac{{{fmt(X)}}}{{{R}}} \\Rightarrow \\phi = {_deg(phi)}$. "
        f"The circuit is {nature}, so the current {rel} the voltage.",
        f"Power factor: $\\cos\\phi = R/Z = {fmt(pf)}$. Average power: $P = I_{{rms}}^2R = ({fmt(I)})^2({R}) = {fmt(P)}$ W "
        f"(the same as $V_{{rms}}I_{{rms}}\\cos\\phi$); only the resistor dissipates energy.",
        f"Component voltages: $V_R = {fmt(VR)}$ V, $V_L = {fmt(VLv)}$ V, $V_C = {fmt(VCv)}$ V. They add as phasors: "
        f"$\\sqrt{{V_R^2 + (V_L - V_C)^2}} = {fmt(math.hypot(VR, VLv - VCv))}$ V $= V_{{rms}}$ ✓ "
        "(individual reactive voltages may exceed the source voltage).",
        f"For reference, the resonant frequency is $f_0 = \\frac{{1}}{{2\\pi\\sqrt{{LC}}}} = {fmt(f0)}$ Hz, where $Z = R$ and "
        "the power factor would be 1.",
    ]
    answer = (f"$X_L = {fmt(XL)}$ Ω, $X_C = {fmt(XC)}$ Ω, $Z = {fmt(Z)}$ Ω, $I_{{rms}} = {fmt(I)}$ A, "
              f"$\\phi = {_deg(phi)}$ (current {rel} the voltage), power factor ${fmt(pf)}$, $P = {fmt(P)}$ W")
    return {
        "question": question,
        "steps": steps,
        "answer": answer,
        "values": {"R": R, "L": L, "C": Cap, "V": V, "f": f, "X_L": XL, "X_C": XC, "Z": Z, "I": I, "phi_deg": phi,
                   "power_factor": pf, "P": P, "f0": f0},
    }


@template("power_factor_correction_capacitor", PHYS, "Electromagnetism", "AC power", "hard")
def power_factor_correction_capacitor(rng):
    load = pick(rng, ["an induction motor", "a workshop's motor load", "a commercial refrigeration unit",
                      "an air-conditioning compressor", "a welding transformer"])
    V, f = pick(rng, [(120, 60), (230, 50), (240, 50), (240, 60), (277, 60)])
    P_kW = nice(rng, 1.0, 12.0, 0.5) if V == 120 else nice(rng, 2, 25, 1)
    pf1 = nice(rng, 0.60, 0.85, 0.01)
    pf2 = pick(rng, [0.90, 0.92, 0.95, 0.98, 1.0])
    P = P_kW * 1000
    phi1, phi2 = math.acos(pf1), math.acos(pf2)
    S1 = P / pf1
    Q1 = P * math.tan(phi1)
    Q2 = P * math.tan(phi2)
    Qc = Q1 - Q2
    Cap = Qc / (2 * math.pi * f * V ** 2)
    I1, I2 = S1 / V, P / (pf2 * V)

    def pfs(x):
        return fmt(x, 3 if x >= 1 else 2)

    question = (
        f"{load[0].upper() + load[1:]} draws {q(P_kW, 'kW')} of real power from a {q(V, 'V')} (rms), {q(f, 'Hz')} single-phase "
        f"supply at a lagging power factor of {pfs(pf1)}. What capacitance must be connected in parallel with it to raise the "
        f"power factor to {pfs(pf2)}, and how does the line current change?"
    )
    steps = [
        f"Before correction: apparent power $S_1 = P/\\cos\\phi_1 = {fmt(P_kW)}/{pfs(pf1)} = {fmt(S1 / 1000)}$ kVA and line "
        f"current $I_1 = S_1/V = {fmt(S1)}/{V} = {fmt(I1)}$ A.",
        f"Phase angle $\\phi_1 = \\arccos({pfs(pf1)}) = {_deg(math.degrees(phi1))}$; reactive power drawn by the inductive load "
        f"$Q_1 = P\\tan\\phi_1 = {fmt(Q1 / 1000)}$ kvar.",
        (f"Target: $\\phi_2 = \\arccos({pfs(pf2)}) = {_deg(math.degrees(phi2))}$, so the reactive power still drawn is "
         f"$Q_2 = P\\tan\\phi_2 = {fmt(Q2 / 1000)}$ kvar." if pf2 < 1 else
         "Target: unity power factor ($\\phi_2 = 0$), so the reactive power drawn from the supply must become $Q_2 = 0$."),
        f"The parallel capacitor must supply $Q_C = Q_1 - Q_2 = {fmt(Qc / 1000)}$ kvar; the real power is unchanged.",
        f"A capacitor across the supply has $Q_C = V^2/X_C = 2\\pi fCV^2$, so "
        f"$C = \\frac{{Q_C}}{{2\\pi fV^2}} = \\frac{{{fmt(Qc)}}}{{2\\pi({f})({V})^2}} = {fmt(Cap)}$ F $= {fmt(Cap * 1e6)}$ μF.",
        f"New line current: $I_2 = \\frac{{P}}{{V\\cos\\phi_2}} = \\frac{{{fmt(P)}}}{{({V})({pfs(pf2)})}} = {fmt(I2)}$ A, "
        f"a reduction of {fmt(100 * (1 - I2 / I1))}%. Resistive losses in the supply wiring scale as $I^2$ and fall to "
        f"{fmt(100 * (I2 / I1) ** 2)}% of their former value.",
    ]
    answer = (f"$C = {fmt(Cap * 1e6)}$ μF ($Q_C = {fmt(Qc / 1000)}$ kvar); line current falls from {q(I1, 'A')} to "
              f"{q(I2, 'A')}")
    return {
        "question": question,
        "steps": steps,
        "answer": answer,
        "values": {"P_kW": P_kW, "V": V, "f": f, "pf1": pf1, "pf2": pf2, "S1_kVA": S1 / 1000, "Q1_kvar": Q1 / 1000,
                   "Qc_kvar": Qc / 1000, "C_uF": Cap * 1e6, "I1": I1, "I2": I2},
    }


# ---------------------------------------------------------------------------
# Electromagnetism: fields, particles and waves
# ---------------------------------------------------------------------------


@template("hall_effect_carrier_density", PHYS, "Electromagnetism", "Hall effect", "medium")
def hall_effect_carrier_density(rng):
    if rng.random() < 0.55:
        sample = pick(rng, ["n-type germanium", "n-type silicon", "indium antimonide", "n-type gallium arsenide"])
        n_true = sig(10 ** rng.uniform(21.0, 22.5), 2)
        I_mA = nice(rng, 1.0, 20.0, 0.5)
        B = nice(rng, 0.10, 1.50, 0.05)
        t_mm = nice(rng, 0.10, 1.00, 0.05)
        w_mm = nice(rng, 2, 10, 1)
        I, t, w = I_mA / 1000, t_mm / 1000, w_mm / 1000
        VH_uV = sig(I * B / (n_true * E_CHARGE * t) * 1e6, 3)
        VH = VH_uV * 1e-6
        n = I * B / (E_CHARGE * t * VH)
        vd = VH / (w * B)
        question = (
            f"A rectangular sample of {sample} is {q(w_mm, 'mm')} wide and {q(t_mm, 'mm')} thick. It carries a current of "
            f"{q(I_mA, 'mA')} along its length in a uniform magnetic field of {q(B, 'T')} perpendicular to its broad face, and a "
            f"Hall voltage of {_voltage(VH_uV)} is measured across its width. Assuming the current is carried by electrons, "
            "find the carrier density, the drift speed of the carriers and the magnitude of the Hall coefficient."
        )
        steps = [
            "The magnetic force deflects the moving carriers sideways until the transverse Hall field $E_H = V_H/w$ balances "
            "it: $qE_H = qv_dB$.",
            "The current is $I = nqv_dA$ with cross-section $A = wt$. Eliminating $v_d$: $V_H = E_Hw = v_dBw = \\frac{IB}{nqt}$ "
            "(the width cancels).",
            f"Carrier density: $n = \\frac{{IB}}{{qtV_H}} = \\frac{{({fmt(I)})({fmt(B)})}}{{(1.602\\times10^{{-19}})({fmt(t)})"
            f"({fmt(VH)})}} = {fmt(n)}$ m⁻³.",
            f"Drift speed: $v_d = \\frac{{E_H}}{{B}} = \\frac{{V_H}}{{wB}} = \\frac{{{fmt(VH)}}}{{({fmt(w)})({fmt(B)})}} = "
            f"{fmt(vd)}$ m/s.",
            f"Hall coefficient: $|R_H| = \\frac{{1}}{{nq}} = {fmt(1 / (n * E_CHARGE))}$ m³/C (negative for electron carriers).",
            f"For comparison, copper has $n \\approx 8.5\\times10^{{28}}$ m⁻³, about ${fmt(8.5e28 / n, 2)}$ times more; the low carrier "
            "density is why semiconductors give large Hall voltages and are used in Hall-effect sensors.",
        ]
        answer = f"$n = {fmt(n)}$ m⁻³; $v_d = {fmt(vd)}$ m/s; $|R_H| = {fmt(1 / (n * E_CHARGE))}$ m³/C"
        values = {"variant": "semiconductor", "I": I, "B": B, "t": t, "w": w, "V_H": VH, "n": n, "v_d": vd,
                  "R_H": 1 / (n * E_CHARGE)}
    else:
        metal, n = pick(rng, [("copper", 8.47e28), ("silver", 5.86e28), ("gold", 5.90e28)])
        I = nice(rng, 1, 20, 1)
        B = nice(rng, 0.5, 2.0, 0.1)
        t_mm = nice(rng, 0.05, 0.50, 0.05)
        w_mm = nice(rng, 5, 30, 1)
        t, w = t_mm / 1000, w_mm / 1000
        VH = I * B / (n * E_CHARGE * t)
        vd = I / (n * E_CHARGE * w * t)
        EH = VH / w
        question = (
            f"A thin {metal} strip {q(w_mm, 'mm')} wide and {q(t_mm, 'mm')} thick carries a current of {q(I, 'A')} along its "
            f"length. A uniform magnetic field of {q(B, 'T')} is perpendicular to its broad face. The free-electron density of "
            f"{metal} is {q(n, 'm⁻³')}. Find the electrons' drift speed, the Hall voltage across the width of the strip and "
            "the Hall electric field."
        )
        steps = [
            f"Drift speed from $I = nev_dA$ with $A = wt = ({fmt(w)})({fmt(t)}) = {fmt(w * t)}$ m²: "
            f"$v_d = \\frac{{I}}{{newt}} = {fmt(vd)}$ m/s $= {fmt(vd * 1000)}$ mm/s. The electrons creep along far more slowly "
            "than walking pace, even though the electrical signal travels at nearly the speed of light.",
            "In equilibrium the Hall field balances the magnetic force on the drifting electrons: $eE_H = ev_dB$.",
            f"$E_H = v_dB = ({fmt(vd)})({fmt(B)}) = {fmt(EH)}$ V/m.",
            f"Hall voltage: $V_H = E_Hw = \\frac{{IB}}{{net}} = \\frac{{({I})({fmt(B)})}}{{({fmt(n)})(1.602\\times10^{{-19}})"
            f"({fmt(t)})}} = {fmt(VH)}$ V $= {fmt(VH * 1e6)}$ μV.",
            "The voltage is tiny because metals have an enormous density of free electrons, so they drift very slowly.",
        ]
        answer = f"$v_d = {fmt(vd)}$ m/s; $V_H = {fmt(VH * 1e6)}$ μV; $E_H = {fmt(EH)}$ V/m"
        values = {"variant": "metal", "I": I, "B": B, "t": t, "w": w, "n": n, "V_H": VH, "v_d": vd, "E_H": EH}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


ISOTOPE_PAIRS = [  # symbol, element, A1, atomic mass 1 (u), A2, atomic mass 2 (u)
    ("Li", "lithium", 6, 6.015123, 7, 7.016003),
    ("B", "boron", 10, 10.012937, 11, 11.009305),
    ("C", "carbon", 12, 12.000000, 13, 13.003355),
    ("O", "oxygen", 16, 15.994915, 18, 17.999160),
    ("Ne", "neon", 20, 19.992440, 22, 21.991385),
    ("Mg", "magnesium", 24, 23.985042, 26, 25.982593),
    ("Cl", "chlorine", 35, 34.968853, 37, 36.965903),
    ("Cu", "copper", 63, 62.929598, 65, 64.927790),
    ("Br", "bromine", 79, 78.918338, 81, 80.916291),
    ("U", "uranium", 235, 235.043930, 238, 238.050788),
]


@template("mass_spectrometer_isotope_separation", PHYS, "Electromagnetism", "Mass spectrometry", "medium")
def mass_spectrometer_isotope_separation(rng):
    while True:
        sym, element, A1, m1u, A2, m2u = pick(rng, ISOTOPE_PAIRS)
        V = nice(rng, 500, 5000, 100)
        B = nice(rng, 0.10, 1.00, 0.01)
        m1, m2 = m1u * U_KG, m2u * U_KG
        r1 = math.sqrt(2 * m1 * V / E_CHARGE) / B
        r2 = math.sqrt(2 * m2 * V / E_CHARGE) / B
        if 0.03 <= r1 and r2 <= 0.8:
            break
    v1 = math.sqrt(2 * E_CHARGE * V / m1)
    dx = 2 * (r2 - r1)
    i1, i2 = f"$^{{{A1}}}\\text{{{sym}}}^+$", f"$^{{{A2}}}\\text{{{sym}}}^+$"
    question = (
        f"In a mass spectrometer, singly charged ions of the {element} isotopes {i1} and {i2} (atomic masses "
        f"{_fixed(m1u, 6)} u and {_fixed(m2u, 6)} u) are accelerated from rest through a potential difference of {q(V, 'V')} "
        f"and then enter a uniform magnetic field of {q(B, 'T')} at right angles to their velocity. After half a circle they "
        "strike a detector plate. Find the speed of the lighter ions, the radius of each path and the distance between the "
        "two impact points. (Take each ion's mass equal to its atomic mass; $1$ u $= 1.66054\\times10^{-27}$ kg.)"
    )
    steps = [
        f"Energy gained in the accelerating gap: $\\tfrac12mv^2 = qV \\Rightarrow v = \\sqrt{{2qV/m}}$. For {i1}: "
        f"$m_1 = ({_fixed(m1u, 6)})(1.66054\\times10^{{-27}}) = {fmt(m1, 5)}$ kg, so "
        f"$v_1 = \\sqrt{{\\frac{{2(1.602\\times10^{{-19}})({V})}}{{{fmt(m1, 5)}}}}} = {fmt(v1)}$ m/s.",
        "In the field the magnetic force supplies the centripetal force: $qvB = \\frac{mv^2}{r} \\Rightarrow "
        "r = \\frac{mv}{qB} = \\frac{1}{B}\\sqrt{\\frac{2mV}{q}}$.",
        f"$r_1 = \\frac{{1}}{{{fmt(B)}}}\\sqrt{{\\frac{{2({fmt(m1, 5)})({V})}}{{1.602\\times10^{{-19}}}}}} = {fmt(r1, 4)}$ m "
        f"$= {fmt(r1 * 100, 4)}$ cm.",
        f"For {i2} ($m_2 = {fmt(m2, 5)}$ kg): $r_2 = {fmt(r2, 4)}$ m $= {fmt(r2 * 100, 4)}$ cm. "
        f"Check: $r_2/r_1 = \\sqrt{{m_2/m_1}} = {fmt(math.sqrt(m2u / m1u), 5)}$ ✓.",
        f"Each ion lands a distance $2r$ (one diameter) from the entrance slit, so the impact points are "
        f"$\\Delta x = 2(r_2 - r_1) = {fmt(dx * 1000)}$ mm apart.",
    ]
    answer = f"$v_1 = {fmt(v1)}$ m/s; $r_1 = {fmt(r1 * 100, 4)}$ cm, $r_2 = {fmt(r2 * 100, 4)}$ cm; separation {q(dx * 1000, 'mm')}"
    return {
        "question": question,
        "steps": steps,
        "answer": answer,
        "values": {"m1_u": m1u, "m2_u": m2u, "V": V, "B": B, "v1": v1, "r1": r1, "r2": r2, "separation": dx},
    }


@template("em_wave_intensity_radiation_pressure", PHYS, "Electromagnetism", "Electromagnetic waves", "medium")
def em_wave_intensity_radiation_pressure(rng):
    if rng.random() < 0.6:
        if rng.random() < 0.5:
            P_mW = nice(rng, 0.5, 5.0, 0.5)
            P, src, P_txt = P_mW / 1000, "A laser pointer", q(P_mW, "mW")
            d_mm = nice(rng, 0.8, 3.0, 0.1)
        else:
            P = nice(rng, 1, 100, 1)
            src, P_txt = "A continuous-wave laboratory laser", q(P, "W")
            d_mm = nice(rng, 1.0, 10.0, 0.5)
        reflect = rng.random() < 0.5
        d = d_mm / 1000
        A = math.pi * d ** 2 / 4
        I = P / A
        E0 = math.sqrt(2 * I / (C * EPS0))
        B0 = E0 / C
        k = 2 if reflect else 1
        p_rad = k * I / C
        F = p_rad * A
        surface = "perfectly reflecting mirror" if reflect else "perfectly absorbing (black) target"
        question = (
            f"{src} emits {P_txt} in a beam of circular cross-section {q(d_mm, 'mm')} in diameter (assume the intensity is "
            "uniform across the beam). Find the intensity, the amplitudes of the electric and magnetic fields, and the "
            f"radiation pressure and force when the beam strikes a {surface} at normal incidence."
        )
        steps = [
            f"Beam area: $A = \\pi d^2/4 = \\pi({fmt(d)})^2/4 = {fmt(A)}$ m²; intensity $I = P/A = {fmt(P)}/({fmt(A)}) = {fmt(I)}$ W/m².",
            f"For a plane wave $I = \\tfrac12c\\varepsilon_0E_0^2$, so $E_0 = \\sqrt{{\\frac{{2I}}{{c\\varepsilon_0}}}} = "
            f"\\sqrt{{\\frac{{2({fmt(I)})}}{{(2.998\\times10^8)(8.854\\times10^{{-12}})}}}} = {fmt(E0)}$ V/m.",
            f"$B_0 = E_0/c = {fmt(B0)}$ T.",
            (f"Light carries momentum flux $I/c$. A reflector reverses it, so $p_{{rad}} = 2I/c = {fmt(p_rad)}$ Pa." if reflect
             else f"Light carries momentum flux $I/c$; an absorber takes all of it, so $p_{{rad}} = I/c = {fmt(p_rad)}$ Pa."),
            f"Force: $F = p_{{rad}}A = {'2' if reflect else ''}P/c = {fmt(F)}$ N, equal to the weight of a mere "
            f"{q(F / 9.81, 'kg')}; radiation pressure is negligible in everyday life but matters for tiny particles "
            "(optical tweezers) and for spacecraft.",
        ]
        answer = (f"$I = {fmt(I)}$ W/m²; $E_0 = {fmt(E0)}$ V/m; $B_0 = {fmt(B0)}$ T; $p_{{rad}} = {fmt(p_rad)}$ Pa; "
                  f"$F = {fmt(F)}$ N")
        values = {"variant": "laser", "P": P, "d": d, "reflect": reflect, "I": I, "E0": E0, "B0": B0, "p_rad": p_rad, "F": F}
    else:
        while True:
            r_AU = pick(rng, [0.39, 0.72, 1.0, 1.52]) if rng.random() < 0.4 else nice(rng, 0.3, 1.6, 0.1)
            A = nice(rng, 20, 2000, 20)
            m = nice(rng, 1, 100, 1)
            if 0.005 <= m / A <= 0.5:
                break
        I = SOLAR_CONSTANT / r_AU ** 2
        F = 2 * I * A / C
        a = F / m
        dv = a * 86400
        E0 = math.sqrt(2 * I / (C * EPS0))
        question = (
            f"A solar-sail spacecraft has a sail of area {q(A, 'm²')} and a total mass of {q(m, 'kg')}. It is {q(r_AU, 'AU')} "
            "from the Sun with the sail facing the sunlight squarely. The solar intensity at 1 AU is 1361 W/m² and falls off "
            "as $1/r^2$. Treating the sail as a perfect reflector, find the intensity at the sail, the electric-field amplitude "
            "of the sunlight, the radiation force, the acceleration and the speed gained in one day (assume the force stays "
            "constant over that day and ignore gravity)."
        )
        steps = [
            f"Intensity: $I = 1361/r^2 = 1361/({fmt(r_AU)})^2 = {fmt(I)}$ W/m².",
            f"Field amplitude: $E_0 = \\sqrt{{2I/(c\\varepsilon_0)}} = {fmt(E0)}$ V/m.",
            f"Perfect reflection doubles the momentum transfer: $p_{{rad}} = 2I/c = {fmt(2 * I / C)}$ Pa, so "
            f"$F = \\frac{{2IA}}{{c}} = \\frac{{2({fmt(I)})({A})}}{{2.998\\times10^8}} = {fmt(F)}$ N.",
            f"Acceleration: $a = F/m = {fmt(F)}/{m} = {fmt(a)}$ m/s².",
            f"Speed gained in one day (86 400 s): $\\Delta v = at = {fmt(dv)}$ m/s. The thrust is tiny but continuous and "
            "needs no propellant.",
        ]
        answer = f"$I = {fmt(I)}$ W/m²; $E_0 = {fmt(E0)}$ V/m; $F = {fmt(F)}$ N; $a = {fmt(a)}$ m/s²; $\\Delta v = {fmt(dv)}$ m/s per day"
        values = {"variant": "solar_sail", "r_AU": r_AU, "A": A, "m": m, "I": I, "E0": E0, "F": F, "a": a, "dv_day": dv}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Waves and optics
# ---------------------------------------------------------------------------


NUM_WORDS = {1: "one", 2: "two", 3: "three", 4: "four"}


@template("malus_law_polarizer_chain", PHYS, "Waves and Optics", "Polarization", "easy")
def malus_law_polarizer_chain(rng):
    I0 = nice(rng, 10, 900, 10)
    mode = pick(rng, ["unpolarized", "unpolarized", "polarized", "crossed"])
    if mode == "crossed":
        th = nice(rng, 5, 85, 5)
        angles = [0, th, 90]
    elif mode == "unpolarized":
        angles = [0] + sorted(rng.sample(range(10, 95, 5), rng.randint(1, 3)))
    else:
        angles = sorted(rng.sample(range(10, 95, 5), rng.randint(1, 3)))
    ang_txt = _and(f"${a}^\\circ$" for a in angles)
    if mode == "crossed":
        question = (
            f"Unpolarized light of intensity {q(I0, 'W/m²')} falls on two crossed ideal polarizers (transmission axes vertical "
            f"and horizontal). A third ideal polarizer is inserted between them with its axis at ${th}^\\circ$ to the vertical. "
            "What intensity emerges? What would emerge without the middle polarizer, and for what orientation of the middle "
            "polarizer is the transmitted intensity largest?"
        )
    elif mode == "unpolarized":
        question = (
            f"Unpolarized light of intensity {q(I0, 'W/m²')} passes through {NUM_WORDS[len(angles)]} ideal polarizing filters in turn. "
            f"Their transmission axes make angles of {ang_txt} with the vertical. Find the intensity after each filter and the "
            "fraction of the incident intensity that is transmitted."
        )
    else:
        question = (
            f"Vertically polarized laser light of intensity {q(I0, 'W/m²')} passes through "
            + ("an ideal polarizer whose transmission axis makes an angle of " if len(angles) == 1
               else f"{NUM_WORDS[len(angles)]} ideal polarizers in turn whose transmission axes make angles of ")
            + f"{ang_txt} with the vertical. Find the intensity after each filter and the fraction of the incident "
            "intensity that is transmitted."
        )
    steps = []
    intensities = []
    if mode == "polarized":
        c2 = _cos2(angles[0])
        I = I0 * c2
        steps.append(f"Malus's law, $I = I_0\\cos^2\\theta$, with $\\theta$ the angle between the light's polarization and the "
                     f"filter axis. Filter 1: $I_1 = {I0}\\cos^2 {angles[0]}^\\circ = ({I0})({fmt(c2, 4)}) = {fmt(I)}$ W/m².")
    else:
        I = I0 / 2
        steps.append(f"An ideal polarizer passes half of unpolarized light (the average of $\\cos^2\\theta$ over all directions "
                     f"is $\\tfrac12$): $I_1 = I_0/2 = {fmt(I)}$ W/m², now polarized along ${angles[0]}^\\circ$.")
    intensities.append(I)
    for k in range(1, len(angles)):
        dth = angles[k] - angles[k - 1]
        c2 = _cos2(dth)
        prev, I = I, I * c2
        intensities.append(I)
        steps.append(f"Filter {k + 1}: the angle between successive axes is ${dth}^\\circ$, so by Malus's law "
                     f"$I_{k + 1} = I_{k}\\cos^2 {dth}^\\circ = ({fmt(prev)})({fmt(c2, 4)}) = {fmt(I)}$ W/m²; the light leaves "
                     f"polarized along ${angles[k]}^\\circ$.")
    frac = I / I0
    steps.append(f"Fraction transmitted: $I/I_0 = {fmt(I)}/{I0} = {fmt(frac)}$ ({fmt(100 * frac)}%).")
    if mode == "crossed":
        steps += [
            "Without the middle filter the two crossed polarizers are at $90^\\circ$ and transmit nothing, since $\\cos^2 90^\\circ = 0$.",
            f"In general $I = \\frac{{I_0}}{{2}}\\cos^2\\theta\\sin^2\\theta = \\frac{{I_0}}{{8}}\\sin^2 2\\theta$; here "
            f"$\\frac{{{I0}}}{{8}}\\sin^2 {2 * th}^\\circ = {fmt(I0 / 8 * math.sin(math.radians(2 * th)) ** 2)}$ W/m² ✓. "
            f"The maximum, $I_0/8 = {fmt(I0 / 8)}$ W/m², occurs at $\\theta = 45^\\circ$.",
        ]
        answer = (f"{q(I, 'W/m²')} ({fmt(100 * frac)}% of $I_0$); zero without the middle polarizer; maximum "
                  f"{q(I0 / 8, 'W/m²')} at $45^\\circ$")
    else:
        answer = "intensities " + ", ".join(f"{fmt(x)}" for x in intensities) + f" W/m²; fraction transmitted {fmt(frac)}"
    return {
        "question": question,
        "steps": steps,
        "answer": answer,
        "values": {"I0": I0, "mode": mode, "angles_deg": angles, "intensities": intensities, "I_final": I,
                   "fraction": frac},
    }


BREWSTER_MEDIA = [("crown glass", 1.52), ("flint glass", 1.66), ("acrylic", 1.49), ("polycarbonate", 1.59),
                  ("diamond", 2.42), ("sapphire", 1.77), ("fused quartz", 1.46), ("water", 1.33), ("ice", 1.31)]


@template("brewster_angle_polarization", PHYS, "Waves and Optics", "Polarization", "medium")
def brewster_angle_polarization(rng):
    if rng.random() < 0.55:
        while True:
            name, n = pick(rng, BREWSTER_MEDIA)
            case = pick(rng, ["from_air", "from_water", "inside"])
            if case == "from_air":
                m1, n1, m2, n2 = "air", 1.00, name, n
            elif case == "from_water":
                m1, n1, m2, n2 = "water", 1.33, name, n
            else:
                m1, n1, m2, n2 = name, n, "air", 1.00
            if abs(n1 - n2) > 0.05:
                break
        I0 = nice(rng, 100, 1000, 50)
        thB = math.degrees(math.atan(n2 / n1))
        tht = 90 - thB
        Rs = math.sin(math.radians(thB - tht)) ** 2
        Ir = 0.5 * Rs * I0
        where = (f"travels in {m1} ($n_1 = {fmt(n1)}$) and strikes a flat surface of {m2} ($n_2 = {fmt(n2)}$)" if case != "inside"
                 else f"travels inside a block of {m1} ($n_1 = {fmt(n1)}$) and strikes its flat surface with air ($n_2 = 1.00$)")
        question = (
            f"A beam of unpolarized light of intensity {q(I0, 'W/m²')} {where}. (a) At what angle of incidence is the reflected "
            "light completely polarized? (b) What is the angle of refraction then? (c) Using the Fresnel equation for "
            "s-polarized light, what is the intensity of the reflected beam?"
        )
        steps = [
            "At Brewster's angle the reflected and refracted rays are perpendicular ($\\theta_B + \\theta_t = 90^\\circ$), and "
            "the component polarized in the plane of incidence (p) is not reflected at all. Combining this with Snell's law "
            "gives $\\tan\\theta_B = n_2/n_1$.",
            f"$\\theta_B = \\arctan\\frac{{{fmt(n2)}}}{{{fmt(n1)}}} = {_deg(thB)}$.",
            f"$\\theta_t = 90^\\circ - \\theta_B = {_deg(tht)}$. Check with Snell's law: $n_1\\sin\\theta_B = "
            f"{fmt(n1 * math.sin(math.radians(thB)), 4)}$ and $n_2\\sin\\theta_t = {fmt(n2 * math.sin(math.radians(tht)), 4)}$ ✓.",
            f"Only the s-component (perpendicular to the plane of incidence) is reflected, with reflectance "
            f"$R_s = \\frac{{\\sin^2(\\theta_B - \\theta_t)}}{{\\sin^2(\\theta_B + \\theta_t)}} = \\sin^2({_deg(thB - tht)}) = {fmt(Rs)}$.",
            f"Unpolarized light is half s and half p, so $I_r = \\tfrac12R_sI_0 = \\tfrac12({fmt(Rs)})({I0}) = {fmt(Ir)}$ W/m², "
            "linearly polarized parallel to the surface. This is why polarizing sunglasses cut glare.",
        ]
        if n1 > n2:
            thc = math.degrees(math.asin(n2 / n1))
            steps.append(f"Note that $\\theta_B$ is smaller than the critical angle $\\theta_c = \\arcsin(n_2/n_1) = {_deg(thc)}$, "
                         "so the reflected light is fully polarized before total internal reflection sets in.")
        answer = f"(a) $\\theta_B = {_deg(thB)}$; (b) $\\theta_t = {_deg(tht)}$; (c) $I_r = {fmt(Ir)}$ W/m² ($R_s = {fmt(Rs)}$)"
        values = {"variant": "forward", "n1": n1, "n2": n2, "I0": I0, "theta_B": thB, "theta_t": tht, "R_s": Rs,
                  "I_reflected": Ir}
    else:
        thB = nice(rng, 53.0, 68.0, 0.1)
        n = math.tan(math.radians(thB))
        tht = 90 - thB
        thc = math.degrees(math.asin(1 / n))
        question = (
            "A student shines light on a flat, polished sample of an unknown transparent material in air and finds that the "
            f"reflected light is completely polarized when the angle of incidence is ${_deg(thB)}$. Find the refractive index "
            "of the material, the angle of refraction at this incidence and the critical angle for total internal reflection "
            "inside the material."
        )
        steps = [
            "At Brewster's angle $\\tan\\theta_B = n_2/n_1$; with air as the first medium ($n_1 = 1.00$), $n = \\tan\\theta_B$.",
            f"$n = \\tan {_deg(thB)} = {fmt(n, 4)}$.",
            f"The reflected and refracted rays are perpendicular, so $\\theta_t = 90^\\circ - {_deg(thB)} = {_deg(tht)}$. "
            f"Check: $\\sin\\theta_B/\\sin\\theta_t = {fmt(math.sin(math.radians(thB)) / math.sin(math.radians(tht)), 4)} = n$ ✓.",
            f"Critical angle: $\\sin\\theta_c = 1/n \\Rightarrow \\theta_c = \\arcsin(1/{fmt(n, 4)}) = {_deg(thc)}$.",
        ]
        answer = f"$n = {fmt(n, 4)}$; $\\theta_t = {_deg(tht)}$; $\\theta_c = {_deg(thc)}$"
        values = {"variant": "find_index", "theta_B": thB, "n": n, "theta_t": tht, "theta_c": thc}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("thin_film_interference_colors", PHYS, "Waves and Optics", "Thin-film interference", "hard")
def thin_film_interference_colors(rng):
    if rng.random() < 0.55:
        film, n, below, nb = pick(rng, [("soap film", 1.33, "air", 1.00), ("soap film", 1.33, "air", 1.00),
                                        ("film of oil", 1.45, "water", 1.33), ("film of oil", 1.50, "water", 1.33),
                                        ("film of kerosene", 1.39, "water", 1.33)])
        while True:
            t = nice(rng, 250, 900, 10)
            opd = 2 * n * t
            bright = [opd / (m + 0.5) for m in range(40) if 380 <= opd / (m + 0.5) <= 750]
            if bright:
                break
        dark = [opd / m for m in range(1, 40) if 380 <= opd / m <= 750]
        listing = []
        m = 0
        while True:
            lam = opd / (m + 0.5)
            listing.append(f"$m = {m}$: ${fmt(lam)}$ nm ({_region(lam)})")
            if lam < 380:
                break
            m += 1
        surround = "in air" if below == "air" else f"floating on {below} ($n = {fmt(nb)}$)"
        question = (
            f"A {film} ($n = {fmt(n)}$) {q(t, 'nm')} thick is {surround} and is viewed in reflected white "
            "light at normal incidence. Which visible wavelengths (380–750 nm) are most strongly reflected, and which are "
            "missing from the reflected light?"
        )
        steps = [
            f"Phase changes: reflection at the top surface (air → film, into a higher index) adds a half-wavelength shift; "
            f"reflection at the bottom surface (film → {below}, into a lower index) does not. The two reflected waves therefore "
            "differ by half a wavelength in addition to their path difference.",
            f"Extra optical path of the wave reflected from the bottom: $2nt = 2({fmt(n)})({t}) = {fmt(opd, 4)}$ nm.",
            "Bright (constructive) reflection: $2nt = (m + \\tfrac12)\\lambda \\Rightarrow \\lambda = \\frac{2nt}{m + 1/2}$: "
            + "; ".join(listing) + ".",
            f"Visible wavelengths strongly reflected: {_and(f'{fmt(x)} nm ({_region(x)})' for x in bright)}.",
            ("Missing (destructive) wavelengths satisfy $2nt = m\\lambda$: "
             + _and(f"{fmt(x)} nm" for x in dark) + " in the visible range." if dark else
             "Destructive reflection needs $2nt = m\\lambda$; no visible wavelength satisfies it for this thickness."),
            "As the thickness varies across the film, the reflected color changes, producing the familiar swirling bands; "
            "where the film becomes much thinner than a wavelength it looks black in reflection.",
        ]
        answer = ("bright: " + _and(f"{fmt(x)} nm" for x in bright)
                  + ("; missing: " + _and(f"{fmt(x)} nm" for x in dark) if dark else "; no visible wavelength is fully cancelled"))
        values = {"variant": "film_colors", "n_film": n, "n_below": nb, "t_nm": t, "lam_bright": bright, "lam_dark": dark}
    else:
        coat, formula, nc, sub, ns, use = pick(rng, [
            ("magnesium fluoride", "MgF₂", 1.38, "crown glass", 1.52, "camera lens"),
            ("magnesium fluoride", "MgF₂", 1.38, "flint glass", 1.62, "eyeglass lens"),
            ("magnesium fluoride", "MgF₂", 1.38, "dense flint glass", 1.75, "microscope objective"),
            ("silicon nitride", "Si₃N₄", 2.00, "silicon", 3.90, "solar cell"),
            ("silicon dioxide", "SiO₂", 1.46, "silicon", 3.90, "photodiode"),
        ])
        lam = nice(rng, 550, 700, 10) if sub == "silicon" else nice(rng, 450, 650, 5)
        t1 = lam / (4 * nc)
        t2 = 3 * lam / (4 * nc)
        R0 = ((ns - 1) / (ns + 1)) ** 2
        Rc = ((ns - nc ** 2) / (ns + nc ** 2)) ** 2
        question = (
            f"A {use} made of {sub} ($n = {fmt(ns)}$) is given an anti-reflection coating of {coat} ({formula}, $n = {fmt(nc)}$). What "
            f"is the minimum coating thickness that minimizes reflection of {q(lam, 'nm')} light at normal incidence, and "
            "what is the next thickness that works? Estimate the reflectance at that wavelength with and without the "
            "coating."
        )
        steps = [
            f"Both reflections occur going into a higher index (air → coating since ${fmt(nc)} > 1$, coating → {sub} since "
            f"${fmt(ns)} > {fmt(nc)}$), so both waves get a half-wavelength shift; these cancel, and only the path difference "
            "$2n_ct$ matters.",
            "Destructive interference: $2n_ct = (m + \\tfrac12)\\lambda \\Rightarrow t = \\frac{(2m + 1)\\lambda}{4n_c}$.",
            f"Minimum (quarter-wave) thickness: $t = \\frac{{\\lambda}}{{4n_c}} = \\frac{{{lam}}}{{4({fmt(nc)})}} = {fmt(t1)}$ nm "
            f"— a quarter of the wavelength inside the coating, ${lam}/{fmt(nc)} = {fmt(lam / nc)}$ nm.",
            f"Next thickness ($m = 1$): $t = \\frac{{3\\lambda}}{{4n_c}} = {fmt(t2)}$ nm (thicker coatings work over a narrower "
            "band of wavelengths).",
            f"Uncoated reflectance at normal incidence: $R_0 = \\left(\\frac{{n_s - 1}}{{n_s + 1}}\\right)^2 = "
            f"\\left(\\frac{{{fmt(ns - 1)}}}{{{fmt(ns + 1)}}}\\right)^2 = {fmt(R0)}$ ({fmt(100 * R0)}%).",
            f"With a quarter-wave coating: $R = \\left(\\frac{{n_s - n_c^2}}{{n_s + n_c^2}}\\right)^2 = "
            f"\\left(\\frac{{{fmt(ns)} - {fmt(nc ** 2, 4)}}}{{{fmt(ns)} + {fmt(nc ** 2, 4)}}}\\right)^2 = {fmt(Rc)}$ "
            f"({fmt(100 * Rc)}%). Complete cancellation would need $n_c = \\sqrt{{n_s}} = {fmt(math.sqrt(ns))}$.",
        ]
        answer = (f"$t_{{min}} = {fmt(t1)}$ nm (next {fmt(t2)} nm); reflectance falls from {fmt(100 * R0)}% to "
                  f"{fmt(100 * Rc)}%")
        values = {"variant": "ar_coating", "n_c": nc, "n_s": ns, "lam_nm": lam, "t_min": t1, "t_next": t2,
                  "R_uncoated": R0, "R_coated": Rc}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


LASERS = [(405, "violet diode"), (450, "blue diode"), (473, "blue DPSS"), (532, "green"), (589, "sodium-yellow"),
          (633, "helium-neon"), (650, "red diode")]


@template("single_slit_diffraction_minima", PHYS, "Waves and Optics", "Diffraction", "medium")
def single_slit_diffraction_minima(rng):
    lam_nm, kind = pick(rng, LASERS)
    lam = lam_nm * 1e-9
    if rng.random() < 0.6:
        a_um = nice(rng, 10, 200, 5)
        L = nice(rng, 0.50, 4.00, 0.05)
        a = a_um * 1e-6
        th1 = math.asin(lam / a)
        th2 = math.asin(2 * lam / a)
        y1, y2 = L * math.tan(th1), L * math.tan(th2)
        W = 2 * y1
        question = (
            f"Light from a {kind} laser ($\\lambda = {lam_nm}$ nm) passes through a single slit {q(a_um, 'μm')} wide and "
            f"falls on a screen {q(L, 'm')} away. Find the angles of the first and second dark fringes, their distances "
            "from the center of the pattern, and the width of the central bright maximum."
        )
        steps = [
            "Dark fringes of single-slit diffraction satisfy $a\\sin\\theta = m\\lambda$ ($m = \\pm1, \\pm2, \\dots$): the slit "
            "can be split into pairs of strips whose wavelets cancel.",
            f"First minimum: $\\sin\\theta_1 = \\lambda/a = ({fmt(lam)})/({fmt(a)}) = {fmt(lam / a, 4)} \\Rightarrow "
            f"\\theta_1 = {_deg(math.degrees(th1), 4)}$.",
            f"Second minimum: $\\sin\\theta_2 = 2\\lambda/a = {fmt(2 * lam / a, 4)} \\Rightarrow \\theta_2 = "
            f"{_deg(math.degrees(th2), 4)}$.",
            f"Positions on the screen: $y = L\\tan\\theta$: $y_1 = ({fmt(L)})\\tan {_deg(math.degrees(th1), 4)} = "
            f"{fmt(y1 * 1000)}$ mm and $y_2 = {fmt(y2 * 1000)}$ mm.",
            f"The central maximum extends between the two first minima: width $W = 2y_1 = {fmt(W * 1000)}$ mm (small-angle "
            f"estimate $2\\lambda L/a = {fmt(2 * lam * L / a * 1000)}$ mm). The side maxima are about half as wide, "
            f"$y_2 - y_1 = {fmt((y2 - y1) * 1000)}$ mm.",
            "A narrower slit gives a wider pattern: diffraction spreading is inversely proportional to the aperture.",
        ]
        answer = (f"$\\theta_1 = {_deg(math.degrees(th1), 4)}$, $\\theta_2 = {_deg(math.degrees(th2), 4)}$; "
                  f"$y_1 = {fmt(y1 * 1000)}$ mm, $y_2 = {fmt(y2 * 1000)}$ mm; central maximum {q(W * 1000, 'mm')} wide")
        values = {"variant": "find_pattern", "lam_nm": lam_nm, "a_um": a_um, "L": L, "theta1_deg": math.degrees(th1),
                  "y1_mm": y1 * 1000, "y2_mm": y2 * 1000, "W_mm": W * 1000}
    else:
        W_mm = nice(rng, 2.0, 30.0, 0.5)
        L = nice(rng, 1.0, 4.0, 0.1)
        th1 = math.atan(W_mm / 2000 / L)
        a = lam / math.sin(th1)
        question = (
            f"A {kind} laser beam ($\\lambda = {lam_nm}$ nm) passes through a narrow slit. On a screen {q(L, 'm')} away the "
            f"central bright band of the diffraction pattern is {q(W_mm, 'mm')} wide (measured between the first dark fringes "
            "on either side). How wide is the slit?"
        )
        steps = [
            "The central maximum lies between the first minima, $a\\sin\\theta_1 = \\lambda$, on either side of the center.",
            f"Half-width on the screen: $y_1 = W/2 = {fmt(W_mm / 2)}$ mm, so $\\tan\\theta_1 = y_1/L = {fmt(W_mm / 2000 / L, 4)}$ "
            f"and $\\theta_1 = {_deg(math.degrees(th1), 4)}$.",
            f"Slit width: $a = \\frac{{\\lambda}}{{\\sin\\theta_1}} = \\frac{{{fmt(lam)}}}{{{fmt(math.sin(th1), 4)}}} = "
            f"{fmt(a)}$ m $= {fmt(a * 1e6)}$ μm.",
            f"Small-angle check: $a \\approx 2\\lambda L/W = {fmt(2 * lam * L / (W_mm / 1000) * 1e6)}$ μm ✓.",
        ]
        answer = f"$a = {fmt(a * 1e6)}$ μm"
        values = {"variant": "find_slit", "lam_nm": lam_nm, "L": L, "W_mm": W_mm, "theta1_deg": math.degrees(th1),
                  "a_um": a * 1e6}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("rayleigh_resolution_limit", PHYS, "Waves and Optics", "Resolving power", "easy")
def rayleigh_resolution_limit(rng):
    variant = pick(rng, ["eye", "moon", "satellite"])
    if variant == "eye":
        D_mm = nice(rng, 4.0, 7.0, 0.5)
        lam_nm = nice(rng, 500, 600, 10)
        s = nice(rng, 1.2, 1.8, 0.1)
        D = D_mm / 1000
        theta = 1.22 * lam_nm * 1e-9 / D
        L = s / theta
        question = (
            f"At night the pupil of a driver's eye has a diameter of {q(D_mm, 'mm')}. The headlights of an oncoming car are "
            f"{q(s, 'm')} apart. Taking $\\lambda = {lam_nm}$ nm and considering only diffraction at the pupil, find the "
            "eye's limiting angular resolution and the greatest distance at which the two headlights can be seen as separate."
        )
        steps = [
            "Rayleigh criterion for a circular aperture: two point sources are just resolved when "
            "$\\theta_{min} = 1.22\\lambda/D$.",
            f"$\\theta_{{min}} = \\frac{{1.22({fmt(lam_nm * 1e-9)})}}{{{fmt(D)}}} = {fmt(theta)}$ rad "
            f"$= {fmt(theta * 206265)}$ arcseconds.",
            f"The headlights subtend $s/L$, so they are resolved out to $L = \\frac{{s}}{{\\theta_{{min}}}} = "
            f"\\frac{{{fmt(s)}}}{{{fmt(theta)}}} = {fmt(L)}$ m $= {fmt(L / 1000)}$ km.",
            "In practice the retina and the eye's optical imperfections limit vision to about 1 arcminute "
            "($2.9\\times10^{-4}$ rad), so real eyes resolve the lights only at a shorter distance.",
        ]
        answer = f"$\\theta_{{min}} = {fmt(theta)}$ rad; $L_{{max}} = {fmt(L / 1000)}$ km"
        values = {"variant": variant, "lam_nm": lam_nm, "D": D, "s": s, "theta": theta, "L_max": L}
    elif variant == "moon":
        D = pick(rng, [nice(rng, 0.05, 1.00, 0.05), 2.4, 10.0])
        lam_nm = nice(rng, 400, 700, 10)
        theta = 1.22 * lam_nm * 1e-9 / D
        d_moon = 3.84e8
        s = theta * d_moon
        scope = ("the Hubble Space Telescope (mirror diameter 2.4 m)" if D == 2.4 else
                 "a 10.0 m Keck telescope (ignore atmospheric blurring)" if D == 10.0 else
                 f"a telescope with an objective {q(D * 100, 'cm')} in diameter")
        question = (
            f"What is the diffraction-limited angular resolution of {scope} at a wavelength of {q(lam_nm, 'nm')}? What is the "
            "smallest separation between two features on the Moon (distance $3.84\\times10^8$ m) that it could resolve?"
        )
        steps = [
            "Rayleigh criterion for a circular aperture: $\\theta_{min} = 1.22\\lambda/D$.",
            f"$\\theta_{{min}} = \\frac{{1.22({fmt(lam_nm * 1e-9)})}}{{{fmt(D)}}} = {fmt(theta)}$ rad "
            f"$= {fmt(theta * 206265)}$ arcseconds (1 rad = 206 265 arcseconds).",
            f"Smallest resolvable separation on the Moon: $s = \\theta_{{min}}d = ({fmt(theta)})(3.84\\times10^8) = {fmt(s)}$ m"
            + (f" $= {fmt(s / 1000)}$ km." if s >= 1000 else "."),
            "Larger apertures and shorter wavelengths give finer resolution; ground-based telescopes also need adaptive "
            "optics to beat atmospheric seeing (about 1 arcsecond).",
        ]
        answer = (f"$\\theta_{{min}} = {fmt(theta)}$ rad ({fmt(theta * 206265)} arcseconds); smallest lunar feature ≈ "
                  + (q(s / 1000, 'km') if s >= 1000 else q(s, 'm')))
        values = {"variant": variant, "lam_nm": lam_nm, "D": D, "theta": theta, "theta_arcsec": theta * 206265,
                  "s_min": s}
    else:
        h_km = nice(rng, 200, 800, 10)
        D = nice(rng, 0.5, 3.0, 0.1)
        lam_nm = nice(rng, 400, 700, 10)
        theta = 1.22 * lam_nm * 1e-9 / D
        s = theta * h_km * 1000
        question = (
            f"An Earth-observation satellite orbits {q(h_km, 'km')} above the ground and photographs it through a telescope whose "
            f"mirror is {q(D, 'm')} in diameter. Ignoring the atmosphere, what is the smallest separation of two objects on the ground "
            f"that it can resolve in light of wavelength {q(lam_nm, 'nm')}?"
        )
        steps = [
            "Rayleigh criterion for a circular aperture: $\\theta_{min} = 1.22\\lambda/D$.",
            f"$\\theta_{{min}} = \\frac{{1.22({fmt(lam_nm * 1e-9)})}}{{{fmt(D)}}} = {fmt(theta)}$ rad.",
            f"Ground resolution: $s = \\theta_{{min}}h = ({fmt(theta)})({fmt(h_km * 1000)}) = {fmt(s)}$ m "
            f"$= {fmt(s * 100)}$ cm.",
            "Atmospheric turbulence and detector pixel size usually make the real resolution somewhat worse.",
        ]
        answer = f"$\\theta_{{min}} = {fmt(theta)}$ rad; ground resolution ≈ {q(s * 100, 'cm')}"
        values = {"variant": variant, "lam_nm": lam_nm, "D": D, "h_km": h_km, "theta": theta, "s_min": s}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


NOTES = [("C3", 130.8), ("G3", 196.0), ("A3", 220.0), ("C4 (middle C)", 261.6), ("D4", 293.7), ("E4", 329.6),
         ("F4", 349.2), ("G4", 392.0), ("A4", 440.0), ("B4", 493.9), ("C5", 523.3)]


@template("air_column_pipe_resonance", PHYS, "Waves and Optics", "Standing waves", "easy")
def air_column_pipe_resonance(rng):
    kind = pick(rng, ["open", "closed"])
    T_C = nice(rng, 0, 35, 1)
    T = T_C + 273.15
    v = 331.3 * math.sqrt(T / 273.15)
    desc = "open at both ends" if kind == "open" else "closed at one end"
    speed_step = (f"Speed of sound in air at {T_C} °C: $v = 331.3\\sqrt{{T/273.15\\text{{ K}}}} = "
                  f"331.3\\sqrt{{{fmt(T, 5)}/273.15}} = {fmt(v, 4)}$ m/s.")
    if kind == "open":
        rule = ("An open end is a displacement antinode. With antinodes at both ends, $L = n\\lambda/2$, so "
                "$f_n = \\frac{nv}{2L}$ with $n = 1, 2, 3, \\dots$ (all harmonics).")
    else:
        rule = ("The closed end is a displacement node and the open end an antinode, so $L = n\\lambda/4$ with $n$ odd: "
                "$f_n = \\frac{nv}{4L}$, $n = 1, 3, 5, \\dots$ (odd harmonics only).")
    if rng.random() < 0.55:
        L = nice(rng, 0.20, 2.50, 0.01)
        ns = [1, 2, 3] if kind == "open" else [1, 3, 5]
        div = 2 if kind == "open" else 4
        freqs = [n * v / (div * L) for n in ns]
        question = (
            f"An organ pipe {q(L, 'm')} long is {desc}. The air temperature is {T_C} °C. Find the speed of sound, the "
            "wavelength of the fundamental and the frequencies of the three lowest resonances (neglect the end correction)."
        )
        steps = [
            speed_step,
            rule,
            f"Fundamental wavelength: $\\lambda_1 = {div}L = {div}({fmt(L)}) = {fmt(div * L)}$ m; "
            f"$f_1 = \\frac{{v}}{{{div}L}} = \\frac{{{fmt(v, 4)}}}{{{fmt(div * L)}}} = {fmt(freqs[0], 4)}$ Hz.",
            "The next resonances: " + _and(f"$f_{n} = {n}f_1 = {fmt(fr, 4)}$ Hz" for n, fr in zip(ns[1:], freqs[1:])) + ".",
            ("Because a closed pipe supports only odd harmonics, its tone sounds different (more hollow) from an open pipe of "
             "the same fundamental." if kind == "closed" else
             "A pipe of the same length closed at one end would have a fundamental an octave lower, $v/(4L)$."),
        ]
        answer = (f"$v = {fmt(v, 4)}$ m/s; $\\lambda_1 = {fmt(div * L)}$ m; resonances "
                  + ", ".join(f"{fmt(fr, 4)}" for fr in freqs) + " Hz")
        values = {"variant": "find_frequencies", "kind": kind, "L": L, "T_C": T_C, "v": v, "freqs": freqs}
    else:
        note, f1 = pick(rng, NOTES)
        div = 2 if kind == "open" else 4
        L = v / (div * f1)
        nxt = 2 if kind == "open" else 3
        question = (
            f"An organ builder needs a pipe {desc} whose fundamental is the note {note}, {q(f1, 'Hz', 4)}, when the air is at "
            f"{T_C} °C. How long must the pipe be (neglect the end correction), and what is the frequency of its next resonance?"
        )
        steps = [
            speed_step,
            rule,
            f"Fundamental: $f_1 = \\frac{{v}}{{{div}L}} \\Rightarrow L = \\frac{{v}}{{{div}f_1}} = "
            f"\\frac{{{fmt(v, 4)}}}{{{div}({fmt(f1, 4)})}} = {fmt(L, 4)}$ m.",
            f"Next resonance: $f_{nxt} = {nxt}f_1 = {fmt(nxt * f1, 4)}$ Hz.",
            "On a warmer day the speed of sound increases, so the pipe's pitch rises slightly (about 0.18% per °C).",
        ]
        answer = f"$L = {fmt(L, 4)}$ m; next resonance {q(nxt * f1, 'Hz', 4)}"
        values = {"variant": "find_length", "kind": kind, "f1": f1, "T_C": T_C, "v": v, "L": L, "f_next": nxt * f1}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("beat_frequency_tuning", PHYS, "Waves and Optics", "Beats", "easy")
def beat_frequency_tuning(rng):
    effect = pick(rng, ["decreases", "increases"])
    if rng.random() < 0.5:
        note, f_ref = pick(rng, NOTES[2:])
        fb = nice(rng, 0.5, 6.0, 0.5)
        T = nice(rng, 40, 900, 10)
        f_s = f_ref - fb if effect == "decreases" else f_ref + fb
        T_new = T * (f_ref / f_s) ** 2
        question = (
            f"A piano tuner sounds a {note} tuning fork ({q(f_ref, 'Hz', 4)}) together with the corresponding piano string and "
            f"hears {q(fb, 'beats/s', 2)}. When the string's tension is increased slightly, the beat frequency {effect}. "
            f"What was the string's frequency, and to what tension must the string be set to be in tune if its present tension "
            f"is {q(T, 'N')}?"
        )
        steps = [
            "Two tones of nearby frequency produce beats at $f_{beat} = |f_1 - f_2|$, so the string is at "
            f"${fmt(f_ref, 4)} \\pm {fmt(fb, 2)}$ Hz.",
            "Raising the tension raises the string's frequency ($f \\propto \\sqrt{T}$). "
            + ("The beats slow down, so the string was moving toward the fork: it was flat."
               if effect == "decreases" else "The beats speed up, so the string was moving away from the fork: it was sharp."),
            f"String frequency: $f_s = {fmt(f_ref, 4)} {'-' if effect == 'decreases' else '+'} {fmt(fb, 2)} = {fmt(f_s, 4)}$ Hz.",
            f"Since $f \\propto \\sqrt{{T}}$, $T_{{new}} = T\\left(\\frac{{f_{{ref}}}}{{f_s}}\\right)^2 = "
            f"{T}\\left(\\frac{{{fmt(f_ref, 4)}}}{{{fmt(f_s, 4)}}}\\right)^2 = {fmt(T_new, 4)}$ N, "
            f"a change of {fmt(100 * (T_new / T - 1), 2)}%.",
        ]
        answer = f"$f_s = {fmt(f_s, 4)}$ Hz; required tension {q(T_new, 'N', 4)}"
        values = {"variant": "string", "f_ref": f_ref, "f_beat": fb, "effect": effect, "f_string": f_s, "T": T,
                  "T_new": T_new}
    else:
        fA = nice(rng, 250, 520, 1)
        fb = nice(rng, 1, 8, 1)
        fB = fA - fb if effect == "increases" else fA + fb
        question = (
            f"Tuning fork A has a frequency of {q(fA, 'Hz')}. When it is sounded together with fork B, {fb} beats per second "
            f"are heard. After a small piece of wax is stuck to a prong of fork B, the beat frequency {effect}. What is the "
            "frequency of fork B (before the wax was added), and what is the time between successive beats?"
        )
        steps = [
            f"The beat frequency is $|f_A - f_B| = {fb}$ Hz, so $f_B = {fA} \\pm {fb}$ Hz, i.e. {fA - fb} Hz or {fA + fb} Hz.",
            "Adding wax increases the vibrating mass, which lowers fork B's frequency.",
            ("Lowering $f_B$ makes the beats faster, so $f_B$ was already below $f_A$ and moves further away."
             if effect == "increases" else
             "Lowering $f_B$ makes the beats slower, so $f_B$ was above $f_A$ and moves closer to it."),
            f"Therefore $f_B = {fB}$ Hz.",
            f"Time between beats: $T_{{beat}} = 1/f_{{beat}} = 1/{fb} = {fmt(1 / fb)}$ s.",
        ]
        answer = f"$f_B = {fB}$ Hz; beats every {q(1 / fb, 's')}"
        values = {"variant": "forks", "f_A": fA, "f_beat": fb, "effect": effect, "f_B": fB, "beat_period": 1 / fb}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Quantum and atomic physics
# ---------------------------------------------------------------------------

PHOTON_SOURCES = [("molybdenum Kα X-rays", 17.48), ("silver Kα X-rays", 22.16), ("tungsten Kα X-rays", 59.32),
                  ("americium-241 gamma rays", 59.54), ("technetium-99m gamma rays", 140.5),
                  ("positron-annihilation photons", 511.0), ("cesium-137 gamma rays", 661.7),
                  ("cobalt-60 gamma rays", 1332.5)]


@template("compton_scattering_shift", PHYS, "Quantum Mechanics", "Compton effect", "medium")
def compton_scattering_shift(rng):
    theta = nice(rng, 15, 180, 5)
    if rng.random() < 0.5:
        src, E = pick(rng, PHOTON_SOURCES)
        lam = HC_KEV_PM / E
        given_energy = True
        incident = f"{src} with photon energy ${_exact(E)}$ keV"
    else:
        lam = nice(rng, 5.0, 100.0, 0.5)
        E = HC_KEV_PM / lam
        given_energy = False
        incident = f"X-ray photons of wavelength {q(lam, 'pm')}"
    lamC = LAMBDA_C * 1e12
    dlam = lamC * (1 - math.cos(math.radians(theta)))
    lam2 = lam + dlam
    E2 = HC_KEV_PM / lam2
    K = E - E2
    if theta == 180:
        phi = 0.0
    else:
        phi = math.degrees(math.atan(1 / ((1 + E / ME_C2_KEV) * math.tan(math.radians(theta / 2)))))
    question = (
        f"In a Compton-scattering experiment, {incident} scatter from essentially free electrons at rest. For photons "
        f"scattered through ${theta}^\\circ$, find the wavelength shift, the scattered wavelength and photon energy, the "
        "kinetic energy of the recoil electron and the direction in which it recoils."
    )
    steps = []
    if given_energy:
        steps.append(f"Incident wavelength: $\\lambda = hc/E = \\frac{{{fmt(HC_KEV_PM, 6)}\\text{{ keV·pm}}}}{{{_exact(E)}\\text{{ keV}}}} "
                     f"= {fmt(lam, 4)}$ pm.")
    else:
        steps.append(f"Incident photon energy: $E = hc/\\lambda = \\frac{{{fmt(HC_KEV_PM, 6)}\\text{{ keV·pm}}}}{{{fmt(lam)}\\text{{ pm}}}} "
                     f"= {fmt(E, 4)}$ keV.")
    steps += [
        f"Compton wavelength of the electron: $\\lambda_C = \\frac{{h}}{{m_ec}} = \\frac{{6.626\\times10^{{-34}}}}"
        f"{{(9.109\\times10^{{-31}})(2.998\\times10^8)}} = {fmt(lamC, 4)}$ pm.",
        f"Shift (from energy and momentum conservation): $\\Delta\\lambda = \\lambda_C(1 - \\cos\\theta) = "
        f"{fmt(lamC, 4)}(1 - \\cos {theta}^\\circ) = {fmt(dlam, 4)}$ pm.",
        f"Scattered wavelength: $\\lambda' = {fmt(lam, 4)} + {fmt(dlam, 4)} = {fmt(lam2, 4)}$ pm, so "
        f"$E' = hc/\\lambda' = {fmt(E2, 4)}$ keV.",
        f"Electron kinetic energy (energy conservation): $K = E - E' = {fmt(E, 4)} - {fmt(E2, 4)} = {fmt(K, 4)}$ keV, "
        f"{fmt(100 * K / E)}% of the photon's energy.",
        (f"Recoil direction: $\\cot\\phi = \\left(1 + \\frac{{E}}{{m_ec^2}}\\right)\\tan\\frac{{\\theta}}{{2}}$ with "
         f"$m_ec^2 = {fmt(ME_C2_KEV, 4)}$ keV gives $\\phi = {_deg(phi)}$ from the incident direction, on the opposite side "
         "to the scattered photon." if theta != 180 else
         "Recoil direction: for back-scattering ($\\theta = 180^\\circ$) the electron recoils straight forward, $\\phi = 0^\\circ$, "
         "and receives the maximum possible energy."),
    ]
    answer = (f"$\\Delta\\lambda = {fmt(dlam, 4)}$ pm; $\\lambda' = {fmt(lam2, 4)}$ pm; $E' = {fmt(E2, 4)}$ keV; "
              f"$K_e = {fmt(K, 4)}$ keV at $\\phi = {_deg(phi)}$")
    return {
        "question": question,
        "steps": steps,
        "answer": answer,
        "values": {"given_energy": given_energy, "E_keV": E, "lam_pm": lam, "theta_deg": theta, "dlam_pm": dlam,
                   "lam2_pm": lam2, "E2_keV": E2, "K_keV": K, "phi_deg": phi},
    }


IONS = [("He⁺", "helium", 2), ("He⁺", "helium", 2), ("Li²⁺", "lithium", 3), ("Be³⁺", "beryllium", 4),
        ("B⁴⁺", "boron", 5), ("C⁵⁺", "carbon", 6)]


@template("hydrogen_like_ion_levels", PHYS, "Quantum Mechanics", "Atomic structure", "medium")
def hydrogen_like_ion_levels(rng):
    ion, element, Z = pick(rng, IONS)
    n_lo = rng.randint(1, 4)
    n_hi = n_lo + rng.randint(1, 5)
    absorb = rng.random() < 0.35
    E_hi = -13.6 * Z ** 2 / n_hi ** 2
    E_lo = -13.6 * Z ** 2 / n_lo ** 2
    dE = E_hi - E_lo
    lam = 1240 / dE
    E_ion = 13.6 * Z ** 2
    r_hi = A0_NM * n_hi ** 2 / Z
    action = (f"absorbs a photon and jumps from the $n = {n_lo}$ level to the $n = {n_hi}$ level" if absorb else
              f"drops from the $n = {n_hi}$ level to the $n = {n_lo}$ level, emitting a photon")
    question = (
        f"The electron in a hydrogen-like {element} ion, {ion} ($Z = {Z}$), {action}. Using the Bohr model "
        "($E_n = -13.6\\,Z^2/n^2$ eV; ignore the reduced-mass correction), find the energies of the two levels, the photon's "
        f"energy and wavelength, the ionization energy of the ion in its ground state and the radius of the $n = {n_hi}$ orbit."
    )
    steps = [
        "A one-electron ion with nuclear charge $Ze$ has energies $Z^2$ times those of hydrogen, $E_n = -13.6Z^2/n^2$ eV, and "
        "orbit radii $r_n = a_0n^2/Z$ with $a_0 = 0.0529$ nm.",
        f"$E_{{{n_hi}}} = -13.6({Z})^2/{n_hi}^2 = {fmt(E_hi, 4)}$ eV and $E_{{{n_lo}}} = -13.6({Z})^2/{n_lo}^2 = {fmt(E_lo, 4)}$ eV.",
        f"Photon energy: $\\Delta E = E_{{{n_hi}}} - E_{{{n_lo}}} = 13.6({Z})^2\\left(\\frac{{1}}{{{n_lo}^2}} - "
        f"\\frac{{1}}{{{n_hi}^2}}\\right) = {fmt(dE, 4)}$ eV.",
        f"Wavelength: $\\lambda = hc/\\Delta E = 1240/{fmt(dE, 4)} = {fmt(lam, 4)}$ nm ({_region(lam)}).",
        f"Ionization energy from the ground state: $E_{{ion}} = 13.6Z^2 = 13.6({Z})^2 = {fmt(E_ion, 4)}$ eV, "
        f"{Z ** 2} times that of hydrogen.",
        f"Orbit radius: $r_{{{n_hi}}} = a_0\\frac{{n^2}}{{Z}} = 0.0529\\times\\frac{{{n_hi}^2}}{{{Z}}} = {fmt(r_hi, 4)}$ nm.",
    ]
    if Z == 2 and n_lo % 2 == 0 and n_hi % 2 == 0:
        steps.append(f"Because $E \\propto Z^2/n^2$, this He⁺ line has the same wavelength as the hydrogen transition "
                     f"$n = {n_hi // 2} \\to {n_lo // 2}$ (this coincidence confused early spectroscopists; the Pickering series).")
    answer = (f"$E_{{{n_hi}}} = {fmt(E_hi, 4)}$ eV, $E_{{{n_lo}}} = {fmt(E_lo, 4)}$ eV; photon {fmt(dE, 4)} eV, "
              f"$\\lambda = {fmt(lam, 4)}$ nm; $E_{{ion}} = {fmt(E_ion, 4)}$ eV; $r_{{{n_hi}}} = {fmt(r_hi, 4)}$ nm")
    return {
        "question": question,
        "steps": steps,
        "answer": answer,
        "values": {"Z": Z, "n_upper": n_hi, "n_lower": n_lo, "absorption": absorb, "E_upper_eV": E_hi,
                   "E_lower_eV": E_lo, "dE_eV": dE, "lambda_nm": lam, "E_ion_eV": E_ion, "r_upper_nm": r_hi},
    }


# ---------------------------------------------------------------------------
# Relativity
# ---------------------------------------------------------------------------


@template("relativistic_velocity_addition", PHYS, "Relativity", "Velocity addition", "medium")
def relativistic_velocity_addition(rng):
    if rng.random() < 0.6:
        u = nice(rng, 0.10, 0.95, 0.05)
        vp = nice(rng, 0.10, 0.95, 0.05)
        s = pick(rng, [1, 1, -1])
        v = (u + s * vp) / (1 + s * u * vp)
        galilean = u + s * vp
        obj = pick(rng, ["a probe", "a small shuttle", "a beam of particles", "a missile"])
        question = (
            f"A spaceship moves away from Earth at ${fmt(u, 2)}c$. It launches {obj} that moves at ${fmt(vp, 2)}c$ relative to "
            f"the ship, directed {'forward (away from Earth)' if s > 0 else 'backward (toward Earth)'}. What is the velocity "
            "of the launched object relative to Earth? Compare with the Galilean prediction."
        )
        sv = fmt(s * vp, 2)
        gs = _exact(round(galilean, 2))
        if galilean > 1:
            compare = ", faster than light — impossible."
        elif abs(v) < abs(galilean):
            compare = "; the relativistic result is smaller in magnitude."
        elif abs(v) > abs(galilean):
            compare = ("; here the relativistic result is slightly larger, because for opposite velocities the denominator "
                       "$1 + uv'/c^2$ is less than 1.")
        else:
            compare = "; the two agree in this special case."
        if v > 0:
            where = f"The object moves away from Earth at {q(v * C, 'm/s')}."
        elif v < 0:
            where = f"The object moves toward Earth at {q(-v * C, 'm/s')}."
        else:
            where = "The object is at rest relative to Earth."
        steps = [
            "Relativistic velocity addition (all motion along one line, away from Earth taken as positive): "
            "$v = \\frac{u + v'}{1 + uv'/c^2}$.",
            f"Here $u = {fmt(u, 2)}c$ and $v' = {sv}c$: $v = \\frac{{{fmt(u, 2)} + ({sv})}}{{1 + ({fmt(u, 2)})({sv})}}c = "
            f"\\frac{{{gs}}}{{{fmt(1 + s * u * vp, 4)}}}c = {fmt(v, 4)}c$.",
            f"Galilean addition would give $u + v' = {gs}c$" + compare,
            where + " Check: if $v' = c$ the formula gives exactly $c$, as the invariance of the speed of light requires.",
        ]
        direction = "away from Earth" if v > 0 else ("toward Earth" if v < 0 else "at rest relative to Earth")
        answer = f"$v = {fmt(v, 4)}c$ ({direction}); Galilean estimate ${gs}c$"
        values = {"variant": "launch", "u": u, "v_rel": vp, "direction": s, "v": v, "v_galilean": galilean}
    else:
        a = nice(rng, 0.10, 0.95, 0.05)
        b = nice(rng, 0.10, 0.95, 0.05)
        v = (a + b) / (1 + a * b)
        gamma = 1 / math.sqrt(1 - v ** 2)
        question = (
            f"Two spacecraft approach each other head-on. Observers on Earth measure their speeds as ${fmt(a, 2)}c$ and "
            f"${fmt(b, 2)}c$. How fast does each ship see the other approaching, and what Lorentz factor does each crew "
            "assign to the other ship?"
        )
        steps = [
            "Work in the rest frame of the first ship (speed $a$ relative to Earth). In that frame Earth recedes at $a$, and the "
            "second ship moves toward it at $b$ relative to Earth, so combining the two velocities relativistically gives "
            "$v = \\frac{a + b}{1 + ab/c^2}$.",
            f"$v = \\frac{{{fmt(a, 2)} + {fmt(b, 2)}}}{{1 + ({fmt(a, 2)})({fmt(b, 2)})}}c = "
            f"\\frac{{{_exact(round(a + b, 2))}}}{{{fmt(1 + a * b, 4)}}}c = {fmt(v, 4)}c$.",
            f"Lorentz factor: $\\gamma = 1/\\sqrt{{1 - v^2/c^2}} = {fmt(gamma, 4)}$.",
            f"Galilean addition would give ${_exact(round(a + b, 2))}c$" + (", exceeding $c$." if a + b > 1 else ".")
            + " The relative speed is always below $c$.",
        ]
        answer = f"$v = {fmt(v, 4)}c$; $\\gamma = {fmt(gamma, 4)}$"
        values = {"variant": "approach", "a": a, "b": b, "v": v, "gamma": gamma}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


SPECTRAL_LINES = [("hydrogen-alpha (Hα)", 656.3), ("hydrogen-beta (Hβ)", 486.1), ("Lyman-alpha", 121.6),
                  ("calcium K", 393.4), ("[O III]", 500.7), ("magnesium II", 279.8)]


@template("relativistic_doppler_redshift", PHYS, "Relativity", "Relativistic Doppler effect", "medium")
def relativistic_doppler_redshift(rng):
    line, lam0 = pick(rng, SPECTRAL_LINES)
    if rng.random() < 0.5:
        beta = nice(rng, 0.02, 0.90, 0.01)
        receding = rng.random() < 0.6
        factor = math.sqrt((1 + beta) / (1 - beta)) if receding else math.sqrt((1 - beta) / (1 + beta))
        lam = lam0 * factor
        z = lam / lam0 - 1
        classical = lam0 * (1 + beta) if receding else lam0 * (1 - beta)
        question = (
            f"A source (for example a jet of gas ejected from an active galaxy) moves directly "
            f"{'away from' if receding else 'toward'} Earth at ${fmt(beta, 2)}c$ and emits the {line} line, whose rest "
            f"wavelength is {q(lam0, 'nm', 4)}. At what wavelength is the line observed, and what is the redshift $z$? "
            "Compare with the non-relativistic Doppler formula."
        )
        frac = "\\frac{1 + \\beta}{1 - \\beta}" if receding else "\\frac{1 - \\beta}{1 + \\beta}"
        num, den = (1 + beta, 1 - beta) if receding else (1 - beta, 1 + beta)
        steps = [
            f"Relativistic Doppler shift for motion along the line of sight: $\\lambda_{{obs}} = \\lambda_0\\sqrt{{{frac}}}$ "
            "(it combines the classical change in wave spacing with time dilation of the source).",
            f"$\\lambda_{{obs}} = {fmt(lam0, 4)}\\sqrt{{\\frac{{{fmt(num, 3)}}}{{{fmt(den, 3)}}}}} = {fmt(lam0, 4)}"
            f"\\times{fmt(factor, 4)} = {fmt(lam, 4)}$ nm ({_region(lam)}).",
            f"$z = \\frac{{\\lambda_{{obs}} - \\lambda_0}}{{\\lambda_0}} = {fmt(z, 4)}$"
            + (" (negative: a blueshift)." if not receding else "."),
            f"Non-relativistic estimate $\\lambda_0(1 {'+' if receding else '-'} \\beta) = {fmt(classical, 4)}$ nm; the "
            f"difference of {fmt(abs(lam - classical), 3)} nm shows the relativistic correction, which grows rapidly with speed.",
        ]
        answer = f"$\\lambda_{{obs}} = {fmt(lam, 4)}$ nm; $z = {fmt(z, 4)}$"
        values = {"variant": "find_wavelength", "lam0": lam0, "beta": beta, "receding": receding, "lam_obs": lam, "z": z}
    else:
        b_true = nice(rng, 0.02, 0.90, 0.01) * pick(rng, [1, 1, -1])
        lam = sig(lam0 * math.sqrt((1 + b_true) / (1 - b_true)), 4)
        r = lam / lam0
        beta_s = (r ** 2 - 1) / (r ** 2 + 1)
        receding = beta_s > 0
        z = r - 1
        question = (
            f"The {line} line (rest wavelength {q(lam0, 'nm', 4)}) in the spectrum of a distant object is observed at "
            f"{q(lam, 'nm', 4)}. Assuming the shift is due entirely to motion along the line of sight, find the redshift $z$ "
            "and the object's speed, and say whether it is approaching or receding."
        )
        steps = [
            f"$z = \\frac{{\\lambda_{{obs}} - \\lambda_0}}{{\\lambda_0}} = \\frac{{{fmt(lam, 4)} - {fmt(lam0, 4)}}}{{{fmt(lam0, 4)}}} = "
            f"{fmt(z, 4)}$" + (" (a redshift)." if receding else " (a blueshift)."),
            "Invert the relativistic Doppler formula $\\frac{\\lambda_{obs}}{\\lambda_0} = \\sqrt{\\frac{1 + \\beta}{1 - \\beta}}$ "
            "(with $\\beta > 0$ for recession): $\\beta = \\frac{(\\lambda_{obs}/\\lambda_0)^2 - 1}{(\\lambda_{obs}/\\lambda_0)^2 + 1}$.",
            f"$\\lambda_{{obs}}/\\lambda_0 = {fmt(r, 5)}$, so $\\beta = \\frac{{{fmt(r ** 2, 5)} - 1}}{{{fmt(r ** 2, 5)} + 1}} = "
            f"{fmt(beta_s, 4)}$.",
            f"The object is {'receding' if receding else 'approaching'} at ${fmt(abs(beta_s), 4)}c = {fmt(abs(beta_s) * C)}$ m/s"
            + (f"; the naive estimate $v \\approx zc$ would give ${fmt(abs(z), 4)}c$." if abs(z) > 0 else "."),
        ]
        if z > 0.1:
            steps.append("Caveat: the large redshifts of distant galaxies and quasars are mostly caused by the expansion of the "
                         "universe, so this special-relativistic speed is a formal interpretation rather than a true velocity.")
        answer = f"$z = {fmt(z, 4)}$; speed ${fmt(abs(beta_s), 4)}c$ ({'receding' if receding else 'approaching'})"
        values = {"variant": "find_speed", "lam0": lam0, "lam_obs": lam, "z": z, "beta": abs(beta_s), "receding": receding}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("muon_time_dilation_survival", PHYS, "Relativity", "Time dilation", "hard")
def muon_time_dilation_survival(rng):
    h_km = nice(rng, 5.0, 20.0, 0.5)
    N0 = nice(rng, 1000, 100000, 1000)
    values = {}
    if rng.random() < 0.5:
        beta = nice(rng, 0.980, 0.999, 0.001)
        gamma = 1 / math.sqrt(1 - beta ** 2)
        beta_txt = fmt(beta, 3)
        speed = f"at ${beta_txt}c$"
        steps = [f"Lorentz factor: $\\gamma = \\frac{{1}}{{\\sqrt{{1 - \\beta^2}}}} = \\frac{{1}}{{\\sqrt{{1 - {fmt(beta, 3)}^2}}}} = "
                 f"{fmt(gamma, 4)}$."]
    else:
        E_GeV = nice(rng, 0.5, 10.0, 0.1)
        gamma = E_GeV * 1000 / MUON_MC2_MEV
        beta = math.sqrt(1 - 1 / gamma ** 2)
        beta_txt = fmt(beta, 6)
        speed = f"with a total energy of {q(E_GeV, 'GeV')} (muon rest energy 105.66 MeV)"
        steps = [f"Lorentz factor from the energy: $\\gamma = \\frac{{E}}{{mc^2}} = \\frac{{{fmt(E_GeV * 1000, 4)}}}{{105.66}} = "
                 f"{fmt(gamma, 4)}$, so $\\beta = \\sqrt{{1 - 1/\\gamma^2}} = {beta_txt}$."]
        values["E_GeV"] = E_GeV
    h = h_km * 1000
    t_lab = h / (beta * C)
    t0 = t_lab / gamma
    N = N0 * math.exp(-t0 / TAU_MUON)
    N_cl = N0 * math.exp(-t_lab / TAU_MUON)
    question = (
        f"Muons are produced {q(h_km, 'km')} above sea level and travel straight down {speed}. Their mean lifetime at rest is "
        f"2.197 μs. Of {N0} muons that start down together, how many are expected to reach sea level? Ignore energy loss in "
        "the air and compare with the prediction that ignores time dilation."
    )
    steps += [
        f"Earth-frame travel time: $t = \\frac{{h}}{{\\beta c}} = \\frac{{{fmt(h)}}}{{({beta_txt})(2.998\\times10^8)}} = "
        f"{fmt(t_lab * 1e6)}$ μs, about ${fmt(t_lab / TAU_MUON)}$ mean lifetimes.",
        f"The muons' own clocks run slow, so the proper time elapsed is $t_0 = t/\\gamma = {fmt(t_lab * 1e6)}/{fmt(gamma, 4)} = "
        f"{fmt(t0 * 1e6)}$ μs.",
        f"Survivors: $N = N_0e^{{-t_0/\\tau}} = {N0}\\,e^{{-{fmt(t0 / TAU_MUON)}}} = {fmt(N)}$.",
        f"Without time dilation: $N_0e^{{-t/\\tau}} = {N0}\\,e^{{-{fmt(t_lab / TAU_MUON)}}} = {fmt(N_cl)}$ — far fewer. The "
        "large muon flux observed at sea level is direct evidence for time dilation.",
        f"Muon-frame view: the atmosphere is length-contracted to $h/\\gamma = {fmt(h / gamma / 1000)}$ km, crossed in "
        f"$\\frac{{h/\\gamma}}{{\\beta c}} = {fmt(t0 * 1e6)}$ μs — the same proper time, so both frames agree ✓.",
    ]
    answer = (f"about ${fmt(N)}$ muons reach sea level ($\\gamma = {fmt(gamma, 4)}$, $t_0 = {fmt(t0 * 1e6)}$ μs); "
              f"without time dilation only ${fmt(N_cl)}$")
    values.update({"h_km": h_km, "N0": N0, "beta": beta, "gamma": gamma, "t_lab": t_lab, "t_proper": t0, "N_sea": N,
                   "N_classical": N_cl})
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Nuclear physics
# ---------------------------------------------------------------------------

NUCLIDES = {  # key: (LaTeX symbol, atomic mass in u, name)
    "n": ("{}^{1}_{0}n", 1.008665, "neutron"),
    "p": ("{}^{1}_{1}\\text{H}", 1.007825, "proton"),
    "d": ("{}^{2}_{1}\\text{H}", 2.014102, "deuteron"),
    "t": ("{}^{3}_{1}\\text{H}", 3.016049, "triton"),
    "He3": ("{}^{3}_{2}\\text{He}", 3.016029, "helium-3"),
    "He4": ("{}^{4}_{2}\\text{He}", 4.002603, "alpha particle"),
    "Li6": ("{}^{6}_{3}\\text{Li}", 6.015123, "lithium-6"),
    "Li7": ("{}^{7}_{3}\\text{Li}", 7.016003, "lithium-7"),
    "Be7": ("{}^{7}_{4}\\text{Be}", 7.016929, "beryllium-7"),
    "Be9": ("{}^{9}_{4}\\text{Be}", 9.012183, "beryllium-9"),
    "B10": ("{}^{10}_{5}\\text{B}", 10.012937, "boron-10"),
    "C12": ("{}^{12}_{6}\\text{C}", 12.000000, "carbon-12"),
    "C13": ("{}^{13}_{6}\\text{C}", 13.003355, "carbon-13"),
    "N14": ("{}^{14}_{7}\\text{N}", 14.003074, "nitrogen-14"),
    "O17": ("{}^{17}_{8}\\text{O}", 16.999132, "oxygen-17"),
    "Al27": ("{}^{27}_{13}\\text{Al}", 26.981538, "aluminum-27"),
    "P30": ("{}^{30}_{15}\\text{P}", 29.978313, "phosphorus-30"),
}

# id, reactants, products, kind, context. For "beam" reactions the reactants are (target, projectile).
REACTIONS = [
    ("d+t->He4+n", ("d", "t"), ("He4", "n"), "fusion", "deuterium–tritium fusion, the reaction planned for tokamaks such as ITER"),
    ("d+d->He3+n", ("d", "d"), ("He3", "n"), "fusion", "one of the two branches of deuterium–deuterium fusion"),
    ("d+d->t+p", ("d", "d"), ("t", "p"), "fusion", "one of the two branches of deuterium–deuterium fusion"),
    ("d+He3->He4+p", ("d", "He3"), ("He4", "p"), "fusion", "deuterium–helium-3 fusion, a candidate low-neutron fuel cycle"),
    ("Li6+n->He4+t", ("Li6", "n"), ("He4", "t"), "capture", "the tritium-breeding reaction in a fusion-reactor blanket"),
    ("B10+n->Li7+He4", ("B10", "n"), ("Li7", "He4"), "capture", "the reaction used in boron neutron capture therapy and boron-lined neutron detectors"),
    ("He3+n->t+p", ("He3", "n"), ("t", "p"), "capture", "the reaction used in helium-3 neutron detectors"),
    ("Li7+p->He4+He4", ("Li7", "p"), ("He4", "He4"), "beam", "the reaction Cockcroft and Walton used in 1932 to split the nucleus with accelerated protons"),
    ("Be9+He4->C12+n", ("Be9", "He4"), ("C12", "n"), "beam", "the reaction in which Chadwick discovered the neutron in 1932"),
    ("C12+d->C13+p", ("C12", "d"), ("C13", "p"), "beam", "a deuteron-stripping reaction studied with accelerators"),
    ("N14+He4->O17+p", ("N14", "He4"), ("O17", "p"), "beam", "Rutherford's first artificial transmutation (1919)"),
    ("Al27+He4->P30+n", ("Al27", "He4"), ("P30", "n"), "beam", "the reaction in which the Joliot-Curies made the first artificial radioisotope (1934)"),
    ("Li7+p->Be7+n", ("Li7", "p"), ("Be7", "n"), "beam", "a common accelerator-based neutron source"),
    ("t+p->He3+n", ("t", "p"), ("He3", "n"), "beam", "a reaction used to produce nearly monoenergetic neutrons"),
]


@template("nuclear_reaction_q_value", PHYS, "Nuclear Physics", "Nuclear reactions", "hard")
def nuclear_reaction_q_value(rng):
    rid, react, prod, kind, context = pick(rng, REACTIONS)
    m_in = [NUCLIDES[k][1] for k in react]
    m_out = [NUCLIDES[k][1] for k in prod]
    M_in, M_out = sum(m_in), sum(m_out)
    dm = M_in - M_out
    Q = dm * U_MEV
    eq = " + ".join(NUCLIDES[k][0] for k in react) + " \\rightarrow " + " + ".join(NUCLIDES[k][0] for k in prod)
    masses = "; ".join(f"${NUCLIDES[k][0]}$: {_fixed(NUCLIDES[k][1], 6)} u" for k in dict.fromkeys(react + prod))
    steps = [
        "$Q = (\\sum m_{initial} - \\sum m_{final})c^2$. Atomic masses can be used because the number of electrons is the same "
        "on both sides (charge is conserved); $1$ u $= 931.494$ MeV/$c^2$.",
        f"Initial mass: ${' + '.join(_fixed(m, 6) for m in m_in)} = {_fixed(M_in, 6)}$ u; final mass: "
        f"${' + '.join(_fixed(m, 6) for m in m_out)} = {_fixed(M_out, 6)}$ u.",
        f"$\\Delta m = {_fixed(M_in, 6)} - {_fixed(M_out, 6)} = {fmt(dm, 4)}$ u, so $Q = ({fmt(dm, 4)})(931.494) = {fmt(Q, 4)}$ MeV — "
        + ("energy is released (exothermic)." if Q > 0 else "energy must be supplied (endothermic)."),
    ]
    values = {"reaction": rid, "kind": kind, "M_initial_u": M_in, "M_final_u": M_out, "dm_u": dm, "Q_MeV": Q}
    if kind in ("fusion", "capture"):
        a, b = prod
        ma, mb = NUCLIDES[a][1], NUCLIDES[b][1]
        Ka, Kb = Q * mb / (ma + mb), Q * ma / (ma + mb)
        m_mg = nice(rng, 1, 1000, 1)
        if kind == "fusion":
            M_fuel = M_in
            fuel = "fuel (in the proportions of the reaction)"
            note = "the reactants' kinetic energies (tens of keV in a hot plasma) are negligible compared with $Q$"
            count_step = (f"Each reaction consumes ${_fixed(M_in, 6)}$ u of fuel, i.e. ${_fixed(M_in, 6)}$ g per mole of "
                          f"reactions: $N = \\frac{{{fmt(m_mg / 1000)}\\text{{ g}}}}{{{_fixed(M_in, 6)}\\text{{ g/mol}}}}(6.022\\times10^{{23}})")
        else:
            M_fuel = NUCLIDES[react[0]][1]
            fuel = NUCLIDES[react[0]][2]
            note = "the captured neutrons are thermal (about 0.025 eV), so the reactants are effectively at rest"
            count_step = (f"Each reaction consumes one {fuel} nucleus: $N = \\frac{{{fmt(m_mg / 1000)}\\text{{ g}}}}"
                          f"{{{_fixed(M_fuel, 6)}\\text{{ g/mol}}}}(6.022\\times10^{{23}})")
        N = m_mg / 1000 / M_fuel * N_A
        E = N * Q * MEV_J
        question = (
            f"The reaction ${eq}$ is {context}. Using the atomic masses {masses}, find the $Q$-value. Taking the reactants to "
            f"be at rest, how is this energy shared between the two products? How much energy is released if {q(m_mg, 'mg')} "
            f"of {fuel} reacts completely?"
        )
        same = a == b
        steps += [
            f"Sharing: {note}. The total momentum is therefore zero, and the two products fly apart with equal and opposite "
            "momenta. Since $K = p^2/2m$, the lighter product takes the larger share: $K_a = Q\\frac{m_b}{m_a + m_b}$.",
            (f"Both products are identical, so each gets $Q/2 = {fmt(Ka, 4)}$ MeV." if same else
             f"${NUCLIDES[a][0]}$: $K = {fmt(Q, 4)}\\times\\frac{{{_fixed(mb, 6)}}}{{{_fixed(ma + mb, 6)}}} = {fmt(Ka, 4)}$ MeV; "
             f"${NUCLIDES[b][0]}$: $K = {fmt(Q, 4)}\\times\\frac{{{_fixed(ma, 6)}}}{{{_fixed(ma + mb, 6)}}} = {fmt(Kb, 4)}$ MeV."),
            count_step + f" = {fmt(N)}$ reactions.",
            f"Energy released: $E = NQ = ({fmt(N)})({fmt(Q, 4)}\\text{{ MeV}})(1.602\\times10^{{-13}}\\text{{ J/MeV}}) = {fmt(E)}$ J "
            f"$= {fmt(E / 3.6e6)}$ kWh.",
        ]
        answer = (f"$Q = {fmt(Q, 4)}$ MeV; ${NUCLIDES[a][0]}$ gets {fmt(Ka, 4)} MeV and ${NUCLIDES[b][0]}$ gets "
                  f"{fmt(Kb, 4)} MeV; {q(m_mg, 'mg')} releases {q(E, 'J')}")
        values.update({"K_a_MeV": Ka, "K_b_MeV": Kb, "m_mg": m_mg, "N_reactions": N, "E_J": E})
    else:
        target, proj = react
        m_t, m_p = NUCLIDES[target][1], NUCLIDES[proj][1]
        pname = NUCLIDES[proj][2]
        if Q > 0:
            K = nice(rng, 0.3, 6.0, 0.1)
            Kout = K + Q
            question = (
                f"The reaction ${eq}$ is {context}. Using the atomic masses {masses}, find the $Q$-value. If the incident "
                f"{pname} has a kinetic energy of {q(K, 'MeV')} and the target nucleus is at rest, what is the total kinetic "
                "energy of the reaction products?"
            )
            steps += [
                "An exothermic reaction has no threshold: it can occur at any projectile energy that overcomes the Coulomb "
                "barrier (and the nuclei must still get close enough to react).",
                f"Energy conservation: $K_{{products}} = K_{{projectile}} + Q = {fmt(K)} + {fmt(Q, 4)} = {fmt(Kout, 4)}$ MeV; "
                "how it is shared depends on the emission angles.",
            ]
            answer = f"$Q = {fmt(Q, 4)}$ MeV; products share {q(Kout, 'MeV', 4)} of kinetic energy"
            values.update({"K_MeV": K, "K_products_MeV": Kout})
        else:
            Kth = -Q * (1 + m_p / m_t)
            while True:
                factor = nice(rng, 0.5, 3.0, 0.1)
                if abs(factor - 1) > 0.05:
                    break
            K = sig(Kth * factor, 3)
            possible = K > Kth
            question = (
                f"The reaction ${eq}$ is {context}. Using the atomic masses {masses}, find the $Q$-value and the threshold "
                f"kinetic energy of the incident {pname} (target at rest, non-relativistic). Can the reaction occur when the "
                f"{pname} has {q(K, 'MeV')}, and if so, what total kinetic energy do the products carry?"
            )
            steps += [
                "Threshold: the projectile must supply $|Q|$ plus the kinetic energy the products must keep because momentum "
                "is conserved. Non-relativistically, $K_{th} = -Q\\left(1 + \\frac{m_{projectile}}{m_{target}}\\right)$.",
                f"$K_{{th}} = {fmt(-Q, 4)}\\left(1 + \\frac{{{_fixed(m_p, 6)}}}{{{_fixed(m_t, 6)}}}\\right) = {fmt(Kth, 4)}$ MeV.",
            ]
            if possible:
                Kout = K + Q
                steps.append(f"Since {fmt(K)} MeV > {fmt(Kth, 4)} MeV, the reaction can occur. Products' total kinetic energy: "
                             f"$K + Q = {fmt(K)} + ({fmt(Q, 4)}) = {fmt(Kout, 4)}$ MeV.")
                answer = (f"$Q = {fmt(Q, 4)}$ MeV; $K_{{th}} = {fmt(Kth, 4)}$ MeV; yes — products carry {q(Kout, 'MeV', 4)}")
                values["K_products_MeV"] = Kout
            else:
                steps.append(f"Since {fmt(K)} MeV < {fmt(Kth, 4)} MeV, the {pname} lacks the energy needed and the reaction "
                             "cannot occur (ignoring the barrier-penetration subtleties of real nuclei).")
                answer = f"$Q = {fmt(Q, 4)}$ MeV; $K_{{th}} = {fmt(Kth, 4)}$ MeV; no — {q(K, 'MeV')} is below threshold"
            values.update({"K_MeV": K, "K_th_MeV": Kth, "possible": possible})
    return {"question": question, "steps": steps, "answer": answer, "values": values}


RADIOISOTOPES = [  # name, half-life, unit, molar mass (g/mol), mass unit for samples
    ("cobalt-60", 5.271, "years", 59.934, "mg"), ("cesium-137", 30.08, "years", 136.907, "mg"),
    ("strontium-90", 28.79, "years", 89.908, "mg"), ("iodine-131", 8.025, "days", 130.906, "μg"),
    ("radium-226", 1600, "years", 226.025, "mg"), ("americium-241", 432.6, "years", 241.057, "mg"),
    ("technetium-99m", 6.007, "hours", 98.906, "ng"), ("phosphorus-32", 14.27, "days", 31.974, "μg"),
    ("plutonium-239", 24110, "years", 239.052, "g"), ("uranium-238", 4.468e9, "years", 238.051, "g"),
    ("carbon-14", 5730, "years", 14.003, "mg"), ("tritium (hydrogen-3)", 12.32, "years", 3.016, "mg"),
    ("polonium-210", 138.4, "days", 209.983, "μg"), ("fluorine-18", 109.8, "minutes", 18.001, "ng"),
]
TIME_UNIT_S = {"years": YEAR_S, "days": 86400.0, "hours": 3600.0, "minutes": 60.0}
MASS_UNIT_G = {"g": 1.0, "mg": 1e-3, "μg": 1e-6, "ng": 1e-9}


@template("radioisotope_activity_from_mass", PHYS, "Nuclear Physics", "Radioactive decay", "medium")
def radioisotope_activity_from_mass(rng):
    iso, th, unit, M, munit = pick(rng, RADIOISOTOPES)
    th_s = th * TIME_UNIT_S[unit]
    lam = math.log(2) / th_s
    year_note = " (1 year = 365.25 days)" if unit == "years" else ""
    if rng.random() < 0.6:
        m_val = nice(rng, 1, 500, 1)
        m_g = m_val * MASS_UNIT_G[munit]
        N = m_g / M * N_A
        A = lam * N
        question = (
            f"A sample contains {q(m_val, munit)} of {iso} (molar mass ${_exact(M)}$ g/mol, half-life ${_exact(th)}$ {unit}). "
            "How many radioactive nuclei does it contain, what is the decay constant, and what is the sample's activity in "
            "becquerels and in curies?"
        )
        steps = [
            f"Number of nuclei: $N = \\frac{{m}}{{M}}N_A = \\frac{{{fmt(m_g)}\\text{{ g}}}}{{{_exact(M)}\\text{{ g/mol}}}}"
            f"(6.022\\times10^{{23}}) = {fmt(N)}$.",
            f"Half-life in seconds{year_note}: $t_{{1/2}} = {fmt(th_s, 4)}$ s, so $\\lambda = \\frac{{\\ln 2}}{{t_{{1/2}}}} = "
            f"{fmt(lam)}$ s⁻¹.",
            f"Activity: $A = \\lambda N = ({fmt(lam)})({fmt(N)}) = {fmt(A)}$ Bq (decays per second).",
            f"In curies (1 Ci $= 3.7\\times10^{{10}}$ Bq): $A = {fmt(A / 3.7e10)}$ Ci.",
            f"Specific activity: $A/m = {fmt(A / m_g)}$ Bq/g — the shorter the half-life (and the lighter the atom), the "
            "more active each gram is. (One gram of radium-226 has about 1 Ci, the origin of the unit.)",
        ]
        answer = f"$N = {fmt(N)}$; $\\lambda = {fmt(lam)}$ s⁻¹; $A = {fmt(A)}$ Bq $= {fmt(A / 3.7e10)}$ Ci"
        values = {"variant": "find_activity", "isotope": iso, "half_life_s": th_s, "M": M, "m_g": m_g, "N": N,
                  "lambda": lam, "A_Bq": A}
    else:
        aunit, afac = pick(rng, [("MBq", 1e6), ("GBq", 1e9), ("mCi", 3.7e7), ("Ci", 3.7e10)])
        a_val = nice(rng, 1, 900, 1)
        A = a_val * afac
        N = A / lam
        m_g = N * M / N_A
        question = (
            f"A laboratory needs a {iso} source with an activity of {q(a_val, aunit)}. Given the half-life of {iso} "
            f"(${_exact(th)}$ {unit}) and its molar mass (${_exact(M)}$ g/mol), how many radioactive nuclei and what mass of "
            f"{iso} does the source contain?"
        )
        conv = "" if aunit in ("MBq", "GBq") else " (1 Ci $= 3.7\\times10^{10}$ Bq)"
        steps = [
            f"Activity in becquerels{conv}: $A = {fmt(A)}$ Bq.",
            f"Half-life in seconds{year_note}: $t_{{1/2}} = {fmt(th_s, 4)}$ s, so $\\lambda = \\ln 2/t_{{1/2}} = {fmt(lam)}$ s⁻¹.",
            f"From $A = \\lambda N$: $N = A/\\lambda = ({fmt(A)})/({fmt(lam)}) = {fmt(N)}$ nuclei.",
            f"Mass: $m = \\frac{{N}}{{N_A}}M = \\frac{{{fmt(N)}}}{{6.022\\times10^{{23}}}}({_exact(M)}) = {fmt(m_g)}$ g.",
            "Short-lived isotopes reach a large activity with a remarkably small mass.",
        ]
        answer = f"$N = {fmt(N)}$ nuclei; $m = {fmt(m_g)}$ g"
        values = {"variant": "find_mass", "isotope": iso, "half_life_s": th_s, "M": M, "A_Bq": A, "lambda": lam, "N": N,
                  "m_g": m_g}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("fission_u235_vs_coal", PHYS, "Nuclear Physics", "Nuclear fission", "medium")
def fission_u235_vs_coal(rng):
    Hc = nice(rng, 24, 32, 1)  # MJ/kg of coal
    E_fis = 200.0  # MeV per fission
    M_U = 235.044
    e_per_kg_U = 1000 / M_U * N_A * E_fis * MEV_J
    ratio = e_per_kg_U / (Hc * 1e6)
    common = [
        f"Energy per kilogram of U-235: $\\frac{{1000\\text{{ g}}}}{{235.044\\text{{ g/mol}}}}(6.022\\times10^{{23}})"
        f"(200\\text{{ MeV}})(1.602\\times10^{{-13}}\\text{{ J/MeV}}) = {fmt(e_per_kg_U)}$ J/kg.",
        f"Coal releases {Hc} MJ/kg, so fission yields about ${fmt(ratio)}$ times more energy per kilogram of fuel.",
    ]
    if rng.random() < 0.5:
        P_e = nice(rng, 100, 1600, 50)
        eta = nice(rng, 30, 38, 1)
        days = pick(rng, [1, 7, 30, 365]) if rng.random() < 0.5 else nice(rng, 2, 365, 1)
        t = days * 86400
        E_th = P_e * 1e6 / (eta / 100) * t
        N = E_th / (E_fis * MEV_J)
        m_U = N * M_U / N_A / 1000
        m_coal = E_th / (Hc * 1e6)
        dm = E_th / C ** 2
        question = (
            f"A nuclear power station delivers {q(P_e, 'MW')} of electrical power with a thermal efficiency of {eta}%. Assuming "
            f"about 200 MeV is released per fission of uranium-235 (molar mass 235.044 g/mol), how much U-235 is fissioned in "
            f"{days} day{'s' if days != 1 else ''} of full-power operation? How much coal (heat of combustion {Hc} MJ/kg) would "
            "a coal-fired station of the same efficiency burn in that time?"
        )
        steps = [
            f"Thermal power: $P_{{th}} = P_e/\\eta = {P_e}/{fmt(eta / 100, 2)} = {fmt(P_e / (eta / 100))}$ MW.",
            f"Heat released in {days} day{'s' if days != 1 else ''} ($t = {fmt(t)}$ s): $E = P_{{th}}t = {fmt(E_th)}$ J.",
            f"Energy per fission: $200\\text{{ MeV}} = 200(1.602\\times10^{{-13}}) = {fmt(E_fis * MEV_J)}$ J, so the number of "
            f"fissions is $N = E/E_f = {fmt(N)}$.",
            f"Mass of U-235: $m = \\frac{{N}}{{N_A}}M = \\frac{{{fmt(N)}}}{{6.022\\times10^{{23}}}}(235.044\\text{{ g/mol}}) = "
            f"{fmt(m_U * 1000)}$ g $= {fmt(m_U)}$ kg.",
            f"Coal needed for the same heat: $m_{{coal}} = \\frac{{{fmt(E_th)}}}{{{Hc}\\times10^6}} = {fmt(m_coal)}$ kg "
            f"$= {fmt(m_coal / 1000)}$ tonnes.",
        ] + common + [
            f"Mass actually converted to energy: $\\Delta m = E/c^2 = {fmt(dm * 1000)}$ g, about "
            f"{fmt(100 * dm / m_U, 2)}% of the uranium fissioned.",
        ]
        answer = (f"{q(m_U, 'kg')} of U-235 versus {q(m_coal / 1000, 'tonnes')} of coal (about ${fmt(ratio)}$ times more "
                  "energy per kilogram)")
        values = {"variant": "power_plant", "P_e_MW": P_e, "eta_pct": eta, "days": days, "Hc_MJ_per_kg": Hc,
                  "E_th_J": E_th, "N_fissions": N, "m_U_kg": m_U, "m_coal_kg": m_coal, "ratio": ratio, "dm_kg": dm}
    else:
        m_g = nice(rng, 1, 1000, 1)
        eta = nice(rng, 30, 38, 1)
        use = nice(rng, 3, 12, 1)  # MWh of electricity per household per year
        N = m_g / M_U * N_A
        E = N * E_fis * MEV_J
        m_coal = E / (Hc * 1e6)
        years = E * eta / 100 / (use * 3.6e9)
        question = (
            f"Suppose {q(m_g, 'g')} of uranium-235 (molar mass 235.044 g/mol) undergoes complete fission, releasing about "
            f"200 MeV per fission. How much heat is released, what mass of coal (heat of combustion {Hc} MJ/kg) releases the "
            f"same heat, and for how many years could the energy supply a household using {use} MWh of electricity per year "
            f"if it is converted to electricity at {eta}% efficiency?"
        )
        steps = [
            f"Number of nuclei: $N = \\frac{{{m_g}\\text{{ g}}}}{{235.044\\text{{ g/mol}}}}(6.022\\times10^{{23}}) = {fmt(N)}$.",
            f"Heat released: $E = N(200\\text{{ MeV}})(1.602\\times10^{{-13}}\\text{{ J/MeV}}) = {fmt(E)}$ J.",
            f"Equivalent coal: $m_{{coal}} = \\frac{{{fmt(E)}}}{{{Hc}\\times10^6}} = {fmt(m_coal)}$ kg $= {fmt(m_coal / 1000)}$ tonnes.",
            f"Electricity: $({fmt(eta / 100, 2)})({fmt(E)}) = {fmt(E * eta / 100)}$ J $= {fmt(E * eta / 100 / 3.6e9)}$ MWh "
            f"(1 MWh $= 3.6\\times10^9$ J), enough for ${fmt(years)}$ years at {use} MWh per year.",
        ] + common
        answer = f"$E = {fmt(E)}$ J; equivalent to {q(m_coal / 1000, 'tonnes')} of coal; about {fmt(years)} household-years"
        values = {"variant": "mass_given", "m_g": m_g, "eta_pct": eta, "use_MWh": use, "Hc_MJ_per_kg": Hc, "N_fissions": N,
                  "E_J": E, "m_coal_kg": m_coal, "years": years, "ratio": ratio}
    return {"question": question, "steps": steps, "answer": answer, "values": values}
