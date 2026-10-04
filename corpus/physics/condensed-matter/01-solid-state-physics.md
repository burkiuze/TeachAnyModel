---
title: Solid State Physics - Crystals, Band Theory, Semiconductors and Superconductivity
field: Physics
subfield: Condensed Matter Physics
level: undergraduate
keywords: [crystal lattice, unit cell, Bravais lattice, Miller indices, reciprocal lattice, phonons, Debye model, free electron model, Fermi energy, density of states, Bloch theorem, energy bands, band gap, metals, insulators, semiconductors, doping, p-n junction, diode, transistor, LED, solar cell, superconductivity, BCS theory, Meissner effect, topological insulators, graphene]
---

# Solid State Physics: Crystals, Band Theory, Semiconductors and Superconductivity

Condensed matter physics — the largest branch of physics by number of researchers — studies how the collective behavior of ~$10^{23}$ interacting atoms and electrons gives rise to the properties of solids and liquids: hardness, conductivity, magnetism, color, superconductivity. Its practical fruits include the transistor, the integrated circuit, lasers, LEDs, solar cells, hard disks and MRI magnets. As Philip Anderson put it, "More is different": new laws and concepts emerge at each level of complexity.

## 1. Crystal Structure

### Lattices and unit cells
A **crystal** is a periodic arrangement of atoms. It is described by a **lattice** (a periodic array of points) plus a **basis** (the group of atoms attached to each lattice point). The smallest repeating volume is the **primitive unit cell**; often a larger **conventional cell** displays the symmetry better.

In 3D there are exactly **14 Bravais lattices** in 7 crystal systems (cubic, tetragonal, orthorhombic, hexagonal, trigonal, monoclinic, triclinic). Combining lattices with point symmetries gives 230 space groups.

### Common structures

| Structure | Atoms per conventional cell | Coordination number | Packing fraction | Examples |
|---|---|---|---|---|
| Simple cubic (SC) | 1 | 6 | 52% | Polonium (rare) |
| Body-centered cubic (BCC) | 2 | 8 | 68% | Fe (α), Cr, W, Na, K |
| Face-centered cubic (FCC) | 4 | 12 | 74% | Cu, Al, Au, Ag, Ni, Pb |
| Hexagonal close-packed (HCP) | 2 (primitive) | 12 | 74% | Mg, Zn, Ti, Co |
| Diamond | 8 | 4 | 34% | C (diamond), Si, Ge |
| Rock salt (NaCl) | 4 + 4 | 6 | — | NaCl, MgO, KCl |
| Cesium chloride | 1 + 1 | 8 | — | CsCl |
| Zincblende | 4 + 4 | 4 | — | GaAs, ZnS, InP |
| Perovskite (ABX₃) | 5 | — | — | SrTiO₃, BaTiO₃, CH₃NH₃PbI₃ (solar cells) |

FCC and HCP are the two ways to stack spheres most densely (74%, Kepler's conjecture, proved by Hales in 1998/2017). Diamond-structure silicon is the foundation of electronics.

### Miller indices and X-ray diffraction
Crystal planes are labeled by **Miller indices** $(hkl)$: the reciprocals of the plane's intercepts with the axes (in units of lattice constants), cleared of fractions. For a cubic lattice with constant $a$, the spacing between $(hkl)$ planes is $d_{hkl} = \frac{a}{\sqrt{h^2 + k^2 + l^2}}$. Combined with **Bragg's law** $2d\sin\theta = n\lambda$, X-ray diffraction determines crystal structures.

### The reciprocal lattice
The **reciprocal lattice** consists of wavevectors $\vec G$ such that $e^{i\vec G\cdot\vec R} = 1$ for all lattice vectors $\vec R$. Diffraction occurs when the change in wavevector equals a reciprocal lattice vector (**Laue condition** $\Delta\vec k = \vec G$, equivalent to Bragg's law). The primitive cell of the reciprocal lattice centered at the origin is the **first Brillouin zone** — the natural domain for describing electron and phonon wavevectors.

### Defects
Real crystals contain **point defects** (vacancies, interstitials, substitutional impurities), **line defects** (dislocations — which make metals ductile, since slip occurs by dislocation motion at stresses far below the theoretical strength of a perfect crystal), **planar defects** (grain boundaries, stacking faults), and volume defects. Doping semiconductors is the deliberate introduction of substitutional impurities.

**Quasicrystals** (Dan Shechtman, 1982; Nobel Chemistry 2011) are ordered but not periodic, with "forbidden" fivefold symmetry.

## 2. Bonding in Solids

| Type | Mechanism | Properties | Examples |
|---|---|---|---|
| Ionic | Electrostatic attraction between ions | Hard, brittle, high melting point, insulating (conducts when molten) | NaCl, MgO |
| Covalent | Shared electron pairs, directional bonds | Very hard, high melting point, insulators/semiconductors | Diamond, Si, SiC |
| Metallic | Delocalized electron "sea" | Conductive, ductile, malleable, lustrous | Cu, Fe, Al |
| Molecular (van der Waals) | Weak dispersion/dipole forces between molecules | Soft, low melting point | Solid Ar, I₂, dry ice |
| Hydrogen-bonded | H bonded to N, O, F interacting with lone pairs | Intermediate | Ice |

## 3. Lattice Vibrations: Phonons

Atoms in a crystal vibrate about their equilibrium positions. For a 1D chain of atoms (mass $m$, spacing $a$, spring constant $K$), the normal modes have the **dispersion relation**
$$\omega(k) = 2\sqrt{\frac Km}\left|\sin\frac{ka}{2}\right|$$
- For small $k$ (long wavelength), $\omega \approx v_sk$: ordinary sound waves with speed $v_s = a\sqrt{K/m}$.
- At the Brillouin zone boundary ($k = \pi/a$), the group velocity is zero: standing waves.
- With two atoms per cell, an **optical branch** appears (atoms oscillate against each other; can couple to infrared light) in addition to the **acoustic branch**.

Quantized lattice vibrations are **phonons**, bosonic quasiparticles with energy $\hbar\omega$. They carry heat in insulators, scatter electrons (causing electrical resistance in metals), and mediate the attraction responsible for conventional superconductivity.

### Heat capacity of solids
- Classical **Dulong–Petit law**: $C = 3Nk_B$ (fails at low $T$).
- **Einstein model** (1907): all atoms vibrate at one frequency; explains the drop at low $T$ but predicts an exponential decrease, too fast.
- **Debye model** (1912): treats phonons as sound waves up to a cutoff frequency, characterized by the **Debye temperature** $\Theta_D$. At low temperature,
$$C \propto T^3 \qquad (T \ll \Theta_D)$$
in excellent agreement with experiment. Typical $\Theta_D$: lead 105 K, copper 343 K, silicon 645 K, diamond 2230 K (which is why diamond's heat capacity is low at room temperature).

## 4. The Free Electron Model of Metals

### Drude model (1900)
Treats conduction electrons as a classical gas colliding with ions, with mean free time $\tau$. It gives Ohm's law, $\sigma = ne^2\tau/m$, and the Wiedemann–Franz law qualitatively, but fails for heat capacity (predicts $\frac32Nk_B$ electronic contribution, which is not observed) and for the sign of the Hall coefficient in some metals.

### Sommerfeld (quantum free-electron) model (1928)
Electrons are free fermions in a box, obeying Fermi–Dirac statistics. At $T = 0$ they fill all states up to the **Fermi energy**:
$$E_F = \frac{\hbar^2}{2m}(3\pi^2n)^{2/3}$$

| Metal | Electron density $n$ (10²⁸ m⁻³) | $E_F$ (eV) | $T_F$ (10⁴ K) | $v_F$ (10⁶ m/s) |
|---|---|---|---|---|
| Na | 2.65 | 3.24 | 3.77 | 1.07 |
| Cu | 8.47 | 7.00 | 8.16 | 1.57 |
| Al | 18.1 | 11.7 | 13.6 | 2.03 |

- The **density of states** in 3D is $g(E) \propto\sqrt E$.
- Only electrons within ~$k_BT$ of $E_F$ can be excited, so the electronic heat capacity is $C_e = \frac{\pi^2}{2}Nk_B\frac{T}{T_F}$ — about 1% of the classical value at room temperature, resolving Drude's paradox. At very low temperatures, $C = \gamma T + \beta T^3$ (electrons + phonons).
- Electrons at the Fermi surface move at ~$10^6$ m/s even at absolute zero — a purely quantum effect of the Pauli principle.

## 5. Band Theory

The free-electron model cannot explain why some materials are insulators. The answer lies in the periodic potential of the ions.

### Bloch's theorem
In a periodic potential $V(\vec r + \vec R) = V(\vec r)$, energy eigenstates have the form (Felix Bloch, 1928)
$$\psi_{n\vec k}(\vec r) = e^{i\vec k\cdot\vec r}u_{n\vec k}(\vec r)$$
where $u$ has the periodicity of the lattice. Electrons are not scattered by a perfect periodic lattice; they propagate as waves. Resistance arises only from deviations from perfect periodicity (phonons, impurities, defects). This explains why pure metals at low temperature have very long mean free paths.

### Energy bands and gaps
Energy as a function of crystal momentum $\hbar\vec k$ forms **bands** $E_n(\vec k)$ separated by **band gaps** — energy ranges with no allowed states.

Two complementary pictures:
1. **Nearly-free electron model:** a weak periodic potential causes Bragg reflection of electron waves at Brillouin zone boundaries ($k = \pm\pi/a$), where standing waves concentrate electron density either on the ions (lower energy) or between them (higher energy). The splitting opens a gap $E_g = 2|V_G|$.
2. **Tight-binding model:** start from atomic orbitals. When $N$ atoms come together, each atomic level splits into $N$ closely spaced levels — a band — whose width depends on orbital overlap. Gaps remain between bands derived from different atomic levels.

Each band holds $2N$ electrons (two spin states for each of the $N$ allowed $\vec k$ values in the Brillouin zone).

### Metals, insulators, semiconductors

| Type | Band structure | Band gap | Conductivity (room T) |
|---|---|---|---|
| Metal | Partially filled band (or overlapping bands) | None | High, decreases with $T$ |
| Semimetal | Slight band overlap | ~0 (small overlap) | Moderate (Bi, graphite) |
| Semiconductor | Filled valence band, empty conduction band | Small (~0.1–3 eV) | Low, increases sharply with $T$ |
| Insulator | Filled valence band, empty conduction band | Large (> ~4 eV) | Very low |

A completely filled band carries no current — for every electron moving one way, another moves the opposite way. Conduction requires empty states nearby in energy.
- Sodium (one valence electron per atom) half-fills its band → metal.
- Magnesium (two valence electrons) would fill a band, but bands overlap → metal.
- Diamond (gap 5.5 eV) → insulator; silicon (1.12 eV) → semiconductor.

**Band gaps and color:** photons with energy less than the gap pass through. Diamond (5.5 eV) and quartz are transparent to visible light (1.65–3.3 eV); silicon (1.12 eV) absorbs visible light and looks gray-metallic; CdS (2.4 eV) absorbs blue/violet and appears yellow. Metals reflect visible light because free electrons respond to it (below the plasma frequency).

| Semiconductor | Band gap at 300 K (eV) | Type |
|---|---|---|
| Ge | 0.66 | Indirect |
| Si | 1.12 | Indirect |
| GaAs | 1.42 | Direct |
| CdTe | 1.44 | Direct |
| InP | 1.34 | Direct |
| GaN | 3.4 | Direct |
| SiC (4H) | 3.26 | Indirect |
| Diamond | 5.47 | Indirect |

**Direct vs. indirect gaps:** in a direct-gap material (GaAs, GaN) the conduction-band minimum and valence-band maximum occur at the same $\vec k$, so electrons and holes recombine efficiently by emitting photons — ideal for LEDs and lasers. In indirect-gap materials (Si, Ge), recombination also needs a phonon to supply momentum, making silicon a poor light emitter (but fine for solar cells and transistors).

### Effective mass and holes
Near a band extremum, $E \approx E_0 + \frac{\hbar^2k^2}{2m^*}$: electrons behave as free particles with an **effective mass** $m^* = \hbar^2/(d^2E/dk^2)$, which can be much smaller or larger than $m_e$ (GaAs conduction electrons: $0.067m_e$). A nearly full band is best described in terms of the missing electrons — **holes** — which behave as positive charge carriers with positive effective mass. The positive Hall coefficients of some metals and p-type semiconductors are explained by hole conduction.

## 6. Semiconductors

### Intrinsic semiconductors
In a pure semiconductor, thermal energy excites electrons across the gap, creating equal numbers of electrons ($n$) and holes ($p$):
$$n = p = n_i \propto T^{3/2}e^{-E_g/2k_BT}$$
For Si at 300 K, $n_i \approx 1.0\times10^{10}$ cm⁻³ (about one free electron per $5\times10^{12}$ atoms). The strong temperature dependence makes semiconductors useful as thermistors. **Mass-action law:** $np = n_i^2$ in equilibrium, even when doped.

### Doping
Adding tiny amounts of impurities dramatically changes conductivity:
- **n-type:** group-15 donors (P, As, Sb) in Si have one extra valence electron, loosely bound (~0.045 eV for P, like a hydrogen atom with screened charge and effective mass) and easily ionized at room temperature. Electrons are the majority carriers.
- **p-type:** group-13 acceptors (B, Al, Ga) have one fewer electron, creating holes as majority carriers.

A doping level of 1 part per million ($5\times10^{16}$ cm⁻³) increases silicon's conductivity by a factor of ~$10^6$. The **Fermi level** shifts toward the conduction band (n-type) or valence band (p-type).

### The p–n junction
Joining p- and n-type regions: electrons diffuse from n to p and holes from p to n, recombining near the interface and leaving behind fixed ionized dopants — the **depletion region** (~0.1–1 μm), with a built-in electric field and potential (~0.7 V for Si) that halts further diffusion.

**Diode behavior** (Shockley equation):
$$I = I_s\left(e^{eV/k_BT} - 1\right)$$
- **Forward bias** (p positive): lowers the barrier; current grows exponentially.
- **Reverse bias:** raises the barrier; only a tiny saturation current $I_s$ flows (until breakdown — Zener and avalanche diodes exploit this).

Diodes rectify AC to DC and protect circuits.

### Optoelectronic devices
- **Light-emitting diodes (LEDs):** in forward bias, electrons and holes recombine in a direct-gap material, emitting photons with energy ≈ $E_g$. Color is set by the gap: GaAs (infrared), GaAsP (red), InGaN (blue/green). Efficient **blue LEDs** (Akasaki, Amano, Nakamura; Nobel 2014) enabled white LED lighting (blue LED + yellow phosphor), now using roughly a tenth of the energy of incandescent bulbs for the same light.
- **Laser diodes:** add an optical cavity and population inversion — used in fiber optics, Blu-ray, barcode scanners and LIDAR.
- **Photodiodes and image sensors:** absorbed photons create electron–hole pairs that are separated by the junction field (CCD and CMOS camera sensors; Boyle and Smith, Nobel 2009 for the CCD).
- **Solar cells:** a large-area p–n junction under illumination. Photons with $E > E_g$ create carriers that the built-in field separates, producing voltage and current. The **Shockley–Queisser limit** for a single junction under unconcentrated sunlight is ~33.7% (optimal gap ~1.34 eV). Commercial silicon panels achieve 20–24%; multi-junction cells exceed 47% under concentration; perovskite–silicon tandems have surpassed 33% in the laboratory.

### Transistors
- **Bipolar junction transistor (BJT)** (npn or pnp): invented at Bell Labs — point-contact transistor by Bardeen and Brattain (December 1947), junction transistor by Shockley (1948); Nobel 1956. A small base current controls a large collector current.
- **MOSFET** (metal–oxide–semiconductor field-effect transistor): a gate voltage, insulated by a thin oxide, creates or removes a conducting channel between source and drain. MOSFETs are the building blocks of digital logic (CMOS) and memory. A modern processor contains tens of billions of transistors with feature sizes of a few nanometers; architectures have evolved from planar to FinFET to gate-all-around (nanosheet) transistors.
- **Integrated circuits** (Kilby, 1958; Noyce, 1959). **Moore's law** (1965): the number of transistors per chip doubles roughly every two years — held for decades, now slowing as dimensions approach atomic scales.

## 7. Superconductivity

### Phenomenology
Below a critical temperature $T_c$, certain materials exhibit:
1. **Zero DC electrical resistance** (Kamerlingh Onnes, mercury, 4.2 K, 1911). Persistent currents have flowed for years without measurable decay.
2. **Meissner effect** (1933): magnetic fields are **expelled** from the interior (perfect diamagnetism), which allows magnetic levitation. A superconductor is not merely a perfect conductor.
3. **Critical field and current:** superconductivity is destroyed above a critical magnetic field $B_c(T)$ and critical current density. **Type I** superconductors (most pure elements) have one critical field; **Type II** (alloys, compounds, cuprates) allow magnetic flux to penetrate in quantized **vortices** between $B_{c1}$ and $B_{c2}$, sustaining superconductivity in very high fields (Nb₃Sn: ~30 T).
4. **Flux quantization:** magnetic flux through a superconducting loop is quantized in units of $\Phi_0 = h/(2e) = 2.07\times10^{-15}$ Wb — the factor $2e$ reveals paired electrons.
5. An **energy gap** $\Delta$ in the excitation spectrum and an exponential drop in electronic heat capacity below $T_c$.

### BCS theory (1957)
John Bardeen, Leon Cooper and Robert Schrieffer (Nobel 1972) explained conventional superconductivity:
- An electron moving through the lattice attracts positive ions, creating a region of positive charge that attracts a second electron — a phonon-mediated attraction. (Evidence: the **isotope effect**, $T_c \propto M^{-1/2}$.)
- Any attraction, however weak, binds electrons near the Fermi surface into **Cooper pairs** (opposite momenta and spins), with sizes (coherence length) of ~100–1000 nm — much larger than the spacing between pairs, so pairs overlap enormously.
- Cooper pairs are bosons and condense into a single coherent macroscopic quantum state. Scattering a pair requires breaking it, costing at least $2\Delta$; at low temperatures there is not enough energy, so current flows without resistance.
- BCS predicts $2\Delta(0) \approx 3.53k_BT_c$, in good agreement with experiment for conventional superconductors.

### Josephson effects
Cooper pairs can tunnel through a thin insulating barrier between two superconductors (Brian Josephson, 1962; Nobel 1973). A DC current flows with zero voltage; an applied voltage $V$ produces an AC current at frequency $f = 2eV/h$ (483.6 GHz per mV) — now used to define the volt. **SQUIDs** (superconducting quantum interference devices) built from Josephson junctions detect magnetic fields as small as ~$10^{-15}$ T (brain activity in magnetoencephalography). Josephson junctions are also the nonlinear element of superconducting **qubits** (Clarke, Devoret, Martinis; Nobel 2025, for macroscopic quantum tunneling and energy quantization in electrical circuits).

### Materials and records

| Material | $T_c$ (K) | Year | Notes |
|---|---|---|---|
| Hg | 4.15 | 1911 | First superconductor |
| Pb | 7.2 | 1913 | |
| Nb | 9.3 | 1930 | Highest elemental $T_c$ at ambient pressure |
| NbTi | ~10 | 1962 | MRI and LHC magnets |
| Nb₃Sn | 18.3 | 1954 | High-field magnets (ITER) |
| MgB₂ | 39 | 2001 | Conventional, surprisingly high |
| La₂₋ₓBaₓCuO₄ | ~35 | 1986 | Bednorz and Müller, first cuprate (Nobel 1987) |
| YBa₂Cu₃O₇ (YBCO) | 92 | 1987 | First above 77 K (liquid nitrogen) |
| HgBa₂Ca₂Cu₃O₈ | 133 (164 under pressure) | 1993 | Ambient-pressure record |
| Iron pnictides (e.g. SmFeAsO₁₋ₓFₓ) | up to ~55 | 2008 | Second high-$T_c$ family |
| H₃S | 203 | 2015 | At ~150 GPa |
| LaH₁₀ | ~250 | 2019 | At ~170 GPa |

**High-temperature (cuprate) superconductivity** is not explained by conventional BCS phonon pairing; its mechanism (likely related to antiferromagnetic spin fluctuations, with d-wave pairing symmetry) remains one of the great open problems of physics. Claims of room-temperature superconductivity at ambient pressure (e.g. "LK-99", 2023) have not been substantiated.

**Applications:** MRI scanners (the largest commercial use), particle accelerator magnets, NMR spectrometers, maglev trains (e.g. Japan's SCMaglev, 603 km/h record), fusion reactor magnets (high-temperature REBCO tape magnets enabling compact tokamaks), SQUIDs, superconducting qubits, power cables and fault-current limiters.

## 8. Magnetism in Solids (Brief)

- **Diamagnetism** (all materials), **paramagnetism** (unpaired spins, Curie law $\chi = C/T$), **Pauli paramagnetism** of conduction electrons (temperature-independent).
- **Ferromagnetism** arises from the exchange interaction (Heisenberg model $H = -J\sum\vec S_i\cdot\vec S_j$, $J > 0$); spontaneous magnetization vanishes at the Curie temperature. **Antiferromagnetism** ($J < 0$, Néel temperature) and **ferrimagnetism** also occur.
- **Spintronics:** giant magnetoresistance (Fert, Grünberg; Nobel 2007) and tunnel magnetoresistance enabled high-density hard drives and MRAM.

## 9. Frontiers of Condensed Matter

- **Graphene:** a single layer of carbon atoms in a honeycomb lattice, isolated with sticky tape in 2004 (Geim and Novoselov, Nobel 2010). Its electrons behave like massless Dirac fermions with a linear dispersion $E = \pm\hbar v_F|k|$ ($v_F \approx 10^6$ m/s). Exceptional strength, conductivity and thermal conductivity. Stacking two layers at a "magic angle" of ~1.1° (twisted bilayer graphene, 2018) produces flat bands with superconductivity and correlated insulating states.
- **Other 2D materials:** hexagonal boron nitride, transition-metal dichalcogenides (MoS₂, WSe₂), enabling van der Waals heterostructures.
- **Topological phases:** the integer quantum Hall effect (von Klitzing, 1980) has Hall conductance quantized as $\sigma_{xy} = \nu e^2/h$ with integer $\nu$, precise to parts per billion, because it is protected by topology (Thouless, Haldane, Kosterlitz; Nobel 2016). The fractional quantum Hall effect (Tsui, Störmer, Laughlin; Nobel 1998) features quasiparticles with fractional charge such as $e/3$. **Topological insulators** (predicted 2005–2006, observed 2007–2008) are insulating inside but have protected conducting surface states with spin–momentum locking. Topological ideas are pursued for fault-tolerant quantum computing (Majorana zero modes, non-Abelian anyons).
- **Strongly correlated electrons:** Mott insulators (insulating because of electron–electron repulsion despite partially filled bands), heavy-fermion compounds, quantum spin liquids, quantum criticality.
- **Phase transitions and emergence:** spontaneous symmetry breaking (crystals break translational symmetry, magnets break rotational symmetry, superconductors break gauge symmetry), Goldstone modes (phonons, magnons), and Landau's theory of phase transitions; the Anderson–Higgs mechanism in superconductors anticipated the Higgs mechanism in particle physics.
- **Soft condensed matter:** liquid crystals (displays), polymers, colloids, gels, granular materials, active matter (de Gennes, Nobel 1991).

## 10. Summary

| Concept | Formula / Value |
|---|---|
| Plane spacing (cubic) | $d_{hkl} = a/\sqrt{h^2+k^2+l^2}$ |
| Bragg's law | $2d\sin\theta = n\lambda$ |
| 1D phonon dispersion | $\omega = 2\sqrt{K/m}\lvert\sin(ka/2)\rvert$ |
| Debye low-$T$ heat capacity | $C \propto T^3$ |
| Fermi energy | $E_F = \frac{\hbar^2}{2m}(3\pi^2n)^{2/3}$ |
| Bloch theorem | $\psi = e^{i\vec k\cdot\vec r}u(\vec r)$ |
| Intrinsic carriers | $n_i \propto T^{3/2}e^{-E_g/2k_BT}$ |
| Mass-action law | $np = n_i^2$ |
| Diode equation | $I = I_s(e^{eV/k_BT} - 1)$ |
| Flux quantum | $\Phi_0 = h/2e = 2.07\times10^{-15}$ Wb |
| BCS gap | $2\Delta \approx 3.53k_BT_c$ |
| Josephson frequency | $f = 2eV/h$ |
| Quantum Hall conductance | $\sigma_{xy} = \nu e^2/h$ |
