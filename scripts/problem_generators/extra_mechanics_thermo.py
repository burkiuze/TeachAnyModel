"""Additional Physics templates: classical mechanics and thermodynamics.

Classical mechanics: frictionless banked curves, the conical pendulum, tension in a vertical
circle, loop-the-loop tracks, centre of mass, physical pendulums (parallel-axis theorem), damped
and driven oscillators, Hohmann transfers, orbital energy, Stokes settling, Torricelli efflux,
Poiseuille flow, the ballistic pendulum, recoil and the road-load power of vehicles.

Thermodynamics: adiabatic and isothermal processes of an ideal gas, entropy changes of water,
conduction through composite walls, the air-standard Otto cycle and evaporative cooling.
"""

import math

from .common import R_GAS, fmt, nice, pick, template

PHYS = "Physics"
MECH = "Classical Mechanics"
THERMO = "Thermodynamics"

g = 9.81                 # m/s^2
MU_EARTH = 3.986e14      # GM of Earth, m^3/s^2
R_EARTH_KM = 6371        # mean radius of Earth, km
C_WATER = 4186           # specific heat of liquid water, J/(kg K)
RHO_AIR = 1.20           # density of air near sea level, kg/m^3
HP = 745.7               # 1 mechanical horsepower in W
MMHG = 133.3             # 1 mmHg in Pa
L_SWEAT = 2.42e6         # latent heat of vaporization of water at skin temperature, J/kg
C_BODY = 3500            # average specific heat of the human body, J/(kg K)


def ex(x, min_sig=2):
    """Format ``x`` with the fewest significant figures (at least ``min_sig``) that show it exactly."""
    if isinstance(x, int) and abs(x) < 100000:
        return str(x)
    x = float(x)
    if x == 0:
        return "0"
    for s in range(min_sig, 11):
        if math.isclose(float(f"{x:.{s}g}"), x, rel_tol=1e-12):
            return fmt(x, s)
    return fmt(x, 10)


def qx(x, unit="", min_sig=2):
    """Exact quantity: ``$x$ unit`` with ``x`` shown to as many figures as it has."""
    s = f"${ex(x, min_sig)}$"
    return f"{s} {unit}" if unit else s


def draw(rng, rng_spec):
    """nice() over a (lo, hi, step) tuple."""
    lo, hi, step = rng_spec
    return nice(rng, lo, hi, step)


# ---------------------------------------------------------------------------
# Circular motion
# ---------------------------------------------------------------------------

BANK_SITES = [
    # site, vehicle, surface, radius (m), speed (km/h), mass (kg), allowed bank angle (deg)
    ("highway exit ramp", "car", "road", (50, 250, 10), (40, 90, 5), (900, 2200, 50), (4, 25)),
    ("turn of an oval motor-racing track", "race car", "track", (200, 600, 20), (120, 220, 10), (700, 1000, 20), (8, 32)),
    ("velodrome turn", "track cyclist (rider plus bicycle)", "track", (20, 50, 1), (40, 70, 5), (60, 100, 1), (25, 48)),
    ("high-speed railway curve", "passenger railcar", "rails", (2000, 7000, 100), (160, 300, 10), (40000, 60000, 1000), (2, 7)),
]


@template("banked_curve_no_friction", PHYS, MECH, "Circular motion", "medium")
def banked_curve_no_friction(rng):
    site, veh, surface, r_rng, v_rng, m_rng, (th_lo, th_hi) = pick(rng, BANK_SITES)
    short = veh.split(" (")[0]
    m = draw(rng, m_rng)
    force_steps = [
        "Treat the vehicle as a particle. With no friction only two forces act on the "
        f"{short}: its weight $mg$ (vertically down) and the normal force $N$ (perpendicular to the banked surface). "
        "Their resultant must be the horizontal centripetal force $mv^2/r$ pointing toward the center of the curve.",
        "Vertical components balance: $N\\cos\\theta = mg$. Horizontal components give the centripetal force: "
        "$N\\sin\\theta = \\frac{mv^2}{r}$.",
    ]
    if rng.random() < 0.55:
        mode = "find_angle"
        for _ in range(1000):
            r = draw(rng, r_rng)
            v_kmh = draw(rng, v_rng)
            v = v_kmh / 3.6
            th = math.degrees(math.atan(v * v / (r * g)))
            if th_lo <= th <= th_hi:
                break
        else:
            raise RuntimeError("no valid banked-curve parameters")
        tan_th = v * v / (r * g)
        N = m * g / math.cos(math.radians(th))
        question = (
            f"A {site} is a circular arc of radius {qx(r, 'm')}. At what angle must it be banked so that a {veh} of mass "
            f"{qx(m, 'kg')} traveling at {qx(v_kmh, 'km/h')} can round it without any sideways friction force (the design "
            f"speed of the curve)? What normal force does the {surface} then exert on the {veh}?"
        )
        steps = [f"Convert the speed to SI units: $v = {ex(v_kmh)}/3.6 = {fmt(v, 4)}$ m/s."] + force_steps + [
            f"Dividing the two equations eliminates both $N$ and $m$: $\\tan\\theta = \\frac{{v^2}}{{rg}} = "
            f"\\frac{{({fmt(v, 4)})^2}}{{({ex(r)})(9.81)}} = {fmt(tan_th, 4)}$, so $\\theta = {fmt(th)}°$.",
            f"Normal force: $N = \\frac{{mg}}{{\\cos\\theta}} = \\frac{{({ex(m)})(9.81)}}{{\\cos {fmt(th)}°}} = {fmt(N)}$ N, "
            f"which is ${fmt(N / (m * g))}$ times the weight.",
            f"Interpretation: the bank angle does not depend on the mass. A slower {short} would tend to slide down the slope "
            "(friction would have to act up the slope), a faster one would tend to slide up and outward.",
        ]
        answer = f"$\\theta = {fmt(th)}°$; $N = {fmt(N)}$ N"
        values = {"mode": mode, "r": r, "v_kmh": v_kmh, "m": m, "v": v, "theta_deg": th, "N": N}
    else:
        mode = "find_speed"
        r = draw(rng, r_rng)
        th = nice(rng, th_lo, th_hi, 1)
        v = math.sqrt(r * g * math.tan(math.radians(th)))
        v_kmh = 3.6 * v
        N = m * g / math.cos(math.radians(th))
        question = (
            f"A {site} of radius {qx(r, 'm')} is banked at ${th}°$. At what speed can a {veh} of mass {qx(m, 'kg')} round it "
            "with no sideways friction force at all (the design speed)? Give the speed in m/s and km/h, and find the normal "
            f"force exerted by the {surface}."
        )
        steps = force_steps + [
            "Dividing the two equations eliminates $N$ and $m$: $\\tan\\theta = \\frac{v^2}{rg}$.",
            f"Design speed: $v = \\sqrt{{rg\\tan\\theta}} = \\sqrt{{({ex(r)})(9.81)\\tan {th}°}} = {fmt(v)}$ m/s "
            f"$= {fmt(v)} \\times 3.6 = {fmt(v_kmh)}$ km/h.",
            f"Normal force: $N = \\frac{{mg}}{{\\cos\\theta}} = \\frac{{({ex(m)})(9.81)}}{{\\cos {th}°}} = {fmt(N)}$ N "
            f"(${fmt(N / (m * g))}$ times the weight).",
            f"Interpretation: any {short}, whatever its mass, can take the curve at this speed without friction; "
            "below it friction must act up the slope, above it down the slope.",
        ]
        answer = f"$v = {fmt(v)}$ m/s $= {fmt(v_kmh)}$ km/h; $N = {fmt(N)}$ N"
        values = {"mode": mode, "r": r, "theta_deg": th, "m": m, "v": v, "v_kmh": v_kmh, "N": N}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


CONICAL_OBJECTS = ["small ball", "stone", "pendulum bob", "rubber stopper", "steel ball"]


@template("conical_pendulum_motion", PHYS, MECH, "Circular motion", "medium")
def conical_pendulum_motion(rng):
    obj = pick(rng, CONICAL_OBJECTS)
    m = nice(rng, 0.05, 2.00, 0.05)
    L = nice(rng, 0.30, 2.00, 0.05)
    intro = (f"A {obj} of mass {qx(m, 'kg')} hangs from a light string of length {qx(L, 'm')} and moves at constant "
             "speed in a horizontal circle (a conical pendulum).")
    if rng.random() < 0.55:
        mode = "angle_given"
        th = nice(rng, 10, 70, 1)
        c, s = math.cos(math.radians(th)), math.sin(math.radians(th))
        T = m * g / c
        r = L * s
        v = math.sqrt(r * g * math.tan(math.radians(th)))
        P = 2 * math.pi * math.sqrt(L * c / g)
        n_rpm = 60 / P
        P0 = 2 * math.pi * math.sqrt(L / g)
        question = (f"{intro} The string makes a constant angle of ${th}°$ with the vertical. Find the tension in the string, "
                    f"the speed of the {obj} and the period of its motion.")
        steps = [
            "Two forces act: the weight $mg$ and the tension $T$ along the string. The vertical component of $T$ balances "
            "the weight; the horizontal component supplies the centripetal force.",
            f"Vertical: $T\\cos\\theta = mg \\Rightarrow T = \\frac{{mg}}{{\\cos\\theta}} = "
            f"\\frac{{({ex(m)})(9.81)}}{{\\cos {th}°}} = {fmt(T)}$ N.",
            f"Radius of the circle: $r = L\\sin\\theta = ({ex(L)})\\sin {th}° = {fmt(r)}$ m.",
            f"Horizontal: $T\\sin\\theta = \\frac{{mv^2}}{{r}}$. Dividing by the vertical equation gives "
            f"$\\tan\\theta = \\frac{{v^2}}{{rg}}$, so $v = \\sqrt{{rg\\tan\\theta}} = \\sqrt{{({fmt(r)})(9.81)\\tan {th}°}} = {fmt(v)}$ m/s.",
            f"Period: $P = \\frac{{2\\pi r}}{{v}} = 2\\pi\\sqrt{{\\frac{{L\\cos\\theta}}{{g}}}} = {fmt(P)}$ s, "
            f"i.e. ${fmt(n_rpm)}$ revolutions per minute.",
            f"Check: the period depends only on the height of the cone $L\\cos\\theta$, not on the mass; it is shorter than "
            f"the small-angle simple-pendulum period $2\\pi\\sqrt{{L/g}} = {fmt(P0)}$ s, as it should be.",
        ]
        answer = f"$T = {fmt(T)}$ N; $v = {fmt(v)}$ m/s; period $= {fmt(P)}$ s"
        values = {"mode": mode, "m": m, "L": L, "theta_deg": th, "T": T, "r": r, "v": v, "P": P}
    else:
        mode = "rate_given"
        for _ in range(1000):
            n_rpm = nice(rng, 20, 140, 1)
            w = 2 * math.pi * n_rpm / 60
            cth = g / (w * w * L)
            if 0.15 <= cth <= 0.95:
                break
        else:
            raise RuntimeError("no valid conical-pendulum rate")
        th = math.degrees(math.acos(cth))
        T = m * w * w * L
        r = L * math.sin(math.radians(th))
        v = w * r
        n_min = 60 / (2 * math.pi) * math.sqrt(g / L)
        question = (f"{intro} It makes {qx(n_rpm)} revolutions per minute. What angle does the string make with the "
                    f"vertical, what is the tension in the string, and how fast is the {obj} moving?")
        steps = [
            f"Angular speed: $\\omega = \\frac{{2\\pi n}}{{60}} = \\frac{{2\\pi({ex(n_rpm)})}}{{60}} = {fmt(w, 4)}$ rad/s.",
            "Horizontal (centripetal) equation with radius $r = L\\sin\\theta$: $T\\sin\\theta = m\\omega^2L\\sin\\theta$, so "
            f"$T = m\\omega^2L = ({ex(m)})({fmt(w, 4)})^2({ex(L)}) = {fmt(T)}$ N.",
            f"Vertical equation: $T\\cos\\theta = mg \\Rightarrow \\cos\\theta = \\frac{{g}}{{\\omega^2L}} = "
            f"\\frac{{9.81}}{{({fmt(w, 4)})^2({ex(L)})}} = {fmt(cth, 4)}$, so $\\theta = {fmt(th)}°$.",
            f"Radius $r = L\\sin\\theta = {fmt(r)}$ m and speed $v = \\omega r = {fmt(v)}$ m/s.",
            f"Check: a conical pendulum needs $\\omega^2L > g$, i.e. more than $\\frac{{60}}{{2\\pi}}\\sqrt{{g/L}} = {fmt(n_min)}$ "
            "rev/min; below that rate the string would simply hang vertically.",
        ]
        answer = f"$\\theta = {fmt(th)}°$; $T = {fmt(T)}$ N; $v = {fmt(v)}$ m/s"
        values = {"mode": mode, "m": m, "L": L, "n_rpm": n_rpm, "theta_deg": th, "T": T, "r": r, "v": v}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


VC_OBJECTS = [
    # object, tether, mass range (kg), radius range (m)
    ("ball", "a light string", (0.10, 1.00, 0.05), (0.50, 1.50, 0.05)),
    ("stone", "a light cord", (0.05, 0.50, 0.01), (0.40, 1.20, 0.05)),
    ("small bucket of water", "a rope", (1.0, 4.0, 0.1), (0.80, 1.20, 0.05)),
    ("metal sphere", "a light wire", (0.20, 2.00, 0.10), (0.50, 2.00, 0.10)),
]


@template("vertical_circle_string_tension", PHYS, MECH, "Circular motion", "medium")
def vertical_circle_string_tension(rng):
    obj, tether, m_rng, r_rng = pick(rng, VC_OBJECTS)
    m = draw(rng, m_rng)
    r = draw(rng, r_rng)
    vmin = math.sqrt(g * r)
    tether_word = tether.split()[-1]
    if rng.random() < 0.5:
        mode = "top_given"
        for _ in range(1000):
            vt = nice(rng, 1.0, 12.0, 0.1)
            if 1.05 * vmin <= vt <= 2.5 * vmin:
                break
        else:
            raise RuntimeError("no valid top speed")
        vb = math.sqrt(vt * vt + 4 * g * r)
        given = f"At the top of the circle its speed is {qx(vt, 'm/s')}."
        ask = "find the tension at the top, the speed at the bottom, and the tension at the bottom of the circle."
        energy = (f"$v_b = \\sqrt{{v_t^2 + 4gr}} = \\sqrt{{({ex(vt)})^2 + 4(9.81)({ex(r)})}} = {fmt(vb)}$ m/s.")
    else:
        mode = "bottom_given"
        for _ in range(1000):
            vb = nice(rng, 3.0, 16.0, 0.1)
            if (1.05 ** 2 + 4) * g * r <= vb * vb <= 10.25 * g * r:
                break
        else:
            raise RuntimeError("no valid bottom speed")
        vt = math.sqrt(vb * vb - 4 * g * r)
        given = f"At the lowest point its speed is {qx(vb, 'm/s')}."
        ask = "find its speed at the top, and the tension at the top and at the bottom of the circle."
        energy = (f"$v_t = \\sqrt{{v_b^2 - 4gr}} = \\sqrt{{({ex(vb)})^2 - 4(9.81)({ex(r)})}} = {fmt(vt)}$ m/s.")
    Tt = m * (vt * vt / r - g)
    Tb = m * (vb * vb / r + g)
    question = (f"A {obj} of mass {qx(m, 'kg')} tied to {tether} is swung in a vertical circle of radius {qx(r, 'm')}. "
                f"{given} Neglecting air resistance, {ask}")
    steps = [
        "Energy: the tension is always perpendicular to the velocity and does no work, so mechanical energy is conserved. "
        "The lowest point is $2r$ below the top: $\\tfrac12mv_b^2 = \\tfrac12mv_t^2 + mg(2r)$.",
        energy,
        f"At the top, tension and weight both point down, toward the center: $T_t + mg = \\frac{{mv_t^2}}{{r}}$, so "
        f"$T_t = m\\left(\\frac{{v_t^2}}{{r}} - g\\right) = ({ex(m)})\\left(\\frac{{({fmt(vt, 4)})^2}}{{{ex(r)}}} - 9.81\\right) = {fmt(Tt)}$ N.",
        f"At the bottom, tension points up (toward the center) and weight down: $T_b - mg = \\frac{{mv_b^2}}{{r}}$, so "
        f"$T_b = m\\left(\\frac{{v_b^2}}{{r}} + g\\right) = ({ex(m)})\\left(\\frac{{({fmt(vb, 4)})^2}}{{{ex(r)}}} + 9.81\\right) = {fmt(Tb)}$ N.",
        f"Check: $T_b - T_t = {fmt(Tb - Tt)}$ N $= 6mg = 6({ex(m)})(9.81)$, a general result for a vertical circle "
        "that does not depend on the speed. ✓",
        f"The {tether_word} stays taut at the top only if $v_t \\ge \\sqrt{{gr}} = {fmt(vmin)}$ m/s; here "
        f"$v_t = {fmt(vt)}$ m/s, so the {obj} completes the circle.",
    ]
    answer = f"$T_{{top}} = {fmt(Tt)}$ N; $v_{{top}} = {fmt(vt)}$ m/s, $v_{{bottom}} = {fmt(vb)}$ m/s; $T_{{bottom}} = {fmt(Tb)}$ N"
    values = {"mode": mode, "m": m, "r": r, "v_top": vt, "v_bottom": vb, "T_top": Tt, "T_bottom": Tb}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


LOOP_OBJECTS = [
    # object, motion, radius range (m), mass range, mass unit, release-height step (m)
    ("toy car", "slide", (0.10, 0.30, 0.01), (20, 100, 5), "g", 0.01),
    ("roller-coaster car (with its riders)", "slide", (6.0, 15.0, 0.5), (400, 900, 50), "kg", 0.5),
    ("small block", "slide", (0.20, 1.00, 0.05), (0.1, 2.0, 0.1), "kg", 0.05),
    ("marble (a uniform solid sphere)", "roll", (0.10, 0.40, 0.01), (5, 30, 1), "g", 0.01),
]


@template("loop_the_loop_track", PHYS, MECH, "Energy conservation", "medium")
def loop_the_loop_track(rng):
    obj, motion, R_rng, m_rng, m_unit, h_step = pick(rng, LOOP_OBJECTS)
    R = draw(rng, R_rng)
    m_disp = draw(rng, m_rng)
    m = m_disp / 1000 if m_unit == "g" else m_disp
    c = 1.0 if motion == "slide" else 1.4
    h_min = R * (2 + c / 2)
    for _ in range(2000):
        h = nice(rng, h_step, round(4 * R / h_step) * h_step, h_step)
        if 1.05 * h_min <= h <= 4 * R:
            break
    else:
        raise RuntimeError("no valid release height")
    vt = math.sqrt(2 * g * (h - 2 * R) / c)
    vb = math.sqrt(2 * g * h / c)
    Nt = m * (vt * vt / R - g)
    Nb = m * (vb * vb / R + g)
    if motion == "slide":
        ideal = f"Neglect friction and air resistance and treat the {obj.split(' (')[0]} as a particle."
        ke = "$\\tfrac12mv^2$"
        work_note = "Only gravity does work (the normal force is perpendicular to the motion)"
        energy_eq = "mgh = mg(2R) + \\tfrac12mv^2"
        top_v = "v_t = \\sqrt{2g(h - 2R)}"
        bot_v = "v_b = \\sqrt{2gh}"
        hmin_expr = "h_{min} = 2R + \\tfrac12R = 2.5R"
    else:
        ideal = ("The marble rolls without slipping, its own radius is much smaller than $R$, and rolling friction and air "
                 "resistance are negligible ($I = \\tfrac25mr^2$).")
        ke = "$\\tfrac12mv^2 + \\tfrac12I\\omega^2 = \\tfrac12mv^2(1 + \\tfrac25) = 0.7mv^2$"
        work_note = ("Only gravity does work (the normal force is perpendicular to the motion and static friction acts at "
                     "the instantaneously resting contact point)")
        energy_eq = "mgh = mg(2R) + 0.7mv^2"
        top_v = "v_t = \\sqrt{\\tfrac{10}{7}g(h - 2R)}"
        bot_v = "v_b = \\sqrt{\\tfrac{10}{7}gh}"
        hmin_expr = "h_{min} = 2R + 0.7R = 2.7R"
    short = obj.split(" (")[0]
    question = (
        f"A {obj} of mass {qx(m_disp, m_unit)} is released from rest at a height {qx(h, 'm')} above the bottom of a vertical "
        f"circular loop of radius {qx(R, 'm')}. {ideal} (a) What is the minimum release height for the {short} to stay "
        "on the track at the top of the loop? (b) For the actual release height, find its speed at the top and the normal "
        "force exerted by the track at the top and at the bottom of the loop."
    )
    mass_note = f"Mass in SI units: $m = {ex(m)}$ kg. " if m_unit == "g" else ""
    steps = [
        f"{mass_note}Kinetic energy of the {short}: {ke}. {work_note}, so mechanical energy is conserved.",
        "At the top the track can only push (down). The limiting case is $N = 0$, when gravity alone supplies the centripetal "
        "force: $mg = \\frac{mv_{min}^2}{R} \\Rightarrow v_{min}^2 = gR$.",
        f"Energy from release to the top (height $2R$): ${energy_eq}$. Setting $v^2 = gR$ gives "
        f"${hmin_expr} = {fmt(h_min, 4)}$ m.",
        f"Actual release from $h = {ex(h)}$ m $> h_{{min}}$: ${top_v} = {fmt(vt)}$ m/s.",
        f"Normal force at the top (weight and $N$ both point down): $N_t = m\\left(\\frac{{v_t^2}}{{R}} - g\\right) = "
        f"({ex(m)})\\left(\\frac{{({fmt(vt, 4)})^2}}{{{ex(R)}}} - 9.81\\right) = {fmt(Nt)}$ N (${fmt(Nt / (m * g))}$ times the weight).",
        f"At the bottom: ${bot_v} = {fmt(vb)}$ m/s and $N_b = m\\left(\\frac{{v_b^2}}{{R}} + g\\right) = {fmt(Nb)}$ N "
        f"(${fmt(Nb / (m * g))}$ times the weight).",
        (f"Check: $N_b - N_t = {fmt(Nb - Nt)}$ N $= 6mg$, independent of $h$. ✓" if motion == "slide" else
         f"Check: $N_b - N_t = {fmt(Nb - Nt)}$ N $= mg\\left(2 + \\tfrac{{4}}{{1.4}}\\right)$, independent of $h$. ✓"),
    ]
    answer = f"$h_{{min}} = {fmt(h_min)}$ m; $v_{{top}} = {fmt(vt)}$ m/s; $N_{{top}} = {fmt(Nt)}$ N; $N_{{bottom}} = {fmt(Nb)}$ N"
    values = {"motion": motion, "R": R, "h": h, "m": m, "m_disp": m_disp, "c": c, "h_min": h_min,
              "v_top": vt, "v_bottom": vb, "N_top": Nt, "N_bottom": Nb}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Centre of mass and rigid bodies
# ---------------------------------------------------------------------------

BARYCENTERS = [
    # big body, mass (kg), radius (m), small body, mass (kg), center-to-center distance (m)
    ("Earth", 5.972e24, 6.371e6, "the Moon", 7.342e22, 3.844e8),
    ("the Sun", 1.989e30, 6.957e8, "Jupiter", 1.898e27, 7.785e11),
    ("Pluto", 1.303e22, 1.188e6, "Charon", 1.586e21, 1.9596e7),
    ("the Sun", 1.989e30, 6.957e8, "Earth", 5.972e24, 1.496e11),
]

COM_SETTINGS = [
    ("Small weights are glued to a light rigid board at the following positions", "g", "cm"),
    ("Point masses are fixed to a light rigid frame lying in the $xy$-plane", "kg", "m"),
    ("The main components of a small drone can be modeled as point masses on its light frame", "g", "cm"),
    ("Small heavy balls are joined by light rods into a flat rigid structure", "kg", "m"),
]


@template("center_of_mass_point_masses", PHYS, MECH, "Center of mass", "easy")
def center_of_mass_point_masses(rng):
    if rng.random() < 0.12:
        A, MA, RA, B, MB, D = pick(rng, BARYCENTERS)
        d = MB * D / (MA + MB)
        inside = d < RA
        cap = A[0].upper() + A[1:]
        question = (
            f"{cap} (mass ${ex(MA)}$ kg, radius ${ex(RA)}$ m) and {B} (mass ${ex(MB)}$ kg) are ${ex(D)}$ m apart, center to "
            f"center. Locate their common center of mass (the barycenter about which both bodies orbit) relative to the "
            f"center of {A}. Does it lie inside or outside {A}?"
        )
        steps = [
            f"Put the origin at the center of {A} and the $x$-axis toward {B}: $x_{{cm}} = \\frac{{M_A(0) + M_BD}}{{M_A + M_B}} = \\frac{{M_BD}}{{M_A + M_B}}$.",
            f"$x_{{cm}} = \\frac{{({ex(MB)})({ex(D)})}}{{{ex(MA)} + {ex(MB)}}} = {fmt(d)}$ m $= {fmt(d / 1000)}$ km.",
            f"Compare with the radius of {A}: $x_{{cm}}/R = {fmt(d / RA)}$, so the barycenter lies "
            f"{'inside' if inside else 'outside'} {A}.",
            f"Interpretation: both bodies orbit this point; {A} {'wobbles about a point beneath its surface' if inside else 'itself circles a point in space outside its own surface'}.",
        ]
        answer = f"$x_{{cm}} = {fmt(d)}$ m from the center of {A}, {'inside' if inside else 'outside'} it"
        values = {"mode": "barycenter", "M_A": MA, "R_A": RA, "M_B": MB, "D": D, "d": d, "inside": inside}
        return {"question": question, "steps": steps, "answer": answer, "values": values}

    setting, munit, lunit = pick(rng, COM_SETTINGS)
    n = pick(rng, [3, 4])
    pts = []
    while len(pts) < n:
        pt = (rng.randint(0, 30), rng.randint(0, 30)) if lunit == "cm" else (rng.randint(-4, 6), rng.randint(-4, 6))
        if pt not in pts:
            pts.append(pt)
    ms = [nice(rng, 20, 400, 10) if munit == "g" else nice(rng, 0.5, 5.0, 0.5) for _ in range(n)]
    M = sum(ms)
    sx = sum(mi * p[0] for mi, p in zip(ms, pts))
    sy = sum(mi * p[1] for mi, p in zip(ms, pts))
    xc, yc = sx / M, sy / M
    dist = math.hypot(xc, yc)
    listing = "; ".join(f"$m_{i + 1} = {ex(mi)}$ {munit} at $({p[0]}, {p[1]})$ {lunit}" for i, (mi, p) in enumerate(zip(ms, pts)))
    question = f"{setting}: {listing}. Find the coordinates of the center of mass of the system and its distance from the origin."
    terms_x = " + ".join(f"({ex(mi)})({p[0]})" for mi, p in zip(ms, pts))
    terms_y = " + ".join(f"({ex(mi)})({p[1]})" for mi, p in zip(ms, pts))
    heavy = max(range(n), key=lambda i: ms[i])
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    steps = [
        f"Total mass: $M = \\sum m_i = {' + '.join(ex(mi) for mi in ms)} = {ex(M)}$ {munit}.",
        f"$x_{{cm}} = \\frac{{\\sum m_ix_i}}{{M}} = \\frac{{{terms_x}}}{{{ex(M)}}} = \\frac{{{ex(sx)}}}{{{ex(M)}}} = {fmt(xc)}$ {lunit}.",
        f"$y_{{cm}} = \\frac{{\\sum m_iy_i}}{{M}} = \\frac{{{terms_y}}}{{{ex(M)}}} = \\frac{{{ex(sy)}}}{{{ex(M)}}} = {fmt(yc)}$ {lunit}.",
        f"Distance from the origin: $\\sqrt{{x_{{cm}}^2 + y_{{cm}}^2}} = {fmt(dist)}$ {lunit}.",
        f"Check: ${min(xs)} \\le x_{{cm}} \\le {max(xs)}$ and ${min(ys)} \\le y_{{cm}} \\le {max(ys)}$, as it must be for positive "
        f"masses; the center of mass is pulled toward the heaviest mass ($m_{heavy + 1}$)."
        + (" The mass unit cancels, so grams can be used directly." if munit == "g" else ""),
    ]
    answer = f"$(x_{{cm}}, y_{{cm}}) = ({fmt(xc)}, {fmt(yc)})$ {lunit}; distance from the origin ${fmt(dist)}$ {lunit}"
    values = {"mode": "points", "masses": ms, "xs": xs, "ys": ys, "M": M, "x_cm": xc, "y_cm": yc, "dist": dist}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("physical_pendulum_parallel_axis", PHYS, MECH, "Rotational dynamics", "hard")
def physical_pendulum_parallel_axis(rng):
    mode = pick(rng, ["rod", "rod", "disk", "rod_bob"])
    if mode == "rod":
        L = nice(rng, 0.40, 2.00, 0.10)
        d = nice(rng, 0.05, round(L / 2, 2), 0.05)
        M = nice(rng, 0.2, 3.0, 0.1)
        Icm = M * L * L / 12
        I = Icm + M * d * d
        T = 2 * math.pi * math.sqrt(I / (M * g * d))
        Leq = I / (M * d)
        d_star = L / math.sqrt(12)
        T_min = 2 * math.pi * math.sqrt(2 * L / (math.sqrt(12) * g))
        where = ("through one of its ends" if math.isclose(d, L / 2)
                 else f"through a small hole drilled {qx(d, 'm')} from its center")
        question = (
            f"A uniform rod of mass {qx(M, 'kg')} and length {qx(L, 'm')} swings freely in a vertical plane about a "
            f"horizontal axis {where}. Find its moment of inertia about the pivot, its period for small oscillations and "
            "the length of the equivalent simple pendulum."
        )
        steps = [
            f"Moment of inertia of a uniform rod about its center: $I_{{cm}} = \\tfrac{{1}}{{12}}ML^2 = "
            f"\\tfrac{{1}}{{12}}({ex(M)})({ex(L)})^2 = {fmt(Icm, 4)}$ kg·m².",
            f"Parallel-axis theorem with the pivot $d = {ex(d)}$ m from the center of mass: $I = I_{{cm}} + Md^2 = "
            f"{fmt(Icm, 4)} + ({ex(M)})({ex(d)})^2 = {fmt(I, 4)}$ kg·m².",
            "For small angles the gravitational torque is $\\tau = -Mgd\\sin\\theta \\approx -Mgd\\theta$, so "
            "$I\\ddot\\theta = -Mgd\\theta$: simple harmonic motion with $T = 2\\pi\\sqrt{\\frac{I}{Mgd}}$.",
            f"$T = 2\\pi\\sqrt{{\\frac{{{fmt(I, 4)}}}{{({ex(M)})(9.81)({ex(d)})}}}} = {fmt(T)}$ s.",
            f"Equivalent simple pendulum: $L_{{eq}} = \\frac{{I}}{{Md}} = {fmt(Leq)}$ m (a simple pendulum of this length has "
            "the same period). The mass cancels in $T$.",
            f"Insight: for a rod the period is smallest when $d = L/\\sqrt{{12}} = {fmt(d_star)}$ m, where "
            f"$T_{{min}} = {fmt(T_min)}$ s; our period is not shorter than this. ✓",
        ]
        values = {"mode": mode, "L": L, "d": d, "M": M, "I": I, "T": T, "L_eq": Leq}
    elif mode == "disk":
        R = nice(rng, 0.05, 0.40, 0.01)
        d = nice(rng, 0.01, R, 0.01)
        M = nice(rng, 0.5, 5.0, 0.1)
        Icm = M * R * R / 2
        I = Icm + M * d * d
        T = 2 * math.pi * math.sqrt(I / (M * g * d))
        Leq = I / (M * d)
        where = ("a point on its rim" if math.isclose(d, R) else f"a point {qx(d, 'm')} from its center")
        question = (
            f"A uniform flat disk of mass {qx(M, 'kg')} and radius {qx(R, 'm')} hangs in a vertical plane from a horizontal "
            f"axle (perpendicular to the disk) through {where}. Find its moment of inertia about the axle and its period "
            "for small oscillations."
        )
        steps = [
            f"Moment of inertia of a disk about its central axis: $I_{{cm}} = \\tfrac12MR^2 = \\tfrac12({ex(M)})({ex(R)})^2 = {fmt(Icm, 4)}$ kg·m².",
            f"Parallel-axis theorem: $I = I_{{cm}} + Md^2 = {fmt(Icm, 4)} + ({ex(M)})({ex(d)})^2 = {fmt(I, 4)}$ kg·m².",
            "Small-angle restoring torque $-Mgd\\theta$ gives simple harmonic motion with $T = 2\\pi\\sqrt{\\frac{I}{Mgd}}$.",
            f"$T = 2\\pi\\sqrt{{\\frac{{{fmt(I, 4)}}}{{({ex(M)})(9.81)({ex(d)})}}}} = {fmt(T)}$ s.",
            f"Equivalent simple pendulum length: $L_{{eq}} = \\frac{{I}}{{Md}} = \\frac{{R^2/2 + d^2}}{{d}} = {fmt(Leq)}$ m; "
            "the mass cancels.",
            f"Insight: the period is shortest for a pivot at $d = R/\\sqrt2 = {fmt(R / math.sqrt(2))}$ m and grows without "
            "limit as the pivot approaches the center.",
        ]
        values = {"mode": mode, "R": R, "d": d, "M": M, "I": I, "T": T, "L_eq": Leq}
    else:
        L = nice(rng, 0.30, 1.50, 0.05)
        M = nice(rng, 0.10, 1.00, 0.05)
        mb = nice(rng, 0.10, 2.00, 0.05)
        I = M * L * L / 3 + mb * L * L
        dcm = (M * L / 2 + mb * L) / (M + mb)
        T = 2 * math.pi * math.sqrt(I / ((M + mb) * g * dcm))
        Leq = I / ((M + mb) * dcm)
        T0 = 2 * math.pi * math.sqrt(L / g)
        question = (
            f"A pendulum consists of a uniform rod of mass {qx(M, 'kg')} and length {qx(L, 'm')}, pivoted at its upper end, "
            f"with a small bob of mass {qx(mb, 'kg')} (treat it as a point mass) fixed to the lower end. Find the moment of "
            "inertia about the pivot, the distance of the center of mass below the pivot and the period for small "
            "oscillations. Compare with the period you would get by ignoring the rod's mass."
        )
        steps = [
            "Rod about its end, from the parallel-axis theorem: $I_{rod} = \\tfrac{1}{12}ML^2 + M\\left(\\tfrac{L}{2}\\right)^2 = "
            f"\\tfrac13ML^2 = {fmt(M * L * L / 3, 4)}$ kg·m².",
            f"Bob: $I_{{bob}} = mL^2 = ({ex(mb)})({ex(L)})^2 = {fmt(mb * L * L, 4)}$ kg·m². Total $I = {fmt(I, 4)}$ kg·m².",
            f"Center of mass below the pivot: $d = \\frac{{M(L/2) + mL}}{{M + m}} = \\frac{{({ex(M)})({fmt(L / 2, 4)}) + "
            f"({ex(mb)})({ex(L)})}}{{{ex(M + mb)}}} = {fmt(dcm, 4)}$ m.",
            f"Physical pendulum: $T = 2\\pi\\sqrt{{\\frac{{I}}{{(M + m)gd}}}} = 2\\pi\\sqrt{{\\frac{{{fmt(I, 4)}}}"
            f"{{({ex(M + mb)})(9.81)({fmt(dcm, 4)})}}}} = {fmt(T)}$ s.",
            f"Ignoring the rod (simple pendulum of length $L$): $T_0 = 2\\pi\\sqrt{{L/g}} = {fmt(T0)}$ s. The real period is "
            f"shorter (equivalent length $L_{{eq}} = I/[(M+m)d] = {fmt(Leq)}$ m $< L$) because part of the mass sits closer to the pivot.",
        ]
        values = {"mode": mode, "L": L, "M": M, "m": mb, "I": I, "d_cm": dcm, "T": T, "L_eq": Leq, "T0": T0}
    answer = f"$I = {fmt(I)}$ kg·m²; $T = {fmt(T)}$ s"
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Damped and driven oscillations
# ---------------------------------------------------------------------------

DAMPED_SETUPS = [
    "A {m} kg glider attached to a spring of stiffness {k} N/m oscillates on an air track and is slowed by a magnetic "
    "(eddy-current) brake that exerts a drag force $F = -bv$",
    "A {m} kg mass hangs from a spring of stiffness {k} N/m and is connected to a dashpot (viscous damper) that exerts "
    "a drag force $F = -bv$",
    "The {m} kg test mass of a simple seismometer is suspended from a spring of stiffness {k} N/m; its motion is damped "
    "by a viscous force $F = -bv$",
]


@template("damped_oscillator_q_factor", PHYS, MECH, "Oscillations", "hard")
def damped_oscillator_q_factor(rng):
    setup = pick(rng, DAMPED_SETUPS)
    if rng.random() < 0.55:
        mode = "forward"
        for _ in range(2000):
            m = nice(rng, 0.20, 5.00, 0.05)
            k = nice(rng, 10, 800, 10)
            b = nice(rng, 0.02, 4.00, 0.02)
            A0 = nice(rng, 2.0, 20.0, 1.0)
            t = nice(rng, 1, 60, 1)
            w0 = math.sqrt(k / m)
            gam = b / (2 * m)
            Q = w0 / (2 * gam)
            if 3 <= Q <= 200 and math.exp(-gam * t) >= 0.02:
                break
        else:
            raise RuntimeError("no valid damped oscillator")
        wd = math.sqrt(w0 * w0 - gam * gam)
        Td = 2 * math.pi / wd
        A = A0 * math.exp(-gam * t)
        t_half = math.log(2) / gam
        E_frac = math.exp(-2 * gam * t)
        intro = setup.format(m=f"${ex(m)}$", k=f"${ex(k)}$")
        question = (
            f"{intro} with $b = {ex(b)}$ kg/s. It is pulled {qx(A0, 'cm')} from equilibrium and released. Find the quality "
            f"factor $Q$, the damped period, the amplitude after {qx(t, 's')}, and the time for the amplitude to halve."
        )
        steps = [
            f"Natural angular frequency: $\\omega_0 = \\sqrt{{k/m}} = \\sqrt{{{ex(k)}/{ex(m)}}} = {fmt(w0, 4)}$ rad/s.",
            f"Damping rate: $\\gamma = \\frac{{b}}{{2m}} = \\frac{{{ex(b)}}}{{2({ex(m)})}} = {fmt(gam, 4)}$ s⁻¹; the amplitude "
            "decays as $A(t) = A_0e^{-\\gamma t}$.",
            f"Since $\\gamma < \\omega_0$ the motion is underdamped: $\\omega_d = \\sqrt{{\\omega_0^2 - \\gamma^2}} = {fmt(wd, 4)}$ rad/s, "
            f"damped period $T_d = 2\\pi/\\omega_d = {fmt(Td)}$ s.",
            f"Quality factor: $Q = \\frac{{\\omega_0}}{{2\\gamma}} = \\frac{{m\\omega_0}}{{b}} = {fmt(Q)}$ (roughly the number of "
            "radians of oscillation for the energy to fall by a factor $e$).",
            f"Amplitude after $t = {ex(t)}$ s (about ${fmt(t / Td)}$ oscillations): $A = A_0e^{{-\\gamma t}} = "
            f"({ex(A0)})e^{{-({fmt(gam, 4)})({ex(t)})}} = {fmt(A)}$ cm. The energy, proportional to $A^2$, has fallen to "
            f"${fmt(100 * E_frac)}$% of its initial value.",
            f"Half-amplitude time: $t_{{1/2}} = \\frac{{\\ln 2}}{{\\gamma}} = {fmt(t_half)}$ s.",
        ]
        answer = f"$Q = {fmt(Q)}$; $T_d = {fmt(Td)}$ s; $A = {fmt(A)}$ cm; $t_{{1/2}} = {fmt(t_half)}$ s"
        values = {"mode": mode, "m": m, "k": k, "b": b, "A0_cm": A0, "t": t, "omega0": w0, "gamma": gam,
                  "omega_d": wd, "Q": Q, "A_cm": A, "t_half": t_half}
    else:
        mode = "inverse"
        for _ in range(2000):
            m = nice(rng, 0.20, 5.00, 0.05)
            k = nice(rng, 10, 800, 10)
            A0 = nice(rng, 5.0, 20.0, 1.0)
            A1 = nice(rng, 1.0, A0 - 1, 0.5)
            t = nice(rng, 2, 60, 1)
            w0 = math.sqrt(k / m)
            gam = math.log(A0 / A1) / t
            Q = w0 / (2 * gam)
            if 3 <= Q <= 300:
                break
        else:
            raise RuntimeError("no valid damped oscillator")
        b = 2 * m * gam
        wd = math.sqrt(w0 * w0 - gam * gam)
        Td = 2 * math.pi / wd
        loss = 1 - math.exp(-2 * gam * Td)
        intro = setup.format(m=f"${ex(m)}$", k=f"${ex(k)}$")
        question = (
            f"{intro}. It is released from an amplitude of {qx(A0, 'cm')}, and {qx(t, 's')} later the amplitude has decreased "
            f"to {qx(A1, 'cm')}. Find the damping constant $b$, the quality factor $Q$, and the fraction of the oscillation "
            "energy lost per cycle."
        )
        steps = [
            "For linear damping the amplitude decays exponentially, $A(t) = A_0e^{-\\gamma t}$ with $\\gamma = b/(2m)$.",
            f"$\\gamma = \\frac{{\\ln(A_0/A)}}{{t}} = \\frac{{\\ln({ex(A0)}/{ex(A1)})}}{{{ex(t)}}} = {fmt(gam, 4)}$ s⁻¹.",
            f"Damping constant: $b = 2m\\gamma = 2({ex(m)})({fmt(gam, 4)}) = {fmt(b)}$ kg/s.",
            f"Natural angular frequency $\\omega_0 = \\sqrt{{k/m}} = {fmt(w0, 4)}$ rad/s, so $Q = \\frac{{\\omega_0}}{{2\\gamma}} = {fmt(Q)}$ "
            "(underdamped, since $Q > \\tfrac12$).",
            f"Damped period $T_d = 2\\pi/\\sqrt{{\\omega_0^2 - \\gamma^2}} = {fmt(Td)}$ s. Energy $\\propto A^2$ decays as "
            f"$e^{{-2\\gamma t}}$, so the fraction lost per cycle is $1 - e^{{-2\\gamma T_d}} = {fmt(loss)}$ (${fmt(100 * loss)}$%).",
        ]
        answer = f"$b = {fmt(b)}$ kg/s; $Q = {fmt(Q)}$; energy loss per cycle ${fmt(100 * loss)}$%"
        values = {"mode": mode, "m": m, "k": k, "A0_cm": A0, "A1_cm": A1, "t": t, "gamma": gam, "b": b,
                  "omega0": w0, "Q": Q, "T_d": Td, "loss_per_cycle": loss}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


DRIVEN_SETUPS = [
    "A {m} kg mass on a spring of stiffness {k} N/m, with a damper of constant {b} kg/s, is driven by a shaker that applies "
    "a sinusoidal force of amplitude {F}",
    "A {m} kg machine component sits on spring mounts of total stiffness {k} N/m with damping constant {b} kg/s; a motor "
    "subjects it to a sinusoidal force of amplitude {F}",
    "A {m} kg model building on a shake table behaves as a mass on a spring (stiffness {k} N/m, damping constant {b} kg/s) "
    "driven by a sinusoidal force of amplitude {F}",
]


@template("driven_oscillator_resonance", PHYS, MECH, "Oscillations", "hard")
def driven_oscillator_resonance(rng):
    for _ in range(5000):
        m = nice(rng, 0.5, 5.0, 0.1)
        k = nice(rng, 50, 2000, 10)
        b = nice(rng, 0.2, 10.0, 0.1)
        w0 = math.sqrt(k / m)
        Q = m * w0 / b
        if 3 <= Q <= 60:
            break
    else:
        raise RuntimeError("no valid driven oscillator")
    F0 = nice(rng, 1, 30, 1)
    f0 = w0 / (2 * math.pi)
    lo = max(0.05, round(0.3 * f0 / 0.05) * 0.05)
    hi = round(2.0 * f0 / 0.05) * 0.05
    for _ in range(1000):
        fd = nice(rng, lo, hi, 0.05)
        if abs(fd / f0 - 1) > 0.03:
            break
    else:
        raise RuntimeError("no valid driving frequency")
    w = 2 * math.pi * fd
    gterm = b * w / m
    A = (F0 / m) / math.sqrt((w0 * w0 - w * w) ** 2 + gterm ** 2)
    delta = math.degrees(math.atan2(gterm, w0 * w0 - w * w))
    A_res = F0 / (b * w0)
    x_static = F0 / k
    setup = pick(rng, DRIVEN_SETUPS).format(m=f"${ex(m)}$", k=f"${ex(k)}$", b=f"${ex(b)}$", F=qx(F0, "N"))
    question = (
        f"{setup} at a frequency of {qx(fd, 'Hz')}. Find the steady-state amplitude and the phase lag of the displacement "
        "behind the force. What would the amplitude be if the driving frequency were tuned to the natural frequency "
        "$f_0$, and what is the quality factor of the system?"
    )
    side = "below" if fd < f0 else "above"
    steps = [
        f"Natural angular frequency: $\\omega_0 = \\sqrt{{k/m}} = \\sqrt{{{ex(k)}/{ex(m)}}} = {fmt(w0, 4)}$ rad/s, "
        f"i.e. $f_0 = {fmt(f0, 4)}$ Hz. Driving angular frequency: $\\omega = 2\\pi f = {fmt(w, 4)}$ rad/s.",
        "Steady-state amplitude of $m\\ddot x + b\\dot x + kx = F_0\\cos\\omega t$: "
        "$A = \\frac{F_0/m}{\\sqrt{(\\omega_0^2 - \\omega^2)^2 + (b\\omega/m)^2}}$.",
        f"$A = \\frac{{{ex(F0)}/{ex(m)}}}{{\\sqrt{{({fmt(w0 * w0, 4)} - {fmt(w * w, 4)})^2 + ({fmt(gterm, 4)})^2}}}} = "
        f"{fmt(A)}$ m $= {fmt(100 * A)}$ cm.",
        f"Phase lag: $\\tan\\delta = \\frac{{b\\omega/m}}{{\\omega_0^2 - \\omega^2}} \\Rightarrow \\delta = {fmt(delta)}°$ "
        f"(driving {side} resonance, so $\\delta$ is {'less' if fd < f0 else 'more'} than $90°$).",
        f"Driven at $\\omega = \\omega_0$: $A_0 = \\frac{{F_0}}{{b\\omega_0}} = \\frac{{{ex(F0)}}}{{({ex(b)})({fmt(w0, 4)})}} = "
        f"{fmt(A_res)}$ m $= {fmt(100 * A_res)}$ cm, ${fmt(A_res / A)}$ times the amplitude found above.",
        f"Quality factor: $Q = \\frac{{m\\omega_0}}{{b}} = {fmt(Q)}$. Check: the static deflection is $F_0/k = {fmt(100 * x_static)}$ cm "
        f"and $A_0/(F_0/k) = {fmt(A_res / x_static)} = Q$ ✓ — at resonance the response is amplified $Q$ times.",
    ]
    answer = (f"$A = {fmt(100 * A)}$ cm, $\\delta = {fmt(delta)}°$; at $f_0 = {fmt(f0)}$ Hz, $A_0 = {fmt(100 * A_res)}$ cm; "
              f"$Q = {fmt(Q)}$")
    values = {"m": m, "k": k, "b": b, "F0": F0, "f_drive": fd, "omega0": w0, "A": A, "delta_deg": delta,
              "A_res": A_res, "Q": Q}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Orbits
# ---------------------------------------------------------------------------

EARTH_DATA = "$GM_E = 3.986 \\times 10^{14}$ m³/s² and $R_E = 6371$ km"


@template("hohmann_transfer_earth_orbits", PHYS, MECH, "Gravitation", "hard")
def hohmann_transfer_earth_orbits(rng):
    h1 = nice(rng, 200, 1000, 10)
    target = pick(rng, ["geo", "gps", "other", "other"])
    if target == "geo":
        h2, tname = 35786, "geostationary orbit"
    elif target == "gps":
        h2, tname = 20200, "GPS-like medium Earth orbit"
    else:
        h2, tname = nice(rng, 2000, 40000, 100), "higher circular orbit"
    r1 = (R_EARTH_KM + h1) * 1000.0
    r2 = (R_EARTH_KM + h2) * 1000.0
    a = (r1 + r2) / 2
    v1 = math.sqrt(MU_EARTH / r1)
    v2 = math.sqrt(MU_EARTH / r2)
    vp = math.sqrt(MU_EARTH * (2 / r1 - 1 / a))
    va = math.sqrt(MU_EARTH * (2 / r2 - 1 / a))
    dv1, dv2 = vp - v1, v2 - va
    dv = dv1 + dv2
    t_tr = math.pi * math.sqrt(a ** 3 / MU_EARTH)
    rocket = rng.random() < 0.5
    question = (
        f"A satellite is in a circular orbit at an altitude of {qx(h1, 'km')} above Earth. It is to be moved to a {tname} at "
        f"an altitude of {qx(h2, 'km')} by a Hohmann transfer: a tangential burn that puts it on an elliptical transfer "
        "orbit, and a second tangential burn at apogee to circularize. Using "
        f"{EARTH_DATA}, find the two velocity changes, the total $\\Delta v$ and the time spent on the transfer orbit."
    )
    values = {"h1_km": h1, "h2_km": h2, "r1": r1, "r2": r2, "a": a, "v1": v1, "v2": v2, "v_p": vp, "v_a": va,
              "dv1": dv1, "dv2": dv2, "dv_total": dv, "t_transfer": t_tr}
    steps = [
        f"Orbital radii: $r_1 = R_E + h_1 = {ex(R_EARTH_KM + h1)}$ km, $r_2 = R_E + h_2 = {ex(R_EARTH_KM + h2)}$ km. "
        f"The transfer ellipse touches both, so its semi-major axis is $a = \\frac{{r_1 + r_2}}{{2}} = {fmt(a / 1000, 5)}$ km.",
        f"Circular-orbit speeds, $v = \\sqrt{{GM/r}}$: $v_1 = {fmt(v1, 4)}$ m/s and $v_2 = {fmt(v2, 4)}$ m/s.",
        "On the ellipse the vis-viva equation $v^2 = GM\\left(\\frac{2}{r} - \\frac{1}{a}\\right)$ gives "
        f"$v_p = {fmt(vp, 4)}$ m/s at perigee ($r_1$) and $v_a = {fmt(va, 4)}$ m/s at apogee ($r_2$).",
        f"Check: angular momentum is conserved on the ellipse, $r_1v_p = r_2v_a = {fmt(r1 * vp, 4)}$ m²/s. ✓",
        f"Burns: $\\Delta v_1 = v_p - v_1 = {fmt(dv1)}$ m/s and $\\Delta v_2 = v_2 - v_a = {fmt(dv2)}$ m/s (both prograde); "
        f"total $\\Delta v = {fmt(dv)}$ m/s $= {fmt(dv / 1000)}$ km/s.",
        f"Transfer time = half the period of the ellipse: $t = \\pi\\sqrt{{\\frac{{a^3}}{{GM}}}} = {fmt(t_tr)}$ s $= {fmt(t_tr / 3600)}$ h.",
    ]
    answer = (f"$\\Delta v_1 = {fmt(dv1)}$ m/s, $\\Delta v_2 = {fmt(dv2)}$ m/s, total ${fmt(dv / 1000)}$ km/s; "
              f"transfer time ${fmt(t_tr / 3600)}$ h")
    if rocket:
        m0 = nice(rng, 500, 6000, 100)
        ve = nice(rng, 2.5, 4.5, 0.1)
        mf = m0 * math.exp(-dv / (ve * 1000))
        mp = m0 - mf
        question += (f" The satellite's mass before the first burn is {qx(m0, 'kg')} and its engine's exhaust speed is "
                     f"{qx(ve, 'km/s')}; how much propellant does the transfer use?")
        steps.append(
            f"Rocket equation: $m_f = m_0e^{{-\\Delta v/v_e}} = ({ex(m0)})e^{{-{fmt(dv, 4)}/{fmt(ve * 1000, 4)}}} = {fmt(mf)}$ kg, "
            f"so the propellant used is $m_0 - m_f = {fmt(mp)}$ kg (${fmt(100 * mp / m0)}$% of the initial mass)."
        )
        answer += f"; propellant ${fmt(mp)}$ kg"
        values.update({"m0": m0, "ve_kms": ve, "m_prop": mp})
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("satellite_orbital_energy_budget", PHYS, MECH, "Gravitation", "medium")
def satellite_orbital_energy_budget(rng):
    m = nice(rng, 100, 5000, 50)
    R = R_EARTH_KM * 1000.0
    if rng.random() < 0.5:
        mode = "launch"
        h = pick(rng, [400, 550, 800, 20200, 35786]) if rng.random() < 0.3 else nice(rng, 200, 36000, 10)
        r = R + h * 1000
        v = math.sqrt(MU_EARTH / r)
        KE = MU_EARTH * m / (2 * r)
        U = -MU_EARTH * m / r
        E = KE + U
        U0 = -MU_EARTH * m / R
        E_need = E - U0
        question = (
            f"A {qx(m, 'kg')} satellite is in a circular orbit {qx(h, 'km')} above Earth's surface. Using {EARTH_DATA}, find "
            "its kinetic, potential and total mechanical energy, its binding energy, and the minimum energy needed to "
            "place it in this orbit from rest on the ground (ignore Earth's rotation, air drag and the rocket's own mass)."
        )
        steps = [
            f"Orbital radius: $r = R_E + h = {fmt(r, 5)}$ m. Orbital speed $v = \\sqrt{{GM_E/r}} = {fmt(v, 4)}$ m/s.",
            f"Kinetic energy: $K = \\tfrac12mv^2 = \\frac{{GM_Em}}{{2r}} = {fmt(KE, 4)}$ J.",
            f"Potential energy (zero at infinity): $U = -\\frac{{GM_Em}}{{r}} = {fmt(U, 4)}$ J $= -2K$.",
            f"Total energy: $E = K + U = -\\frac{{GM_Em}}{{2r}} = {fmt(E, 4)}$ J $= -K$ (negative: the satellite is bound). "
            f"Binding energy $= -E = {fmt(-E, 4)}$ J.",
            f"On the ground at rest: $E_0 = U_0 = -\\frac{{GM_Em}}{{R_E}} = {fmt(U0, 4)}$ J. Minimum energy to supply: "
            f"$\\Delta E = E - E_0 = GM_Em\\left(\\frac{{1}}{{R_E}} - \\frac{{1}}{{2r}}\\right) = {fmt(E_need, 4)}$ J $= {fmt(E_need / 1e9)}$ GJ.",
            f"Of this, ${fmt(100 * KE / E_need)}$% ends up as kinetic energy and the rest as gained potential energy.",
        ]
        answer = (f"$K = {fmt(KE)}$ J, $U = {fmt(U)}$ J, $E = {fmt(E)}$ J (binding energy ${fmt(-E)}$ J); "
                  f"energy needed ${fmt(E_need / 1e9)}$ GJ")
        values = {"mode": mode, "m": m, "h_km": h, "r": r, "v": v, "KE": KE, "U": U, "E": E, "E_needed": E_need}
    else:
        mode = "raise"
        for _ in range(1000):
            h1 = nice(rng, 200, 2000, 10)
            h2 = nice(rng, 1000, 40000, 100)
            if h2 >= h1 + 300:
                break
        else:
            raise RuntimeError("no valid orbit pair")
        r1, r2 = R + h1 * 1000, R + h2 * 1000
        E1 = -MU_EARTH * m / (2 * r1)
        E2 = -MU_EARTH * m / (2 * r2)
        dE = E2 - E1
        v1, v2 = math.sqrt(MU_EARTH / r1), math.sqrt(MU_EARTH / r2)
        dK = 0.5 * m * (v2 * v2 - v1 * v1)
        dU = MU_EARTH * m * (1 / r1 - 1 / r2)
        question = (
            f"A {qx(m, 'kg')} satellite is moved from a circular orbit {qx(h1, 'km')} above Earth to a circular orbit "
            f"{qx(h2, 'km')} above Earth. Using {EARTH_DATA}, find the change in its total mechanical energy, and the changes "
            "in its kinetic and potential energy. Does it speed up or slow down?"
        )
        steps = [
            f"Radii: $r_1 = {fmt(r1, 5)}$ m, $r_2 = {fmt(r2, 5)}$ m. For a circular orbit $E = -\\frac{{GM_Em}}{{2r}}$.",
            f"$E_1 = {fmt(E1, 4)}$ J and $E_2 = {fmt(E2, 4)}$ J, so $\\Delta E = \\frac{{GM_Em}}{{2}}\\left(\\frac{{1}}{{r_1}} - "
            f"\\frac{{1}}{{r_2}}\\right) = {fmt(dE, 4)}$ J $= {fmt(dE / 1e9)}$ GJ (energy must be supplied).",
            f"Speeds: $v_1 = \\sqrt{{GM_E/r_1}} = {fmt(v1, 4)}$ m/s and $v_2 = {fmt(v2, 4)}$ m/s, so "
            f"$\\Delta K = {fmt(dK, 4)}$ J: the satellite slows down.",
            f"$\\Delta U = GM_Em\\left(\\frac{{1}}{{r_1}} - \\frac{{1}}{{r_2}}\\right) = {fmt(dU, 4)}$ J $= 2\\Delta E$.",
            "Check: $\\Delta K + \\Delta U = \\Delta E$ and $\\Delta K = -\\Delta E$ ✓ — adding energy to a satellite raises its "
            "orbit but lowers its speed.",
        ]
        answer = f"$\\Delta E = {fmt(dE)}$ J; $\\Delta K = {fmt(dK)}$ J (it slows down); $\\Delta U = {fmt(dU)}$ J"
        values = {"mode": mode, "m": m, "h1_km": h1, "h2_km": h2, "dE": dE, "dK": dK, "dU": dU}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Fluids
# ---------------------------------------------------------------------------

STOKES_CASES = [
    # particle, fluid, rho_s, rho_f, eta, radius unit, radius range, height unit, height range
    ("spherical fog droplet of water", "still air", 1000, 1.20, 1.81e-5, "µm", (2, 30, 1), "m", (5, 200, 5)),
    ("spherical silt grain of quartz", "still water", 2650, 998, 1.00e-3, "µm", (5, 40, 1), "m", (0.5, 5.0, 0.1)),
    ("steel ball bearing", "glycerin", 7800, 1260, 1.41, "mm", (0.5, 3.0, 0.1), "cm", (20, 100, 5)),
    ("glass bead", "castor oil", 2500, 961, 0.99, "mm", (0.5, 3.0, 0.1), "cm", (20, 100, 5)),
]


@template("stokes_terminal_velocity", PHYS, MECH, "Fluids", "medium")
def stokes_terminal_velocity(rng):
    if rng.random() < 0.7:
        mode = "terminal"
        part, fluid, rs, rf, eta, runit, r_rng, hunit, h_rng = pick(rng, STOKES_CASES)
        r_disp = draw(rng, r_rng)
        r = r_disp * (1e-6 if runit == "µm" else 1e-3)
        H_disp = draw(rng, h_rng)
        H = H_disp / 100 if hunit == "cm" else H_disp
        v = 2 * r * r * (rs - rf) * g / (9 * eta)
        Re = rf * v * 2 * r / eta
        t = H / v
        tau = 2 * r * r * rs / (9 * eta)
        question = (
            f"A {part} of radius {qx(r_disp, runit)} (density {qx(rs, 'kg/m³')}) falls through {fluid} (density "
            f"{qx(rf, 'kg/m³')}, viscosity {qx(eta, 'Pa·s')}). Assuming Stokes' drag law, find its terminal velocity, check "
            f"that the Reynolds number is small enough for Stokes' law to apply, and estimate how long it takes to fall "
            f"{qx(H_disp, hunit)} at this speed."
        )
        steps = [
            "At terminal velocity the net force is zero: weight = buoyancy + drag, "
            "$\\tfrac43\\pi r^3\\rho_sg = \\tfrac43\\pi r^3\\rho_fg + 6\\pi\\eta rv_t$.",
            f"Solving: $v_t = \\frac{{2r^2(\\rho_s - \\rho_f)g}}{{9\\eta}} = \\frac{{2({ex(r)})^2({ex(rs)} - {ex(rf)})(9.81)}}"
            f"{{9({ex(eta)})}} = {fmt(v)}$ m/s.",
            f"Reynolds number: $Re = \\frac{{\\rho_fv_t(2r)}}{{\\eta}} = {fmt(Re)}$, well below 1, so the flow around the "
            "particle is creeping flow and Stokes' law is valid.",
            f"Time to fall $H = {ex(H)}$ m: $t = H/v_t = {fmt(t)}$ s" + (f" $= {fmt(t / 60)}$ min." if t > 120 else "."),
            f"The particle reaches terminal velocity almost at once: the response time $\\tau = \\frac{{2r^2\\rho_s}}{{9\\eta}} = "
            f"{fmt(tau)}$ s is negligible compared with $t$.",
        ]
        answer = f"$v_t = {fmt(v)}$ m/s; $Re = {fmt(Re)}$; fall time ${fmt(t)}$ s"
        values = {"mode": mode, "rho_s": rs, "rho_f": rf, "eta": eta, "r": r, "r_disp": r_disp, "H": H, "H_disp": H_disp,
                  "v_t": v, "Re": Re, "t_fall": t, "tau": tau}
    else:
        mode = "viscometer"
        rs = 7800
        for _ in range(5000):
            rf = nice(rng, 850, 960, 10)
            r_mm = nice(rng, 0.5, 2.0, 0.1)
            D_cm = nice(rng, 10, 50, 5)
            t = nice(rng, 1.0, 60.0, 0.1)
            r = r_mm / 1000
            v = D_cm / 100 / t
            eta = 2 * r * r * (rs - rf) * g / (9 * v)
            Re = rf * v * 2 * r / eta
            if 0.05 <= eta <= 3.0 and Re < 0.5:
                break
        else:
            raise RuntimeError("no valid viscometer data")
        question = (
            f"In a falling-ball viscometer a steel ball (density {qx(rs, 'kg/m³')}) of radius {qx(r_mm, 'mm')} is dropped into "
            f"an oil of density {qx(rf, 'kg/m³')}. After reaching terminal velocity it takes {qx(t, 's')} to fall between two "
            f"marks {qx(D_cm, 'cm')} apart. Find the viscosity of the oil and check that Stokes' law applies."
        )
        steps = [
            f"Terminal velocity: $v_t = \\frac{{d}}{{t}} = \\frac{{{fmt(D_cm / 100, 3)}}}{{{ex(t)}}} = {fmt(v)}$ m/s.",
            "Force balance at terminal velocity (weight = buoyancy + Stokes drag $6\\pi\\eta rv_t$) gives "
            "$\\eta = \\frac{2r^2(\\rho_s - \\rho_f)g}{9v_t}$.",
            f"$\\eta = \\frac{{2({ex(r)})^2({ex(rs)} - {ex(rf)})(9.81)}}{{9({fmt(v, 4)})}} = {fmt(eta)}$ Pa·s.",
            f"Check: $Re = \\frac{{\\rho_fv_t(2r)}}{{\\eta}} = {fmt(Re)} \\ll 1$, so Stokes' law holds (wall effects of the "
            "tube are neglected).",
        ]
        answer = f"$\\eta = {fmt(eta)}$ Pa·s ($Re = {fmt(Re)}$)"
        values = {"mode": mode, "rho_s": rs, "rho_f": rf, "r": r, "r_mm": r_mm, "D_cm": D_cm, "t": t, "v_t": v,
                  "eta": eta, "Re": Re}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


TANKS = [
    # tank, depth above hole (m), hole height (m), hole diameter (mm), tank diameter (m)
    ("large open water tank", (0.5, 4.0, 0.1), (0.5, 3.0, 0.1), (5, 20, 1), (1.5, 4.0, 0.1)),
    ("rain barrel", (0.20, 0.90, 0.05), (0.20, 1.00, 0.05), (3, 12, 1), (0.50, 0.70, 0.05)),
    ("tall cylindrical water cistern", (0.5, 2.5, 0.1), (1.0, 4.0, 0.1), (5, 25, 1), (1.0, 2.5, 0.1)),
]


@template("torricelli_efflux_jet", PHYS, MECH, "Fluids", "medium")
def torricelli_efflux_jet(rng):
    tank, h_rng, y_rng, d_rng, D_rng = pick(rng, TANKS)
    h = draw(rng, h_rng)
    y = draw(rng, y_rng)
    d_mm = draw(rng, d_rng)
    d = d_mm / 1000
    v = math.sqrt(2 * g * h)
    a = math.pi * d * d / 4
    Q = a * v
    tf = math.sqrt(2 * y / g)
    x = v * tf
    H = h + y
    drain = rng.random() < 0.5
    question = (
        f"A {tank} open to the air stands on level ground. A small round hole of diameter {qx(d_mm, 'mm')} is opened in its "
        f"side, {qx(y, 'm')} above the ground, while the water surface is {qx(h, 'm')} above the hole. Treat the water as an "
        "ideal fluid (no viscous losses, jet area equal to the hole area) and neglect air resistance. At this instant, find "
        "(a) the speed of the water leaving the hole, (b) the volume flow rate, and (c) how far from the base of the tank "
        "the jet lands."
    )
    steps = [
        "Bernoulli's equation from the free surface (pressure $p_0$, speed ≈ 0 because the tank is much wider than the "
        "hole) to the jet (also at $p_0$): $\\rho gh = \\tfrac12\\rho v^2$.",
        f"Torricelli's law: $v = \\sqrt{{2gh}} = \\sqrt{{2(9.81)({ex(h)})}} = {fmt(v)}$ m/s — the speed of a body falling freely through $h$.",
        f"Flow rate: $Q = Av = \\frac{{\\pi d^2}}{{4}}v = \\frac{{\\pi({ex(d)})^2}}{{4}}({fmt(v, 4)}) = {fmt(Q)}$ m³/s "
        f"$= {fmt(Q * 1000)}$ L/s $= {fmt(Q * 60000)}$ L/min.",
        f"The jet leaves horizontally and falls $y = {ex(y)}$ m in $t = \\sqrt{{2y/g}} = {fmt(tf)}$ s, so it lands "
        f"$x = vt = 2\\sqrt{{hy}} = {fmt(x)}$ m from the tank.",
        f"Check: with the surface $H = h + y = {ex(H)}$ m above the ground, $2\\sqrt{{hy}}$ is largest for a hole at "
        f"$y = H/2$, where $x_{{max}} = H = {ex(H)}$ m; our range ${fmt(x)}$ m does not exceed this. ✓",
    ]
    answer = f"$v = {fmt(v)}$ m/s; $Q = {fmt(Q * 1000)}$ L/s; range ${fmt(x)}$ m"
    values = {"h": h, "y": y, "d_mm": d_mm, "v": v, "Q": Q, "x": x}
    if drain:
        D = draw(rng, D_rng)
        t_drain = (D / d) ** 2 * math.sqrt(2 * h / g)
        question += (f" (d) The tank is a vertical cylinder of inner diameter {qx(D, 'm')}. How long does it take for the "
                     "water level to fall to the hole?")
        steps.append(
            f"Draining: $A_T\\frac{{dh}}{{dt}} = -A\\sqrt{{2gh}}$ integrates to $t = \\frac{{A_T}}{{A}}\\sqrt{{\\frac{{2h}}{{g}}}} = "
            f"\\left(\\frac{{{ex(D)}}}{{{ex(d)}}}\\right)^2\\sqrt{{\\frac{{2({ex(h)})}}{{9.81}}}} = {fmt(t_drain)}$ s "
            f"$= {fmt(t_drain / 3600)}$ h — twice as long as if the initial flow rate were maintained."
        )
        answer += f"; drain time ${fmt(t_drain / 3600)}$ h"
        values.update({"D_tank": D, "t_drain": t_drain})
    return {"question": question, "steps": steps, "answer": answer, "values": values}


PIPE_CASES = [
    # description, fluid, eta, rho, (r unit, scale, range), (L unit, scale, range), (dP unit, scale, range), Q unit/scale
    ("Blood flows through an arteriole", "blood", 3.5e-3, 1060, ("µm", 1e-6, (20, 75, 5)), ("mm", 1e-3, (1, 10, 1)),
     ("mmHg", MMHG, (5, 40, 1)), ("mm³/s", 1e9)),
    ("Saline solution flows through a hypodermic needle", "saline", 1.0e-3, 1005, ("mm", 1e-3, (0.10, 0.30, 0.01)),
     ("cm", 1e-2, (2.0, 5.0, 0.5)), ("kPa", 1e3, (1.0, 15.0, 0.5)), ("mL/s", 1e6)),
    ("Lubricating oil is pumped through a straight pipe", "oil", 0.20, 880, ("cm", 1e-2, (0.5, 2.5, 0.1)),
     ("m", 1.0, (1, 20, 1)), ("kPa", 1e3, (5, 100, 5)), ("L/min", 6e4)),
    ("Glycerin flows through a laboratory tube", "glycerin", 1.41, 1260, ("mm", 1e-3, (1.0, 5.0, 0.5)),
     ("cm", 1e-2, (20, 100, 5)), ("kPa", 1e3, (2, 50, 1)), ("mL/s", 1e6)),
]


@template("poiseuille_pipe_flow", PHYS, MECH, "Fluids", "medium")
def poiseuille_pipe_flow(rng):
    desc, fluid, eta, rho, (ru, rs, r_rng), (Lu, Ls, L_rng), (pu, ps, p_rng), (qu, qs) = pick(rng, PIPE_CASES)
    for _ in range(5000):
        r_d, L_d, p_d = draw(rng, r_rng), draw(rng, L_rng), draw(rng, p_rng)
        r, L, dP = r_d * rs, L_d * Ls, p_d * ps
        Q = math.pi * r ** 4 * dP / (8 * eta * L)
        vbar = Q / (math.pi * r * r)
        Re = rho * vbar * 2 * r / eta
        if Re < 2000:
            break
    else:
        raise RuntimeError("no laminar pipe-flow parameters")
    p = nice(rng, 5, 30, 5)
    factor = (1 - p / 100) ** 4
    Q2 = Q * factor
    question = (
        f"{desc} of inner radius {qx(r_d, ru)} and length {qx(L_d, Lu)}; the pressure difference between its ends is "
        f"{qx(p_d, pu)}. Treat the {fluid} as a Newtonian fluid of viscosity {qx(eta, 'Pa·s')} and density "
        f"{qx(rho, 'kg/m³')} in steady laminar flow. Find the volume flow rate and the mean flow speed, and confirm that "
        f"the flow is laminar. What does the flow rate become if the radius is reduced by {qx(p)}% with the same pressure "
        "difference?"
    )
    conv = f"$\\Delta P = {ex(p_d)} \\times {ex(ps)} = {fmt(dP, 4)}$ Pa" if pu == "mmHg" else f"$\\Delta P = {fmt(dP, 4)}$ Pa"
    steps = [
        f"SI units: $r = {ex(r)}$ m, $L = {ex(L)}$ m, {conv}" + (" (1 mmHg = 133.3 Pa)." if pu == "mmHg" else "."),
        f"Poiseuille's law: $Q = \\frac{{\\pi r^4\\Delta P}}{{8\\eta L}} = \\frac{{\\pi({ex(r)})^4({fmt(dP, 4)})}}{{8({ex(eta)})({ex(L)})}} = "
        f"{fmt(Q)}$ m³/s $= {fmt(Q * qs)}$ {qu}.",
        f"Mean speed: $\\bar v = \\frac{{Q}}{{\\pi r^2}} = {fmt(vbar)}$ m/s (the parabolic profile has twice this speed, "
        f"${fmt(2 * vbar)}$ m/s, on the axis).",
        f"Reynolds number: $Re = \\frac{{\\rho\\bar v(2r)}}{{\\eta}} = {fmt(Re)} < 2000$, so the flow is laminar and "
        "Poiseuille's law applies.",
        f"Because $Q \\propto r^4$, reducing the radius by ${p}$% multiplies the flow by $(1 - {ex(p / 100, 1)})^4 = {fmt(factor, 4)}$: "
        f"$Q' = {fmt(Q2)}$ m³/s $= {fmt(Q2 * qs)}$ {qu}, a ${fmt(100 * (1 - factor))}$% drop. "
        + ("This strong radius dependence is how arterioles regulate blood flow." if fluid == "blood" else
           "Halving the radius would cut the flow sixteen-fold."),
    ]
    answer = f"$Q = {fmt(Q * qs)}$ {qu}; $\\bar v = {fmt(vbar)}$ m/s; $Re = {fmt(Re)}$; $Q' = {fmt(Q2 * qs)}$ {qu}"
    values = {"r": r, "L": L, "dP": dP, "eta": eta, "rho": rho, "r_disp": r_d, "L_disp": L_d, "dP_disp": p_d,
              "Q": Q, "v_mean": vbar, "Re": Re, "reduction_pct": p, "Q_reduced": Q2}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Momentum
# ---------------------------------------------------------------------------


@template("ballistic_pendulum_speed", PHYS, MECH, "Momentum", "medium")
def ballistic_pendulum_speed(rng):
    if rng.random() < 0.55:
        mode = "find_speed"
        for _ in range(2000):
            m_g = nice(rng, 5, 30, 1)
            m = m_g / 1000
            M = nice(rng, 1.0, 8.0, 0.1)
            h_cm = nice(rng, 1.0, 40.0, 0.5)
            V = math.sqrt(2 * g * h_cm / 100)
            v = (m + M) / m * V
            if 150 <= v <= 1200:
                break
        else:
            raise RuntimeError("no valid ballistic pendulum data")
        frac_lost = M / (m + M)
        question = (
            f"A {qx(m_g, 'g')} bullet is fired horizontally into a {qx(M, 'kg')} wooden block hanging at rest from long light "
            f"strings (a ballistic pendulum). The bullet embeds itself in the block, which swings up so that its center of "
            f"mass rises {qx(h_cm, 'cm')}. What was the bullet's speed, and what fraction of its kinetic energy was lost in "
            "the collision?"
        )
        steps = [
            "Work backwards in two stages. Swing stage: after the collision only gravity does work, so mechanical energy is "
            "conserved: $\\tfrac12(m + M)V^2 = (m + M)gh$.",
            f"$V = \\sqrt{{2gh}} = \\sqrt{{2(9.81)({fmt(h_cm / 100, 3)})}} = {fmt(V)}$ m/s just after the collision.",
            "Collision stage: the impact is very brief and the strings are vertical, so horizontal momentum is conserved "
            "(kinetic energy is not — the collision is perfectly inelastic): $mv = (m + M)V$.",
            f"$v = \\frac{{m + M}}{{m}}V = \\frac{{{ex(m)} + {ex(M)}}}{{{ex(m)}}}({fmt(V, 4)}) = {fmt(v)}$ m/s.",
            f"Energy: $K_i = \\tfrac12mv^2 = {fmt(0.5 * m * v * v)}$ J, $K_f = \\tfrac12(m + M)V^2 = {fmt(0.5 * (m + M) * V * V)}$ J. "
            f"Fraction lost $= \\frac{{M}}{{m + M}} = {fmt(frac_lost, 4)}$ (${fmt(100 * frac_lost, 4)}$%), converted to heat and "
            "deformation of the wood.",
        ]
        answer = f"$v = {fmt(v)}$ m/s; ${fmt(100 * frac_lost, 4)}$% of the kinetic energy is lost"
        values = {"mode": mode, "m_g": m_g, "M": M, "h_cm": h_cm, "V": V, "v": v, "frac_lost": frac_lost}
    else:
        mode = "find_angle"
        for _ in range(2000):
            m_g = nice(rng, 5, 30, 1)
            m = m_g / 1000
            M = nice(rng, 1.0, 8.0, 0.1)
            v = nice(rng, 150, 900, 10)
            L = nice(rng, 0.5, 3.0, 0.1)
            V = m * v / (m + M)
            h = V * V / (2 * g)
            if h < L * (1 - math.cos(math.radians(75))):
                break
        else:
            raise RuntimeError("no valid ballistic pendulum data")
        frac_lost = M / (m + M)
        th = math.degrees(math.acos(1 - h / L))
        question = (
            f"A {qx(m_g, 'g')} bullet moving horizontally at {qx(v, 'm/s')} embeds itself in a {qx(M, 'kg')} block hanging at rest "
            f"from a light cord of length {qx(L, 'm')} (a ballistic pendulum). Find the speed of the block just after the "
            "impact, the height it rises, and the maximum angle the cord makes with the vertical."
        )
        steps = [
            "Collision (very brief, cord vertical): horizontal momentum is conserved, $mv = (m + M)V$.",
            f"$V = \\frac{{mv}}{{m + M}} = \\frac{{({ex(m)})({ex(v)})}}{{{ex(m + M)}}} = {fmt(V)}$ m/s.",
            f"Swing: mechanical energy is conserved, $\\tfrac12V^2 = gh \\Rightarrow h = \\frac{{V^2}}{{2g}} = {fmt(h)}$ m "
            f"$= {fmt(100 * h)}$ cm.",
            f"Geometry: $h = L(1 - \\cos\\theta) \\Rightarrow \\cos\\theta = 1 - \\frac{{h}}{{L}} = {fmt(1 - h / L, 4)}$, so "
            f"$\\theta = {fmt(th)}°$.",
            f"Only $\\frac{{m}}{{m + M}} = {fmt(100 * (1 - frac_lost))}$% of the bullet's kinetic energy survives the collision; "
            "using energy conservation through the impact would be wrong.",
        ]
        answer = f"$V = {fmt(V)}$ m/s; $h = {fmt(100 * h)}$ cm; $\\theta = {fmt(th)}°$"
        values = {"mode": mode, "m_g": m_g, "M": M, "v": v, "L": L, "V": V, "h": h, "theta_deg": th}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("recoil_momentum_conservation", PHYS, MECH, "Momentum", "easy")
def recoil_momentum_conservation(rng):
    mode = pick(rng, ["rifle", "rifle", "cannon", "astronaut"])
    if mode == "rifle":
        M = nice(rng, 2.5, 6.0, 0.1)
        m_g = nice(rng, 4, 15, 1)
        m = m_g / 1000
        v = nice(rng, 300, 1000, 10)
        d_cm = nice(rng, 2, 10, 1)
        V = m * v / M
        Kb, Kg = 0.5 * m * v * v, 0.5 * M * V * V
        F = Kg / (d_cm / 100)
        question = (
            f"A {qx(M, 'kg')} rifle, initially at rest, fires a {qx(m_g, 'g')} bullet horizontally with a speed of {qx(v, 'm/s')} "
            f"relative to the ground. Find the recoil speed of the rifle and compare the kinetic energies of the bullet and "
            f"the rifle. If the shooter's shoulder brings the rifle to rest over {qx(d_cm, 'cm')}, what average force does it "
            "exert? (Neglect the momentum of the propellant gases.)"
        )
        steps = [
            "The system (rifle + bullet) starts at rest, and during firing only internal forces act horizontally, so total "
            "momentum stays zero: $0 = mv + MV$.",
            f"$V = -\\frac{{mv}}{{M}} = -\\frac{{({ex(m)})({ex(v)})}}{{{ex(M)}}} = -{fmt(V)}$ m/s: the rifle recoils at "
            f"${fmt(V)}$ m/s opposite to the bullet.",
            f"Kinetic energies: bullet $\\tfrac12mv^2 = {fmt(Kb)}$ J; rifle $\\tfrac12MV^2 = {fmt(Kg)}$ J. Their ratio is "
            f"$M/m = {fmt(M / m)}$ — equal and opposite momenta, but the light bullet carries almost all the energy.",
            f"Stopping the rifle: work–energy theorem, $F d = \\tfrac12MV^2 \\Rightarrow F = \\frac{{{fmt(Kg, 4)}}}{{{fmt(d_cm / 100, 2)}}} = {fmt(F)}$ N.",
        ]
        answer = f"$V = {fmt(V)}$ m/s; $K_{{bullet}} = {fmt(Kb)}$ J vs $K_{{rifle}} = {fmt(Kg)}$ J; $F = {fmt(F)}$ N"
        values = {"mode": mode, "M": M, "m_g": m_g, "v": v, "d_cm": d_cm, "V": V, "K_bullet": Kb, "K_gun": Kg, "F": F}
    elif mode == "cannon":
        M = nice(rng, 800, 3000, 50)
        m = nice(rng, 3.0, 15.0, 0.5)
        v = nice(rng, 150, 500, 10)
        th = pick(rng, [0, 0, 10, 15, 20, 25, 30, 35, 40, 45])
        d = nice(rng, 0.5, 3.0, 0.1)
        V = m * v * math.cos(math.radians(th)) / M
        Kg = 0.5 * M * V * V
        F = Kg / d
        aim = "horizontally" if th == 0 else f"at ${th}°$ above the horizontal"
        question = (
            f"A {qx(M, 'kg')} cannon on a smooth horizontal track fires a {qx(m, 'kg')} shell {aim} with a speed of "
            f"{qx(v, 'm/s')} relative to the ground. Find the recoil speed of the cannon. If a recoil brake then stops the "
            f"cannon within {qx(d, 'm')}, what average braking force is needed? (Neglect the propellant gases.)"
        )
        steps = [
            "Horizontal external forces are negligible (smooth track), so the horizontal momentum of cannon + shell stays "
            "zero." + ("" if th == 0 else " Vertical momentum is not conserved: the track pushes up on the cannon during firing."),
            f"$0 = mv\\cos\\theta - MV \\Rightarrow V = \\frac{{mv\\cos\\theta}}{{M}} = \\frac{{({ex(m)})({ex(v)})\\cos {th}°}}{{{ex(M)}}} = {fmt(V)}$ m/s.",
            f"Recoil kinetic energy: $\\tfrac12MV^2 = {fmt(Kg)}$ J.",
            f"Average braking force: $F = \\frac{{\\tfrac12MV^2}}{{d}} = \\frac{{{fmt(Kg, 4)}}}{{{ex(d)}}} = {fmt(F)}$ N "
            f"(${fmt(F / (M * g))}$ times the cannon's weight).",
        ]
        answer = f"$V = {fmt(V)}$ m/s; $F = {fmt(F)}$ N"
        values = {"mode": mode, "M": M, "m": m, "v": v, "theta_deg": th, "d": d, "V": V, "K_gun": Kg, "F": F}
    else:
        M = nice(rng, 80, 140, 1)
        m = nice(rng, 0.5, 5.0, 0.5)
        v = nice(rng, 2.0, 10.0, 0.5)
        D = nice(rng, 5, 50, 1)
        V = m * v / M
        t = D / V
        question = (
            f"An astronaut floating at rest {qx(D, 'm')} from her space station has a total mass (with suit and backpack) of "
            f"{qx(M, 'kg')}. To get back she throws a {qx(m, 'kg')} tool directly away from the station at {qx(v, 'm/s')} "
            "relative to the station. How fast does she drift toward the station, and how long does it take her to reach it?"
        )
        steps = [
            "Relative to the station no external forces act (astronaut, tool and station share the same orbital free "
            "fall), so the total momentum of astronaut + tool stays zero: $0 = mv - MV$.",
            f"$V = \\frac{{mv}}{{M}} = \\frac{{({ex(m)})({ex(v)})}}{{{ex(M)}}} = {fmt(V)}$ m/s toward the station.",
            f"Time to cover {qx(D, 'm')} at constant speed: $t = D/V = {fmt(t)}$ s $= {fmt(t / 60)}$ min.",
            f"Kinetic energy check: the tool gets $\\tfrac12mv^2 = {fmt(0.5 * m * v * v)}$ J, the astronaut only "
            f"$\\tfrac12MV^2 = {fmt(0.5 * M * V * V)}$ J.",
        ]
        answer = f"$V = {fmt(V)}$ m/s; $t = {fmt(t)}$ s"
        values = {"mode": mode, "M": M, "m": m, "v": v, "D": D, "V": V, "t": t}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


VEHICLES = [
    # name, mass (kg), Cd, frontal area (m^2), Crr, drivetrain efficiency (%), speed (km/h)
    ("compact car", (1000, 1400, 50), (0.28, 0.34, 0.01), (2.00, 2.30, 0.05), (0.009, 0.012, 0.001), (85, 92, 1), (60, 130, 5)),
    ("SUV", (1700, 2400, 50), (0.33, 0.42, 0.01), (2.60, 3.00, 0.05), (0.010, 0.014, 0.001), (84, 90, 1), (60, 130, 5)),
    ("electric sedan", (1600, 2200, 50), (0.22, 0.28, 0.01), (2.20, 2.40, 0.05), (0.008, 0.010, 0.001), (88, 94, 1), (60, 130, 5)),
    ("delivery van", (2500, 3500, 50), (0.35, 0.45, 0.01), (3.50, 4.50, 0.10), (0.010, 0.015, 0.001), (84, 90, 1), (50, 110, 5)),
]


@template("vehicle_road_load_power", PHYS, MECH, "Work and power", "medium")
def vehicle_road_load_power(rng):
    name, m_r, cd_r, A_r, crr_r, eff_r, v_r = pick(rng, VEHICLES)
    m, Cd, A, Crr, eff, v_kmh = (draw(rng, s) for s in (m_r, cd_r, A_r, crr_r, eff_r, v_r))
    grade = pick(rng, [0, 0, 0, 1, 2, 3, 4, 5, 6, 8])
    v = v_kmh / 3.6
    th = math.atan(grade / 100)
    Fd = 0.5 * RHO_AIR * Cd * A * v * v
    Fr = Crr * m * g * math.cos(th)
    Fg = m * g * math.sin(th)
    F = Fd + Fr + Fg
    P = F * v
    Pe = P / (eff / 100)
    road = "on a level road" if grade == 0 else f"up a {qx(grade)}% grade (rise/run $= {fmt(grade / 100, 2)}$)"
    question = (
        f"A {name} of mass {qx(m, 'kg')} travels at a steady {qx(v_kmh, 'km/h')} {road} in still air. Its drag coefficient is "
        f"{qx(Cd)}, its frontal area {qx(A, 'm²')} and its rolling-resistance coefficient {qx(Crr)}; take the air density as "
        f"$1.20$ kg/m³. Find the resisting forces, the power that must be delivered to the wheels and the power the "
        f"engine or motor must produce if the drivetrain efficiency is {qx(eff)}%."
    )
    steps = [f"Speed in SI units: $v = {ex(v_kmh)}/3.6 = {fmt(v, 4)}$ m/s."]
    steps.append(f"Aerodynamic drag: $F_d = \\tfrac12\\rho C_dAv^2 = \\tfrac12(1.20)({ex(Cd)})({ex(A)})({fmt(v, 4)})^2 = {fmt(Fd)}$ N.")
    if grade == 0:
        steps.append(f"Rolling resistance: $F_r = C_{{rr}}mg = ({ex(Crr)})({ex(m)})(9.81) = {fmt(Fr)}$ N.")
    else:
        steps += [
            f"Slope angle: $\\theta = \\arctan({fmt(grade / 100, 2)}) = {fmt(math.degrees(th))}°$.",
            f"Rolling resistance: $F_r = C_{{rr}}mg\\cos\\theta = ({ex(Crr)})({ex(m)})(9.81)\\cos\\theta = {fmt(Fr)}$ N.",
            f"Gravity along the slope: $F_g = mg\\sin\\theta = ({ex(m)})(9.81)\\sin\\theta = {fmt(Fg)}$ N.",
        ]
    steps += [
        f"At constant speed the driving force equals the total resistance: $F = {fmt(F)}$ N.",
        f"Power at the wheels: $P = Fv = ({fmt(F, 4)})({fmt(v, 4)}) = {fmt(P)}$ W $= {fmt(P / 1000)}$ kW "
        f"(${fmt(P / HP)}$ hp, with 1 hp = 745.7 W).",
        f"Engine/motor power: $P_{{engine}} = P/\\eta = {fmt(P / 1000, 4)}/{fmt(eff / 100, 2)} = {fmt(Pe / 1000)}$ kW.",
        f"Insight: drag accounts for ${fmt(100 * Fd / F)}$% of the resistance here; since $F_d \\propto v^2$, the power "
        "needed to overcome drag grows as $v^3$, which is why fuel use rises steeply at high speed.",
    ]
    answer = f"$P_{{wheels}} = {fmt(P / 1000)}$ kW; $P_{{engine}} = {fmt(Pe / 1000)}$ kW (drag ${fmt(Fd)}$ N, total force ${fmt(F)}$ N)"
    values = {"m": m, "Cd": Cd, "A": A, "Crr": Crr, "eff_pct": eff, "v_kmh": v_kmh, "grade_pct": grade,
              "F_drag": Fd, "F_roll": Fr, "F_grade": Fg, "F_total": F, "P_wheels": P, "P_engine": Pe}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Thermodynamics of ideal gases
# ---------------------------------------------------------------------------

ADIABATIC_CASES = [
    # context sentence, gas, gamma, direction, ratio range, V1 (L), P1 unit, P1 range, T1 (deg C)
    ("During the compression stroke of a diesel engine, the air in a cylinder is compressed rapidly.", "air", 1.4,
     "compression", (14, 22, 1), (0.40, 1.20, 0.05), "kPa", (95, 105, 1), (15, 50, 1)),
    ("The outlet of a bicycle pump is blocked and the handle is pushed in rapidly, compressing the air inside.", "air", 1.4,
     "compression", (1.5, 4.0, 0.1), (0.10, 0.50, 0.01), "kPa", (98, 103, 1), (10, 35, 1)),
    ("Helium in a well-insulated cylinder fitted with a piston is {verb} slowly.", "helium", 5 / 3,
     "either", (2.0, 8.0, 0.5), (1.0, 10.0, 0.5), "kPa", (100, 500, 10), (0, 100, 1)),
    ("During the power stroke of an engine, hot combustion gas (treated as air) pushes the piston out and expands.", "air", 1.4,
     "expansion", (6.0, 12.0, 0.5), (0.050, 0.100, 0.005), "MPa", (3.0, 8.0, 0.1), (1200, 2200, 50)),
]


@template("adiabatic_process_ideal_gas", PHYS, THERMO, "Thermodynamic processes", "hard")
def adiabatic_process_ideal_gas(rng):
    ctx, gas, gam, direction, r_rng, V_rng, pu, p_rng, T_rng = pick(rng, ADIABATIC_CASES)
    if direction == "either":
        direction = pick(rng, ["compression", "expansion"])
    ratio = draw(rng, r_rng)
    V1_L = draw(rng, V_rng)
    P1_d = draw(rng, p_rng)
    T1_C = draw(rng, T_rng)
    pscale = 1e3 if pu == "kPa" else 1e6
    P1, V1, T1 = P1_d * pscale, V1_L / 1000, T1_C + 273.15
    V2 = V1 / ratio if direction == "compression" else V1 * ratio
    T2 = T1 * (V1 / V2) ** (gam - 1)
    P2 = P1 * (V1 / V2) ** gam
    n = P1 * V1 / (R_GAS * T1)
    W_by = (P1 * V1 - P2 * V2) / (gam - 1)
    mono = gam > 1.5
    g_txt = "\\frac{5}{3}" if mono else "1.40"
    gm1_txt = "\\frac{2}{3}" if mono else "0.40"
    kind = "monatomic" if mono else "diatomic"
    vr = "V_1/V_2" if direction == "compression" else "V_2/V_1"
    ctx = ctx.format(verb="compressed" if direction == "compression" else "allowed to expand")
    question = (
        f"{ctx} Treat the gas as ideal with $\\gamma = {g_txt}$ and the process as quasi-static and adiabatic. "
        f"Initially $P_1 = {ex(P1_d)}$ {pu}, $T_1 = {ex(T1_C)}$ °C and $V_1 = {ex(V1_L)}$ L, and the volume ratio is "
        f"${vr} = {ex(ratio)}$. Find the final temperature and pressure and the work done "
        f"{'on' if direction == 'compression' else 'by'} the gas."
    )
    steps = [
        f"For a reversible adiabatic process ($Q = 0$) of an ideal gas, $PV^\\gamma$ and $TV^{{\\gamma - 1}}$ stay constant; "
        f"$\\gamma = {g_txt}$ for a {kind} gas.",
        f"Final volume: $V_2 = {fmt(V2 * 1000, 4)}$ L. In kelvin $T_1 = {ex(T1)}$ K.",
        f"$T_2 = T_1\\left(\\frac{{V_1}}{{V_2}}\\right)^{{\\gamma - 1}} = ({ex(T1)})({fmt(V1 / V2, 4)})^{{{gm1_txt}}} = {fmt(T2, 4)}$ K "
        f"$= {fmt(T2 - 273.15, 4)}$ °C.",
        f"$P_2 = P_1\\left(\\frac{{V_1}}{{V_2}}\\right)^{{\\gamma}} = ({ex(P1_d)})({fmt(V1 / V2, 4)})^{{{g_txt}}} = "
        f"{fmt(P2 / pscale, 4)}$ {pu}.",
        f"Check with the ideal-gas law: $\\frac{{P_1V_1}}{{T_1}} = \\frac{{P_2V_2}}{{T_2}} = {fmt(P1 * V1 / T1, 4)}$ J/K $= nR$, "
        f"so $n = {fmt(n, 4)}$ mol. ✓",
        f"Work done by the gas: $W = \\frac{{P_1V_1 - P_2V_2}}{{\\gamma - 1}} = \\frac{{{fmt(P1 * V1, 4)} - {fmt(P2 * V2, 4)}}}"
        f"{{{gm1_txt}}} = {fmt(W_by, 4)}$ J.",
    ]
    if direction == "compression":
        steps.append(
            f"So the work done on the gas is ${fmt(-W_by)}$ J; with $Q = 0$ it all becomes internal energy, "
            f"$\\Delta U = nC_v\\Delta T = {fmt(-W_by)}$ J, which is why the gas heats up."
        )
        answer = f"$T_2 = {fmt(T2)}$ K ({fmt(T2 - 273.15)} °C); $P_2 = {fmt(P2 / pscale)}$ {pu}; work on gas ${fmt(-W_by)}$ J"
    else:
        steps.append(
            f"The gas does ${fmt(W_by)}$ J of work on the piston at the expense of its internal energy "
            f"($\\Delta U = nC_v\\Delta T = {fmt(-W_by)}$ J), so it cools."
        )
        answer = f"$T_2 = {fmt(T2)}$ K ({fmt(T2 - 273.15)} °C); $P_2 = {fmt(P2 / pscale)}$ {pu}; work by gas ${fmt(W_by)}$ J"
    if "diesel" in ctx:
        steps.append("Interpretation: this is far above the autoignition temperature of diesel fuel (about 210 °C), so fuel "
                     "injected now ignites without a spark plug.")
    values = {"gas": gas, "gamma": gam, "direction": direction, "ratio": ratio, "V1_L": V1_L, "P1": P1, "T1_C": T1_C,
              "T2": T2, "P2": P2, "n": n, "W_by": W_by}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("isothermal_process_ideal_gas", PHYS, THERMO, "Thermodynamic processes", "medium")
def isothermal_process_ideal_gas(rng):
    gas = pick(rng, ["nitrogen", "argon", "air", "helium", "oxygen", "carbon dioxide (treated as ideal)"])
    n = nice(rng, 0.20, 5.00, 0.05)
    T_C = nice(rng, 0, 200, 1)
    T = T_C + 273.15
    expand = rng.random() < 0.6
    by_volume = rng.random() < 0.5
    for _ in range(1000):
        if by_volume:
            V1 = nice(rng, 1.0, 20.0, 0.5)
            V2 = nice(rng, 1.0, 60.0, 0.5)
            ratio = V2 / V1
        else:
            P1 = nice(rng, 100, 1000, 10)
            P2 = nice(rng, 50, 1000, 10)
            ratio = P1 / P2
        if (expand and 1.5 <= ratio <= 6) or (not expand and 1 / 6 <= ratio <= 1 / 1.5):
            break
    else:
        raise RuntimeError("no valid isothermal process")
    W = n * R_GAS * T * math.log(ratio)
    dS = n * R_GAS * math.log(ratio)
    proc = "expands" if expand else "is compressed"
    if by_volume:
        P1 = n * R_GAS * T / (V1 / 1000) / 1000
        P2 = n * R_GAS * T / (V2 / 1000) / 1000
        change = f"from {qx(V1, 'L')} to {qx(V2, 'L')}"
        state = (f"Pressures from $P = nRT/V$: $P_1 = {fmt(P1, 4)}$ kPa, $P_2 = {fmt(P2, 4)}$ kPa "
                 "(Boyle's law: $P_1V_1 = P_2V_2$).")
        sym, num = "\\frac{V_2}{V_1}", f"\\frac{{{ex(V2)}}}{{{ex(V1)}}}"
    else:
        V1 = n * R_GAS * T / (P1 * 1000) * 1000
        V2 = n * R_GAS * T / (P2 * 1000) * 1000
        change = f"from a pressure of {qx(P1, 'kPa')} to {qx(P2, 'kPa')}"
        state = (f"Volumes from $V = nRT/P$: $V_1 = {fmt(V1, 4)}$ L, $V_2 = {fmt(V2, 4)}$ L; at constant $T$, "
                 "$V_2/V_1 = P_1/P_2$.")
        sym, num = "\\frac{P_1}{P_2}", f"\\frac{{{ex(P1)}}}{{{ex(P2)}}}"
    question = (
        f"A sample of {qx(n, 'mol')} of {gas} {proc} slowly and isothermally at {qx(T_C, '°C')}, in contact with a large heat reservoir, "
        f"{change}. Treating it as an ideal gas, find the work done by the gas, the heat exchanged with the reservoir, the "
        "change in internal energy and the entropy change of the gas."
    )
    steps = [
        f"Temperature in kelvin: $T = {ex(T)}$ K. {state}",
        "For an ideal gas $U$ depends only on $T$, so $\\Delta U = 0$ and the first law gives $Q = W$.",
        f"Work done by the gas: $W = \\int P\\,dV = nRT\\ln{sym} = ({ex(n)})(8.314)({ex(T)})\\ln{num} = {fmt(W)}$ J.",
        f"Heat: $Q = W = {fmt(W)}$ J — the gas {'absorbs' if expand else 'gives off'} ${fmt(abs(W))}$ J "
        f"{'from' if expand else 'to'} the reservoir.",
        f"Entropy change of the gas: $\\Delta S = \\frac{{Q}}{{T}} = nR\\ln\\frac{{V_2}}{{V_1}} = {fmt(dS)}$ J/K. For this reversible "
        "process the reservoir's entropy changes by exactly the opposite amount, so the total is zero.",
    ]
    answer = f"$W = {fmt(W)}$ J; $Q = {fmt(W)}$ J; $\\Delta U = 0$; $\\Delta S = {fmt(dS)}$ J/K"
    values = {"n": n, "T_C": T_C, "expand": expand, "by_volume": by_volume, "V1_L": V1, "V2_L": V2,
              "P1_kPa": P1, "P2_kPa": P2, "W": W, "Q": W, "dS": dS}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


# ---------------------------------------------------------------------------
# Entropy, conduction, engines, evaporation
# ---------------------------------------------------------------------------


@template("entropy_change_water", PHYS, THERMO, "Entropy", "medium")
def entropy_change_water(rng):
    if rng.random() < 0.5:
        m = nice(rng, 0.2, 5.0, 0.1)
        T1_C = nice(rng, 5, 40, 1)
        T2_C = nice(rng, 50, 95, 1)
        Tr_C = nice(rng, 100, 300, 10)
        T1, T2, Tr = T1_C + 273.15, T2_C + 273.15, Tr_C + 273.15
        Q = m * C_WATER * (T2 - T1)
        dS_w = m * C_WATER * math.log(T2 / T1)
        dS_r = -Q / Tr
        dS_t = dS_w + dS_r
        question = (
            f"A pan containing {qx(m, 'kg')} of water is heated from {qx(T1_C, '°C')} to {qx(T2_C, '°C')} by a hot plate whose surface is held "
            f"at {qx(Tr_C, '°C')} (treat the plate as a heat reservoir). Using $c = 4186$ J/(kg·K) and neglecting heat losses "
            "to the surroundings, find the heat absorbed by the water, the entropy change of the water and of the "
            "reservoir, and the total entropy change."
        )
        steps = [
            f"Kelvin temperatures: $T_1 = {ex(T1)}$ K, $T_2 = {ex(T2)}$ K, $T_{{res}} = {ex(Tr)}$ K.",
            f"Heat absorbed: $Q = mc\\Delta T = ({ex(m)})(4186)({ex(T2_C - T1_C)}) = {fmt(Q)}$ J.",
            f"The water's temperature changes, so integrate $dS = \\frac{{dQ}}{{T}} = \\frac{{mc\\,dT}}{{T}}$: "
            f"$\\Delta S_w = mc\\ln\\frac{{T_2}}{{T_1}} = ({ex(m)})(4186)\\ln\\frac{{{ex(T2)}}}{{{ex(T1)}}} = {fmt(dS_w)}$ J/K.",
            f"Check: $Q/\\bar T$ with the mean temperature $\\bar T = {fmt((T1 + T2) / 2, 5)}$ K gives "
            f"${fmt(Q / ((T1 + T2) / 2))}$ J/K, close to the exact value.",
            f"The reservoir loses $Q$ at constant temperature: $\\Delta S_{{res}} = -\\frac{{Q}}{{T_{{res}}}} = {fmt(dS_r)}$ J/K.",
            f"Total: $\\Delta S_{{total}} = {fmt(dS_t)}$ J/K $> 0$, as the second law requires for heat flowing across a finite "
            "temperature difference (an irreversible process).",
        ]
        answer = f"$Q = {fmt(Q)}$ J; $\\Delta S_w = {fmt(dS_w)}$ J/K; $\\Delta S_{{res}} = {fmt(dS_r)}$ J/K; $\\Delta S_{{total}} = {fmt(dS_t)}$ J/K"
        values = {"mode": "heating", "m": m, "T1_C": T1_C, "T2_C": T2_C, "T_res_C": Tr_C, "Q": Q,
                  "dS_water": dS_w, "dS_res": dS_r, "dS_total": dS_t}
        diff = "medium"
    else:
        m1 = nice(rng, 0.1, 3.0, 0.1)
        m2 = nice(rng, 0.1, 3.0, 0.1)
        T1_C = nice(rng, 5, 40, 1)
        T2_C = nice(rng, 50, 95, 1)
        Tf_C = (m1 * T1_C + m2 * T2_C) / (m1 + m2)
        T1, T2, Tf = T1_C + 273.15, T2_C + 273.15, Tf_C + 273.15
        dS1 = m1 * C_WATER * math.log(Tf / T1)
        dS2 = m2 * C_WATER * math.log(Tf / T2)
        dS = dS1 + dS2
        Qx = m1 * C_WATER * (Tf - T1)
        question = (
            f"In an insulated container, {qx(m1, 'kg')} of water at {qx(T1_C, '°C')} is mixed with {qx(m2, 'kg')} of water at "
            f"{qx(T2_C, '°C')}. Using $c = 4186$ J/(kg·K), find the final temperature, the entropy change of each sample and "
            "the total entropy change."
        )
        steps = [
            f"Energy conservation (no losses, same $c$): $m_1c(T_f - T_1) = m_2c(T_2 - T_f) \\Rightarrow T_f = "
            f"\\frac{{m_1T_1 + m_2T_2}}{{m_1 + m_2}} = {fmt(Tf_C, 4)}$ °C $= {fmt(Tf, 5)}$ K.",
            f"Heat transferred: $Q = m_1c(T_f - T_1) = {fmt(Qx)}$ J from the hot sample to the cold one.",
            f"Cold sample: $\\Delta S_1 = m_1c\\ln\\frac{{T_f}}{{T_1}} = ({ex(m1)})(4186)\\ln\\frac{{{fmt(Tf, 5)}}}{{{ex(T1)}}} = {fmt(dS1)}$ J/K.",
            f"Hot sample: $\\Delta S_2 = m_2c\\ln\\frac{{T_f}}{{T_2}} = ({ex(m2)})(4186)\\ln\\frac{{{fmt(Tf, 5)}}}{{{ex(T2)}}} = {fmt(dS2)}$ J/K.",
            f"Total: $\\Delta S = \\Delta S_1 + \\Delta S_2 = {fmt(dS)}$ J/K $> 0$. The cold water gains more entropy than the hot "
            "water loses because the same heat enters it at a lower temperature: mixing is irreversible.",
        ]
        answer = f"$T_f = {fmt(Tf_C)}$ °C; $\\Delta S_1 = {fmt(dS1)}$ J/K, $\\Delta S_2 = {fmt(dS2)}$ J/K; $\\Delta S_{{total}} = {fmt(dS)}$ J/K"
        values = {"mode": "mixing", "m1": m1, "m2": m2, "T1_C": T1_C, "T2_C": T2_C, "Tf_C": Tf_C,
                  "dS1": dS1, "dS2": dS2, "dS_total": dS}
        diff = "hard"
    return {"question": question, "steps": steps, "answer": answer, "values": values, "difficulty": diff}


INNER_LAYERS = [("gypsum plasterboard", 0.17, (1.0, 2.0, 0.25)), ("pine boards", 0.12, (1.5, 3.0, 0.5))]
INSULATION = [("fiberglass insulation", 0.040, (5, 20, 1)), ("expanded polystyrene foam", 0.033, (3, 15, 1)),
              ("mineral wool", 0.038, (5, 20, 1))]
STRUCTURE = [("common brick", 0.72, (9, 24, 1)), ("concrete", 1.40, (10, 25, 1))]


@template("composite_wall_conduction", PHYS, THERMO, "Heat transfer", "medium")
def composite_wall_conduction(rng):
    layers = []
    if rng.random() < 0.6:
        layers.append(pick(rng, INNER_LAYERS))
    layers.append(pick(rng, INSULATION))
    layers.append(pick(rng, STRUCTURE))
    names = [ly[0] for ly in layers]
    ks = [ly[1] for ly in layers]
    Ls = [draw(rng, ly[2]) for ly in layers]
    A = nice(rng, 6.0, 30.0, 0.5)
    T_in = nice(rng, 18, 24, 1)
    T_out = nice(rng, -25, 10, 1)
    Rs = [L / 100 / (k * A) for L, k in zip(Ls, ks)]
    R_tot = sum(Rs)
    P = (T_in - T_out) / R_tot
    temps = []
    T = T_in
    for R in Rs[:-1]:
        T -= P * R
        temps.append(T)
    U = 1 / (R_tot * A)
    E_kWh = P * 24 / 1000
    ins = 1 if len(layers) == 3 else 0
    desc = "; ".join(f"{qx(L, 'cm')} of {nm} ($k = {ex(k)}$ W/(m·K))" for nm, k, L in zip(names, ks, Ls))
    question = (
        f"An exterior wall of area {qx(A, 'm²')} consists of the following layers, from inside to outside: {desc}. The inside "
        f"surface is at {qx(T_in, '°C')} and the outside surface at {qx(T_out, '°C')}. Assuming steady one-dimensional "
        "conduction (no thermal bridges), find the thermal resistance of each layer, the rate of heat loss through the "
        "wall, the temperature at each interface between layers, the wall's U-value and the energy lost per day."
    )
    steps = ["Each layer is a thermal resistance $R = \\frac{L}{kA}$; the layers are in series, so the same heat current flows through all of them."]
    for nm, k, L, R in zip(names, ks, Ls, Rs):
        steps.append(f"{nm.capitalize()}: $R = \\frac{{{fmt(L / 100, 3)}}}{{({ex(k)})({ex(A)})}} = {fmt(R, 4)}$ K/W.")
    steps += [
        f"Total resistance: $R_{{tot}} = {' + '.join(fmt(R, 4) for R in Rs)} = {fmt(R_tot, 4)}$ K/W.",
        f"Heat current: $P = \\frac{{T_{{in}} - T_{{out}}}}{{R_{{tot}}}} = \\frac{{{ex(T_in)} - ({ex(T_out)})}}{{{fmt(R_tot, 4)}}} = {fmt(P)}$ W.",
    ]
    T = T_in
    for i, (nm, R) in enumerate(zip(names[:-1], Rs[:-1])):
        steps.append(f"Temperature after the {nm}: $T_{i + 1} = {fmt(T, 4)} - ({fmt(P, 4)})({fmt(R, 4)}) = {fmt(temps[i], 4)}$ °C.")
        T = temps[i]
    T_end = T - P * Rs[-1]
    steps += [
        f"Check: after the {names[-1]} the temperature is ${fmt(T, 4)} - ({fmt(P, 4)})({fmt(Rs[-1], 4)}) = {fmt(T_end, 4)}$ °C, "
        "the given outside temperature. ✓",
        f"U-value: $U = \\frac{{1}}{{R_{{tot}}A}} = {fmt(U)}$ W/(m²·K). Energy lost per day: $P \\times 24$ h $= {fmt(E_kWh)}$ kWh "
        f"$= {fmt(P * 86400 / 1e6)}$ MJ.",
        f"Insight: the {names[ins]} provides ${fmt(100 * Rs[ins] / R_tot)}$% of the total resistance, so most of the "
        "temperature drop occurs across it.",
    ]
    answer = (f"$P = {fmt(P)}$ W; interface temperatures " + ", ".join(f"${fmt(t)}$ °C" for t in temps)
              + f"; $U = {fmt(U)}$ W/(m²·K); ${fmt(E_kWh)}$ kWh per day")
    values = {"A": A, "T_in": T_in, "T_out": T_out, "layers": names, "k": ks, "L_cm": Ls, "R": Rs, "R_tot": R_tot,
              "P": P, "T_interfaces": temps, "U": U, "E_kWh_day": E_kWh}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("otto_cycle_engine", PHYS, THERMO, "Heat engines", "medium")
def otto_cycle_engine(rng):
    r = nice(rng, 7.0, 12.0, 0.5)
    T1_C = nice(rng, 15, 45, 1)
    T3 = nice(rng, 1800, 2800, 50)
    Qin = nice(rng, 300, 1500, 50)
    ncyl = pick(rng, [4, 4, 6, 8])
    rpm = nice(rng, 1500, 6000, 100)
    gam = 1.4
    T1 = T1_C + 273.15
    k = r ** (gam - 1)
    eta = 1 - 1 / k
    T2 = T1 * k
    T4 = T3 / k
    W = eta * Qin
    Qout = Qin - W
    P = W * ncyl * rpm / 120
    eta_c = 1 - T1 / T3
    question = (
        f"An idealized four-stroke gasoline engine runs on the air-standard Otto cycle with compression ratio {qx(r)} "
        f"($\\gamma = 1.40$). At the start of compression the air is at {qx(T1_C, '°C')}, and the peak temperature after "
        f"combustion is {qx(T3, 'K')}. Each cylinder takes in {qx(Qin, 'J')} of heat per cycle. Find (a) the thermal "
        "efficiency and the temperatures at the end of compression and of expansion, (b) the net work and the heat "
        f"rejected per cycle per cylinder, (c) the ideal power output if the engine has ${ncyl}$ cylinders and runs at "
        f"{qx(rpm)} rpm, and (d) the Carnot efficiency between the extreme temperatures."
    )
    steps = [
        f"Otto efficiency depends only on the compression ratio: $\\eta = 1 - \\frac{{1}}{{r^{{\\gamma - 1}}}} = "
        f"1 - \\frac{{1}}{{({ex(r)})^{{0.40}}}} = {fmt(eta, 4)}$ (${fmt(100 * eta)}$%).",
        f"$T_1 = {ex(T1)}$ K. Adiabatic compression: $T_2 = T_1r^{{\\gamma - 1}} = ({ex(T1)})({fmt(k, 4)}) = {fmt(T2, 4)}$ K. "
        f"Adiabatic expansion: $T_4 = T_3/r^{{\\gamma - 1}} = {ex(T3)}/{fmt(k, 4)} = {fmt(T4, 4)}$ K.",
        f"Check: $1 - T_1/T_2 = 1 - T_4/T_3 = {fmt(1 - T4 / T3, 4)} = \\eta$ ✓.",
        f"Net work: $W = \\eta Q_{{in}} = ({fmt(eta, 4)})({ex(Qin)}) = {fmt(W)}$ J; heat rejected $Q_{{out}} = Q_{{in}} - W = {fmt(Qout)}$ J.",
        f"A four-stroke cylinder completes one cycle every two revolutions, i.e. ${ex(rpm)}/120 = {fmt(rpm / 120, 4)}$ cycles "
        f"per second. Power: $P = W \\times {ncyl} \\times {fmt(rpm / 120, 4)} = {fmt(P)}$ W $= {fmt(P / 1000)}$ kW.",
        f"Carnot limit: $\\eta_C = 1 - T_1/T_3 = 1 - {ex(T1)}/{ex(T3)} = {fmt(eta_c, 4)}$ (${fmt(100 * eta_c)}$%), higher than "
        "the Otto value because heat is not all added at the peak temperature. Real engines reach only about 25–35% "
        "because of friction, heat loss and incomplete combustion.",
    ]
    answer = (f"$\\eta = {fmt(100 * eta)}$%; $T_2 = {fmt(T2)}$ K, $T_4 = {fmt(T4)}$ K; $W = {fmt(W)}$ J, $Q_{{out}} = {fmt(Qout)}$ J; "
              f"$P = {fmt(P / 1000)}$ kW; $\\eta_C = {fmt(100 * eta_c)}$%")
    values = {"r": r, "gamma": gam, "T1_C": T1_C, "T3": T3, "Q_in": Qin, "n_cyl": ncyl, "rpm": rpm, "eta": eta,
              "T2": T2, "T4": T4, "W": W, "Q_out": Qout, "P": P, "eta_carnot": eta_c}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


SWEATERS = [
    # who, activity, heat rate (W), duration (min), evaporated fraction (%), body mass (kg)
    ("marathon runner", "a race", (600, 1200, 50), (30, 240, 5), (50, 85, 5), (50, 85, 1)),
    ("cyclist", "a long ride on a hot day", (400, 1000, 50), (30, 300, 10), (60, 90, 5), (55, 95, 1)),
    ("construction worker", "a shift in hot weather", (250, 500, 10), (60, 480, 30), (50, 90, 5), (60, 110, 1)),
    ("soccer player", "a match", (500, 1000, 50), (45, 95, 5), (55, 85, 5), (60, 90, 1)),
]


@template("evaporative_cooling_sweat", PHYS, THERMO, "Phase changes", "easy")
def evaporative_cooling_sweat(rng):
    who, activity, p_rng, t_rng, f_rng, M_rng = pick(rng, SWEATERS)
    P = draw(rng, p_rng)
    t_min = draw(rng, t_rng)
    f = draw(rng, f_rng)
    M = draw(rng, M_rng)
    Q = f / 100 * P * t_min * 60
    m = Q / L_SWEAT
    rate = m / (t_min / 60)
    dT = Q / (M * C_BODY)
    question = (
        f"During {activity}, a {who} with a body mass of {qx(M, 'kg')} produces excess (waste) heat at an average rate of "
        f"{qx(P, 'W')} for {qx(t_min, 'min')}. If {qx(f)}% of this heat is removed by the evaporation of sweat, what mass and volume of sweat "
        "must evaporate? Take the latent heat of vaporization of water at skin temperature as $2.42 \\times 10^6$ J/kg. "
        "By how much would the body temperature rise if this heat were not removed at all? (Average specific heat of the "
        "body: 3500 J/(kg·K).)"
    )
    severity = ("enough to cause life-threatening heat stroke" if dT > 3
                else "a noticeable rise that the body must avoid")
    steps = [
        f"Duration in seconds: $t = {ex(t_min)} \\times 60 = {ex(t_min * 60)}$ s.",
        f"Heat removed by evaporation: $Q = f P t = ({fmt(f / 100, 2)})({ex(P)})({ex(t_min * 60)}) = {fmt(Q)}$ J.",
        f"Mass of sweat: $m = \\frac{{Q}}{{L_v}} = \\frac{{{fmt(Q, 4)}}}{{2.42 \\times 10^6}} = {fmt(m)}$ kg, i.e. about "
        f"${fmt(m)}$ L (1 kg of water ≈ 1 L), an average of ${fmt(rate)}$ L per hour.",
        f"Without this cooling: $\\Delta T = \\frac{{Q}}{{Mc}} = \\frac{{{fmt(Q, 4)}}}{{({ex(M)})(3500)}} = {fmt(dT)}$ K — {severity}.",
        "Only sweat that actually evaporates cools the body; sweat that drips off removes almost no heat, which is why "
        "humid air (slow evaporation) makes exercise in the heat dangerous.",
    ]
    answer = f"$m = {fmt(m)}$ kg (about ${fmt(m)}$ L) of sweat; $\\Delta T = {fmt(dT)}$ K without cooling"
    values = {"P": P, "t_min": t_min, "f_pct": f, "M": M, "Q": Q, "m_sweat": m, "rate_L_per_h": rate, "dT": dT}
    return {"question": question, "steps": steps, "answer": answer, "values": values}
