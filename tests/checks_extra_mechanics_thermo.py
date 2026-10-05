"""Independent re-computation for scripts/problem_generators/extra_mechanics_thermo.py.

Each entry maps a template name to ``function(values) -> [(recomputed, stored), ...]``. The formulas
and constants are written out here, independently of the generator module.
"""

import math

GRAV = 9.81                # m/s^2
GM_EARTH = 3.986e14        # m^3/s^2
RADIUS_EARTH = 6.371e6     # m
GAS_R = 8.314              # J/(mol K)
CW = 4186.0                # J/(kg K), liquid water
AIR_RHO = 1.20             # kg/m^3
LV_SKIN = 2.42e6           # J/kg
CBODY = 3500.0             # J/(kg K)
ZERO_C = 273.15


def _rad(deg):
    return deg * math.pi / 180


def _deg(rad):
    return rad * 180 / math.pi


def banked(v):
    if v["mode"] == "find_angle":
        speed = v["v_kmh"] * 1000 / 3600
        theta = _deg(math.atan2(speed ** 2, v["r"] * GRAV))
        return [(speed, v["v"]), (theta, v["theta_deg"]),
                (v["m"] * GRAV / math.cos(_rad(theta)), v["N"]),
                (float(v["theta_deg"] < 60), 1.0)]
    speed = (v["r"] * GRAV * math.tan(_rad(v["theta_deg"]))) ** 0.5
    return [(speed, v["v"]), (speed * 3600 / 1000, v["v_kmh"]),
            (v["m"] * GRAV / math.cos(_rad(v["theta_deg"])), v["N"])]


def conical(v):
    L, m = v["L"], v["m"]
    if v["mode"] == "angle_given":
        th = _rad(v["theta_deg"])
        radius = L * math.sin(th)
        # horizontal: T sin = m v^2 / r, vertical: T cos = m g
        tension = m * GRAV / math.cos(th)
        speed = (tension * math.sin(th) * radius / m) ** 0.5
        period = 2 * math.pi * radius / speed
        return [(tension, v["T"]), (radius, v["r"]), (speed, v["v"]), (period, v["P"])]
    omega = v["n_rpm"] * 2 * math.pi / 60
    th = math.acos(GRAV / (omega ** 2 * L))
    radius = L * math.sin(th)
    return [(_deg(th), v["theta_deg"]), (m * omega ** 2 * L, v["T"]), (radius, v["r"]), (omega * radius, v["v"]),
            (float(omega ** 2 * L > GRAV), 1.0)]


def vertical_circle(v):
    m, r = v["m"], v["r"]
    if v["mode"] == "top_given":
        vt = v["v_top"]
        vb = (vt ** 2 + 2 * GRAV * (2 * r)) ** 0.5
        out = [(vb, v["v_bottom"])]
    else:
        vb = v["v_bottom"]
        vt = (vb ** 2 - 2 * GRAV * (2 * r)) ** 0.5
        out = [(vt, v["v_top"])]
    t_top = m * vt ** 2 / r - m * GRAV
    t_bot = m * vb ** 2 / r + m * GRAV
    return out + [(t_top, v["T_top"]), (t_bot, v["T_bottom"]), (v["T_bottom"] - v["T_top"], 6 * m * GRAV),
                  (float(t_top > 0), 1.0)]


def loop(v):
    R, h, m = v["R"], v["h"], v["m"]
    k = 1.0 if v["motion"] == "slide" else 1.0 + 2.0 / 5.0   # KE = k * (1/2) m v^2
    # top: m g = m v^2 / R and m g h = m g 2R + k/2 m v^2
    h_min = 2 * R + k * R / 2
    vt2 = (GRAV * h - 2 * GRAV * R) * 2 / k
    vb2 = GRAV * h * 2 / k
    mass_ok = v["m_disp"] in (m, round(m * 1000, 6))
    return [(h_min, v["h_min"]), (vt2 ** 0.5, v["v_top"]), (vb2 ** 0.5, v["v_bottom"]),
            (m * (vt2 / R - GRAV), v["N_top"]), (m * (vb2 / R + GRAV), v["N_bottom"]),
            (float(h > h_min and mass_ok), 1.0)]


def center_of_mass(v):
    if v["mode"] == "barycenter":
        d = v["D"] / (1 + v["M_A"] / v["M_B"])
        return [(d, v["d"]), (float(d < v["R_A"]), float(v["inside"]))]
    ms, xs, ys = v["masses"], v["xs"], v["ys"]
    total = math.fsum(ms)
    xc = math.fsum(a * b for a, b in zip(ms, xs)) / total
    yc = math.fsum(a * b for a, b in zip(ms, ys)) / total
    return [(total, v["M"]), (xc, v["x_cm"]), (yc, v["y_cm"]), (math.sqrt(xc * xc + yc * yc), v["dist"])]


def physical_pendulum(v):
    mode = v["mode"]
    if mode == "rod":
        M, L, d = v["M"], v["L"], v["d"]
        inertia = M * (L ** 2 / 12 + d ** 2)
        mass, arm = M, d
    elif mode == "disk":
        M, R, d = v["M"], v["R"], v["d"]
        inertia = M * (R ** 2 / 2 + d ** 2)
        mass, arm = M, d
    else:
        M, mb, L = v["M"], v["m"], v["L"]
        inertia = M * L ** 2 / 12 + M * (L / 2) ** 2 + mb * L ** 2
        mass = M + mb
        arm = (M * L / 2 + mb * L) / mass
    period = 2 * math.pi * math.sqrt(inertia / (mass * GRAV * arm))
    out = [(inertia, v["I"]), (period, v["T"]), (inertia / (mass * arm), v["L_eq"])]
    if mode == "rod_bob":
        out += [(arm, v["d_cm"]), (2 * math.pi * math.sqrt(v["L"] / GRAV), v["T0"]), (float(period < v["T0"]), 1.0)]
    return out


def damped(v):
    m, k = v["m"], v["k"]
    w0 = math.sqrt(k / m)
    if v["mode"] == "forward":
        b = v["b"]
        gam = b / (2 * m)
        return [(w0, v["omega0"]), (gam, v["gamma"]), (math.sqrt(w0 ** 2 - gam ** 2), v["omega_d"]),
                (m * w0 / b, v["Q"]), (v["A0_cm"] * math.exp(-gam * v["t"]), v["A_cm"]),
                (math.log(2) * 2 * m / b, v["t_half"])]
    gam = (math.log(v["A0_cm"]) - math.log(v["A1_cm"])) / v["t"]
    b = 2 * m * gam
    Td = 2 * math.pi / math.sqrt(w0 ** 2 - gam ** 2)
    return [(gam, v["gamma"]), (b, v["b"]), (m * w0 / b, v["Q"]), (Td, v["T_d"]),
            (1 - math.exp(-b * Td / m), v["loss_per_cycle"])]


def driven(v):
    m, k, b, F0 = v["m"], v["k"], v["b"], v["F0"]
    w = 2 * math.pi * v["f_drive"]
    # complex amplitude X = F0 / (k - m w^2 + i b w)
    z = complex(k - m * w * w, b * w)
    amp = F0 / abs(z)
    phase = _deg(math.atan2(b * w, k - m * w * w))
    w0 = math.sqrt(k / m)
    return [(w0, v["omega0"]), (amp, v["A"]), (phase, v["delta_deg"]), (F0 / (b * w0), v["A_res"]),
            (math.sqrt(k * m) / b, v["Q"])]


def hohmann(v):
    r1 = RADIUS_EARTH + 1000 * v["h1_km"]
    r2 = RADIUS_EARTH + 1000 * v["h2_km"]
    a = 0.5 * (r1 + r2)
    v1, v2 = math.sqrt(GM_EARTH / r1), math.sqrt(GM_EARTH / r2)
    # perigee/apogee speeds from energy and angular-momentum conservation
    vp = math.sqrt(2 * GM_EARTH * r2 / (r1 * (r1 + r2)))
    va = vp * r1 / r2
    dv = (vp - v1) + (v2 - va)
    period = 2 * math.pi * math.sqrt(a ** 3 / GM_EARTH)
    out = [(r1, v["r1"]), (r2, v["r2"]), (v1, v["v1"]), (v2, v["v2"]), (vp, v["v_p"]), (va, v["v_a"]),
           (vp - v1, v["dv1"]), (v2 - va, v["dv2"]), (dv, v["dv_total"]), (period / 2, v["t_transfer"])]
    if "m0" in v:
        out.append((v["m0"] * (1 - math.exp(-dv / (1000 * v["ve_kms"]))), v["m_prop"]))
    return out


def orbital_energy(v):
    m = v["m"]
    if v["mode"] == "launch":
        r = RADIUS_EARTH + 1000 * v["h_km"]
        speed = math.sqrt(GM_EARTH / r)
        ke = 0.5 * m * speed ** 2
        pe = -GM_EARTH * m / r
        return [(speed, v["v"]), (ke, v["KE"]), (pe, v["U"]), (ke + pe, v["E"]),
                (ke + pe + GM_EARTH * m / RADIUS_EARTH, v["E_needed"])]
    r1 = RADIUS_EARTH + 1000 * v["h1_km"]
    r2 = RADIUS_EARTH + 1000 * v["h2_km"]
    e1, e2 = -GM_EARTH * m / (2 * r1), -GM_EARTH * m / (2 * r2)
    k1, k2 = GM_EARTH * m / (2 * r1), GM_EARTH * m / (2 * r2)
    return [(e2 - e1, v["dE"]), (k2 - k1, v["dK"]), (GM_EARTH * m / r1 - GM_EARTH * m / r2, v["dU"])]


def stokes(v):
    rs, rf, r = v["rho_s"], v["rho_f"], v["r"]
    weight_minus_buoyancy = 4 / 3 * math.pi * r ** 3 * (rs - rf) * GRAV
    if v["mode"] == "terminal":
        eta = v["eta"]
        vt = weight_minus_buoyancy / (6 * math.pi * eta * r)
        return [(vt, v["v_t"]), (rf * vt * 2 * r / eta, v["Re"]), (v["H"] / vt, v["t_fall"]),
                (2 * r * r * rs / (9 * eta), v["tau"]), (float(rf * vt * 2 * r / eta < 1), 1.0)]
    vt = v["D_cm"] / 100 / v["t"]
    eta = weight_minus_buoyancy / (6 * math.pi * r * vt)
    return [(v["r_mm"] / 1000, r), (vt, v["v_t"]), (eta, v["eta"]), (rf * vt * 2 * r / eta, v["Re"])]


def torricelli(v):
    speed = math.sqrt(2 * GRAV * v["h"])
    d = v["d_mm"] / 1000
    flow = math.pi * (d / 2) ** 2 * speed
    rng_x = speed * math.sqrt(2 * v["y"] / GRAV)
    out = [(speed, v["v"]), (flow, v["Q"]), (rng_x, v["x"]), (rng_x, 2 * math.sqrt(v["h"] * v["y"])),
           (float(rng_x <= v["h"] + v["y"] + 1e-12), 1.0)]
    if "t_drain" in v:
        out.append(((v["D_tank"] / d) ** 2 * math.sqrt(2 * v["h"] / GRAV), v["t_drain"]))
    return out


def poiseuille(v):
    r, L, dP, eta = v["r"], v["L"], v["dP"], v["eta"]
    flow = math.pi * dP * r ** 4 / (8 * eta * L)
    vbar = flow / (math.pi * r ** 2)
    reynolds = v["rho"] * vbar * 2 * r / eta
    r_new = r * (1 - v["reduction_pct"] / 100)
    flow2 = math.pi * dP * r_new ** 4 / (8 * eta * L)
    return [(flow, v["Q"]), (vbar, v["v_mean"]), (reynolds, v["Re"]), (flow2, v["Q_reduced"]),
            (float(reynolds < 2000), 1.0)]


def ballistic(v):
    m, M = v["m_g"] / 1000, v["M"]
    if v["mode"] == "find_speed":
        V = math.sqrt(2 * GRAV * v["h_cm"] / 100)
        return [(V, v["V"]), (V * (m + M) / m, v["v"]), (1 - m / (m + M), v["frac_lost"])]
    V = m * v["v"] / (m + M)
    h = V * V / (2 * GRAV)
    return [(V, v["V"]), (h, v["h"]), (_deg(math.acos(1 - h / v["L"])), v["theta_deg"])]


def recoil(v):
    mode = v["mode"]
    if mode == "rifle":
        m = v["m_g"] / 1000
        V = m * v["v"] / v["M"]
        kg = 0.5 * v["M"] * V ** 2
        return [(V, v["V"]), (0.5 * m * v["v"] ** 2, v["K_bullet"]), (kg, v["K_gun"]), (kg / (v["d_cm"] / 100), v["F"])]
    if mode == "cannon":
        V = v["m"] * v["v"] * math.cos(_rad(v["theta_deg"])) / v["M"]
        kg = 0.5 * v["M"] * V ** 2
        return [(V, v["V"]), (kg, v["K_gun"]), (kg / v["d"], v["F"])]
    V = v["m"] * v["v"] / v["M"]
    return [(V, v["V"]), (v["D"] / V, v["t"])]


def road_load(v):
    speed = v["v_kmh"] / 3.6
    slope = math.atan(v["grade_pct"] / 100)
    weight = v["m"] * GRAV
    fd = AIR_RHO * v["Cd"] * v["A"] * speed ** 2 / 2
    fr = v["Crr"] * weight * math.cos(slope)
    fg = weight * math.sin(slope)
    total = fd + fr + fg
    return [(fd, v["F_drag"]), (fr, v["F_roll"]), (fg, v["F_grade"]), (total, v["F_total"]),
            (total * speed, v["P_wheels"]), (total * speed * 100 / v["eff_pct"], v["P_engine"])]


def adiabatic(v):
    gam = v["gamma"]
    T1 = v["T1_C"] + ZERO_C
    V1 = v["V1_L"] * 1e-3
    V2 = V1 / v["ratio"] if v["direction"] == "compression" else V1 * v["ratio"]
    P1 = v["P1"]
    P2 = P1 * (V1 / V2) ** gam
    T2 = P2 * V2 / (P1 * V1) * T1
    n = P1 * V1 / (GAS_R * T1)
    cv = GAS_R / (gam - 1)
    w_by = -n * cv * (T2 - T1)        # first law with Q = 0
    out = [(P2, v["P2"]), (T2, v["T2"]), (n, v["n"]), (w_by, v["W_by"]),
           (T1 * (V1 / V2) ** (gam - 1), v["T2"])]
    expected_sign = 1.0 if v["direction"] == "expansion" else -1.0
    out.append((float(math.copysign(1.0, w_by) == expected_sign), 1.0))
    if v["gas"] == "helium":
        out.append((gam, 5 / 3))
    else:
        out.append((gam, 1.4))
    return out


def isothermal(v):
    T = v["T_C"] + ZERO_C
    n = v["n"]
    if v["by_volume"]:
        V1, V2 = v["V1_L"], v["V2_L"]
        out = [(n * GAS_R * T / V1, v["P1_kPa"]), (n * GAS_R * T / V2, v["P2_kPa"])]  # kPa = J/L
    else:
        P1, P2 = v["P1_kPa"], v["P2_kPa"]
        V1, V2 = n * GAS_R * T / P1, n * GAS_R * T / P2
        out = [(V1, v["V1_L"]), (V2, v["V2_L"])]
    work = n * GAS_R * T * (math.log(V2) - math.log(V1))
    out += [(work, v["W"]), (work, v["Q"]), (work / T, v["dS"]), (float((work > 0) == v["expand"]), 1.0)]
    return out


def entropy_water(v):
    if v["mode"] == "heating":
        T1, T2, Tr = v["T1_C"] + ZERO_C, v["T2_C"] + ZERO_C, v["T_res_C"] + ZERO_C
        heat = v["m"] * CW * (v["T2_C"] - v["T1_C"])
        s_w = v["m"] * CW * (math.log(T2) - math.log(T1))
        return [(heat, v["Q"]), (s_w, v["dS_water"]), (-heat / Tr, v["dS_res"]), (s_w - heat / Tr, v["dS_total"]),
                (float(s_w - heat / Tr > 0), 1.0)]
    m1, m2 = v["m1"], v["m2"]
    tf = (m1 * v["T1_C"] + m2 * v["T2_C"]) / (m1 + m2)
    Tf = tf + ZERO_C
    s1 = m1 * CW * math.log(Tf / (v["T1_C"] + ZERO_C))
    s2 = m2 * CW * math.log(Tf / (v["T2_C"] + ZERO_C))
    return [(tf, v["Tf_C"]), (s1, v["dS1"]), (s2, v["dS2"]), (s1 + s2, v["dS_total"]), (float(s1 + s2 > 0), 1.0)]


def composite_wall(v):
    A = v["A"]
    resist = [L / 100 / (k * A) for L, k in zip(v["L_cm"], v["k"])]
    total = math.fsum(resist)
    power = (v["T_in"] - v["T_out"]) / total
    out = [(total, v["R_tot"]), (power, v["P"]), (1 / (total * A), v["U"]), (power * 86400 / 3.6e6, v["E_kWh_day"])]
    out += list(zip(resist, v["R"]))
    temp = v["T_in"]
    for R, stored in zip(resist, v["T_interfaces"]):
        temp -= power * R
        out.append((temp, stored))
    out.append((v["T_in"] - power * total, v["T_out"]))
    return out


def otto(v):
    r, gam = v["r"], v["gamma"]
    T1 = v["T1_C"] + ZERO_C
    T2 = T1 * r ** (gam - 1)
    T4 = v["T3"] * r ** (1 - gam)
    eta = 1 - (T4 - T1) / (v["T3"] - T2)   # from Q_out / Q_in of the constant-volume steps
    work = eta * v["Q_in"]
    return [(eta, v["eta"]), (1 - r ** (1 - gam), v["eta"]), (T2, v["T2"]), (T4, v["T4"]), (work, v["W"]),
            (v["Q_in"] - work, v["Q_out"]), (work * v["n_cyl"] * v["rpm"] / 60 / 2, v["P"]),
            (1 - T1 / v["T3"], v["eta_carnot"]), (float(v["eta_carnot"] > eta), 1.0)]


def sweat(v):
    heat = v["P"] * v["t_min"] * 60 * v["f_pct"] / 100
    mass = heat / LV_SKIN
    return [(heat, v["Q"]), (mass, v["m_sweat"]), (mass * 60 / v["t_min"], v["rate_L_per_h"]),
            (heat / (v["M"] * CBODY), v["dT"])]


CHECKS = {
    "banked_curve_no_friction": banked,
    "conical_pendulum_motion": conical,
    "vertical_circle_string_tension": vertical_circle,
    "loop_the_loop_track": loop,
    "center_of_mass_point_masses": center_of_mass,
    "physical_pendulum_parallel_axis": physical_pendulum,
    "damped_oscillator_q_factor": damped,
    "driven_oscillator_resonance": driven,
    "hohmann_transfer_earth_orbits": hohmann,
    "satellite_orbital_energy_budget": orbital_energy,
    "stokes_terminal_velocity": stokes,
    "torricelli_efflux_jet": torricelli,
    "poiseuille_pipe_flow": poiseuille,
    "ballistic_pendulum_speed": ballistic,
    "recoil_momentum_conservation": recoil,
    "vehicle_road_load_power": road_load,
    "adiabatic_process_ideal_gas": adiabatic,
    "isothermal_process_ideal_gas": isothermal,
    "entropy_change_water": entropy_water,
    "composite_wall_conduction": composite_wall,
    "otto_cycle_engine": otto,
    "evaporative_cooling_sweat": sweat,
}
