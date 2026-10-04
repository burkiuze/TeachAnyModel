---
title: Nuclear Physics - Structure, Radioactivity, Fission and Fusion
field: Physics
subfield: Nuclear Physics
level: high-school to undergraduate
keywords: [nucleus, proton, neutron, isotope, strong nuclear force, binding energy, mass defect, semi-empirical mass formula, nuclear shell model, magic numbers, radioactivity, alpha decay, beta decay, gamma decay, half-life, decay constant, radiocarbon dating, nuclear fission, chain reaction, nuclear reactor, nuclear fusion, stellar nucleosynthesis, radiation dosimetry, sievert]
---

# Nuclear Physics: Structure, Radioactivity, Fission and Fusion

The atomic nucleus contains more than 99.9% of an atom's mass in a region about 100 000 times smaller than the atom. Nuclear physics explains why the Sun shines, how the elements were made, how to date ancient artifacts, how nuclear power plants and weapons work, and how radiation is used in medicine.

## 1. Discovery and Basic Structure

- **1896:** Henri Becquerel discovered radioactivity in uranium salts.
- **1898:** Marie and Pierre Curie discovered polonium and radium. Marie Curie is the only person to win Nobel Prizes in two different sciences (Physics 1903, Chemistry 1911).
- **1899–1903:** Ernest Rutherford identified alpha and beta rays; Paul Villard discovered gamma rays (1900). Rutherford and Frederick Soddy showed radioactivity transmutes elements.
- **1911:** Rutherford's analysis of Geiger and Marsden's gold-foil scattering revealed the nucleus.
- **1919:** Rutherford achieved the first artificial transmutation (nitrogen + alpha → oxygen + proton), identifying the proton.
- **1932:** James Chadwick discovered the neutron.

### Notation and terminology
A nuclide is written $^A_ZX$:
- $Z$ = **atomic number** (number of protons) — determines the element.
- $N$ = **neutron number**.
- $A = Z + N$ = **mass number** (number of nucleons).

Example: $^{235}_{92}$U has 92 protons and 143 neutrons.

- **Isotopes:** same $Z$, different $N$ (e.g. ¹H, ²H deuterium, ³H tritium; ¹²C, ¹³C, ¹⁴C).
- **Isobars:** same $A$ (e.g. ¹⁴C and ¹⁴N).
- **Isotones:** same $N$.
- **Isomers:** same nuclide in a long-lived excited state (e.g. technetium-99m).

### Size and density
Nuclear radius: $R \approx R_0A^{1/3}$, $R_0 \approx 1.2$ fm (1 fm = $10^{-15}$ m). Since volume $\propto A$, all nuclei have roughly the **same density**, ~$2.3\times10^{17}$ kg/m³ — like incompressible liquid drops. A teaspoon of nuclear matter would weigh about a billion tonnes. Neutron stars are essentially giant nuclei held together by gravity.

### Masses
The unified atomic mass unit: $1\text{ u} = \frac{1}{12}m(^{12}\text{C}) = 1.66054\times10^{-27}$ kg $= 931.494$ MeV/c².
- Proton: 1.007276 u (938.272 MeV/c²)
- Neutron: 1.008665 u (939.565 MeV/c²) — slightly heavier than the proton, so free neutrons decay (half-life ~10 min).
- Electron: 0.000549 u (0.511 MeV/c²)

## 2. The Strong Nuclear Force

Protons repel each other electrically; at nuclear distances the repulsion is enormous (~230 N between two protons 1 fm apart — on a single proton!). Nuclei are held together by the **strong nuclear force** (residual strong interaction), which:
- Is **attractive** and very strong at distances ~1–2 fm (about 100 times stronger than electromagnetism at that range).
- Has **short range** (~2–3 fm), falling off rapidly — so nucleons interact essentially only with nearest neighbors (**saturation**).
- Becomes strongly **repulsive** below ~0.5 fm (hard core), preventing collapse.
- Is approximately **charge-independent**: p–p, n–n and p–n interactions are nearly identical (isospin symmetry).
- Is spin-dependent and has a non-central (tensor) component.

At a deeper level it is a residual effect of quantum chromodynamics (QCD) binding quarks via gluons, analogous to van der Waals forces between neutral molecules. Yukawa (1935) modeled it as exchange of a massive particle; the range $\hbar/(m_\pi c) \approx 1.4$ fm predicted the **pion** (discovered 1947).

## 3. Binding Energy

### Mass defect
The mass of a nucleus is **less** than the sum of its constituents' masses. The difference, the **mass defect** $\Delta m$, corresponds to the **binding energy** — the energy needed to separate the nucleus into free nucleons:
$$\boxed{B = [Zm_p + Nm_n - M_{\text{nucleus}}]c^2 = [Zm(^1\text{H}) + Nm_n - M_{\text{atom}}]c^2}$$
(The second form uses atomic masses, so electron masses cancel.)

**Worked example 3.1 — Helium-4:**
$2m(^1\text{H}) + 2m_n = 2(1.007825) + 2(1.008665) = 4.032980$ u.
$M(^4\text{He}) = 4.002603$ u. $\Delta m = 0.030377$ u.
$B = 0.030377\times931.494 \approx 28.30$ MeV, i.e. **7.07 MeV per nucleon**.
By comparison, the binding energy of the hydrogen atom's electron is 13.6 eV — nuclear energies are about a million times larger than chemical energies.

### The binding energy curve
The **binding energy per nucleon** $B/A$ is the key to nuclear energy:
- Rises steeply for light nuclei (²H: 1.11 MeV; ⁴He: 7.07 MeV — anomalously high, which is why alpha particles are emitted as units).
- Peaks around **iron and nickel** (⁵⁶Fe: 8.79 MeV; ⁶²Ni: 8.79 MeV, the most tightly bound per nucleon).
- Slowly decreases for heavy nuclei (²³⁸U: 7.57 MeV) because of growing Coulomb repulsion.

**Consequences:**
- **Fusion** of light nuclei into heavier ones (up to iron) releases energy.
- **Fission** of heavy nuclei into medium-mass ones releases energy.
- Iron is the "ash" of nuclear burning: stars cannot extract energy by fusing beyond iron, which triggers core collapse in massive stars.

### The semi-empirical mass formula (liquid-drop model)
Weizsäcker (1935) modeled the nucleus as a charged liquid drop:
$$B(A, Z) = a_VA - a_SA^{2/3} - a_C\frac{Z(Z-1)}{A^{1/3}} - a_A\frac{(A - 2Z)^2}{A} + \delta(A, Z)$$

| Term | Physical origin | Typical coefficient |
|---|---|---|
| Volume $a_VA$ | Each nucleon bound to neighbors (saturation) | ~15.8 MeV |
| Surface $-a_SA^{2/3}$ | Surface nucleons have fewer neighbors | ~18.3 MeV |
| Coulomb $-a_CZ(Z-1)/A^{1/3}$ | Proton repulsion | ~0.71 MeV |
| Asymmetry $-a_A(N - Z)^2/A$ | Pauli principle: unequal $N$, $Z$ costs energy | ~23.2 MeV |
| Pairing $\delta$ | Extra binding for paired nucleons: + even–even, − odd–odd, 0 odd-$A$ | ~$\pm12/\sqrt A$ MeV |

It reproduces binding energies to within ~1% for most nuclei, predicts the **valley of stability** (stable nuclei have $N \approx Z$ for light elements, $N > Z$ for heavy ones — ²⁰⁸Pb has $N/Z \approx 1.54$ — to dilute Coulomb repulsion), and explains why fission releases energy.

### The nuclear shell model
Nuclei with certain numbers of protons or neutrons — the **magic numbers 2, 8, 20, 28, 50, 82, 126** — are exceptionally stable (higher binding energy, more stable isotopes, low neutron-capture cross sections, spherical shapes). Maria Goeppert Mayer and J. Hans D. Jensen (1949, Nobel 1963) explained them with a shell model in which nucleons occupy quantized orbitals in a mean potential with strong **spin–orbit coupling**. **Doubly magic** nuclei include ⁴He, ¹⁶O, ⁴⁰Ca, ⁴⁸Ca, ²⁰⁸Pb. Searches for the "island of stability" among superheavy elements are guided by predicted magic numbers near $Z = 114$–126, $N = 184$.

## 4. Radioactive Decay

Unstable nuclei decay spontaneously to more stable configurations, emitting radiation. Of ~3300 known nuclides, only about 250 are stable.

### Types of decay

| Decay | Emitted | Change | Example | Penetration |
|---|---|---|---|---|
| Alpha (α) | ⁴He nucleus | $Z - 2$, $A - 4$ | $^{238}_{92}\text{U}\to{}^{234}_{90}\text{Th} + \alpha$ | Stopped by paper or skin (~cm in air) |
| Beta-minus (β⁻) | Electron + antineutrino | $Z + 1$, $A$ same | $^{14}_6\text{C}\to{}^{14}_7\text{N} + e^- + \bar\nu_e$ | Stopped by few mm aluminum |
| Beta-plus (β⁺) | Positron + neutrino | $Z - 1$, $A$ same | $^{18}_9\text{F}\to{}^{18}_8\text{O} + e^+ + \nu_e$ | Positron annihilates → two 511 keV photons |
| Electron capture (EC) | Neutrino (X-rays follow) | $Z - 1$ | $^{40}_{19}\text{K} + e^-\to{}^{40}_{18}\text{Ar} + \nu_e$ | — |
| Gamma (γ) | High-energy photon | None (de-excitation) | $^{60}\text{Ni}^*\to{}^{60}\text{Ni} + \gamma$ | Reduced by cm of lead, m of concrete |
| Spontaneous fission | Two fragments + neutrons | Splits | ²⁵²Cf | — |
| Neutron emission | Neutron | $A - 1$ | Very neutron-rich nuclei | Highly penetrating |

**Conservation laws in decays:** charge, nucleon number (baryon number), lepton number, energy, momentum and angular momentum are all conserved.

### Alpha decay
Occurs mainly in heavy nuclei ($A > 150$). The released energy is shared between the alpha and the recoiling daughter, giving alphas **discrete** energies (4–9 MeV). The process requires quantum tunneling through the Coulomb barrier (Gamow, 1928), explaining the Geiger–Nuttall relation between energy and half-life. Smoke detectors use americium-241 alpha sources to ionize air.

### Beta decay and the neutrino
In β⁻ decay a neutron converts to a proton: $n \to p + e^- + \bar\nu_e$ (at the quark level, $d \to u + e^- + \bar\nu_e$ via a virtual W⁻ boson). Electrons emerge with a **continuous** energy spectrum, which seemed to violate energy conservation. In 1930 Wolfgang Pauli proposed a nearly massless, neutral particle carrying away the missing energy — the **neutrino** ("little neutral one", named by Fermi). Fermi's theory of beta decay (1934) introduced the weak interaction. Neutrinos were detected by Cowan and Reines in 1956 at the Savannah River reactor. Trillions of solar neutrinos pass through your body every second.

β⁺ decay converts a proton to a neutron and requires the parent's atomic mass to exceed the daughter's by at least $2m_ec^2 = 1.022$ MeV. Positron emitters (¹⁸F, ¹¹C, ¹⁵O) are used in **PET scans**.

### Gamma decay
After alpha or beta decay, the daughter nucleus is often left excited; it emits gamma photons (keV–MeV) with discrete energies characteristic of nuclear energy levels. **Technetium-99m** (140 keV gamma, 6-hour half-life) is the most widely used medical radioisotope (~40 million procedures per year).

### Decay series
Heavy elements decay through chains of alpha and beta decays until reaching a stable lead isotope:
- Uranium series: ²³⁸U → ... → ²⁰⁶Pb (8 α, 6 β⁻)
- Actinium series: ²³⁵U → ... → ²⁰⁷Pb
- Thorium series: ²³²Th → ... → ²⁰⁸Pb
Radon-222, a gas in the uranium series, seeps from soil and rocks into buildings and is the second leading cause of lung cancer after smoking.

## 5. The Law of Radioactive Decay

Decay is a **random** quantum process: each nucleus has a constant probability per unit time $\lambda$ (the **decay constant**) of decaying, independent of its age and of external conditions (temperature, pressure, chemistry — with tiny exceptions for electron capture).
$$\frac{dN}{dt} = -\lambda N \quad\Longrightarrow\quad \boxed{N(t) = N_0e^{-\lambda t}}$$

**Half-life:** the time for half the nuclei to decay:
$$\boxed{t_{1/2} = \frac{\ln2}{\lambda} \approx \frac{0.693}{\lambda}}$$
After $n$ half-lives, the fraction remaining is $(1/2)^n$. **Mean lifetime:** $\tau = 1/\lambda = t_{1/2}/\ln2 \approx 1.443\,t_{1/2}$.

**Activity:** decays per second, $A = \lambda N = A_0e^{-\lambda t}$. Units: becquerel (1 Bq = 1 decay/s); curie (1 Ci = $3.7\times10^{10}$ Bq, approximately the activity of 1 g of radium-226).

| Nuclide | Half-life | Decay | Use / significance |
|---|---|---|---|
| Polonium-214 | 164 μs | α | Uranium series |
| Fluorine-18 | 110 min | β⁺ | PET imaging |
| Technetium-99m | 6.01 h | γ (IT) | Medical imaging |
| Iodine-131 | 8.02 d | β⁻ | Thyroid treatment; fallout hazard |
| Cobalt-60 | 5.27 y | β⁻, γ | Radiotherapy, sterilization |
| Tritium (³H) | 12.3 y | β⁻ | Fusion fuel, glowing signs |
| Strontium-90 | 28.8 y | β⁻ | Fallout hazard (bone-seeking) |
| Cesium-137 | 30.2 y | β⁻, γ | Fallout (Chernobyl, Fukushima) |
| Radium-226 | 1600 y | α | Historical luminous paint |
| Carbon-14 | 5730 y | β⁻ | Radiocarbon dating |
| Plutonium-239 | 24 100 y | α | Reactor fuel, weapons |
| Uranium-235 | 704 million y | α | Reactor fuel |
| Potassium-40 | 1.25 billion y | β⁻, EC | Dating rocks; natural body radioactivity |
| Uranium-238 | 4.47 billion y | α | Dating Earth's oldest rocks |
| Thorium-232 | 14.0 billion y | α | Possible future reactor fuel |
| Bismuth-209 | $2.0\times10^{19}$ y | α | Long thought stable (decay observed 2003) |

### Worked example 5.1
**Problem:** A sample contains $10^{20}$ atoms of iodine-131 ($t_{1/2} = 8.02$ d). Find its initial activity and the number remaining after 30 days.
**Solution:** $\lambda = 0.693/(8.02\times86400\text{ s}) = 1.00\times10^{-6}$ s⁻¹. $A_0 = \lambda N_0 = 1.0\times10^{14}$ Bq (≈ 2700 Ci).
After 30 days: $N = 10^{20}e^{-0.0864\times30} = 10^{20}e^{-2.59} \approx 7.5\times10^{18}$ (about 7.5% remains).

### Radiometric dating
**Radiocarbon dating** (Willard Libby, 1949; Nobel 1960): cosmic-ray neutrons convert atmospheric ¹⁴N into ¹⁴C, which mixes into CO₂ and enters living organisms, maintaining a roughly constant ratio ¹⁴C/¹²C ≈ $1.2\times10^{-12}$. When an organism dies, intake stops and ¹⁴C decays. Measuring the remaining fraction gives the age:
$$t = \frac{t_{1/2}}{\ln2}\ln\frac{N_0}{N}$$
Useful up to ~50 000 years. Calibration curves (tree rings, corals, cave deposits) correct for historical variations in atmospheric ¹⁴C. Nuclear weapons tests in the 1950s–60s nearly doubled atmospheric ¹⁴C (the "bomb pulse"), now used in forensics to date tissues.

**Worked example 5.2:** charcoal from an ancient hearth has 25% of the ¹⁴C activity of living wood. Age = 2 half-lives = 11 460 years.

**Other methods:** potassium–argon and argon–argon dating (volcanic rocks, up to billions of years; dated hominin fossils at Olduvai Gorge); uranium–lead dating of zircon crystals (oldest terrestrial minerals: 4.4 billion years, Jack Hills, Australia); rubidium–strontium; meteorite dating gives the age of the Solar System, 4.567 billion years.

## 6. Nuclear Reactions

General form: $a + X \to Y + b$, written $X(a, b)Y$. Conserved: charge, nucleon number, energy, momentum, angular momentum.

**Q-value:** energy released, $Q = (m_{\text{initial}} - m_{\text{final}})c^2$. $Q > 0$: exothermic; $Q < 0$: endothermic (requires a threshold kinetic energy).

Examples:
- $^{14}\text{N}(\alpha, p)^{17}\text{O}$: first artificial transmutation (Rutherford, 1919).
- $^9\text{Be}(\alpha, n)^{12}\text{C}$: Chadwick's neutron source.
- Neutron activation: $^{59}\text{Co}(n, \gamma)^{60}\text{Co}$.
- $^{6}\text{Li}(n, \alpha)^3\text{H}$: breeding tritium for fusion.

Reaction probabilities are expressed as **cross sections** $\sigma$, in **barns** (1 b = $10^{-28}$ m², roughly the geometric size of a heavy nucleus; "as big as a barn" by nuclear standards). Slow (thermal) neutrons have huge cross sections for some reactions — ²³⁵U fission: ~585 b; ¹¹³Cd capture: ~20 000 b; ¹³⁵Xe capture: ~2.6 million b (a notorious reactor poison).

## 7. Nuclear Fission

### Discovery
In December 1938 Otto Hahn and Fritz Strassmann found barium among the products of uranium bombarded with neutrons. Lise Meitner and her nephew Otto Frisch interpreted this as the uranium nucleus splitting in two — **fission** — and calculated that it releases ~200 MeV, using the liquid-drop model and $E = mc^2$.

### The process
A thermal neutron absorbed by ²³⁵U forms ²³⁶U in a highly excited state, which deforms and splits:
$$n + {}^{235}\text{U} \to {}^{236}\text{U}^* \to {}^{141}\text{Ba} + {}^{92}\text{Kr} + 3n + \sim200\text{ MeV}$$
(one of many possible channels; fragment masses cluster around $A \approx 95$ and $A \approx 140$).

**Energy budget per fission (~200 MeV):** fragment kinetic energy ~167 MeV; prompt neutrons ~5 MeV; prompt gammas ~7 MeV; beta and gamma decay of fragments ~13 MeV; antineutrinos ~10 MeV (escapes).

Fission of 1 kg of ²³⁵U releases about $8\times10^{13}$ J (~20 kilotons of TNT equivalent; ~22 GWh) — about 2.7 million times more than burning 1 kg of coal.

**Fissile vs. fertile:** ²³⁵U, ²³³U and ²³⁹Pu are **fissile** (fission with slow neutrons). ²³⁸U and ²³²Th are **fertile**: they absorb neutrons and transmute (via beta decays) into fissile ²³⁹Pu and ²³³U. Natural uranium is 99.27% ²³⁸U and only 0.72% ²³⁵U.

### Chain reactions
Each fission releases on average ~2.4 neutrons. If at least one causes another fission, a self-sustaining **chain reaction** results. The **multiplication factor** $k$ is the average number of fissions caused by neutrons from one fission:
- $k < 1$: subcritical (dies out)
- $k = 1$: critical (steady — a reactor at constant power)
- $k > 1$: supercritical (exponential growth — power increase, or a bomb)

The first controlled chain reaction: Chicago Pile-1, under Enrico Fermi, 2 December 1942.

### Nuclear reactors
Components of a typical **light-water reactor**:
- **Fuel:** uranium oxide enriched to 3–5% ²³⁵U.
- **Moderator:** water (or graphite, heavy water) slows fast neutrons (~2 MeV) to thermal energies (~0.025 eV) where the fission cross section is much larger.
- **Control rods:** neutron absorbers (boron, cadmium, hafnium) inserted or withdrawn to regulate $k$.
- **Coolant:** carries heat to steam generators; turbines drive electrical generators (~33% efficiency).
- **Delayed neutrons:** about 0.65% of fission neutrons (for ²³⁵U) are emitted seconds after fission by fragment decays. This slows reactor response from milliseconds to seconds, making control possible.
- **Negative feedback:** in water-moderated reactors, rising temperature reduces moderation and reactivity — inherent safety. (The Chernobyl RBMK design had a positive void coefficient, contributing to the 1986 disaster.)

**Nuclear power** provides about 9–10% of world electricity with very low CO₂ emissions per kWh. Challenges: long-lived radioactive waste (spent fuel requires isolation for thousands of years; deep geological repositories such as Finland's Onkalo), accident risk (Three Mile Island 1979, Chernobyl 1986, Fukushima 2011), proliferation concerns, and high capital costs. Developments: small modular reactors, fast breeder reactors, thorium fuel cycles.

**Natural reactor:** about 2 billion years ago, uranium deposits at **Oklo, Gabon** sustained natural fission chain reactions for hundreds of thousands of years, when ²³⁵U was ~3% of natural uranium.

### Nuclear weapons
A fission bomb rapidly assembles a supercritical mass of highly enriched uranium (>90% ²³⁵U) or plutonium-239 — by gun-type assembly (Hiroshima, 1945, ~15 kt) or implosion (Trinity test and Nagasaki, ~21 kt). Thermonuclear (hydrogen) bombs use a fission primary to ignite fusion in a secondary, with yields up to megatons (Tsar Bomba, 1961: ~50 Mt).

## 8. Nuclear Fusion

### Fusion in stars
Fusing light nuclei releases energy but requires overcoming the Coulomb barrier, which demands extreme temperatures (millions of kelvin) and densities. In the Sun's core (~15.7 million K), fusion proceeds via the **proton–proton chain**:
$$p + p \to {}^2\text{H} + e^+ + \nu_e \quad(\text{slow weak-interaction step, ~billions of years per proton})$$
$$^2\text{H} + p \to {}^3\text{He} + \gamma$$
$$^3\text{He} + {}^3\text{He} \to {}^4\text{He} + 2p$$
Net: $4p \to {}^4\text{He} + 2e^+ + 2\nu_e + 26.7$ MeV (about 0.7% of the mass converted to energy). The Sun converts ~600 million tonnes of hydrogen into helium each second. In stars heavier than ~1.3 solar masses, the **CNO cycle** dominates, using carbon, nitrogen and oxygen as catalysts (Bethe, Nobel 1967).

### Stellar nucleosynthesis
- **Big Bang nucleosynthesis** (first ~3–20 minutes): ~75% H, ~25% He by mass, traces of D, ³He, ⁷Li.
- **Stars:** helium burning (triple-alpha process, $3\,^4\text{He}\to{}^{12}\text{C}$, via the Hoyle resonance predicted by Fred Hoyle in 1953), then carbon, neon, oxygen and silicon burning in massive stars, up to iron.
- **Beyond iron:** neutron capture — the slow **s-process** in asymptotic giant branch stars and the rapid **r-process** in neutron-star mergers and possibly some supernovae (confirmed by the 2017 kilonova). The gold in jewelry and the iodine in your thyroid were forged in such events.
"We are made of star stuff." — Carl Sagan.

### Controlled fusion on Earth
The most accessible reaction is deuterium–tritium:
$$^2\text{H} + {}^3\text{H} \to {}^4\text{He}\;(3.5\text{ MeV}) + n\;(14.1\text{ MeV}), \qquad Q = 17.6\text{ MeV}$$
Requirements (**Lawson criterion**): temperature ~100–150 million K (hotter than the Sun's core, since we lack its density and size), and a sufficient product of density and confinement time ($n\tau_E \gtrsim 10^{20}$ s/m³ for D–T).
- **Magnetic confinement:** tokamaks (JET; ITER in France, under construction; JT-60SA), stellarators (Wendelstein 7-X). JET set an energy record of 69 MJ in 2023.
- **Inertial confinement:** lasers compress fuel pellets. The **National Ignition Facility** achieved ignition (target gain > 1: 3.15 MJ out from 2.05 MJ of laser energy) on 5 December 2022, with later shots exceeding 5 MJ.
- Advantages: abundant fuel (deuterium from seawater; tritium bred from lithium), no long-lived high-level waste, no chain-reaction runaway. Challenges: sustaining plasmas, materials withstanding 14 MeV neutron bombardment, tritium breeding, net electricity production.

## 9. Radiation and Health

### Interaction with matter
- **Alpha particles:** heavy and doubly charged; lose energy rapidly through ionization; range ~4 cm in air, ~40 μm in tissue. Harmless externally (stopped by dead skin) but very dangerous if ingested or inhaled (e.g. polonium-210, radon progeny).
- **Beta particles:** range ~meters in air, mm in tissue; shielded by plastic or aluminum (avoid high-Z materials for high-energy betas, which produce bremsstrahlung X-rays).
- **Gamma rays and X-rays:** interact by the photoelectric effect, Compton scattering and pair production; attenuate exponentially, $I = I_0e^{-\mu x}$; characterized by half-value layers. Dense materials (lead, concrete) shield best.
- **Neutrons:** uncharged; slowed by hydrogen-rich materials (water, polyethylene) and captured by boron or cadmium.

### Dosimetry
| Quantity | Unit | Meaning |
|---|---|---|
| Absorbed dose | gray (Gy) = J/kg | Energy deposited per mass |
| Equivalent dose | sievert (Sv) = Gy × $w_R$ | Weighted by radiation type ($w_R$ = 1 for photons/electrons, 20 for alphas, 2.5–20 for neutrons) |
| Effective dose | sievert (Sv) | Further weighted by tissue sensitivity |

Older units: 1 rad = 0.01 Gy; 1 rem = 0.01 Sv.

### Typical doses
| Source | Effective dose |
|---|---|
| Eating a banana (⁴⁰K) | ~0.1 μSv |
| Chest X-ray | ~0.02–0.1 mSv |
| Transatlantic flight | ~0.04–0.08 mSv |
| Average annual natural background | ~2.4 mSv (radon ~1.3) |
| Head CT scan | ~2 mSv |
| Annual occupational limit (radiation workers) | 20 mSv (averaged) |
| ISS astronaut, 6 months | ~80–160 mSv |
| Threshold for acute radiation sickness | ~1 Sv (1000 mSv) |
| ~50% lethal without treatment (LD50/60) | ~4–5 Sv |

Health effects: **deterministic** effects (radiation burns, acute radiation syndrome, cataracts) above thresholds; **stochastic** effects (cancer risk, ~5% per Sv by the linear no-threshold model used for radiation protection). Protection principles: **time** (minimize), **distance** (inverse-square law), **shielding**, and ALARA ("as low as reasonably achievable").

### Medical applications
Diagnostic imaging (X-ray, CT, PET, SPECT with ⁹⁹ᵐTc), radiotherapy (external photon and proton beams, brachytherapy), radiopharmaceutical therapy (¹³¹I for thyroid, ¹⁷⁷Lu-PSMA for prostate cancer), sterilization of medical equipment, and food irradiation.

## 10. Summary

| Concept | Formula |
|---|---|
| Nuclear radius | $R = 1.2\text{ fm}\times A^{1/3}$ |
| Binding energy | $B = (Zm_H + Nm_n - M)c^2$ |
| Mass–energy conversion | 1 u = 931.494 MeV/c² |
| Decay law | $N = N_0e^{-\lambda t}$ |
| Half-life | $t_{1/2} = \ln2/\lambda$ |
| Activity | $A = \lambda N$ (Bq) |
| Dating | $t = (t_{1/2}/\ln2)\ln(N_0/N)$ |
| Q-value | $Q = (m_i - m_f)c^2$ |
| Fission energy | ~200 MeV per ²³⁵U fission |
| D–T fusion | 17.6 MeV |
| pp chain | $4p\to{}^4\text{He}$ + 26.7 MeV |
| Peak binding | ~8.8 MeV/nucleon (Fe, Ni) |
