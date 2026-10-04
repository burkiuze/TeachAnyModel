---
title: Stars - Properties, Life Cycles and Stellar Remnants
field: Astronomy
subfield: Astrophysics
level: high-school to undergraduate
keywords: [stars, parallax, parsec, apparent magnitude, absolute magnitude, luminosity, inverse square law, stellar spectra, spectral classes, OBAFGKM, Hertzsprung-Russell diagram, main sequence, stellar mass, mass-luminosity relation, binary stars, star formation, nebula, protostar, hydrostatic equilibrium, nuclear fusion, red giant, planetary nebula, white dwarf, Chandrasekhar limit, supernova, neutron star, pulsar, black hole, nucleosynthesis, variable stars, Cepheids]
---

# Stars: Properties, Life Cycles and Stellar Remnants

Stars are self-gravitating balls of plasma that shine by nuclear fusion. They forge nearly all chemical elements heavier than helium, create the conditions for planets and life, and end their lives as white dwarfs, neutron stars or black holes. Remarkably, almost everything we know about stars comes from analyzing their light.

## 1. Measuring Distances: Parallax

As Earth orbits the Sun, nearby stars appear to shift against more distant background stars. The **parallax angle** $p$ is half the total annual shift:
$$\boxed{d\,(\text{parsecs}) = \frac{1}{p\,(\text{arcseconds})}}$$
- 1 **parsec** (pc) ≈ 3.26 light-years ≈ 206 265 AU ≈ $3.086\times10^{16}$ m.
- The nearest star, **Proxima Centauri**, has $p = 0.768''$ → 1.30 pc (4.24 ly).
- Friedrich Bessel measured the first stellar parallax (61 Cygni) in 1838.
- ESA's **Gaia** spacecraft (2013–2025) measured parallaxes of nearly 2 billion stars with microarcsecond precision, producing the most detailed 3D map of the Milky Way.

Beyond parallax range, astronomers use the **cosmic distance ladder**: spectroscopic parallax, Cepheid variables, Type Ia supernovae, and redshift.

## 2. Brightness, Luminosity and Magnitudes

- **Luminosity** ($L$): total power emitted (watts). Sun: $L_\odot = 3.83\times10^{26}$ W.
- **Apparent brightness (flux)** falls with the inverse square of distance:
$$F = \frac{L}{4\pi d^2}$$

### The magnitude system
Dating back to Hipparchus (~150 BCE), who ranked stars from 1st magnitude (brightest) to 6th (faintest visible). Formalized by Norman Pogson (1856): a difference of **5 magnitudes = factor of 100** in brightness, so 1 magnitude = $100^{1/5} \approx 2.512$. **Smaller (or negative) magnitudes are brighter.**
$$m_1 - m_2 = -2.5\log_{10}\frac{F_1}{F_2}$$

| Object | Apparent magnitude $m$ |
|---|---|
| Sun | −26.74 |
| Full Moon | −12.7 |
| Venus (brightest) | −4.9 |
| Sirius (brightest star) | −1.46 |
| Vega | 0.03 |
| Polaris | 1.98 |
| Faintest naked-eye stars | ~6 |
| Hubble/JWST limits | ~31–34 |

**Absolute magnitude** ($M$): the apparent magnitude a star would have at 10 pc. The **distance modulus**:
$$m - M = 5\log_{10}d - 5\quad(d\text{ in pc})$$
The Sun's absolute magnitude is +4.83 — a fairly ordinary star seen from 10 pc.

**Worked example 2.1:** Sirius has $m = -1.46$ and $d = 2.64$ pc. $M = m - 5\log_{10}(2.64) + 5 = -1.46 - 2.11 + 5 = 1.43$. Compared with the Sun ($M = 4.83$): luminosity ratio $= 10^{(4.83 - 1.43)/2.5} = 10^{1.36} \approx 23$ — Sirius is about 23–25 times more luminous than the Sun.

## 3. Stellar Temperatures, Colors and Spectra

### Blackbody radiation
Stars approximate blackbodies:
- **Wien's law:** $\lambda_{\max} = \frac{2.898\times10^{-3}\text{ m·K}}{T}$. Hot stars peak in blue/UV; cool stars in red/IR. Betelgeuse (~3500 K) is reddish; Rigel (~12 000 K) is blue-white.
- **Stefan–Boltzmann law:** $L = 4\pi R^2\sigma T^4$. Knowing $L$ and $T$ gives the radius.

**Worked example 3.1:** a star with $T = 2T_\odot$ and $R = R_\odot$ has $L = 16L_\odot$. A red supergiant with $T = 0.6T_\odot$ but $L = 100\,000L_\odot$ has $R = R_\odot\sqrt{100\,000/0.6^4} \approx 880R_\odot$ — larger than Mars's orbit.

### Spectral lines
Stellar spectra show dark **absorption lines** (Fraunhofer lines in the Sun, catalogued 1814), formed when cooler outer layers absorb specific wavelengths. **Kirchhoff's laws** (1859): a hot dense object emits a continuous spectrum; a hot thin gas emits an emission-line spectrum; a cool thin gas in front of a hot source produces absorption lines. Each element has a unique fingerprint (Bunsen and Kirchhoff identified elements in the Sun; helium was discovered in the solar spectrum in 1868 by Janssen and Lockyer, before it was found on Earth in 1895).

### Spectral classification
The **Harvard classification** (developed by Annie Jump Cannon, Williamina Fleming, Antonia Maury and others, ~1900–1924, from hundreds of thousands of spectra) orders stars by temperature: **O B A F G K M** ("Oh Be A Fine Girl/Guy, Kiss Me"), each subdivided 0–9. Cecilia Payne-Gaposchkin showed in her 1925 thesis that the sequence reflects temperature (ionization states, via the Saha equation) and that stars are composed mainly of hydrogen and helium — a revolutionary discovery initially resisted.

| Class | Temperature (K) | Color | Key spectral features | Example |
|---|---|---|---|---|
| O | > 30 000 | Blue | Ionized helium (He II) | Zeta Puppis |
| B | 10 000–30 000 | Blue-white | Neutral helium, hydrogen | Rigel, Spica |
| A | 7500–10 000 | White | Strongest hydrogen (Balmer) lines | Sirius A, Vega |
| F | 6000–7500 | Yellow-white | Hydrogen, ionized metals (Ca II) | Procyon, Canopus |
| G | 5200–6000 | Yellow | Ionized calcium, neutral metals | **Sun (G2)**, Alpha Centauri A |
| K | 3700–5200 | Orange | Neutral metals | Arcturus, Aldebaran |
| M | 2400–3700 | Red | Molecular bands (TiO) | Betelgeuse, Proxima Centauri |
| L, T, Y | < 2400 | Deep red/infrared | Metal hydrides, methane, water | Brown dwarfs |

**Luminosity classes** (MK system): I supergiants, II bright giants, III giants, IV subgiants, V main-sequence dwarfs, D white dwarfs. The Sun is **G2V**.

**Doppler shifts** of spectral lines reveal radial velocities, rotation (line broadening), binary orbits and exoplanets. **Zeeman splitting** reveals magnetic fields.

## 4. The Hertzsprung–Russell Diagram

Ejnar Hertzsprung (1911) and Henry Norris Russell (1913) independently plotted luminosity (or absolute magnitude) against temperature (or spectral class). Temperature increases to the **left**. Stars fall into distinct regions:

- **Main sequence** (~90% of stars): a diagonal band from hot, luminous blue stars (upper left) to cool, dim red dwarfs (lower right). Stars fusing hydrogen into helium in their cores. Position along the main sequence is set primarily by **mass**.
- **Red giants and supergiants** (upper right): cool but very luminous because of enormous radii.
- **White dwarfs** (lower left): hot but faint because they are tiny (Earth-sized).

The H–R diagram is the most important tool in stellar astrophysics: it encodes stellar structure and evolution. Star clusters, whose members share age and distance, show how stars evolve: the **main-sequence turnoff** point reveals the cluster's age (old globular clusters: 11–13 billion years).

## 5. Stellar Masses and the Mass–Luminosity Relation

Masses are measured directly from **binary stars** (about half of Sun-like stars are in binary or multiple systems) using Kepler's third law: $M_1 + M_2 = \frac{a^3}{P^2}$ (solar masses, AU, years). Eclipsing binaries also give radii.

For main-sequence stars:
$$L \propto M^{3.5}\quad(\text{roughly, for } 0.5\text{–}20\,M_\odot)$$

Stellar masses range from ~0.08 $M_\odot$ (below which hydrogen fusion cannot ignite — **brown dwarfs**, "failed stars" of ~13–80 Jupiter masses) to perhaps ~150–300 $M_\odot$ (R136a1 in the Large Magellanic Cloud, ~200 $M_\odot$). Low-mass stars vastly outnumber high-mass stars; **red dwarfs** (M class) make up ~75% of stars in the Milky Way, though none are visible to the naked eye.

### Main-sequence lifetime
Fuel ∝ $M$; burning rate ∝ $L \propto M^{3.5}$:
$$t_{\text{MS}} \approx 10^{10}\text{ years}\times\left(\frac{M}{M_\odot}\right)^{-2.5}$$

| Mass ($M_\odot$) | Spectral type | Luminosity ($L_\odot$) | Main-sequence lifetime |
|---|---|---|---|
| 60 | O3 | ~800 000 | ~3 million years |
| 10 | B0 | ~10 000 | ~30 million years |
| 3 | A0 | ~80 | ~400 million years |
| 1.5 | F2 | ~5 | ~3 billion years |
| 1.0 | G2 | 1 | ~10 billion years |
| 0.5 | M0 | ~0.06 | ~50–100 billion years |
| 0.1 | M7 | ~0.001 | trillions of years |

**Massive stars live fast and die young.** No red dwarf in the universe has yet left the main sequence — the universe (13.8 billion years) is too young.

## 6. Stellar Structure

A main-sequence star is in **hydrostatic equilibrium**: outward pressure (thermal gas pressure, plus radiation pressure in massive stars) balances inward gravity at every layer:
$$\frac{dP}{dr} = -\frac{GM(r)\rho(r)}{r^2}$$
This balance is **self-regulating** (a thermostat): if the core contracts and heats, fusion increases, pressure rises, and the core expands and cools.

**Energy generation:**
- **Proton–proton chain** (dominant in stars ≤ ~1.3 $M_\odot$, including the Sun): $4\,^1\text{H}\to{}^4\text{He} + 2e^+ + 2\nu_e + 26.7$ MeV. About 0.7% of the mass is converted to energy.
- **CNO cycle** (dominant in more massive, hotter cores): carbon, nitrogen and oxygen act as catalysts; extremely temperature-sensitive (~$T^{17}$ vs. ~$T^4$ for pp).

**Energy transport:** by **radiation** (photon diffusion) or **convection**. The Sun has a radiative core and convective outer layer; massive stars have convective cores and radiative envelopes; low-mass red dwarfs are fully convective (mixing all their hydrogen, extending their lives).

## 7. Star Formation

1. **Molecular clouds:** cold (~10–20 K), dense clouds of molecular hydrogen and dust (e.g. the Orion Nebula, the Eagle Nebula's "Pillars of Creation"). Giant molecular clouds contain ~10⁴–10⁶ solar masses.
2. **Collapse:** when a region's gravity overcomes thermal pressure (the **Jeans criterion**), possibly triggered by supernova shocks or collisions, it collapses and fragments into clumps — stars typically form in **clusters**.
3. **Protostar:** the collapsing core heats up by gravitational contraction (converting potential energy into heat); surrounded by an infalling envelope and a rotating **accretion disk**; bipolar jets (Herbig–Haro objects) carry away angular momentum. Protostars are hidden in dust and best observed in infrared (Spitzer, JWST).
4. **T Tauri stage** (for Sun-like stars): pre-main-sequence stars contracting along the **Hayashi track**, with strong winds clearing the surroundings. Disks form planets.
5. **Zero-age main sequence:** core temperature reaches ~10 million K; hydrogen fusion ignites; hydrostatic equilibrium is established. For a solar-mass star, this takes ~50 million years; massive stars form much faster (~100 000 years).

## 8. The Evolution of Sun-Like Stars (≲ 8 $M_\odot$)

1. **Main sequence** (~10 billion years for the Sun; currently ~4.6 billion years in): core hydrogen fusion. The Sun slowly brightens (~1% per 100 million years; it was ~30% fainter when young — the "faint young Sun paradox").
2. **Subgiant and red giant branch:** when core hydrogen is exhausted, the helium core contracts and heats, hydrogen fusion continues in a **shell** around it, and the envelope expands enormously and cools → **red giant** (radius 10–100× larger). The Sun will swell to ~100–200 $R_\odot$ in ~5 billion years, engulfing Mercury and Venus and possibly Earth. Long before that (in ~1 billion years), the brightening Sun will boil away Earth's oceans.
3. **Helium flash and horizontal branch:** when the degenerate helium core reaches ~100 million K, **helium fusion** ignites (triple-alpha process: $3\,^4\text{He}\to{}^{12}\text{C}$, plus $^{12}\text{C} + {}^4\text{He}\to{}^{16}\text{O}$) — explosively in low-mass stars (the helium flash), smoothly in more massive ones. The star settles into stable core helium burning.
4. **Asymptotic giant branch (AGB):** after core helium is exhausted, a carbon–oxygen core remains, surrounded by helium- and hydrogen-burning shells; the star becomes a large, luminous, pulsating red giant, losing mass in strong winds. **s-process** neutron capture in AGB stars produces about half of the elements heavier than iron (e.g. strontium, barium, lead).
5. **Planetary nebula:** the outer layers are ejected, forming a glowing shell of gas ionized by the hot exposed core (e.g. the Ring Nebula, Helix Nebula, Cat's Eye Nebula). The name is historical — they have nothing to do with planets (they looked like planetary disks in small telescopes). They last ~10 000–50 000 years.
6. **White dwarf:** the exposed carbon–oxygen core, about Earth-sized, with a mass typically ~0.6 $M_\odot$ — a teaspoon weighs several tonnes (density ~10⁹ kg/m³). No fusion; supported by **electron degeneracy pressure** (Pauli exclusion principle). It cools and fades over billions of years toward a hypothetical cold "black dwarf" (none exist yet). Sirius B (discovered 1862) was the first white dwarf identified.
   - **Chandrasekhar limit:** ~1.4 $M_\odot$ — the maximum mass electron degeneracy can support (Subrahmanyan Chandrasekhar, 1930, calculated during a sea voyage aged 19; Nobel 1983). More massive white dwarfs cannot exist.
   - White dwarfs crystallize as they cool (confirmed by Gaia in 2019) — giant "diamonds" of carbon and oxygen.

## 9. The Evolution of Massive Stars (≳ 8 $M_\odot$)

1. **Rapid main-sequence life** (millions of years) as blue O or B stars.
2. **Red (or blue) supergiant:** successive fusion stages in the core, each faster than the last, producing an "onion-shell" structure:

| Fusion stage | Main products | Duration (for a ~25 $M_\odot$ star) | Core temperature |
|---|---|---|---|
| Hydrogen | Helium | ~7 million years | ~40 million K |
| Helium | Carbon, oxygen | ~500 000 years | ~200 million K |
| Carbon | Neon, sodium, magnesium | ~600 years | ~800 million K |
| Neon | Oxygen, magnesium | ~1 year | ~1.5 billion K |
| Oxygen | Silicon, sulfur | ~6 months | ~2 billion K |
| Silicon | Iron, nickel | ~1 day | ~3 billion K |

3. **Iron core:** iron-56 (and nickel-62) has the highest binding energy per nucleon, so fusing iron **absorbs** energy rather than releasing it. Fusion stops; the core can no longer support itself.
4. **Core collapse:** when the iron core exceeds the Chandrasekhar mass, it collapses in less than a second, from Earth-size to ~20 km, reaching nuclear density. Electrons combine with protons to form neutrons and neutrinos (neutronization). The collapse halts abruptly as neutron degeneracy and nuclear forces resist; infalling material rebounds; a flood of ~10⁵⁸ neutrinos (carrying ~99% of the energy, ~10⁴⁶ J) helps drive a shock wave outward.
5. **Type II (core-collapse) supernova:** the star's outer layers are blasted into space at ~10 000+ km/s. For weeks the supernova can outshine an entire galaxy (~10⁹–10¹⁰ $L_\odot$). Elements are synthesized and dispersed; the **r-process** (rapid neutron capture) in supernovae and especially **neutron-star mergers** produces the heaviest elements (gold, platinum, uranium).
   - **SN 1987A** in the Large Magellanic Cloud (168 000 ly) was the closest supernova in centuries; ~25 neutrinos were detected hours before the light arrived, confirming core-collapse theory (Masatoshi Koshiba, Nobel 2002).
   - Historical supernovae: SN 1006 (brightest recorded), SN 1054 (created the Crab Nebula, recorded by Chinese astronomers), Tycho's (1572) and Kepler's (1604) — the last observed in our galaxy.
   - **Betelgeuse** (a red supergiant ~550 light-years away) will explode within the next ~100 000 years; it dimmed dramatically in 2019–2020 due to a dust cloud. It poses no danger to Earth.
6. **Remnant:** a **neutron star** (if the remnant core is below ~2–3 $M_\odot$) or a **black hole** (above).

### Type Ia supernovae (thermonuclear)
A white dwarf in a binary system gains mass from a companion (or merges with another white dwarf) until it approaches the Chandrasekhar limit; carbon fusion ignites explosively and the white dwarf is completely destroyed. Because they explode near the same mass, they have similar peak luminosities (after calibration) — **standard candles** used to measure cosmic distances, which revealed the **accelerating expansion of the universe** (1998; Perlmutter, Schmidt, Riess, Nobel 2011). Type Ia supernovae produce much of the universe's iron.

**Novae** (distinct from supernovae) are recurrent surface hydrogen explosions on accreting white dwarfs.

## 10. Stellar Remnants

| Remnant | Progenitor | Mass | Size | Supported by | Density |
|---|---|---|---|---|---|
| White dwarf | < ~8 $M_\odot$ | ≲ 1.4 $M_\odot$ | ~Earth (~10 000 km) | Electron degeneracy | ~10⁹ kg/m³ |
| Neutron star | ~8–25 $M_\odot$ | ~1.1–2.3 $M_\odot$ | ~20–25 km diameter | Neutron degeneracy + nuclear forces | ~10¹⁷–10¹⁸ kg/m³ |
| Black hole | ≳ 25 $M_\odot$ (uncertain) | ≳ 3 $M_\odot$ | Event horizon ~6 km per $M_\odot$ (diameter) | Nothing — collapse to singularity | — |

### Neutron stars and pulsars
- Predicted by Walter Baade and Fritz Zwicky in 1934, shortly after the neutron's discovery.
- A sugar-cube volume weighs ~hundreds of millions to a billion tonnes; surface gravity ~10¹¹ times Earth's; escape velocity ~1/3–1/2 the speed of light.
- Rapid rotation (conservation of angular momentum during collapse) and intense magnetic fields (10⁸–10¹¹ T; **magnetars** up to ~10¹¹ T).
- **Pulsars:** rotating neutron stars beaming radiation from their magnetic poles, seen as regular pulses like a lighthouse. Discovered in 1967 by graduate student **Jocelyn Bell Burnell** (the signal was half-jokingly labeled "LGM-1", for "little green men"); Antony Hewish shared the 1974 Nobel Prize (controversially, without Bell Burnell). The Crab Pulsar spins 30 times per second; **millisecond pulsars** (spun up by accreting from a companion) up to ~716 times per second. Pulsars are extraordinarily precise clocks used to test general relativity (Hulse–Taylor binary) and to search for gravitational waves (pulsar timing arrays).
- **Maximum mass** (Tolman–Oppenheimer–Volkoff limit): ~2.2–2.3 $M_\odot$; the heaviest measured neutron stars are ~2.0–2.35 $M_\odot$.
- **Neutron-star mergers** (GW170817, 2017) produce kilonovae and heavy elements.

### Black holes
Regions where gravity is so strong that nothing, not even light, can escape (see the general relativity document).
- **Stellar-mass black holes** form from the collapse of the most massive stars; detected in X-ray binaries (Cygnus X-1, 1971) and through gravitational waves from mergers (LIGO/Virgo, since 2015); Gaia found dormant black holes in binaries (Gaia BH1, BH2, BH3 — the last ~33 $M_\odot$).
- **Supermassive black holes** (millions to billions of solar masses) at galactic centers.
- Matter falling into a black hole forms a hot **accretion disk**, emitting X-rays — accretion is the most efficient energy source known after matter–antimatter annihilation (up to ~6–42% of rest mass energy converted to radiation, vs. 0.7% for fusion).

## 11. Variable Stars and Binary Stars

- **Cepheid variables:** pulsating supergiants whose brightness varies with periods of days to months. **Henrietta Swan Leavitt** (1908–1912) discovered the **period–luminosity relation** from Cepheids in the Small Magellanic Cloud — longer period means greater luminosity — making them **standard candles**. Edwin Hubble used Cepheids in the Andromeda "nebula" (1923–1924) to show it is a separate galaxy far beyond the Milky Way.
- **RR Lyrae** variables (old, low-mass, horizontal-branch stars; all have similar luminosities) — distance indicators for globular clusters.
- **Mira variables** (long-period pulsating AGB stars).
- **Eclipsing binaries** (Algol, "the Demon Star", dims every 2.87 days).
- **Cataclysmic variables** and novae (accreting white dwarfs).
- **X-ray binaries** (accreting neutron stars or black holes).

## 12. Star Clusters
- **Open clusters:** young (up to a few billion years), loosely bound groups of hundreds to thousands of stars in the galactic disk (the Pleiades, ~100 million years old; the Hyades).
- **Globular clusters:** ancient (~11–13 billion years), dense spherical swarms of 10⁵–10⁶ stars in the galactic halo (Omega Centauri, M13). The Milky Way has ~150–160.

## 13. Cosmic Nucleosynthesis Summary

| Elements | Main origin |
|---|---|
| H, He (most), some Li | Big Bang nucleosynthesis (first ~20 minutes) |
| Li, Be, B (mostly) | Cosmic-ray spallation |
| C, N, O | Low- and intermediate-mass stars (AGB) and massive stars |
| O through Fe (α elements, Si, S, Ca) | Massive stars and core-collapse supernovae |
| Fe, Ni (much) | Type Ia supernovae |
| Heavy elements (s-process: Sr, Ba, Pb) | AGB stars |
| Heavy elements (r-process: Eu, Au, Pt, U) | Neutron-star mergers, rare supernovae |

The calcium in our bones, the iron in our blood, the oxygen we breathe and the gold in our jewelry were all forged in stars that lived and died before the Sun was born.

## 14. Summary

| Concept | Formula / Key fact |
|---|---|
| Parallax distance | $d\,(\text{pc}) = 1/p\,('')$ |
| Inverse-square law | $F = L/(4\pi d^2)$ |
| Magnitudes | 5 mag = 100× in brightness; $m - M = 5\log d - 5$ |
| Stefan–Boltzmann | $L = 4\pi R^2\sigma T^4$ |
| Wien's law | $\lambda_{\max}T = 2.898\times10^{-3}$ m·K |
| Spectral classes | O B A F G K M (hot → cool) |
| Mass–luminosity | $L \propto M^{3.5}$ |
| Lifetime | $t \approx 10^{10}(M/M_\odot)^{-2.5}$ years |
| Low-mass fate | Red giant → planetary nebula → white dwarf |
| High-mass fate | Supergiant → core-collapse supernova → neutron star or black hole |
| Chandrasekhar limit | ~1.4 $M_\odot$ |
| Hydrostatic equilibrium | Pressure gradient balances gravity |
