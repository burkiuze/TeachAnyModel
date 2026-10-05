---
title: Stars - Properties, Life Cycles and Stellar Remnants
field: Astronomy
subfield: Astrophysics
level: high-school to undergraduate
keywords: [stars, parallax, parsec, apparent magnitude, absolute magnitude, luminosity, inverse square law, stellar spectra, spectral classes, OBAFGKM, Hertzsprung-Russell diagram, main sequence, stellar mass, mass-luminosity relation, binary stars, star formation, nebula, protostar, hydrostatic equilibrium, nuclear fusion, red giant, planetary nebula, white dwarf, Chandrasekhar limit, supernova, neutron star, pulsar, black hole, nucleosynthesis, variable stars, Cepheids, Stefan-Boltzmann law, Wien's law, Planck's law, Saha equation, Doppler shift, distance modulus, bolometric magnitude, virial theorem, Kelvin-Helmholtz timescale, proton-proton chain, CNO cycle, triple-alpha process, solar neutrinos, Eddington luminosity, Jeans mass, free-fall time, initial mass function, degeneracy pressure, Schwarzschild radius, pulsar spin-down, Type Ia supernova, binding energy per nucleon, Gaia]
---

# Stars: Properties, Life Cycles and Stellar Remnants

Stars are self-gravitating balls of plasma that shine by nuclear fusion. They forge nearly all chemical elements heavier than helium, create the conditions for planets and life, and end their lives as white dwarfs, neutron stars or black holes. Remarkably, almost everything we know about stars comes from analyzing their light: how bright it is, what color it has, which dark and bright lines cross its spectrum, and how all of these change with time.

This chapter follows the same logic astronomers used historically. First we measure the basic properties of stars — distance, luminosity, temperature, radius, composition and mass. Then we use physics (gravity, thermodynamics, quantum mechanics and nuclear physics) to explain how stars work, how they are born, how they evolve and what they leave behind.

## 1. Measuring Distances: Parallax

As Earth orbits the Sun, nearby stars appear to shift against more distant background stars, tracing a small ellipse over the course of a year. The **parallax angle** $p$ is half the total annual shift — the angle subtended at the star by the radius of Earth's orbit.

### Deriving the parallax formula

Picture a right triangle whose short side is the Earth–Sun distance (1 AU), whose long side is the distance $d$ to the star, and whose small angle at the star is $p$. Then $\tan p = (1\ \text{AU})/d$. Stellar parallaxes are tiny, so the small-angle approximation $\tan p \approx p$ (with $p$ in radians) is excellent:
$$d = \frac{1\ \text{AU}}{p\,(\text{rad})}$$
One arcsecond is $1/3600$ of a degree, or $\pi/(180\times3600) = 4.848\times10^{-6}$ rad. Substituting $p\,(\text{rad}) = 4.848\times10^{-6}\,p\,('')$ gives
$$d = \frac{206\,265\ \text{AU}}{p\,('')}$$
The **parsec** ("parallax of one arcsecond") is defined as the distance at which $p = 1''$, that is, 206 265 AU. Measured in parsecs, the distance is simply the reciprocal of the parallax in arcseconds:
$$\boxed{d\,(\text{parsecs}) = \frac{1}{p\,(\text{arcseconds})}}$$

- 1 **parsec** (pc) ≈ 3.26 light-years ≈ 206 265 AU ≈ $3.086\times10^{16}$ m.
- The nearest star, **Proxima Centauri**, has $p = 0.768''$ → 1.30 pc (4.24 ly).
- Friedrich Bessel measured the first stellar parallax (61 Cygni) in 1838; Thomas Henderson (Alpha Centauri) and Friedrich Georg Wilhelm Struve (Vega) reported parallaxes at almost the same time. Parallaxes are so small that it took more than two centuries of telescopic astronomy to detect one — the absence of visible parallax had been used since antiquity as an argument against Earth's motion.
- From the ground, atmospheric blurring ("seeing") of roughly an arcsecond limited precise parallaxes to relatively nearby stars. ESA's **Hipparcos** satellite (1989–1993) measured parallaxes of about 118 000 stars to roughly one milliarcsecond.
- ESA's **Gaia** spacecraft (2013–2025) measured positions of about 1.8 billion sources and parallaxes for roughly 1.5 billion of them (Data Release 3, 2022), with uncertainties as small as a few tens of microarcseconds for bright stars, producing the most detailed 3D map of the Milky Way.

**Worked example 1.1 — a parallax with an uncertainty.** A star's parallax is measured as $p = 0.0125'' \pm 0.0005''$. Find its distance and the uncertainty.
1. Distance: $d = 1/0.0125 = 80$ pc.
2. In light-years: $80\times3.26 = 261$ ly.
3. Because $d \propto p^{-1}$, a small fractional error in $p$ produces the same fractional error in $d$: $0.0005/0.0125 = 0.04 = 4\%$.
4. Absolute uncertainty: $0.04\times80 = 3.2$ pc.

**Answer:** $d = 80 \pm 3$ pc, about $261 \pm 10$ light-years. For comparison, with Gaia's best uncertainty of about 0.02 milliarcseconds, a 10% distance is possible down to $p = 0.2$ milliarcseconds, i.e. out to about 5000 pc — a large fraction of the Galactic disk. Note that when the fractional error exceeds roughly 20%, simply inverting the parallax gives biased distances, and statistical methods are needed.

Beyond parallax range, astronomers use the **cosmic distance ladder**: spectroscopic parallax (Section 4), Cepheid variables (Section 11), Type Ia supernovae (Section 9) and, for distant galaxies, redshift. Each rung is calibrated on the one below it, so parallax is the foundation of the entire cosmic distance scale.

## 2. Brightness, Luminosity and Magnitudes

- **Luminosity** ($L$): total power emitted (watts). Sun: $L_\odot = 3.828\times10^{26}$ W (the IAU 2015 nominal value). Luminosity is an intrinsic property of the star.
- **Apparent brightness (flux)** $F$: power received per unit area (W/m²). It depends on both the luminosity and the distance.

### The inverse-square law
In empty space energy is conserved, so the whole luminosity crosses every imaginary sphere centered on the star. A sphere of radius $d$ has area $4\pi d^2$, so the power per unit area is
$$F = \frac{L}{4\pi d^2}$$
Doubling the distance spreads the same power over four times the area and cuts the flux to one quarter.

**Worked example 2.1 — the solar constant.** How much solar power reaches each square metre at Earth's distance (above the atmosphere)?
1. Distance: $d = 1\ \text{AU} = 1.496\times10^{11}$ m.
2. Area of the sphere: $4\pi d^2 = 4\pi(1.496\times10^{11}\ \text{m})^2 = 2.812\times10^{23}\ \text{m}^2$.
3. Flux: $F = (3.828\times10^{26}\ \text{W})/(2.812\times10^{23}\ \text{m}^2) = 1361\ \text{W/m}^2$.

**Answer:** about 1361 W/m², in agreement with the total solar irradiance measured by satellites. The logic also runs backwards: measuring $F$ and $d$ for any star yields its luminosity $L = 4\pi d^2 F$, which is exactly how stellar luminosities are determined.

### The magnitude system
The system dates back to Hipparchus (2nd century BCE), who ranked stars from 1st magnitude (brightest) to 6th (faintest visible). Formalized by Norman Pogson (1856): a difference of **5 magnitudes = factor of 100** in brightness, so 1 magnitude = $100^{1/5} \approx 2.512$. **Smaller (or negative) magnitudes are brighter.** Pogson's rule says that a magnitude difference $\Delta m$ corresponds to a flux ratio $100^{\Delta m/5} = 10^{0.4\,\Delta m}$; taking the logarithm and inserting a minus sign (so that brighter means smaller) gives
$$m_1 - m_2 = -2.5\log_{10}\frac{F_1}{F_2}$$
The logarithmic scale is not arbitrary: human perception of brightness is roughly logarithmic, which is why the ancient naked-eye ranking maps so neatly onto a ratio scale.

| Object | Apparent magnitude $m$ |
|---|---|
| Sun | −26.74 |
| Full Moon | −12.7 |
| Venus (brightest) | −4.9 |
| Sirius (brightest star) | −1.46 |
| Vega | 0.03 |
| Polaris | 1.98 |
| Faintest naked-eye stars | ~6 |
| Deepest Hubble/JWST images | ~30–31 |

### Absolute magnitude and the distance modulus
**Absolute magnitude** ($M$) is the apparent magnitude a star would have at a standard distance of 10 pc. To relate $m$ and $M$, compare the flux at the true distance, $F_d = L/(4\pi d^2)$, with the flux at 10 pc, $F_{10} = L/(4\pi(10\ \text{pc})^2)$:
$$m - M = -2.5\log_{10}\frac{F_d}{F_{10}} = -2.5\log_{10}\left(\frac{10\ \text{pc}}{d}\right)^2 = 5\log_{10}\frac{d}{10\ \text{pc}}$$
This is the **distance modulus**:
$$m - M = 5\log_{10}d - 5\quad(d\text{ in pc}),\qquad d = 10^{(m - M + 5)/5}\ \text{pc}$$
Interstellar dust dims and reddens starlight; with an extinction of $A$ magnitudes the relation becomes $m - M = 5\log_{10}d - 5 + A$. The Sun's absolute visual magnitude is +4.83 — a fairly ordinary star seen from 10 pc.

Filters (U, B, V, ...) capture only part of a star's light. The **bolometric magnitude** counts all wavelengths and is tied directly to luminosity:
$$M_{\text{bol}} = 4.74 - 2.5\log_{10}\frac{L}{L_\odot}$$
where 4.74 is the Sun's bolometric absolute magnitude (IAU 2015 convention). The difference between bolometric and visual magnitudes, the bolometric correction, is largest for very hot and very cool stars, which emit most of their energy in the ultraviolet or infrared.

**Worked example 2.2 — Sirius.** Sirius has $m = -1.46$ and $d = 2.64$ pc. How luminous is it compared with the Sun?
1. $5\log_{10}(2.64) = 2.11$.
2. $M = m - 5\log_{10}d + 5 = -1.46 - 2.11 + 5 = 1.43$.
3. Luminosity ratio in the visual band: $10^{(4.83 - 1.43)/2.5} = 10^{1.36} \approx 23$.

**Answer:** Sirius emits about 23 times more visible light than the Sun; its total (bolometric) luminosity is about 25 $L_\odot$ because, being hotter, it radiates relatively more in the ultraviolet.

## 3. Stellar Temperatures, Colors and Spectra

### Blackbody radiation
Stars approximate blackbodies — idealized emitters whose spectrum depends only on temperature. Max Planck's law (1900) gives the power emitted per unit area, per unit wavelength, per unit solid angle:
$$B_\lambda(T) = \frac{2hc^2}{\lambda^5}\,\frac{1}{e^{hc/(\lambda k_B T)} - 1}$$
Two laws follow from it:
- **Wien's law** (Wilhelm Wien, 1893): $\lambda_{\max} = \frac{2.898\times10^{-3}\text{ m·K}}{T}$. Hot stars peak in blue/UV; cool stars in red/IR. Betelgeuse (~3500–3600 K) peaks near 800 nm in the near-infrared and looks reddish; Rigel (~12 000 K) peaks near 240 nm in the ultraviolet and looks blue-white.
- **Stefan–Boltzmann law** (found experimentally by Josef Stefan in 1879 and derived by Ludwig Boltzmann in 1884): each square metre of a blackbody surface emits $\sigma T^4$, with $\sigma = 5.670\times10^{-8}$ W m⁻² K⁻⁴. Multiplying by the surface area $4\pi R^2$ gives $L = 4\pi R^2\sigma T^4$. Knowing $L$ and $T$ gives the radius.

The temperature in the Stefan–Boltzmann law is the **effective temperature** $T_{\text{eff}}$: the temperature of a blackbody of the same radius that would emit the same total power. Dividing by the solar values gives a convenient form:
$$\frac{R}{R_\odot} = \left(\frac{L}{L_\odot}\right)^{1/2}\left(\frac{T_\odot}{T}\right)^2$$

**Worked example 3.1 — scaling with temperature and radius.** A star with $T = 2T_\odot$ and $R = R_\odot$ has $L = 2^4 L_\odot = 16L_\odot$. A red supergiant with $T = 0.6T_\odot$ but $L = 100\,000L_\odot$ has $R = R_\odot\sqrt{100\,000/0.6^4} \approx 880R_\odot$ — about 4 AU, larger than the orbit of Mars.

**Worked example 3.2 — the Sun's effective temperature.** Use $L_\odot = 3.828\times10^{26}$ W and $R_\odot = 6.957\times10^8$ m.
1. Surface area: $4\pi R^2 = 4\pi(6.957\times10^8\ \text{m})^2 = 6.082\times10^{18}\ \text{m}^2$.
2. Multiply by $\sigma$: $5.670\times10^{-8}\times6.082\times10^{18} = 3.449\times10^{11}$ W/K⁴.
3. $T^4 = L/(4\pi R^2\sigma) = 3.828\times10^{26}/3.449\times10^{11} = 1.110\times10^{15}$ K⁴.
4. $T = (1.110\times10^{15})^{1/4} = 5772$ K.
5. Peak wavelength: $\lambda_{\max} = 2.898\times10^{-3}/5772 = 5.02\times10^{-7}$ m = 502 nm.

**Answer:** $T_{\text{eff}} \approx 5772$ K, with the spectrum peaking near 500 nm in the blue-green. Because the Sun's spectrum is broad and covers the whole visible range, its light is essentially white; it looks yellowish from the ground partly because air scatters some blue light out of the direct beam.

### Color index
Comparing magnitudes through a blue (B) and a visual (V) filter gives the **color index** $B - V$. Hot blue stars have small or negative $B - V$; cool red stars have large positive values (the Sun's is about 0.65). The color index is a cheap thermometer that works even for stars too faint for detailed spectroscopy.

### Spectral lines
Stellar spectra show dark **absorption lines** (Fraunhofer lines in the Sun, catalogued 1814), formed when cooler outer layers absorb specific wavelengths. **Kirchhoff's laws** (1859): a hot dense object emits a continuous spectrum; a hot thin gas emits an emission-line spectrum; a cool thin gas in front of a hot source produces absorption lines. Each element has a unique fingerprint (Bunsen and Kirchhoff identified elements in the Sun; helium was discovered in the solar spectrum in 1868 by Janssen and Lockyer, before it was found on Earth in 1895).

### Why line strengths depend on temperature
Nearly all stars have similar compositions, yet their spectra differ dramatically. The reason is that a line appears only if atoms are in the right **energy level** and the right **ionization state**, and both depend steeply on temperature.

The fraction of atoms in an excited level follows the **Boltzmann equation**:
$$\frac{N_2}{N_1} = \frac{g_2}{g_1}\,e^{-(E_2 - E_1)/k_BT}$$
The visible **Balmer lines** of hydrogen are absorbed by atoms whose electron sits in level $n = 2$, which lies 10.2 eV above the ground state (statistical weights $g_1 = 2$, $g_2 = 8$). The ratio $N_2/N_1$ is about $5\times10^{-9}$ at 5800 K, $3\times10^{-5}$ at 10 000 K and $1\times10^{-2}$ at 20 000 K. Higher temperatures populate level 2 — but they also ionize hydrogen (ionization energy 13.6 eV), removing the atoms altogether. The ionization balance follows the **Saha equation** (Meghnad Saha, 1920):
$$\frac{N_{i+1}\,n_e}{N_i} = \frac{2Z_{i+1}}{Z_i}\left(\frac{2\pi m_e k_BT}{h^2}\right)^{3/2}e^{-\chi_i/k_BT}$$
where $N_i$ is the number density of ions in stage $i$, $n_e$ the electron density, $Z$ the partition functions and $\chi_i$ the ionization energy. Combining the two effects, the number of hydrogen atoms able to absorb Balmer lines peaks near 9000–10 000 K, which is why A stars show the strongest hydrogen lines while hotter O and B stars and cooler K and M stars show weaker ones.

### Spectral classification
The **Harvard classification** (developed by Annie Jump Cannon, Williamina Fleming, Antonia Maury and others, ~1900–1924, from hundreds of thousands of spectra; the Henry Draper Catalogue of 1918–1924 lists more than 225 000 stars) orders stars by temperature: **O B A F G K M** ("Oh Be A Fine Girl/Guy, Kiss Me"), each subdivided 0–9. Cecilia Payne-Gaposchkin showed in her 1925 thesis, using the Saha equation, that the sequence reflects temperature (ionization and excitation states) and that stars are composed mainly of hydrogen and helium — a revolutionary discovery initially resisted. Henry Norris Russell persuaded her to call the enormous hydrogen abundance "almost certainly not real"; four years later Russell himself reached the same conclusion by another route.

| Class | Temperature (K) | Color | Key spectral features | Example |
|---|---|---|---|---|
| O | > 30 000 | Blue | Ionized helium (He II) | Zeta Puppis |
| B | 10 000–30 000 | Blue-white | Neutral helium, hydrogen | Rigel, Spica |
| A | 7500–10 000 | White | Strongest hydrogen (Balmer) lines | Sirius A, Vega |
| F | 6000–7500 | Yellow-white | Hydrogen, ionized metals (Ca II) | Procyon, Polaris |
| G | 5200–6000 | Yellow | Ionized calcium, neutral metals | **Sun (G2)**, Alpha Centauri A |
| K | 3700–5200 | Orange | Neutral metals | Arcturus, Aldebaran |
| M | 2400–3700 | Red | Molecular bands (TiO) | Betelgeuse, Proxima Centauri |
| L, T, Y | < 2400 | Deep red/infrared | Metal hydrides, methane, water | Brown dwarfs (early L types also include the lowest-mass stars) |

**Luminosity classes** (MK system): I supergiants, II bright giants, III giants, IV subgiants, V main-sequence dwarfs, D white dwarfs. The Sun is **G2V**. Stars of the same temperature but different size can be told apart because the low-density atmospheres of giants produce narrower absorption lines (less pressure broadening) than the dense atmospheres of dwarfs.

### Doppler shifts and magnetic fields
Motion along the line of sight shifts every line by the same fractional amount. For speeds much smaller than $c$:
$$v_r = c\,\frac{\lambda_{\text{obs}} - \lambda_0}{\lambda_0}$$
A positive $v_r$ (redshift) means recession; a negative value (blueshift) means approach.

**Worked example 3.3 — a radial velocity.** The hydrogen-alpha line, with rest wavelength 656.28 nm, is observed at 656.72 nm in a star's spectrum.
1. Shift: $\Delta\lambda = 656.72 - 656.28 = 0.44$ nm.
2. Fractional shift: $0.44/656.28 = 6.70\times10^{-4}$.
3. Velocity: $v_r = 6.70\times10^{-4}\times2.998\times10^5\ \text{km/s} = 201$ km/s.

**Answer:** the star recedes at about 200 km/s. If the shift oscillates with time, the star is orbiting a companion.

Doppler shifts reveal radial velocities, rotation (line broadening), binary orbits and exoplanets. Jupiter makes the Sun wobble at about 12.5 m/s; detecting such tiny periodic shifts in another star led Michel Mayor and Didier Queloz to the first planet around a Sun-like star, 51 Pegasi b (1995; Nobel Prize 2019). **Zeeman splitting** of lines reveals magnetic fields; George Ellery Hale used it in 1908 to discover the strong magnetic fields of sunspots.

## 4. The Hertzsprung–Russell Diagram

Ejnar Hertzsprung (1911) and Henry Norris Russell (1913) independently plotted luminosity (or absolute magnitude) against temperature (or spectral class). Temperature increases to the **left**. Stars fall into distinct regions:

- **Main sequence** (~90% of stars): a diagonal band from hot, luminous blue stars (upper left) to cool, dim red dwarfs (lower right). Stars fusing hydrogen into helium in their cores. Position along the main sequence is set primarily by **mass**.
- **Red giants and supergiants** (upper right): cool but very luminous because of enormous radii.
- **White dwarfs** (lower left): hot but faint because they are tiny (Earth-sized).

Why the radius can be read from the diagram: taking the logarithm of $L = 4\pi R^2\sigma T^4$ gives
$$\log_{10}L = 2\log_{10}R + 4\log_{10}T + \text{constant}$$
so on a log–log H–R diagram, stars of equal radius lie along straight diagonal lines. Moving up at fixed temperature means moving to larger radius; this is why the upper-right stars must be giants and the lower-left stars must be dwarfs.

The H–R diagram is the most important tool in stellar astrophysics: it encodes stellar structure and evolution. Star clusters, whose members share age and distance, show how stars evolve: the **main-sequence turnoff** point reveals the cluster's age (old globular clusters: 11–13 billion years). A nearly vertical **instability strip** crossing the giant region contains pulsating stars such as Cepheids and RR Lyrae variables (Section 11). Gaia's 2018 H–R diagram of millions of nearby stars, with precise parallaxes, revealed fine structure such as distinct white-dwarf sequences that earlier data had blurred.

**Spectroscopic parallax** turns the diagram into a distance tool: classify a star's spectrum (temperature class plus luminosity class), read off its absolute magnitude from a calibrated H–R diagram, then apply the distance modulus. Despite the name, no parallax is measured.

**Worked example 4.1 — spectroscopic parallax.** A star has a G2V spectrum (so $M \approx 4.8$, like the Sun) and apparent magnitude $m = 12.3$. Ignoring extinction, how far away is it?
1. Distance modulus: $m - M = 12.3 - 4.8 = 7.5$.
2. $d = 10^{(m - M + 5)/5} = 10^{12.5/5} = 10^{2.5}$ pc.
3. $d \approx 316$ pc.

**Answer:** about 320 pc (roughly 1000 light-years). The method's accuracy is limited to perhaps 10–25% because stars of the same spectral type differ somewhat in luminosity.

## 5. Stellar Masses and the Mass–Luminosity Relation

Mass is the single most important property of a star, and it can be measured directly only through gravity — mainly in **binary stars** (about half of Sun-like stars are in binary or multiple systems).

### Kepler's third law for binaries
Newton's generalization of Kepler's third law for two bodies orbiting each other with period $P$ and relative semimajor axis $a$ is
$$P^2 = \frac{4\pi^2a^3}{G(M_1 + M_2)}$$
For Earth's orbit ($a = 1$ AU, $P = 1$ yr, $M_1 + M_2 \approx 1\,M_\odot$) the constant $4\pi^2/G$ equals 1 when masses are in solar masses, distances in AU and times in years. Therefore
$$M_1 + M_2 = \frac{a^3}{P^2}\quad(\text{solar masses, AU, years})$$
To split the total, use the center of mass: $M_1a_1 = M_2a_2$, so $M_1/M_2 = a_2/a_1$, where $a_1$ and $a_2$ are each star's distance from the center of mass. In spectroscopic binaries the same ratio follows from the velocity amplitudes, $M_1/M_2 = v_2/v_1$. Eclipsing binaries also give radii, from the durations of the eclipses.

**Worked example 5.1 — the mass of Sirius A + B.** Sirius B orbits Sirius A with $P = 50.1$ yr; the orbit's angular semimajor axis is $7.50''$ and the distance is 2.64 pc.
1. Convert the angle to a length. By the definition of the parsec, $1''$ at 1 pc corresponds to 1 AU, so $a = 7.50\times2.64 = 19.8$ AU.
2. $a^3 = 19.8^3 = 7762$ AU³; $P^2 = 50.1^2 = 2510$ yr².
3. $M_1 + M_2 = 7762/2510 = 3.09\,M_\odot$.
4. Sirius B's orbit about the center of mass is roughly twice as large as Sirius A's, so $M_A \approx 2M_B$, giving $M_A \approx 2.06\,M_\odot$ and $M_B \approx 1.03\,M_\odot$.

**Answer:** the pair has a total mass of about 3.1 $M_\odot$; Sirius B, a white dwarf, contains about one solar mass.

### The mass–luminosity relation
For main-sequence stars:
$$L \propto M^{3.5}\quad(\text{roughly, for } 0.5\text{–}20\,M_\odot)$$
A simple physical argument explains the steepness. Heat leaks out of a star by radiative diffusion, so the luminosity is set by the temperature gradient and the opacity. Hydrostatic equilibrium and the ideal gas law imply that a star's internal temperature scales as $T \propto M/R$; inserting this into the diffusion law gives $L \propto M^3/\kappa$, where $\kappa$ is the opacity. Variations of opacity and the onset of convection modify the exponent in different mass ranges. Commonly used approximate fits are:

| Mass range ($M_\odot$) | Approximate relation |
|---|---|
| below 0.43 | $L/L_\odot \approx 0.23\,(M/M_\odot)^{2.3}$ |
| 0.43–2 | $L/L_\odot \approx (M/M_\odot)^{4}$ |
| 2–55 | $L/L_\odot \approx 1.4\,(M/M_\odot)^{3.5}$ |
| above 55 | $L/L_\odot \approx 32\,000\,(M/M_\odot)$ |

The flattening at the top is caused by radiation pressure: very massive stars approach the Eddington limit (Section 6), at which $L$ can grow only in proportion to $M$.

Stellar masses range from ~0.08 $M_\odot$ (below which hydrogen fusion cannot ignite — **brown dwarfs**, "failed stars" of ~13–80 Jupiter masses) to perhaps ~150–300 $M_\odot$ (R136a1 in the Large Magellanic Cloud, ~200 $M_\odot$). Low-mass stars vastly outnumber high-mass stars; **red dwarfs** (M class) make up ~75% of stars in the Milky Way, yet not one is easily visible to the naked eye.

### Main-sequence lifetime
The time a star spends on the main sequence is its fuel supply divided by its burning rate. Fuel ∝ $M$; burning rate ∝ $L \propto M^{3.5}$; hence $t \propto M/L \propto M^{-2.5}$. The normalization comes from the Sun.

**Worked example 5.2 — the Sun's nuclear lifetime.** Assume that only the central ~10% of the Sun's mass becomes hot enough to fuse hydrogen, and that fusion converts 0.7% of the fused mass into energy.
1. Mass available: $0.1\times1.989\times10^{30} = 1.989\times10^{29}$ kg.
2. Energy released: $E = 0.007\times1.989\times10^{29}\ \text{kg}\times(2.998\times10^8\ \text{m/s})^2 = 1.25\times10^{44}$ J.
3. Lifetime: $t = E/L_\odot = 1.25\times10^{44}/3.828\times10^{26} = 3.27\times10^{17}$ s.
4. Convert: $3.27\times10^{17}\ \text{s}/(3.156\times10^7\ \text{s/yr}) = 1.04\times10^{10}$ yr.

**Answer:** about 10 billion years, in agreement with detailed solar models. Combining this with the scaling law:
$$t_{\text{MS}} \approx 10^{10}\text{ years}\times\left(\frac{M}{M_\odot}\right)^{-2.5}$$

| Mass ($M_\odot$) | Approx. spectral type | Luminosity ($L_\odot$) | Main-sequence lifetime |
|---|---|---|---|
| 60 | O3 | ~800 000 | ~3 million years |
| 10 | B1–B2 | ~5000–10 000 | ~20–30 million years |
| 3 | B8–B9 | ~80 | ~400 million years |
| 1.5 | F2 | ~5 | ~3 billion years |
| 1.0 | G2 | 1 | ~10 billion years |
| 0.5 | M0 | ~0.06 | ~50–100 billion years |
| 0.1 | M6–M7 | ~0.001 | trillions of years |

The lifetimes in the table come from detailed models. The simple power law works best near a solar mass; for very massive stars it fails badly (it would give only about 0.4 million years for 60 $M_\odot$), because their luminosity grows roughly in proportion to mass, so lifetimes level off at about 3 million years. **Massive stars live fast and die young.** No red dwarf in the universe has yet left the main sequence — the universe (13.8 billion years) is too young.

## 6. Stellar Structure

### Hydrostatic equilibrium
A main-sequence star is in **hydrostatic equilibrium**: outward pressure (thermal gas pressure, plus radiation pressure in massive stars) balances inward gravity at every layer. To derive the condition, consider a small cylinder of gas at radius $r$ with base area $A$, thickness $dr$ and density $\rho(r)$. Its mass is $\rho A\,dr$, and gravity pulls it inward with force $GM(r)\rho A\,dr/r^2$, where $M(r)$ is the mass inside radius $r$ (by Newton's shell theorem, mass outside $r$ exerts no net force). The pressure below the cylinder exceeds the pressure above it, giving a net outward force $[P(r) - P(r + dr)]A = -(dP/dr)\,dr\,A$. Setting the two forces equal:
$$\frac{dP}{dr} = -\frac{GM(r)\rho(r)}{r^2}$$
Pressure must therefore increase toward the center. This balance is **self-regulating** (a thermostat): if the core contracts and heats, fusion increases, pressure rises, and the core expands and cools.

### The equations of stellar structure
A spherical star in a steady state is described by four coupled differential equations:
$$\frac{dP}{dr} = -\frac{GM(r)\rho}{r^2},\qquad \frac{dM}{dr} = 4\pi r^2\rho,\qquad \frac{dL}{dr} = 4\pi r^2\rho\,\varepsilon,\qquad \frac{dT}{dr} = -\frac{3\kappa\rho L(r)}{64\pi\sigma r^2T^3}$$
They express hydrostatic equilibrium, mass conservation, energy generation ($\varepsilon$ is the nuclear power released per kilogram) and radiative energy transport ($\kappa$ is the opacity); in convective regions the last equation is replaced by the adiabatic temperature gradient. Supplemented by an equation of state $P(\rho, T)$, an opacity law and nuclear reaction rates, and solved on a computer, they produce stellar models. The **Vogt–Russell theorem** summarizes the result: a star's structure is fixed by its mass and its chemical composition.

**Worked example 6.1 — a minimum central pressure for the Sun.** Combining the first two equations gives $dP/dM = -GM/(4\pi r^4)$. Everywhere inside the star $r < R$, so $1/r^4 > 1/R^4$, and integrating from the center ($M = 0$) to the surface ($M = M_\odot$, $P = 0$):
$$P_c = \int_0^{M_\odot}\frac{GM}{4\pi r^4}\,dM > \int_0^{M_\odot}\frac{GM}{4\pi R^4}\,dM = \frac{GM_\odot^2}{8\pi R_\odot^4}$$
1. $GM_\odot^2 = 6.674\times10^{-11}\times(1.989\times10^{30})^2 = 2.640\times10^{50}$ N·m².
2. $8\pi R_\odot^4 = 8\pi\times(6.957\times10^8)^4 = 5.886\times10^{36}$ m⁴.
3. $P_c > 2.640\times10^{50}/5.886\times10^{36} = 4.5\times10^{13}$ Pa.

**Answer:** at least $4.5\times10^{13}$ Pa, or about 440 million atmospheres. Standard solar models give about $2.4\times10^{16}$ Pa — some 500 times larger — because the Sun's mass is strongly concentrated toward the center.

### The virial theorem: why stars heat up as they lose energy
For a star in equilibrium, the **virial theorem** relates the total thermal kinetic energy $K$ to the gravitational potential energy $U$:
$$2K + U = 0$$
For a uniform sphere $U = -\frac{3}{5}GM^2/R$, and an ideal gas of $N = M/(\mu m_H)$ particles has $K = \frac{3}{2}Nk_B\bar{T}$, where $\mu$ is the mean mass per particle in units of the hydrogen mass. Solving for the average temperature:
$$\bar{T} = \frac{\mu m_H GM}{5k_BR}$$
For the Sun (ionized gas, $\mu \approx 0.6$) this gives about 3 million K — the right order of magnitude for the interior, whose central temperature is 15.7 million K.

The total energy is $E = K + U = -K$. When a star radiates energy away, $E$ becomes more negative, so $K$ — and the temperature — *increases*. A self-gravitating gas therefore has a **negative heat capacity**: it heats up as it loses energy, contracting as it does so. This explains why protostars heat up as they shine, why stellar cores grow hotter each time a fuel is exhausted, and why fusion in a star is stable: overproduction of energy makes the core expand and cool, damping the reaction.

### The Kelvin–Helmholtz timescale and the age problem
Before nuclear physics, Hermann von Helmholtz (1854) and William Thomson, Lord Kelvin (1860s), proposed that the Sun shines by slowly contracting, converting gravitational energy into heat. The time this could last is the **Kelvin–Helmholtz timescale**:
$$t_{\text{KH}} \sim \frac{GM^2}{RL}$$

**Worked example 6.2 — how long could gravity power the Sun?**
1. $GM_\odot^2 = 2.640\times10^{50}$ J·m (from Worked example 6.1).
2. $R_\odot L_\odot = 6.957\times10^8\times3.828\times10^{26} = 2.663\times10^{35}$ W·m.
3. $t_{\text{KH}} = 2.640\times10^{50}/2.663\times10^{35} = 9.9\times10^{14}$ s $\approx 3.1\times10^7$ yr.

**Answer:** about 30 million years. Kelvin's estimates of this order clashed with geologists and with Charles Darwin, who needed hundreds of millions of years or more. Radioactive dating in the early 20th century showed that Earth is billions of years old, so the Sun needed a far richer energy source. Arthur Eddington (1920) suggested the fusion of hydrogen into helium, inspired by Francis Aston's precise measurements showing that a helium atom is slightly lighter than four hydrogen atoms. Hans Bethe worked out the specific reaction chains in 1938–1939 (Nobel Prize 1967); the pp chain was developed with Charles Critchfield, and Carl Friedrich von Weizsäcker independently proposed the CNO cycle.

### Energy generation
- **Proton–proton chain** (dominant in stars ≤ ~1.3 $M_\odot$, including the Sun): $4\,^1\text{H}\to{}^4\text{He} + 2e^+ + 2\nu_e + 26.7$ MeV. About 0.7% of the mass is converted to energy. Its main branch (pp-I) runs:
$$p + p \to {}^2\text{H} + e^+ + \nu_e,\qquad {}^2\text{H} + p \to {}^3\text{He} + \gamma,\qquad {}^3\text{He} + {}^3\text{He} \to {}^4\text{He} + 2p$$
The first step requires a proton to turn into a neutron through the weak nuclear force, which is so improbable that an average proton in the solar core waits billions of years before fusing. This bottleneck is why the Sun burns slowly and steadily.
- **CNO cycle** (dominant in more massive, hotter cores): carbon, nitrogen and oxygen act as catalysts; extremely temperature-sensitive (~$T^{17}$ vs. ~$T^4$ for pp). In its main loop, ¹²C captures a proton to become ¹³N, which decays to ¹³C; further captures produce ¹⁴N, ¹⁵O (which decays to ¹⁵N), and finally ¹⁵N + p → ¹²C + ⁴He, returning the carbon. The slowest step, proton capture on ¹⁴N, makes nitrogen pile up — one source of the nitrogen in the universe.

**Quantum tunneling makes fusion possible.** Two protons must approach within about $10^{-15}$ m for the strong force to act, but there their electrostatic repulsion is about 1 MeV ($e^2/(4\pi\varepsilon_0 r) \approx 1.44$ MeV at $r = 10^{-15}$ m). The typical thermal energy at the Sun's center is only $k_BT \approx 1.35$ keV — about a thousand times smaller. Classically, fusion would be impossible. George Gamow showed in 1928 that particles can tunnel through such barriers, and Robert Atkinson and Fritz Houtermans (1929) applied this to stars: fusion proceeds through the rare fast protons in the tail of the Maxwell–Boltzmann distribution that also tunnel through the barrier.

**Worked example 6.3 — the Sun's mass-to-energy budget.** Atomic masses: ¹H = 1.007825 u, ⁴He = 4.002603 u; 1 u = 931.494 MeV/$c^2$.
1. Mass of four hydrogen atoms: $4\times1.007825 = 4.031300$ u.
2. Mass defect: $\Delta m = 4.031300 - 4.002603 = 0.028697$ u.
3. Energy per helium nucleus: $0.028697\times931.494 = 26.73$ MeV.
4. Fraction of mass converted: $0.028697/4.031300 = 0.712\%$.
5. Mass converted per second: $L_\odot/c^2 = 3.828\times10^{26}/(2.998\times10^8)^2 = 4.26\times10^9$ kg/s.
6. Hydrogen fused per second: $4.26\times10^9/0.00712 = 6.0\times10^{11}$ kg/s.

**Answer:** each helium nucleus formed releases 26.7 MeV; the Sun loses about 4.3 million tonnes of mass per second as energy and fuses about 600 million tonnes of hydrogen per second. (Using atomic masses automatically includes the annihilation of the two positrons with electrons.)

### Solar neutrinos
Every helium nucleus produced by the pp chain emits two electron neutrinos, which escape the Sun almost without interacting.

**Worked example 6.4 — the solar neutrino flux at Earth.**
1. Energy per reaction: $26.73\ \text{MeV}\times1.602\times10^{-13}\ \text{J/MeV} = 4.28\times10^{-12}$ J.
2. Reactions per second: $3.828\times10^{26}/4.28\times10^{-12} = 8.9\times10^{37}$ s⁻¹.
3. Neutrinos per second: $2\times8.9\times10^{37} = 1.8\times10^{38}$ s⁻¹.
4. Flux at 1 AU: $1.8\times10^{38}/(2.812\times10^{23}\ \text{m}^2) = 6.4\times10^{14}$ m⁻² s⁻¹.

**Answer:** about $6\times10^{10}$ neutrinos pass through every square centimetre of your body each second, day and night (the Earth is nearly transparent to them). A small fraction of the energy is carried off by the neutrinos themselves, so this estimate is slightly high, but it matches detailed models well.

Raymond Davis Jr.'s chlorine experiment in the Homestake mine (results from 1968 onward) detected only about a third of the predicted neutrinos — the **solar neutrino problem**. It was solved when Super-Kamiokande (1998) and the Sudbury Neutrino Observatory (2001–2002) showed that neutrinos change flavor during their journey, which requires them to have mass. Davis and Masatoshi Koshiba shared the 2002 Nobel Prize; Takaaki Kajita and Arthur McDonald received the 2015 prize for neutrino oscillations. In 2020 the Borexino experiment detected neutrinos from the CNO cycle in the Sun, confirming that this cycle operates in stars.

### Energy transport
Energy moves outward by **radiation** (photon diffusion) or **convection**. The Sun has a radiative core and convective outer layer (the granulation pattern on its surface is the top of the convection cells); massive stars have convective cores and radiative envelopes; low-mass red dwarfs are fully convective (mixing all their hydrogen, extending their lives). Convection takes over whenever the temperature gradient needed to carry the energy by radiation would be steeper than the adiabatic gradient (the Schwarzschild criterion), which happens where the opacity is high or where energy generation is extremely concentrated.

In the radiative zone, a photon is absorbed and re-emitted in a random direction after traveling a short mean free path $\ell$. After $N$ random steps a random walker is only about $\sqrt{N}\,\ell$ from its starting point, so escaping a distance $R$ requires $N \approx (R/\ell)^2$ steps and a time $t \approx R^2/(\ell c)$. With an average $\ell$ of order 1 mm, $t \approx (6.957\times10^8)^2/(10^{-3}\times3.0\times10^8)\ \text{s} \approx 5\times10^4$ yr; detailed models give tens of thousands to a few hundred thousand years. The energy released in the core today will emerge as sunlight in the distant future — and then take only 8.3 minutes to reach Earth.

### The Eddington limit
Radiation carries momentum. When a star's luminosity is high enough, the outward push of radiation on free electrons (which drag protons along electrostatically) equals gravity's pull. Setting the radiation force on an electron, $\sigma_T L/(4\pi r^2c)$, equal to the gravitational force on a proton, $GMm_p/r^2$, gives the **Eddington luminosity**:
$$L_{\text{Edd}} = \frac{4\pi GMm_pc}{\sigma_T}$$
where $\sigma_T = 6.652\times10^{-29}$ m² is the Thomson scattering cross section of the electron.

**Worked example 6.5 — the Eddington limit for a 100 $M_\odot$ star.**
1. For one solar mass: $4\pi GM_\odot m_pc = 4\pi\times6.674\times10^{-11}\times1.989\times10^{30}\times1.673\times10^{-27}\times2.998\times10^8 = 836.5$ (SI units).
2. Divide by $\sigma_T$: $836.5/6.652\times10^{-29} = 1.26\times10^{31}$ W, i.e. $3.3\times10^4\,L_\odot$ per solar mass.
3. For 100 $M_\odot$: $L_{\text{Edd}} = 3.3\times10^6\,L_\odot$.

**Answer:** about 3 million solar luminosities. The most massive stars shine at a sizeable fraction of this limit, which is why they drive powerful winds, shed mass violently and why stars much above ~200–300 $M_\odot$ are not observed. The same limit caps the brightness of accreting black holes and quasars.

### The Sun by the numbers

| Quantity | Value |
|---|---|
| Mass | $1.989\times10^{30}$ kg |
| Radius (nominal) | $6.957\times10^8$ m (109 Earth radii) |
| Luminosity (nominal) | $3.828\times10^{26}$ W |
| Effective temperature | 5772 K |
| Mean density | 1410 kg/m³ |
| Central temperature | ~15.7 million K |
| Central density | ~150 000 kg/m³ |
| Age | ~4.6 billion years |
| Surface composition (by mass) | ~74% H, ~25% He, ~1.3% heavier elements |
| Spectral type; absolute visual magnitude | G2V; +4.83 |
| Light travel time to Earth | 499 s (8.3 min) |

## 7. Star Formation

1. **Molecular clouds:** cold (~10–20 K), dense clouds of molecular hydrogen and dust (e.g. the Orion Molecular Cloud complex, whose glowing Orion Nebula is lit by newborn stars, and the Eagle Nebula's "Pillars of Creation"). Giant molecular clouds contain ~10⁴–10⁶ solar masses.
2. **Collapse:** when a region's gravity overcomes thermal pressure (the **Jeans criterion**), possibly triggered by supernova shocks or collisions, it collapses and fragments into clumps — stars typically form in **clusters**.
3. **Protostar:** the collapsing core heats up by gravitational contraction (converting potential energy into heat); surrounded by an infalling envelope and a rotating **accretion disk**; bipolar jets (Herbig–Haro objects) carry away angular momentum. Protostars are hidden in dust and best observed in infrared (Spitzer, JWST).
4. **T Tauri stage** (for Sun-like stars): pre-main-sequence stars contracting along the **Hayashi track**, with strong winds clearing the surroundings. Disks form planets.
5. **Zero-age main sequence:** core temperature reaches ~10 million K; hydrogen fusion ignites; hydrostatic equilibrium is established. For a solar-mass star, this takes ~50 million years; massive stars form much faster (~100 000 years).

### The Jeans mass
A cloud collapses if its gravitational binding energy outweighs its thermal energy. Using the virial theorem as the dividing line, a uniform sphere of mass $M$, radius $R$ and temperature $T$ collapses when $2K < \lvert U\rvert$:
$$3\,\frac{M}{\mu m_H}\,k_BT < \frac{3}{5}\,\frac{GM^2}{R}\quad\Longrightarrow\quad M > \frac{5k_BT}{G\mu m_H}\,R$$
Eliminating the radius with $R = (3M/(4\pi\rho))^{1/3}$ gives the critical **Jeans mass** (after James Jeans, 1902):
$$M_J = \left(\frac{5k_BT}{G\mu m_H}\right)^{3/2}\left(\frac{3}{4\pi\rho}\right)^{1/2}$$
Since $M_J \propto T^{3/2}\rho^{-1/2}$, cold and dense gas collapses most easily. As a cloud collapses while staying cold (it radiates its heat away efficiently), its density rises and $M_J$ falls, so smaller and smaller pieces become unstable — the cloud **fragments** into many stars. A collapsing cloud with no pressure support falls inward on the **free-fall time**
$$t_{\text{ff}} = \sqrt{\frac{3\pi}{32G\rho}}$$
which depends only on the density, not on the cloud's size.

**Worked example 7.1 — a molecular-cloud core.** A cloud core has $T = 10$ K and a number density of $10^4$ molecules per cm³ ($10^{10}$ m⁻³). Take $\mu = 2.33$ (molecular hydrogen with helium) and $m_H = 1.674\times10^{-27}$ kg.
1. Density: $\rho = n\mu m_H = 10^{10}\times2.33\times1.674\times10^{-27} = 3.9\times10^{-17}$ kg/m³.
2. First factor: $5k_BT/(G\mu m_H) = 5\times1.381\times10^{-23}\times10/(6.674\times10^{-11}\times2.33\times1.674\times10^{-27}) = 2.65\times10^{15}$ kg/m; raised to the power 3/2 this is $1.37\times10^{23}$ (SI units).
3. Second factor: $(3/(4\pi\rho))^{1/2} = (6.12\times10^{15})^{1/2} = 7.8\times10^7$ (SI units).
4. $M_J = 1.37\times10^{23}\times7.8\times10^7 = 1.07\times10^{31}$ kg $\approx 5.4\,M_\odot$.
5. Free-fall time: $t_{\text{ff}} = \sqrt{3\pi/(32\times6.674\times10^{-11}\times3.9\times10^{-17})} = 1.06\times10^{13}$ s $\approx 3.4\times10^5$ yr.

**Answer:** clumps of more than about 5 solar masses are unstable and would collapse in roughly 300 000 years if nothing resisted. Real clouds collapse more slowly because magnetic fields and turbulence provide extra support.

### The initial mass function
Star formation produces many more small stars than large ones. Edwin Salpeter (1955) found that the number of stars born per unit mass interval follows a power law, the **initial mass function (IMF)**:
$$\frac{dN}{dM} \propto M^{-2.35}$$
Later work (for example by Pavel Kroupa and Gilles Chabrier) showed that the IMF flattens below about 0.5 $M_\odot$, but the Salpeter slope still describes stars above about 1 $M_\odot$ well.

**Worked example 7.2 — counting stars with the IMF.** For every star born with 10–20 $M_\odot$, how many are born with 1–2 $M_\odot$?
1. Integrate: $N(M_a\text{ to }M_b) \propto \int_{M_a}^{M_b}M^{-2.35}\,dM \propto M_a^{-1.35} - M_b^{-1.35}$.
2. Low-mass bin: $1^{-1.35} - 2^{-1.35}$. High-mass bin: $10^{-1.35} - 20^{-1.35} = 10^{-1.35}(1^{-1.35} - 2^{-1.35})$.
3. The ratio is $10^{1.35} = 22.4$.

**Answer:** about 22 stars of 1–2 $M_\odot$ for each star of 10–20 $M_\odot$. Because massive stars are rare but enormously luminous and short-lived, they nevertheless dominate the light of young star-forming regions and the production of heavy elements.

Objects below about 0.08 $M_\odot$ never ignite sustained hydrogen fusion; above about 13 Jupiter masses they briefly fuse deuterium. Such brown dwarfs were predicted in the 1960s and first confirmed in 1995 (Teide 1 in the Pleiades and Gliese 229B).

## 8. The Evolution of Sun-Like Stars (≲ 8 $M_\odot$)

1. **Main sequence** (~10 billion years for the Sun; currently ~4.6 billion years in): core hydrogen fusion. The Sun slowly brightens (~1% per 100 million years; it was ~30% fainter when young — the "faint young Sun paradox"). The brightening happens because fusion turns four particles into one, raising the mean particle mass $\mu$ in the core; to keep up the pressure the core contracts and heats slightly, which speeds up fusion.
2. **Subgiant and red giant branch:** when core hydrogen is exhausted, the helium core contracts and heats, hydrogen fusion continues in a **shell** around it, and the envelope expands enormously and cools → **red giant** (radius 10–100× larger, or more). The Sun will swell to roughly 150–250 $R_\odot$ (about 0.7–1.2 AU) in ~5 billion years, engulfing Mercury and Venus and possibly Earth. Long before that (in ~1 billion years), the brightening Sun will boil away Earth's oceans.
3. **Helium flash and horizontal branch:** when the degenerate helium core reaches ~100 million K, **helium fusion** ignites (triple-alpha process: $3\,^4\text{He}\to{}^{12}\text{C}$, plus $^{12}\text{C} + {}^4\text{He}\to{}^{16}\text{O}$) — explosively in low-mass stars (the helium flash), smoothly in more massive ones. The star settles into stable core helium burning.
4. **Asymptotic giant branch (AGB):** after core helium is exhausted, a carbon–oxygen core remains, surrounded by helium- and hydrogen-burning shells; the star becomes a large, luminous, pulsating red giant, losing mass in strong winds. **s-process** neutron capture in AGB stars produces about half of the elements heavier than iron (e.g. strontium, barium, lead).
5. **Planetary nebula:** the outer layers are ejected, forming a glowing shell of gas ionized by the hot exposed core (e.g. the Ring Nebula, Helix Nebula, Cat's Eye Nebula). The name is historical — they have nothing to do with planets (they looked like planetary disks in small telescopes). They last ~10 000–50 000 years.
6. **White dwarf:** the exposed carbon–oxygen core, about Earth-sized, with a mass typically ~0.6 $M_\odot$ — a teaspoon weighs several tonnes (density ~10⁹ kg/m³). No fusion; supported by **electron degeneracy pressure** (Pauli exclusion principle). It cools and fades over billions of years toward a hypothetical cold "black dwarf" (none exist yet). 40 Eridani B was recognized as an anomalously hot, faint star in 1910; Sirius B, first seen in 1862 by Alvan Graham Clark, had its white-dwarf nature revealed by Walter Adams's spectrum in 1915.
   - **Chandrasekhar limit:** ~1.4 $M_\odot$ — the maximum mass electron degeneracy can support (Subrahmanyan Chandrasekhar, 1930, calculated during a sea voyage aged 19; Nobel 1983). More massive white dwarfs cannot exist.
   - White dwarfs crystallize as they cool (confirmed by Gaia in 2019): their carbon and oxygen nuclei freeze into a regular lattice immersed in a sea of degenerate electrons. Popular accounts call them "cosmic diamonds", but the structure is not that of diamond, whose carbon atoms are held together by covalent bonds.

### The triple-alpha process
Helium fusion faces a puzzle: two helium-4 nuclei combine into beryllium-8, which is unstable and falls apart in about $10^{-16}$ s. Carbon can form only if a third alpha particle strikes during that instant. In 1953 Fred Hoyle argued that the observed abundance of carbon required carbon-12 to have an excited state near 7.65 MeV, which would make the three-body reaction resonant and fast; experimenters at Caltech soon found it. This "Hoyle state" is a famous example of a prediction made from the existence of the elements. The energy released is
$$3\times4.002603\ \text{u} - 12.000000\ \text{u} = 0.007809\ \text{u} \;\Rightarrow\; 0.007809\times931.494\ \text{MeV} = 7.27\ \text{MeV}$$
per carbon nucleus — only about a tenth of the energy per unit mass released by hydrogen fusion, which is one reason the helium-burning phase is much shorter than the main sequence.

### Why white dwarfs have a maximum mass
In a white dwarf the electrons are packed so tightly that the Pauli exclusion principle forces them into high-momentum states, creating **degeneracy pressure** that does not depend on temperature. For non-relativistic electrons $P \propto (\rho/\mu_e)^{5/3}$, where $\mu_e$ is the number of nucleons per electron ($\mu_e = 2$ for carbon and oxygen). A scaling argument shows the consequences:
- Hydrostatic equilibrium requires a central pressure of order $P \sim GM^2/R^4$.
- Non-relativistic degeneracy supplies $P \sim K\rho^{5/3} \sim KM^{5/3}/R^5$.
- Equating them gives $R \propto M^{-1/3}$: **more massive white dwarfs are smaller.**

As the mass grows, the electrons become relativistic and the pressure law stiffens less, $P \sim K'\rho^{4/3} \sim K'M^{4/3}/R^4$. Now both sides scale as $R^{-4}$, the radius cancels, and equilibrium is possible for only one mass. A detailed calculation gives the **Chandrasekhar mass**:
$$M_{\text{Ch}} = \frac{\sqrt{3\pi}}{2}\,\omega_3\left(\frac{\hbar c}{G}\right)^{3/2}\frac{1}{(\mu_em_H)^2} \approx 1.43\,M_\odot\quad(\mu_e = 2)$$
where $\omega_3 \approx 2.018$ is a numerical constant from the structure equations. Above this mass no amount of electron degeneracy pressure can halt collapse. When Chandrasekhar presented the result, Arthur Eddington ridiculed it at a Royal Astronomical Society meeting in January 1935, and acceptance was delayed for years.

**Worked example 8.1 — Sirius B.** Take Sirius B's mass as 1.0 $M_\odot$ and its radius as 5800 km.
1. Volume: $\frac{4}{3}\pi(5.8\times10^6\ \text{m})^3 = 8.17\times10^{20}$ m³.
2. Density: $1.989\times10^{30}/8.17\times10^{20} = 2.4\times10^9$ kg/m³ — 2.4 tonnes per cubic centimetre.
3. Surface gravity: $g = GM/R^2 = 6.674\times10^{-11}\times1.989\times10^{30}/(5.8\times10^6)^2 = 3.9\times10^6$ m/s², about 400 000 times Earth's.
4. Gravitational redshift, expressed as an equivalent velocity: $v = GM/(Rc) = 6.674\times10^{-11}\times1.989\times10^{30}/(5.8\times10^6\times2.998\times10^8) = 7.6\times10^4$ m/s.

**Answer:** density ~$2\times10^9$ kg/m³, surface gravity ~400 000 g, and a predicted redshift of about 76 km/s. Walter Adams attempted this measurement in 1925 as a test of general relativity; modern Hubble Space Telescope spectra give about 80 km/s, in good agreement.

## 9. The Evolution of Massive Stars (≳ 8 $M_\odot$)

1. **Rapid main-sequence life** (millions of years) as blue O or B stars, with strong stellar winds.
2. **Red (or blue) supergiant:** successive fusion stages in the core, each faster than the last, producing an "onion-shell" structure:

| Fusion stage | Main products | Duration (for a ~25 $M_\odot$ star) | Core temperature |
|---|---|---|---|
| Hydrogen | Helium | ~7 million years | ~40 million K |
| Helium | Carbon, oxygen | ~500 000 years | ~200 million K |
| Carbon | Neon, sodium, magnesium | ~600 years | ~800 million K |
| Neon | Oxygen, magnesium | ~1 year | ~1.5 billion K |
| Oxygen | Silicon, sulfur | ~6 months | ~2 billion K |
| Silicon | Iron, nickel | ~1 day | ~3 billion K |

(The durations depend on the stellar model, especially on mass loss and mixing; they are order-of-magnitude values.) Each stage is shorter because heavier fuels release less energy per kilogram and because, from carbon burning onward, most of the energy escapes as neutrinos rather than light, draining the core extremely fast.

3. **Iron core:** nuclei near iron sit at the peak of the binding-energy curve (nickel-62 has the highest binding energy per nucleon, with iron-58 and iron-56 extremely close behind), so fusing iron **absorbs** energy rather than releasing it. Fusion stops; the core can no longer support itself.

| Nucleus | Binding energy per nucleon (MeV) |
|---|---|
| ²H | 1.112 |
| ⁴He | 7.074 |
| ¹²C | 7.680 |
| ¹⁶O | 7.976 |
| ²⁰Ne | 8.032 |
| ²⁸Si | 8.448 |
| ⁵⁶Fe | 8.790 |
| ⁶²Ni | 8.795 |
| ²³⁸U | 7.570 |

The steep rise from hydrogen to helium explains why hydrogen fusion is so productive; the gentle slope beyond carbon explains why later stages release so little; and the decline beyond the iron peak explains why heavy elements are made by neutron capture rather than by fusion.

4. **Core collapse:** when the iron core exceeds the Chandrasekhar mass, it collapses in less than a second, from Earth-size to ~20 km, reaching nuclear density. Electron captures and the photodisintegration of iron by energetic photons remove pressure support and speed up the collapse. Electrons combine with protons to form neutrons and neutrinos (neutronization). The collapse halts abruptly as neutron degeneracy and nuclear forces resist; infalling material rebounds; a flood of ~10⁵⁸ neutrinos (carrying ~99% of the energy, ~10⁴⁶ J) helps drive a shock wave outward.
5. **Type II (core-collapse) supernova:** the star's outer layers are blasted into space at ~10 000+ km/s. For weeks the supernova can rival the light of an entire galaxy (core-collapse supernovae typically peak at ~10⁸–10⁹ $L_\odot$; the brightest supernovae of all types reach ~10¹⁰ $L_\odot$). Elements are synthesized and dispersed; the **r-process** (rapid neutron capture) in supernovae and especially **neutron-star mergers** produces the heaviest elements (gold, platinum, uranium).
   - **SN 1987A** in the Large Magellanic Cloud (168 000 ly) was the closest supernova in centuries; ~25 neutrinos were detected hours before the light arrived, confirming core-collapse theory (Masatoshi Koshiba, Nobel 2002).
   - **Betelgeuse** (a red supergiant ~550 light-years away) will explode within the next ~100 000 years; it dimmed dramatically in 2019–2020 due to a dust cloud. It poses no danger to Earth.
6. **Remnant:** a **neutron star** (if the remnant core is below ~2–3 $M_\odot$) or a **black hole** (above).

**Worked example 9.1 — the energy of core collapse.** Estimate the gravitational energy released when an iron core of 1.4 $M_\odot$ collapses to a neutron star of radius 12 km. (The initial radius of thousands of kilometres can be neglected, since the energy is dominated by the final radius.)
1. $M = 1.4\times1.989\times10^{30} = 2.785\times10^{30}$ kg.
2. Binding energy of a uniform sphere: $E \approx \frac{3}{5}GM^2/R = 0.6\times6.674\times10^{-11}\times(2.785\times10^{30})^2/(1.2\times10^4) = 2.6\times10^{46}$ J.
3. If neutrinos carry this away with an average energy of about 10 MeV ($1.6\times10^{-12}$ J): $N \approx 2.6\times10^{46}/1.6\times10^{-12} = 1.6\times10^{58}$ neutrinos.
4. Compare with the Sun's total output over 10 billion years: $3.828\times10^{26}\ \text{W}\times3.156\times10^{17}\ \text{s} = 1.2\times10^{44}$ J.

**Answer:** about $3\times10^{46}$ J — some 200 times what the Sun radiates in its entire main-sequence life — released in about 10 seconds, mostly as $\sim10^{58}$ neutrinos. Only about 1% (~$10^{44}$ J) ends up as kinetic energy of the ejecta, and less than 0.01% as light.

### Classifying supernovae
Supernova types are defined by their spectra, but the physics divides them into two families:

| Type | Spectral signature | Mechanism | Typical progenitor |
|---|---|---|---|
| Ia | No hydrogen; strong silicon absorption | Thermonuclear explosion | White dwarf in a binary system |
| Ib | No hydrogen; helium lines | Core collapse | Massive star stripped of its hydrogen envelope |
| Ic | No hydrogen or helium | Core collapse | Massive star stripped of hydrogen and helium |
| II (II-P, II-L, IIn, IIb) | Hydrogen lines | Core collapse | Massive star with its envelope, often a red supergiant |

After the first days, supernova light is powered by radioactivity. Explosive silicon burning makes nickel-56, which decays to cobalt-56 (half-life 6.1 days) and then to stable iron-56 (half-life 77 days). The slow tail of a supernova light curve follows the cobalt decay; SN 1987A produced about 0.07 $M_\odot$ of nickel-56, and gamma-ray lines from cobalt-56 were detected directly. Much of the iron in our blood passed through this decay chain.

Historical supernovae include SN 1006 (the brightest ever recorded, a Type Ia), SN 1054 (a core-collapse event that created the Crab Nebula, recorded by Chinese astronomers), and Tycho's (1572) and Kepler's (1604) supernovae — both now thought to have been thermonuclear (Tycho's was confirmed as Type Ia from the spectrum of its light echo) and the last observed with the naked eye in our galaxy.

### Type Ia supernovae (thermonuclear)
A white dwarf in a binary system gains mass from a companion (or merges with another white dwarf) until it approaches the Chandrasekhar limit; carbon fusion ignites explosively and the white dwarf is completely destroyed. Because they explode near the same mass, they have similar peak luminosities (after calibration) — **standard candles** used to measure cosmic distances, which revealed the **accelerating expansion of the universe** (1998; Perlmutter, Schmidt, Riess, Nobel 2011). The calibration relies on the empirical relation published by Mark Phillips in 1993: Type Ia supernovae that fade more slowly are intrinsically brighter. Type Ia supernovae produce much of the universe's iron.

**Novae** (distinct from supernovae) are recurrent surface hydrogen explosions on accreting white dwarfs; the white dwarf survives.

## 10. Stellar Remnants

| Remnant | Progenitor | Mass | Size | Supported by | Density |
|---|---|---|---|---|---|
| White dwarf | < ~8 $M_\odot$ | ≲ 1.4 $M_\odot$ | ~Earth (~10 000 km) | Electron degeneracy | ~10⁹ kg/m³ |
| Neutron star | ~8–25 $M_\odot$ | ~1.1–2.3 $M_\odot$ | ~20–25 km diameter | Neutron degeneracy + nuclear forces | ~10¹⁷–10¹⁸ kg/m³ |
| Black hole | ≳ 25 $M_\odot$ (uncertain) | ≳ 3 $M_\odot$ | Event horizon ~6 km per $M_\odot$ (diameter) | Nothing — collapse to singularity | — |

### Neutron stars and pulsars
- Predicted by Walter Baade and Fritz Zwicky in 1934, shortly after the neutron's discovery (James Chadwick, 1932). In 1939 J. Robert Oppenheimer and George Volkoff calculated the first neutron-star models with general relativity.
- A sugar-cube volume weighs ~hundreds of millions to a billion tonnes; surface gravity ~10¹¹ times Earth's; escape velocity roughly half the speed of light or more (~0.6 $c$ for a typical neutron star).
- Rapid rotation (conservation of angular momentum during collapse) and intense magnetic fields: ~10⁸ T for ordinary young pulsars, ~10⁴–10⁵ T for old millisecond pulsars, and ~10¹⁰–10¹¹ T for **magnetars** — the strongest magnetic fields known.
- **Pulsars:** rotating neutron stars beaming radiation from their magnetic poles, seen as regular pulses like a lighthouse. Discovered in 1967 by graduate student **Jocelyn Bell Burnell** (the signal was half-jokingly labeled "LGM-1", for "little green men"); Antony Hewish shared the 1974 Nobel Prize (controversially, without Bell Burnell). The Crab Pulsar spins 30 times per second; **millisecond pulsars** (spun up by accreting from a companion) up to ~716 times per second. Pulsars are extraordinarily precise clocks used to test general relativity (Hulse–Taylor binary) and to search for gravitational waves (pulsar timing arrays).
- **Maximum mass** (Tolman–Oppenheimer–Volkoff limit): ~2.2–2.3 $M_\odot$; the heaviest measured neutron stars are ~2.0–2.35 $M_\odot$.
- **Neutron-star mergers** (GW170817, 2017) produce kilonovae and heavy elements.

**Worked example 10.1 — life on a neutron star's surface.** Take $M = 1.4\,M_\odot = 2.785\times10^{30}$ kg and $R = 12$ km.
1. Density: $\rho = M/(\frac{4}{3}\pi R^3) = 2.785\times10^{30}/7.24\times10^{12} = 3.8\times10^{17}$ kg/m³. One cubic centimetre ($10^{-6}$ m³) holds $3.8\times10^{11}$ kg — about 380 million tonnes.
2. Surface gravity: $g = GM/R^2 = 6.674\times10^{-11}\times2.785\times10^{30}/(1.2\times10^4)^2 = 1.3\times10^{12}$ m/s², about $1.3\times10^{11}$ times Earth's.
3. Escape speed (Newtonian estimate): $v = \sqrt{2GM/R} = 1.76\times10^8$ m/s $= 0.59\,c$.

**Answer:** a neutron star is about as dense as an atomic nucleus, and its gravity is so strong that general relativity, not Newton's theory, is needed for precise work — light leaving the surface is noticeably redshifted and bent.

**Worked example 10.2 — why pulsars spin so fast.** Imagine (as an idealized thought experiment) that the Sun, which rotates once every 25.4 days at its equator, collapsed to a radius of 10 km while conserving angular momentum and keeping the same mass distribution.
1. Angular momentum $I\omega$ with $I \propto MR^2$ is conserved, so $\omega \propto R^{-2}$ and the period $P \propto R^2$.
2. Radius ratio: $10^4\ \text{m}/6.957\times10^8\ \text{m} = 1.44\times10^{-5}$; squared: $2.07\times10^{-10}$.
3. New period: $25.4\times86\,400\ \text{s}\times2.07\times10^{-10} = 4.5\times10^{-4}$ s.

**Answer:** about 0.5 milliseconds — a rotation rate of 2000 turns per second. Real collapsing cores lose angular momentum and newborn pulsars spin more slowly (tens of milliseconds), but the calculation shows why collapse naturally produces rapid rotators.

**Worked example 10.3 — the Crab Pulsar powers its nebula.** The Crab Pulsar has period $P = 0.0337$ s, slowing at $\dot{P} = 4.2\times10^{-13}$ s per second. Take the standard moment of inertia $I = 10^{38}$ kg·m².
1. Rotational energy: $E = \frac{1}{2}I\omega^2$ with $\omega = 2\pi/P$.
2. Differentiate: $\dot{E} = I\omega\dot{\omega}$, and $\dot{\omega} = -2\pi\dot{P}/P^2$, so the energy loss rate is $\lvert\dot{E}\rvert = 4\pi^2I\dot{P}/P^3$.
3. Substitute: $4\pi^2\times10^{38}\times4.2\times10^{-13}/(0.0337)^3 = 4.3\times10^{31}$ W.
4. Characteristic age: $\tau = P/(2\dot{P}) = 0.0337/(8.4\times10^{-13}) = 4.0\times10^{10}$ s $\approx 1300$ yr.

**Answer:** the pulsar loses about $4\times10^{31}$ W (about 100 000 $L_\odot$) of rotational energy — of the same order as the power radiated by the whole Crab Nebula, which shows that the spinning neutron star is the nebula's power source. The characteristic age of ~1300 years is a rough but reasonable match to the true age (the supernova was seen in 1054).

### Black holes
Regions where gravity is so strong that nothing, not even light, can escape (see the general relativity document).
- **Schwarzschild radius:** setting the Newtonian escape speed $\sqrt{2GM/r}$ equal to $c$ gives $r_s = 2GM/c^2$ — a heuristic argument used by John Michell (1783) and Pierre-Simon Laplace (1796) for "dark stars", which happens to give the exact event-horizon radius found by Karl Schwarzschild in general relativity (1916). Numerically $r_s = 2.95$ km per solar mass: 29.5 km for a 10 $M_\odot$ black hole, and only 8.9 mm for an object with Earth's mass.
- **Stellar-mass black holes** form from the collapse of the most massive stars; detected in X-ray binaries (Cygnus X-1, 1971) and through gravitational waves from mergers (LIGO/Virgo, since 2015); Gaia found dormant black holes in binaries (Gaia BH1, BH2, BH3 — the last ~33 $M_\odot$).
- **Supermassive black holes** (millions to billions of solar masses) at galactic centers; the Event Horizon Telescope imaged the shadows of those in M87 (2019) and the Milky Way's Sagittarius A* (2022).
- Matter falling into a black hole forms a hot **accretion disk**, emitting X-rays — accretion is the most efficient energy source known after matter–antimatter annihilation (up to ~6–42% of rest mass energy converted to radiation, vs. 0.7% for fusion).

## 11. Variable Stars and Binary Stars

- **Cepheid variables:** pulsating supergiants whose brightness varies with periods of days to months. The variability of Delta Cephei, the prototype, was discovered by John Goodricke in 1784. **Henrietta Swan Leavitt** (1908–1912) discovered the **period–luminosity relation** from Cepheids in the Small Magellanic Cloud — longer period means greater luminosity — making them **standard candles**. Edwin Hubble used Cepheids in the Andromeda "nebula" (1923–1924) to show it is a separate galaxy far beyond the Milky Way. Polaris is itself a low-amplitude Cepheid.
- **RR Lyrae** variables (old, low-mass, horizontal-branch stars; all have similar luminosities) — distance indicators for globular clusters.
- **Mira variables** (long-period pulsating AGB stars).
- **Eclipsing binaries** (Algol, "the Demon Star", dims every 2.87 days; Goodricke measured its period in 1783).
- **Cataclysmic variables** and novae (accreting white dwarfs).
- **X-ray binaries** (accreting neutron stars or black holes).

### Why Cepheids pulsate
Cepheids pulsate because of a valve in their outer layers, the **kappa ($\kappa$) mechanism**. In a zone where helium is partly ionized, compression increases the opacity instead of decreasing it, so the layer traps heat when compressed, pushes outward, becomes transparent as it expands, releases the heat and falls back — an engine that keeps the oscillation going. Eddington proposed such a valve in the 1910s–1920s; Sergei Zhevakin identified the helium ionization zone as its location in 1953.

The pulsation period is close to the time a sound wave or a free-falling layer needs to cross the star, which scales as $(G\bar{\rho})^{-1/2}$. Thus $P\sqrt{\bar{\rho}} \approx$ constant: large, low-density supergiants pulsate slowly, and since larger Cepheids are also more luminous, longer periods go with higher luminosity — the physical origin of Leavitt's law.

**Worked example 11.1 — a Cepheid distance.** One calibration of the visual period–luminosity relation, based on Hubble Space Telescope parallaxes of nearby Cepheids (Benedict and collaborators, 2007), is $M_V = -2.43(\log_{10}P - 1) - 4.05$ with $P$ in days. A Cepheid in a nearby galaxy has $P = 10.0$ days and mean apparent magnitude $\langle m_V\rangle = 20.4$. Ignore extinction.
1. $\log_{10}10.0 = 1$, so $M_V = -2.43\times0 - 4.05 = -4.05$.
2. Distance modulus: $m - M = 20.4 - (-4.05) = 24.45$.
3. $d = 10^{(24.45 + 5)/5} = 10^{5.89} = 7.8\times10^5$ pc.

**Answer:** about 780 kpc, or roughly 2.5 million light-years — comparable to the distance of the Andromeda Galaxy. Hubble's original calibration gave a distance under a million light-years; in 1952 Walter Baade recognized that there are two kinds of Cepheids with different luminosities, roughly doubling the extragalactic distance scale.

## 12. Star Clusters
- **Open clusters:** young (up to a few billion years), loosely bound groups of hundreds to thousands of stars in the galactic disk (the Pleiades, ~100 million years old; the Hyades).
- **Globular clusters:** ancient (~11–13 billion years), dense spherical swarms of 10⁵–10⁶ stars in the galactic halo (Omega Centauri, M13). The Milky Way has ~150–160.

Clusters are natural laboratories: all members formed at about the same time from the same gas and lie at the same distance, so differences between them are due to mass alone. As a cluster ages its main sequence is "eaten away" from the top, because the most massive stars leave first.

**Worked example 12.1 — a cluster age from the turnoff.** The most massive stars still on the main sequence in a cluster have about 1.3 $M_\odot$. Estimate the cluster's age.
1. Stars at the turnoff are just finishing core hydrogen burning, so the cluster's age equals their main-sequence lifetime.
2. $t \approx 10^{10}\ \text{yr}\times1.3^{-2.5} = 10^{10}\times0.519 = 5.2\times10^9$ yr.

**Answer:** about 5 billion years — similar to the Sun's age. This is a rough estimate; precise cluster ages come from fitting theoretical **isochrones** (curves of stars of equal age) to the whole color–magnitude diagram, and they typically come out somewhat younger for this turnoff mass.

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

The theory was laid out in 1957 in the paper by Margaret Burbidge, Geoffrey Burbidge, William Fowler and Fred Hoyle (known as B²FH) and independently by Alastair Cameron; Fowler shared the 1983 Nobel Prize with Chandrasekhar. Direct evidence that nucleosynthesis happens inside stars today came in 1952, when Paul Merrill detected technetium in the spectra of certain red giants. Technetium has no stable isotopes and none of its isotopes lives longer than a few million years — far shorter than the ages of those stars — so it must have been made inside them recently and mixed to the surface.

Neutron capture builds elements beyond iron because neutrons, being uncharged, face no Coulomb barrier. In the **s-process** (slow) a nucleus usually has time to beta-decay before capturing the next neutron, so the path hugs the valley of stable nuclei; in the **r-process** (rapid) the neutron flux is so intense that nuclei swell with neutrons before decaying back toward stability, producing the most neutron-rich heavy isotopes, including uranium and thorium.

The calcium in our bones, the iron in our blood, the oxygen we breathe and the gold in our jewelry were all forged in stars that lived and died before the Sun was born.

## 14. Historical Development: How We Learned What Stars Are

| Date | Discovery | People |
|---|---|---|
| 2nd century BCE | Naked-eye star catalogue with brightness classes (magnitudes) | Hipparchus |
| 1814 | Dark lines mapped in the solar spectrum | Joseph von Fraunhofer |
| 1838 | First stellar parallax (61 Cygni) | Friedrich Bessel |
| 1859–1860 | Spectral analysis; elements identified in the Sun | Gustav Kirchhoff, Robert Bunsen |
| 1868 | Helium discovered in the solar spectrum | Jules Janssen, Norman Lockyer |
| 1908–1912 | Cepheid period–luminosity relation | Henrietta Swan Leavitt |
| 1911–1913 | Hertzsprung–Russell diagram | Ejnar Hertzsprung, Henry Norris Russell |
| 1918–1924 | Henry Draper Catalogue; OBAFGKM sequence | Annie Jump Cannon and colleagues |
| 1920 | Hydrogen fusion proposed as the Sun's energy source | Arthur Eddington |
| 1925 | Stars are mostly hydrogen and helium | Cecilia Payne(-Gaposchkin) |
| 1926 | White dwarfs explained by electron degeneracy | Ralph Fowler |
| 1928–1929 | Quantum tunneling applied to stellar fusion | George Gamow; Robert Atkinson, Fritz Houtermans |
| 1930 | Upper mass limit of white dwarfs | Subrahmanyan Chandrasekhar |
| 1934 | Neutron stars and supernovae proposed | Walter Baade, Fritz Zwicky |
| 1938–1939 | pp chain and CNO cycle | Hans Bethe, Charles Critchfield, Carl Friedrich von Weizsäcker |
| 1955 | Initial mass function | Edwin Salpeter |
| 1957 | Theory of stellar nucleosynthesis (B²FH) | Burbidge, Burbidge, Fowler, Hoyle; Cameron |
| 1967 | Pulsars discovered | Jocelyn Bell Burnell, Antony Hewish |
| 1968 | Solar neutrino deficit reported | Raymond Davis Jr. |
| 1987 | Neutrinos from supernova SN 1987A | Kamiokande II, IMB and Baksan teams |
| 1995 | First confirmed brown dwarfs; first planet around a Sun-like star | Several teams; Michel Mayor, Didier Queloz |
| 1998 | Accelerating universe from Type Ia supernovae | Saul Perlmutter, Brian Schmidt, Adam Riess |
| 2015 | First gravitational waves (merging black holes) | LIGO Scientific Collaboration |
| 2017 | Neutron-star merger and kilonova (GW170817) | LIGO/Virgo and many observatories |
| 2019 | White-dwarf crystallization seen in Gaia data | Pier-Emmanuel Tremblay and colleagues |

The story shows a recurring pattern: new instruments (the spectroscope, photographic plates, radio telescopes, neutrino detectors, astrometric satellites, gravitational-wave interferometers) repeatedly opened new windows, and each time physics developed in terrestrial laboratories — atomic spectra, quantum mechanics, nuclear physics, relativity — turned out to be exactly what was needed to interpret them.

## 15. Applications in Technology, Medicine and Everyday Life

- **Fusion energy.** Fusion reactors on Earth cannot use the pp chain: its first step relies on the weak force and is far too slow. They use deuterium–tritium fusion (D + T → ⁴He + n + 17.6 MeV) instead, and because they lack the Sun's enormous density and confinement time, they need temperatures around 100–150 million K — roughly ten times hotter than the solar core. In December 2022 the National Ignition Facility in the United States released about 3.15 MJ of fusion energy from a target hit with 2.05 MJ of laser light, the first laboratory fusion "ignition"; the ITER tokamak is under construction in France.
- **Chemical analysis.** The spectroscopy that revealed stellar compositions is used every day in laboratories: atomic absorption and emission spectrometers measure lead in drinking water, trace metals in blood, and the composition of steel. Bunsen and Kirchhoff themselves discovered cesium (1860) and rubidium (1861) this way.
- **Medicine.** Helium, first found in the solar spectrum, is used as liquid helium to cool the superconducting magnets of MRI scanners. Gravitational-redshift and relativity corrections first tested on white dwarfs are the same physics that the GPS system must correct for.
- **Imaging detectors.** Astronomers were among the first users of the charge-coupled device (invented in 1969 by Willard Boyle and George Smith, Nobel 2009), and techniques for faint-light imaging developed for telescopes fed into digital cameras and medical X-ray imaging.
- **Navigation and timekeeping.** Sailors used stars for celestial navigation for centuries. Today pulsars are studied as natural clocks: in 2017 NASA's SEXTANT experiment aboard the International Space Station used X-ray pulsar timing to determine the station's orbit autonomously, a step toward pulsar navigation for deep-space probes. In 2023 pulsar timing arrays (including NANOGrav) reported evidence for a background of low-frequency gravitational waves.
- **Space weather.** Stellar activity matters on Earth: a solar storm caused the March 1989 blackout of the Quebec power grid, and power companies and satellite operators now monitor solar activity.
- **Everyday life and nature.** Human vision is most sensitive near 555 nm, close to the peak of sunlight, and photosynthesis evolved to use the visible solar spectrum. Silicon solar cells are designed around the Sun's spectrum. Earth's internal heat, which drives plate tectonics and the magnetic field, comes partly from the decay of uranium, thorium and potassium-40 — nuclei forged in earlier generations of stars.

## 16. Connections to Other Subjects

- **Thermodynamics and statistical physics:** blackbody radiation, the Boltzmann and Saha distributions, the virial theorem and the negative heat capacity of self-gravitating systems.
- **Quantum mechanics:** atomic energy levels (spectral lines), tunneling (fusion), the Pauli exclusion principle (white dwarfs and neutron stars).
- **Nuclear and particle physics:** binding energies, reaction rates, the weak interaction, neutrino oscillations and neutrino mass — a discovery that came from studying the Sun.
- **Relativity:** $E = mc^2$ (stellar energy), gravitational redshift (white dwarfs), event horizons, gravitational waves from merging remnants, and the binary pulsar as a test of general relativity.
- **Chemistry:** the origin of the periodic table's elements; spectroscopy; ionization equilibria (the Saha equation is the plasma analogue of a chemical equilibrium constant); molecules such as TiO in cool stellar atmospheres and CO and H₂ in star-forming clouds.
- **Biology:** the elements of life (carbon, nitrogen, oxygen, phosphorus, sulfur, iron) were made in stars; the habitable zone of a planetary system scales with the star's luminosity. Since a planet receives flux $L/(4\pi d^2)$, the distance receiving Earth-like flux is $d = \sqrt{L/L_\odot}$ AU — about 0.1 AU for a red dwarf with $L = 0.01\,L_\odot$. Long main-sequence lifetimes give life time to evolve.
- **Mathematics:** logarithms (magnitudes), power laws and log–log plots (mass–luminosity relation, IMF), the small-angle approximation (parallax), coupled differential equations (stellar structure), random walks (photon diffusion), error propagation (parallax distances).
- **Earth science:** the 19th-century debate over the ages of the Sun and Earth, radioactive heating of planetary interiors.
- **Cosmology:** Cepheids and Type Ia supernovae measure the expansion of the universe; the first generation of stars ended the cosmic "dark ages" and began the chemical enrichment of the cosmos.

## 17. Common Misconceptions

- **"Stars burn like fires."** Chemical burning releases only about $10^7$ J per kilogram. If the Sun's entire mass ($2\times10^{30}$ kg) burned like coal ($3\times10^7$ J/kg), it would last only about 5000 years at its present luminosity. Stars shine by nuclear fusion, which releases millions of times more energy per kilogram.
- **"The Sun is a yellow star."** The Sun's spectrum peaks in the blue-green and spans all visible colors, so its light is white. It appears yellow or orange near the horizon because the atmosphere scatters blue light out of the beam.
- **"Brighter-looking stars are closer or more powerful."** Apparent brightness depends on both luminosity and distance. Deneb, among the brightest stars in the sky, is a distant supergiant tens of thousands of times more luminous than the Sun, while the nearest star, Proxima Centauri, is invisible to the naked eye.
- **"Polaris is the brightest star in the sky."** It is only about the 50th brightest. It is famous because it lies close to the north celestial pole.
- **"More massive stars live longer because they have more fuel."** They do have more fuel, but they burn it at a rate that rises much faster than their mass ($L \propto M^{3.5}$), so their lifetimes are far shorter.
- **"Fusion happens because the core is hot enough for protons to overcome their repulsion."** At 15.7 million K a typical proton has about a thousandth of the energy needed to climb over the Coulomb barrier. Fusion happens only because of quantum tunneling.
- **"A star's core cools when its fuel runs out."** The opposite happens: losing energy makes a self-gravitating core contract and heat up (negative heat capacity), which is how heavier fuels eventually ignite.
- **"The Sun will explode as a supernova or become a black hole."** The Sun is far too low in mass. It will become a red giant, eject a planetary nebula and end as a white dwarf of about 0.5–0.6 $M_\odot$.
- **"Black holes suck in everything around them."** Far from a black hole, its gravity is the same as that of any object with the same mass. If the Sun were replaced by a one-solar-mass black hole, Earth's orbit would not change (though Earth would freeze).
- **"Neutron stars are made purely of neutrons."** They have a solid crust of nuclei and electrons, and their interiors contain a few percent protons and electrons; the composition of the deepest core is still uncertain.
- **"Planetary nebulae are related to planets."** The name comes from their disk-like appearance in small telescopes; they are gas shells ejected by dying stars.
- **"Many of the stars we see have already died."** Most naked-eye stars are within a few thousand light-years and live millions to billions of years, so the light from nearly all of them left stars that still exist.
- **"Twinkling is a property of the star."** Twinkling is caused by turbulence in Earth's atmosphere; seen from space, stars do not twinkle.
- **"The Sun is an average star."** Because most stars are red dwarfs, the Sun is more massive and more luminous than the large majority of stars in the Milky Way.
- **"White dwarfs are dead, dark objects."** A newborn white dwarf has a surface temperature above 100 000 K; it shines for billions of years from stored heat, and none in the universe has yet cooled to a black dwarf.

## 18. Practice Problems

1. (Easy) Two stars differ in apparent magnitude by 7.5. What is the ratio of their fluxes?
2. (Easy, conceptual) Two stars have the same apparent magnitude. Star A has parallax $0.10''$ and star B has parallax $0.010''$. Which is more luminous, and by what factor?
3. (Medium) A star has apparent visual magnitude $m = 8.0$ and lies at 50 pc. Ignoring extinction, find its absolute magnitude and its visual luminosity relative to the Sun ($M_\odot = 4.83$).
4. (Medium) A star has $T_{\text{eff}} = 10\,000$ K and $L = 50\,L_\odot$. Find its radius in solar radii (take $T_\odot = 5772$ K) and the wavelength at which its spectrum peaks.
5. (Medium) In a visual binary the orbital period is 10.0 years and the relative semimajor axis is 8.0 AU. Star A is three times closer to the center of mass than star B. Find both masses.
6. (Medium) Use the scaling laws $L \propto M^{3.5}$ and $t \approx 10^{10}\ \text{yr}\,(M/M_\odot)^{-2.5}$ to estimate the luminosity and main-sequence lifetime of a 2.0 $M_\odot$ star.
7. (Conceptual) Explain, using the virial theorem, why the core of a star heats up after it exhausts its hydrogen, even though fusion in the core has stopped.
8. (Medium) A molecular cloud core has a Jeans mass of 5 $M_\odot$. If its temperature doubles and its density increases by a factor of 4, what is the new Jeans mass?
9. (Conceptual, with numbers) Explain why the hydrogen Balmer lines are weak in both O stars (above 30 000 K) and M stars (below 3700 K), but strong in A stars. Use the Boltzmann factor for level $n = 2$ at 5800 K, 10 000 K and 20 000 K in your answer.
10. (Medium) A Cepheid has a period of 30.0 days and mean apparent magnitude $\langle m_V\rangle = 25.0$. Using $M_V = -2.43(\log_{10}P - 1) - 4.05$ and ignoring extinction, find its distance.
11. (Hard) A core-collapse supernova 10 kpc away emits $3\times10^{46}$ J in neutrinos with mean energy 10 MeV. How many neutrinos pass through each square metre at Earth, and how many pass through a person with a cross-sectional area of 0.5 m²?
12. (Medium, conceptual) Compute the Schwarzschild radius of a 3.0 $M_\odot$ object and compare it with a typical neutron-star radius of 12 km. Why can a neutron star not exceed about 2–3 $M_\odot$, even though a 3 $M_\odot$, 12 km object would still be larger than its event horizon?

### Solutions

**1.** Flux ratio $= 10^{0.4\Delta m} = 10^{0.4\times7.5} = 10^3$. **Answer:** a factor of 1000.

**2.** Distances: $d_A = 1/0.10 = 10$ pc and $d_B = 1/0.010 = 100$ pc. Equal apparent magnitudes mean equal fluxes, and $L = 4\pi d^2F$, so $L_B/L_A = (d_B/d_A)^2 = 10^2$. **Answer:** star B is 100 times more luminous.

**3.**
1. $5\log_{10}50 = 8.49$.
2. $M = m - 5\log_{10}d + 5 = 8.0 - 8.49 + 5 = 4.51$.
3. $L/L_\odot = 10^{(4.83 - 4.51)/2.5} = 10^{0.13} = 1.35$.

**Answer:** $M \approx 4.5$, and the star emits about 1.35 times the Sun's visible light.

**4.**
1. $R/R_\odot = (L/L_\odot)^{1/2}(T_\odot/T)^2 = \sqrt{50}\times(5772/10\,000)^2$.
2. $\sqrt{50} = 7.07$ and $(0.5772)^2 = 0.333$, so $R = 2.36\,R_\odot$.
3. $\lambda_{\max} = 2.898\times10^{-3}/10\,000 = 2.90\times10^{-7}$ m.

**Answer:** about 2.4 $R_\odot$; the spectrum peaks at 290 nm, in the ultraviolet (the star looks white to blue-white).

**5.**
1. Total mass: $M_A + M_B = a^3/P^2 = 8.0^3/10.0^2 = 512/100 = 5.12\,M_\odot$.
2. Center of mass: $M_Aa_A = M_Ba_B$ with $a_B = 3a_A$, so $M_A = 3M_B$.
3. $4M_B = 5.12$, so $M_B = 1.28\,M_\odot$ and $M_A = 3.84\,M_\odot$.

**Answer:** $M_A \approx 3.8\,M_\odot$, $M_B \approx 1.3\,M_\odot$.

**6.**
1. $L \approx 2.0^{3.5}\,L_\odot = 11.3\,L_\odot$.
2. $t \approx 10^{10}\times2.0^{-2.5}$ yr $= 10^{10}\times0.177$ yr $= 1.8\times10^9$ yr.

**Answer:** roughly 11 $L_\odot$ (the steeper fit $L \propto M^4$ for this range gives about 16 $L_\odot$; real 2 $M_\odot$ stars lie in between) and about 1.8 billion years — less than a fifth of the Sun's lifetime.

**7.** For a bound, self-gravitating gas in equilibrium, $2K + U = 0$, so the total energy is $E = -K$. When core fusion stops, the core still loses energy (to the surrounding layers and ultimately to space). Losing energy makes $E$ more negative, so $K$ increases: the core contracts, gravitational potential energy is released, half of it is radiated and half heats the gas. The core temperature therefore rises until it is hot enough either to ignite the next fuel (helium at ~100 million K) or until degeneracy pressure halts the contraction. This "negative heat capacity" drives each step of stellar evolution.

**8.**
1. $M_J \propto T^{3/2}\rho^{-1/2}$.
2. Factor: $2^{3/2}\times4^{-1/2} = 2.83/2 = 1.41$.
3. New mass: $5\times1.41 = 7.1\,M_\odot$.

**Answer:** about 7 $M_\odot$ — heating stabilizes the cloud more than the compression destabilizes it.

**9.** Balmer absorption requires neutral hydrogen with its electron in level $n = 2$. The Boltzmann factor $N_2/N_1 = 4e^{-10.2\ \text{eV}/k_BT}$ is $5\times10^{-9}$ at 5800 K, $3\times10^{-5}$ at 10 000 K and $1\times10^{-2}$ at 20 000 K. In M stars, therefore, practically no hydrogen atoms are excited to $n = 2$, so the lines are weak. As the temperature rises the excited fraction grows rapidly, but by 20 000–30 000 K the Saha equation shows that nearly all hydrogen is ionized, leaving few neutral atoms to absorb. The product of "enough atoms excited" and "enough atoms still neutral" peaks near 9000–10 000 K — the A stars. **Answer:** the lines are weak in M stars because of too little excitation and weak in O stars because of too much ionization.

**10.**
1. $\log_{10}30.0 = 1.477$, so $M_V = -2.43\times0.477 - 4.05 = -5.21$.
2. $m - M = 25.0 + 5.21 = 30.21$.
3. $d = 10^{(30.21 + 5)/5} = 10^{7.04} = 1.1\times10^7$ pc.

**Answer:** about 11 Mpc, or roughly 36 million light-years — a galaxy well beyond the Local Group.

**11.**
1. Neutrino energy: $10\ \text{MeV}\times1.602\times10^{-13}\ \text{J/MeV} = 1.602\times10^{-12}$ J.
2. Number emitted: $N = 3\times10^{46}/1.602\times10^{-12} = 1.9\times10^{58}$.
3. Distance: $10\ \text{kpc} = 10^4\times3.086\times10^{16}\ \text{m} = 3.086\times10^{20}$ m; sphere area $4\pi d^2 = 1.20\times10^{42}$ m².
4. Fluence: $1.9\times10^{58}/1.20\times10^{42} = 1.6\times10^{16}$ m⁻².
5. Through a person: $1.6\times10^{16}\times0.5 = 8\times10^{15}$.

**Answer:** about $1.6\times10^{16}$ neutrinos per square metre, so roughly $8\times10^{15}$ pass through a person within about 10 seconds — harmlessly, since nearly all of them pass straight through. Large detectors such as Super-Kamiokande would record thousands of events from such a galactic supernova.

**12.**
1. $r_s = 2.95\ \text{km}\times3.0 = 8.9$ km.
2. A 12 km object of 3 $M_\odot$ would be larger than its event horizon, so it is not "already a black hole".

**Answer:** $r_s \approx 8.9$ km. The limit on neutron-star masses comes not from the horizon but from pressure support: in general relativity pressure itself contributes to gravity, and above the Tolman–Oppenheimer–Volkoff mass (about 2.2–2.3 $M_\odot$ for realistic nuclear matter) no equation of state can provide enough pressure to resist collapse. The star then collapses inside its Schwarzschild radius and becomes a black hole.

## 19. Summary and Key Equations

| Concept | Formula / Key fact |
|---|---|
| Parallax distance | $d\,(\text{pc}) = 1/p\,('')$ |
| Inverse-square law | $F = L/(4\pi d^2)$ |
| Magnitudes | 5 mag = 100× in brightness; $m_1 - m_2 = -2.5\log_{10}(F_1/F_2)$ |
| Distance modulus | $m - M = 5\log_{10}d - 5$ (plus extinction $A$) |
| Bolometric magnitude | $M_{\text{bol}} = 4.74 - 2.5\log_{10}(L/L_\odot)$ |
| Stefan–Boltzmann | $L = 4\pi R^2\sigma T^4$ |
| Wien's law | $\lambda_{\max}T = 2.898\times10^{-3}$ m·K |
| Doppler shift | $v_r = c\,\Delta\lambda/\lambda_0$ |
| Spectral classes | O B A F G K M (hot → cool); Sun G2V |
| Binary masses | $M_1 + M_2 = a^3/P^2$ (AU, yr, $M_\odot$); $M_1a_1 = M_2a_2$ |
| Mass–luminosity | $L \propto M^{3.5}$ |
| Lifetime | $t \approx 10^{10}(M/M_\odot)^{-2.5}$ years |
| Hydrostatic equilibrium | $dP/dr = -GM(r)\rho/r^2$ |
| Virial theorem | $2K + U = 0$; stars heat up as they lose energy |
| Kelvin–Helmholtz time | $t_{\text{KH}} \sim GM^2/(RL) \approx 3\times10^7$ yr for the Sun |
| Hydrogen fusion | $4\,^1\text{H}\to{}^4\text{He}$, 26.7 MeV, 0.7% of mass |
| Eddington luminosity | $L_{\text{Edd}} = 4\pi GMm_pc/\sigma_T \approx 3.3\times10^4\,L_\odot\,(M/M_\odot)$ |
| Jeans mass | $M_J = (5k_BT/(G\mu m_H))^{3/2}(3/(4\pi\rho))^{1/2}$ |
| Free-fall time | $t_{\text{ff}} = \sqrt{3\pi/(32G\rho)}$ |
| Initial mass function | $dN/dM \propto M^{-2.35}$ (Salpeter) |
| Low-mass fate | Red giant → planetary nebula → white dwarf |
| High-mass fate | Supergiant → core-collapse supernova → neutron star or black hole |
| Chandrasekhar limit | ~1.4 $M_\odot$; white-dwarf radius $R \propto M^{-1/3}$ |
| Schwarzschild radius | $r_s = 2GM/c^2 \approx 2.95$ km per $M_\odot$ |
| Pulsar spin-down power | $\dot{E} = 4\pi^2I\dot{P}/P^3$ |
| Cepheid law | Longer period → higher luminosity |

### Useful constants

| Constant | Value |
|---|---|
| Gravitational constant $G$ | $6.674\times10^{-11}$ N m² kg⁻² |
| Speed of light $c$ | $2.998\times10^8$ m/s |
| Stefan–Boltzmann constant $\sigma$ | $5.670\times10^{-8}$ W m⁻² K⁻⁴ |
| Boltzmann constant $k_B$ | $1.381\times10^{-23}$ J/K |
| Planck constant $h$ | $6.626\times10^{-34}$ J s |
| Proton mass $m_p$ | $1.673\times10^{-27}$ kg |
| Atomic mass unit | 1 u = 931.494 MeV/$c^2$ |
| Wien constant | $2.898\times10^{-3}$ m·K |
| Astronomical unit | $1.496\times10^{11}$ m |
| Parsec | $3.086\times10^{16}$ m = 3.26 ly = 206 265 AU |
| Solar mass, radius, luminosity | $1.989\times10^{30}$ kg; $6.957\times10^8$ m; $3.828\times10^{26}$ W |

Stars are understood through a chain of reasoning that starts with simple measurements of light and ends with nuclear physics, quantum mechanics and general relativity. Their properties are set mainly by mass: mass determines a star's luminosity, temperature, lifetime and fate, and the deaths of stars seed the galaxy with the elements from which new stars, planets and living things form.
