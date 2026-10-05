"""Independent re-computation for scripts/problem_generators/extra_em_waves_modern.py.

Each entry maps a template name to ``function(values) -> [(recomputed, stored), ...]``. The formulas and constants are
written out here independently of the generator module (which is deliberately not imported).
"""

import math

c_ = 2.998e8           # speed of light, m/s
h_ = 6.626e-34         # Planck constant, J s
e_ = 1.602e-19         # elementary charge, C
me_ = 9.109e-31        # electron mass, kg
eps0_ = 8.854e-12      # vacuum permittivity, F/m
NA_ = 6.022e23         # Avogadro constant, 1/mol
u_kg_ = 1.66054e-27    # atomic mass unit, kg
u_MeV_ = 931.494       # MeV per u
MeV_J_ = 1.602e-13     # J per MeV
S0_ = 1361.0           # solar constant, W/m^2
tau_mu_ = 2.197e-6     # muon lifetime, s
m_mu_MeV_ = 105.66     # muon rest energy, MeV


def _pairs(*items):
    return list(items)


# --------------------------------------------------------------------- circuits


def _capacitors(v):
    C1, C2, C3, V = v["C1_uF"], v["C2_uF"], v["C3_uF"], v["V"]
    if v["config"] == "series_with_parallel_pair":
        Cp = C2 + C3
        Ceq = 1 / (1 / C1 + 1 / Cp)
        Qtot = Ceq * V
        q1, v1 = Qtot, Qtot / C1
        vp = V - v1
        q2, q3, v2, v3 = C2 * vp, C3 * vp, vp, vp
    else:
        Cs = 1 / (1 / C1 + 1 / C2)
        Ceq = Cs + C3
        qs = Cs * V
        q1 = q2 = qs
        v1, v2 = qs / C1, qs / C2
        q3, v3 = C3 * V, V
        Qtot = qs + q3
    U = (q1 * v1 + q2 * v2 + q3 * v3) / 2 / 1000  # mJ, from the sum of the parts
    return _pairs((Ceq, v["C_eq_uF"]), (Qtot, v["Q_total_uC"]), (q1, v["Q1_uC"]), (q2, v["Q2_uC"]), (q3, v["Q3_uC"]),
                  (v1, v["V1"]), (v2, v["V2"]), (v3, v["V3"]), (U, v["U_total_mJ"]))


def _kirchhoff(v):
    E1, e2 = v["E1"], v["orient2"] * v["E2"]
    R1, R2, R3 = v["R1"], v["R2"], v["R3"]
    # node-voltage method instead of loop currents
    Va = (E1 / R1 + e2 / R2) / (1 / R1 + 1 / R2 + 1 / R3)
    I1, I2, I3 = (E1 - Va) / R1, (e2 - Va) / R2, Va / R3
    return _pairs((I1, v["I1"]), (I2, v["I2"]), (I3, v["I3"]), (Va, v["V_ab"]),
                  (E1 * I1 + e2 * I2, v["P_dissipated"]))


def _bridge(v):
    if v["variant"] == "wheatstone":
        Rx = v["R3"] * v["R2"] / v["R1"]
        Rpar = 1 / (1 / (v["R1"] + v["R2"]) + 1 / (v["R3"] + Rx))
        I = v["V"] / Rpar
        Ix = v["V"] / (v["R3"] + Rx)
        return _pairs((Rx, v["Rx"]), (I * 1000, v["I_total_mA"]), (Ix * Ix * Rx * 1000, v["P_x_mW"]))
    l = v["l_cm"]
    Rx = v["R_known"] * l / (100 - l)
    ratio = (Rx + v["S"]) / v["R_known"]
    l_new = 100 * ratio / (1 + ratio)
    return _pairs((Rx, v["Rx"]), (l_new, v["l_new_cm"]))


def _rl(v):
    L, R, E = v["L"], v["R"], v["emf"]
    tau = L / R
    out = [(tau, v["tau"]), (E / R, v["I_final"])]
    if v["variant"] == "at_time":
        I = E / R * (1 - math.exp(-v["t"] * R / L))
        out += [(I, v["I_t"]), (E - I * R, v["V_L"]), (L * I * I / 2, v["U_t"])]
    else:
        out += [(tau * math.log(100 / (100 - v["percent"])), v["t"]), (L * (E / R) ** 2 / 2, v["U_final"])]
    return out


def _rlc(v):
    w = 2 * math.pi * v["f"]
    XL, XC = w * v["L"], 1 / (w * v["C"])
    Z = math.sqrt(v["R"] ** 2 + (XL - XC) ** 2)
    I = v["V"] / Z
    phi = math.degrees(math.atan((XL - XC) / v["R"]))
    return _pairs((XL, v["X_L"]), (XC, v["X_C"]), (Z, v["Z"]), (I, v["I"]), (phi, v["phi_deg"]),
                  (math.cos(math.radians(phi)), v["power_factor"]), (v["V"] * I * v["R"] / Z, v["P"]),
                  (1 / (2 * math.pi * math.sqrt(v["L"] * v["C"])), v["f0"]))


def _pf_correction(v):
    P = v["P_kW"] * 1000
    Q1 = P * math.sqrt(1 - v["pf1"] ** 2) / v["pf1"]
    Q2 = P * math.sqrt(1 - v["pf2"] ** 2) / v["pf2"]
    Cap = (Q1 - Q2) / (2 * math.pi * v["f"] * v["V"] ** 2)
    return _pairs((P / v["pf1"] / 1000, v["S1_kVA"]), (Q1 / 1000, v["Q1_kvar"]), ((Q1 - Q2) / 1000, v["Qc_kvar"]),
                  (Cap * 1e6, v["C_uF"]), (P / (v["pf1"] * v["V"]), v["I1"]), (P / (v["pf2"] * v["V"]), v["I2"]))


# --------------------------------------------------------------------- fields and particles


def _hall(v):
    I, B, t, w = v["I"], v["B"], v["t"], v["w"]
    if v["variant"] == "semiconductor":
        n = I * B / (e_ * t * v["V_H"])
        vd = I / (n * e_ * w * t)
        return _pairs((n, v["n"]), (vd, v["v_d"]), (1 / (n * e_), v["R_H"]))
    vd = I / (v["n"] * e_ * w * t)
    return _pairs((vd, v["v_d"]), (vd * B * w, v["V_H"]), (vd * B, v["E_H"]))


def _mass_spec(v):
    V, B = v["V"], v["B"]
    m1, m2 = v["m1_u"] * u_kg_, v["m2_u"] * u_kg_
    v1 = math.sqrt(2 * e_ * V / m1)
    r1 = m1 * v1 / (e_ * B)
    r2 = m2 * math.sqrt(2 * e_ * V / m2) / (e_ * B)
    return _pairs((v1, v["v1"]), (r1, v["r1"]), (r2, v["r2"]), (2 * (r2 - r1), v["separation"]))


def _em_wave(v):
    if v["variant"] == "laser":
        area = math.pi * (v["d"] / 2) ** 2
        I = v["P"] / area
        E0 = math.sqrt(2 * I / (c_ * eps0_))
        k = 2 if v["reflect"] else 1
        return _pairs((I, v["I"]), (E0, v["E0"]), (E0 / c_, v["B0"]), (k * I / c_, v["p_rad"]), (k * v["P"] / c_, v["F"]))
    I = S0_ / v["r_AU"] ** 2
    F = 2 * I * v["A"] / c_
    return _pairs((I, v["I"]), (math.sqrt(2 * I / (c_ * eps0_)), v["E0"]), (F, v["F"]), (F / v["m"], v["a"]),
                  (F / v["m"] * 86400, v["dv_day"]))


# --------------------------------------------------------------------- waves and optics


def _malus(v):
    angles = v["angles_deg"]
    I = v["I0"] * (math.cos(math.radians(angles[0])) ** 2 if v["mode"] == "polarized" else 0.5)
    seq = [I]
    for a, b in zip(angles, angles[1:]):
        I *= math.cos(math.radians(b - a)) ** 2
        seq.append(I)
    out = [(float(len(seq)), float(len(v["intensities"])))]
    out += list(zip(seq, v["intensities"]))
    out += [(I, v["I_final"]), (I / v["I0"], v["fraction"])]
    if v["mode"] == "crossed":
        out.append((v["I0"] / 8 * math.sin(math.radians(2 * angles[1])) ** 2, v["I_final"]))
    return out


def _brewster(v):
    if v["variant"] == "forward":
        thB = math.atan2(v["n2"], v["n1"])
        tht = math.asin(v["n1"] * math.sin(thB) / v["n2"])  # Snell's law, independently of thB + tht = 90
        rs = (v["n1"] * math.cos(thB) - v["n2"] * math.cos(tht)) / (v["n1"] * math.cos(thB) + v["n2"] * math.cos(tht))
        return _pairs((math.degrees(thB), v["theta_B"]), (math.degrees(tht), v["theta_t"]), (rs * rs, v["R_s"]),
                      (rs * rs * v["I0"] / 2, v["I_reflected"]))
    n = math.tan(math.radians(v["theta_B"]))
    return _pairs((n, v["n"]), (math.degrees(math.asin(math.sin(math.radians(v["theta_B"])) / n)), v["theta_t"]),
                  (math.degrees(math.asin(1 / n)), v["theta_c"]))


def _thin_film(v):
    if v["variant"] == "film_colors":
        path = 2 * v["n_film"] * v["t_nm"]
        bright = [path / (k + 0.5) for k in range(200) if 380 <= path / (k + 0.5) <= 750]
        dark = [path / k for k in range(1, 200) if 380 <= path / k <= 750]
        out = [(float(len(bright)), float(len(v["lam_bright"]))), (float(len(dark)), float(len(v["lam_dark"])))]
        return out + list(zip(bright, v["lam_bright"])) + list(zip(dark, v["lam_dark"]))
    nc, ns, lam = v["n_c"], v["n_s"], v["lam_nm"]
    r1, r2 = (1 - nc) / (1 + nc), (nc - ns) / (nc + ns)
    # quarter-wave layer: the two reflections are in antiphase; combine the amplitudes with multiple reflections
    r = (r1 - r2) / (1 - r1 * r2)
    return _pairs((lam / nc / 4, v["t_min"]), (0.75 * lam / nc, v["t_next"]), (((1 - ns) / (1 + ns)) ** 2, v["R_uncoated"]),
                  (r * r, v["R_coated"]))


def _single_slit(v):
    lam = v["lam_nm"] * 1e-9
    if v["variant"] == "find_pattern":
        a = v["a_um"] * 1e-6
        s1, s2 = lam / a, 2 * lam / a
        y1 = v["L"] * s1 / math.sqrt(1 - s1 * s1)
        y2 = v["L"] * s2 / math.sqrt(1 - s2 * s2)
        return _pairs((math.degrees(math.asin(s1)), v["theta1_deg"]), (y1 * 1000, v["y1_mm"]), (y2 * 1000, v["y2_mm"]),
                      (2 * y1 * 1000, v["W_mm"]))
    y1 = v["W_mm"] / 2 / 1000
    sin1 = y1 / math.hypot(y1, v["L"])
    return _pairs((lam / sin1 * 1e6, v["a_um"]), (math.degrees(math.asin(sin1)), v["theta1_deg"]))


def _rayleigh(v):
    theta = 1.22 * v["lam_nm"] * 1e-9 / v["D"]
    if v["variant"] == "eye":
        return _pairs((theta, v["theta"]), (v["s"] / theta, v["L_max"]))
    if v["variant"] == "moon":
        return _pairs((theta, v["theta"]), (theta * 180 / math.pi * 3600, v["theta_arcsec"]), (theta * 3.84e8, v["s_min"]))
    return _pairs((theta, v["theta"]), (theta * v["h_km"] * 1000, v["s_min"]))


def _pipe(v):
    speed = 331.3 * math.sqrt((v["T_C"] + 273.15) / 273.15)
    out = [(speed, v["v"])]
    if v["variant"] == "find_frequencies":
        if v["kind"] == "open":
            f = [k * speed / (2 * v["L"]) for k in (1, 2, 3)]
        else:
            f = [k * speed / (4 * v["L"]) for k in (1, 3, 5)]
        out += list(zip(f, v["freqs"])) + [(3.0, float(len(v["freqs"])))]
    else:
        quarter = v["kind"] == "closed"
        L = speed / ((4 if quarter else 2) * v["f1"])
        out += [(L, v["L"]), ((3 if quarter else 2) * v["f1"], v["f_next"])]
    return out


def _beats(v):
    if v["variant"] == "string":
        flat = v["effect"] == "decreases"  # tightening helps -> string was below the fork
        fs = v["f_ref"] - v["f_beat"] if flat else v["f_ref"] + v["f_beat"]
        return _pairs((fs, v["f_string"]), (v["T"] * v["f_ref"] ** 2 / fs ** 2, v["T_new"]))
    below = v["effect"] == "increases"  # lowering f_B increases the beats -> f_B < f_A
    fB = v["f_A"] - v["f_beat"] if below else v["f_A"] + v["f_beat"]
    return _pairs((fB, v["f_B"]), (1 / v["f_beat"], v["beat_period"]))


# --------------------------------------------------------------------- quantum, relativity, nuclear


def _compton(v):
    hc_keV_pm = h_ * c_ / e_ * 1e9  # eV·m -> keV·pm
    lam = v["lam_pm"] if not v["given_energy"] else hc_keV_pm / v["E_keV"]
    E = hc_keV_pm / lam
    th = math.radians(v["theta_deg"])
    dl = h_ / (me_ * c_) * 1e12 * (1 - math.cos(th))
    E2 = hc_keV_pm / (lam + dl)
    mc2 = me_ * c_ ** 2 / e_ / 1000
    # electron recoil angle from momentum components (photon momenta in keV/c)
    px = E - E2 * math.cos(th)
    py = E2 * math.sin(th)
    phi = math.degrees(math.atan2(py, px)) if v["theta_deg"] != 180 else 0.0
    out = _pairs((lam, v["lam_pm"]), (E, v["E_keV"]), (dl, v["dlam_pm"]), (lam + dl, v["lam2_pm"]), (E2, v["E2_keV"]),
                 (E - E2, v["K_keV"]), (phi, v["phi_deg"]))
    # energy-momentum consistency of the electron: (K + mc^2)^2 = (pc)^2 + (mc^2)^2
    K = E - E2
    out.append(((K + mc2) ** 2, (px ** 2 + py ** 2) + mc2 ** 2))
    return out


def _hydrogen_like(v):
    Z, nu, nl = v["Z"], v["n_upper"], v["n_lower"]
    Eu, El = -13.6 * Z * Z / nu ** 2, -13.6 * Z * Z / nl ** 2
    dE = Eu - El
    return _pairs((Eu, v["E_upper_eV"]), (El, v["E_lower_eV"]), (dE, v["dE_eV"]), (1240 / dE, v["lambda_nm"]),
                  (13.6 * Z * Z, v["E_ion_eV"]), (0.0529 * nu ** 2 / Z, v["r_upper_nm"]))


def _vel_add(v):
    if v["variant"] == "launch":
        w = v["direction"] * v["v_rel"]
        # rapidities add linearly
        res = math.tanh(math.atanh(v["u"]) + math.atanh(w))
        return _pairs((res, v["v"]), (v["u"] + w, v["v_galilean"]))
    res = math.tanh(math.atanh(v["a"]) + math.atanh(v["b"]))
    return _pairs((res, v["v"]), (math.cosh(math.atanh(v["a"]) + math.atanh(v["b"])), v["gamma"]))


def _doppler(v):
    if v["variant"] == "find_wavelength":
        b = v["beta"] if v["receding"] else -v["beta"]
        lam = v["lam0"] * math.exp(math.atanh(b))  # sqrt((1+b)/(1-b)) = e^rapidity
        return _pairs((lam, v["lam_obs"]), (lam / v["lam0"] - 1, v["z"]))
    rap = math.log(v["lam_obs"] / v["lam0"])
    b = math.tanh(rap)
    return _pairs((abs(b), v["beta"]), (float(b > 0), float(v["receding"])), (v["lam_obs"] / v["lam0"] - 1, v["z"]))


def _muon(v):
    if "E_GeV" in v:
        gamma = v["E_GeV"] * 1000 / m_mu_MeV_
        beta = math.sqrt(gamma ** 2 - 1) / gamma
    else:
        beta = v["beta"]
        gamma = 1 / math.sqrt((1 - beta) * (1 + beta))
    h = v["h_km"] * 1000
    t = h / (beta * c_)
    t0 = (h / gamma) / (beta * c_)  # muon frame: contracted atmosphere
    return _pairs((beta, v["beta"]), (gamma, v["gamma"]), (t, v["t_lab"]), (t0, v["t_proper"]),
                  (v["N0"] * 0.5 ** (t0 / (tau_mu_ * math.log(2))), v["N_sea"]),
                  (v["N0"] * math.exp(-t / tau_mu_), v["N_classical"]))


MASS_U = {"n": 1.008665, "p": 1.007825, "d": 2.014102, "t": 3.016049, "He3": 3.016029, "He4": 4.002603,
          "Li6": 6.015123, "Li7": 7.016003, "Be7": 7.016929, "Be9": 9.012183, "B10": 10.012937, "C12": 12.0,
          "C13": 13.003355, "N14": 14.003074, "O17": 16.999132, "Al27": 26.981538, "P30": 29.978313}


def _parse_reaction(rid):
    left, right = rid.split("->")
    return left.split("+"), right.split("+")


def _q_value(v):
    react, prod = _parse_reaction(v["reaction"])
    Min = sum(MASS_U[k] for k in react)
    Mout = sum(MASS_U[k] for k in prod)
    Q = (Min - Mout) * u_MeV_
    out = [(Min, v["M_initial_u"]), (Mout, v["M_final_u"]), (Q, v["Q_MeV"])]
    if v["kind"] in ("fusion", "capture"):
        ma, mb = MASS_U[prod[0]], MASS_U[prod[1]]
        # equal and opposite momenta: K_a / K_b = m_b / m_a and K_a + K_b = Q
        Kb = Q / (1 + mb / ma)
        out += [(Q - Kb, v["K_a_MeV"]), (Kb, v["K_b_MeV"])]
        grams = v["m_mg"] / 1000
        molar = Min if v["kind"] == "fusion" else MASS_U[react[0]]
        N = grams / molar * NA_
        out += [(N, v["N_reactions"]), (N * Q * MeV_J_, v["E_J"])]
    elif Q > 0:
        out.append((v["K_MeV"] + Q, v["K_products_MeV"]))
    else:
        target, proj = react
        Kth = -Q * (MASS_U[target] + MASS_U[proj]) / MASS_U[target]
        out += [(Kth, v["K_th_MeV"]), (float(v["K_MeV"] > Kth), float(v["possible"]))]
        if v["possible"]:
            out.append((v["K_MeV"] + Q, v["K_products_MeV"]))
    return out


def _activity(v):
    lam = 0.693147180559945 / v["half_life_s"]
    if v["variant"] == "find_activity":
        N = v["m_g"] * NA_ / v["M"]
        return _pairs((lam, v["lambda"]), (N, v["N"]), (lam * N, v["A_Bq"]))
    N = v["A_Bq"] / lam
    return _pairs((lam, v["lambda"]), (N, v["N"]), (N / NA_ * v["M"], v["m_g"]))


def _fission(v):
    J_per_fission = 200 * MeV_J_
    per_kg = NA_ / 0.235044 * J_per_fission
    out = [(per_kg / (v["Hc_MJ_per_kg"] * 1e6), v["ratio"])]
    if v["variant"] == "power_plant":
        E = v["P_e_MW"] * 1e6 * 100 / v["eta_pct"] * v["days"] * 24 * 3600
        out += [(E, v["E_th_J"]), (E / J_per_fission, v["N_fissions"]), (E / per_kg, v["m_U_kg"]),
                (E / (v["Hc_MJ_per_kg"] * 1e6), v["m_coal_kg"]), (E / c_ ** 2, v["dm_kg"])]
    else:
        E = v["m_g"] / 1000 * per_kg
        out += [(E, v["E_J"]), (E / J_per_fission, v["N_fissions"]), (E / (v["Hc_MJ_per_kg"] * 1e6), v["m_coal_kg"]),
                (E * v["eta_pct"] / 100 / 3.6e9 / v["use_MWh"], v["years"])]
    return out


CHECKS = {
    "capacitor_network_charge_energy": _capacitors,
    "kirchhoff_two_loop_circuit": _kirchhoff,
    "wheatstone_bridge_balance": _bridge,
    "rl_circuit_current_growth": _rl,
    "series_rlc_phase_power": _rlc,
    "power_factor_correction_capacitor": _pf_correction,
    "hall_effect_carrier_density": _hall,
    "mass_spectrometer_isotope_separation": _mass_spec,
    "em_wave_intensity_radiation_pressure": _em_wave,
    "malus_law_polarizer_chain": _malus,
    "brewster_angle_polarization": _brewster,
    "thin_film_interference_colors": _thin_film,
    "single_slit_diffraction_minima": _single_slit,
    "rayleigh_resolution_limit": _rayleigh,
    "air_column_pipe_resonance": _pipe,
    "beat_frequency_tuning": _beats,
    "compton_scattering_shift": _compton,
    "hydrogen_like_ion_levels": _hydrogen_like,
    "relativistic_velocity_addition": _vel_add,
    "relativistic_doppler_redshift": _doppler,
    "muon_time_dilation_survival": _muon,
    "nuclear_reaction_q_value": _q_value,
    "radioisotope_activity_from_mass": _activity,
    "fission_u235_vs_coal": _fission,
}
