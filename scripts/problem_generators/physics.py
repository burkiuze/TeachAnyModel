"""Physics problem templates (mechanics, thermodynamics, EM, waves, modern)."""

import math

from .common import (
    C, E_CHARGE, EPS0, EV, G, G_EARTH, H, HBAR, HC_EV_NM, K_B, K_E, M_E,
    M_EARTH, M_P, MU0, N_A, R_EARTH, R_GAS, SIGMA_SB, WIEN_B, fmt, nice, pick,
    q, sig, template,
)

g = G_EARTH
PHYS = "Physics"

# ---------------------------------------------------------------------------
# Kinematics
# ---------------------------------------------------------------------------


@template("kinematics_constant_acceleration", PHYS, "Classical Mechanics", "Kinematics", "easy")
def kinematics_constant_acceleration(rng):
    obj = pick(rng, ["car", "cyclist", "train", "motorboat", "sprinter", "rocket sled"])
    v0 = nice(rng, 0, 20, 1)
    a = nice(rng, 0.5, 6.0, 0.5)
    t = nice(rng, 2, 15, 1)
    v = v0 + a * t
    s = v0 * t + 0.5 * a * t * t
    question = (
        f"A {obj} moving at {q(v0, 'm/s')} accelerates uniformly at {q(a, 'm/s²')} "
        f"for {q(t, 's')}. Find its final velocity and the distance it covers during this time."
    )
    steps = [
        f"For constant acceleration, $v = v_0 + at = {fmt(v0)} + ({fmt(a)})({fmt(t)}) = {fmt(v)}$ m/s.",
        f"Displacement: $s = v_0t + \\tfrac12at^2 = ({fmt(v0)})({fmt(t)}) + \\tfrac12({fmt(a)})({fmt(t)})^2 = {fmt(s)}$ m.",
        f"Check with the average velocity: $\\frac{{v_0 + v}}{{2}}t = \\frac{{{fmt(v0)} + {fmt(v)}}}{{2}}({fmt(t)}) = {fmt((v0 + v) / 2 * t)}$ m. ✓",
    ]
    return {
        "question": question,
        "given": [f"$v_0 = {fmt(v0)}$ m/s", f"$a = {fmt(a)}$ m/s²", f"$t = {fmt(t)}$ s"],
        "steps": steps,
        "answer": f"$v = {fmt(v)}$ m/s; distance $= {fmt(s)}$ m",
        "values": {"v0": v0, "a": a, "t": t, "v": v, "s": s},
    }


@template("kinematics_stopping_distance", PHYS, "Classical Mechanics", "Kinematics", "medium")
def kinematics_stopping_distance(rng):
    vkmh = nice(rng, 40, 130, 5)
    dec = nice(rng, 3.0, 9.0, 0.5)
    tr = nice(rng, 0.5, 1.5, 0.1)
    v0 = vkmh / 3.6
    d1 = v0 * tr
    d2 = v0 ** 2 / (2 * dec)
    d = d1 + d2
    question = (
        f"A driver traveling at {q(vkmh, 'km/h')} sees an obstacle and brakes. The reaction time is "
        f"{q(tr, 's')} and the car then decelerates uniformly at {q(dec, 'm/s²')}. "
        "What is the total stopping distance?"
    )
    steps = [
        f"Convert the speed: $v_0 = {fmt(vkmh)}/3.6 = {fmt(v0)}$ m/s.",
        f"Reaction distance (constant speed): $d_1 = v_0t_r = ({fmt(v0)})({fmt(tr)}) = {fmt(d1)}$ m.",
        f"Braking distance from $v^2 = v_0^2 - 2ad$ with $v = 0$: $d_2 = \\frac{{v_0^2}}{{2a}} = \\frac{{({fmt(v0)})^2}}{{2({fmt(dec)})}} = {fmt(d2)}$ m.",
        f"Total: $d = d_1 + d_2 = {fmt(d)}$ m. (Braking distance grows with the square of speed.)",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"about {q(d, 'm')} (reaction {q(d1, 'm')} + braking {q(d2, 'm')})",
        "values": {"v_kmh": vkmh, "decel": dec, "t_reaction": tr, "d_total": d, "d_reaction": d1, "d_braking": d2},
    }


@template("free_fall", PHYS, "Classical Mechanics", "Kinematics", "easy")
def free_fall(rng):
    h = nice(rng, 5, 200, 5)
    t = math.sqrt(2 * h / g)
    v = math.sqrt(2 * g * h)
    where = pick(rng, ["the top of a building", "a bridge", "a cliff", "a hot-air balloon at rest", "a tower"])
    question = (
        f"A stone is dropped from rest from {where} {q(h, 'm')} above the ground. Neglecting air resistance "
        f"($g = 9.81$ m/s²), how long does it take to reach the ground and how fast is it moving on impact?"
    )
    steps = [
        f"From $h = \\tfrac12gt^2$: $t = \\sqrt{{2h/g}} = \\sqrt{{2({fmt(h)})/9.81}} = {fmt(t)}$ s.",
        f"Impact speed: $v = gt = 9.81 \\times {fmt(t)} = {fmt(v)}$ m/s (equivalently $v = \\sqrt{{2gh}}$).",
        f"In km/h this is ${fmt(v * 3.6)}$ km/h. The result does not depend on the stone's mass.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$t = {fmt(t)}$ s; $v = {fmt(v)}$ m/s",
        "values": {"h": h, "t": t, "v": v},
    }


@template("vertical_throw", PHYS, "Classical Mechanics", "Kinematics", "easy")
def vertical_throw(rng):
    v0 = nice(rng, 5.0, 40.0, 0.5)
    t_top = v0 / g
    h = v0 ** 2 / (2 * g)
    T = 2 * t_top
    question = (
        f"A ball is thrown straight up with an initial speed of {q(v0, 'm/s')}. Ignoring air resistance, find "
        "(a) the time to reach the highest point, (b) the maximum height, and (c) the total time until it returns to the launch point."
    )
    steps = [
        f"At the top the velocity is zero: $0 = v_0 - gt \\Rightarrow t_{{top}} = v_0/g = {fmt(v0)}/9.81 = {fmt(t_top)}$ s.",
        f"Maximum height: $h = \\frac{{v_0^2}}{{2g}} = \\frac{{({fmt(v0)})^2}}{{2(9.81)}} = {fmt(h)}$ m.",
        f"By symmetry the descent takes as long as the ascent: $T = 2t_{{top}} = {fmt(T)}$ s.",
        "Note: at the top the velocity is zero but the acceleration is still $g$ downward.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"(a) {q(t_top, 's')}; (b) {q(h, 'm')}; (c) {q(T, 's')}",
        "values": {"v0": v0, "t_top": t_top, "h_max": h, "T": T},
    }


@template("projectile_motion", PHYS, "Classical Mechanics", "Projectile motion", "medium")
def projectile_motion(rng):
    v0 = nice(rng, 10, 50, 1)
    th = nice(rng, 15, 75, 1)
    r = math.radians(th)
    vx, vy = v0 * math.cos(r), v0 * math.sin(r)
    T = 2 * vy / g
    H = vy ** 2 / (2 * g)
    R = vx * T
    obj = pick(rng, ["ball", "stone", "golf ball", "water jet", "arrow"])
    question = (
        f"A {obj} is launched from level ground at {q(v0, 'm/s')} at an angle of ${th}°$ above the horizontal. "
        "Neglecting air resistance, find the time of flight, the maximum height and the horizontal range."
    )
    steps = [
        f"Resolve the velocity: $v_x = v_0\\cos\\theta = {fmt(v0)}\\cos {th}° = {fmt(vx)}$ m/s; $v_y = v_0\\sin\\theta = {fmt(vy)}$ m/s.",
        f"Time of flight: $T = \\frac{{2v_y}}{{g}} = \\frac{{2({fmt(vy)})}}{{9.81}} = {fmt(T)}$ s.",
        f"Maximum height: $H = \\frac{{v_y^2}}{{2g}} = {fmt(H)}$ m.",
        f"Range: $R = v_xT = ({fmt(vx)})({fmt(T)}) = {fmt(R)}$ m.",
        f"Check: $R = \\frac{{v_0^2\\sin 2\\theta}}{{g}} = \\frac{{({fmt(v0)})^2\\sin {2 * th}°}}{{9.81}} = {fmt(v0 ** 2 * math.sin(2 * r) / g)}$ m. ✓",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$T = {fmt(T)}$ s, $H = {fmt(H)}$ m, $R = {fmt(R)}$ m",
        "values": {"v0": v0, "theta_deg": th, "T": T, "H": H, "R": R},
    }


@template("horizontal_launch", PHYS, "Classical Mechanics", "Projectile motion", "medium")
def horizontal_launch(rng):
    h = nice(rng, 2, 80, 1)
    v0 = nice(rng, 2, 30, 1)
    t = math.sqrt(2 * h / g)
    x = v0 * t
    vy = g * t
    v = math.hypot(v0, vy)
    ang = math.degrees(math.atan2(vy, v0))
    question = (
        f"A ball rolls off a horizontal table-top (or cliff edge) {q(h, 'm')} high with a speed of {q(v0, 'm/s')}. "
        "How long is it in the air, how far from the base does it land, and what is its speed just before impact?"
    )
    steps = [
        f"Vertical motion is free fall from rest: $t = \\sqrt{{2h/g}} = \\sqrt{{2({fmt(h)})/9.81}} = {fmt(t)}$ s.",
        f"Horizontal motion is uniform: $x = v_0t = ({fmt(v0)})({fmt(t)}) = {fmt(x)}$ m.",
        f"Vertical velocity at impact: $v_y = gt = {fmt(vy)}$ m/s; speed $v = \\sqrt{{v_0^2 + v_y^2}} = {fmt(v)}$ m/s.",
        f"The velocity points ${fmt(ang)}°$ below the horizontal.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$t = {fmt(t)}$ s; lands {q(x, 'm')} away; impact speed {q(v, 'm/s')}",
        "values": {"h": h, "v0": v0, "t": t, "x": x, "v_impact": v},
    }


# ---------------------------------------------------------------------------
# Dynamics
# ---------------------------------------------------------------------------


@template("incline_with_friction", PHYS, "Classical Mechanics", "Newton's laws", "medium")
def incline_with_friction(rng):
    while True:
        m = nice(rng, 1, 50, 1)
        th = nice(rng, 15, 50, 1)
        mu = nice(rng, 0.05, 0.6, 0.05)
        r = math.radians(th)
        if math.sin(r) > mu * math.cos(r) + 0.05:
            break
    N = m * g * math.cos(r)
    f = mu * N
    a = g * (math.sin(r) - mu * math.cos(r))
    question = (
        f"A {q(m, 'kg')} block slides down a ramp inclined at ${th}°$. The coefficient of kinetic friction is "
        f"$\\mu_k = {fmt(mu, 2)}$. Find the normal force, the friction force and the block's acceleration."
    )
    steps = [
        "Choose axes parallel and perpendicular to the incline.",
        f"Perpendicular: $N = mg\\cos\\theta = ({fmt(m)})(9.81)\\cos {th}° = {fmt(N)}$ N.",
        f"Friction: $f_k = \\mu_kN = ({fmt(mu, 2)})({fmt(N)}) = {fmt(f)}$ N, directed up the slope.",
        f"Parallel: $ma = mg\\sin\\theta - f_k \\Rightarrow a = g(\\sin\\theta - \\mu_k\\cos\\theta) = 9.81(\\sin {th}° - {fmt(mu, 2)}\\cos {th}°) = {fmt(a)}$ m/s².",
        "The acceleration is independent of the mass.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$N = {fmt(N)}$ N, $f_k = {fmt(f)}$ N, $a = {fmt(a)}$ m/s² down the incline",
        "values": {"m": m, "theta_deg": th, "mu_k": mu, "N": N, "f": f, "a": a},
    }


@template("horizontal_push_friction", PHYS, "Classical Mechanics", "Newton's laws", "easy")
def horizontal_push_friction(rng):
    while True:
        m = nice(rng, 2, 40, 1)
        mu = nice(rng, 0.1, 0.5, 0.05)
        F = nice(rng, 20, 300, 5)
        if F > mu * m * g + 2:
            break
    f = mu * m * g
    a = (F - f) / m
    question = (
        f"A horizontal force of {q(F, 'N')} pushes a {q(m, 'kg')} crate across a floor with "
        f"$\\mu_k = {fmt(mu, 2)}$. What is the crate's acceleration?"
    )
    steps = [
        f"Normal force on a horizontal floor: $N = mg = ({fmt(m)})(9.81) = {fmt(m * g)}$ N.",
        f"Kinetic friction: $f_k = \\mu_kN = {fmt(f)}$ N.",
        f"Newton's second law: $a = \\frac{{F - f_k}}{{m}} = \\frac{{{fmt(F)} - {fmt(f)}}}{{{fmt(m)}}} = {fmt(a)}$ m/s².",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$a = {fmt(a)}$ m/s²",
        "values": {"m": m, "mu_k": mu, "F": F, "a": a},
    }


@template("atwood_machine", PHYS, "Classical Mechanics", "Newton's laws", "medium")
def atwood_machine(rng):
    m1 = nice(rng, 1.0, 10.0, 0.5)
    m2 = m1 + nice(rng, 0.5, 8.0, 0.5)
    a = (m2 - m1) / (m1 + m2) * g
    T = 2 * m1 * m2 / (m1 + m2) * g
    question = (
        f"Two masses, {q(m1, 'kg')} and {q(m2, 'kg')}, hang from the ends of a light string over a frictionless, "
        "massless pulley (an Atwood machine). Find the acceleration of the masses and the tension in the string."
    )
    steps = [
        f"Lighter mass ($m_1$) accelerates up: $T - m_1g = m_1a$.",
        f"Heavier mass ($m_2$) accelerates down: $m_2g - T = m_2a$.",
        f"Adding: $a = \\frac{{m_2 - m_1}}{{m_1 + m_2}}g = \\frac{{{fmt(m2)} - {fmt(m1)}}}{{{fmt(m1 + m2)}}}(9.81) = {fmt(a)}$ m/s².",
        f"Tension: $T = \\frac{{2m_1m_2}}{{m_1 + m_2}}g = {fmt(T)}$ N.",
        f"Check: $T$ lies between $m_1g = {fmt(m1 * g)}$ N and $m_2g = {fmt(m2 * g)}$ N. ✓",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$a = {fmt(a)}$ m/s², $T = {fmt(T)}$ N",
        "values": {"m1": m1, "m2": m2, "a": a, "T": T},
    }


@template("table_and_hanging_mass", PHYS, "Classical Mechanics", "Newton's laws", "hard")
def table_and_hanging_mass(rng):
    while True:
        m1 = nice(rng, 1, 20, 1)
        m2 = nice(rng, 1, 15, 1)
        mu = nice(rng, 0.0, 0.5, 0.05)
        if m2 > mu * m1 + 0.3:
            break
    a = (m2 - mu * m1) * g / (m1 + m2)
    T = m2 * (g - a)
    question = (
        f"A {q(m1, 'kg')} block on a horizontal table is connected by a light string over a frictionless pulley "
        f"at the table's edge to a hanging {q(m2, 'kg')} mass. The coefficient of kinetic friction between the block "
        f"and the table is {fmt(mu, 2)}. Find the acceleration of the system and the tension in the string."
    )
    steps = [
        f"Block on table: $T - \\mu_km_1g = m_1a$.",
        f"Hanging mass: $m_2g - T = m_2a$.",
        f"Add the equations: $a = \\frac{{(m_2 - \\mu_km_1)g}}{{m_1 + m_2}} = \\frac{{({fmt(m2)} - {fmt(mu, 2)}\\times{fmt(m1)})(9.81)}}{{{fmt(m1 + m2)}}} = {fmt(a)}$ m/s².",
        f"Tension: $T = m_2(g - a) = {fmt(m2)}(9.81 - {fmt(a)}) = {fmt(T)}$ N.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$a = {fmt(a)}$ m/s², $T = {fmt(T)}$ N",
        "values": {"m1": m1, "m2": m2, "mu_k": mu, "a": a, "T": T},
    }


@template("elevator_scale", PHYS, "Classical Mechanics", "Newton's laws", "easy")
def elevator_scale(rng):
    m = nice(rng, 40, 110, 1)
    a = nice(rng, 0.5, 4.0, 0.5)
    direction = pick(rng, ["accelerating upward", "accelerating downward", "moving upward while slowing down", "moving downward while slowing down"])
    sign = {"accelerating upward": 1, "moving downward while slowing down": 1}.get(direction, -1)
    N = m * (g + sign * a)
    question = (
        f"A {q(m, 'kg')} person stands on a bathroom scale in an elevator that is {direction} at {q(a, 'm/s²')}. "
        "What does the scale read (in newtons), and what is the person's apparent mass?"
    )
    steps = [
        "The scale reads the normal force $N$. Take upward as positive.",
        f"The acceleration vector points {'up' if sign > 0 else 'down'}, so $a_y = {'+' if sign > 0 else '-'}{fmt(a)}$ m/s².",
        f"Newton's second law: $N - mg = ma_y \\Rightarrow N = m(g {'+' if sign > 0 else '-'} a) = {fmt(m)}(9.81 {'+' if sign > 0 else '-'} {fmt(a)}) = {fmt(N)}$ N.",
        f"Apparent mass $= N/g = {fmt(N / g)}$ kg (true mass {fmt(m)} kg).",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$N = {fmt(N)}$ N (apparent mass {q(N / g, 'kg')})",
        "values": {"m": m, "a": a, "sign": sign, "N": N},
    }


@template("circular_motion", PHYS, "Classical Mechanics", "Circular motion", "easy")
def circular_motion(rng):
    m = nice(rng, 0.1, 5.0, 0.1) if rng.random() < 0.3 else nice(rng, 500, 2000, 50)
    v = nice(rng, 2, 40, 1)
    r = nice(rng, 5, 200, 5)
    ac = v ** 2 / r
    F = m * ac
    period = 2 * math.pi * r / v
    question = (
        f"An object of mass {q(m, 'kg')} moves in a horizontal circle of radius {q(r, 'm')} at a constant speed of "
        f"{q(v, 'm/s')}. Find its centripetal acceleration, the net (centripetal) force on it and its period."
    )
    steps = [
        f"Centripetal acceleration: $a_c = \\frac{{v^2}}{{r}} = \\frac{{({fmt(v)})^2}}{{{fmt(r)}}} = {fmt(ac)}$ m/s², directed toward the center.",
        f"Net force: $F_c = ma_c = ({fmt(m)})({fmt(ac)}) = {fmt(F)}$ N.",
        f"Period: $T = \\frac{{2\\pi r}}{{v}} = {fmt(period)}$ s.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$a_c = {fmt(ac)}$ m/s², $F_c = {fmt(F)}$ N, $T = {fmt(period)}$ s",
        "values": {"m": m, "v": v, "r": r, "a_c": ac, "F_c": F, "T": period},
    }


@template("flat_curve_max_speed", PHYS, "Classical Mechanics", "Circular motion", "medium")
def flat_curve_max_speed(rng):
    mu = nice(rng, 0.2, 1.0, 0.05)
    r = nice(rng, 20, 300, 10)
    v = math.sqrt(mu * g * r)
    surface = "dry asphalt" if mu >= 0.7 else ("wet road" if mu >= 0.4 else "icy or snowy road")
    question = (
        f"What is the maximum speed at which a car can safely round a flat (unbanked) curve of radius {q(r, 'm')} "
        f"if the coefficient of static friction between the tires and the road ({surface}) is {fmt(mu, 2)}?"
    )
    steps = [
        "Static friction supplies the centripetal force: $\\mu_smg \\ge \\frac{mv^2}{r}$.",
        f"The mass cancels: $v_{{max}} = \\sqrt{{\\mu_sgr}} = \\sqrt{{({fmt(mu, 2)})(9.81)({fmt(r)})}} = {fmt(v)}$ m/s.",
        f"In km/h: ${fmt(v)} \\times 3.6 = {fmt(v * 3.6)}$ km/h.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v_{{max}} = {fmt(v)}$ m/s ≈ {q(v * 3.6, 'km/h')}",
        "values": {"mu_s": mu, "r": r, "v_max": v},
    }


# ---------------------------------------------------------------------------
# Work, energy, momentum
# ---------------------------------------------------------------------------


@template("energy_conservation_slide", PHYS, "Classical Mechanics", "Energy conservation", "easy")
def energy_conservation_slide(rng):
    h = nice(rng, 1, 60, 1)
    m = nice(rng, 1, 80, 1)
    v = math.sqrt(2 * g * h)
    what = pick(rng, ["a child on a frictionless slide", "a skateboarder on a smooth ramp", "a roller-coaster car", "a sled on frictionless ice"])
    question = (
        f"{what.capitalize()} of total mass {q(m, 'kg')} starts from rest at a height of {q(h, 'm')}. "
        "Neglecting friction, how fast is it moving at the bottom (height 0)?"
    )
    steps = [
        "Only gravity does work, so mechanical energy is conserved: $mgh = \\tfrac12mv^2$.",
        f"The mass cancels: $v = \\sqrt{{2gh}} = \\sqrt{{2(9.81)({fmt(h)})}} = {fmt(v)}$ m/s.",
        f"The potential energy converted is $mgh = {fmt(m * g * h)}$ J.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v = {fmt(v)}$ m/s",
        "values": {"h": h, "m": m, "v": v},
    }


@template("spring_launch", PHYS, "Classical Mechanics", "Energy conservation", "medium")
def spring_launch(rng):
    k = nice(rng, 100, 2000, 50)
    x = nice(rng, 0.02, 0.30, 0.01)
    m = nice(rng, 0.05, 2.0, 0.05)
    U = 0.5 * k * x * x
    v = math.sqrt(k / m) * x
    question = (
        f"A spring with spring constant {q(k, 'N/m')} is compressed by {q(x * 100, 'cm')} and used to launch a "
        f"{q(m, 'kg')} block on a frictionless horizontal surface. What is the block's speed after it leaves the spring?"
    )
    steps = [
        f"Elastic potential energy stored: $U = \\tfrac12kx^2 = \\tfrac12({fmt(k)})({fmt(x)})^2 = {fmt(U)}$ J.",
        f"All of it becomes kinetic energy: $\\tfrac12mv^2 = U \\Rightarrow v = x\\sqrt{{k/m}} = {fmt(x)}\\sqrt{{{fmt(k)}/{fmt(m)}}} = {fmt(v)}$ m/s.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v = {fmt(v)}$ m/s",
        "values": {"k": k, "x": x, "m": m, "U": U, "v": v},
    }


@template("work_and_power_lifting", PHYS, "Classical Mechanics", "Work and power", "easy")
def work_and_power_lifting(rng):
    m = nice(rng, 10, 1000, 10)
    h = nice(rng, 2, 50, 1)
    t = nice(rng, 2, 120, 1)
    W = m * g * h
    P = W / t
    question = (
        f"A motor lifts a {q(m, 'kg')} load at constant speed through a height of {q(h, 'm')} in {q(t, 's')}. "
        "How much work does the motor do, and what is its average power output (in W and in horsepower)?"
    )
    steps = [
        f"At constant speed the lifting force equals the weight: $F = mg = {fmt(m * g)}$ N.",
        f"Work: $W = Fh = mgh = ({fmt(m)})(9.81)({fmt(h)}) = {fmt(W)}$ J.",
        f"Power: $P = W/t = {fmt(W)}/{fmt(t)} = {fmt(P)}$ W $= {fmt(P / 745.7)}$ hp (1 hp = 745.7 W).",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$W = {fmt(W)}$ J; $P = {fmt(P)}$ W ≈ {q(P / 745.7, 'hp')}",
        "values": {"m": m, "h": h, "t": t, "W": W, "P": P},
    }


@template("perfectly_inelastic_collision", PHYS, "Classical Mechanics", "Momentum", "medium")
def perfectly_inelastic_collision(rng):
    m1 = nice(rng, 500, 3000, 100)
    m2 = nice(rng, 500, 3000, 100)
    v1 = nice(rng, 5, 30, 1)
    v2 = -nice(rng, 0, 25, 1) if rng.random() < 0.5 else nice(rng, 0, 4, 1)
    vf = (m1 * v1 + m2 * v2) / (m1 + m2)
    ke_i = 0.5 * m1 * v1 ** 2 + 0.5 * m2 * v2 ** 2
    ke_f = 0.5 * (m1 + m2) * vf ** 2
    lost = ke_i - ke_f
    question = (
        f"A {q(m1, 'kg')} car moving at {q(v1, 'm/s')} collides with a {q(m2, 'kg')} car moving at {q(v2, 'm/s')} "
        "along the same line (positive = direction of the first car). The cars lock together. Find their common velocity "
        "just after the collision and the kinetic energy lost."
    )
    steps = [
        f"Momentum is conserved: $m_1v_1 + m_2v_2 = (m_1 + m_2)v_f$.",
        f"$v_f = \\frac{{({fmt(m1)})({fmt(v1)}) + ({fmt(m2)})({fmt(v2)})}}{{{fmt(m1 + m2)}}} = {fmt(vf)}$ m/s.",
        f"Initial kinetic energy: $K_i = {fmt(ke_i)}$ J; final: $K_f = \\tfrac12(m_1 + m_2)v_f^2 = {fmt(ke_f)}$ J.",
        f"Kinetic energy lost (to deformation, heat, sound): $\\Delta K = {fmt(lost)}$ J ({fmt(100 * lost / ke_i)}% of the initial).",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v_f = {fmt(vf)}$ m/s; kinetic energy lost $= {fmt(lost)}$ J",
        "values": {"m1": m1, "m2": m2, "v1": v1, "v2": v2, "vf": vf, "KE_lost": lost},
    }


@template("elastic_collision_1d", PHYS, "Classical Mechanics", "Momentum", "hard")
def elastic_collision_1d(rng):
    m1 = nice(rng, 0.5, 10.0, 0.5)
    m2 = nice(rng, 0.5, 10.0, 0.5)
    v1 = nice(rng, 1, 15, 1)
    v1f = (m1 - m2) / (m1 + m2) * v1
    v2f = 2 * m1 / (m1 + m2) * v1
    question = (
        f"A {q(m1, 'kg')} ball moving at {q(v1, 'm/s')} collides head-on and elastically with a stationary "
        f"{q(m2, 'kg')} ball. Find the velocities of both balls after the collision."
    )
    steps = [
        "Elastic collision: both momentum and kinetic energy are conserved, and the relative velocity reverses.",
        f"$v_1' = \\frac{{m_1 - m_2}}{{m_1 + m_2}}v_1 = \\frac{{{fmt(m1)} - {fmt(m2)}}}{{{fmt(m1 + m2)}}}({fmt(v1)}) = {fmt(v1f)}$ m/s.",
        f"$v_2' = \\frac{{2m_1}}{{m_1 + m_2}}v_1 = {fmt(v2f)}$ m/s.",
        f"Check momentum: before ${fmt(m1 * v1)}$, after ${fmt(m1 * v1f + m2 * v2f)}$ kg·m/s. ✓",
        "A negative $v_1'$ means the first ball bounces back." if v1f < 0 else ("The balls exchange velocities (equal masses)." if m1 == m2 else "Both balls move forward."),
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v_1' = {fmt(v1f)}$ m/s, $v_2' = {fmt(v2f)}$ m/s",
        "values": {"m1": m1, "m2": m2, "v1": v1, "v1f": v1f, "v2f": v2f},
    }


@template("impulse_average_force", PHYS, "Classical Mechanics", "Momentum", "medium")
def impulse_average_force(rng):
    m = nice(rng, 0.05, 0.5, 0.01)
    vi = nice(rng, 5, 45, 1)
    vf = nice(rng, 5, 50, 1)
    dt = nice(rng, 0.5, 10.0, 0.5) * 1e-3
    J = m * (vf + vi)  # reversal of direction
    F = J / dt
    ball = pick(rng, ["baseball", "tennis ball", "cricket ball", "soccer ball", "hockey puck"])
    question = (
        f"A {q(m, 'kg')} {ball} arrives at {q(vi, 'm/s')} and is struck so that it leaves in the opposite direction at "
        f"{q(vf, 'm/s')}. The contact lasts {q(dt * 1000, 'ms')}. Find the impulse and the average force."
    )
    steps = [
        "Take the outgoing direction as positive, so the incoming velocity is negative.",
        f"Impulse = change in momentum: $J = m(v_f - v_i) = {fmt(m)}[{fmt(vf)} - (-{fmt(vi)})] = {fmt(J)}$ N·s.",
        f"Average force: $F = J/\\Delta t = {fmt(J)}/({fmt(dt)}) = {fmt(F)}$ N.",
        f"That is about ${fmt(F / (m * g))}$ times the ball's weight.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$J = {fmt(J)}$ N·s; $F_{{avg}} = {fmt(F)}$ N",
        "values": {"m": m, "vi": vi, "vf": vf, "dt": dt, "J": J, "F": F},
    }


# ---------------------------------------------------------------------------
# Rotation, gravitation, oscillations, fluids
# ---------------------------------------------------------------------------

ROLLERS = [
    ("solid sphere", 2 / 5, "\\tfrac25"),
    ("solid cylinder", 1 / 2, "\\tfrac12"),
    ("thin hoop", 1.0, "1"),
    ("hollow sphere", 2 / 3, "\\tfrac23"),
]


@template("rolling_down_incline", PHYS, "Classical Mechanics", "Rotational dynamics", "hard")
def rolling_down_incline(rng):
    name, c, cs = pick(rng, ROLLERS)
    h = nice(rng, 0.5, 10.0, 0.5)
    v = math.sqrt(2 * g * h / (1 + c))
    v_slide = math.sqrt(2 * g * h)
    question = (
        f"A {name} is released from rest and rolls without slipping down a ramp of vertical height {q(h, 'm')}. "
        "What is its speed at the bottom? Compare with a block sliding down a frictionless ramp."
    )
    steps = [
        f"For a {name}, $I = cMR^2$ with $c = {cs}$; rolling without slipping means $v = \\omega R$.",
        "Energy conservation: $Mgh = \\tfrac12Mv^2 + \\tfrac12I\\omega^2 = \\tfrac12Mv^2(1 + c)$.",
        f"$v = \\sqrt{{\\frac{{2gh}}{{1 + c}}}} = \\sqrt{{\\frac{{2(9.81)({fmt(h)})}}{{1 + {fmt(c)}}}}} = {fmt(v)}$ m/s.",
        f"A frictionless sliding block would reach $\\sqrt{{2gh}} = {fmt(v_slide)}$ m/s; the rolling object is slower because part of the energy goes into rotation.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v = {fmt(v)}$ m/s (vs. {q(v_slide, 'm/s')} for sliding without friction)",
        "values": {"c": c, "h": h, "v": v},
    }


@template("torque_angular_acceleration", PHYS, "Classical Mechanics", "Rotational dynamics", "medium")
def torque_angular_acceleration(rng):
    M = nice(rng, 1, 50, 1)
    R = nice(rng, 0.1, 1.0, 0.05)
    F = nice(rng, 5, 200, 5)
    t = nice(rng, 1, 10, 1)
    I = 0.5 * M * R * R
    tau = F * R
    alpha = tau / I
    omega = alpha * t
    rpm = omega * 60 / (2 * math.pi)
    question = (
        f"A uniform solid disk (mass {q(M, 'kg')}, radius {q(R, 'm')}) can spin freely about its central axis. "
        f"A constant tangential force of {q(F, 'N')} is applied at its rim, starting from rest. Find the angular "
        f"acceleration and the angular speed after {q(t, 's')}."
    )
    steps = [
        f"Moment of inertia: $I = \\tfrac12MR^2 = \\tfrac12({fmt(M)})({fmt(R)})^2 = {fmt(I)}$ kg·m².",
        f"Torque: $\\tau = FR = ({fmt(F)})({fmt(R)}) = {fmt(tau)}$ N·m.",
        f"Angular acceleration: $\\alpha = \\tau/I = {fmt(alpha)}$ rad/s².",
        f"After {fmt(t)} s: $\\omega = \\alpha t = {fmt(omega)}$ rad/s $= {fmt(rpm)}$ rpm.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\alpha = {fmt(alpha)}$ rad/s²; $\\omega = {fmt(omega)}$ rad/s",
        "values": {"M": M, "R": R, "F": F, "t": t, "alpha": alpha, "omega": omega},
    }


@template("angular_momentum_skater", PHYS, "Classical Mechanics", "Rotational dynamics", "medium")
def angular_momentum_skater(rng):
    I1 = nice(rng, 2.0, 6.0, 0.1)
    I2 = round(I1 * nice(rng, 0.25, 0.6, 0.05), 2)
    w1 = nice(rng, 0.5, 3.0, 0.1)
    w2 = I1 * w1 / I2
    ratio = (0.5 * I2 * w2 ** 2) / (0.5 * I1 * w1 ** 2)
    question = (
        f"A figure skater spins at {q(w1, 'rev/s')} with arms extended (moment of inertia {q(I1, 'kg·m²')}). "
        f"Pulling in the arms reduces the moment of inertia to {q(I2, 'kg·m²')}. Find the new spin rate and the ratio of "
        "final to initial rotational kinetic energy."
    )
    steps = [
        "No external torque acts about the vertical axis, so angular momentum is conserved: $I_1\\omega_1 = I_2\\omega_2$.",
        f"$\\omega_2 = \\frac{{I_1}}{{I_2}}\\omega_1 = \\frac{{{fmt(I1)}}}{{{fmt(I2)}}}({fmt(w1)}) = {fmt(w2)}$ rev/s.",
        f"$\\frac{{K_2}}{{K_1}} = \\frac{{I_2\\omega_2^2}}{{I_1\\omega_1^2}} = \\frac{{I_1}}{{I_2}} = {fmt(ratio)}$.",
        "Kinetic energy increases; the extra energy comes from the work the skater's muscles do pulling the arms inward.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\omega_2 = {fmt(w2)}$ rev/s; $K_2/K_1 = {fmt(ratio)}$",
        "values": {"I1": I1, "I2": I2, "w1": w1, "w2": w2, "KE_ratio": ratio},
    }


@template("satellite_orbit", PHYS, "Classical Mechanics", "Gravitation", "medium")
def satellite_orbit(rng):
    h_km = pick(rng, [200, 400, 550, 1000, 20200, 35786]) if rng.random() < 0.3 else nice(rng, 160, 40000, 10)
    r = R_EARTH + h_km * 1000
    v = math.sqrt(G * M_EARTH / r)
    T = 2 * math.pi * r / v
    gloc = G * M_EARTH / r ** 2
    question = (
        f"A satellite is in a circular orbit {q(h_km, 'km')} above Earth's surface. Using "
        f"$M_E = 5.97\\times10^{{24}}$ kg and $R_E = 6371$ km, find its orbital speed, its period and the gravitational "
        "acceleration at that altitude."
    )
    steps = [
        f"Orbital radius: $r = R_E + h = {fmt(r / 1000, 4)}$ km $= {fmt(r, 4)}$ m.",
        f"Gravity supplies the centripetal force: $\\frac{{GMm}}{{r^2}} = \\frac{{mv^2}}{{r}} \\Rightarrow v = \\sqrt{{GM/r}} = {fmt(v)}$ m/s.",
        f"Period: $T = 2\\pi r/v = {fmt(T)}$ s $= {fmt(T / 60)}$ min $= {fmt(T / 3600)}$ h.",
        f"Local gravitational acceleration: $g = GM/r^2 = {fmt(gloc)}$ m/s² — astronauts feel weightless because they are in free fall, not because gravity vanishes.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v = {fmt(v)}$ m/s; $T = {fmt(T / 60)}$ min; $g = {fmt(gloc)}$ m/s²",
        "values": {"h_km": h_km, "v": v, "T": T, "g_local": gloc},
    }


PLANETS = [
    ("Mercury", 3.301e23, 2.4397e6),
    ("Venus", 4.867e24, 6.0518e6),
    ("Earth", 5.972e24, 6.371e6),
    ("the Moon", 7.342e22, 1.7374e6),
    ("Mars", 6.417e23, 3.3895e6),
    ("Jupiter", 1.898e27, 6.9911e7),
    ("Saturn", 5.683e26, 5.8232e7),
    ("Uranus", 8.681e25, 2.5362e7),
    ("Neptune", 1.024e26, 2.4622e7),
]


@template("surface_gravity_escape_velocity", PHYS, "Classical Mechanics", "Gravitation", "medium")
def surface_gravity_escape_velocity(rng):
    name, M, R = pick(rng, PLANETS)
    gs = G * M / R ** 2
    vesc = math.sqrt(2 * G * M / R)
    question = (
        f"{name.capitalize() if name.startswith('the') else name} has mass ${fmt(M, 4)}$ kg and radius ${fmt(R / 1000, 5)}$ km. "
        "Calculate its surface gravitational acceleration and its escape velocity."
    )
    steps = [
        f"Surface gravity: $g = \\frac{{GM}}{{R^2}} = \\frac{{(6.674\\times10^{{-11}})({fmt(M, 4)})}}{{({fmt(R, 4)})^2}} = {fmt(gs)}$ m/s² (${fmt(gs / 9.81)}$ times Earth's).",
        f"Escape velocity (total energy zero): $v_{{esc}} = \\sqrt{{2GM/R}} = {fmt(vesc)}$ m/s $= {fmt(vesc / 1000)}$ km/s.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$g = {fmt(gs)}$ m/s²; $v_{{esc}} = {fmt(vesc / 1000)}$ km/s",
        "values": {"M": M, "R": R, "g_surface": gs, "v_esc": vesc},
    }


@template("pendulum_period", PHYS, "Classical Mechanics", "Oscillations", "easy")
def pendulum_period(rng):
    L = nice(rng, 0.1, 5.0, 0.05)
    place, gl = pick(rng, [("on Earth", 9.81), ("on the Moon", 1.62), ("on Mars", 3.71), ("on Earth", 9.81)])
    T = 2 * math.pi * math.sqrt(L / gl)
    f = 1 / T
    question = (
        f"What is the period of a simple pendulum of length {q(L, 'm')} {place} ($g = {fmt(gl)}$ m/s²) for small oscillations? "
        "How many complete swings does it make per minute?"
    )
    steps = [
        f"Small-angle period: $T = 2\\pi\\sqrt{{L/g}} = 2\\pi\\sqrt{{{fmt(L)}/{fmt(gl)}}} = {fmt(T)}$ s.",
        f"Frequency $f = 1/T = {fmt(f)}$ Hz, i.e. ${fmt(60 * f)}$ oscillations per minute.",
        "The period does not depend on the bob's mass or (for small angles) on the amplitude.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$T = {fmt(T)}$ s ({fmt(60 * f)} swings per minute)",
        "values": {"L": L, "g": gl, "T": T},
    }


@template("spring_mass_shm", PHYS, "Classical Mechanics", "Oscillations", "medium")
def spring_mass_shm(rng):
    m = nice(rng, 0.1, 5.0, 0.1)
    k = nice(rng, 10, 1000, 10)
    A = nice(rng, 0.01, 0.30, 0.01)
    w = math.sqrt(k / m)
    T = 2 * math.pi / w
    vmax = A * w
    amax = A * w * w
    E = 0.5 * k * A * A
    question = (
        f"A {q(m, 'kg')} mass on a spring ($k = {fmt(k)}$ N/m) oscillates on a frictionless surface with amplitude "
        f"{q(A * 100, 'cm')}. Find the angular frequency, period, maximum speed, maximum acceleration and total energy."
    )
    steps = [
        f"$\\omega = \\sqrt{{k/m}} = \\sqrt{{{fmt(k)}/{fmt(m)}}} = {fmt(w)}$ rad/s; $T = 2\\pi/\\omega = {fmt(T)}$ s.",
        f"$v_{{max}} = A\\omega = ({fmt(A)})({fmt(w)}) = {fmt(vmax)}$ m/s (at equilibrium).",
        f"$a_{{max}} = A\\omega^2 = {fmt(amax)}$ m/s² (at the turning points).",
        f"$E = \\tfrac12kA^2 = {fmt(E)}$ J (constant).",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\omega = {fmt(w)}$ rad/s, $T = {fmt(T)}$ s, $v_{{max}} = {fmt(vmax)}$ m/s, $a_{{max}} = {fmt(amax)}$ m/s², $E = {fmt(E)}$ J",
        "values": {"m": m, "k": k, "A": A, "omega": w, "T": T, "v_max": vmax, "a_max": amax, "E": E},
    }


@template("hydrostatic_pressure", PHYS, "Classical Mechanics", "Fluids", "easy")
def hydrostatic_pressure(rng):
    d = nice(rng, 1, 200, 1)
    fluid, rho = pick(rng, [("fresh water", 1000), ("seawater", 1025)])
    Pg = rho * g * d
    Pabs = 101325 + Pg
    question = (
        f"What is the gauge pressure and the absolute pressure at a depth of {q(d, 'm')} in {fluid} "
        f"($\\rho = {rho}$ kg/m³)? Express the absolute pressure in atmospheres."
    )
    steps = [
        f"Gauge pressure: $P_g = \\rho gh = ({rho})(9.81)({fmt(d)}) = {fmt(Pg)}$ Pa.",
        f"Absolute pressure: $P = P_{{atm}} + \\rho gh = 101\\,325 + {fmt(Pg)} = {fmt(Pabs)}$ Pa.",
        f"In atmospheres: ${fmt(Pabs)}/101\\,325 = {fmt(Pabs / 101325)}$ atm.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$P_g = {fmt(Pg)}$ Pa; $P = {fmt(Pabs)}$ Pa ≈ {q(Pabs / 101325, 'atm')}",
        "values": {"depth": d, "rho": rho, "P_gauge": Pg, "P_abs": Pabs},
    }


@template("buoyancy_floating", PHYS, "Classical Mechanics", "Fluids", "easy")
def buoyancy_floating(rng):
    obj, rho_o = pick(rng, [("ice", 917), ("oak wood", 750), ("pine wood", 500), ("polyethylene", 950), ("cork", 240), ("a human body (lungs full)", 985)])
    fluid, rho_f = pick(rng, [("fresh water", 1000), ("seawater", 1025)])
    V = nice(rng, 0.01, 2.0, 0.01)
    frac = rho_o / rho_f
    FB = rho_o * V * g
    question = (
        f"A block of {obj} (density {q(rho_o, 'kg/m³')}) with volume {q(V, 'm³')} floats in {fluid} "
        f"(density {q(rho_f, 'kg/m³')}). What fraction of its volume is submerged, and what is the buoyant force?"
    )
    steps = [
        "For a floating object, buoyant force = weight: $\\rho_f V_{sub} g = \\rho_o V g$.",
        f"Fraction submerged: $\\frac{{V_{{sub}}}}{{V}} = \\frac{{\\rho_o}}{{\\rho_f}} = \\frac{{{rho_o}}}{{{rho_f}}} = {fmt(frac)}$ ({fmt(100 * frac)}%).",
        f"Buoyant force = weight $= \\rho_oVg = ({rho_o})({fmt(V)})(9.81) = {fmt(FB)}$ N.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"{fmt(100 * frac)}% submerged; $F_B = {fmt(FB)}$ N",
        "values": {"rho_object": rho_o, "rho_fluid": rho_f, "V": V, "fraction": frac, "F_B": FB},
    }


@template("continuity_bernoulli", PHYS, "Classical Mechanics", "Fluids", "hard")
def continuity_bernoulli(rng):
    d1 = nice(rng, 2, 10, 1)
    d2 = nice(rng, 1, d1 - 1 if d1 > 1 else 1, 1) if d1 > 2 else 1
    v1 = nice(rng, 0.5, 4.0, 0.5)
    P1 = nice(rng, 120, 400, 10) * 1000
    v2 = v1 * (d1 / d2) ** 2
    P2 = P1 + 0.5 * 1000 * (v1 ** 2 - v2 ** 2)
    question = (
        f"Water flows through a horizontal pipe that narrows from a diameter of {q(d1, 'cm')} to {q(d2, 'cm')}. "
        f"In the wide section the speed is {q(v1, 'm/s')} and the pressure is {q(P1 / 1000, 'kPa')}. "
        "Find the speed and pressure in the narrow section."
    )
    steps = [
        f"Continuity ($A_1v_1 = A_2v_2$, $A \\propto d^2$): $v_2 = v_1(d_1/d_2)^2 = {fmt(v1)}({fmt(d1)}/{fmt(d2)})^2 = {fmt(v2)}$ m/s.",
        f"Bernoulli at equal height: $P_2 = P_1 + \\tfrac12\\rho(v_1^2 - v_2^2) = {fmt(P1)} + 500({fmt(v1 ** 2)} - {fmt(v2 ** 2)}) = {fmt(P2)}$ Pa.",
        "Faster flow means lower pressure (the Venturi effect)." + (" (A negative absolute pressure would indicate cavitation — the model breaks down.)" if P2 < 0 else ""),
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v_2 = {fmt(v2)}$ m/s; $P_2 = {fmt(P2 / 1000)}$ kPa",
        "values": {"d1": d1, "d2": d2, "v1": v1, "P1": P1, "v2": v2, "P2": P2},
    }


# ---------------------------------------------------------------------------
# Thermodynamics
# ---------------------------------------------------------------------------


@template("ideal_gas_pressure", PHYS, "Thermodynamics", "Ideal gas law", "easy")
def ideal_gas_pressure(rng):
    n = nice(rng, 0.1, 5.0, 0.1)
    TC = nice(rng, -50, 300, 5)
    VL = nice(rng, 1, 100, 1)
    T = TC + 273.15
    P = n * R_GAS * T / (VL / 1000)
    question = (
        f"What pressure is exerted by {q(n, 'mol')} of an ideal gas in a {q(VL, 'L')} container at {q(TC, '°C')}? "
        "Give the answer in kPa and atm."
    )
    steps = [
        f"Convert units: $T = {fmt(TC)} + 273.15 = {fmt(T, 5)}$ K; $V = {fmt(VL)}$ L $= {fmt(VL / 1000)}$ m³.",
        f"$P = \\frac{{nRT}}{{V}} = \\frac{{({fmt(n)})(8.314)({fmt(T, 5)})}}{{{fmt(VL / 1000)}}} = {fmt(P)}$ Pa.",
        f"$P = {fmt(P / 1000)}$ kPa $= {fmt(P / 101325)}$ atm.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$P = {fmt(P / 1000)}$ kPa ≈ {q(P / 101325, 'atm')}",
        "values": {"n": n, "T_C": TC, "V_L": VL, "P": P},
    }


METALS = [("aluminum", 900), ("copper", 385), ("iron", 450), ("lead", 128), ("silver", 235), ("brass", 380)]


@template("calorimetry_mixing", PHYS, "Thermodynamics", "Calorimetry", "medium")
def calorimetry_mixing(rng):
    metal, cm = pick(rng, METALS)
    mm = nice(rng, 0.05, 1.0, 0.05)
    Tm = nice(rng, 60, 300, 5)
    mw = nice(rng, 0.1, 2.0, 0.1)
    Tw = nice(rng, 5, 30, 1)
    cw = 4186
    Tf = (mm * cm * Tm + mw * cw * Tw) / (mm * cm + mw * cw)
    question = (
        f"A {q(mm, 'kg')} piece of {metal} ($c = {cm}$ J/(kg·K)) at {q(Tm, '°C')} is dropped into {q(mw, 'kg')} of water "
        f"($c = 4186$ J/(kg·K)) at {q(Tw, '°C')} in an insulated container. Find the final equilibrium temperature."
    )
    steps = [
        "Heat lost by the metal equals heat gained by the water: $m_mc_m(T_m - T_f) = m_wc_w(T_f - T_w)$.",
        f"Solve: $T_f = \\frac{{m_mc_mT_m + m_wc_wT_w}}{{m_mc_m + m_wc_w}} = \\frac{{({fmt(mm)})({cm})({fmt(Tm)}) + ({fmt(mw)})(4186)({fmt(Tw)})}}{{({fmt(mm)})({cm}) + ({fmt(mw)})(4186)}}$.",
        f"$T_f = {fmt(Tf)}$ °C. Water's large heat capacity keeps the final temperature close to its starting value.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$T_f = {fmt(Tf)}$ °C",
        "values": {"m_metal": mm, "c_metal": cm, "T_metal": Tm, "m_water": mw, "T_water": Tw, "T_final": Tf},
    }


@template("heating_ice_to_steam", PHYS, "Thermodynamics", "Phase changes", "hard")
def heating_ice_to_steam(rng):
    m = nice(rng, 0.1, 3.0, 0.1)
    Ti = -nice(rng, 1, 40, 1)
    Tf = pick(rng, [nice(rng, 1, 99, 1), nice(rng, 101, 150, 1)])
    c_ice, c_w, c_st, Lf, Lv = 2100, 4186, 2010, 334000, 2257000
    Q1 = m * c_ice * (0 - Ti)
    Q2 = m * Lf
    if Tf < 100:
        Q3 = m * c_w * (Tf - 0)
        Q4 = Q5 = 0.0
    else:
        Q3 = m * c_w * 100
        Q4 = m * Lv
        Q5 = m * c_st * (Tf - 100)
    Qt = Q1 + Q2 + Q3 + Q4 + Q5
    final_state = "water" if Tf < 100 else "steam"
    question = (
        f"How much heat is needed to convert {q(m, 'kg')} of ice at {q(Ti, '°C')} into {final_state} at {q(Tf, '°C')}? "
        "Use $c_{ice} = 2100$, $c_{water} = 4186$, $c_{steam} = 2010$ J/(kg·K), $L_f = 334$ kJ/kg, $L_v = 2257$ kJ/kg."
    )
    steps = [
        f"Warm the ice to 0 °C: $Q_1 = mc_{{ice}}\\Delta T = ({fmt(m)})(2100)({fmt(-Ti)}) = {fmt(Q1)}$ J.",
        f"Melt it: $Q_2 = mL_f = {fmt(Q2)}$ J.",
    ]
    if Tf < 100:
        steps.append(f"Warm the water to {fmt(Tf)} °C: $Q_3 = mc_w\\Delta T = {fmt(Q3)}$ J.")
    else:
        steps += [
            f"Warm the water to 100 °C: $Q_3 = mc_w(100) = {fmt(Q3)}$ J.",
            f"Boil it: $Q_4 = mL_v = {fmt(Q4)}$ J.",
            f"Warm the steam to {fmt(Tf)} °C: $Q_5 = mc_{{steam}}\\Delta T = {fmt(Q5)}$ J.",
        ]
    steps.append(f"Total: $Q = {fmt(Qt)}$ J $= {fmt(Qt / 1000)}$ kJ.")
    return {
        "question": question,
        "steps": steps,
        "answer": f"$Q = {fmt(Qt / 1000)}$ kJ",
        "values": {"m": m, "T_initial": Ti, "T_final": Tf, "Q_total": Qt},
    }


@template("carnot_engine", PHYS, "Thermodynamics", "Heat engines", "medium")
def carnot_engine(rng):
    Th_C = nice(rng, 150, 900, 10)
    Tc_C = nice(rng, 0, 60, 5)
    Qh = nice(rng, 100, 5000, 100)
    Th, Tc = Th_C + 273.15, Tc_C + 273.15
    eta = 1 - Tc / Th
    W = eta * Qh
    Qc = Qh - W
    question = (
        f"A Carnot engine operates between a hot reservoir at {q(Th_C, '°C')} and a cold reservoir at {q(Tc_C, '°C')}. "
        f"If it absorbs {q(Qh, 'J')} of heat per cycle, find its efficiency, the work done per cycle, and the heat rejected."
    )
    steps = [
        f"Convert to kelvin: $T_H = {fmt(Th, 5)}$ K, $T_C = {fmt(Tc, 5)}$ K.",
        f"Carnot efficiency: $\\eta = 1 - T_C/T_H = 1 - {fmt(Tc, 5)}/{fmt(Th, 5)} = {fmt(eta)}$ ({fmt(100 * eta)}%).",
        f"Work: $W = \\eta Q_H = {fmt(W)}$ J; heat rejected: $Q_C = Q_H - W = {fmt(Qc)}$ J.",
        "No real engine between these temperatures can be more efficient (second law).",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\eta = {fmt(100 * eta)}$%; $W = {fmt(W)}$ J; $Q_C = {fmt(Qc)}$ J",
        "values": {"T_hot_C": Th_C, "T_cold_C": Tc_C, "Q_hot": Qh, "efficiency": eta, "W": W, "Q_cold": Qc},
    }


GASES = [("hydrogen (H₂)", 2.016e-3), ("helium", 4.003e-3), ("nitrogen (N₂)", 28.01e-3), ("oxygen (O₂)", 32.00e-3),
         ("carbon dioxide", 44.01e-3), ("argon", 39.95e-3), ("water vapor", 18.02e-3), ("methane", 16.04e-3)]


@template("rms_speed_gas", PHYS, "Thermodynamics", "Kinetic theory", "medium")
def rms_speed_gas(rng):
    gas, M = pick(rng, GASES)
    TC = nice(rng, -100, 500, 10)
    T = TC + 273.15
    v = math.sqrt(3 * R_GAS * T / M)
    KE = 1.5 * K_B * T
    question = (
        f"Calculate the root-mean-square speed of {gas} molecules (molar mass {q(M * 1000, 'g/mol', 4)}) at {q(TC, '°C')}, "
        "and the average translational kinetic energy per molecule."
    )
    steps = [
        f"$T = {fmt(T, 5)}$ K; $M = {fmt(M, 4)}$ kg/mol.",
        f"$v_{{rms}} = \\sqrt{{3RT/M}} = \\sqrt{{3(8.314)({fmt(T, 5)})/{fmt(M, 4)}}} = {fmt(v)}$ m/s.",
        f"$\\langle K\\rangle = \\tfrac32k_BT = 1.5(1.381\\times10^{{-23}})({fmt(T, 5)}) = {fmt(KE)}$ J — the same for every gas at this temperature.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v_{{rms}} = {fmt(v)}$ m/s; $\\langle K\\rangle = {fmt(KE)}$ J",
        "values": {"M": M, "T_C": TC, "v_rms": v, "KE_avg": KE},
    }


@template("thermal_expansion", PHYS, "Thermodynamics", "Thermal expansion", "easy")
def thermal_expansion(rng):
    mat, alpha = pick(rng, [("steel", 12e-6), ("aluminum", 23e-6), ("copper", 17e-6), ("concrete", 12e-6), ("glass", 9e-6), ("brass", 19e-6)])
    L = nice(rng, 1, 1500, 1)
    dT = nice(rng, 10, 80, 5)
    dL = alpha * L * dT
    question = (
        f"A {mat} structure is {q(L, 'm')} long. By how much does its length change when the temperature rises by "
        f"{q(dT, '°C')}? ($\\alpha = {fmt(alpha * 1e6)}\\times10^{{-6}}$ K⁻¹)"
    )
    steps = [
        f"Linear expansion: $\\Delta L = \\alpha L_0\\Delta T = ({fmt(alpha)})({fmt(L)})({fmt(dT)})$.",
        f"$\\Delta L = {fmt(dL)}$ m $= {fmt(dL * 1000)}$ mm.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\Delta L = {fmt(dL * 1000)}$ mm",
        "values": {"alpha": alpha, "L": L, "dT": dT, "dL": dL},
    }


# ---------------------------------------------------------------------------
# Electricity and magnetism
# ---------------------------------------------------------------------------


@template("coulomb_force", PHYS, "Electromagnetism", "Electrostatics", "easy")
def coulomb_force(rng):
    q1 = nice(rng, -10, 10, 1) or 3
    q2 = nice(rng, -10, 10, 1) or -2
    r = nice(rng, 1, 100, 1)
    F = K_E * abs(q1 * q2) * 1e-12 / (r / 100) ** 2
    kind = "repulsive" if q1 * q2 > 0 else "attractive"
    question = (
        f"Two point charges, $q_1 = {q1}$ μC and $q_2 = {q2}$ μC, are {q(r, 'cm')} apart. Find the magnitude of the "
        "electrostatic force between them and state whether it is attractive or repulsive."
    )
    steps = [
        f"Coulomb's law: $F = k\\frac{{|q_1q_2|}}{{r^2}} = (8.99\\times10^9)\\frac{{({abs(q1)}\\times10^{{-6}})({abs(q2)}\\times10^{{-6}})}}{{({fmt(r / 100)})^2}}$.",
        f"$F = {fmt(F)}$ N.",
        f"The charges have {'the same' if q1 * q2 > 0 else 'opposite'} signs, so the force is {kind}.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$F = {fmt(F)}$ N, {kind}",
        "values": {"q1_uC": q1, "q2_uC": q2, "r_cm": r, "F": F},
    }


@template("parallel_plate_capacitor", PHYS, "Electromagnetism", "Capacitance", "medium")
def parallel_plate_capacitor(rng):
    A_cm2 = nice(rng, 10, 1000, 10)
    d_mm = nice(rng, 0.1, 5.0, 0.1)
    V = nice(rng, 5, 500, 5)
    kappa, diel = pick(rng, [(1.0, "air"), (2.1, "Teflon"), (3.5, "paper"), (5.0, "glass")])
    A, d = A_cm2 * 1e-4, d_mm * 1e-3
    Cap = kappa * EPS0 * A / d
    Qc = Cap * V
    U = 0.5 * Cap * V * V
    E = V / d
    question = (
        f"A parallel-plate capacitor has plates of area {q(A_cm2, 'cm²')} separated by {q(d_mm, 'mm')} of {diel} "
        f"($\\kappa = {fmt(kappa, 2)}$). It is connected to a {q(V, 'V')} battery. Find the capacitance, the stored charge, "
        "the stored energy and the electric field between the plates."
    )
    steps = [
        f"$C = \\frac{{\\kappa\\varepsilon_0A}}{{d}} = \\frac{{({fmt(kappa, 2)})(8.854\\times10^{{-12}})({fmt(A)})}}{{{fmt(d)}}} = {fmt(Cap)}$ F.",
        f"$Q = CV = {fmt(Qc)}$ C.",
        f"$U = \\tfrac12CV^2 = {fmt(U)}$ J.",
        f"$E = V/d = {fmt(E)}$ V/m.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$C = {fmt(Cap)}$ F, $Q = {fmt(Qc)}$ C, $U = {fmt(U)}$ J, $E = {fmt(E)}$ V/m",
        "values": {"A": A, "d": d, "V": V, "kappa": kappa, "C": Cap, "Q": Qc, "U": U, "E": E},
    }


@template("resistor_network", PHYS, "Electromagnetism", "DC circuits", "medium")
def resistor_network(rng):
    R1 = nice(rng, 1, 100, 1)
    R2 = nice(rng, 1, 100, 1)
    R3 = nice(rng, 1, 100, 1)
    V = nice(rng, 3, 48, 1)
    Rp = R2 * R3 / (R2 + R3)
    Req = R1 + Rp
    I = V / Req
    V1 = I * R1
    Vp = I * Rp
    I2 = Vp / R2
    I3 = Vp / R3
    P = V * I
    question = (
        f"A resistor $R_1 = {R1}$ Ω is connected in series with a parallel combination of $R_2 = {R2}$ Ω and "
        f"$R_3 = {R3}$ Ω, across an ideal {q(V, 'V')} battery. Find the equivalent resistance, the current from the battery, "
        "the current through each parallel branch, and the total power delivered."
    )
    steps = [
        f"Parallel part: $R_p = \\frac{{R_2R_3}}{{R_2 + R_3}} = \\frac{{({R2})({R3})}}{{{R2 + R3}}} = {fmt(Rp)}$ Ω.",
        f"Equivalent resistance: $R_{{eq}} = R_1 + R_p = {fmt(Req)}$ Ω.",
        f"Battery current: $I = V/R_{{eq}} = {fmt(I)}$ A.",
        f"Voltage across the parallel pair: $V_p = IR_p = {fmt(Vp)}$ V (and $V_1 = IR_1 = {fmt(V1)}$ V; $V_1 + V_p = {fmt(V1 + Vp)}$ V ✓).",
        f"Branch currents: $I_2 = V_p/R_2 = {fmt(I2)}$ A, $I_3 = V_p/R_3 = {fmt(I3)}$ A (sum $= {fmt(I2 + I3)}$ A ✓).",
        f"Power: $P = VI = {fmt(P)}$ W.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$R_{{eq}} = {fmt(Req)}$ Ω, $I = {fmt(I)}$ A, $I_2 = {fmt(I2)}$ A, $I_3 = {fmt(I3)}$ A, $P = {fmt(P)}$ W",
        "values": {"R1": R1, "R2": R2, "R3": R3, "V": V, "R_eq": Req, "I": I, "I2": I2, "I3": I3, "P": P},
    }


@template("electrical_power_energy", PHYS, "Electromagnetism", "DC circuits", "easy")
def electrical_power_energy(rng):
    dev, P = pick(rng, [("kettle", 2000), ("hair dryer", 1800), ("microwave oven", 1000), ("LED bulb", 9),
                        ("laptop charger", 65), ("space heater", 1500), ("television", 120), ("refrigerator", 150)])
    V = pick(rng, [230, 120])
    hours = nice(rng, 0.5, 10.0, 0.5)
    price = nice(rng, 0.10, 0.40, 0.01)
    I = P / V
    R = V * V / P
    E_kwh = P * hours / 1000
    cost = E_kwh * price
    question = (
        f"A {q(P, 'W')} {dev} runs on a {q(V, 'V')} supply for {q(hours, 'h')}. Find the current it draws, its resistance "
        f"(treating it as a resistor), the energy used in kWh, and the cost at {fmt(price, 2)} per kWh."
    )
    steps = [
        f"$I = P/V = {P}/{V} = {fmt(I)}$ A.",
        f"$R = V^2/P = {fmt(R)}$ Ω.",
        f"Energy: $E = Pt = ({fmt(P / 1000)}$ kW$)({fmt(hours)}$ h$) = {fmt(E_kwh)}$ kWh $= {fmt(E_kwh * 3.6e6)}$ J.",
        f"Cost: ${fmt(E_kwh)} \\times {fmt(price, 2)} = {fmt(cost)}$ currency units.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$I = {fmt(I)}$ A, $R = {fmt(R)}$ Ω, $E = {fmt(E_kwh)}$ kWh, cost ≈ {fmt(cost)}",
        "values": {"P": P, "V": V, "hours": hours, "I": I, "R": R, "E_kWh": E_kwh},
    }


@template("rc_charging", PHYS, "Electromagnetism", "DC circuits", "hard")
def rc_charging(rng):
    Rk = nice(rng, 1, 100, 1)
    Cu = nice(rng, 1, 1000, 1)
    emf = nice(rng, 3, 24, 1)
    R, Cap = Rk * 1e3, Cu * 1e-6
    tau = R * Cap
    t = sig(tau * nice(rng, 0.2, 4.0, 0.1), 3)
    Vc = emf * (1 - math.exp(-t / tau))
    Ic = emf / R * math.exp(-t / tau)
    question = (
        f"An uncharged {q(Cu, 'μF')} capacitor is connected in series with a {q(Rk, 'kΩ')} resistor to a {q(emf, 'V')} "
        f"battery at $t = 0$. Find the time constant, and the capacitor voltage and circuit current at $t = {fmt(t)}$ s."
    )
    steps = [
        f"Time constant: $\\tau = RC = ({fmt(R)})({fmt(Cap)}) = {fmt(tau)}$ s.",
        f"Charging: $V_C(t) = \\mathcal{{E}}(1 - e^{{-t/\\tau}}) = {fmt(emf)}(1 - e^{{-{fmt(t / tau)}}}) = {fmt(Vc)}$ V.",
        f"Current: $I(t) = \\frac{{\\mathcal{{E}}}}{{R}}e^{{-t/\\tau}} = {fmt(Ic)}$ A.",
        f"At $t = \\tau$ the capacitor would be at 63.2% of {fmt(emf)} V; after $5\\tau$ it is essentially fully charged.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\tau = {fmt(tau)}$ s; $V_C = {fmt(Vc)}$ V; $I = {fmt(Ic)}$ A",
        "values": {"R": R, "C": Cap, "emf": emf, "t": t, "tau": tau, "V_C": Vc, "I": Ic},
    }


@template("charged_particle_in_b_field", PHYS, "Electromagnetism", "Magnetism", "medium")
def charged_particle_in_b_field(rng):
    name, m, qq = pick(rng, [("proton", M_P, E_CHARGE), ("electron", M_E, E_CHARGE), ("alpha particle", 6.645e-27, 2 * E_CHARGE)])
    v = nice(rng, 1, 9, 1) * 10 ** pick(rng, [5, 6]) if name != "electron" else nice(rng, 1, 9, 1) * 10 ** pick(rng, [6, 7])
    B = nice(rng, 0.01, 2.0, 0.01)
    F = qq * v * B
    r = m * v / (qq * B)
    f = qq * B / (2 * math.pi * m)
    question = (
        f"An {name}" if name[0] in "aeiou" else f"A {name}"
    ) + (
        f" moves at ${fmt(v)}$ m/s perpendicular to a uniform magnetic field of {q(B, 'T')}. "
        "Find the magnetic force on it, the radius of its circular path, and its cyclotron frequency."
    )
    steps = [
        f"Force: $F = |q|vB = ({fmt(qq, 4)})({fmt(v)})({fmt(B)}) = {fmt(F)}$ N (perpendicular to the velocity; does no work).",
        f"Radius: $r = \\frac{{mv}}{{|q|B}} = {fmt(r)}$ m.",
        f"Cyclotron frequency: $f = \\frac{{|q|B}}{{2\\pi m}} = {fmt(f)}$ Hz (independent of speed).",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$F = {fmt(F)}$ N, $r = {fmt(r)}$ m, $f = {fmt(f)}$ Hz",
        "values": {"m": m, "q": qq, "v": v, "B": B, "F": F, "r": r, "f": f},
    }


@template("magnetic_field_wire_solenoid", PHYS, "Electromagnetism", "Magnetism", "easy")
def magnetic_field_wire_solenoid(rng):
    if rng.random() < 0.5:
        I = nice(rng, 1, 100, 1)
        r = nice(rng, 0.5, 50.0, 0.5)
        B = MU0 * I / (2 * math.pi * r / 100)
        question = (
            f"What is the magnetic field strength {q(r, 'cm')} from a long straight wire carrying {q(I, 'A')}? "
            "Compare it with Earth's field (~50 μT)."
        )
        steps = [
            f"Ampère's law for a long wire: $B = \\frac{{\\mu_0I}}{{2\\pi r}} = \\frac{{(4\\pi\\times10^{{-7}})({fmt(I)})}}{{2\\pi({fmt(r / 100)})}}$.",
            f"$B = {fmt(B)}$ T $= {fmt(B * 1e6)}$ μT, about ${fmt(B / 50e-6)}$ times Earth's field.",
        ]
        return {"question": question, "steps": steps, "answer": f"$B = {fmt(B * 1e6)}$ μT",
                "values": {"I": I, "r_cm": r, "B": B}}
    n = nice(rng, 100, 5000, 100)
    I = nice(rng, 0.5, 20.0, 0.5)
    B = MU0 * n * I
    question = (
        f"A long solenoid has {n} turns per meter and carries a current of {q(I, 'A')}. What is the magnetic field inside it?"
    )
    steps = [
        f"For an ideal solenoid: $B = \\mu_0nI = (4\\pi\\times10^{{-7}})({n})({fmt(I)})$.",
        f"$B = {fmt(B)}$ T $= {fmt(B * 1000)}$ mT, uniform inside and nearly zero outside.",
    ]
    return {"question": question, "steps": steps, "answer": f"$B = {fmt(B * 1000)}$ mT",
            "values": {"n": n, "I": I, "B": B}}


@template("faraday_induction", PHYS, "Electromagnetism", "Induction", "medium")
def faraday_induction(rng):
    N = nice(rng, 10, 1000, 10)
    A_cm2 = nice(rng, 10, 500, 10)
    B1 = nice(rng, 0.0, 1.0, 0.05)
    B2 = nice(rng, 0.0, 1.0, 0.05)
    if B1 == B2:
        B2 = round(B1 + 0.3, 2)
    dt = nice(rng, 0.01, 2.0, 0.01)
    Rcoil = nice(rng, 1, 50, 1)
    A = A_cm2 * 1e-4
    emf = N * A * abs(B2 - B1) / dt
    I = emf / Rcoil
    question = (
        f"A coil of {N} turns, each of area {q(A_cm2, 'cm²')}, is perpendicular to a magnetic field that changes uniformly "
        f"from {q(B1, 'T')} to {q(B2, 'T')} in {q(dt, 's')}. Find the average induced EMF and, if the coil's resistance is "
        f"{q(Rcoil, 'Ω')}, the induced current."
    )
    steps = [
        f"Change in flux per turn: $\\Delta\\Phi = A\\Delta B = ({fmt(A)})({fmt(B2 - B1)}) = {fmt(A * (B2 - B1))}$ Wb.",
        f"Faraday's law: $|\\mathcal{{E}}| = N\\frac{{|\\Delta\\Phi|}}{{\\Delta t}} = ({N})\\frac{{{fmt(abs(A * (B2 - B1)))}}}{{{fmt(dt)}}} = {fmt(emf)}$ V.",
        f"Current: $I = \\mathcal{{E}}/R = {fmt(I)}$ A; by Lenz's law it flows so as to oppose the change in flux.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\mathcal{{E}} = {fmt(emf)}$ V; $I = {fmt(I)}$ A",
        "values": {"N": N, "A": A, "B1": B1, "B2": B2, "dt": dt, "emf": emf, "I": I},
    }


@template("transformer", PHYS, "Electromagnetism", "Induction", "easy")
def transformer(rng):
    Vp = pick(rng, [120, 230, 400, 11000, 33000])
    Np = nice(rng, 100, 5000, 100)
    Ns = nice(rng, 10, 5000, 10)
    Pload = nice(rng, 10, 5000, 10)
    Vs = Vp * Ns / Np
    Is = Pload / Vs
    Ip = Pload / Vp
    kind = "step-up" if Ns > Np else "step-down"
    question = (
        f"An ideal transformer has {Np} turns on the primary and {Ns} turns on the secondary. The primary is connected to "
        f"{q(Vp, 'V')} AC and the secondary supplies {q(Pload, 'W')}. Find the secondary voltage and both currents."
    )
    steps = [
        f"$V_s = V_p\\frac{{N_s}}{{N_p}} = {Vp}\\times\\frac{{{Ns}}}{{{Np}}} = {fmt(Vs)}$ V — a {kind} transformer.",
        f"Ideal transformer: $P_p = P_s$. Secondary current $I_s = P/V_s = {fmt(Is)}$ A; primary current $I_p = P/V_p = {fmt(Ip)}$ A.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$V_s = {fmt(Vs)}$ V; $I_s = {fmt(Is)}$ A; $I_p = {fmt(Ip)}$ A",
        "values": {"Vp": Vp, "Np": Np, "Ns": Ns, "P": Pload, "Vs": Vs, "Is": Is, "Ip": Ip},
    }


@template("lc_resonance", PHYS, "Electromagnetism", "AC circuits", "medium")
def lc_resonance(rng):
    L_mH = nice(rng, 0.01, 100.0, 0.01)
    C_nF = nice(rng, 0.1, 1000.0, 0.1)
    L, Cap = L_mH * 1e-3, C_nF * 1e-9
    f0 = 1 / (2 * math.pi * math.sqrt(L * Cap))
    question = (
        f"What is the resonant frequency of a series LC (or RLC) circuit with $L = {fmt(L_mH)}$ mH and $C = {fmt(C_nF)}$ nF?"
    )
    steps = [
        "At resonance the inductive and capacitive reactances are equal: $\\omega L = 1/(\\omega C)$.",
        f"$f_0 = \\frac{{1}}{{2\\pi\\sqrt{{LC}}}} = \\frac{{1}}{{2\\pi\\sqrt{{({fmt(L)})({fmt(Cap)})}}}} = {fmt(f0)}$ Hz.",
    ]
    return {"question": question, "steps": steps, "answer": f"$f_0 = {fmt(f0)}$ Hz",
            "values": {"L": L, "C": Cap, "f0": f0}}


# ---------------------------------------------------------------------------
# Waves and optics
# ---------------------------------------------------------------------------


@template("string_harmonics", PHYS, "Waves and Optics", "Standing waves", "medium")
def string_harmonics(rng):
    L = nice(rng, 0.3, 1.5, 0.05)
    T = nice(rng, 20, 300, 5)
    mu = nice(rng, 0.5, 10.0, 0.5) * 1e-3
    v = math.sqrt(T / mu)
    f1 = v / (2 * L)
    question = (
        f"A string of length {q(L, 'm')} and linear mass density {q(mu * 1000, 'g/m')} is fixed at both ends under a tension "
        f"of {q(T, 'N')}. Find the wave speed, the fundamental frequency and the next two harmonics."
    )
    steps = [
        f"Wave speed: $v = \\sqrt{{T/\\mu}} = \\sqrt{{{fmt(T)}/{fmt(mu)}}} = {fmt(v)}$ m/s.",
        f"Fundamental (node at each end, $L = \\lambda/2$): $f_1 = \\frac{{v}}{{2L}} = {fmt(f1)}$ Hz.",
        f"Harmonics are integer multiples: $f_2 = {fmt(2 * f1)}$ Hz, $f_3 = {fmt(3 * f1)}$ Hz.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$v = {fmt(v)}$ m/s; $f_1 = {fmt(f1)}$ Hz; $f_2 = {fmt(2 * f1)}$ Hz; $f_3 = {fmt(3 * f1)}$ Hz",
        "values": {"L": L, "T": T, "mu": mu, "v": v, "f1": f1},
    }


@template("doppler_sound", PHYS, "Waves and Optics", "Doppler effect", "medium")
def doppler_sound(rng):
    f = nice(rng, 200, 1500, 10)
    vs = nice(rng, 5, 60, 1)
    vsound = 343
    f_app = f * vsound / (vsound - vs)
    f_rec = f * vsound / (vsound + vs)
    src = pick(rng, ["ambulance siren", "train horn", "police car siren", "racing car engine"])
    question = (
        f"An {src}" if src[0] in "aeiou" else f"A {src}"
    ) + (
        f" emits sound at {q(f, 'Hz')} while moving at {q(vs, 'm/s')} past a stationary listener. With the speed of sound "
        "343 m/s, what frequencies does the listener hear as the source approaches and as it recedes?"
    )
    steps = [
        "For a moving source and stationary observer: $f' = f\\frac{v}{v \\mp v_s}$ (minus while approaching).",
        f"Approaching: $f' = {fmt(f)}\\times\\frac{{343}}{{343 - {fmt(vs)}}} = {fmt(f_app)}$ Hz.",
        f"Receding: $f' = {fmt(f)}\\times\\frac{{343}}{{343 + {fmt(vs)}}} = {fmt(f_rec)}$ Hz.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"approaching {q(f_app, 'Hz')}; receding {q(f_rec, 'Hz')}",
        "values": {"f": f, "v_source": vs, "f_approach": f_app, "f_recede": f_rec},
    }


@template("sound_intensity_decibels", PHYS, "Waves and Optics", "Sound", "medium")
def sound_intensity_decibels(rng):
    P = nice(rng, 0.01, 10.0, 0.01)
    r = nice(rng, 1, 100, 1)
    I = P / (4 * math.pi * r * r)
    beta = 10 * math.log10(I / 1e-12)
    question = (
        f"A small loudspeaker radiates {q(P, 'W')} of sound power uniformly in all directions. What is the sound intensity "
        f"and the intensity level (in dB) at a distance of {q(r, 'm')}?"
    )
    steps = [
        f"Intensity spreads over a sphere: $I = \\frac{{P}}{{4\\pi r^2}} = \\frac{{{fmt(P)}}}{{4\\pi({fmt(r)})^2}} = {fmt(I)}$ W/m².",
        f"Intensity level: $\\beta = 10\\log_{{10}}(I/I_0)$ with $I_0 = 10^{{-12}}$ W/m²: $\\beta = {fmt(beta)}$ dB.",
        "Doubling the distance lowers the level by about 6 dB.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$I = {fmt(I)}$ W/m²; $\\beta = {fmt(beta)}$ dB",
        "values": {"P": P, "r": r, "I": I, "beta": beta},
    }


MEDIA = [("air", 1.000), ("water", 1.333), ("crown glass", 1.52), ("flint glass", 1.62), ("diamond", 2.42), ("ethanol", 1.36), ("acrylic", 1.49)]


@template("snell_refraction", PHYS, "Waves and Optics", "Refraction", "medium")
def snell_refraction(rng):
    (m1, n1), (m2, n2) = rng.sample(MEDIA, 2)
    th1 = nice(rng, 5, 80, 1)
    s2 = n1 * math.sin(math.radians(th1)) / n2
    steps = [f"Snell's law: $n_1\\sin\\theta_1 = n_2\\sin\\theta_2 \\Rightarrow \\sin\\theta_2 = \\frac{{{fmt(n1, 4)}\\sin {th1}°}}{{{fmt(n2, 4)}}} = {fmt(s2, 4)}$."]
    values = {"n1": n1, "n2": n2, "theta1": th1}
    if s2 > 1:
        crit = math.degrees(math.asin(n2 / n1))
        steps += [
            "Since $\\sin\\theta_2 > 1$, no refracted ray exists: **total internal reflection** occurs.",
            f"Critical angle: $\\sin\\theta_c = n_2/n_1 \\Rightarrow \\theta_c = {fmt(crit)}°$, which is smaller than {th1}°.",
        ]
        answer = f"total internal reflection (critical angle {fmt(crit)}°)"
        values["theta_c"] = crit
    else:
        th2 = math.degrees(math.asin(s2))
        bend = "toward" if n2 > n1 else "away from"
        steps.append(f"$\\theta_2 = {fmt(th2)}°$; the ray bends {bend} the normal.")
        if n1 > n2:
            crit = math.degrees(math.asin(n2 / n1))
            steps.append(f"(Total internal reflection would occur for incidence beyond $\\theta_c = {fmt(crit)}°$.)")
            values["theta_c"] = crit
        answer = f"$\\theta_2 = {fmt(th2)}°$"
        values["theta2"] = th2
    question = (
        f"A light ray passes from {m1} ($n = {fmt(n1, 4)}$) into {m2} ($n = {fmt(n2, 4)}$), striking the boundary at "
        f"${th1}°$ to the normal. Find the angle of refraction (or show that total internal reflection occurs)."
    )
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("thin_lens", PHYS, "Waves and Optics", "Lenses", "medium")
def thin_lens(rng):
    while True:
        f = nice(rng, -30, 40, 5)
        do = nice(rng, 5, 100, 5)
        if f != 0 and abs(do - f) > 1e-9:
            break
    di = 1 / (1 / f - 1 / do)
    m = -di / do
    kind = "converging" if f > 0 else "diverging"
    nature = ("real" if di > 0 else "virtual") + ", " + ("inverted" if m < 0 else "upright") + ", " + ("enlarged" if abs(m) > 1 else "reduced")
    question = (
        f"An object is placed {q(do, 'cm')} in front of a thin {kind} lens of focal length {q(f, 'cm')}. "
        "Find the image distance and magnification, and describe the image."
    )
    steps = [
        f"Thin-lens equation: $\\frac{{1}}{{d_i}} = \\frac1f - \\frac{{1}}{{d_o}} = \\frac{{1}}{{{fmt(f)}}} - \\frac{{1}}{{{fmt(do)}}}$.",
        f"$d_i = {fmt(di)}$ cm ({'opposite side — real image' if di > 0 else 'same side as the object — virtual image'}).",
        f"Magnification: $m = -d_i/d_o = {fmt(m)}$.",
        f"The image is {nature}.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$d_i = {fmt(di)}$ cm, $m = {fmt(m)}$ ({nature})",
        "values": {"f": f, "do": do, "di": di, "m": m},
    }


@template("double_slit", PHYS, "Waves and Optics", "Interference", "medium")
def double_slit(rng):
    lam_nm = pick(rng, [405, 450, 488, 532, 589, 633, 650, 694])
    d_mm = nice(rng, 0.05, 1.0, 0.05)
    L = nice(rng, 0.5, 5.0, 0.1)
    lam, d = lam_nm * 1e-9, d_mm * 1e-3
    dy = lam * L / d
    question = (
        f"Light of wavelength {q(lam_nm, 'nm')} passes through two narrow slits {q(d_mm, 'mm')} apart and forms an "
        f"interference pattern on a screen {q(L, 'm')} away. What is the spacing between adjacent bright fringes, and "
        "where is the third-order bright fringe?"
    )
    steps = [
        "Bright fringes satisfy $d\\sin\\theta = m\\lambda$; for small angles $y_m = m\\lambda L/d$.",
        f"Fringe spacing: $\\Delta y = \\frac{{\\lambda L}}{{d}} = \\frac{{({fmt(lam)})({fmt(L)})}}{{{fmt(d)}}} = {fmt(dy)}$ m $= {fmt(dy * 1000)}$ mm.",
        f"Third-order fringe: $y_3 = 3\\Delta y = {fmt(3 * dy * 1000)}$ mm from the central maximum.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\Delta y = {fmt(dy * 1000)}$ mm; $y_3 = {fmt(3 * dy * 1000)}$ mm",
        "values": {"lambda": lam, "d": d, "L": L, "dy": dy},
    }


@template("diffraction_grating", PHYS, "Waves and Optics", "Diffraction", "medium")
def diffraction_grating(rng):
    lines = pick(rng, [100, 300, 500, 600, 1000, 1200])
    lam_nm = pick(rng, [405, 436, 486, 532, 546, 589, 633, 656])
    d = 1e-3 / lines
    lam = lam_nm * 1e-9
    m_max = int(d / lam)
    th1 = math.degrees(math.asin(lam / d))
    question = (
        f"Light of wavelength {q(lam_nm, 'nm')} falls normally on a diffraction grating with {lines} lines per mm. "
        "Find the angle of the first-order maximum and the highest order that can be observed."
    )
    steps = [
        f"Line spacing: $d = 1/{lines}$ mm $= {fmt(d)}$ m.",
        f"First order: $\\sin\\theta_1 = \\lambda/d = {fmt(lam / d, 4)} \\Rightarrow \\theta_1 = {fmt(th1)}°$.",
        f"Highest order requires $\\sin\\theta \\le 1$: $m_{{max}} = \\lfloor d/\\lambda\\rfloor = \\lfloor {fmt(d / lam, 4)}\\rfloor = {m_max}$.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\theta_1 = {fmt(th1)}°$; highest order $m = {m_max}$",
        "values": {"lines_per_mm": lines, "lambda": lam, "theta1": th1, "m_max": m_max},
    }


# ---------------------------------------------------------------------------
# Modern physics
# ---------------------------------------------------------------------------


@template("photon_energy", PHYS, "Quantum Mechanics", "Photons", "easy")
def photon_energy(rng):
    lam_nm = pick(rng, [nice(rng, 100, 1500, 5), pick(rng, [121.6, 254, 365, 450, 532, 589, 633, 700, 1064, 1550])])
    lam = lam_nm * 1e-9
    E = H * C / lam
    EeV = E / EV
    f = C / lam
    region = "ultraviolet" if lam_nm < 380 else ("visible" if lam_nm <= 750 else "infrared")
    question = (
        f"Find the frequency of light with wavelength {q(lam_nm, 'nm', 4)} and the energy of one photon in joules and electron volts. "
        "In which region of the spectrum is it?"
    )
    steps = [
        f"$f = c/\\lambda = (2.998\\times10^8)/({fmt(lam)}) = {fmt(f)}$ Hz.",
        f"$E = hf = hc/\\lambda = {fmt(E)}$ J.",
        f"In eV: $E = {fmt(E)}/(1.602\\times10^{{-19}}) = {fmt(EeV)}$ eV (shortcut: $1240/\\lambda_{{nm}} = {fmt(HC_EV_NM / lam_nm)}$ eV).",
        f"This wavelength lies in the {region}.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$f = {fmt(f)}$ Hz; $E = {fmt(E)}$ J $= {fmt(EeV)}$ eV ({region})",
        "values": {"lambda_nm": lam_nm, "f": f, "E_J": E, "E_eV": EeV},
    }


WORK_FUNCTIONS = [("cesium", 2.1), ("potassium", 2.3), ("sodium", 2.3), ("calcium", 2.9), ("zinc", 4.3), ("copper", 4.7), ("silver", 4.7), ("platinum", 5.6)]


@template("photoelectric_effect", PHYS, "Quantum Mechanics", "Photoelectric effect", "medium")
def photoelectric_effect(rng):
    metal, phi = pick(rng, WORK_FUNCTIONS)
    lam_nm = nice(rng, 150, 700, 5)
    E = HC_EV_NM / lam_nm
    lam0 = HC_EV_NM / phi
    question = (
        f"Light of wavelength {q(lam_nm, 'nm')} shines on a clean {metal} surface (work function {q(phi, 'eV')}). "
        "Are electrons emitted? If so, find their maximum kinetic energy, the stopping potential and their maximum speed."
    )
    steps = [
        f"Photon energy: $E = hc/\\lambda = 1240/{fmt(lam_nm)} = {fmt(E)}$ eV.",
        f"Threshold wavelength: $\\lambda_0 = 1240/\\phi = {fmt(lam0)}$ nm.",
    ]
    values = {"phi": phi, "lambda_nm": lam_nm, "E_photon_eV": E}
    if E <= phi:
        steps.append(f"Since $E < \\phi$ (equivalently $\\lambda > \\lambda_0$), **no electrons are emitted**, however intense the light.")
        answer = "no photoelectrons are emitted (photon energy below the work function)"
        values["K_max_eV"] = 0.0
    else:
        K = E - phi
        v = math.sqrt(2 * K * EV / M_E)
        steps += [
            f"Einstein's equation: $K_{{max}} = hf - \\phi = {fmt(E)} - {fmt(phi)} = {fmt(K)}$ eV.",
            f"Stopping potential: $V_s = K_{{max}}/e = {fmt(K)}$ V.",
            f"Maximum speed: $v = \\sqrt{{2K/m_e}} = {fmt(v)}$ m/s.",
        ]
        answer = f"yes; $K_{{max}} = {fmt(K)}$ eV, $V_s = {fmt(K)}$ V, $v_{{max}} = {fmt(v)}$ m/s"
        values.update({"K_max_eV": K, "v_max": v})
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("de_broglie_wavelength", PHYS, "Quantum Mechanics", "Matter waves", "medium")
def de_broglie_wavelength(rng):
    if rng.random() < 0.6:
        V = nice(rng, 10, 50000, 10)
        p = math.sqrt(2 * M_E * E_CHARGE * V)
        lam = H / p
        question = (
            f"An electron is accelerated from rest through a potential difference of {q(V, 'V')}. Find its de Broglie wavelength "
            "(non-relativistic treatment)."
        )
        steps = [
            f"Kinetic energy: $K = eV = {fmt(V)}$ eV $= {fmt(E_CHARGE * V)}$ J.",
            f"Momentum: $p = \\sqrt{{2m_eK}} = {fmt(p)}$ kg·m/s.",
            f"$\\lambda = h/p = {fmt(lam)}$ m $= {fmt(lam * 1e9)}$ nm (shortcut $\\lambda \\approx 1.226/\\sqrt{{V}}$ nm).",
        ]
        return {"question": question, "steps": steps, "answer": f"$\\lambda = {fmt(lam * 1e9)}$ nm",
                "values": {"V": V, "lambda": lam}}
    obj, m, v = pick(rng, [("baseball", 0.145, 40.0), ("tennis ball", 0.057, 50.0), ("person walking", 70.0, 1.4),
                            ("car", 1200.0, 25.0), ("dust grain", 1e-9, 0.01), ("bullet", 0.01, 900.0)])
    lam = H / (m * v)
    question = f"Calculate the de Broglie wavelength of a {obj} of mass {q(m, 'kg')} moving at {q(v, 'm/s')}. Why don't we observe its wave nature?"
    steps = [
        f"$\\lambda = \\frac{{h}}{{mv}} = \\frac{{6.626\\times10^{{-34}}}}{{({fmt(m)})({fmt(v)})}} = {fmt(lam)}$ m.",
        "This is vastly smaller than any slit or atomic nucleus (~$10^{-15}$ m), so diffraction and interference are utterly undetectable for everyday objects.",
    ]
    return {"question": question, "steps": steps, "answer": f"$\\lambda = {fmt(lam)}$ m",
            "values": {"m": m, "v": v, "lambda": lam}}


@template("hydrogen_transition", PHYS, "Quantum Mechanics", "Atomic spectra", "medium")
def hydrogen_transition(rng):
    nf = pick(rng, [1, 2, 2, 3, 4])
    ni = nf + rng.randint(1, 5)
    dE = 13.6 * (1 / nf ** 2 - 1 / ni ** 2)
    lam = HC_EV_NM / dE
    series = {1: "Lyman", 2: "Balmer", 3: "Paschen", 4: "Brackett"}[nf]
    region = "ultraviolet" if lam < 380 else ("visible" if lam <= 750 else "infrared")
    question = (
        f"An electron in a hydrogen atom drops from the $n = {ni}$ level to the $n = {nf}$ level. Find the energy and wavelength of "
        "the emitted photon and name the spectral series."
    )
    steps = [
        "Bohr energy levels: $E_n = -13.6\\text{ eV}/n^2$.",
        f"$E_{ni} = {fmt(-13.6 / ni ** 2)}$ eV; $E_{nf} = {fmt(-13.6 / nf ** 2)}$ eV.",
        f"Photon energy: $\\Delta E = 13.6\\left(\\frac{{1}}{{{nf}^2}} - \\frac{{1}}{{{ni}^2}}\\right) = {fmt(dE)}$ eV.",
        f"Wavelength: $\\lambda = hc/\\Delta E = 1240/{fmt(dE)} = {fmt(lam)}$ nm ({region}).",
        f"Transitions ending on $n = {nf}$ belong to the {series} series.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$\\Delta E = {fmt(dE)}$ eV; $\\lambda = {fmt(lam)}$ nm ({series} series, {region})",
        "values": {"n_initial": ni, "n_final": nf, "dE_eV": dE, "lambda_nm": lam},
    }


@template("particle_in_a_box", PHYS, "Quantum Mechanics", "Particle in a box", "hard")
def particle_in_a_box(rng):
    L_nm = nice(rng, 0.1, 10.0, 0.1)
    n = rng.randint(1, 4)
    L = L_nm * 1e-9
    E1 = H ** 2 / (8 * M_E * L ** 2)
    En = n ** 2 * E1
    dE = ((n + 1) ** 2 - n ** 2) * E1
    lam = H * C / dE
    question = (
        f"An electron is confined in a one-dimensional infinite square well of width {q(L_nm, 'nm')}. Find the energy of the "
        f"$n = {n}$ level (in eV) and the wavelength of the photon emitted in the transition from $n = {n + 1}$ to $n = {n}$."
    )
    steps = [
        "Energy levels: $E_n = \\frac{n^2h^2}{8mL^2}$.",
        f"Ground state: $E_1 = \\frac{{(6.626\\times10^{{-34}})^2}}{{8(9.109\\times10^{{-31}})({fmt(L)})^2}} = {fmt(E1)}$ J $= {fmt(E1 / EV)}$ eV.",
        f"$E_{n} = {n}^2E_1 = {fmt(En / EV)}$ eV.",
        f"Transition energy: $\\Delta E = ({n + 1}^2 - {n}^2)E_1 = {fmt(dE / EV)}$ eV; $\\lambda = hc/\\Delta E = {fmt(lam * 1e9)}$ nm.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"$E_{n} = {fmt(En / EV)}$ eV; $\\lambda = {fmt(lam * 1e9)}$ nm",
        "values": {"L": L, "n": n, "E1_eV": E1 / EV, "En_eV": En / EV, "lambda": lam},
    }


@template("heisenberg_uncertainty", PHYS, "Quantum Mechanics", "Uncertainty principle", "medium")
def heisenberg_uncertainty(rng):
    name, m = pick(rng, [("electron", M_E), ("proton", M_P), ("electron", M_E)])
    dx_nm = sig(10 ** rng.uniform(-2, 2), 2)
    dx = dx_nm * 1e-9
    dp = HBAR / (2 * dx)
    dv = dp / m
    question = (
        f"An {name}" if name[0] in "aeiou" else f"A {name}"
    ) + f" is localized to within $\\Delta x = {fmt(dx_nm)}$ nm. What are the minimum uncertainties in its momentum and velocity?"
    steps = [
        "Heisenberg: $\\Delta x\\,\\Delta p \\ge \\hbar/2$.",
        f"$\\Delta p_{{min}} = \\frac{{\\hbar}}{{2\\Delta x}} = \\frac{{1.055\\times10^{{-34}}}}{{2({fmt(dx)})}} = {fmt(dp)}$ kg·m/s.",
        f"$\\Delta v = \\Delta p/m = {fmt(dv)}$ m/s.",
    ]
    return {"question": question, "steps": steps, "answer": f"$\\Delta p \\ge {fmt(dp)}$ kg·m/s; $\\Delta v \\ge {fmt(dv)}$ m/s",
            "values": {"m": m, "dx": dx, "dp": dp, "dv": dv}}


@template("tunneling_probability", PHYS, "Quantum Mechanics", "Tunneling", "hard")
def tunneling_probability(rng):
    while True:
        E = nice(rng, 0.5, 8.0, 0.5)
        V0 = nice(rng, 1.0, 12.0, 0.5)
        L_nm = nice(rng, 0.1, 1.5, 0.1)
        if V0 > E + 0.4:
            break
    kappa = math.sqrt(2 * M_E * (V0 - E) * EV) / HBAR
    x = 2 * kappa * L_nm * 1e-9
    T = 16 * (E / V0) * (1 - E / V0) * math.exp(-x)
    question = (
        f"An electron with energy {q(E, 'eV')} approaches a rectangular potential barrier of height {q(V0, 'eV')} and width "
        f"{q(L_nm, 'nm')}. Estimate the probability that it tunnels through."
    )
    steps = [
        f"Decay constant: $\\kappa = \\frac{{\\sqrt{{2m(V_0 - E)}}}}{{\\hbar}} = {fmt(kappa)}$ m⁻¹.",
        f"$2\\kappa L = {fmt(x)}$.",
        f"Thick-barrier approximation: $T \\approx 16\\frac{{E}}{{V_0}}\\left(1 - \\frac{{E}}{{V_0}}\\right)e^{{-2\\kappa L}} = {fmt(T)}$.",
        "Classically the transmission would be exactly zero. The exponential makes tunneling extremely sensitive to the barrier width (the principle of the scanning tunneling microscope)."
        + (" (Here $2\\kappa L$ is not large, so the approximation is rough.)" if x < 2 else ""),
    ]
    return {"question": question, "steps": steps, "answer": f"$T \\approx {fmt(T)}$",
            "values": {"E_eV": E, "V0_eV": V0, "L_nm": L_nm, "kappa": kappa, "T": T}}


ISOTOPES = [
    ("carbon-14", 5730, "years"), ("iodine-131", 8.02, "days"), ("cobalt-60", 5.27, "years"), ("cesium-137", 30.2, "years"),
    ("radon-222", 3.82, "days"), ("technetium-99m", 6.01, "hours"), ("strontium-90", 28.8, "years"),
    ("phosphorus-32", 14.3, "days"), ("tritium (hydrogen-3)", 12.3, "years"), ("fluorine-18", 110, "minutes"),
    ("plutonium-239", 24100, "years"), ("uranium-238", 4.47e9, "years"),
]


@template("radioactive_decay", PHYS, "Nuclear Physics", "Radioactive decay", "medium")
def radioactive_decay(rng):
    iso, th, unit = pick(rng, ISOTOPES)
    t = sig(th * nice(rng, 0.25, 6.0, 0.25), 4)
    mult = t / th
    m0 = nice(rng, 1, 500, 1)
    frac = 0.5 ** (t / th)
    lam = math.log(2) / th
    question = (
        f"The half-life of {iso} is {q(th, unit, 4)}. Starting with {q(m0, 'mg')}, how much remains after {q(t, unit, 4)}? "
        "What fraction has decayed, and what is the decay constant?"
    )
    steps = [
        f"Number of half-lives: $t/t_{{1/2}} = {fmt(t, 4)}/{fmt(th, 4)} = {fmt(mult)}$.",
        f"Fraction remaining: $(1/2)^{{{fmt(mult)}}} = {fmt(frac)}$, so $m = {fmt(m0)}\\times{fmt(frac)} = {fmt(m0 * frac)}$ mg.",
        f"Fraction decayed: $1 - {fmt(frac)} = {fmt(1 - frac)}$ ({fmt(100 * (1 - frac))}%).",
        f"Decay constant: $\\lambda = \\ln 2/t_{{1/2}} = {fmt(lam)}$ per {unit[:-1] if unit.endswith('s') else unit}.",
    ]
    return {
        "question": question,
        "steps": steps,
        "answer": f"{q(m0 * frac, 'mg')} remains ({fmt(100 * (1 - frac))}% decayed); $\\lambda = {fmt(lam)}$ per {unit[:-1] if unit.endswith('s') else unit}",
        "values": {"half_life": th, "t": t, "m0": m0, "fraction_remaining": frac, "lambda": lam},
    }


@template("radiocarbon_dating", PHYS, "Nuclear Physics", "Radiometric dating", "medium")
def radiocarbon_dating(rng):
    pct = nice(rng, 2, 95, 1)
    t = 5730 / math.log(2) * math.log(100 / pct)
    sample = pick(rng, ["a wooden tool", "charcoal from an ancient hearth", "a bone fragment", "a linen cloth", "a seed"])
    question = (
        f"The carbon-14 activity of {sample} is {pct}% of that of living material. Given a half-life of 5730 years, how old is the sample?"
    )
    steps = [
        "Decay law: $N/N_0 = e^{-\\lambda t}$ with $\\lambda = \\ln2/5730$ yr⁻¹.",
        f"$t = \\frac{{5730}}{{\\ln2}}\\ln\\frac{{N_0}}{{N}} = \\frac{{5730}}{{0.693}}\\ln\\frac{{100}}{{{pct}}} = {fmt(t)}$ years.",
        f"Check: that is ${fmt(t / 5730)}$ half-lives, and $(1/2)^{{{fmt(t / 5730)}}} = {fmt(0.5 ** (t / 5730))}$. ✓",
    ]
    return {"question": question, "steps": steps, "answer": f"about {q(t, 'years')}",
            "values": {"percent_remaining": pct, "age": t}}


@template("time_dilation", PHYS, "Relativity", "Special relativity", "medium")
def time_dilation(rng):
    beta = pick(rng, [0.1, 0.3, 0.5, 0.6, 0.8, 0.866, 0.9, 0.95, 0.99, 0.995, 0.999])
    t0 = nice(rng, 1, 50, 1)
    gamma = 1 / math.sqrt(1 - beta ** 2)
    t = gamma * t0
    Lc = 1 / gamma
    question = (
        f"A spaceship travels at ${fmt(beta, 4)}c$ relative to Earth. A clock on board records {q(t0, 'years')} for a journey. "
        "How much time passes on Earth? By what factor are lengths along the motion contracted for Earth observers?"
    )
    steps = [
        f"Lorentz factor: $\\gamma = \\frac{{1}}{{\\sqrt{{1 - v^2/c^2}}}} = \\frac{{1}}{{\\sqrt{{1 - {fmt(beta, 4)}^2}}}} = {fmt(gamma, 4)}$.",
        f"The ship's clock measures proper time: $\\Delta t = \\gamma\\Delta t_0 = {fmt(gamma, 4)}\\times{fmt(t0)} = {fmt(t)}$ years on Earth.",
        f"Length contraction: $L = L_0/\\gamma$, a factor of ${fmt(Lc, 4)}$.",
    ]
    return {"question": question, "steps": steps, "answer": f"$\\gamma = {fmt(gamma, 4)}$; Earth time {q(t, 'years')}; lengths × {fmt(Lc, 4)}",
            "values": {"beta": beta, "t0": t0, "gamma": gamma, "t": t}}


@template("relativistic_energy", PHYS, "Relativity", "Relativistic energy", "hard")
def relativistic_energy(rng):
    name, mc2 = pick(rng, [("electron", 0.511), ("proton", 938.3), ("muon", 105.7)])
    beta = pick(rng, [0.5, 0.6, 0.8, 0.9, 0.95, 0.99, 0.999]) if rng.random() < 0.4 else nice(rng, 0.10, 0.98, 0.01)
    gamma = 1 / math.sqrt(1 - beta ** 2)
    E = gamma * mc2
    K = E - mc2
    pc = math.sqrt(E ** 2 - mc2 ** 2)
    Kc = 0.5 * mc2 * beta ** 2
    question = (
        f"A {name} (rest energy {q(mc2, 'MeV', 4)}) moves at ${fmt(beta, 3)}c$. Find its Lorentz factor, total energy, kinetic energy "
        "and momentum. Compare with the classical kinetic energy."
    )
    steps = [
        f"$\\gamma = 1/\\sqrt{{1 - \\beta^2}} = {fmt(gamma, 4)}$.",
        f"Total energy: $E = \\gamma mc^2 = {fmt(E, 4)}$ MeV.",
        f"Kinetic energy: $K = (\\gamma - 1)mc^2 = {fmt(K, 4)}$ MeV.",
        f"Momentum: $pc = \\sqrt{{E^2 - (mc^2)^2}} = {fmt(pc, 4)}$ MeV, so $p = {fmt(pc, 4)}$ MeV/c.",
        f"Classical $\\tfrac12mv^2 = {fmt(Kc, 4)}$ MeV — it underestimates $K$ at relativistic speeds.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$\\gamma = {fmt(gamma, 4)}$, $E = {fmt(E, 4)}$ MeV, $K = {fmt(K, 4)}$ MeV, $p = {fmt(pc, 4)}$ MeV/c",
            "values": {"mc2": mc2, "beta": beta, "gamma": gamma, "E": E, "K": K, "pc": pc}}


NUCLEI = [  # name, Z, N, atomic mass (u)
    ("helium-4", 2, 2, 4.002602), ("carbon-12", 6, 6, 12.000000), ("oxygen-16", 8, 8, 15.994915),
    ("iron-56", 26, 30, 55.934936), ("lithium-7", 3, 4, 7.016003), ("uranium-238", 92, 146, 238.050788),
    ("deuterium (hydrogen-2)", 1, 1, 2.014102), ("nitrogen-14", 7, 7, 14.003074),
]


@template("nuclear_binding_energy", PHYS, "Nuclear Physics", "Binding energy", "hard")
def nuclear_binding_energy(rng):
    name, Z, N, M = pick(rng, NUCLEI)
    mH, mn = 1.007825, 1.008665
    dm = Z * mH + N * mn - M
    BE = dm * 931.494
    A = Z + N
    question = (
        f"The atomic mass of {name} is {q(M, 'u', 7)}. Using $m(^1\\text{{H}}) = 1.007825$ u and $m_n = 1.008665$ u, find the "
        "mass defect, the total binding energy and the binding energy per nucleon."
    )
    steps = [
        f"{name[0].upper() + name[1:]} has $Z = {Z}$ protons and $N = {N}$ neutrons ($A = {A}$).",
        f"Mass of separated constituents: ${Z}(1.007825) + {N}(1.008665) = {fmt(Z * mH + N * mn, 7)}$ u.",
        f"Mass defect: $\\Delta m = {fmt(Z * mH + N * mn, 7)} - {fmt(M, 7)} = {fmt(dm, 4)}$ u.",
        f"Binding energy: $B = \\Delta m\\times931.494$ MeV/u $= {fmt(BE, 4)}$ MeV.",
        f"Per nucleon: $B/A = {fmt(BE / A, 4)}$ MeV.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$\\Delta m = {fmt(dm, 4)}$ u, $B = {fmt(BE, 4)}$ MeV, $B/A = {fmt(BE / A, 4)}$ MeV",
            "values": {"Z": Z, "N": N, "M": M, "mass_defect": dm, "BE_MeV": BE, "BE_per_nucleon": BE / A}}


@template("stefan_wien_radiation", PHYS, "Thermodynamics", "Blackbody radiation", "medium")
def stefan_wien_radiation(rng):
    obj, T, A, e = pick(rng, [
        ("a human body", 307.0, 1.8, 0.97), ("a hot stove element", 900.0, 0.03, 0.9),
        ("an incandescent filament", 2800.0, 5e-5, 0.35), ("a red-hot iron bar", 1200.0, 0.01, 0.7),
        ("a brick wall in sunlight", 320.0, 10.0, 0.93),
    ])
    T = sig(T * rng.uniform(0.92, 1.08), 3) if T > 400 else T + rng.randint(-4, 4)
    A = sig(A * rng.uniform(0.7, 1.4), 2)
    lam = WIEN_B / T
    P = e * SIGMA_SB * A * T ** 4
    question = (
        f"Estimate the peak wavelength of thermal radiation from {obj} at {q(T, 'K', 4)}, and the total power it radiates "
        f"(area {q(A, 'm²')}, emissivity {fmt(e, 2)})."
    )
    steps = [
        f"Wien's law: $\\lambda_{{max}} = \\frac{{2.898\\times10^{{-3}}}}{{T}} = {fmt(lam)}$ m $= {fmt(lam * 1e6)}$ μm.",
        f"Stefan–Boltzmann: $P = e\\sigma AT^4 = ({fmt(e, 2)})(5.67\\times10^{{-8}})({fmt(A)})({fmt(T, 4)})^4 = {fmt(P)}$ W.",
        "(The net power exchanged with surroundings at $T_s$ would be $e\\sigma A(T^4 - T_s^4)$.)",
    ]
    return {"question": question, "steps": steps, "answer": f"$\\lambda_{{max}} = {fmt(lam * 1e6)}$ μm; $P = {fmt(P)}$ W",
            "values": {"T": T, "A": A, "e": e, "lambda_max": lam, "P": P}}
