---
title: General Relativity, Gravitation and Black Holes
field: Physics
subfield: Relativity
level: undergraduate
keywords: [general relativity, equivalence principle, spacetime curvature, geodesic, Einstein field equations, metric tensor, Schwarzschild metric, gravitational time dilation, gravitational redshift, GPS, light bending, gravitational lensing, perihelion precession, black hole, event horizon, Hawking radiation, gravitational waves, LIGO, frame dragging]
---

# General Relativity, Gravitation and Black Holes

Special relativity (1905) unified space and time but left gravity out: Newton's gravity acts instantaneously at a distance, which conflicts with the cosmic speed limit $c$. After ten years of effort, Einstein completed the **general theory of relativity** in November 1915. Its central idea: **gravity is not a force but the curvature of spacetime caused by mass and energy**. Objects in free fall follow the straightest possible paths (geodesics) through curved spacetime. As John Wheeler summarized: *"Spacetime tells matter how to move; matter tells spacetime how to curve."*

## 1. The Equivalence Principle

### Weak equivalence principle
All objects fall with the same acceleration in a gravitational field, regardless of their mass or composition (Galileo, Newton; verified by Eötvös-type torsion balance experiments and the MICROSCOPE satellite to about 1 part in $10^{15}$). Equivalently, gravitational mass equals inertial mass.

In Newtonian physics this equality is an unexplained coincidence. Einstein made it the foundation of a new theory.

### Einstein's equivalence principle
> In a small enough region of spacetime, the effects of gravity are indistinguishable from those of acceleration. Locally, the laws of physics in a freely falling frame are those of special relativity.

Einstein called the realization that "a person falling freely would not feel their own weight" his "happiest thought" (1907).

**Thought experiments:**
1. An observer in a closed elevator at rest on Earth feels exactly the same as one in a rocket accelerating at $9.8$ m/s² in deep space. No local experiment can distinguish them.
2. An observer in a freely falling elevator experiences weightlessness — as if gravity were absent. Astronauts in orbit are in free fall.

**Why "local":** over large regions, gravity's non-uniformity (tidal effects) can be detected. Two objects released side by side in a falling elevator slowly converge (both fall toward Earth's center). **Tidal effects are the true signature of spacetime curvature** and cannot be eliminated by any choice of frame.

### Consequences derived from the equivalence principle alone
- **Light bends in a gravitational field:** in an accelerating rocket, a horizontal light beam appears to curve downward. By equivalence, gravity must bend light.
- **Gravitational time dilation:** clocks lower in a gravitational potential run slower. In an accelerating rocket, light sent from the floor to the ceiling arrives redshifted (the ceiling has picked up speed while the light traveled), so the ceiling observer concludes the floor clock runs slow.

## 2. Spacetime Geometry

### The metric
Geometry is encoded in the **metric tensor** $g_{\mu\nu}$, which gives the spacetime interval between nearby events:
$$ds^2 = g_{\mu\nu}\,dx^\mu dx^\nu$$
(summation over repeated indices). In flat spacetime (special relativity), $g_{\mu\nu} = \eta_{\mu\nu} = \text{diag}(1, -1, -1, -1)$. In curved spacetime, $g_{\mu\nu}$ varies from point to point.

### Geodesics
Free particles follow **geodesics** — paths of extremal proper time (for massive particles, maximal). Light follows null geodesics ($ds^2 = 0$). The geodesic equation is
$$\frac{d^2x^\mu}{d\tau^2} + \Gamma^\mu_{\alpha\beta}\frac{dx^\alpha}{d\tau}\frac{dx^\beta}{d\tau} = 0$$
where the **Christoffel symbols** $\Gamma^\mu_{\alpha\beta}$ are built from derivatives of the metric. In the weak-field, slow-motion limit with $g_{00} \approx 1 + 2\Phi/c^2$ ($\Phi$ = Newtonian potential), the geodesic equation reduces to Newton's law $\ddot{\vec x} = -\nabla\Phi$.

**Analogy:** two travelers starting at the equator and both heading due north along "straight lines" (great circles) find themselves converging, as if attracted, even though no force acts. Curvature of the surface does the work. Similarly, an apple and Earth "fall together" because spacetime is curved — mostly, for everyday gravity, it is the curvature of **time** (the warping of $g_{00}$) that matters.

### Curvature
Curvature is described by the **Riemann tensor** $R^\rho{}_{\sigma\mu\nu}$, which measures how vectors change when parallel-transported around closed loops (and governs tidal forces through the geodesic deviation equation). Its contractions are the **Ricci tensor** $R_{\mu\nu}$ and the **Ricci scalar** $R$.

## 3. The Einstein Field Equations

$$\boxed{G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}}, \qquad G_{\mu\nu} = R_{\mu\nu} - \tfrac12Rg_{\mu\nu}$$

- Left side: **geometry** — the Einstein tensor $G_{\mu\nu}$ describes spacetime curvature; $\Lambda$ is the **cosmological constant**.
- Right side: **matter and energy** — the stress–energy tensor $T_{\mu\nu}$ (energy density, momentum density, pressure, stress).
- The coupling $8\pi G/c^4 \approx 2.1\times10^{-43}$ s²/(kg·m) is tiny: spacetime is extremely "stiff", so enormous energy densities are needed for significant curvature.

These are 10 coupled nonlinear partial differential equations. Key features:
- **Not only mass but all energy, momentum and pressure gravitate.** Pressure contributes to gravity, which matters in neutron stars and cosmology.
- The equations automatically imply local energy–momentum conservation ($\nabla_\mu T^{\mu\nu} = 0$).
- In the weak-field limit they reduce to Poisson's equation $\nabla^2\Phi = 4\pi G\rho$ — Newtonian gravity.
- Einstein introduced $\Lambda$ in 1917 to allow a static universe; after Hubble discovered cosmic expansion, he reportedly called it his "biggest blunder". Since 1998, observations of distant supernovae show the expansion is accelerating, consistent with a positive $\Lambda$ (dark energy).

## 4. The Schwarzschild Solution

Just weeks after Einstein published his equations, Karl Schwarzschild — while serving on the Russian front in World War I — found the exact solution for the spacetime outside a spherical, non-rotating mass $M$:
$$ds^2 = \left(1 - \frac{r_s}{r}\right)c^2dt^2 - \left(1 - \frac{r_s}{r}\right)^{-1}dr^2 - r^2(d\theta^2 + \sin^2\theta\,d\phi^2)$$
with the **Schwarzschild radius**
$$\boxed{r_s = \frac{2GM}{c^2}}$$

| Object | Mass | $r_s$ |
|---|---|---|
| Earth | $5.97\times10^{24}$ kg | 8.9 mm |
| Sun | $1.99\times10^{30}$ kg | 2.95 km |
| Typical stellar black hole (10 $M_\odot$) | | 29.5 km |
| Sagittarius A* (4.3 million $M_\odot$) | | ~12.7 million km (~0.085 AU) |
| M87* (6.5 billion $M_\odot$) | | ~1.9×10¹⁰ km (~130 AU) |

For ordinary bodies, $r_s$ is far inside the object, where the exterior solution doesn't apply.

## 5. Classical Tests and Modern Confirmations

### 5.1 Perihelion precession of Mercury
Mercury's elliptical orbit rotates (precesses) by 574 arcseconds per century. Newtonian perturbations from other planets account for 531″. The remaining **43″ per century** had puzzled astronomers since Le Verrier (1859), who even proposed an unseen planet "Vulcan". General relativity predicts exactly 43″ — Einstein's first triumph (1915). He wrote that he was "beside himself with joy" for days.

### 5.2 Deflection of light
GR predicts light grazing the Sun is deflected by
$$\delta = \frac{4GM}{c^2R} \approx 1.75''$$
twice the value from a naive Newtonian/equivalence-principle calculation (half the effect comes from the curvature of space, half from time). The 1919 solar-eclipse expeditions led by Arthur Eddington (Príncipe) and Andrew Crommelin (Sobral, Brazil) measured the shift of stars near the eclipsed Sun, confirming Einstein's prediction and making him world-famous overnight. Modern radio interferometry confirms it to 0.01%.

**Gravitational lensing:** massive galaxies and clusters bend light from background objects, producing multiple images, arcs and **Einstein rings**. Lensing is used to map dark matter, weigh galaxy clusters, magnify very distant galaxies, and detect exoplanets (microlensing).

### 5.3 Gravitational time dilation and redshift
A clock at radius $r$ outside a mass $M$ runs slower than a distant clock by the factor
$$\frac{d\tau}{dt} = \sqrt{1 - \frac{r_s}{r}} \approx 1 - \frac{GM}{rc^2}$$
Near Earth's surface, a height difference $h$ gives a fractional rate difference $\frac{gh}{c^2} \approx 1.1\times10^{-16}$ per meter.

- **Pound–Rebka experiment (1959):** gamma rays sent up a 22.5 m tower at Harvard were blueshifted/redshifted by the predicted $2.5\times10^{-15}$, measured using the Mössbauer effect.
- **Optical atomic clocks** now detect time dilation from height differences of just centimeters (NIST, 2010; and millimeter-scale differences within a single atomic sample, 2022).
- **Gravitational redshift** of light from white dwarfs (e.g. Sirius B) and of stars orbiting Sgr A* (S2, observed 2018).
- **Shapiro delay:** radar signals passing near the Sun take longer than expected (confirmed by Cassini to 1 part in 10⁵).

### 5.4 GPS: relativity in your pocket
GPS satellites orbit at ~20 200 km altitude with speed ~3.9 km/s.
- **Special relativity** (velocity): satellite clocks run slow by about **7 μs/day**.
- **General relativity** (weaker gravity at altitude): satellite clocks run fast by about **45 μs/day**.
- **Net:** satellite clocks gain about **38 μs/day** relative to ground clocks.
Light travels about 11.4 km in 38 μs. Without relativistic corrections, GPS positions would accumulate errors of roughly 10 km per day. The satellite clocks are deliberately tuned slow before launch (10.22999999543 MHz instead of 10.23 MHz) to compensate.

### 5.5 Frame dragging
A rotating mass drags spacetime around with it (the **Lense–Thirring effect**). Gravity Probe B (2011) measured the precession of gyroscopes in Earth orbit due to both geodetic effects (6606 milliarcseconds/year) and frame dragging (39 mas/year), confirming GR's predictions.

## 6. Black Holes

A **black hole** is a region of spacetime from which nothing, not even light, can escape. It forms when matter collapses within its Schwarzschild radius.

### Anatomy (non-rotating black hole)
- **Event horizon** at $r = r_s$: the boundary of no return. It is not a physical surface; a freely falling observer crossing a large black hole's horizon notices nothing special locally. To a distant observer, however, an infalling object appears to slow down, redden and fade, never quite crossing.
- **Photon sphere** at $r = 1.5r_s$: light can orbit the black hole (unstably).
- **Innermost stable circular orbit (ISCO)** at $r = 3r_s$ for massive particles; matter in accretion disks spirals inward from here.
- **Singularity** at $r = 0$: curvature becomes infinite and GR breaks down; a quantum theory of gravity is needed.

The coordinate singularity at $r = r_s$ in the Schwarzschild metric is an artifact of the coordinates (removable by changing coordinates, e.g. Kruskal–Szekeres or Eddington–Finkelstein); the singularity at $r = 0$ is physical.

### Rotating and charged black holes
The **no-hair theorem**: a stationary black hole is fully characterized by just three numbers — **mass, angular momentum and electric charge**. All other information about what fell in is (classically) hidden.
- **Kerr solution** (1963): rotating black holes. Outside the horizon lies the **ergosphere**, where nothing can remain stationary; energy can be extracted from the rotation (Penrose process), which may power astrophysical jets.
- Astrophysical black holes are essentially uncharged but often spin rapidly.

### Types and evidence
- **Stellar-mass black holes** (~3–100 $M_\odot$): remnants of massive stars. First strong candidate: Cygnus X-1 (1971), an X-ray binary.
- **Supermassive black holes** ($10^6$–$10^{10}$ $M_\odot$) at the centers of most galaxies. Sagittarius A* in the Milky Way (~4.3 million $M_\odot$) was established by tracking stars' orbits for decades (Genzel and Ghez, Nobel 2020). Quasars are supermassive black holes accreting matter at enormous rates.
- **Intermediate-mass black holes** (~$10^2$–$10^5$ $M_\odot$): fewer clear detections; GW190521 produced a ~142 $M_\odot$ remnant.
- **Images:** the Event Horizon Telescope imaged the shadows of M87* (2019) and Sgr A* (2022).

Roger Penrose (Nobel 2020) proved that black hole formation is a robust prediction of GR, not an artifact of perfect symmetry.

### Hawking radiation
Stephen Hawking (1974) combined quantum field theory with curved spacetime and found that black holes emit thermal radiation with temperature
$$T_H = \frac{\hbar c^3}{8\pi GMk_B} \approx 6.2\times10^{-8}\text{ K}\times\frac{M_\odot}{M}$$
Black holes therefore have entropy, given by the **Bekenstein–Hawking formula** $S = \frac{k_Bc^3A}{4G\hbar}$ — proportional to the horizon **area**, not volume, which inspired the holographic principle. Stellar black holes are far colder than the cosmic microwave background (2.7 K), so they currently absorb more than they emit. A solar-mass black hole would take ~$10^{67}$ years to evaporate. Hawking radiation has not been observed directly. The fate of information that falls into an evaporating black hole — the **information paradox** — remains a central question in theoretical physics.

## 7. Gravitational Waves

General relativity predicts that accelerating masses produce ripples in spacetime that propagate at the speed of light — **gravitational waves**. They stretch and squeeze space perpendicular to their direction of travel, with strain $h = \Delta L/L$.

- **Indirect evidence:** the Hulse–Taylor binary pulsar (discovered 1974) loses orbital energy at exactly the rate GR predicts for gravitational radiation (Nobel 1993).
- **Direct detection:** on 14 September 2015 LIGO detected **GW150914**, from two black holes (~36 and ~29 $M_\odot$) merging ~1.3 billion light-years away. About 3 solar masses were converted to gravitational-wave energy in a fraction of a second — a peak power exceeding the combined light output of all stars in the observable universe. The strain at Earth was ~$10^{-21}$.
- **GW170817 (2017):** merging neutron stars detected in gravitational waves *and* across the electromagnetic spectrum (a gamma-ray burst and a kilonova) — the birth of multi-messenger astronomy. It confirmed that gravitational waves travel at the speed of light (to 1 part in $10^{15}$) and that such mergers produce heavy elements like gold and platinum via the r-process.
- Since then, the LIGO–Virgo–KAGRA network has detected hundreds of merger events. **Pulsar timing arrays** (NANOGrav and others, 2023) found evidence for a low-frequency gravitational-wave background, likely from supermassive black hole binaries. The space-based detector **LISA** is planned for the 2030s.

## 8. Cosmology (Brief)

Applying GR to a homogeneous, isotropic universe gives the **Friedmann–Lemaître–Robertson–Walker** (FLRW) metric and the Friedmann equations, describing an expanding (or contracting) universe. GR thus predicted that the universe cannot be static — confirmed by Hubble's discovery of expansion (1929). The Big Bang model, cosmic microwave background, and the ΛCDM model are covered in the astronomy documents.

## 9. Open Problems

- **Quantum gravity:** GR is a classical theory, incompatible with quantum mechanics at the Planck scale ($\ell_P = \sqrt{\hbar G/c^3} \approx 1.6\times10^{-35}$ m, $E_P \approx 1.2\times10^{19}$ GeV). Candidates include string theory and loop quantum gravity.
- **Singularities:** inside black holes and at the Big Bang, GR predicts its own breakdown.
- **Dark matter and dark energy:** explained within GR by unseen matter and a cosmological constant, but their nature is unknown. Some modified-gravity theories try to avoid them; so far GR passes every test.

## 10. Summary

| Concept | Formula / Value |
|---|---|
| Einstein field equations | $G_{\mu\nu} + \Lambda g_{\mu\nu} = \frac{8\pi G}{c^4}T_{\mu\nu}$ |
| Schwarzschild radius | $r_s = 2GM/c^2$ |
| Gravitational time dilation | $d\tau/dt = \sqrt{1 - r_s/r}$ |
| Weak-field rate difference | $\Delta f/f \approx gh/c^2$ |
| Light deflection by Sun | $4GM/(c^2R) \approx 1.75''$ |
| Mercury's anomalous precession | 43″ per century |
| Photon sphere | $1.5r_s$ |
| ISCO (Schwarzschild) | $3r_s$ |
| Hawking temperature | $T = \hbar c^3/(8\pi GMk_B)$ |
| Black hole entropy | $S = k_Bc^3A/(4G\hbar)$ |
| GPS clock offset | ≈ +38 μs/day (−7 SR, +45 GR) |
