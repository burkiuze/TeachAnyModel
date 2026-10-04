"""Tests for the synthetic problem generators.

Run from the repository root:

    python -m unittest discover -s tests -v

Besides schema and determinism checks, ``RecomputeTest`` re-derives the answer of
almost every template from the inputs stored in ``values`` using independently
written formulas, so a bug in a generator's arithmetic shows up as a failure.
"""

import json
import math
import os
import random
import re
import sys
import unittest
from fractions import Fraction

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
sys.path.insert(0, os.path.join(ROOT, "scripts"))

from generate_problems import generate  # noqa: E402
from problem_generators import REGISTRY, build  # noqa: E402
from problem_generators.biology import CODON_TABLE  # noqa: E402
from problem_generators.chemistry import electron_configuration, molar_mass, parse_formula, unpaired  # noqa: E402
from problem_generators.common import fix_articles, fmt  # noqa: E402

# Constants written out independently of problem_generators.common
g = 9.81
G_ = 6.674e-11
c_ = 2.998e8
h_ = 6.626e-34
hbar_ = 1.055e-34
e_ = 1.602e-19
me_ = 9.109e-31
kB_ = 1.381e-23
R_ = 8.314
NA_ = 6.022e23
F_ = 96485.0
EPS0_ = 8.854e-12
MU0_ = 1.2566e-6
SIGMA_ = 5.670e-8
KE_ = 8.988e9
AU_ = 1.496e11
PC_ = 3.086e16
MSUN_ = 1.989e30
RSUN_ = 6.957e8
MEARTH_ = 5.972e24
REARTH_ = 6.371e6
SAMPLES = 25


def records(name, n=SAMPLES, seed="test"):
    meta = next(m for m in REGISTRY if m["name"] == name)
    rng = random.Random(f"{seed}:{name}")
    return [build(meta, meta["fn"](rng), i) for i in range(n)]


def poly_eval(coeffs, x):
    total = 0
    for cf in coeffs:
        total = total * x + cf
    return total


# ---------------------------------------------------------------------------
# Independent recomputation: template name -> function(values) -> [(computed, stored), ...]
# ---------------------------------------------------------------------------


def _physics():
    rad = math.radians
    checks = {
        "kinematics_constant_acceleration": lambda v: [(v["v0"] + v["a"] * v["t"], v["v"]),
                                                       (v["v0"] * v["t"] + 0.5 * v["a"] * v["t"] ** 2, v["s"])],
        "kinematics_stopping_distance": lambda v: [(v["v_kmh"] / 3.6 * v["t_reaction"] + (v["v_kmh"] / 3.6) ** 2 / (2 * v["decel"]), v["d_total"])],
        "free_fall": lambda v: [(math.sqrt(2 * v["h"] / g), v["t"]), (math.sqrt(2 * g * v["h"]), v["v"])],
        "vertical_throw": lambda v: [(v["v0"] / g, v["t_top"]), (v["v0"] ** 2 / (2 * g), v["h_max"]), (2 * v["v0"] / g, v["T"])],
        "projectile_motion": lambda v: [(2 * v["v0"] * math.sin(rad(v["theta_deg"])) / g, v["T"]),
                                        ((v["v0"] * math.sin(rad(v["theta_deg"]))) ** 2 / (2 * g), v["H"]),
                                        (v["v0"] ** 2 * math.sin(rad(2 * v["theta_deg"])) / g, v["R"])],
        "horizontal_launch": lambda v: [(v["v0"] * math.sqrt(2 * v["h"] / g), v["x"]),
                                        (math.sqrt(v["v0"] ** 2 + 2 * g * v["h"]), v["v_impact"])],
        "incline_with_friction": lambda v: [(g * (math.sin(rad(v["theta_deg"])) - v["mu_k"] * math.cos(rad(v["theta_deg"]))), v["a"]),
                                            (v["m"] * g * math.cos(rad(v["theta_deg"])), v["N"])],
        "horizontal_push_friction": lambda v: [((v["F"] - v["mu_k"] * v["m"] * g) / v["m"], v["a"])],
        "atwood_machine": lambda v: [((v["m2"] - v["m1"]) / (v["m1"] + v["m2"]) * g, v["a"]),
                                     (2 * v["m1"] * v["m2"] * g / (v["m1"] + v["m2"]), v["T"])],
        "table_and_hanging_mass": lambda v: [((v["m2"] - v["mu_k"] * v["m1"]) * g / (v["m1"] + v["m2"]), v["a"])],
        "elevator_scale": lambda v: [(v["m"] * (g + v["sign"] * v["a"]), v["N"])],
        "circular_motion": lambda v: [(v["m"] * v["v"] ** 2 / v["r"], v["F_c"]), (2 * math.pi * v["r"] / v["v"], v["T"])],
        "flat_curve_max_speed": lambda v: [(math.sqrt(v["mu_s"] * g * v["r"]), v["v_max"])],
        "energy_conservation_slide": lambda v: [(math.sqrt(2 * g * v["h"]), v["v"])],
        "spring_launch": lambda v: [(0.5 * v["k"] * v["x"] ** 2, v["U"]), (v["x"] * math.sqrt(v["k"] / v["m"]), v["v"])],
        "work_and_power_lifting": lambda v: [(v["m"] * g * v["h"], v["W"]), (v["m"] * g * v["h"] / v["t"], v["P"])],
        "perfectly_inelastic_collision": lambda v: [((v["m1"] * v["v1"] + v["m2"] * v["v2"]) / (v["m1"] + v["m2"]), v["vf"])],
        "elastic_collision_1d": lambda v: [((v["m1"] - v["m2"]) / (v["m1"] + v["m2"]) * v["v1"], v["v1f"]),
                                           (2 * v["m1"] / (v["m1"] + v["m2"]) * v["v1"], v["v2f"])],
        "impulse_average_force": lambda v: [(v["m"] * (v["vf"] + v["vi"]), v["J"]), (v["m"] * (v["vf"] + v["vi"]) / v["dt"], v["F"])],
        "rolling_down_incline": lambda v: [(math.sqrt(2 * g * v["h"] / (1 + v["c"])), v["v"])],
        "torque_angular_acceleration": lambda v: [(2 * v["F"] / (v["M"] * v["R"]), v["alpha"])],
        "angular_momentum_skater": lambda v: [(v["I1"] * v["w1"] / v["I2"], v["w2"]), (v["I1"] / v["I2"], v["KE_ratio"])],
        "satellite_orbit": lambda v: [(math.sqrt(G_ * MEARTH_ / (REARTH_ + 1000 * v["h_km"])), v["v"])],
        "surface_gravity_escape_velocity": lambda v: [(G_ * v["M"] / v["R"] ** 2, v["g_surface"]),
                                                      (math.sqrt(2 * G_ * v["M"] / v["R"]), v["v_esc"])],
        "pendulum_period": lambda v: [(2 * math.pi * math.sqrt(v["L"] / v["g"]), v["T"])],
        "spring_mass_shm": lambda v: [(math.sqrt(v["k"] / v["m"]), v["omega"]), (0.5 * v["k"] * v["A"] ** 2, v["E"]),
                                      (v["A"] * v["k"] / v["m"], v["a_max"])],
        "hydrostatic_pressure": lambda v: [(v["rho"] * g * v["depth"], v["P_gauge"])],
        "buoyancy_floating": lambda v: [(v["rho_object"] / v["rho_fluid"], v["fraction"]),
                                        (v["rho_object"] * v["V"] * g, v["F_B"])],
        "continuity_bernoulli": lambda v: [(v["v1"] * (v["d1"] / v["d2"]) ** 2, v["v2"]),
                                           (v["P1"] + 500 * (v["v1"] ** 2 - (v["v1"] * (v["d1"] / v["d2"]) ** 2) ** 2), v["P2"])],
        "ideal_gas_pressure": lambda v: [(v["n"] * R_ * (v["T_C"] + 273.15) / (v["V_L"] / 1000), v["P"])],
        "calorimetry_mixing": lambda v: [((v["m_metal"] * v["c_metal"] * v["T_metal"] + v["m_water"] * 4186 * v["T_water"])
                                          / (v["m_metal"] * v["c_metal"] + v["m_water"] * 4186), v["T_final"])],
        "heating_ice_to_steam": lambda v: [(v["m"] * (2100 * -v["T_initial"] + 334000
                                                      + (4186 * v["T_final"] if v["T_final"] < 100 else
                                                         4186 * 100 + 2257000 + 2010 * (v["T_final"] - 100))), v["Q_total"])],
        "carnot_engine": lambda v: [(1 - (v["T_cold_C"] + 273.15) / (v["T_hot_C"] + 273.15), v["efficiency"])],
        "rms_speed_gas": lambda v: [(math.sqrt(3 * R_ * (v["T_C"] + 273.15) / v["M"]), v["v_rms"]),
                                    (1.5 * kB_ * (v["T_C"] + 273.15), v["KE_avg"])],
        "thermal_expansion": lambda v: [(v["alpha"] * v["L"] * v["dT"], v["dL"])],
        "coulomb_force": lambda v: [(KE_ * abs(v["q1_uC"] * v["q2_uC"]) * 1e-12 / (v["r_cm"] / 100) ** 2, v["F"])],
        "parallel_plate_capacitor": lambda v: [(v["kappa"] * EPS0_ * v["A"] / v["d"], v["C"]), (v["V"] / v["d"], v["E"])],
        "resistor_network": lambda v: [(v["R1"] + v["R2"] * v["R3"] / (v["R2"] + v["R3"]), v["R_eq"]),
                                       (v["V"] / v["R_eq"], v["I"]), (v["I2"] + v["I3"], v["I"])],
        "electrical_power_energy": lambda v: [(v["P"] / v["V"], v["I"]), (v["V"] ** 2 / v["P"], v["R"]),
                                              (v["P"] * v["hours"] / 1000, v["E_kWh"])],
        "rc_charging": lambda v: [(v["R"] * v["C"], v["tau"]), (v["emf"] * (1 - math.exp(-v["t"] / (v["R"] * v["C"]))), v["V_C"])],
        "charged_particle_in_b_field": lambda v: [(v["q"] * v["v"] * v["B"], v["F"]), (v["m"] * v["v"] / (v["q"] * v["B"]), v["r"]),
                                                  (v["q"] * v["B"] / (2 * math.pi * v["m"]), v["f"])],
        "magnetic_field_wire_solenoid": lambda v: [(MU0_ * v["I"] / (2 * math.pi * v["r_cm"] / 100), v["B"])] if "r_cm" in v
        else [(MU0_ * v["n"] * v["I"], v["B"])],
        "faraday_induction": lambda v: [(v["N"] * v["A"] * abs(v["B2"] - v["B1"]) / v["dt"], v["emf"])],
        "transformer": lambda v: [(v["Vp"] * v["Ns"] / v["Np"], v["Vs"]), (v["P"] / v["Vp"], v["Ip"])],
        "lc_resonance": lambda v: [(1 / (2 * math.pi * math.sqrt(v["L"] * v["C"])), v["f0"])],
        "string_harmonics": lambda v: [(math.sqrt(v["T"] / v["mu"]), v["v"]), (math.sqrt(v["T"] / v["mu"]) / (2 * v["L"]), v["f1"])],
        "doppler_sound": lambda v: [(v["f"] * 343 / (343 - v["v_source"]), v["f_approach"]),
                                    (v["f"] * 343 / (343 + v["v_source"]), v["f_recede"])],
        "sound_intensity_decibels": lambda v: [(v["P"] / (4 * math.pi * v["r"] ** 2), v["I"]),
                                               (10 * math.log10(v["P"] / (4 * math.pi * v["r"] ** 2) / 1e-12), v["beta"])],
        "snell_refraction": lambda v: ([(math.degrees(math.asin(v["n1"] * math.sin(rad(v["theta1"])) / v["n2"])), v["theta2"])]
                                       if "theta2" in v else []) +
                                      ([(math.degrees(math.asin(v["n2"] / v["n1"])), v["theta_c"])] if "theta_c" in v else []),
        "thin_lens": lambda v: [(1 / (1 / v["f"] - 1 / v["do"]), v["di"]), (-v["di"] / v["do"], v["m"])],
        "double_slit": lambda v: [(v["lambda"] * v["L"] / v["d"], v["dy"])],
        "diffraction_grating": lambda v: [(math.degrees(math.asin(v["lambda"] * v["lines_per_mm"] * 1000)), v["theta1"]),
                                          (math.floor(1 / (v["lines_per_mm"] * 1000) / v["lambda"]), v["m_max"])],
        "photon_energy": lambda v: [(c_ / (v["lambda_nm"] * 1e-9), v["f"]), (h_ * c_ / (v["lambda_nm"] * 1e-9) / e_, v["E_eV"])],
        "photoelectric_effect": lambda v: [(1240 / v["lambda_nm"], v["E_photon_eV"]),
                                           (max(0.0, 1240 / v["lambda_nm"] - v["phi"]), v["K_max_eV"])],
        "de_broglie_wavelength": lambda v: [(h_ / math.sqrt(2 * me_ * e_ * v["V"]), v["lambda"])] if "V" in v
        else [(h_ / (v["m"] * v["v"]), v["lambda"])],
        "hydrogen_transition": lambda v: [(13.6 * abs(1 / v["n_final"] ** 2 - 1 / v["n_initial"] ** 2), v["dE_eV"]),
                                          (1240 / (13.6 * abs(1 / v["n_final"] ** 2 - 1 / v["n_initial"] ** 2)), v["lambda_nm"])],
        "particle_in_a_box": lambda v: [(h_ ** 2 / (8 * me_ * v["L"] ** 2) / e_, v["E1_eV"]), (v["n"] ** 2 * v["E1_eV"], v["En_eV"]),
                                        (h_ * c_ / (((v["n"] + 1) ** 2 - v["n"] ** 2) * h_ ** 2 / (8 * me_ * v["L"] ** 2)), v["lambda"])],
        "heisenberg_uncertainty": lambda v: [(hbar_ / (2 * v["dx"]), v["dp"]), (hbar_ / (2 * v["dx"]) / v["m"], v["dv"])],
        "tunneling_probability": lambda v: [(math.sqrt(2 * me_ * (v["V0_eV"] - v["E_eV"]) * e_) / hbar_, v["kappa"])],
        "radioactive_decay": lambda v: [(0.5 ** (v["t"] / v["half_life"]), v["fraction_remaining"]),
                                        (math.log(2) / v["half_life"], v["lambda"])],
        "radiocarbon_dating": lambda v: [(5730 / math.log(2) * math.log(100 / v["percent_remaining"]), v["age"])],
        "time_dilation": lambda v: [(1 / math.sqrt(1 - v["beta"] ** 2), v["gamma"]), (v["t0"] / math.sqrt(1 - v["beta"] ** 2), v["t"])],
        "relativistic_energy": lambda v: [(v["mc2"] / math.sqrt(1 - v["beta"] ** 2), v["E"]),
                                          (math.sqrt(v["E"] ** 2 - v["mc2"] ** 2), v["pc"])],
        "stefan_wien_radiation": lambda v: [(2.898e-3 / v["T"], v["lambda_max"]), (v["e"] * SIGMA_ * v["A"] * v["T"] ** 4, v["P"])],
    }
    return checks


def _chemistry():
    def hi_check(v):
        return [(v["HI"] ** 2 / (v["H2"] * v["I2"]), v["K"])]

    def diss_check(v):
        x, c0 = v["x"], v["c0"]
        return [((4 if v["nu"] == 2 else 1) * x * x / (c0 - x), v["K"])]

    def buffer_check(v):
        na, nb = v["ca"] * v["V"], v["cb"] * v["V"]
        pka = -math.log10(v["Ka"])
        if v["added"] == "HCl":
            na, nb = na + v["n_add"], nb - v["n_add"]
        else:
            na, nb = na - v["n_add"], nb + v["n_add"]
        return [(pka + math.log10(v["cb"] / v["ca"]), v["pH0"]), (pka + math.log10(nb / na), v["pH1"])]

    def strong_check(v):
        ion = v["c"] * v["n_ion"]
        return [(-math.log10(ion) if v["kind"] == "acid" else 14 + math.log10(ion), v["pH"])]

    return {
        "moles_and_particles": lambda v: [(molar_mass(v["formula"]), v["M"]), (v["mass"] / v["M"], v["n"]),
                                          (v["n"] * NA_, v["particles"]),
                                          (v["particles"] * parse_formula(v["formula"])[v["element"]], v["atoms"])],
        "percent_composition": lambda v: [(sum(val for k, val in v.items() if k.startswith("pct_")), 100.0)],
        "solution_preparation": lambda v: [(v["c"] * v["V_mL"] / 1000 * v["M"], v["mass"])],
        "dilution": lambda v: [(v["c2"] * v["V2"] / v["c1"], v["V1"])],
        "limiting_reactant": lambda v: [(100 * v["actual_g"] / v["theoretical_g"], v["percent_yield"])],
        "gas_stoichiometry": lambda v: [(v["n_gas"] * 0.08206 * (v["T_C"] + 273.15) / v["P_atm"], v["V_L"])],
        "titration_strong": lambda v: [(v["Cb"] * v["Vb_mL"] * v["base_OH"] / (v["Va_mL"] * v["acid_H"]), v["Ca"])],
        "gas_molar_mass_from_density": lambda v: [(v["d"] * 0.08206 * (v["T_C"] + 273.15) / v["P_atm"], v["M"])],
        "graham_effusion": lambda v: [(math.sqrt(v["M2"] / v["M1"]), v["rate_ratio"]), (v["t2"] / v["rate_ratio"], v["t1"])],
        "colligative_bp_fp": lambda v: [(v["m_solute"] / v["M"] / (v["m_solvent_g"] / 1000), v["molality"]),
                                        (v["i"] * v["Kb"] * v["molality"], v["dTb"]), (v["i"] * v["Kf"] * v["molality"], v["dTf"])],
        "osmotic_pressure_molar_mass": lambda v: [(v["m_mg"] / 1000 * 0.08206 * 298.15 / (v["pi_mmHg"] / 760 * v["V_mL"] / 1000), v["M"])],
        "clausius_clapeyron": lambda v: [(math.log(v["P2_mmHg"] / 760), -v["dH_kJ"] * 1000 / R_ * (1 / v["T2"] - 1 / v["Tb"]))],
        "enthalpy_from_formation": lambda v: [(-v["dHc"] * v["mass"] / molar_mass(v["formula"]), v["heat_kJ"])],
        "neutralization_calorimetry": lambda v: [(min(v["c_acid"], v["c_base"]) * v["V_mL"] / 1000, v["n_water"]),
                                                 (-(2 * v["V_mL"] * 4.18 * v["dT"]) / v["n_water"] / 1000, v["dH_kJ"])],
        "gibbs_spontaneity": lambda v: [(v["dH"] - v["T"] * v["dS"] / 1000, v["dG"])]
        + ([(v["dH"] * 1000 / v["dS"], v["T_crossover"])] if v["T_crossover"] is not None else []),
        "equilibrium_constant_gibbs": lambda v: [(math.log(v["K"]), -v["dG_kJ"] * 1000 / (R_ * v["T"]))],
        "equilibrium_ice_hi": hi_check,
        "equilibrium_dissociation": diss_check,
        "ksp_solubility": lambda v: [((v["a"] ** v["a"]) * (v["b"] ** v["b"]) * v["s"] ** (v["a"] + v["b"]), v["Ksp"])],
        "common_ion_solubility": lambda v: [(v["s_common"] * (v["s_common"] + v["c_common"]), v["Ksp"]),
                                            (math.sqrt(v["Ksp"]), v["s_water"])],
        "strong_acid_base_ph": strong_check,
        "weak_acid_ph": lambda v: [(v["H3O"] ** 2 / (v["c"] - v["H3O"]), v["Ka"]), (-math.log10(v["H3O"]), v["pH"])],
        "weak_base_ph": lambda v: [(v["OH"] ** 2 / (v["c"] - v["OH"]), v["Kb"]), (14 + math.log10(v["OH"]), v["pH"])],
        "buffer_ph": buffer_check,
        "weak_acid_titration": lambda v: [(v["Ca"] * v["Va"] / v["Cb"], v["Veq"]), (-math.log10(v["Ka"]), v["pH_half"])],
        "first_order_kinetics": lambda v: [(math.log(2) / v["t_half"], v["k"]), (v["A0"] * math.exp(-v["k"] * v["t"]), v["A"]),
                                           (math.log(100 / v["pct_target"]) / v["k"], v["t_target"])],
        "second_order_kinetics": lambda v: [(1 / (1 / v["A0"] + v["k"] * v["t"]), v["A"]), (1 / (v["k"] * v["A0"]), v["t_half_1"]),
                                            (2 * v["t_half_1"], v["t_half_2"])],
        "arrhenius_activation_energy": lambda v: [(R_ * math.log(v["k2"] / v["k1"]) / (1 / v["T1"] - 1 / v["T2"]) / 1000, v["Ea_kJ"])],
        "galvanic_cell_potential": lambda v: [(-v["n"] * F_ * v["E_cell"] / 1000, v["dG_kJ"]), (v["n"] * v["E_cell"] / 0.05916, v["log10K"])],
        "nernst_equation": lambda v: [(v["E0"] - 0.05916 / v["n"] * math.log10(v["Q"]), v["E"])],
        "electrolysis_faraday": lambda v: [(v["I"] * v["t_s"] * v["M"] / (v["n"] * F_), v["mass"])],
    }


def _biology():
    def chi(obs, exp):
        return sum((o - e) ** 2 / e for o, e in zip(obs, exp))

    def hw_chi(v):
        n = v["AA"] + v["Aa"] + v["aa"]
        p = (2 * v["AA"] + v["Aa"]) / (2 * n)
        exp = [p * p * n, 2 * p * (1 - p) * n, (1 - p) ** 2 * n]
        return [(chi([v["AA"], v["Aa"], v["aa"]], exp), v["chi2"])]

    def mendel_chi(v):
        n, tot = sum(v["observed"]), sum(v["expected_ratio"])
        return [(chi(v["observed"], [n * r / tot for r in v["expected_ratio"]]), v["chi2"])]

    def mono(v):
        p = v["p_recessive"] if v["target_recessive"] else 1 - v["p_recessive"]
        return [(math.comb(v["n"], v["k"]) * p ** v["k"] * (1 - p) ** (v["n"] - v["k"]), v["probability"])]

    def goldman(v):
        num = v["Ko"] + v["pNa"] * v["Nao"] + v["pCl"] * v["Cli"]
        den = v["Ki"] + v["pNa"] * v["Nai"] + v["pCl"] * v["Clo"]
        return [(61.5 * math.log10(num / den), v["Vm_mV"])]

    def diversity(v):
        n = sum(v["counts"])
        simpson = 1 - sum(k * (k - 1) for k in v["counts"]) / (n * (n - 1))
        shannon = -sum(k / n * math.log(k / n) for k in v["counts"])
        return [(simpson, v["simpson"]), (shannon, v["shannon"])]

    def primer(v):
        s = v["sequence"]
        at, gc = s.count("A") + s.count("T"), s.count("G") + s.count("C")
        comp = "".join({"A": "T", "T": "A", "G": "C", "C": "G"}[b] for b in reversed(s))
        return [(2 * at + 4 * gc, v["tm"]), (2 * at + 3 * gc, v["h_bonds"]), (float(comp == v["complement"]), 1.0)]

    def logistic(v):
        r, K, N0, t = v["r"], v["K"], v["N0"], v["t"]
        return [(N0 * math.exp(r * t), v["N_exp"]), (K / (1 + (K - N0) / N0 * math.exp(-r * t)), v["N_log"]),
                (r * v["N_now"] * (1 - v["N_now"] / K), v["dNdt"])]

    return {
        "hardy_weinberg": lambda v: [(math.sqrt(v["q2"]), v["q"]), (2 * v["q"] * (1 - v["q"]), v["carrier_freq"])],
        "hardy_weinberg_chi_square": hw_chi,
        "selection_against_recessive": lambda v: [(v["q0"] * (1 - v["s"] * v["q0"]) / (1 - v["s"] * v["q0"] ** 2), v["q1"])],
        "monohybrid_cross": mono,
        "x_linked_cross": lambda v: [((v["p_son_affected"] + v["p_daughter_affected"]) / 2, v["p_child_affected"])],
        "chi_square_mendelian": mendel_chi,
        "linkage_map_distance": lambda v: [(v["recombinants"] / v["N"], v["rf"])],
        "chargaff_rule": lambda v: [(v["A"], v["T"]), (v["G"], v["C"]), (v["A"] + v["T"] + v["G"] + v["C"], 100.0)],
        "primer_melting_temperature": primer,
        "michaelis_menten": lambda v: [(v["Vmax"] * v["S"] / (v["Km"] + v["S"]), v["v"])] if "v" in v
        else [(v["fraction"] * v["Km"] / (1 - v["fraction"]), v["S"])],
        "nernst_membrane_potential": lambda v: [(R_ * 310.15 / F_ / v["z"] * math.log(v["c_out"] / v["c_in"]) * 1000, v["E_mV"])],
        "goldman_resting_potential": goldman,
        "cardiac_output": lambda v: [(v["HR"] * v["SV"] / 1000, v["CO"])] if "HR" in v else [(v["VO2"] / (v["Ca"] - v["Cv"]), v["CO"])],
        "water_potential": lambda v: [(-v["i"] * v["C"] * 0.0831 * v["T"] + v["psi_p"], v["psi_cell"]),
                                      (-v["C_out"] * 0.0831 * v["T"], v["psi_out"])],
        "q10_temperature_coefficient": lambda v: [((v["R2"] / v["R1"]) ** (10 / (v["T2"] - v["T1"])), v["Q10"])],
        "microscope_magnification": lambda v: [(v["image_mm"] * 1000 / v["magnification"], v["actual_um"])],
        "surface_area_volume": lambda v: [(3 / v["r1"], v["ratio1"]), (3 / v["r2"], v["ratio2"])],
        "bacterial_growth": lambda v: [(v["N0"] * 2 ** (v["t_min"] / v["td_min"]), v["N"]),
                                       (v["td_min"] * math.log2(v["target"] / v["N0"]), v["t_target_min"])],
        "serial_dilution_plate_count": lambda v: [(v["colonies"] / v["volume_mL"] * 10 ** v["dilution_exp"], v["cfu_per_mL"])],
        "trophic_energy_transfer": lambda v: [(v["E0"] * v["efficiency"] ** v["levels"], v["E_top"])],
        "mark_recapture": lambda v: [(v["M"] * v["C"] / v["R"], v["N"])],
        "population_growth_models": logistic,
        "species_diversity": diversity,
    }


def _astronomy():
    return {
        "stellar_parallax": lambda v: [(1 / v["parallax"], v["d_pc"])],
        "distance_modulus": lambda v: [(v["m"] - v["M"], 5 * math.log10(v["d_pc"] / 10))],
        "magnitude_flux_ratio": lambda v: [(10 ** (0.4 * (v["m2"] - v["m1"])), v["flux_ratio"])],
        "inverse_square_irradiance": lambda v: [(1361 / v["a_AU"] ** 2, v["S"])],
        "light_travel_time": lambda v: [(v["distance_m"] / c_, v["t_s"])],
        "angular_size": lambda v: [(v["D_km"] / v["d_km"] * 206265, v["theta_arcsec"])],
        "wien_stellar_temperature": lambda v: [(2.898e-3 / v["T"] * 1e9, v["lambda_max_nm"])],
        "stellar_radius_luminosity": lambda v: [(math.sqrt(v["L"]) * (5772 / v["T"]) ** 2, v["R_solar"])],
        "main_sequence_lifetime": lambda v: [(v["M"] ** 3.5, v["L"]), (1e10 * v["M"] ** -2.5, v["t_years"])],
        "schwarzschild_radius": lambda v: [(2 * G_ * v["M_solar"] * MSUN_ / c_ ** 2, v["Rs_m"])],
        "kepler_third_law": lambda v: [((v["P_days"] / 365.25) ** 2 * v["M_star"], v["a_AU"] ** 3)] if "P_days" in v
        else [(v["P_years"] ** 2 * v["M_star"], v["a_AU"] ** 3)],
        "binary_star_mass": lambda v: [(v["a_arcsec"] / v["parallax"], v["a_AU"]), (v["a_AU"] ** 3 / v["P_years"] ** 2, v["M_total"])],
        "synodic_period": lambda v: [(1 / abs(1 - 1 / v["P"]), v["S_years"])],
        "planet_equilibrium_temperature": lambda v: [(v["T_star"] * math.sqrt(v["R_star"] * RSUN_ / (2 * v["a_AU"] * AU_))
                                                      * (1 - v["albedo"]) ** 0.25, v["T_eq"])],
        "exoplanet_transit_depth": lambda v: [(math.sqrt(v["depth_percent"] / 100) * v["R_star"] * RSUN_ / 1000, v["Rp_km"])],
        "hubble_law_redshift": lambda v: [((v["lambda_obs"] - v["lambda0"]) / v["lambda0"], v["z"]),
                                          (v["z"] * c_ / 1000 / 70, v["d_Mpc"])],
        "cosmic_scale_factor": lambda v: [(1 / (1 + v["z"]), v["a"]), (2.725 * (1 + v["z"]), v["T_K"])],
        "hubble_time": lambda v: [(PC_ * 1e6 / 1000 / v["H0"] / 3.156e7, v["t_H_years"])],
        "galaxy_rotation_mass": lambda v: [((v["v_kms"] * 1e3) ** 2 * v["r_kpc"] * 1e3 * PC_ / G_ / MSUN_, v["M_solar"])],
    }


def _mathematics():
    def phi(z):
        return 0.5 * (1 + math.erf(z / math.sqrt(2)))

    def deriv(v):
        cs = v["coeffs"]
        n = len(cs) - 1
        d = [cf * (n - i) for i, cf in enumerate(cs[:-1])]
        return [(float(d == v["derivative"]), 1.0), (poly_eval(d, v["x0"]), v["slope"]),
                (poly_eval(cs, v["x0"]) - v["slope"] * v["x0"], v["intercept"])]

    def integral(v):
        cs = v["coeffs"]
        n = len(cs) - 1
        anti = [Fraction(cf, n - i + 1) for i, cf in enumerate(cs)] + [Fraction(0)]
        return [(float(poly_eval(anti, Fraction(v["b"])) - poly_eval(anti, Fraction(v["a"]))), v["integral"])]

    def ode(v):
        """Check y(0), y'(0) and the ODE residual using analytic derivatives of the stored solution."""
        b, c, y0, v0 = v["b"], v["c"], v["y0"], v["v0"]
        if v["damping"] == "over":
            r1, r2, C1, C2 = v["r1"], v["r2"], v["C1"], v["C2"]

            def derivs(t):
                e1, e2 = math.exp(r1 * t), math.exp(r2 * t)
                return (C1 * e1 + C2 * e2, C1 * r1 * e1 + C2 * r2 * e2, C1 * r1 * r1 * e1 + C2 * r2 * r2 * e2)
        elif v["damping"] == "critical":
            r, C1, C2 = v["r"], v["C1"], v["C2"]

            def derivs(t):
                e, u = math.exp(r * t), C1 + C2 * t
                return (u * e, (C2 + r * u) * e, (2 * r * C2 + r * r * u) * e)
        else:
            al, be, A, B = v["alpha"], v["beta"], v["A"], v["B"]
            A1, B1 = al * A + be * B, al * B - be * A
            A2, B2 = al * A1 + be * B1, al * B1 - be * A1

            def derivs(t):
                e, cs, sn = math.exp(al * t), math.cos(be * t), math.sin(be * t)
                return (e * (A * cs + B * sn), e * (A1 * cs + B1 * sn), e * (A2 * cs + B2 * sn))
        y, yp, _ = derivs(0.0)
        out = [(y + 100, y0 + 100), (yp + 100, v0 + 100)]
        for t in (0.3, 1.1):
            y, yp, ypp = derivs(t)
            out.append((ypp + b * yp + c * y + 1.0, 1.0))  # residual should vanish
        return out

    def eigen(v):
        A, (l1, l2) = v["A"], v["eigenvalues"]
        out = []
        for lam, vec in ((l1, v["v1"]), (l2, v["v2"])):
            for row in range(2):
                out.append((A[row][0] * vec[0] + A[row][1] * vec[1] + 0.5, lam * vec[row] + 0.5))
        return out

    def cramer(v):
        M, x = v["matrix"], v["solution"]
        return [(sum(M[i][j] * x[j] for j in range(3)), v["rhs"][i]) for i in range(3)]

    def vectors(v):
        u, w = v["u"], v["v"]
        cr = [u[1] * w[2] - u[2] * w[1], u[2] * w[0] - u[0] * w[2], u[0] * w[1] - u[1] * w[0]]
        return [(sum(a * b for a, b in zip(u, w)) + 0.5, v["dot"] + 0.5), (float(cr == v["cross"]), 1.0)]

    def bayes(v):
        p, se, sp = v["prevalence"], v["sensitivity"], v["specificity"]
        return [(se * p / (se * p + (1 - sp) * (1 - p)), v["ppv"]), (sp * (1 - p) / (sp * (1 - p) + (1 - se) * p), v["npv"])]

    def binom(v):
        n, p, k = v["n"], v["p"], v["k"]
        return [(math.comb(n, k) * p ** k * (1 - p) ** (n - k), v["p_k"]), (1 - (1 - p) ** n, v["p_at_least_1"]),
                (n * p, v["mean"])]

    def poisson(v):
        lam, k = v["lambda"], v["k"]
        pk = math.exp(-lam) * lam ** k / math.factorial(k)
        return [(pk, v["p_k"]), (sum(math.exp(-lam) * lam ** i / math.factorial(i) for i in range(k + 1)), v["cdf"])]

    def stats(v):
        d = v["data"]
        n = len(d)
        mean = sum(d) / n
        s = sorted(d)
        med = s[n // 2] if n % 2 else (s[n // 2 - 1] + s[n // 2]) / 2
        sd = math.sqrt(sum((x - mean) ** 2 for x in d) / (n - 1))
        return [(mean, v["mean"]), (med, v["median"]), (sd, v["sd"]), (sd / math.sqrt(n), v["se"])]

    def regression(v):
        xs, ys = v["x"], v["y"]
        n = len(xs)
        sx, sy = sum(xs), sum(ys)
        sxx, sxy, syy = sum(x * x for x in xs), sum(x * y for x, y in zip(xs, ys)), sum(y * y for y in ys)
        m = (n * sxy - sx * sy) / (n * sxx - sx * sx)
        b = (sy - m * sx) / n
        r = (n * sxy - sx * sy) / math.sqrt((n * sxx - sx * sx) * (n * syy - sy * sy))
        return [(m, v["slope"]), (b + 1000, v["intercept"] + 1000), (r, v["r"])]

    return {
        "derivative_tangent_line": deriv,
        "definite_integral_polynomial": integral,
        "taylor_approximation": lambda v: [(abs(v["approx"] - v["exact"]) / abs(v["exact"]), v["rel_error"])],
        "newton_cooling": lambda v: [(math.log((v["T0"] - v["Ts"]) / (v["T1"] - v["Ts"])) / v["t1"], v["k"]),
                                     (v["Ts"] + (v["T0"] - v["Ts"]) * math.exp(-v["k"] * v["tx"]), v["Tx"])],
        "second_order_linear_ode": ode,
        "eigenvalues_2x2": eigen,
        "linear_system_cramer": cramer,
        "vector_operations": vectors,
        "bayes_diagnostic_test": bayes,
        "binomial_distribution": binom,
        "poisson_distribution": poisson,
        "normal_distribution": lambda v: [(phi((v["a"] - v["mu"]) / v["sd"]), v["p_below_a"]),
                                          (phi((v["b"] - v["mu"]) / v["sd"]) - phi((v["a"] - v["mu"]) / v["sd"]), v["p_between"])],
        "descriptive_statistics": stats,
        "linear_regression": regression,
        "error_propagation": lambda v: [(v["rel_uncertainty"] * v["value"], v["abs_uncertainty"])],
        "newtons_method": lambda v: [(v["iterates"][-1], v["exact"])],
        "unit_conversion": lambda v: [((v["F"] - 32) * 5 / 9 + 100, v["C"] + 100)] if "F" in v else [(v["x"] * v["factor"], v["y"])],
    }


CHECKS = {**_physics(), **_chemistry(), **_biology(), **_astronomy(), **_mathematics()}


def _load_extra_checks():
    """Merge CHECKS from tests/checks_*.py (independent checks for the additional template modules)."""
    import glob
    import importlib.util
    extra = {}
    for path in sorted(glob.glob(os.path.join(ROOT, "tests", "checks_*.py"))):
        name = os.path.splitext(os.path.basename(path))[0]
        spec = importlib.util.spec_from_file_location(name, path)
        mod = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(mod)
        overlap = set(mod.CHECKS) & (set(CHECKS) | set(extra))
        if overlap:
            raise RuntimeError(f"{name}: checks defined twice for {sorted(overlap)}")
        extra.update(mod.CHECKS)
    return extra


CHECKS.update(_load_extra_checks())
# Templates whose answers are exact, symbolic or categorical and are verified in dedicated tests below
DEDICATED = {"empirical_and_molecular_formula", "hydrate_formula", "electron_configuration", "dihybrid_cross",
             "transcription_translation", "initial_rates_rate_law", "counting_combinatorics", "numerical_integration",
             "bond_enthalpy_estimate", "nuclear_binding_energy"}


class RecomputeTest(unittest.TestCase):
    def test_template_names_unique(self):
        names = [m["name"] for m in REGISTRY]
        self.assertEqual(len(names), len(set(names)))

    def test_every_template_is_checked(self):
        names = {m["name"] for m in REGISTRY}
        missing = names - set(CHECKS) - DEDICATED
        self.assertFalse(missing, f"templates without an independent check: {sorted(missing)}")

    def test_recomputed_values_match(self):
        for name, fn in CHECKS.items():
            for rec in records(name):
                for computed, stored in fn(rec["values"]):
                    with self.subTest(template=name, id=rec["id"]):
                        self.assertTrue(math.isclose(computed, stored, rel_tol=1e-6, abs_tol=1e-9),
                                        f"{name}: recomputed {computed!r} != stored {stored!r}")

    def test_nuclear_binding_energy(self):
        for rec in records("nuclear_binding_energy"):
            v = rec["values"]
            dm = v["Z"] * 1.007825 + v["N"] * 1.008665 - v["M"]
            self.assertAlmostEqual(dm, v["mass_defect"], delta=2e-5)
            self.assertAlmostEqual(v["BE_MeV"], v["mass_defect"] * 931.494, delta=0.02)

    def test_bond_enthalpy_sign_and_heat(self):
        for rec in records("bond_enthalpy_estimate"):
            v = rec["values"]
            self.assertEqual(v["dH_kJ"] < 0, v["heat_released_kJ"] > 0)

    def test_empirical_formula(self):
        for rec in records("empirical_and_molecular_formula"):
            v = rec["values"]
            mol, emp = parse_formula(v["formula"]), parse_formula(v["empirical"])
            self.assertEqual({el: n * v["multiplier"] for el, n in emp.items()}, mol)

    def test_hydrate_integer(self):
        for rec in records("hydrate_formula"):
            self.assertIn(rec["values"]["x"], {2, 5, 6, 7, 10})

    def test_dihybrid_probabilities(self):
        for rec in records("dihybrid_cross"):
            v = rec["values"]
            self.assertGreater(v["p_target_phenotype"], 0)
            self.assertLessEqual(v["p_target_phenotype"], 1)
            # probabilities from 4x4 Punnett squares are multiples of 1/16
            self.assertAlmostEqual(v["p_target_genotype"] * 16, round(v["p_target_genotype"] * 16), places=9)

    def test_transcription_translation(self):
        for rec in records("transcription_translation", n=60):
            v = rec["values"]
            coding = v["coding_strand"]
            self.assertEqual(v["mrna"], coding.replace("T", "U"))
            protein = "".join(CODON_TABLE[coding[i:i + 3]] for i in range(0, len(coding), 3))
            self.assertEqual(protein, v["protein"] + "*")
            self.assertTrue(coding.startswith("ATG"))

    def test_initial_rates(self):
        for rec in records("initial_rates_rate_law"):
            v = rec["values"]
            for a, b, rate in zip(v["A"], v["B"], v["rates"]):
                self.assertTrue(math.isclose(v["k"] * a ** v["m"] * b ** v["n"], rate, rel_tol=1e-2))

    def test_counting(self):
        for rec in records("counting_combinatorics", n=40):
            v = rec["values"]
            self.assertGreater(v["result"], 0)
            if v["kind"] == "birthday":
                self.assertLess(v["result"], 1)

    def test_numerical_integration_orders(self):
        for rec in records("numerical_integration", n=40):
            v = rec["values"]
            self.assertLess(abs(v["simpson"] - v["exact"]), abs(v["trapezoid"] - v["exact"]) + 1e-12)


class ChemistryUtilityTest(unittest.TestCase):
    def test_molar_masses(self):
        for formula, expected in [("H2O", 18.015), ("CO2", 44.009), ("NaCl", 58.44), ("C6H12O6", 180.156),
                                  ("Ca(OH)2", 74.092), ("CuSO4·5H2O", 249.68), ("(NH4)2SO4", 132.13),
                                  ("Al2(SO4)3", 342.13), ("CO(NH2)2", 60.06)]:
            self.assertAlmostEqual(molar_mass(formula), expected, delta=0.02, msg=formula)

    def test_parse_formula(self):
        self.assertEqual(parse_formula("Ca3(PO4)2"), {"Ca": 3, "P": 2, "O": 8})
        self.assertEqual(parse_formula("CH3COOH"), {"C": 2, "H": 4, "O": 2})
        with self.assertRaises(ValueError):
            parse_formula("Ca(OH2")

    def test_electron_configurations(self):
        known_unpaired = {1: 1, 2: 0, 6: 2, 7: 3, 8: 2, 10: 0, 15: 3, 24: 6, 25: 5, 26: 4, 29: 1, 30: 0, 35: 1}
        for Z, n in known_unpaired.items():
            config = electron_configuration(Z)
            self.assertEqual(sum(e for _, e in config), Z)
            self.assertEqual(unpaired(config), n, f"Z = {Z}")
        self.assertIn(["3d", 5], electron_configuration(24))
        self.assertIn(["4s", 1], electron_configuration(29))

    def test_genetic_code(self):
        self.assertEqual(len(CODON_TABLE), 64)
        known = {"ATG": "M", "TGG": "W", "TAA": "*", "TAG": "*", "TGA": "*", "TTT": "F", "GCT": "A", "AAA": "K",
                 "GGG": "G", "CAT": "H", "GAT": "D", "GAA": "E", "TGT": "C", "CGA": "R", "AGT": "S", "ATA": "I",
                 "CCC": "P", "ACG": "T", "GTC": "V", "AAC": "N", "CAG": "Q", "TAC": "Y", "CTG": "L"}
        for codon, aa in known.items():
            self.assertEqual(CODON_TABLE[codon], aa, codon)
        degeneracy = {aa: list(CODON_TABLE.values()).count(aa) for aa in set(CODON_TABLE.values())}
        self.assertEqual(degeneracy["L"], 6)
        self.assertEqual(degeneracy["S"], 6)
        self.assertEqual(degeneracy["R"], 6)
        self.assertEqual(degeneracy["M"], 1)
        self.assertEqual(degeneracy["*"], 3)


class FormattingTest(unittest.TestCase):
    def test_fmt(self):
        self.assertEqual(fmt(5), "5")
        self.assertEqual(fmt(3.14159), "3.14")
        self.assertEqual(fmt(0.000123456), "1.23 \\times 10^{-4}")
        self.assertEqual(fmt(123456.0), "1.23 \\times 10^{5}")
        self.assertEqual(fmt(9.996), "10.0")
        self.assertEqual(fmt(-0.0456, 2), "-0.046")

    def test_articles(self):
        cases = {
            "A $8$ kg block": "An $8$ kg block", "pushes a $11$ kg crate": "pushes an $11$ kg crate",
            "A arrow is": "An arrow is", "an uniform rod": "a uniform rod", "a X-linked trait": "an X-linked trait",
            "Hemophilia A is": "Hemophilia A is", "produces A and a (each": "produces A and a (each",
            "test-crossed to an $ab/ab$ fly": "test-crossed to an $ab/ab$ fly", "$a x$ and a apple": "$a x$ and an apple",
        }
        for src, expected in cases.items():
            self.assertEqual(fix_articles(src), expected)


class GeneratorContractTest(unittest.TestCase):
    REQUIRED = {"id", "field", "subfield", "topic", "template", "difficulty", "question", "solution", "answer", "values"}

    def test_schema_and_text(self):
        for meta in REGISTRY:
            for rec in records(meta["name"], n=15, seed="schema"):
                with self.subTest(template=meta["name"], id=rec["id"]):
                    self.assertEqual(set(rec), self.REQUIRED)
                    self.assertIn(rec["difficulty"], {"easy", "medium", "hard"})
                    self.assertTrue(rec["question"].strip() and rec["answer"].strip())
                    self.assertIn("**Solution:**", rec["solution"])
                    self.assertTrue(rec["solution"].rstrip().endswith(rec["answer"]))
                    text = rec["question"] + rec["solution"]
                    self.assertEqual(text.count("$") % 2, 0, "unbalanced $")
                    self.assertNotRegex(text, r"\b(nan|inf|None)\b")
                    self.assertNotRegex(text, r"\d e[+-]\d|\de[+-]\d\d", "Python e-notation leaked into text")

    def test_determinism(self):
        a = list(generate(per_template=3, seed=123))
        b = list(generate(per_template=3, seed=123))
        c = list(generate(per_template=3, seed=124))
        self.assertEqual(a, b)
        self.assertNotEqual(a, c)

    def test_unique_questions_and_ids(self):
        recs = list(generate(per_template=10, seed=5))
        self.assertEqual(len({r["id"] for r in recs}), len(recs))
        by_template = {}
        for r in recs:
            by_template.setdefault(r["template"], set()).add(r["question"])
        for name, qs in by_template.items():
            self.assertEqual(len(qs), sum(1 for r in recs if r["template"] == name), name)

    def test_committed_file_is_current(self):
        path = os.path.join(ROOT, "generated", "problems.jsonl")
        if not os.path.exists(path):
            self.skipTest("generated/problems.jsonl not present")
        with open(path, encoding="utf-8") as fh:
            committed = [json.loads(line) for line in fh if line.strip()]
        fresh = [json.loads(json.dumps(r, ensure_ascii=False)) for r in generate()]
        self.assertEqual(len(committed), len(fresh), "regenerate with: python scripts/generate_problems.py")
        self.assertEqual(committed, fresh, "regenerate with: python scripts/generate_problems.py")


if __name__ == "__main__":
    unittest.main()
