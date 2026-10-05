---
title: Lasers and Modern Optics
field: Physics
subfield: Waves and Optics
level: high-school to undergraduate
keywords: [laser, absorption, spontaneous emission, stimulated emission, Einstein coefficients, population inversion, gain coefficient, laser threshold, three-level laser, four-level laser, optical cavity, longitudinal modes, free spectral range, finesse, coherence length, coherence time, Gaussian beam, Rayleigh range, beam divergence, helium-neon laser, diode laser, Nd:YAG laser, CO2 laser, fiber laser, Q-switching, mode-locking, ultrafast laser, holography, optical fiber, numerical aperture, modal dispersion, chromatic dispersion, nonlinear optics, second-harmonic generation, phase matching, Michelson interferometer, LIGO, optical coherence tomography, laser safety]
---

# Lasers and Modern Optics

A light bulb and a laser pointer may both glow red, yet they are profoundly different sources. The bulb's light spreads in every direction, contains a broad jumble of wavelengths, and is emitted by billions of atoms acting independently. The laser's light leaves in a pencil-thin beam, occupies a sliver of the spectrum, and behaves as a single, orderly wave whose crests stay in step over distances of metres or even kilometres. The photons are the same kind of particle in both cases; what differs is how they are organized. That organization is created by **stimulated emission**, a process Albert Einstein identified in 1916–1917, and the word *laser* is an acronym for **L**ight **A**mplification by **S**timulated **E**mission of **R**adiation.

Since the first laser operated in 1960, lasers have become one of the defining technologies of modern life. They carry nearly all long-distance internet traffic through glass fibers, read barcodes at every checkout, reshape corneas, cut steel, pattern the transistors of computer chips, and measure the distance to the Moon. In basic science they cool atoms to millionths of a kelvin and, in the LIGO observatories, sense changes in length a few thousandths of the diameter of a proton.

This chapter builds the physics of lasers from the ground up. We start with how atoms absorb and emit light and derive Einstein's relations between the rates of these processes. We then show why amplification needs a **population inversion**, why three- and four-level schemes are needed to produce one, and how an **optical cavity** turns an amplifier into an oscillator with discrete **longitudinal modes**. We quantify **coherence** and derive the properties of **Gaussian beams**. We survey the main laser types and the pulsed techniques that reach femtosecond durations, and then turn to "modern optics" made possible by lasers: **holography**, **optical fibers** and **dispersion**, **nonlinear optics** (second-harmonic generation), and **interferometry** from Michelson to LIGO. We finish with applications, **laser safety**, common misconceptions, practice problems and a summary. The chapter assumes familiarity with wave optics (interference and diffraction), the photon energy $E = h\nu$, and the Boltzmann distribution.

## 1. Historical Development

- **1887 – Michelson and Morley.** Albert Michelson's interferometer, built to detect motion through the "ether", found no such effect. The same instrument, scaled up enormously, became the LIGO gravitational-wave detector. Michelson received the Nobel Prize in 1907 for his precision optical instruments.
- **1916–1917 – Einstein's quantum theory of radiation.** Re-deriving Planck's blackbody law from rate equations, Einstein showed that equilibrium requires a third process besides absorption and spontaneous emission: **stimulated (induced) emission**, in which an incoming photon triggers an excited atom to emit an identical photon.
- **1948 – Holography.** Dennis Gabor invented holography while trying to improve electron microscopes, long before a suitably coherent light source existed. He received the Nobel Prize in 1971.
- **1954 – The maser.** Charles Townes, James Gordon and Herbert Zeiger at Columbia University built a microwave amplifier using stimulated emission in ammonia molecules. Nikolai Basov and Alexander Prokhorov in Moscow developed the theory independently; the three shared the 1964 Nobel Prize.
- **1957–1958 – The optical maser proposed.** Gordon Gould coined the word "laser" in his 1957 notebooks, and Arthur Schawlow and Townes published a detailed proposal for "optical masers" using a Fabry–Pérot cavity in 1958.
- **16 May 1960 – The first laser.** Theodore Maiman at Hughes Research Laboratories obtained pulsed red light at 694.3 nm from a flash-pumped ruby crystal.
- **December 1960 – First gas laser.** Ali Javan, William Bennett and Donald Herriott at Bell Labs operated a continuous helium–neon laser at 1.15 µm; the familiar red 632.8 nm HeNe line followed in 1962.
- **1961 – Nonlinear optics begins.** Peter Franken and colleagues at the University of Michigan focused a ruby laser into quartz and detected ultraviolet light at 347 nm, half the ruby wavelength: second-harmonic generation. Famously, the faint harmonic spot was removed from the published photograph by the journal's production staff, who mistook it for a speck of dirt.
- **1962 – Semiconductor lasers.** Robert N. Hall's group at General Electric, and groups at IBM and MIT Lincoln Laboratory, demonstrated gallium arsenide diode lasers; Nick Holonyak made the first visible-light version. Practical room-temperature continuous operation came with double-heterostructure designs around 1970 (Zhores Alferov in Leningrad; Izuo Hayashi and Morton Panish at Bell Labs). Alferov and Herbert Kroemer shared the 2000 Nobel Prize.
- **1962–1964 – Practical holography.** Emmett Leith and Juris Upatnieks introduced off-axis laser holography in the USA, and Yuri Denisyuk invented reflection holograms in the USSR.
- **1964 – Workhorse lasers.** C. Kumar N. Patel invented the CO₂ laser, and J. E. Geusic, H. M. Marcos and L. G. Van Uitert demonstrated the Nd:YAG laser, both at Bell Labs.
- **1966–1970 – Optical fibers.** Charles Kao and George Hockham argued that glass fibers could carry signals over long distances if impurities were removed (Kao: Nobel Prize 2009). In 1970 Robert Maurer, Donald Keck and Peter Schultz at Corning made fiber with loss below 20 dB/km.
- **1985 – Chirped-pulse amplification.** Donna Strickland and Gérard Mourou showed how to amplify ultrashort pulses to enormous peak powers (Nobel Prize 2018, shared with Arthur Ashkin for optical tweezers).
- **1987 – Erbium-doped fiber amplifier.** Groups led by David Payne (Southampton) and Emmanuel Desurvire (Bell Labs) demonstrated the optical amplifier that made transoceanic fiber links practical.
- **1991 – Ultrafast and imaging milestones.** Kerr-lens mode-locking of the titanium-sapphire laser (Spence, Kean and Sibbett) made femtosecond pulses routine, and optical coherence tomography was introduced for imaging the eye.
- **14 September 2015 – Gravitational waves.** Both LIGO detectors recorded the merger of two black holes; Rainer Weiss, Barry Barish and Kip Thorne received the 2017 Nobel Prize.

## 2. How Light and Atoms Exchange Energy

### 2.1 Three radiative processes
Consider an atom with two energy levels, a lower level 1 with energy $E_1$ and an upper level 2 with energy $E_2$, and light of frequency $\nu$ close to the transition frequency $\nu_0 = (E_2 - E_1)/h$. Three processes can occur:

1. **Absorption.** An atom in level 1 absorbs a photon and jumps to level 2. The rate depends on how much light is present.
2. **Spontaneous emission.** An atom in level 2 drops to level 1 on its own, emitting a photon in a random direction, with random phase and polarization. This is how ordinary lamps, flames and the Sun emit light.
3. **Stimulated emission.** An incoming photon of the right frequency induces an atom in level 2 to drop to level 1 and emit a second photon that is a *copy* of the first: same frequency, same direction, same phase and same polarization. One photon in, two identical photons out. This is the amplification step in a laser.

Energy is conserved in all three: the emitted or absorbed photon carries exactly $E_2 - E_1$ (within the linewidth of the transition).

### 2.2 Einstein's rate equations
Let $N_1$ and $N_2$ be the number densities (atoms per m³) in the two levels, $g_1$ and $g_2$ their degeneracies, and $\rho(\nu)$ the spectral energy density of the radiation (J m⁻³ Hz⁻¹). Einstein wrote the rates per unit volume as:
$$\text{absorption: } B_{12}\,\rho(\nu)\,N_1, \qquad \text{stimulated emission: } B_{21}\,\rho(\nu)\,N_2, \qquad \text{spontaneous emission: } A_{21}\,N_2$$
$A_{21}$ (units s⁻¹) is the probability per unit time of spontaneous decay, and $B_{12}$, $B_{21}$ are the **Einstein B coefficients**. In the absence of radiation, the upper level decays as $N_2(t) = N_2(0)e^{-A_{21}t}$, so the **radiative lifetime** is $\tau = 1/A_{21}$.

### 2.3 Derivation of the Einstein relations
The three coefficients are not independent. Einstein's argument uses thermal equilibrium at temperature $T$:

1. In equilibrium the upward and downward rates balance:
$$B_{12}\,\rho\,N_1 = A_{21}N_2 + B_{21}\,\rho\,N_2$$
2. Solve for $\rho$:
$$\rho(\nu) = \frac{A_{21}}{B_{12}(N_1/N_2) - B_{21}}$$
3. In equilibrium the populations follow the Boltzmann distribution, $N_2/N_1 = (g_2/g_1)e^{-h\nu/k_BT}$, so
$$\rho(\nu) = \frac{A_{21}}{B_{12}(g_1/g_2)e^{h\nu/k_BT} - B_{21}}$$
4. This must agree with Planck's law for every temperature:
$$\rho(\nu) = \frac{8\pi h\nu^3}{c^3}\,\frac{1}{e^{h\nu/k_BT} - 1}$$
5. Comparing the denominators, the two expressions match for all $T$ only if
$$\boxed{g_1B_{12} = g_2B_{21}}, \qquad \boxed{\frac{A_{21}}{B_{21}} = \frac{8\pi h\nu^3}{c^3}}$$
(In a medium of refractive index $n$, $c$ is replaced by $c/n$.)

Three lessons follow. First, stimulated emission is not optional: without the $B_{21}$ term, step 4 would give Wien's law instead of Planck's. Second, absorption and stimulated emission are mirror-image processes with the same strength per atom (for equal degeneracies), so whichever level holds more atoms wins. Third, the ratio $A_{21}/B_{21}$ grows as $\nu^3$: at high frequencies spontaneous emission dominates, which is one reason ultraviolet and X-ray lasers are much harder to build than microwave masers.

The ratio of stimulated to spontaneous emission rates in thermal radiation is
$$\frac{B_{21}\rho}{A_{21}} = \frac{1}{e^{h\nu/k_BT} - 1}$$
which equals the average number of photons per mode of the radiation field.

### Worked example 2.1 – Stimulated versus spontaneous emission
**Problem:** For the 632.8 nm helium–neon transition, find the photon energy and, in thermal equilibrium, the ratio of stimulated to spontaneous emission (a) at room temperature, 300 K, and (b) at the solar surface, 5800 K. Compare with a 1.0 GHz microwave transition at 300 K.

1. Frequency: $\nu = c/\lambda = (2.998\times10^8)/(632.8\times10^{-9}) = 4.738\times10^{14}$ Hz.
2. Photon energy: $h\nu = 3.139\times10^{-19}$ J $= 1.959$ eV.
3. At 300 K, $k_BT = 4.142\times10^{-21}$ J, so $x = h\nu/k_BT = 75.8$ and the ratio is $1/(e^{75.8} - 1) \approx 1.2\times10^{-33}$.
4. At 5800 K, $x = 3.92$, giving $1/(e^{3.92} - 1) = 0.020$.
5. For 1.0 GHz at 300 K, $x = 1.60\times10^{-4}$, so the ratio is $\approx 1/x = 6.3\times10^3$.

**Answer:** In thermal light at visible wavelengths, stimulated emission is utterly negligible at room temperature ($10^{-33}$) and only about 2% even at the surface of the Sun. At microwave frequencies it dominates. Optical lasers must therefore create conditions far from thermal equilibrium, which is why the maser came before the laser.

### 2.4 Lifetimes and linewidths
A level that decays with lifetime $\tau$ emits a wave train that dies away in a time of order $\tau$, so by the time–frequency uncertainty of Fourier analysis the line has a **natural linewidth** (full width at half maximum)
$$\Delta\nu_{\text{nat}} = \frac{1}{2\pi\tau}$$
The sodium 589 nm transition, with $\tau = 16.2$ ns, has $\Delta\nu_{\text{nat}} = 9.8$ MHz. In a gas, the thermal motion of atoms adds **Doppler broadening**, which for a Maxwell–Boltzmann velocity distribution has a full width
$$\Delta\nu_D = \nu_0\sqrt{\frac{8k_BT\ln 2}{mc^2}}$$
typically about 1 GHz for visible lines. In solids, interactions with the host lattice broaden lines further, to terahertz widths in some materials.

Laser media favor **metastable** upper levels, whose long lifetimes let a large population accumulate:

| Gain medium | Laser wavelength | Upper-level lifetime (approx.) |
|---|---|---|
| Ruby (Cr³⁺:Al₂O₃) | 694.3 nm | 3 ms |
| Nd:YAG | 1064 nm | 230 µs |
| Er³⁺ in silica fiber | ≈ 1550 nm | 10 ms |
| Ti:sapphire (Ti³⁺:Al₂O₃) | 650–1100 nm | 3.2 µs |
| Allowed atomic transition (e.g. Na 589 nm) | 589 nm | 16 ns |

## 3. Absorption, Gain and Population Inversion

### 3.1 From rate equations to the gain coefficient
Send a beam with photon flux density $\Phi$ (photons m⁻² s⁻¹) through a thin slab of thickness $dz$ and area $A$. Describe the strength of the transition by a **cross-section** $\sigma$ (m²): the stimulated-emission rate per excited atom is $\sigma\Phi$, and, for equal degeneracies, the absorption rate per ground-state atom is also $\sigma\Phi$ (this is the relation $g_1B_{12} = g_2B_{21}$ again).

1. Photons added to the beam per second by stimulated emission: $\sigma\Phi\,N_2A\,dz$.
2. Photons removed per second by absorption: $\sigma\Phi\,N_1A\,dz$.
3. Spontaneous emission goes in all directions, so almost none of it joins the beam; we neglect it.
4. The change in photon flow is $A\,d\Phi = \sigma\Phi(N_2 - N_1)A\,dz$, so
$$\frac{d\Phi}{dz} = \sigma(N_2 - N_1)\Phi$$
5. Multiplying by $h\nu$ to get intensity $I$ and integrating:
$$\boxed{I(z) = I(0)\,e^{gz}, \qquad g = \sigma(N_2 - N_1) = \sigma\,\Delta N}$$

In thermal equilibrium $N_1 > N_2$, so $g$ is negative and we recover the **Beer–Lambert law** of absorption, $I = I_0e^{-\alpha z}$ with absorption coefficient $\alpha = \sigma(N_1 - N_2) \approx \sigma N_1$. Light is amplified only if $N_2 > N_1$: a **population inversion**. Formally, the Boltzmann factor would then require a negative absolute temperature, which signals that an inverted medium is far from equilibrium and must be continuously **pumped** by an outside energy source (light, electric discharge, electric current or chemical reaction).

### 3.2 Why a two-level system cannot be inverted
Pump a two-level system (equal degeneracies) with light at the transition frequency, giving an upward rate $W$ per atom. The same light stimulates emission at the same rate $W$ per excited atom:
$$\frac{dN_2}{dt} = WN_1 - WN_2 - A_{21}N_2$$
In steady state, $dN_2/dt = 0$ gives
$$\frac{N_2}{N_1} = \frac{W}{W + A_{21}} < 1$$
However strong the pump, $N_2$ only approaches $N_1$: the medium becomes transparent (**saturated**) but never inverted. The pump must therefore act through additional levels.

### 3.3 Three-level lasers
In a **three-level laser** such as ruby, the pump lifts atoms from the ground level 1 to a broad level (or band) 3, which decays very quickly and without radiation to the metastable upper laser level 2. The laser transition is 2 → 1. Because level 3 empties almost instantly, $N_3 \approx 0$ and $N_1 + N_2 = N$. With pump rate $W_p$ per ground-state atom and upper-level lifetime $\tau$:

1. Rate equation (below threshold, so stimulated emission is negligible):
$$\frac{dN_2}{dt} = W_pN_1 - \frac{N_2}{\tau}$$
2. Steady state: $N_2/N_1 = W_p\tau$.
3. Using $N_1 + N_2 = N$:
$$\frac{\Delta N}{N} = \frac{N_2 - N_1}{N} = \frac{W_p\tau - 1}{W_p\tau + 1}$$

Inversion requires $W_p\tau > 1$, so a long lifetime helps, but the real handicap is that the *lower* laser level is the ground state: more than half of all atoms must be pumped out of it before any gain appears. Maiman's ruby laser needed an intense flash lamp for exactly this reason, and three-level lasers usually run in pulses.

### 3.4 Four-level lasers
In a **four-level laser** such as Nd:YAG, the pump takes atoms from the ground level 0 to a pump level 3, which decays rapidly to the upper laser level 2. Lasing occurs from 2 to a lower level 1 that lies well above the ground state and itself empties very quickly to level 0. Thus $N_1 \approx 0$ and $N_3 \approx 0$:

1. $dN_2/dt = W_pN_0 - N_2/\tau$, so in steady state $N_2 = W_p\tau N_0$.
2. Since $N_1 \approx 0$, $\Delta N = N_2 - N_1 \approx N_2 = N\,\dfrac{W_p\tau}{1 + W_p\tau}$.

Now $\Delta N > 0$ for *any* pumping rate: there is no need to pump half the atoms first. Only a tiny inverted fraction is needed to exceed the cavity losses, so four-level lasers have far lower thresholds and run continuously with ease. For Nd:YAG the lower laser level lies about 0.25 eV above the ground state, so at 300 K its thermal population is only about $e^{-0.25/0.0259} \approx 7\times10^{-5}$ of the ground-state population.

### 3.5 Laser threshold
Place a gain medium of length $l$ between mirrors of reflectance $R_1$ and $R_2$. Let $T_i$ be the fraction of power that survives other losses (scattering, absorption, diffraction) in a round trip. After one round trip, intensity is multiplied by $R_1R_2T_ie^{2gl}$. Oscillation starts when the round-trip gain equals the round-trip loss:
$$R_1R_2T_i\,e^{2g_{\text{th}}l} = 1 \quad\Longrightarrow\quad \boxed{g_{\text{th}} = \frac{1}{2l}\ln\frac{1}{R_1R_2T_i}}, \qquad \Delta N_{\text{th}} = \frac{g_{\text{th}}}{\sigma}$$

### Worked example 3.1 – Threshold of a diode-pumped Nd:YAG laser
**Problem:** An Nd:YAG rod 7.5 cm long, doped with 1.0% Nd (Nd³⁺ density $N = 1.38\times10^{26}$ m⁻³), sits between a mirror with $R_1 = 0.998$ and an output coupler with $R_2 = 0.90$. Other round-trip losses are 2.0% ($T_i = 0.98$). The stimulated-emission cross-section at 1064 nm is $\sigma = 2.8\times10^{-23}$ m². Find the threshold gain coefficient and inversion, and compare with what a three-level system would require.

1. Round-trip loss factor: $R_1R_2T_i = 0.998 \times 0.90 \times 0.98 = 0.8802$.
2. $\ln(1/0.8802) = 0.1276$.
3. $g_{\text{th}} = 0.1276/(2 \times 0.075\ \text{m}) = 0.851$ m⁻¹.
4. $\Delta N_{\text{th}} = g_{\text{th}}/\sigma = 0.851/(2.8\times10^{-23}) = 3.0\times10^{22}$ m⁻³.
5. Fraction of Nd ions that must be inverted: $3.04\times10^{22}/1.38\times10^{26} = 2.2\times10^{-4}$, about 0.02%.
6. A three-level medium with the same ion density would first need $N/2 = 6.9\times10^{25}$ m⁻³ excited ions just to reach transparency, about 2300 times more.

**Answer:** $g_{\text{th}} \approx 0.85$ m⁻¹ and $\Delta N_{\text{th}} \approx 3.0\times10^{22}$ m⁻³ (0.02% of the ions). The four-level scheme lowers the threshold by more than three orders of magnitude.

### 3.6 Above threshold
Once pumped above threshold, the intracavity power grows until stimulated emission depletes the inversion back to $\Delta N_{\text{th}}$: the gain is **clamped** at the loss. Extra pump power then goes into extra output, so the output power rises roughly linearly, $P_{\text{out}} \approx \eta_s(P_{\text{pump}} - P_{\text{th}})$, where $\eta_s$ is the **slope efficiency**. Its upper limit is set by the **quantum defect**: each 808 nm pump photon in Nd:YAG yields at most one 1064 nm photon, so at best $808/1064 = 76\%$ of the absorbed pump energy can emerge as laser light, and at least 24% becomes heat.

## 4. Optical Cavities and Longitudinal Modes

### 4.1 Standing waves in a Fabry–Pérot resonator
A laser cavity of two facing mirrors is a **Fabry–Pérot resonator**. Only waves that reproduce themselves after a round trip build up; equivalently, the field must form a standing wave with nodes at the mirrors, so an integer number $q$ of half-wavelengths fits in the optical length $nL$:
$$nL = q\,\frac{\lambda_q}{2} \quad\Longrightarrow\quad \nu_q = q\,\frac{c}{2nL}$$
These allowed frequencies are the **longitudinal (axial) modes**. Neighbouring modes are separated by the **free spectral range**
$$\boxed{\Delta\nu_{\text{FSR}} = \frac{c}{2nL}}$$
which is also the inverse of the round-trip time $2nL/c$.

### 4.2 How many modes oscillate?
The gain medium amplifies only over its **gain bandwidth** (Doppler-broadened for gases, much broader for solids and semiconductors). The laser can oscillate on every cavity mode for which gain exceeds loss, so the number of modes is roughly the gain bandwidth divided by $\Delta\nu_{\text{FSR}}$. To force a **single longitudinal mode**, one can shorten the cavity until $\Delta\nu_{\text{FSR}}$ exceeds the gain width, or insert a frequency-selective element such as a thin etalon.

### 4.3 Photon lifetime, finesse and mode width
If a fraction $\delta$ of the stored light is lost per round trip (time $2L/c$), the stored energy decays as $dU/dt = -U\delta c/(2L)$, giving a **photon lifetime** $\tau_p = 2L/(c\delta)$. For mirror losses alone, $\delta = \ln[1/(R_1R_2)]$. The passive cavity's resonances therefore have width $\delta\nu_c = 1/(2\pi\tau_p)$, and the **finesse** $\mathcal{F} = \Delta\nu_{\text{FSR}}/\delta\nu_c$ measures how sharp they are compared with their spacing. The linewidth of the operating laser can be much narrower still; the fundamental quantum (Schawlow–Townes) limit is usually far below the broadening caused in practice by vibrations and temperature drifts of the mirrors.

### 4.4 Stability and transverse modes
With curved mirrors of radii $R_1$ and $R_2$, a ray bouncing back and forth stays near the axis only if the cavity is **stable**:
$$0 \le g_1g_2 \le 1, \qquad g_i = 1 - \frac{L}{R_i}$$
A stable cavity supports a family of **transverse electromagnetic modes** TEM$_{mn}$, with $m$ and $n$ counting the nodal lines across the beam. The fundamental TEM$_{00}$ mode has a smooth Gaussian profile (Section 6) and is preferred for most applications; an aperture inside the cavity suppresses the higher-order modes.

### Worked example 4.1 – Modes of a helium–neon laser
**Problem:** A HeNe laser (632.8 nm) has mirrors 30.0 cm apart ($n \approx 1$) with $R_1 = 0.999$ and $R_2 = 0.990$. Neon has atomic mass 20.18 u and the discharge gas is at about 400 K. Find (a) the free spectral range and the mode number $q$, (b) the Doppler gain width and the number of modes that can oscillate, (c) the photon lifetime and passive mode width, and (d) the threshold gain coefficient if mirror losses dominate.

1. $\Delta\nu_{\text{FSR}} = c/(2L) = (2.998\times10^8)/(0.600) = 4.997\times10^8$ Hz $\approx 500$ MHz.
2. $q = 2L/\lambda = 0.600/(632.8\times10^{-9}) = 9.48\times10^5$; nearly a million half-wavelengths fit between the mirrors.
3. $\nu_0 = 4.738\times10^{14}$ Hz; $m = 20.18 \times 1.661\times10^{-27} = 3.351\times10^{-26}$ kg. Then $\Delta\nu_D = \nu_0\sqrt{8k_BT\ln2/(mc^2)} = 1.51\times10^9$ Hz.
4. Number of modes: $1.51\ \text{GHz}/0.500\ \text{GHz} \approx 3$.
5. $\delta = \ln[1/(0.999 \times 0.990)] = 0.01105$, so $\tau_p = 2L/(c\delta) = 0.600/(2.998\times10^8 \times 0.01105) = 1.81\times10^{-7}$ s.
6. $\delta\nu_c = 1/(2\pi\tau_p) = 0.88$ MHz, and $\mathcal{F} = 500/0.88 \approx 570$.
7. $g_{\text{th}} = \delta/(2L) = 0.01105/0.600 = 0.0184$ m⁻¹, a gain of under 2% per metre.

**Answer:** (a) 500 MHz, $q \approx 9.5\times10^5$; (b) 1.5 GHz, about three modes; (c) 0.18 µs and 0.9 MHz; (d) 0.018 m⁻¹. The tiny gain explains why HeNe lasers need mirrors with reflectances above 99%, and a cavity shorter than about $c/(2\Delta\nu_D) \approx 10$ cm would run on a single mode.

## 5. Coherence

### 5.1 Temporal coherence
Real light is never a perfect infinite sine wave. A useful model is a sequence of wave trains, each lasting about a **coherence time** $\tau_c$, with random phase jumps between them. By Fourier analysis, a wave train of duration $\tau_c$ contains a spread of frequencies
$$\Delta\nu \approx \frac{1}{\tau_c}$$
The **coherence length** is the distance light travels in that time:
$$l_c = c\,\tau_c \approx \frac{c}{\Delta\nu}$$
To express this in wavelength, differentiate $\nu = c/\lambda$: $\lvert d\nu\rvert = c\,d\lambda/\lambda^2$, so $\Delta\nu = c\Delta\lambda/\lambda^2$ and
$$\boxed{l_c \approx \frac{\lambda^2}{\Delta\lambda}}$$
In an interferometer, fringes are visible only when the path difference between the two beams is less than about $l_c$; beyond that, the two beams come from different, uncorrelated wave trains. The exact numerical factor depends on the line shape and on how the width is defined, so these formulas give orders of magnitude.

### 5.2 Spatial coherence
**Spatial coherence** describes how well the phases at two points *across* a beam are correlated. Light from an extended source of angular size $\theta_s$ is coherent only over a transverse distance of roughly $\lambda/\theta_s$. For sunlight ($\theta_s = 0.53° = 9.3\times10^{-3}$ rad, $\lambda \approx 0.55$ µm) this is about 60 µm, which is why Young's double-slit experiment with sunlight needs a pinhole or very closely spaced slits. A laser operating in the TEM$_{00}$ mode is spatially coherent across its entire beam; this is what allows it to be focused to a diffraction-limited spot or to diverge so little.

| Source | Spectral width | Coherence time | Coherence length |
|---|---|---|---|
| White light (400–700 nm) | $\Delta\lambda \approx 300$ nm | ≈ 3 fs | ≈ 1 µm |
| Red LED (630 nm) | $\Delta\lambda \approx 20$ nm | ≈ 70 fs | ≈ 20 µm |
| Single line of a low-pressure gas lamp | $\Delta\nu \approx 1$ GHz | ≈ 1 ns | ≈ 0.3 m |
| Multimode HeNe laser | $\Delta\nu \approx 1.5$ GHz | ≈ 0.7 ns | ≈ 0.2 m |
| Single-mode HeNe laser | $\Delta\nu \approx 1$ MHz | ≈ 1 µs | ≈ 300 m |
| Narrow-linewidth fiber laser | $\Delta\nu \approx 1$ kHz | ≈ 1 ms | ≈ 300 km |
| Laser locked to a reference cavity | $\Delta\nu \approx 1$ Hz | ≈ 1 s | ≈ 3×10⁵ km |

### Worked example 5.1 – Which source can record a deep hologram?
**Problem:** A hologram is to be made of an object 15 cm deep. In the recording geometry, light from the back of the object travels up to 30 cm farther than light from the front. Which of these sources is suitable: white light, a red LED (630 nm, $\Delta\lambda = 20$ nm), a multimode HeNe laser ($\Delta\nu = 1.5$ GHz), or a single-mode laser ($\Delta\nu = 1.0$ MHz)?

1. White light: $l_c \approx (550\ \text{nm})^2/(300\ \text{nm}) = 1.0$ µm.
2. LED: $l_c \approx (630\ \text{nm})^2/(20\ \text{nm}) = 2.0\times10^4$ nm $= 20$ µm.
3. Multimode HeNe: $l_c \approx c/\Delta\nu = (3.0\times10^8)/(1.5\times10^9) = 0.20$ m.
4. Single-mode laser: $l_c \approx (3.0\times10^8)/(1.0\times10^6) = 300$ m.
5. Compare with the required 0.30 m path difference.

**Answer:** Only the single-mode laser ($l_c \approx 300$ m) can record the full depth. The multimode HeNe (0.20 m) would lose fringe contrast for the back part of the object, and the LED and white light are hopeless. This is why holography had to wait for the laser.

## 6. Gaussian Beams

### 6.1 Derivation from the paraxial wave equation
A laser beam is a wave that travels mainly along $z$. Write the field as $E = A(x, y, z)\,e^{-ikz}$, where $k = 2\pi/\lambda$ and the envelope $A$ varies slowly with $z$. Substituting into the wave (Helmholtz) equation $\nabla^2E + k^2E = 0$ and dropping $\partial^2A/\partial z^2$, which is small compared with $k\,\partial A/\partial z$, gives the **paraxial wave equation**:
$$\nabla_\perp^2A - 2ik\frac{\partial A}{\partial z} = 0, \qquad \nabla_\perp^2 = \frac{\partial^2}{\partial x^2} + \frac{\partial^2}{\partial y^2}$$
Try a solution of the form $A = \exp\{-i[P(z) + kr^2/(2q(z))]\}$ with $r^2 = x^2 + y^2$:

1. Differentiating twice in $x$ and $y$: $\nabla_\perp^2A = \left(-\dfrac{2ik}{q} - \dfrac{k^2r^2}{q^2}\right)A$.
2. Differentiating in $z$: $-2ik\,\partial A/\partial z = \left(-2kP' + \dfrac{k^2r^2q'}{q^2}\right)A$.
3. Adding and requiring the sum to vanish for every $r$: the $r^2$ terms give $q' = 1$, and the constant terms give $P' = -i/q$.
4. Hence $q(z) = z + iz_R$, where we have chosen the beam's narrowest point (the **waist**) at $z = 0$ and $z_R$ is a real constant.
5. Write $1/q = 1/R(z) - i\lambda/[\pi w^2(z)]$. The factor $\exp[-ikr^2/(2q)]$ then splits into $\exp[-ikr^2/(2R)]$, a spherical wavefront of radius $R$, times $\exp(-r^2/w^2)$, a Gaussian amplitude profile of radius $w$.
6. Since $1/q = (z - iz_R)/(z^2 + z_R^2)$, matching real and imaginary parts gives:
$$\boxed{w(z) = w_0\sqrt{1 + \left(\frac{z}{z_R}\right)^2}}, \qquad \boxed{z_R = \frac{\pi w_0^2}{\lambda}}, \qquad R(z) = z\left[1 + \left(\frac{z_R}{z}\right)^2\right]$$
7. Solving $P' = -i/q$ adds an amplitude factor $w_0/w(z)$, required by energy conservation, and a slowly varying phase $\arctan(z/z_R)$, the **Gouy phase**.

The intensity is therefore
$$I(r, z) = I_0\left[\frac{w_0}{w(z)}\right]^2\exp\left[-\frac{2r^2}{w^2(z)}\right]$$

### 6.2 Waist, Rayleigh range and divergence
- $w_0$ is the **waist radius**, where the intensity falls to $1/e^2 = 13.5\%$ of its axial value.
- The **Rayleigh range** $z_R$ is the distance over which the beam area doubles ($w = \sqrt2\,w_0$); the region $\pm z_R$ is the beam's depth of focus.
- Far from the waist ($z \gg z_R$), $w(z) \approx w_0z/z_R = \lambda z/(\pi w_0)$, so the beam spreads at a constant **half-angle divergence**
$$\boxed{\theta = \frac{\lambda}{\pi w_0}}$$
A narrow waist means rapid spreading: this is diffraction, the same physics as the spreading of light behind a small aperture. Real beams are described by a **beam quality factor** $M^2 \ge 1$, with $\theta = M^2\lambda/(\pi w_0)$; an ideal TEM$_{00}$ beam has $M^2 = 1$.

### 6.3 Power and peak intensity
The total power is the integral of intensity over the beam cross-section:
$$P = \int_0^\infty I_0e^{-2r^2/w^2}\,2\pi r\,dr = I_0\,\frac{\pi w^2}{2} \quad\Longrightarrow\quad \boxed{I_0 = \frac{2P}{\pi w^2}}$$
The same integral taken from 0 to $a$ shows that a circular aperture of radius $a$ passes the fraction $1 - e^{-2a^2/w^2}$ of the power; an aperture of radius $w$ passes 86.5%.

### 6.4 Focusing
A lens of focal length $f$ illuminated by a collimated Gaussian beam of radius $w$ makes the beam converge at half-angle $\theta \approx w/f$. Since the focused waist $w_f$ and its divergence obey $\theta = \lambda/(\pi w_f)$, the focal spot radius is
$$w_f \approx \frac{\lambda f}{\pi w}$$
A larger input beam or a shorter focal length gives a smaller spot, down to a size of order one wavelength.

### Worked example 6.1 – From the laboratory to the Moon
**Problem:** A 5.0 mW HeNe laser (632.8 nm) has a waist radius $w_0 = 0.40$ mm at its output. Find the Rayleigh range, divergence, beam radius at 10 m and at the Moon (384,400 km), and the peak intensity. Then repeat the Moon calculation for a beam expanded to $w_0 = 0.50$ m by a telescope.

1. $z_R = \pi w_0^2/\lambda = \pi(4.0\times10^{-4})^2/(632.8\times10^{-9}) = 0.794$ m.
2. $\theta = \lambda/(\pi w_0) = 5.04\times10^{-4}$ rad $\approx 0.50$ mrad.
3. At 10 m: $w = 0.40\ \text{mm}\times\sqrt{1 + (10/0.794)^2} = 5.05$ mm.
4. At the Moon: $w \approx \theta z = 5.04\times10^{-4} \times 3.844\times10^8 = 1.94\times10^5$ m, i.e. a spot radius of about 190 km.
5. Peak intensity at the waist: $I_0 = 2P/(\pi w_0^2) = 2(5.0\times10^{-3})/[\pi(4.0\times10^{-4})^2] = 2.0\times10^4$ W/m² $= 2.0$ W/cm², about 20 times the intensity of bright sunlight (about 1000 W/m²).
6. Expanded beam: $\theta = 632.8\times10^{-9}/(\pi \times 0.50) = 4.0\times10^{-7}$ rad, so $w \approx 155$ m at the Moon.

**Answer:** $z_R = 0.79$ m, $\theta = 0.50$ mrad, $w = 5.1$ mm at 10 m and about 190 km at the Moon; $I_0 \approx 2.0$ W/cm². Expanding the beam 1250-fold reduces the lunar spot to about 155 m in principle; in practice atmospheric turbulence limits the divergence to roughly one arcsecond, giving a spot roughly 2 km across.

### Worked example 6.2 – Focusing a kilowatt fiber laser for cutting
**Problem:** A 1.0 kW fiber laser at 1070 nm produces a collimated beam of radius 5.0 mm, focused by a lens with $f = 200$ mm. Assuming an ideal Gaussian beam, find the focal spot radius, peak intensity and depth of focus.

1. $w_f = \lambda f/(\pi w) = (1.07\times10^{-6})(0.200)/[\pi(5.0\times10^{-3})] = 1.36\times10^{-5}$ m $= 13.6$ µm.
2. $I_0 = 2P/(\pi w_f^2) = 2000/[\pi(1.36\times10^{-5})^2] = 3.4\times10^{12}$ W/m² $= 3.4\times10^8$ W/cm².
3. Rayleigh range at the focus: $z_R = \pi w_f^2/\lambda = 5.4\times10^{-4}$ m, so the depth of focus $2z_R \approx 1.1$ mm.

**Answer:** $w_f \approx 14$ µm, $I_0 \approx 3\times10^8$ W/cm², depth of focus about 1 mm. This intensity melts and vaporizes steel almost instantly, while the beam stays tightly focused only over about a millimetre, so the focus must be placed carefully relative to the workpiece.

## 7. Types of Lasers

| Laser | Gain medium | Main wavelength(s) | Pump | Typical output | Typical uses |
|---|---|---|---|---|---|
| Helium–neon | He–Ne gas mixture | 632.8 nm (also 543.5 nm, 1.15 µm, 3.39 µm) | DC discharge | 0.5–50 mW, continuous | Alignment, interferometry, teaching |
| Ruby | Cr³⁺ in Al₂O₃ | 694.3 nm | Flash lamp | Pulsed, joules per pulse | Historical; tattoo removal |
| Semiconductor diode | GaN, AlGaInP, AlGaAs, InGaAsP | ≈ 375 nm – 2 µm (e.g. 405, 650, 808, 980, 1550 nm) | Electric current | mW to W per emitter | Telecom, optical storage, pumping, pointers |
| Nd:YAG | Nd³⁺ in Y₃Al₅O₁₂ | 1064 nm (532 nm when doubled) | Flash lamp or 808 nm diodes | mW to kW; ns pulses when Q-switched | Machining, ophthalmology, lidar, pumping |
| CO₂ | CO₂–N₂–He gas | 10.6 µm (second band near 9.4 µm) | Electric discharge | W to tens of kW | Cutting, welding, surgery |
| Fiber | Yb³⁺, Er³⁺ or Tm³⁺ in silica fiber | 1030–1080 nm, ≈ 1550 nm, ≈ 2 µm | Diode lasers | W to tens of kW | Cutting, welding, marking, telecom |
| Ti:sapphire | Ti³⁺ in Al₂O₃ | Tunable ≈ 650–1100 nm | Green (≈ 532 nm) laser | fs pulses, ≈ 1 W average | Ultrafast science, multiphoton microscopy |
| Excimer | ArF, KrF, XeCl | 193, 248, 308 nm | Pulsed discharge | ns pulses | Eye surgery, lithography |

### 7.1 Helium–neon laser
An electric discharge excites helium atoms into long-lived metastable states at about 19.8 and 20.6 eV. These lie very close in energy to excited states of neon, so collisions transfer the energy efficiently to neon (**resonant energy transfer**), creating an inversion on several neon transitions. The red 632.8 nm line is the best known. The gain is small, of order a percent per metre, so HeNe lasers use highly reflective mirrors and emit only milliwatts with wall-plug efficiencies below 0.1%. Their excellent beam quality and frequency stability kept them in use for alignment and interferometry for decades.

### 7.2 Semiconductor diode lasers
A diode laser is a forward-biased p–n junction. Electrons from the n side and holes from the p side recombine in a thin **active layer**, emitting photons with energy close to the band gap $E_g$; when the injected carrier density is high enough, the junction region becomes inverted. A **double heterostructure** sandwiches the active layer between materials of wider band gap and lower refractive index, confining both the carriers and the light. The cleaved crystal facets act as mirrors: with $n \approx 3.6$, the Fresnel reflectance is $R = [(n - 1)/(n + 1)]^2 \approx 0.32$, enough because semiconductor gain is enormous. For GaAs ($E_g = 1.424$ eV at 300 K), $\lambda = hc/E_g = 1239.8\ \text{eV nm}/1.424\ \text{eV} = 871$ nm; changing the alloy composition tunes the wavelength from the near ultraviolet (GaN-based, 405 nm for Blu-ray) to the infrared (InGaAsP, 1310 and 1550 nm for telecommunications). Diode lasers are tiny, cheap, directly modulated by the drive current at gigahertz rates, and can convert more than half of the electrical input into light. Because the emitting region is less than a micrometre thick, diffraction makes their beam diverge strongly and elliptically, so a lens is always needed. **Vertical-cavity surface-emitting lasers** (VCSELs), which emit perpendicular to the wafer, are used in data-centre links and 3D sensing.

### 7.3 Nd:YAG and other solid-state lasers
Neodymium ions replacing about 1% of the yttrium in yttrium aluminium garnet form a classic four-level system with lasing at 1064 nm. Originally pumped by flash lamps, they are now often pumped by 808 nm diode lasers (**diode-pumped solid-state**, DPSS, lasers), which is more efficient and generates less heat. The 230 µs upper-level lifetime makes Nd:YAG ideal for **Q-switching** (Section 7.6). Frequency doubling in a nonlinear crystal gives 532 nm green light: a green laser pointer is typically an 808 nm diode pumping a neodymium crystal whose 1064 nm output is doubled. Related media include Nd:YVO₄, Yb:YAG (thin-disk lasers) and Er:YAG at 2.94 µm.

### 7.4 CO₂ laser
The CO₂ laser works on transitions between *vibrational* levels of the CO₂ molecule. The discharge efficiently excites the first vibrational level of N₂ (about 0.29 eV), which nearly coincides with the asymmetric-stretch level of CO₂ and transfers its energy by collisions. Lasing occurs to a lower vibrational level, emitting at 10.6 µm (photon energy 0.117 eV); helium helps empty the lower level and cools the gas. Efficiencies of 10–20% and continuous powers up to tens of kilowatts make CO₂ lasers industrial workhorses for cutting and welding. Ordinary glass is opaque at 10.6 µm, so CO₂-laser optics use materials such as zinc selenide or germanium. Water absorbs 10.6 µm radiation very strongly, which makes the CO₂ laser a precise surgical scalpel.

### 7.5 Fiber lasers
In a fiber laser the gain medium is the core of an optical fiber doped with rare-earth ions: ytterbium (1030–1080 nm), erbium (around 1550 nm) or thulium (around 2 µm). In a **double-clad** design, multimode pump light from diode lasers travels in a large inner cladding and is gradually absorbed by the small doped core, while the laser light stays in the core. Mirrors are written directly into the fiber as **fiber Bragg gratings**. The long, thin geometry gives a huge surface-to-volume ratio for cooling, the guided mode gives excellent beam quality, and Yb-doped fibers pumped at 976 nm have a small quantum defect (976/1070 = 91% maximum efficiency). As a result, fiber lasers delivering kilowatts have largely taken over industrial metal cutting and welding.

### 7.6 Pulsed operation: Q-switching and mode-locking
**Q-switching.** A fast shutter (an electro-optic Pockels cell, an acousto-optic modulator or a saturable absorber) blocks the cavity while the pump builds up a large inversion, storing energy in the long-lived upper level. When the shutter opens, the stored energy is released in a single giant pulse lasting typically 1–100 ns. A 100 mJ pulse lasting 10 ns has a peak power of $0.1\ \text{J}/10^{-8}\ \text{s} = 10$ MW.

**Mode-locking.** A laser oscillating on $N$ longitudinal modes normally has random phases between them, producing a noisy output. If the modes are forced to keep fixed phases, they interfere to form a single short pulse circulating in the cavity. For $N$ modes of equal amplitude $E_0$, spaced by $\Delta\nu$ and all in phase, the summed field gives
$$I(t) \propto \left\lvert\sum_{q=0}^{N-1}E_0e^{i2\pi(\nu_0 + q\Delta\nu)t}\right\rvert^2 = E_0^2\,\frac{\sin^2(N\pi\Delta\nu t)}{\sin^2(\pi\Delta\nu t)}$$
This is a train of pulses with period $1/\Delta\nu = 2L/c$ (one round trip), peak intensity $N^2E_0^2$ instead of the average $NE_0^2$, and duration about $1/(N\Delta\nu)$, the inverse of the total locked bandwidth. Broad gain bandwidth therefore means short pulses.

**Ultrafast lasers.** Ti:sapphire has a gain bandwidth of hundreds of nanometres and, with Kerr-lens mode-locking, produces pulses shorter than 10 fs. For a Gaussian pulse, duration and bandwidth obey the **time–bandwidth product** $\Delta\nu\,\Delta t \ge 0.441$. Chirped-pulse amplification stretches a pulse in time, amplifies it safely, and recompresses it, reaching petawatt peak powers in the largest facilities. Focusing such pulses into gases generates attosecond pulses of extreme-ultraviolet light through high-harmonic generation, recognized by the 2023 Nobel Prize to Pierre Agostini, Ferenc Krausz and Anne L'Huillier.

### Worked example 7.1 – A mode-locked Ti:sapphire oscillator
**Problem:** A Ti:sapphire oscillator with a cavity length of 1.50 m emits 20 fs Gaussian pulses centred at 800 nm with an average power of 1.0 W. Find the repetition rate, pulse energy, peak power, minimum bandwidth and the number of locked modes.

1. Repetition rate: $f_{\text{rep}} = c/(2L) = (2.998\times10^8)/(3.00) = 9.99\times10^7$ Hz $\approx 100$ MHz (one pulse every 10 ns).
2. Pulse energy: $E_p = P_{\text{avg}}/f_{\text{rep}} = 1.0/(9.99\times10^7) = 1.0\times10^{-8}$ J $= 10$ nJ.
3. Peak power (for a Gaussian pulse, $P_{\text{peak}} \approx 0.94E_p/\Delta t$): $0.94 \times 10^{-8}/(20\times10^{-15}) = 4.7\times10^5$ W.
4. Bandwidth: $\Delta\nu \ge 0.441/\Delta t = 2.2\times10^{13}$ Hz; in wavelength, $\Delta\lambda = \lambda^2\Delta\nu/c = (800\times10^{-9})^2(2.2\times10^{13})/(2.998\times10^8) = 47$ nm.
5. Number of modes: $\Delta\nu/f_{\text{rep}} = 2.2\times10^{13}/9.99\times10^7 \approx 2.2\times10^5$.

**Answer:** 100 MHz, 10 nJ, about 0.47 MW peak (from only 1 W average), at least 47 nm of bandwidth, and about 220,000 phase-locked modes. Such a regularly spaced "comb" of modes, when its offset frequency is stabilized, is an **optical frequency comb**, the ruler used to measure optical frequencies (Nobel Prize 2005 to John Hall and Theodor Hänsch).

## 8. Holography

### 8.1 Recording and reconstruction
A photograph records only the intensity of light, losing the phase and therefore the depth information. A **hologram** records both by interfering the light scattered from an object (complex amplitude $O$ at the plate) with a coherent **reference wave** $R$. The plate records the intensity
$$I = \lvert R + O\rvert^2 = \lvert R\rvert^2 + \lvert O\rvert^2 + R^*O + RO^*$$
The cross terms encode the phase of $O$ relative to $R$ as a fine fringe pattern. After development, suppose the plate's amplitude transmittance is linear in exposure, $t = t_0 + \beta I$. Illuminating it with the original reference wave gives
$$Rt = R\left(t_0 + \beta\lvert R\rvert^2 + \beta\lvert O\rvert^2\right) + \beta\lvert R\rvert^2\,O + \beta R^2\,O^*$$
- The first group is the reference wave passing straight through, slightly modified.
- The term $\beta\lvert R\rvert^2O$ is, for a uniform reference beam, a scaled copy of the *original object wave*. An observer looking through the plate sees a **virtual image** in the original position of the object, in full three dimensions with parallax.
- The term $\beta R^2O^*$ is the phase-conjugate wave, which forms a **real image**.

In Gabor's original in-line arrangement these waves overlapped. Leith and Upatnieks tilted the reference beam (**off-axis holography**) so that the images separate in angle.

### 8.2 Practical requirements
Two plane waves crossing at an angle $\theta$ have wave-vector components $\pm k\sin(\theta/2)$ across the plate, so their interference fringes have spacing
$$\Lambda = \frac{\lambda}{2\sin(\theta/2)}$$
- The recording medium must resolve these fine fringes (thousands of lines per millimetre), far beyond ordinary photographic film, which resolves on the order of 100 lines per millimetre.
- The coherence length must exceed the largest path difference in the setup (Worked example 5.1).
- Nothing may move by more than a small fraction of a wavelength during the exposure, or the fringes wash out; holography tables float on vibration isolators.

### Worked example 8.1 – Fringe spacing and stability
**Problem:** A hologram is recorded with a HeNe laser (632.8 nm). Find the fringe spacing and spatial frequency when the object and reference beams meet at 30°, at 60°, and head-on (180°, a reflection hologram). How far may a mirror in the object beam move during exposure if the fringes may shift by at most a quarter period?

1. $\theta = 30°$: $\Lambda = 632.8/(2\sin15°) = 1222$ nm, i.e. $1/\Lambda = 818$ lines/mm.
2. $\theta = 60°$: $\Lambda = 632.8/(2\sin30°) = 632.8$ nm, i.e. 1580 lines/mm.
3. $\theta = 180°$: $\Lambda = \lambda/2 = 316$ nm in air (3160 lines/mm), and $\lambda/(2n) \approx 211$ nm inside an emulsion with $n = 1.5$.
4. A mirror displacement $d$ changes the object path by $2d$. A quarter-fringe shift corresponds to a path change of $\lambda/4$, so $2d < \lambda/4$, giving $d < \lambda/8 = 79$ nm.

**Answer:** 1.22 µm (818 lines/mm), 0.633 µm (1580 lines/mm) and 0.316 µm (3160 lines/mm); mirror motion must stay below about 80 nm during the exposure.

### 8.3 Uses of holography
- **Security features**: embossed "rainbow" holograms (invented by Stephen Benton in 1968), viewable in white light, appear on banknotes, passports and credit cards because they are hard to counterfeit.
- **Holographic interferometry**: superimposing holograms of an object before and after a tiny deformation produces fringes that map the displacement in steps of about half a wavelength; it is used in non-destructive testing of tyres, turbine blades and aircraft parts.
- **Holographic optical elements**: gratings, lenses and combiners recorded holographically, used in head-up displays and some augmented-reality glasses.
- **Digital and computer-generated holography**: a camera records the interference pattern and a computer reconstructs the wave; spatial light modulators display computed holograms to shape beams for optical tweezers and displays.

## 9. Optical Fibers and Dispersion

### 9.1 Guiding light and the numerical aperture
An optical fiber has a glass **core** of refractive index $n_1$ surrounded by a **cladding** of slightly lower index $n_2$. Light striking the core–cladding boundary at more than the critical angle $\theta_c = \arcsin(n_2/n_1)$ is totally internally reflected and stays trapped. To find the range of entry angles that are guided:

1. A ray entering the flat end face from a medium of index $n_0$ at angle $\theta_a$ refracts to angle $\theta_r$: $n_0\sin\theta_a = n_1\sin\theta_r$.
2. The refracted ray meets the side wall at angle $90° - \theta_r$ from the normal. The limiting ray has $90° - \theta_r = \theta_c$, so $\sin\theta_r = \cos\theta_c$.
3. $\cos\theta_c = \sqrt{1 - \sin^2\theta_c} = \sqrt{1 - (n_2/n_1)^2}$.
4. Therefore
$$\boxed{\text{NA} = n_0\sin\theta_a = \sqrt{n_1^2 - n_2^2}}$$
The **numerical aperture** NA measures how wide a cone of light the fiber accepts.

### 9.2 Multimode and single-mode fibers
Because the core is a waveguide, only certain field patterns (modes) propagate. For a step-index fiber of core radius $a$, the number of modes is set by the **V-number**
$$V = \frac{2\pi a}{\lambda}\,\text{NA}$$
If $V < 2.405$ (the first zero of the Bessel function $J_0$), only one mode propagates: the fiber is **single-mode**. For large $V$ the number of modes is about $V^2/2$. Multimode fibers (core diameter typically 50 or 62.5 µm) are easy to couple light into and are used for short links; single-mode fibers (core diameter about 8–9 µm) are used for all long-distance communication. **Graded-index** multimode fibers, whose core index decreases smoothly outward, make off-axis rays travel faster through lower-index glass, largely equalizing transit times.

### 9.3 Attenuation
Fiber loss is measured in decibels: loss (dB) $= 10\log_{10}(P_{\text{in}}/P_{\text{out}})$. In silica the main loss mechanisms are **Rayleigh scattering** from frozen-in density fluctuations, which scales as $\lambda^{-4}$ (so it is about 11 times stronger at 850 nm than at 1550 nm), and infrared absorption by vibrations of the Si–O bonds at longer wavelengths. Traces of water add an absorption peak near 1383 nm. The resulting "windows" are:

| Wavelength | Typical loss of silica fiber | Remarks |
|---|---|---|
| 850 nm | ≈ 2–3 dB/km | Multimode links with VCSEL sources |
| 1310 nm | ≈ 0.3–0.4 dB/km | Near-zero chromatic dispersion in standard fiber |
| 1550 nm | ≈ 0.2 dB/km | Lowest loss; erbium amplifiers work here |

At 0.2 dB/km, half the light remains after 15 km and 1% after 100 km.

### 9.4 Modal dispersion
In a step-index multimode fiber, different modes (rays at different angles) travel different path lengths:

1. The axial ray travels the fiber length $L$ in time $t_{\min} = Ln_1/c$.
2. The steepest guided ray meets the wall at exactly $\theta_c$, so it makes angle $\phi$ with the axis where $\cos\phi = \sin\theta_c = n_2/n_1$. Its path is $L/\cos\phi = Ln_1/n_2$, taking $t_{\max} = Ln_1^2/(cn_2)$.
3. The spread in arrival times is
$$\boxed{\Delta t_{\text{modal}} = \frac{Ln_1}{c}\left(\frac{n_1}{n_2} - 1\right)}$$
A short input pulse spreads by $\Delta t$, and adjacent pulses blur together if they are separated by less than about $2\Delta t$, which limits the bit rate to roughly $B \approx 1/(2\Delta t)$.

### 9.5 Chromatic dispersion
Even in a single-mode fiber, different wavelengths travel at different group velocities. **Material dispersion** comes from the wavelength dependence of the refractive index of silica; **waveguide dispersion** comes from the way the mode's spread into the cladding changes with wavelength. Their sum is described by the **dispersion parameter** $D$, in ps/(nm·km), and a pulse of spectral width $\Delta\lambda$ spreads by
$$\Delta t_{\text{chrom}} = D\,L\,\Delta\lambda$$
In standard single-mode fiber their sum passes through zero near 1310 nm, while at 1550 nm $D \approx 17$ ps/(nm·km). Engineers manage dispersion with narrow-linewidth lasers, specially designed fibers, dispersion-compensating elements, and digital signal processing in coherent receivers.

### 9.6 Amplifiers and multiplexing
Long links once needed electronic regenerators every few tens of kilometres. The **erbium-doped fiber amplifier** (EDFA), pumped at 980 or 1480 nm, amplifies all signals between about 1530 and 1565 nm at once. This made **dense wavelength-division multiplexing** (DWDM) practical: dozens of laser channels at different wavelengths, typically spaced by 50 or 100 GHz, share one fiber, each carrying its own data stream, for total capacities of tens of terabits per second per fiber. Submarine cables built this way carry the great majority of intercontinental data traffic.

### Worked example 9.1 – A step-index multimode fiber
**Problem:** A step-index fiber has $n_1 = 1.48$ and $n_2 = 1.46$. Find the NA, the acceptance half-angle in air, the critical angle, the modal dispersion over 1.0 km, and the approximate maximum bit rate.

1. $\text{NA} = \sqrt{1.48^2 - 1.46^2} = \sqrt{2.1904 - 2.1316} = \sqrt{0.0588} = 0.242$.
2. $\theta_a = \arcsin(0.242) = 14.0°$.
3. $\theta_c = \arcsin(1.46/1.48) = 80.6°$.
4. Axial transit time: $Ln_1/c = (1000)(1.48)/(2.998\times10^8) = 4.94\times10^{-6}$ s.
5. $\Delta t = 4.94\times10^{-6} \times (1.48/1.46 - 1) = 4.94\times10^{-6} \times 0.0137 = 6.8\times10^{-8}$ s $= 68$ ns.
6. $B \approx 1/(2\Delta t) = 1/(1.35\times10^{-7}\ \text{s}) = 7.4\times10^6$ bit/s.

**Answer:** NA = 0.24, $\theta_a = 14°$, $\theta_c = 80.6°$, $\Delta t \approx 68$ ns per km, so only about 7 Mbit/s over 1 km. This is why long-haul links use single-mode fiber.

### Worked example 9.2 – A single-mode link at 1550 nm
**Problem:** (a) A single-mode fiber has NA = 0.14. What is the largest core radius for single-mode operation at 1550 nm? (b) An 80 km link uses this kind of fiber with $D = 17$ ps/(nm·km) and loss 0.20 dB/km, and a laser of spectral width 0.10 nm launching 1.0 mW. Find the pulse broadening and the received power.

1. Single-mode condition: $V = 2\pi a\,\text{NA}/\lambda < 2.405$, so $a < 2.405\lambda/(2\pi\,\text{NA}) = 2.405(1.55\times10^{-6})/(2\pi \times 0.14) = 4.24\times10^{-6}$ m.
2. The core diameter must therefore be below about 8.5 µm, consistent with the 8–9 µm cores of standard telecom fiber.
3. Broadening: $\Delta t = DL\Delta\lambda = 17 \times 80 \times 0.10 = 136$ ps.
4. Loss: $0.20 \times 80 = 16$ dB, a power ratio of $10^{-1.6} = 0.025$.
5. Received power: $1.0\ \text{mW} \times 0.025 = 25$ µW.

**Answer:** (a) $a < 4.2$ µm; (b) 136 ps of broadening, which would smear bits at 10 Gbit/s (100 ps period) unless compensated, and 25 µW received, easily detected by a photodiode receiver.

## 10. Nonlinear Optics: Second-Harmonic Generation

### 10.1 Nonlinear polarization
Light drives the electrons in a material, creating a dipole moment per unit volume, the **polarization** $P$. For weak fields $P = \varepsilon_0\chi^{(1)}E$, and optics is linear: frequencies never change and beams pass through each other without interacting. Electrons are bound by fields of order $e/(4\pi\varepsilon_0a_0^2) \approx 5\times10^{11}$ V/m, while sunlight's field is under 1 kV/m. Focused laser light, with fields of $10^7$–$10^{10}$ V/m or more, is strong enough that higher-order terms matter:
$$P = \varepsilon_0\left(\chi^{(1)}E + \chi^{(2)}E^2 + \chi^{(3)}E^3 + \cdots\right)$$
Take $E = E_0\cos\omega t$. The quadratic term gives
$$\chi^{(2)}E_0^2\cos^2\omega t = \frac{\chi^{(2)}E_0^2}{2}\left(1 + \cos2\omega t\right)$$
The oscillating dipoles now contain a component at $2\omega$, which radiates light at twice the frequency (half the wavelength): **second-harmonic generation** (SHG). The constant term is a static polarization (optical rectification). In the photon picture, two photons of energy $\hbar\omega$ merge into one of energy $2\hbar\omega$, conserving energy.

### 10.2 Why the crystal must lack inversion symmetry
In a material with a centre of inversion symmetry (glass, water, air, many crystals), reversing the field must exactly reverse the polarization. Replace $E$ by $-E$:
$$-P = \varepsilon_0\left(-\chi^{(1)}E + \chi^{(2)}E^2 - \chi^{(3)}E^3 + \cdots\right)$$
Comparing with $-1$ times the original series term by term requires $\chi^{(2)}E^2 = -\chi^{(2)}E^2$, so $\chi^{(2)} = 0$. Second-harmonic generation therefore requires **non-centrosymmetric** crystals such as potassium dihydrogen phosphate (KDP), beta-barium borate (BBO), lithium triborate (LBO), potassium titanyl phosphate (KTP) and lithium niobate (LiNbO₃). Surfaces and certain biological structures such as collagen also lack inversion symmetry, which SHG microscopy exploits.

### 10.3 Phase matching
The second harmonic generated at each point in the crystal travels at the phase velocity set by $n(2\omega)$, while the driving polarization moves with the fundamental at $n(\omega)$. Because of dispersion these differ, and contributions from different depths drift out of phase:

1. The harmonic field generated in a slice $dz$ at depth $z$ is proportional to $e^{i\Delta k\,z}\,dz$, where the **wave-vector mismatch** is
$$\Delta k = k_{2\omega} - 2k_\omega = \frac{2\omega n(2\omega)}{c} - \frac{2\omega n(\omega)}{c} = \frac{4\pi}{\lambda}\left[n(2\omega) - n(\omega)\right]$$
with $\lambda$ the fundamental wavelength in vacuum.
2. Integrating over a crystal of length $L$: $\int_0^Le^{i\Delta k\,z}dz = (e^{i\Delta kL} - 1)/(i\Delta k)$.
3. Its squared magnitude is $[2 - 2\cos(\Delta kL)]/\Delta k^2 = 4\sin^2(\Delta kL/2)/\Delta k^2$.
4. Hence the harmonic intensity is
$$I_{2\omega} \propto I_\omega^2\,L^2\left[\frac{\sin(\Delta kL/2)}{\Delta kL/2}\right]^2$$

With $\Delta k = 0$ the output grows as $L^2$. Otherwise it oscillates, peaking first at the **coherence length**
$$L_c = \frac{\pi}{\Delta k} = \frac{\lambda}{4\left[n(2\omega) - n(\omega)\right]}$$
and returning to zero at $2L_c$. Two strategies achieve $\Delta k = 0$:
- **Birefringent phase matching**: in an anisotropic crystal, choose the propagation direction and polarizations so that the extraordinary index at $2\omega$ equals the ordinary index at $\omega$.
- **Quasi-phase matching**: reverse the sign of $\chi^{(2)}$ every coherence length by periodically poling a ferroelectric crystal (for example periodically poled lithium niobate, PPLN), so that the harmonic keeps growing. The poling period is $2L_c$.

The output scales as $I_\omega^2$, so SHG is efficient only with intense beams, usually pulsed or inside a laser cavity.

### Worked example 10.1 – Coherence length in lithium niobate
**Problem:** An Nd:YAG laser (1064 nm) is to be frequency-doubled in lithium niobate with both waves polarized along the crystal's optic axis, where the refractive indices are approximately $n = 2.156$ at 1064 nm and $n = 2.234$ at 532 nm. Find the photon energies, $\Delta k$, the coherence length, and the quasi-phase-matching period.

1. Photon energies: $1239.8/1064 = 1.165$ eV and $1239.8/532 = 2.331$ eV, exactly twice as large.
2. $\Delta n = 2.234 - 2.156 = 0.078$.
3. $\Delta k = (4\pi/\lambda)\Delta n = 4\pi(0.078)/(1.064\times10^{-6}\ \text{m}) = 9.2\times10^5$ m⁻¹.
4. $L_c = \lambda/(4\Delta n) = 1.064\ \text{µm}/(4 \times 0.078) = 3.4$ µm.
5. Quasi-phase-matching period: $2L_c = 6.8$ µm.

**Answer:** $L_c \approx 3.4$ µm, so without phase matching the green output would never build beyond what a few micrometres of crystal produce, even in a 1 cm crystal (about 2900 coherence lengths). A poling period of about 6.8 µm, close to the periods used in practice, lets the harmonic grow throughout the crystal.

### 10.4 Other nonlinear effects
- **Sum- and difference-frequency generation**: mixing $\omega_1$ and $\omega_2$ gives $\omega_1 \pm \omega_2$; mixing 1064 nm with 532 nm gives the third harmonic at 355 nm.
- **Optical parametric oscillators**: the reverse process splits one pump photon into two lower-energy photons whose wavelengths can be tuned continuously.
- **Third-order effects**: the intensity-dependent refractive index $n = n_0 + n_2I$ (the optical **Kerr effect**) causes self-focusing and self-phase modulation, enables Kerr-lens mode-locking, and broadens pulses into white-light **supercontinua**.
- **Two-photon absorption**: since its rate scales as $I^2$, it occurs only at the focus, which gives two-photon microscopes their built-in depth sectioning.

## 11. Interferometry: From Michelson to LIGO

### 11.1 The Michelson interferometer
A beam splitter divides a beam into two arms ending in mirrors at distances $d_1$ and $d_2$. The returning beams recombine at the beam splitter, with path difference $\Delta = 2(d_1 - d_2)$. For two beams of equal amplitude $E$, the phase difference is $\phi = 2\pi\Delta/\lambda$, and the output intensity is
$$I = \left\lvert E + Ee^{i\phi}\right\rvert^2 = 2E^2(1 + \cos\phi) = I_{\max}\cos^2\left(\frac{\pi\Delta}{\lambda}\right)$$
Moving one mirror by $\lambda/2$ changes $\Delta$ by $\lambda$ and sweeps the output through one complete fringe. Counting $N$ fringes therefore measures a displacement
$$\Delta d = \frac{N\lambda}{2}$$

### 11.2 What interferometers measure
- **Lengths and displacements**: laser interferometers calibrate machine tools and position the stages of chip-making lithography tools with nanometre precision. Since 1983 the metre has been defined as the distance travelled by light in vacuum in 1/299,792,458 of a second, making optical frequency and wavelength measurements the basis of length standards.
- **Spectra**: when the path difference is scanned, the output is the Fourier transform of the source spectrum. **Fourier-transform infrared (FTIR) spectrometers** work this way.
- **Coherence**: the fringe visibility falls as $\Delta$ exceeds the coherence length, so a Michelson interferometer measures $l_c$ directly. Optical coherence tomography (Section 12) turns this into an imaging method.

### 11.3 LIGO
A passing **gravitational wave** stretches space in one direction while squeezing it in the perpendicular direction. Its **strain** $h$ changes the two arms of an L-shaped interferometer of arm length $L$ in opposite senses, producing a differential length change $\Delta L = hL$. The waves expected from astrophysical sources have $h \sim 10^{-21}$ or smaller.

The **Laser Interferometer Gravitational-Wave Observatory** (LIGO) has two detectors, at Hanford, Washington, and Livingston, Louisiana, about 3000 km apart, each with 4 km arms. Key features:

- Each arm is a **Fabry–Pérot cavity**, so the light makes hundreds of round trips and the phase shift is multiplied accordingly.
- **Power recycling** returns the light that would otherwise travel back toward the laser; together with the arm cavities it raises the circulating power in each arm to hundreds of kilowatts, reducing the relative photon shot noise.
- The light source is a highly stabilized laser at 1064 nm, and the mirrors are 40 kg fused-silica test masses suspended as multi-stage pendulums to isolate them from ground vibration, all inside one of the world's largest ultrahigh-vacuum systems.
- Since 2019, **squeezed light**, a quantum state with reduced phase noise, has been injected to beat the standard quantum limit of shot noise.

On 14 September 2015 both detectors recorded the signal GW150914 from two black holes, each about 30 solar masses, merging about 1.3 billion light-years away; the signal reached Livingston about 7 ms before Hanford. On 17 August 2017, LIGO and the European Virgo detector observed merging neutron stars whose gamma rays and light were also detected by telescopes, opening multi-messenger astronomy.

### Worked example 11.1 – Fringe counting and the LIGO strain
**Problem:** (a) In a Michelson interferometer illuminated by a HeNe laser (632.8 nm), one mirror is moved by 0.100 mm. How many fringes pass? (b) A gravitational wave with $h = 1.0\times10^{-21}$ passes LIGO. Find the differential change in arm length, compare it with the proton diameter (charge radius 0.841 fm), and find the phase shift in a simple Michelson with 1064 nm light. (c) Estimate the phase shift if the arm cavities multiply it by an effective 300 round trips.

1. $N = 2\Delta d/\lambda = 2(1.00\times10^{-4})/(632.8\times10^{-9}) = 316$ fringes.
2. $\Delta L = hL = (1.0\times10^{-21})(4000\ \text{m}) = 4.0\times10^{-18}$ m.
3. Proton diameter: $2 \times 0.841\times10^{-15} = 1.68\times10^{-15}$ m; ratio $1.68\times10^{-15}/4.0\times10^{-18} \approx 420$.
4. The path difference changes by $2\Delta L$, so $\Delta\phi = 2\pi(2\Delta L)/\lambda = 4\pi(4.0\times10^{-18})/(1.064\times10^{-6}) = 4.7\times10^{-11}$ rad.
5. With 300 effective round trips: $\Delta\phi \approx 300 \times 4.7\times10^{-11} = 1.4\times10^{-8}$ rad.

**Answer:** (a) 316 fringes; (b) $\Delta L = 4.0\times10^{-18}$ m, about 1/420 of a proton diameter, with a bare phase shift of $4.7\times10^{-11}$ rad; (c) about $1.4\times10^{-8}$ rad. Detecting phase shifts this small requires enormous circulating power (so that photon-counting noise averages down), seismic isolation and quantum-noise reduction.

## 12. Applications

### Medicine
- **Ophthalmology.** In LASIK, an argon-fluoride excimer laser (193 nm) removes corneal tissue in sub-micrometre layers by photoablation to correct refractive errors, and femtosecond lasers cut the corneal flap. Green lasers (532 nm) photocoagulate leaking retinal vessels in diabetic retinopathy, and Q-switched Nd:YAG pulses open clouded lens capsules after cataract surgery.
- **Surgery.** The CO₂ laser (10.6 µm) and Er:YAG laser (2.94 µm, near a strong absorption peak of water) vaporize tissue precisely while sealing small blood vessels. Holmium lasers (about 2.1 µm) delivered through fibers fragment kidney stones.
- **Dermatology.** In **selective photothermolysis** (Anderson and Parrish, 1983), the wavelength is chosen to be absorbed by a target (haemoglobin, melanin or tattoo ink) and the pulse is shorter than the target's thermal relaxation time, so the target is heated while surrounding tissue is spared. Q-switched nanosecond and picosecond lasers remove tattoos this way.
- **Imaging.** **Optical coherence tomography** (OCT) is "optical ultrasound": a low-coherence source in a Michelson interferometer produces interference only from tissue layers whose path length matches the reference arm to within the coherence length. For a Gaussian spectrum the axial resolution is $\Delta z = (2\ln2/\pi)\,\lambda_0^2/\Delta\lambda$; a source at 840 nm with 50 nm bandwidth gives $\Delta z = 0.441 \times (840\ \text{nm})^2/(50\ \text{nm}) = 6.2$ µm in air (about 4.5 µm in tissue of index 1.38). OCT is now routine for examining the retina. Confocal and two-photon fluorescence microscopy, flow cytometry and photodynamic therapy also rely on lasers.

### Industry and manufacturing
- **Materials processing**: CO₂ and fiber lasers cut, weld, drill and mark metals, plastics, wood and fabrics; ultrafast lasers machine glass and medical stents with minimal heat damage; laser powder-bed fusion 3D-prints metal parts.
- **Lithography**: ArF excimer lasers at 193 nm (with water immersion) and extreme-ultraviolet light at 13.5 nm, generated by CO₂-laser pulses striking tin droplets, pattern the smallest features of modern chips.
- **Sensing and measurement**: lidar maps terrain, forests and the atmosphere and guides autonomous vehicles; laser rangefinders and trackers survey buildings; laser Doppler velocimetry measures flows.
- **Everyday devices**: barcode scanners, laser printers, computer mice and optical discs. The smallest spot a disc player can focus scales as $\lambda/\text{NA}$, which drove the move to shorter wavelengths:

| Format | Laser wavelength | Objective NA | $\lambda/\text{NA}$ | Single-layer capacity |
|---|---|---|---|---|
| CD | 780 nm | 0.45 | 1.73 µm | ≈ 0.7 GB |
| DVD | 650 nm | 0.60 | 1.08 µm | 4.7 GB |
| Blu-ray | 405 nm | 0.85 | 0.48 µm | 25 GB |

The areal density scales as $(\text{NA}/\lambda)^2$, a factor of about 13 from CD to Blu-ray; improved coding and track layout account for the rest of the capacity gain.

### Communications and information
Fiber-optic networks (Section 9) carry telephone, internet and data-centre traffic; semiconductor lasers and modulators encode the data, EDFAs amplify it, and DWDM multiplies the capacity of each fiber. Laser links also connect satellites to each other in space and are being tested for communication with deep-space probes.

### Science and metrology
Laser cooling and trapping of atoms (Nobel Prize 1997 to Steven Chu, Claude Cohen-Tannoudji and William Phillips) led to Bose–Einstein condensates and to optical atomic clocks, which now keep time to about one part in $10^{18}$. Optical tweezers hold and move living cells and single molecules. Retroreflectors left on the Moon by the Apollo astronauts, starting with Apollo 11 in 1969, let observatories time laser pulses to the Moon and back, showing that the Moon recedes from Earth by about 3.8 cm per year. Laser spectroscopy measures atmospheric pollutants and greenhouse gases.

## 13. Laser Safety

### 13.1 Why the eye is especially vulnerable
Between about 400 and 1400 nm (the **retinal hazard region**) the cornea and lens transmit light and focus a collimated beam to a spot on the retina only about 10–20 µm across. Light entering a 7 mm dark-adapted pupil and focused to a 20 µm spot is concentrated by a factor of $(7\ \text{mm}/20\ \text{µm})^2 \approx 1.2\times10^5$. A 1 mW beam focused to a 20 µm-diameter spot gives a retinal irradiance of $10^{-3}/[\pi(10\times10^{-6})^2] \approx 3\times10^6$ W/m², roughly ten times the retinal irradiance produced by staring directly at the midday Sun. Retinal burns are permanent, and a burn in the fovea destroys central vision.

- **Near infrared (700–1400 nm)** is the most insidious: it reaches the retina, but it is invisible, so there is no blink or aversion response. Inexpensive green pointers lacking an infrared filter can leak 808 nm or 1064 nm light.
- **Ultraviolet** (below about 400 nm) and **far infrared** (above about 1400 nm) are absorbed in the cornea and lens, causing photokeratitis, burns or cataracts rather than retinal damage. "Eye-safe" 1550 nm lasers are safer only in this relative sense.
- **Pulsed lasers** deliver enormous peak powers; even a weak scattered reflection from a Q-switched pulse can damage the retina in nanoseconds.
- Other hazards include skin burns, ignition of materials, high-voltage power supplies, toxic gases (excimer lasers use fluorine or hydrogen chloride mixtures) and fumes released during laser cutting.

### 13.2 Laser hazard classes
The international standard IEC 60825-1 groups lasers by their accessible emission. Limits below are for continuous visible lasers:

| Class | Typical limit | Hazard |
|---|---|---|
| 1 | Safe under all normal use | Includes enclosed high-power systems such as laser printers and disc players |
| 1M | As class 1 without optics | Hazardous if viewed through binoculars or a magnifier |
| 2 | Visible, ≤ 1 mW | Eye protected by the blink reflex (about 0.25 s); do not stare into the beam |
| 2M | Visible; ≤ 1 mW through the pupil | As class 2, but hazardous with magnifying optics |
| 3R | ≤ 5 mW (visible) | Low risk, but direct viewing can injure |
| 3B | ≤ 500 mW | Direct beam and mirror-like reflections hazardous; diffuse reflections usually safe |
| 4 | > 500 mW | Direct, specular and diffuse reflections hazardous; skin and fire hazard |

### 13.3 Controls and protective eyewear
Safety measures are layered: **engineering controls** (enclosures, interlocks, beam stops, keeping beams well away from eye level), **administrative controls** (a laser safety officer, training, warning signs, controlled access) and **personal protective equipment**. The exposure that is considered safe is the **maximum permissible exposure** (MPE), which depends on wavelength, exposure time and pulse duration. Protective eyewear is specified by its **optical density** at the laser wavelength, where the transmitted fraction is $T = 10^{-\text{OD}}$. Eyewear must be chosen for the specific wavelength; goggles that block 532 nm may transmit 1064 nm freely. In many countries it is a criminal offence to aim a laser at an aircraft.

### Worked example 13.1 – Choosing laser goggles
**Problem:** A 5.0 W continuous laser at 532 nm is used in a laboratory. What minimum optical density is needed so that the full beam, if it struck the goggles, would transmit less than 1.0 mW (the class 2 limit)?

1. Required transmission: $T \le 1.0\times10^{-3}\ \text{W}/5.0\ \text{W} = 2.0\times10^{-4}$.
2. $\text{OD} \ge \log_{10}(1/T) = \log_{10}(5000) = 3.7$.
3. Choose the next standard rating, OD 4, which transmits $5.0 \times 10^{-4} = 0.5$ mW.

**Answer:** OD ≥ 3.7; in practice OD 4 or higher at 532 nm, with the goggles also confirmed to withstand the beam's power without damage.

## 14. Common Misconceptions

- **"Laser light is a special kind of light."** Laser photons are ordinary photons; what is special is that they share frequency, direction and phase because they are copies made by stimulated emission.
- **"A laser creates energy by amplifying light."** Every amplified photon is paid for by pump energy, and many lasers are inefficient: a HeNe converts less than 0.1% of its electrical input into light. The pump energy simply ends up concentrated into one mode.
- **"Pumping harder will eventually invert a two-level system."** Strong pumping only equalizes the populations (Section 3.2). A third or fourth level is essential for optical pumping.
- **"Laser beams do not spread."** Every beam diverges by diffraction, at least at $\theta = \lambda/(\pi w_0)$. A pointer beam is centimetres wide across a sports field and kilometres wide at the Moon.
- **"Laser light is perfectly monochromatic and coherent."** Every laser has a finite linewidth and a finite coherence length, from millimetres for some diode lasers to thousands of kilometres for the best stabilized lasers.
- **"You can see a laser beam travelling through the air."** You see light scattered sideways by dust, droplets or smoke. In clean air or in space a beam is invisible from the side, unlike in science-fiction films.
- **"Infrared lasers are less dangerous because they are invisible."** Near-infrared light reaches the retina just like visible light but triggers no blink reflex, making it more dangerous.
- **"Floating 3D images at concerts are holograms."** Most such displays are stage illusions using projection or partially reflecting screens; a true hologram reconstructs a recorded wavefront by diffraction.
- **"Fibers guide light with mirror-coated walls."** Guiding comes from total internal reflection at the core–cladding boundary, which loses far less light than any metal mirror.
- **"Second-harmonic generation violates energy conservation by doubling the frequency."** Two input photons are consumed for each output photon, so energy is conserved, and the output power never exceeds the input power.

## 15. Connections to Other Topics

- **Quantum mechanics**: energy levels, transition rates (Fermi's golden rule gives the Einstein coefficients from atomic wavefunctions) and photon statistics; squeezed light in LIGO is a direct application of quantum uncertainty.
- **Statistical and thermal physics**: the Einstein relations rest on the Boltzmann distribution and Planck's blackbody law; population inversion corresponds to negative absolute temperature; the quantum defect sets laser heat loads.
- **Wave optics**: Gaussian-beam divergence is diffraction, laser cavities are Fabry–Pérot interferometers, and coherence determines whether interference fringes appear.
- **Electromagnetism**: refractive index, polarization, total internal reflection, waveguide modes and nonlinear polarization all follow from Maxwell's equations in matter.
- **Solid-state physics**: band gaps and p–n junctions underlie diode lasers, LEDs and photodetectors; crystal symmetry decides which materials allow SHG.
- **Chemistry**: laser spectroscopy (Raman, laser-induced fluorescence), femtosecond studies of chemical reactions, and photochemistry.
- **Biology and medicine**: fluorescence and super-resolution microscopy, optical tweezers, flow cytometry, OCT and laser surgery.
- **Astronomy and relativity**: gravitational-wave detection, lunar laser ranging tests of gravity, laser guide stars for adaptive optics, and optical frequency combs used to calibrate spectrographs searching for exoplanets.
- **Information technology**: fiber-optic communications, optical data storage and silicon photonics in data centres.

## 16. Practice Problems

1. **(Easy)** Find the photon energy in eV and the number of photons emitted per second by (a) a 5.0 mW HeNe laser at 632.8 nm and (b) a 1.0 W CO₂ laser at 10.6 µm.
2. **(Easy–medium)** For a two-level transition with equal degeneracies at 300 K, find the equilibrium population ratio $N_2/N_1$ and the ratio of stimulated to spontaneous emission in blackbody radiation for (a) $\lambda = 10.6$ µm and (b) $\lambda = 632.8$ nm. What do the results imply?
3. **(Medium)** A GaAs diode laser emitting at 850 nm has a cavity 0.30 mm long with refractive index 3.6. Find (a) the longitudinal mode spacing in frequency and in wavelength, (b) the number of modes within a 10 nm gain bandwidth, and (c) the reflectance of an uncoated cleaved facet.
4. **(Easy)** A red diode laser at 650 nm has a linewidth of 0.020 nm. Find its frequency width, coherence time and coherence length. Could it record a hologram of an object 5.0 cm deep, where path differences reach 10 cm?
5. **(Medium)** A 5.0 mW green laser pointer (532 nm) has a waist radius of 0.50 mm. Find (a) its divergence and Rayleigh range, (b) the beam radius and axial intensity at 100 m, (c) the power entering a 7.0 mm diameter pupil at 100 m, and (d) its laser class.
6. **(Medium–hard)** A ruby crystal contains $1.58\times10^{19}$ Cr³⁺ ions per cm³, is pumped through an absorption band at about 550 nm, and has an upper-level lifetime of 3.0 ms. (a) What is the minimum pump rate per ion for inversion? (b) What energy must be absorbed per cm³ just to reach transparency? (c) How much is that for a rod 6.0 mm in diameter and 5.0 cm long? (d) What fraction of each absorbed pump photon's energy is lost as heat when a 694.3 nm photon is emitted?
7. **(Medium)** A fiber has core radius 4.1 µm and NA = 0.12. Find (a) the acceptance half-angle in air, (b) the V-number at 1310 nm and 1550 nm, and (c) the cutoff wavelength below which it becomes multimode.
8. **(Medium)** A 10 Gbit/s link at 1550 nm uses a laser of spectral width 0.050 nm and fiber with $D = 17$ ps/(nm·km) and loss 0.20 dB/km. (a) Find the maximum length if chromatic broadening may not exceed half a bit period (50 ps). (b) If 2.0 mW is launched, what power arrives at that length?
9. **(Medium)** (a) Give the wavelengths and photon energies of the second, third and fourth harmonics of an Nd:YAG laser (1064 nm); the third harmonic is made by sum-frequency mixing of 1064 nm and 532 nm. (b) In a crystal with $n = 1.494$ at 1064 nm and $n = 1.512$ at 532 nm, without phase matching, what is the coherence length for SHG?
10. **(Hard)** A Michelson interferometer is illuminated by the sodium D lines (588.995 nm and 589.592 nm). (a) Show that the fringe visibility falls to a minimum periodically as one mirror moves, and find the mirror displacement between successive minima. (b) How many fringes pass between successive minima? (c) With a different source, 790 fringes pass when the mirror moves 0.250 mm. What is the wavelength?

### Solutions

**1.** Use $E = hc/\lambda$ and photon rate $\dot N = P/E = P\lambda/(hc)$.

(a) $E = 1239.8/632.8 = 1.959$ eV; $\dot N = (5.0\times10^{-3})(632.8\times10^{-9})/[(6.626\times10^{-34})(2.998\times10^8)] = 1.6\times10^{16}$ photons/s.

(b) $E = 1239.8/10600 = 0.117$ eV; $\dot N = (1.0)(10.6\times10^{-6})/(1.986\times10^{-25}) = 5.3\times10^{19}$ photons/s.

Each infrared photon carries about 17 times less energy than a red HeNe photon, so a watt of infrared light contains far more photons.

**2.** At 300 K, $k_BT = 0.02585$ eV.

(a) $x = 0.117/0.02585 = 4.52$: $N_2/N_1 = e^{-4.52} = 0.011$ and the stimulated-to-spontaneous ratio is $1/(e^{4.52} - 1) = 0.011$.

(b) $x = 1.959/0.02585 = 75.8$: both ratios are about $1.2\times10^{-33}$.

In the mid-infrared, thermal excitation of low-lying levels is not negligible (about 1% here). In a CO₂ laser the lower laser level lies only about 0.17 eV above the ground state, so keeping the gas cool (helium helps carry heat away) is important to keep that level nearly empty. In the visible, thermal excitation and stimulated emission are both utterly negligible without a pump.

**3.** (a) $\Delta\nu = c/(2nL) = (2.998\times10^8)/(2 \times 3.6 \times 3.0\times10^{-4}) = 1.39\times10^{11}$ Hz $= 139$ GHz. In wavelength, $\Delta\lambda = \lambda^2/(2nL) = (850\times10^{-9})^2/(2.16\times10^{-3}) = 3.3\times10^{-10}$ m $= 0.33$ nm.

(b) $10\ \text{nm}/0.334\ \text{nm} \approx 30$ modes.

(c) $R = [(3.6 - 1)/(3.6 + 1)]^2 = (2.6/4.6)^2 = 0.32$.

**4.** $\Delta\nu = c\Delta\lambda/\lambda^2 = (2.998\times10^8)(2.0\times10^{-11})/(6.50\times10^{-7})^2 = 1.4\times10^{10}$ Hz $= 14$ GHz. $\tau_c = 1/\Delta\nu = 70$ ps. $l_c = \lambda^2/\Delta\lambda = (650\ \text{nm})^2/(0.020\ \text{nm}) = 2.1\times10^7$ nm $= 21$ mm. Since 21 mm is much less than 10 cm, the fringes from the back of the object would wash out: the laser cannot record the full depth.

**5.** (a) $\theta = \lambda/(\pi w_0) = 532\times10^{-9}/(\pi \times 5.0\times10^{-4}) = 3.4\times10^{-4}$ rad; $z_R = \pi w_0^2/\lambda = \pi(5.0\times10^{-4})^2/(532\times10^{-9}) = 1.48$ m.

(b) $w = w_0\sqrt{1 + (100/1.476)^2} = 3.39\times10^{-2}$ m $= 33.9$ mm; $I_0 = 2P/(\pi w^2) = 2(5.0\times10^{-3})/[\pi(0.0339)^2] = 2.8$ W/m².

(c) Fraction through a 3.5 mm radius: $1 - \exp[-2(3.5)^2/(33.9)^2] = 0.021$, so $P \approx 0.021 \times 5.0\ \text{mW} = 0.11$ mW.

(d) A 5 mW visible continuous laser is class 3R. Close to the pointer the whole 5 mW can enter the eye, so it must never be aimed at people or aircraft, even though at 100 m the power through a pupil has fallen below the class 2 limit.

**6.** (a) Inversion in a three-level system needs $W_p\tau > 1$: $W_p > 1/(3.0\times10^{-3}\ \text{s}) = 333$ s⁻¹ per ground-state ion.

(b) Transparency requires half the ions excited: $7.9\times10^{18}$ ions per cm³. Each 550 nm pump photon carries $hc/\lambda = 3.61\times10^{-19}$ J, so the absorbed energy is $7.9\times10^{18} \times 3.61\times10^{-19} = 2.9$ J per cm³.

(c) Volume $= \pi(0.30\ \text{cm})^2(5.0\ \text{cm}) = 1.41$ cm³, so about 4.0 J must be absorbed. Because a flash lamp converts only a small fraction of its electrical energy into absorbed pump light, the lamp must discharge far more. The energy must also be delivered within a time comparable to the 3 ms lifetime, or the excited ions decay by spontaneous emission before inversion is reached.

(d) $1 - 550/694.3 = 0.21$: about 21% of each absorbed pump photon's energy becomes heat.

**7.** (a) $\theta_a = \arcsin(0.12) = 6.9°$.

(b) $V = 2\pi a\,\text{NA}/\lambda$. At 1310 nm: $2\pi(4.1\times10^{-6})(0.12)/(1.31\times10^{-6}) = 2.36$. At 1550 nm: $1.99$.

(c) $\lambda_c = 2\pi a\,\text{NA}/2.405 = 2\pi(4.1\times10^{-6})(0.12)/2.405 = 1.29$ µm. Both 1310 nm and 1550 nm are longer than the cutoff, so the fiber is single-mode at both, but it would carry several modes at 850 nm.

**8.** (a) $\Delta t = DL\Delta\lambda \le 50$ ps, so $L \le 50/(17 \times 0.050) = 59$ km.

(b) Loss $= 0.20 \times 58.8 = 11.8$ dB, a transmission of $10^{-1.18} = 0.067$, so $P = 2.0 \times 0.067 = 0.13$ mW. At this distance, dispersion rather than attenuation limits the link; a narrower-linewidth laser, dispersion compensation, or operation near 1310 nm (where $D \approx 0$ but loss is higher) would extend it.

**9.** (a) Second harmonic: $1064/2 = 532$ nm, $2 \times 1.165 = 2.331$ eV. Third harmonic: $1/\lambda_3 = 1/1064 + 1/532$, so $\lambda_3 = 354.7$ nm and $E = 3.496$ eV. Fourth harmonic (doubling 532 nm): 266 nm, $E = 4.661$ eV. Energies add because photon energies add in each mixing step.

(b) $L_c = \lambda/[4(n_{2\omega} - n_\omega)] = 1.064\ \text{µm}/(4 \times 0.018) = 14.8$ µm.

**10.** (a) Each wavelength produces its own fringe pattern, with intensity varying as $\cos^2(\pi\Delta/\lambda_1)$ and $\cos^2(\pi\Delta/\lambda_2)$. When the bright fringes of one fall on the dark fringes of the other, visibility is minimal. This recurs when $\Delta/\lambda_1 - \Delta/\lambda_2$ changes by 1, that is, when the path difference changes by $\Delta_{\text{beat}} = \lambda_1\lambda_2/(\lambda_2 - \lambda_1) \approx \lambda^2/\Delta\lambda$. Since $\Delta = 2d$, the mirror displacement between minima is $\lambda^2/(2\Delta\lambda)$. With $\bar\lambda = 589.29$ nm and $\Delta\lambda = 0.597$ nm: $(589.29)^2/(2 \times 0.597) = 2.91\times10^5$ nm $= 0.291$ mm.

(b) $N = 2d/\bar\lambda = 2(0.291\ \text{mm})/(589.29\ \text{nm}) \approx 987$, essentially $\bar\lambda/\Delta\lambda$.

(c) $\lambda = 2\Delta d/N = 2(0.250\times10^{-3})/790 = 6.33\times10^{-7}$ m $= 633$ nm, consistent with a HeNe laser.

## 17. Summary

- Atoms exchange energy with light by absorption, spontaneous emission and stimulated emission. Einstein's equilibrium argument gives $g_1B_{12} = g_2B_{21}$ and $A_{21}/B_{21} = 8\pi h\nu^3/c^3$; spontaneous emission increasingly dominates at high frequencies.
- A medium amplifies light with gain coefficient $g = \sigma(N_2 - N_1)$, so amplification requires a population inversion, which cannot be produced by optically pumping a two-level system.
- Three-level lasers (ruby) must empty more than half the ground state; four-level lasers (Nd:YAG, HeNe, CO₂ in effect) have an almost empty lower level and much lower thresholds. Lasing begins when round-trip gain equals round-trip loss.
- A Fabry–Pérot cavity selects longitudinal modes spaced by $c/(2nL)$; the number that oscillate is the gain bandwidth divided by this spacing. The photon lifetime sets the passive mode width.
- Coherence time and length are inversely proportional to bandwidth: $l_c \approx c/\Delta\nu = \lambda^2/\Delta\lambda$, ranging from about a micrometre for white light to hundreds of kilometres for stabilized lasers.
- A TEM$_{00}$ laser beam is a Gaussian beam with Rayleigh range $\pi w_0^2/\lambda$ and divergence $\lambda/(\pi w_0)$; its peak intensity is $2P/(\pi w^2)$, and it focuses to a spot of radius about $\lambda f/(\pi w)$.
- Key laser types span gases (HeNe, CO₂, excimer), solids (ruby, Nd:YAG, Ti:sapphire), semiconductors (diodes, VCSELs) and doped fibers. Q-switching gives nanosecond pulses; mode-locking gives femtosecond pulses whose duration is limited by the gain bandwidth.
- Holography records amplitude and phase by interference with a coherent reference wave and reconstructs the original wavefront by diffraction.
- Optical fibers guide light by total internal reflection; NA $= \sqrt{n_1^2 - n_2^2}$, single-mode operation needs $V < 2.405$, and modal and chromatic dispersion limit bandwidth. Low loss near 1550 nm, erbium amplifiers and wavelength multiplexing underpin the internet.
- Intense light makes the polarization nonlinear; $\chi^{(2)}$ in non-centrosymmetric crystals produces second-harmonic generation, which is efficient only when phase matched.
- Michelson interferometers measure displacements in units of $\lambda/2$, spectra and coherence; LIGO uses kilometre-scale arm cavities and enormous circulating power to detect strains of $10^{-21}$.
- Lasers are central to medicine, manufacturing, communications and science. Their hazards, especially to the retina in the 400–1400 nm range, are managed through classification, engineering controls and wavelength-specific eyewear of adequate optical density.

### Key equations

| Quantity | Equation |
|---|---|
| Einstein relations | $g_1B_{12} = g_2B_{21}$, $\quad A_{21}/B_{21} = 8\pi h\nu^3/c^3$ |
| Stimulated/spontaneous ratio in thermal light | $1/(e^{h\nu/k_BT} - 1)$ |
| Gain coefficient | $g = \sigma(N_2 - N_1)$, $\quad I = I_0e^{gz}$ |
| Laser threshold | $g_{\text{th}} = \dfrac{1}{2l}\ln\dfrac{1}{R_1R_2T_i}$ |
| Longitudinal mode spacing | $\Delta\nu_{\text{FSR}} = c/(2nL)$ |
| Photon lifetime | $\tau_p = 2L/(c\delta)$, $\quad \delta\nu_c = 1/(2\pi\tau_p)$ |
| Natural and Doppler widths | $\Delta\nu_{\text{nat}} = 1/(2\pi\tau)$, $\quad \Delta\nu_D = \nu_0\sqrt{8k_BT\ln2/(mc^2)}$ |
| Coherence length | $l_c \approx c/\Delta\nu = \lambda^2/\Delta\lambda$ |
| Gaussian beam | $w(z) = w_0\sqrt{1 + (z/z_R)^2}$, $\quad z_R = \pi w_0^2/\lambda$, $\quad \theta = \lambda/(\pi w_0)$ |
| Peak intensity; focused spot | $I_0 = 2P/(\pi w^2)$, $\quad w_f \approx \lambda f/(\pi w)$ |
| Mode-locked pulse train | period $2L/c$, $\quad \Delta\nu\,\Delta t \ge 0.441$ (Gaussian) |
| Hologram fringe spacing | $\Lambda = \lambda/[2\sin(\theta/2)]$ |
| Numerical aperture; V-number | $\text{NA} = \sqrt{n_1^2 - n_2^2}$, $\quad V = 2\pi a\,\text{NA}/\lambda < 2.405$ |
| Fiber dispersion | $\Delta t_{\text{modal}} = (Ln_1/c)(n_1/n_2 - 1)$, $\quad \Delta t_{\text{chrom}} = DL\Delta\lambda$ |
| SHG coherence length | $L_c = \lambda/\{4[n(2\omega) - n(\omega)]\}$ |
| Michelson fringe counting | $\Delta d = N\lambda/2$, $\quad \Delta L = hL$ |
| Optical density | $T = 10^{-\text{OD}}$ |
