"""Astronomy and astrophysics problem templates."""

import math

from .common import (
    AU, C, G, L_SUN, LY, M_SUN, PC, R_SUN, SIGMA_SB, T_SUN, WIEN_B, fmt, nice, pick, q, sig, template,
)

ASTRO = "Astronomy"
H0 = 70.0  # km/s/Mpc, a round value between the CMB-based (~67) and distance-ladder (~73) measurements
R_EARTH_KM = 6371.0
R_JUP_KM = 69911.0

# ---------------------------------------------------------------------------
# Distances and brightness
# ---------------------------------------------------------------------------

STARS_PARALLAX = [  # name, parallax (arcsec)
    ("Proxima Centauri", 0.7685), ("Sirius", 0.3792), ("Vega", 0.1301), ("Altair", 0.1946),
    ("Procyon", 0.2850), ("Arcturus", 0.0887), ("Barnard's Star", 0.5470), ("Aldebaran", 0.0491),
    ("Polaris", 0.0075), ("Betelgeuse", 0.0060),
]


@template("stellar_parallax", ASTRO, "Stellar Astronomy", "Parallax", "easy")
def stellar_parallax(rng):
    if rng.random() < 0.5:
        name, p = pick(rng, STARS_PARALLAX)
    else:
        name, p = "a star", sig(rng.uniform(0.002, 0.5), 3)
    d_pc = 1 / p
    d_ly = d_pc * PC / LY
    d_km = d_pc * PC / 1000
    question = (
        f"The measured annual parallax of {name} is ${fmt(p, 4)}''$. How far away is it in parsecs, light-years and "
        "kilometers?"
    )
    steps = [
        "By definition, a star with a parallax of 1 arcsecond is 1 parsec away: $d\\,(\\text{pc}) = 1/p\\,('')$.",
        f"$d = 1/{fmt(p, 4)} = {fmt(d_pc)}$ pc.",
        f"1 pc = 3.26 ly: $d = {fmt(d_ly)}$ ly.",
        f"1 pc = $3.086\\times10^{{13}}$ km: $d = {fmt(d_km)}$ km.",
        "Light from the star takes about " + fmt(d_ly) + " years to reach us. Ground-based parallaxes are limited to "
        "nearby stars; the Gaia mission measures parallaxes down to tens of microarcseconds.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"${fmt(d_pc)}$ pc $= {fmt(d_ly)}$ ly $= {fmt(d_km)}$ km",
            "values": {"parallax": p, "d_pc": d_pc, "d_ly": d_ly}}


@template("distance_modulus", ASTRO, "Stellar Astronomy", "Magnitudes", "medium")
def distance_modulus(rng):
    M = nice(rng, -8.0, 12.0, 0.1)
    if rng.random() < 0.5:
        d = sig(10 ** rng.uniform(0.5, 4.5), 3)
        m = M + 5 * math.log10(d / 10)
        question = (
            f"A star with absolute magnitude $M = {M:.1f}$ lies at a distance of "
            f"{q(d, 'pc')}. What is its apparent magnitude? Could it be seen with the naked eye (limit ≈ 6)?"
        )
        steps = [
            "Distance modulus: $m - M = 5\\log_{10}(d/10\\text{ pc})$.",
            f"$m = {M:.1f} + 5\\log_{{10}}({fmt(d)}/10) = {M:.1f} + {5 * math.log10(d / 10):.2f} = {m:.2f}$.",
            f"Since {'$m < 6$, it is visible to the naked eye' if m < 6 else '$m > 6$, it needs binoculars or a telescope'} "
            "(larger magnitudes are fainter).",
        ]
        answer = f"$m = {m:.2f}$ ({'naked-eye' if m < 6 else 'not naked-eye'})"
        values = {"M": M, "d_pc": d, "m": m}
    else:
        m = nice(rng, -1.0, 15.0, 0.1)
        d = 10 ** ((m - M + 5) / 5)
        question = (
            f"A star has apparent magnitude $m = {m:.1f}$ and, from its spectral type, an estimated absolute magnitude "
            f"$M = {M:.1f}$. Ignoring interstellar extinction, how far away is it?"
        )
        steps = [
            "Rearrange the distance modulus: $d = 10^{(m - M + 5)/5}$ pc.",
            f"$m - M = {m:.1f} - ({M:.1f}) = {m - M:.1f}$.",
            f"$d = 10^{{({m - M:.1f} + 5)/5}} = 10^{{{(m - M + 5) / 5:.2f}}} = {fmt(d)}$ pc $= {fmt(d * 3.2616)}$ ly.",
            "Interstellar dust would make the star look fainter, so neglecting it overestimates the distance.",
        ]
        answer = f"$d \\approx {fmt(d)}$ pc"
        values = {"m": m, "M": M, "d_pc": d}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("magnitude_flux_ratio", ASTRO, "Stellar Astronomy", "Magnitudes", "easy")
def magnitude_flux_ratio(rng):
    pairs = [("Sirius", -1.46), ("Vega", 0.03), ("Polaris", 1.98), ("Betelgeuse", 0.50), ("Rigel", 0.13),
             ("Deneb", 1.25), ("Antares", 1.06), ("the faintest naked-eye stars", 6.0), ("Pluto", 14.4),
             ("Proxima Centauri", 11.13), ("the full Moon", -12.7), ("Venus at its brightest", -4.6)]
    (n1, m1), (n2, m2) = rng.sample(pairs, 2)
    if m1 > m2:
        (n1, m1), (n2, m2) = (n2, m2), (n1, m1)
    dm = m2 - m1
    ratio = 10 ** (0.4 * dm)
    question = (
        f"{n1[0].upper() + n1[1:]} has apparent magnitude {m1:+.2f} and {n2} has {m2:+.2f}. How many times brighter "
        f"does {n1} appear?"
    )
    steps = [
        "A difference of 5 magnitudes is a factor of exactly 100 in flux, so $\\frac{F_1}{F_2} = 10^{0.4(m_2 - m_1)}$.",
        f"$m_2 - m_1 = {m2:+.2f} - ({m1:+.2f}) = {dm:.2f}$.",
        f"$\\frac{{F_1}}{{F_2}} = 10^{{0.4 \\times {dm:.2f}}} = {fmt(ratio)}$.",
    ]
    return {"question": question, "steps": steps, "answer": f"about ${fmt(ratio)}$ times brighter",
            "values": {"m1": m1, "m2": m2, "flux_ratio": ratio}}


@template("inverse_square_irradiance", ASTRO, "Planetary Science", "Solar irradiance", "easy")
def inverse_square_irradiance(rng):
    planet, a = pick(rng, [("Mercury", 0.387), ("Venus", 0.723), ("Mars", 1.524), ("Jupiter", 5.203),
                           ("Saturn", 9.537), ("Uranus", 19.19), ("Neptune", 30.07), ("the asteroid Ceres", 2.77),
                           ("Pluto (average)", 39.5)])
    if rng.random() < 0.5:
        planet, a = "a spacecraft", sig(10 ** rng.uniform(-0.6, 1.8), 3)
    S0 = 1361.0
    S = S0 / a ** 2
    question = (
        f"The solar irradiance at Earth (1 AU) is about 1361 W/m². What is it at {planet}, which orbits at an average "
        f"of {fmt(a, 4)} AU? How does that compare with Earth?" if planet != "a spacecraft" else
        f"The solar irradiance at Earth (1 AU) is about 1361 W/m². What is it at a spacecraft {fmt(a, 4)} AU from the "
        "Sun? How does that compare with Earth?"
    )
    steps = [
        "Sunlight spreads over a sphere of area $4\\pi d^2$, so irradiance falls as $1/d^2$.",
        f"$S = 1361 \\times (1/{fmt(a, 4)})^2 = {fmt(S)}$ W/m².",
        f"Ratio to Earth: ${fmt(S / S0)}$ (i.e. {'more' if S > S0 else 'less'} than at Earth by a factor of "
        f"{fmt(max(S, S0) / min(S, S0))}).",
    ]
    return {"question": question, "steps": steps, "answer": f"$S \\approx {fmt(S)}$ W/m² (${fmt(S / S0)}$× Earth's)",
            "values": {"a_AU": a, "S": S}}


@template("light_travel_time", ASTRO, "Planetary Science", "Light travel time", "easy")
def light_travel_time(rng):
    obj, d_m, label = pick(rng, [
        ("the Moon", 3.844e8, "384,400 km"), ("the Sun", AU, "1 AU"),
        ("Mars at closest approach", 5.46e10, "54.6 million km"), ("Mars at its farthest", 4.01e11, "401 million km"),
        ("Jupiter at opposition", 7.785e11 - AU, "about 629 million km"),
        ("Neptune at opposition", 4.5e12 - AU, "about 4.35 billion km"),
        ("Voyager 1 (in 2025)", 2.5e13, "about 25 billion km"), ("Proxima Centauri", 4.0e16, "4.0 × 10¹³ km"),
    ])
    if rng.random() < 0.5:
        d_km = nice(rng, 55, 400, 1) * 1e6
        obj, d_m, label = "Mars", d_km * 1000, f"{d_km / 1e6:.0f} million km (its distance on a particular date)"
    t = d_m / C
    question = (
        f"How long does light (or a radio signal) take to travel from Earth to {obj}, a distance of {label}? "
        "What does this imply for controlling a spacecraft there?"
    )
    unit = "s" if t < 120 else "min" if t < 7200 else "h" if t < 3 * 86400 else "yr"
    conv = {"s": 1, "min": 60, "h": 3600, "yr": 3.156e7}[unit]
    steps = [
        f"$t = d/c = \\frac{{{fmt(d_m)}\\text{{ m}}}}{{2.998\\times10^8\\text{{ m/s}}}} = {fmt(t)}$ s.",
        f"In convenient units: ${fmt(t / conv)}$ {unit}.",
        f"A command and its confirmation need a round trip of ${fmt(2 * t / conv)}$ {unit}, so distant spacecraft must "
        "operate autonomously rather than be steered in real time.",
    ]
    return {"question": question, "steps": steps, "answer": f"${fmt(t / conv)}$ {unit} one way",
            "values": {"distance_m": d_m, "t_s": t}}


@template("angular_size", ASTRO, "Observational Astronomy", "Angular size", "easy")
def angular_size(rng):
    obj, D_km, D_txt, d_lo, d_hi = pick(rng, [
        ("the Moon", 3474.8, "3474.8 km", 356500, 406700),
        ("the Sun", 1.3927e6, "1.3927 million km", 1.471e8, 1.521e8),
        ("Jupiter", 139820, "139,820 km", 5.88e8, 9.68e8), ("Mars", 6779, "6779 km", 5.46e7, 4.01e8),
        ("the International Space Station", 0.109, "about 109 m", 410, 1500),
    ])
    d = sig(rng.uniform(d_lo, d_hi), 3)
    theta_rad = D_km / d
    theta_arcsec = theta_rad * 206265
    question = (
        f"What is the angular diameter of {obj} (diameter {D_txt}) seen from a distance of {q(d, 'km')}? "
        "Give the answer in arcseconds (and in degrees if large)."
    )
    steps = [
        "Small-angle formula: $\\theta\\,(\\text{rad}) = D/d$; 1 rad = 206 265″.",
        f"$\\theta = {D_km:g}\\text{{ km}}/{fmt(d)}\\text{{ km}} = {fmt(theta_rad)}$ rad." if D_km < 1e5 else
        f"$\\theta = {fmt(D_km, 5)}\\text{{ km}}/{fmt(d)}\\text{{ km}} = {fmt(theta_rad)}$ rad.",
        f"$\\theta = {fmt(theta_rad)} \\times 206265 = {fmt(theta_arcsec)}''$ $= {fmt(theta_arcsec / 60)}'$ $= {fmt(theta_arcsec / 3600)}°$.",
    ]
    if "Moon" in obj or "Sun" in obj:
        steps.append("The Moon and Sun both subtend about 0.5°, which is why total solar eclipses are possible.")
    return {"question": question, "steps": steps, "answer": f"$\\theta \\approx {fmt(theta_arcsec)}''$ "
                                                              f"(${fmt(theta_arcsec / 3600)}°$)",
            "values": {"D_km": D_km, "d_km": d, "theta_arcsec": theta_arcsec}}


# ---------------------------------------------------------------------------
# Stars
# ---------------------------------------------------------------------------

STAR_TEMPS = [("the Sun", 5772), ("Betelgeuse", 3600), ("Rigel", 12100), ("Sirius A", 9940), ("Vega", 9600),
              ("Proxima Centauri", 3040), ("Arcturus", 4290), ("Spica", 22400), ("Antares", 3400),
              ("Procyon A", 6530)]


def _color(T):
    if T < 3700:
        return "red"
    if T < 5200:
        return "orange"
    if T < 6000:
        return "yellow"
    if T < 7500:
        return "yellow-white"
    if T < 10000:
        return "white"
    return "blue-white"


@template("wien_stellar_temperature", ASTRO, "Stellar Astronomy", "Blackbody radiation", "easy")
def wien_stellar_temperature(rng):
    name, T = pick(rng, STAR_TEMPS)
    if rng.random() < 0.5:
        name, T = "a star", nice(rng, 2500, 35000, 100)
    lam = WIEN_B / T
    lam_nm = lam * 1e9
    region = "ultraviolet" if lam_nm < 380 else ("visible" if lam_nm <= 750 else "near-infrared")
    if rng.random() < 0.5:
        question = (
            f"The surface temperature of {name} is about {T} K. At what wavelength does its blackbody spectrum peak, and "
            "what color does the star appear?"
        )
        steps = [
            "Wien's displacement law: $\\lambda_{max} = b/T$ with $b = 2.898\\times10^{-3}$ m·K.",
            f"$\\lambda_{{max}} = 2.898\\times10^{{-3}}/{T} = {fmt(lam)}$ m $= {fmt(lam_nm)}$ nm ({region}).",
            f"A star at {T} K looks {_color(T)}: the visible light is weighted toward "
            + ("red wavelengths." if T < 4500 else "blue wavelengths." if T > 7500 else "the middle of the spectrum.")
            + " (The Sun peaks in the green yet looks white, because it emits strongly across the whole visible band.)",
        ]
        answer = f"$\\lambda_{{max}} = {fmt(lam_nm)}$ nm; appears {_color(T)}"
        values = {"T": T, "lambda_max_nm": lam_nm}
    else:
        lam_nm_r = sig(lam_nm, 3)
        T_calc = WIEN_B / (lam_nm_r * 1e-9)
        question = (
            f"The thermal spectrum of a star peaks at {q(lam_nm_r, 'nm')}. Estimate its surface temperature and color."
        )
        steps = [
            "Wien's law rearranged: $T = b/\\lambda_{max}$.",
            f"$T = 2.898\\times10^{{-3}}/({fmt(lam_nm_r)}\\times10^{{-9}}) = {fmt(T_calc)}$ K.",
            f"At about {fmt(T_calc)} K the star appears {_color(T_calc)}.",
        ]
        answer = f"$T \\approx {fmt(T_calc)}$ K ({_color(T_calc)})"
        values = {"lambda_max_nm": lam_nm_r, "T": T_calc}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


STAR_LT = [  # name, L/Lsun, T (K)
    ("Sirius A", 25.4, 9940), ("Vega", 40.1, 9600), ("Betelgeuse", 1.0e5, 3600), ("Rigel", 1.2e5, 12100),
    ("Arcturus", 170, 4290), ("Proxima Centauri", 0.0017, 3040), ("Procyon A", 6.9, 6530),
    ("Sirius B (a white dwarf)", 0.025, 25000), ("Antares", 7.5e4, 3400), ("Aldebaran", 440, 3900),
]


@template("stellar_radius_luminosity", ASTRO, "Stellar Astronomy", "Stefan–Boltzmann law", "medium")
def stellar_radius_luminosity(rng):
    name, L, T = pick(rng, STAR_LT)
    if rng.random() < 0.6:
        name, L, T = "a star", sig(10 ** rng.uniform(-3, 5.5), 2), nice(rng, 2800, 30000, 100)
    R = math.sqrt(L) * (T_SUN / T) ** 2
    R_m = R * R_SUN
    question = (
        f"{name[0].upper() + name[1:]} has a luminosity of {fmt(L)} $L_\\odot$ and a surface temperature of {T} K. "
        f"Estimate its radius in solar radii ($T_\\odot = {T_SUN:.0f}$ K)."
    )
    steps = [
        "Stefan–Boltzmann law for a spherical star: $L = 4\\pi R^2\\sigma T^4$.",
        "Divide by the same expression for the Sun: $\\frac{R}{R_\\odot} = \\sqrt{\\frac{L}{L_\\odot}}\\left(\\frac{T_\\odot}{T}\\right)^2$.",
        f"$\\frac{{R}}{{R_\\odot}} = \\sqrt{{{fmt(L)}}}\\left(\\frac{{{T_SUN:.0f}}}{{{T}}}\\right)^2 = ({fmt(math.sqrt(L))})({fmt((T_SUN / T) ** 2)}) = {fmt(R)}$.",
        f"That is $R \\approx {fmt(R_m)}$ m ({fmt(R_m / AU)} AU). "
        + ("A cool star can only be this luminous if it is enormous — a supergiant or giant." if R > 10 else
           "A hot but faint star must be tiny — this is how white dwarfs were recognized." if R < 0.1 else
           "This is comparable to the Sun."),
    ]
    return {"question": question, "steps": steps, "answer": f"$R \\approx {fmt(R)}\\,R_\\odot$",
            "values": {"L": L, "T": T, "R_solar": R}}


@template("main_sequence_lifetime", ASTRO, "Stellar Astronomy", "Stellar evolution", "medium")
def main_sequence_lifetime(rng):
    M = pick(rng, [0.1, 0.2, 0.3, 0.5, 0.8, 1.0, 1.5, 2.0, 3.0, 5.0, 8.0, 10.0, 15.0, 20.0, 40.0])
    if rng.random() < 0.5:
        M = sig(10 ** rng.uniform(-1, 1.6), 2)
    L = M ** 3.5
    t = 1e10 * M ** -2.5
    fate = ("a white dwarf (after a red-giant phase)" if M < 8 else
            "a core-collapse supernova leaving a neutron star or black hole")
    question = (
        f"Using the approximate mass–luminosity relation $L \\propto M^{{3.5}}$ and a solar main-sequence lifetime of "
        f"$10^{{10}}$ years, estimate the luminosity and main-sequence lifetime of a {M} $M_\\odot$ star. What is its "
        "likely fate?"
    )
    steps = [
        f"Luminosity: $L/L_\\odot = ({M})^{{3.5}} = {fmt(L)}$.",
        "Lifetime ∝ fuel/burn rate ∝ $M/L = M^{-2.5}$, so $t = 10^{10}\\,(M/M_\\odot)^{-2.5}$ yr.",
        f"$t = 10^{{10}} \\times ({M})^{{-2.5}} = {fmt(t)}$ yr.",
        f"Fate: {fate}. "
        + ("No star this light has yet left the main sequence — the universe is only 13.8 billion years old."
           if t > 1.38e10 else ""),
    ]
    return {"question": question, "steps": steps, "answer": f"$L \\approx {fmt(L)}\\,L_\\odot$; lifetime ≈ ${fmt(t)}$ yr",
            "values": {"M": M, "L": L, "t_years": t}}


@template("schwarzschild_radius", ASTRO, "Relativistic Astrophysics", "Black holes", "easy")
def schwarzschild_radius(rng):
    name, M_solar = pick(rng, [
        ("a 10 solar-mass stellar black hole", 10.0), ("Cygnus X-1 (≈21 solar masses)", 21.0),
        ("Sagittarius A* (4.3 million solar masses)", 4.3e6), ("M87* (6.5 billion solar masses)", 6.5e9),
        ("a black hole with the mass of the Sun", 1.0), ("a black hole with the mass of Earth", 3.003e-6),
        ("GW150914's final black hole (≈62 solar masses)", 62.0),
    ])
    if rng.random() < 0.6:
        M_solar = sig(10 ** rng.uniform(0.5, 10), 2)
        name = f"a black hole of {fmt(M_solar, 2)} solar masses"
    M = M_solar * M_SUN
    Rs = 2 * G * M / C ** 2
    rho = M / (4 / 3 * math.pi * Rs ** 3)
    question = (
        f"Calculate the Schwarzschild radius of {name}. What is the mean density inside that radius?"
    )
    steps = [
        "$R_s = \\frac{2GM}{c^2}$ — the radius of the event horizon of a non-rotating black hole.",
        f"$M = {fmt(M_solar)} \\times 1.989\\times10^{{30}} = {fmt(M)}$ kg.",
        f"$R_s = \\frac{{2(6.674\\times10^{{-11}})({fmt(M)})}}{{(2.998\\times10^8)^2}} = {fmt(Rs)}$ m.",
        f"Mean density $\\rho = M/(\\tfrac43\\pi R_s^3) = {fmt(rho)}$ kg/m³ — "
        + ("larger than nuclear density (~2×10¹⁷ kg/m³)." if rho > 2e17 else
           "less than that of water: supermassive black holes need not be dense on average." if rho < 1000 else
           "denser than any ordinary matter but below nuclear density."),
    ]
    return {"question": question, "steps": steps, "answer": f"$R_s = {fmt(Rs)}$ m; $\\rho \\approx {fmt(rho)}$ kg/m³",
            "values": {"M_solar": M_solar, "Rs_m": Rs, "density": rho}}


# ---------------------------------------------------------------------------
# Orbits and planets
# ---------------------------------------------------------------------------


@template("kepler_third_law", ASTRO, "Planetary Science", "Kepler's laws", "medium")
def kepler_third_law(rng):
    star_M = pick(rng, [1.0, 1.0, 0.12, 0.5, 0.8, 1.2, 2.0])
    if rng.random() < 0.5:
        P_days = sig(10 ** rng.uniform(0, 3.3), 3)
        P = P_days / 365.25
        a = (star_M * P ** 2) ** (1 / 3)
        question = (
            f"An exoplanet orbits a star of {fmt(star_M, 2)} solar masses with a period of {q(P_days, 'days')}. Find the "
            "semi-major axis of its orbit in AU (assume the planet's mass is negligible)."
        )
        steps = [
            "Kepler's third law in solar-system units: $P^2 = a^3/M$ (P in years, a in AU, M in solar masses).",
            f"$P = {fmt(P_days)}/365.25 = {fmt(P)}$ yr.",
            f"$a = (MP^2)^{{1/3}} = ({fmt(star_M, 2)} \\times {fmt(P)}^2)^{{1/3}} = {fmt(a)}$ AU.",
            f"For comparison, Mercury orbits at 0.387 AU; this planet is {'closer to its star than Mercury is to the Sun' if a < 0.387 else 'farther out than Mercury'}.",
        ]
        answer = f"$a \\approx {fmt(a)}$ AU"
        values = {"M_star": star_M, "P_days": P_days, "a_AU": a}
    else:
        a = sig(10 ** rng.uniform(-1.3, 1.7), 3)
        P = math.sqrt(a ** 3 / star_M)
        question = (
            f"A planet orbits a star of {fmt(star_M, 2)} solar masses at an average distance of {q(a, 'AU')}. What is its "
            "orbital period?"
        )
        steps = [
            "Kepler's third law: $P^2 = a^3/M$ (years, AU, solar masses).",
            f"$P = \\sqrt{{{fmt(a)}^3/{fmt(star_M, 2)}}} = {fmt(P)}$ yr $= {fmt(P * 365.25)}$ days.",
        ]
        answer = f"$P \\approx {fmt(P)}$ yr ({fmt(P * 365.25)} days)"
        values = {"M_star": star_M, "a_AU": a, "P_years": P}
    return {"question": question, "steps": steps, "answer": answer, "values": values}


@template("binary_star_mass", ASTRO, "Stellar Astronomy", "Binary stars", "hard")
def binary_star_mass(rng):
    p = sig(rng.uniform(0.05, 0.6), 3)
    a_arc = sig(rng.uniform(0.5, 10.0), 3)
    a_AU = a_arc / p
    Mtot = nice(rng, 0.5, 6.0, 0.1)
    P = sig(math.sqrt(a_AU ** 3 / Mtot), 3)
    M_calc = a_AU ** 3 / P ** 2
    question = (
        f"A visual binary has an angular semi-major axis of ${fmt(a_arc)}''$ and a parallax of ${fmt(p)}''$. The orbital "
        f"period is {q(P, 'years')}. Find the total mass of the system in solar masses."
    )
    steps = [
        f"Physical semi-major axis: $a\\,(\\text{{AU}}) = \\alpha''/p'' = {fmt(a_arc)}/{fmt(p)} = {fmt(a_AU)}$ AU "
        "(an angle of 1″ at 1 pc corresponds to 1 AU).",
        "Kepler's third law for a binary: $M_1 + M_2 = a^3/P^2$ (solar masses, AU, years).",
        f"$M_1 + M_2 = \\frac{{({fmt(a_AU)})^3}}{{({fmt(P)})^2}} = {fmt(M_calc)}\\,M_\\odot$.",
        "Measuring each star's distance from the center of mass would then give the individual masses — binaries are "
        "our main source of directly measured stellar masses.",
    ]
    return {"question": question, "steps": steps, "answer": f"$M_1 + M_2 \\approx {fmt(M_calc)}\\,M_\\odot$",
            "values": {"a_arcsec": a_arc, "parallax": p, "P_years": P, "a_AU": a_AU, "M_total": M_calc}}


PLANETS = {"Mercury": 0.2408, "Venus": 0.6152, "Mars": 1.8809, "Jupiter": 11.862, "Saturn": 29.457,
           "Uranus": 84.02, "Neptune": 164.8}


@template("synodic_period", ASTRO, "Planetary Science", "Planetary motion", "medium")
def synodic_period(rng):
    name = pick(rng, list(PLANETS))
    P = PLANETS[name]
    if rng.random() < 0.5:
        name, P = "An asteroid", sig(10 ** rng.uniform(-0.5, 1.5), 3)
        if abs(P - 1) < 0.05:
            P = 1.5
    S = 1 / abs(1 - 1 / P)
    inner = P < 1
    question = (
        f"{name} has a sidereal orbital period of {P:g} years. How often does it return to the same position "
        f"relative to the Sun as seen from Earth (its synodic period) — e.g. from one "
        f"{'inferior conjunction' if inner else 'opposition'} to the next?"
    )
    steps = [
        "The angular speeds subtract: $\\frac{1}{S} = \\left|\\frac{1}{P_\\oplus} - \\frac{1}{P}\\right|$ with $P_\\oplus = 1$ yr.",
        f"$\\frac{{1}}{{S}} = \\left|1 - \\frac{{1}}{{{P:g}}}\\right| = {fmt(1 / S, 4)}$ yr⁻¹.",
        f"$S = {fmt(S, 4)}$ yr $= {fmt(S * 365.25, 4)}$ days.",
    ]
    if not inner and P > 10:
        steps.append("For distant planets $S$ is only slightly longer than a year: Earth laps them about once a year.")
    if name == "Mars":
        steps.append("This is why Mars missions launch in windows roughly every 26 months.")
    return {"question": question, "steps": steps, "answer": f"$S \\approx {fmt(S * 365.25, 4)}$ days",
            "values": {"P": P, "S_years": S}}


@template("planet_equilibrium_temperature", ASTRO, "Planetary Science", "Planetary climate", "medium")
def planet_equilibrium_temperature(rng):
    if rng.random() < 0.6:
        name, a, A, T_actual = pick(rng, [("Earth", 1.0, 0.30, 288), ("Mars", 1.524, 0.25, 210),
                                          ("Venus", 0.723, 0.76, 737), ("Jupiter", 5.203, 0.34, 165),
                                          ("the Moon", 1.0, 0.11, 250)])
        T_star, R_star = T_SUN, 1.0
        host = "the Sun"
    else:
        name = "an exoplanet"
        T_star = nice(rng, 2800, 7000, 100)
        R_star = sig((T_star / T_SUN) ** 1.8 * rng.uniform(0.8, 1.2), 2)  # rough main-sequence trend
        a = sig(rng.uniform(0.01, 3.0), 3)
        A = nice(rng, 0.0, 0.6, 0.05)
        T_actual = None
        host = f"a star with $T = {T_star}$ K and $R = {fmt(R_star)}\\,R_\\odot$"
    Teq = T_star * math.sqrt(R_star * R_SUN / (2 * a * AU)) * (1 - A) ** 0.25
    question = (
        f"Estimate the equilibrium temperature of {name}{' that' if name == 'an exoplanet' else ', which'} orbits {host} at {q(a, 'AU', 4)} with a Bond albedo of "
        f"{fmt(A, 2)}. Assume the absorbed sunlight is re-radiated from the whole surface."
    )
    steps = [
        "Energy balance: absorbed $= \\pi R_p^2(1 - A)\\frac{L_*}{4\\pi a^2}$, emitted $= 4\\pi R_p^2\\sigma T_{eq}^4$.",
        "With $L_* = 4\\pi R_*^2\\sigma T_*^4$ this gives $T_{eq} = T_*\\sqrt{\\frac{R_*}{2a}}(1 - A)^{1/4}$.",
        f"$R_*/a = \\frac{{{fmt(R_star * R_SUN)}\\text{{ m}}}}{{{fmt(a * AU)}\\text{{ m}}}} = {fmt(R_star * R_SUN / (a * AU))}$.",
        f"$T_{{eq}} = {T_star:.0f}\\sqrt{{{fmt(R_star * R_SUN / (a * AU))}/2}}\\,(1 - {fmt(A, 2)})^{{1/4}} = {Teq:.0f}$ K "
        f"({Teq - 273.15:.0f} °C).",
    ]
    if T_actual:
        diff = T_actual - Teq
        steps.append(
            f"The observed mean surface temperature is about {T_actual} K. "
            + (f"The {diff:.0f} K difference is due to the greenhouse effect." if diff > 20 else
               "Internal heat and the deep atmosphere also matter for giant planets." if name == "Jupiter" else
               "The agreement is reasonable for a body with little atmosphere.")
        )
    return {"question": question, "steps": steps, "answer": f"$T_{{eq}} \\approx {Teq:.0f}$ K",
            "values": {"T_star": T_star, "R_star": R_star, "a_AU": a, "albedo": A, "T_eq": Teq}}


@template("exoplanet_transit_depth", ASTRO, "Planetary Science", "Exoplanets", "easy")
def exoplanet_transit_depth(rng):
    R_star = nice(rng, 0.1, 1.8, 0.05)
    depth_pct = sig(10 ** rng.uniform(-2.3, 0.5), 2)
    ratio = math.sqrt(depth_pct / 100)
    Rp_km = ratio * R_star * R_SUN / 1000
    question = (
        f"During a transit, a star of radius {fmt(R_star)} $R_\\odot$ dims by {fmt(depth_pct, 2)}%. Estimate the radius of "
        "the planet in Earth radii and in Jupiter radii."
    )
    steps = [
        "The fractional dimming equals the fraction of the stellar disk blocked: $\\delta = (R_p/R_*)^2$.",
        f"$R_p/R_* = \\sqrt{{{fmt(depth_pct / 100, 2)}}} = {fmt(ratio)}$.",
        f"$R_p = {fmt(ratio)} \\times {fmt(R_star)} \\times 6.957\\times10^5\\text{{ km}} = {fmt(Rp_km)}$ km.",
        f"That is ${fmt(Rp_km / R_EARTH_KM)}\\,R_\\oplus$ or ${fmt(Rp_km / R_JUP_KM)}\\,R_J$ — "
        + ("a gas giant." if Rp_km / R_EARTH_KM > 6 else "a Neptune-size planet." if Rp_km / R_EARTH_KM > 2.5 else
           "a rocky or super-Earth-size planet."),
    ]
    return {"question": question, "steps": steps,
            "answer": f"$R_p \\approx {fmt(Rp_km / R_EARTH_KM)}\\,R_\\oplus$ (${fmt(Rp_km / R_JUP_KM)}\\,R_J$)",
            "values": {"R_star": R_star, "depth_percent": depth_pct, "Rp_km": Rp_km, "Rp_earth": Rp_km / R_EARTH_KM}}


# ---------------------------------------------------------------------------
# Galaxies and cosmology
# ---------------------------------------------------------------------------


@template("hubble_law_redshift", ASTRO, "Cosmology", "Hubble's law", "easy")
def hubble_law_redshift(rng):
    line, lam0 = pick(rng, [("hydrogen-alpha", 656.3), ("hydrogen-beta", 486.1), ("calcium K", 393.4),
                            ("calcium H", 396.8), ("sodium D", 589.0)])
    z = sig(rng.uniform(0.002, 0.08), 2)
    lam = round(lam0 * (1 + z), 1)
    z_calc = (lam - lam0) / lam0
    v = z_calc * C / 1000
    d = v / H0
    question = (
        f"In a galaxy's spectrum the {line} line (rest wavelength {fmt(lam0, 4)} nm) is observed at {fmt(lam, 4)} nm. "
        f"Find the redshift, the recession velocity and the distance (take $H_0 = {H0:.0f}$ km/s/Mpc)."
    )
    steps = [
        f"$z = \\frac{{\\lambda_{{obs}} - \\lambda_0}}{{\\lambda_0}} = \\frac{{{fmt(lam, 4)} - {fmt(lam0, 4)}}}{{{fmt(lam0, 4)}}} = {fmt(z_calc)}$.",
        f"For $z \\ll 1$, $v \\approx cz = (2.998\\times10^5)({fmt(z_calc)}) = {fmt(v)}$ km/s.",
        f"Hubble's law: $d = v/H_0 = {fmt(v)}/{H0:.0f} = {fmt(d)}$ Mpc $\\approx {fmt(d * 3.2616)}$ million light-years.",
        "The redshift reflects the expansion of space; the light we see left the galaxy about "
        f"{fmt(d * 3.2616)} million years ago.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$z = {fmt(z_calc)}$; $v \\approx {fmt(v)}$ km/s; $d \\approx {fmt(d)}$ Mpc",
            "values": {"lambda0": lam0, "lambda_obs": lam, "z": z_calc, "v_kms": v, "d_Mpc": d}}


@template("cosmic_scale_factor", ASTRO, "Cosmology", "Expansion of the universe", "easy")
def cosmic_scale_factor(rng):
    z = pick(rng, [0.5, 1.0, 2.0, 3.0, 6.0, 10.0, 14.3, 1100.0, 0.1, 4.5])
    if rng.random() < 0.6:
        z = sig(10 ** rng.uniform(-1.5, 1.2), 2)
    a = 1 / (1 + z)
    T = 2.725 * (1 + z)
    obj = {1100.0: "the cosmic microwave background (last scattering)", 14.3: "one of the most distant known galaxies"}.get(
        z, "a distant quasar or galaxy")
    question = (
        f"Light from {obj} has redshift $z = {fmt(z)}$. By what factor has the universe expanded since the light was "
        "emitted, and what was the temperature of the cosmic background radiation at that time "
        "($T_0 = 2.725$ K today)?"
    )
    steps = [
        "Wavelengths stretch with the expansion: $1 + z = \\frac{\\lambda_{obs}}{\\lambda_{emit}} = \\frac{a_0}{a}$.",
        f"Scale factor then: $a = 1/(1 + z) = {fmt(a)}$; distances have grown by a factor of ${fmt(1 + z)}$.",
        f"Blackbody radiation stays thermal but cools as $T \\propto 1/a$: $T = 2.725(1 + z) = {fmt(T)}$ K.",
    ]
    if z >= 1000:
        steps.append("At ≈3000 K hydrogen became neutral and the universe turned transparent — the CMB we see today.")
    return {"question": question, "steps": steps,
            "answer": f"expanded ${fmt(1 + z)}$×; $a = {fmt(a)}$; $T \\approx {fmt(T)}$ K",
            "values": {"z": z, "a": a, "T_K": T}}


@template("hubble_time", ASTRO, "Cosmology", "Age of the universe", "medium")
def hubble_time(rng):
    H = pick(rng, [67.4, 70.0, 73.0]) if rng.random() < 0.4 else nice(rng, 50.0, 100.0, 0.5)
    Mpc_km = PC * 1e6 / 1000
    tH = Mpc_km / H
    tH_yr = tH / 3.156e7
    question = (
        f"Taking $H_0 = {fmt(H, 3)}$ km/s/Mpc, compute the Hubble time $1/H_0$ in years and the Hubble distance $c/H_0$ "
        "in megaparsecs. Why is the Hubble time only an approximate age of the universe?"
    )
    steps = [
        f"Convert: 1 Mpc $= 3.086\\times10^{{19}}$ km, so $1/H_0 = \\frac{{3.086\\times10^{{19}}}}{{{fmt(H, 3)}}}$ s $= {fmt(tH)}$ s.",
        f"In years: ${fmt(tH)}/3.156\\times10^7 = {fmt(tH_yr)}$ yr.",
        f"Hubble distance: $c/H_0 = 2.998\\times10^5/{fmt(H, 3)} = {fmt(2.998e5 / H)}$ Mpc.",
        "The true age depends on how the expansion rate changed (deceleration by matter, acceleration by dark energy); "
        "for the measured cosmological parameters the two effects nearly cancel, giving 13.8 Gyr.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$1/H_0 \\approx {fmt(tH_yr)}$ yr; $c/H_0 \\approx {fmt(2.998e5 / H)}$ Mpc",
            "values": {"H0": H, "t_H_years": tH_yr, "d_H_Mpc": 2.998e5 / H}}


@template("galaxy_rotation_mass", ASTRO, "Galactic Astronomy", "Dark matter", "hard")
def galaxy_rotation_mass(rng):
    v = nice(rng, 150, 300, 5)
    r_kpc = nice(rng, 5, 50, 1)
    L_visible = sig(rng.uniform(1e10, 8e10), 2)
    r = r_kpc * 1e3 * PC
    M = (v * 1e3) ** 2 * r / G
    M_solar = M / M_SUN
    ML = M_solar / L_visible
    question = (
        f"Stars and gas at {r_kpc} kpc from the center of a spiral galaxy orbit at {v} km/s. Estimate the mass enclosed "
        f"within that radius. If the galaxy's visible luminosity is ${fmt(L_visible, 2)}\\,L_\\odot$, what is the "
        "mass-to-light ratio, and what does it suggest?"
    )
    steps = [
        "For a roughly circular orbit, gravity supplies the centripetal force: $\\frac{GMm}{r^2} = \\frac{mv^2}{r}$, so "
        "$M = \\frac{v^2r}{G}$.",
        f"$r = {r_kpc}\\text{{ kpc}} = {fmt(r)}$ m; $v = {fmt(v * 1e3)}$ m/s.",
        f"$M = \\frac{{({fmt(v * 1e3)})^2({fmt(r)})}}{{6.674\\times10^{{-11}}}} = {fmt(M)}$ kg $= {fmt(M_solar)}\\,M_\\odot$.",
        f"Mass-to-light ratio: ${fmt(M_solar)}/{fmt(L_visible, 2)} = {fmt(ML)}\\,M_\\odot/L_\\odot$.",
        "Stellar populations have $M/L$ of only a few, so a much larger value — together with rotation curves that stay "
        "flat far beyond the visible disk — is evidence for dark matter.",
    ]
    return {"question": question, "steps": steps,
            "answer": f"$M \\approx {fmt(M_solar)}\\,M_\\odot$; $M/L \\approx {fmt(ML)}$",
            "values": {"v_kms": v, "r_kpc": r_kpc, "M_solar": M_solar, "L": L_visible, "M_over_L": ML}}
