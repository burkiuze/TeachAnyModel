---
title: Kinetic Theory of Gases and Statistical Mechanics
field: Physics
subfield: Thermodynamics and Statistical Mechanics
level: undergraduate
keywords: [kinetic theory, ideal gas, pressure from molecular collisions, rms speed, Maxwell-Boltzmann distribution, equipartition theorem, mean free path, Boltzmann factor, partition function, microcanonical ensemble, canonical ensemble, grand canonical ensemble, Fermi-Dirac, Bose-Einstein, Bose-Einstein condensate, van der Waals equation]
---

# Kinetic Theory of Gases and Statistical Mechanics

Thermodynamics describes matter through a few macroscopic variables ($P$, $V$, $T$, $S$) without reference to atoms. **Statistical mechanics** explains these laws from the microscopic behavior of enormous numbers of particles, using probability. Its success — deriving the gas laws, heat capacities, the second law, phase transitions and much more — was among the strongest early evidence that atoms are real. Einstein's 1905 analysis of Brownian motion, confirmed experimentally by Jean Perrin (1908), finally convinced skeptics.

## 1. Kinetic Theory of the Ideal Gas

### Assumptions
1. A gas consists of a very large number of identical molecules in random motion.
2. The molecules' own volume is negligible compared with the container volume.
3. Molecules interact only through brief, elastic collisions (with each other and the walls); no forces between collisions.
4. Newton's laws apply to each molecule.

### Pressure from molecular collisions
A molecule of mass $m$ with velocity component $v_x$ hits a wall perpendicular to $x$ and rebounds elastically, transferring momentum $2mv_x$. It returns to the same wall after time $2L/v_x$ (in a cube of side $L$). The average force from this molecule is $\frac{2mv_x}{2L/v_x} = \frac{mv_x^2}{L}$. Summing over $N$ molecules and dividing by the wall area $L^2$:
$$P = \frac{Nm\langle v_x^2\rangle}{V}$$
By isotropy, $\langle v_x^2\rangle = \langle v_y^2\rangle = \langle v_z^2\rangle = \frac13\langle v^2\rangle$, so
$$\boxed{PV = \tfrac13Nm\langle v^2\rangle = \tfrac23N\langle K_{\text{tr}}\rangle}$$

Comparing with the ideal gas law $PV = Nk_BT$ gives the microscopic meaning of temperature:
$$\boxed{\langle K_{\text{tr}}\rangle = \tfrac12m\langle v^2\rangle = \tfrac32k_BT}$$
**Temperature is proportional to the average translational kinetic energy of the molecules**, independent of their mass. At room temperature (300 K), $\langle K_{\text{tr}}\rangle \approx 6.2\times10^{-21}$ J ≈ 0.039 eV. A useful rule: $k_BT \approx \frac{1}{40}$ eV at room temperature.

### Molecular speeds
$$v_{\text{rms}} = \sqrt{\langle v^2\rangle} = \sqrt{\frac{3k_BT}{m}} = \sqrt{\frac{3RT}{M}}$$
where $M$ is the molar mass in kg/mol.

| Gas | $M$ (g/mol) | $v_{\text{rms}}$ at 300 K (m/s) |
|---|---|---|
| H₂ | 2.016 | 1930 |
| He | 4.003 | 1370 |
| H₂O | 18.0 | 645 |
| N₂ | 28.0 | 517 |
| O₂ | 32.0 | 484 |
| CO₂ | 44.0 | 412 |
| UF₆ | 352 | 146 |

Lighter molecules move faster at the same temperature. This underlies **Graham's law** of effusion (rate $\propto 1/\sqrt M$) and was used in the Manhattan Project to enrich uranium by gaseous diffusion of $^{235}$UF₆ vs. $^{238}$UF₆ (a speed difference of only 0.43% per stage, requiring thousands of stages). Modern enrichment uses gas centrifuges.

The speed of sound in a gas, $v_s = \sqrt{\gamma RT/M}$, is comparable to but less than $v_{\text{rms}}$ (343 m/s in air at 20 °C).

## 2. The Maxwell–Boltzmann Speed Distribution

Molecules do not all have the same speed. James Clerk Maxwell (1860) derived the distribution of speeds in an ideal gas at temperature $T$:
$$\boxed{f(v) = 4\pi\left(\frac{m}{2\pi k_BT}\right)^{3/2}v^2\,e^{-mv^2/(2k_BT)}}$$
$f(v)\,dv$ is the fraction of molecules with speeds between $v$ and $v + dv$; $\int_0^\infty f(v)\,dv = 1$.

The $v^2$ factor comes from the volume of a spherical shell in velocity space ($4\pi v^2\,dv$); the exponential is the Boltzmann factor for kinetic energy. The distribution is skewed with a long high-speed tail.

Three characteristic speeds:
$$v_p = \sqrt{\frac{2k_BT}{m}} \;<\; \langle v\rangle = \sqrt{\frac{8k_BT}{\pi m}} \;<\; v_{\text{rms}} = \sqrt{\frac{3k_BT}{m}}$$
in ratios $1 : 1.128 : 1.225$.

**Consequences of the high-speed tail:**
- **Evaporation:** the fastest molecules escape a liquid's surface, lowering the average energy of those remaining — evaporative cooling.
- **Chemical reaction rates:** only molecules with energy above an activation energy $E_a$ react. The fraction above $E_a$ scales roughly as $e^{-E_a/k_BT}$, explaining the strong temperature dependence of reaction rates (Arrhenius equation). A rule of thumb: many reactions roughly double in rate for each 10 °C rise near room temperature.
- **Atmospheric escape:** light gases (H₂, He) in the tail exceed escape velocity over geological time.
- **Nuclear fusion in the Sun:** protons in the tail (combined with quantum tunneling) can overcome the Coulomb barrier even though the average thermal energy (~1.3 keV at 15 million K) is far below the barrier height (~1 MeV).

## 3. The Equipartition Theorem

In thermal equilibrium at temperature $T$, **each quadratic term** in the energy (each "degree of freedom") has an average energy of $\frac12k_BT$.

| System | Quadratic terms per molecule | Average energy | Molar $C_V$ |
|---|---|---|---|
| Monatomic gas | 3 (translation) | $\frac32k_BT$ | $\frac32R \approx 12.5$ J/(mol·K) |
| Diatomic gas (rigid rotor) | 3 trans + 2 rot | $\frac52k_BT$ | $\frac52R \approx 20.8$ |
| Diatomic gas (with vibration) | 3 + 2 + 2 (vib KE + PE) | $\frac72k_BT$ | $\frac72R \approx 29.1$ |
| Solid (atoms on springs, 3D) | 3 KE + 3 PE | $3k_BT$ | $3R \approx 24.9$ (Dulong–Petit) |

**Failure of classical equipartition** was one of the great puzzles of late-19th-century physics. Measured heat capacities of diatomic gases are $\frac52R$ at room temperature — vibration contributes nothing — and drop to $\frac32R$ for hydrogen at low temperatures (rotation freezes out). Solids' heat capacities fall to zero at low $T$. Explanation: **energy is quantized**. A mode with level spacing $\Delta E \gg k_BT$ cannot be excited and contributes nothing. Vibrational quanta of N₂ correspond to about 3400 K, so vibration is frozen at room temperature. Classical equipartition applied to electromagnetic radiation in a cavity also predicted infinite energy (the "ultraviolet catastrophe"), which Planck resolved in 1900, launching quantum theory.

## 4. Mean Free Path and Transport

A molecule of diameter $d$ sweeps a collision cross-section $\sigma = \pi d^2$. The average distance between collisions — the **mean free path** — is
$$\lambda = \frac{1}{\sqrt2\,n\sigma} = \frac{k_BT}{\sqrt2\,\pi d^2P}$$
where $n = N/V$ is the number density. The $\sqrt2$ accounts for the relative motion of the other molecules.

For air at STP: $n \approx 2.7\times10^{25}$ m⁻³ (Loschmidt's number), $d \approx 3.7\times10^{-10}$ m, $\lambda \approx 60$–$70$ nm — roughly 200 molecular diameters. Each molecule undergoes several billion ($\sim7\times10^9$) collisions per second. In high vacuum ($10^{-7}$ Pa), $\lambda$ is tens of kilometers.

Kinetic theory explains transport properties:
- **Diffusion** (transport of particles): Fick's law, $J = -D\frac{dn}{dx}$, with $D \sim \frac13\lambda\langle v\rangle$. Random-walk displacement grows as $\sqrt t$: $\langle x^2\rangle = 2Dt$ in 1D. This is why diffusion is fast over micrometers (cells) but hopelessly slow over meters — perfume spreads across a room mainly by convection, not diffusion.
- **Viscosity** (transport of momentum): $\eta \sim \frac13nm\langle v\rangle\lambda$ — remarkably independent of pressure (Maxwell's surprising prediction, confirmed experimentally) and increasing as $\sqrt T$.
- **Thermal conductivity** (transport of energy): $\kappa \sim \frac13nc_v\langle v\rangle\lambda$.

**Brownian motion:** pollen grains or colloidal particles jiggle because of unbalanced molecular collisions. Einstein's relation $D = \frac{k_BT}{6\pi\eta r}$ (Stokes–Einstein) let Perrin measure $k_B$ and hence Avogadro's number from microscope observations.

## 5. Real Gases: The van der Waals Equation

Real gases deviate from ideal behavior at high pressure and low temperature because molecules have finite size and attract each other. Johannes van der Waals (1873, Nobel 1910) proposed:
$$\boxed{\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT}$$
- $b$: excluded volume per mole (finite molecular size)
- $a$: strength of intermolecular attraction (reduces pressure on the walls)

| Gas | $a$ (L²·bar/mol²) | $b$ (L/mol) |
|---|---|---|
| He | 0.0346 | 0.0238 |
| H₂ | 0.2476 | 0.0266 |
| N₂ | 1.370 | 0.0387 |
| CO₂ | 3.640 | 0.04267 |
| H₂O | 5.536 | 0.03049 |

The van der Waals equation predicts a **liquid–gas phase transition** and a **critical point** at $T_c = \frac{8a}{27Rb}$, $P_c = \frac{a}{27b^2}$, $V_c = 3nb$. Below $T_c$ its isotherms have an unphysical wiggle, replaced by a horizontal line (Maxwell equal-area construction) representing liquid–vapor coexistence. In reduced variables ($P/P_c$, $V/V_c$, $T/T_c$), all van der Waals gases obey the same equation — the **law of corresponding states**.

The **compressibility factor** $Z = PV/(nRT)$ equals 1 for an ideal gas; real gases show $Z < 1$ at moderate pressure (attraction dominates) and $Z > 1$ at high pressure (repulsion/size dominates).

## 6. Foundations of Statistical Mechanics

### Microstates, macrostates and the fundamental postulate
A **macrostate** is specified by macroscopic variables ($E$, $V$, $N$). A **microstate** is a complete specification of every particle's state. 

**Fundamental postulate (equal a priori probabilities):** an isolated system in equilibrium is equally likely to be in any of its accessible microstates.

From this, entropy is $S = k_B\ln\Omega(E, V, N)$, and temperature, pressure and chemical potential follow:
$$\frac1T = \frac{\partial S}{\partial E}, \qquad \frac PT = \frac{\partial S}{\partial V}, \qquad -\frac\mu T = \frac{\partial S}{\partial N}$$

**Example – Einstein solid:** $N$ oscillators sharing $q$ energy quanta have $\Omega = \binom{q + N - 1}{q}$ microstates. When two such solids exchange energy, the combined multiplicity is sharply peaked at the division where $\frac{\partial\ln\Omega_A}{\partial q_A} = \frac{\partial\ln\Omega_B}{\partial q_B}$ — equal temperatures. For macroscopic $N$ the peak is so sharp that deviations are never observed: this is the statistical origin of thermal equilibrium and the second law.

### Ensembles

| Ensemble | Fixed | Exchanges with reservoir | Key function |
|---|---|---|---|
| Microcanonical | $E, V, N$ | Nothing (isolated) | $S = k_B\ln\Omega$ |
| Canonical | $T, V, N$ | Energy | $F = -k_BT\ln Z$ |
| Grand canonical | $T, V, \mu$ | Energy and particles | $\Phi = -k_BT\ln\mathcal Z$ |

For macroscopic systems all ensembles give the same thermodynamics; one chooses whichever is most convenient.

## 7. The Boltzmann Distribution and the Partition Function

For a system in thermal contact with a large reservoir at temperature $T$, the probability of finding it in a particular microstate $i$ with energy $E_i$ is
$$\boxed{p_i = \frac{e^{-E_i/k_BT}}{Z}}, \qquad \boxed{Z = \sum_i e^{-E_i/k_BT}}$$
$e^{-E/k_BT}$ is the **Boltzmann factor** and $Z$ is the **partition function** (German *Zustandssumme*, "sum over states").

**Derivation sketch:** the probability of the system being in state $i$ is proportional to the number of reservoir microstates compatible with it: $p_i \propto \Omega_R(E_{\text{tot}} - E_i) = e^{S_R(E_{\text{tot}} - E_i)/k_B}$. Expanding $S_R$ to first order, $S_R(E_{\text{tot}} - E_i) \approx S_R(E_{\text{tot}}) - E_i/T$, giving $p_i \propto e^{-E_i/k_BT}$.

**Everything follows from $Z$.** With $\beta = 1/(k_BT)$:
- Average energy: $\langle E\rangle = -\frac{\partial\ln Z}{\partial\beta}$
- Helmholtz free energy: $F = -k_BT\ln Z$
- Entropy: $S = -\frac{\partial F}{\partial T}$
- Pressure: $P = -\frac{\partial F}{\partial V}$
- Heat capacity: $C_V = \frac{\partial\langle E\rangle}{\partial T}$, and energy fluctuations $\langle(\Delta E)^2\rangle = k_BT^2C_V$

### Applications of the Boltzmann factor
- **Barometric formula:** molecules at height $h$ have extra energy $mgh$, so $n(h) = n_0e^{-mgh/k_BT}$.
- **Two-level systems:** for levels separated by $\Delta E$, the population ratio is $\frac{N_2}{N_1} = \frac{g_2}{g_1}e^{-\Delta E/k_BT}$. Lasers require **population inversion** ($N_2 > N_1$), which cannot occur in thermal equilibrium at positive temperature.
- **Paramagnetism:** spins in a magnetic field $B$ have energies $\mp\mu B$; magnetization $M = N\mu\tanh(\mu B/k_BT)$, giving Curie's law $M \propto B/T$ at high temperature.
- **Arrhenius equation:** rate $k = Ae^{-E_a/RT}$.
- **Semiconductor carrier density** scales as $e^{-E_g/2k_BT}$.
- **Nernst equation and membrane potentials** in biology.

### Example – Quantum harmonic oscillator
Levels $E_n = \hbar\omega(n + \frac12)$:
$$Z = \sum_{n=0}^\infty e^{-\beta\hbar\omega(n+1/2)} = \frac{e^{-\beta\hbar\omega/2}}{1 - e^{-\beta\hbar\omega}}$$
$$\langle E\rangle = \frac{\hbar\omega}{2} + \frac{\hbar\omega}{e^{\hbar\omega/k_BT} - 1}$$
- High $T$ ($k_BT \gg \hbar\omega$): $\langle E\rangle \to k_BT$ — classical equipartition.
- Low $T$: $\langle E\rangle \to \frac12\hbar\omega$ — the mode freezes out. This is Einstein's 1907 model of solid heat capacities.

### Ideal monatomic gas partition function
For one particle in volume $V$: $Z_1 = \frac{V}{\lambda_T^3}$, where the **thermal de Broglie wavelength** is
$$\lambda_T = \frac{h}{\sqrt{2\pi mk_BT}}$$
For $N$ indistinguishable particles, $Z = \frac{Z_1^N}{N!}$ (the $N!$ resolves the **Gibbs paradox** of mixing identical gases). This yields $PV = Nk_BT$, $U = \frac32Nk_BT$, and the **Sackur–Tetrode equation** for absolute entropy:
$$S = Nk_B\left[\ln\left(\frac{V}{N\lambda_T^3}\right) + \frac52\right]$$
which contains Planck's constant — a hint that even classical gas entropy is fundamentally quantum.

Classical (Maxwell–Boltzmann) statistics is valid when the interparticle spacing is much larger than $\lambda_T$, i.e. $n\lambda_T^3 \ll 1$. For air at room temperature, $n\lambda_T^3 \sim 10^{-7}$.

## 8. Quantum Statistics

When $n\lambda_T^3 \gtrsim 1$ (low temperature, high density, light particles), quantum effects dominate. Identical quantum particles are indistinguishable, and the **spin–statistics theorem** divides them into two classes:

| | Fermions | Bosons |
|---|---|---|
| Spin | Half-integer (1/2, 3/2, ...) | Integer (0, 1, 2, ...) |
| Examples | Electrons, protons, neutrons, quarks, ³He atoms | Photons, gluons, W/Z, Higgs, ⁴He atoms, phonons |
| Wavefunction under exchange | Antisymmetric | Symmetric |
| Occupancy of a state | 0 or 1 (Pauli exclusion) | Any number |
| Distribution | Fermi–Dirac | Bose–Einstein |

Average occupation of a single-particle state of energy $\varepsilon$:
$$\text{Fermi–Dirac: } \bar n = \frac{1}{e^{(\varepsilon - \mu)/k_BT} + 1}, \qquad \text{Bose–Einstein: } \bar n = \frac{1}{e^{(\varepsilon - \mu)/k_BT} - 1}$$
Both reduce to the Maxwell–Boltzmann form $\bar n \approx e^{-(\varepsilon - \mu)/k_BT}$ when $\bar n \ll 1$.

### Fermi gases
At $T = 0$ fermions fill all states up to the **Fermi energy** $E_F$ — one particle per state, because of the exclusion principle. For electrons in metals $E_F$ is a few eV (copper: 7.0 eV), corresponding to a Fermi temperature $T_F = E_F/k_B \sim 10^4$–$10^5$ K. Since room temperature is far below $T_F$, only electrons within ~$k_BT$ of $E_F$ can be thermally excited — explaining why conduction electrons contribute so little to metals' heat capacity (a major puzzle for classical theory).

**Degeneracy pressure** from the exclusion principle supports **white dwarfs** (electron degeneracy) and **neutron stars** (neutron degeneracy) against gravitational collapse. Chandrasekhar showed that white dwarfs cannot exceed about 1.4 solar masses (the Chandrasekhar limit, Nobel 1983).

### Bose gases and Bose–Einstein condensation
Bosons with $\mu = 0$ and no conservation of number — photons — give **Planck's blackbody radiation law**:
$$u(\nu, T) = \frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT} - 1}$$
which, integrated over frequency, gives the Stefan–Boltzmann law. Phonons similarly give the **Debye $T^3$ law** for heat capacity of solids at low temperature.

For conserved massive bosons, below a critical temperature
$$T_c = \frac{2\pi\hbar^2}{mk_B}\left(\frac{n}{2.612}\right)^{2/3}$$
a macroscopic fraction of particles occupies the single lowest-energy state: a **Bose–Einstein condensate** (BEC), predicted by Bose and Einstein in 1924–25. First produced in dilute rubidium and sodium gases in 1995 at ~100 nK (Cornell, Wieman, Ketterle; Nobel 2001). Related phenomena include **superfluidity** of liquid helium-4 below 2.17 K (the lambda point) — flowing without viscosity and creeping up container walls — and, via electron pairing (Cooper pairs), **superconductivity**.

## 9. Phase Transitions (Brief Overview)

Statistical mechanics explains how collective behavior emerges from simple interactions:
- **First-order transitions** (melting, boiling): latent heat, discontinuous density or entropy.
- **Continuous (second-order) transitions** (ferromagnet at the Curie point, liquid–gas at the critical point, superconductivity): no latent heat, but diverging susceptibilities and correlation lengths, and **critical exponents** that are *universal* — the same for systems as different as magnets and fluids.
- The **Ising model** (spins $\pm1$ on a lattice with nearest-neighbor coupling) is the prototype. Onsager's exact 2D solution (1944) showed a genuine phase transition; Wilson's renormalization group (Nobel 1982) explained universality.

## 10. Summary

| Result | Formula |
|---|---|
| Kinetic pressure | $PV = \frac13Nm\langle v^2\rangle$ |
| Temperature | $\frac12m\langle v^2\rangle = \frac32k_BT$ |
| rms speed | $v_{\text{rms}} = \sqrt{3RT/M}$ |
| Maxwell–Boltzmann | $f(v) \propto v^2e^{-mv^2/2k_BT}$ |
| Equipartition | $\frac12k_BT$ per quadratic degree of freedom |
| Mean free path | $\lambda = 1/(\sqrt2n\pi d^2)$ |
| van der Waals | $(P + an^2/V^2)(V - nb) = nRT$ |
| Boltzmann entropy | $S = k_B\ln\Omega$ |
| Boltzmann distribution | $p_i = e^{-E_i/k_BT}/Z$ |
| Free energy | $F = -k_BT\ln Z$ |
| Fermi–Dirac | $\bar n = 1/(e^{(\varepsilon-\mu)/k_BT} + 1)$ |
| Bose–Einstein | $\bar n = 1/(e^{(\varepsilon-\mu)/k_BT} - 1)$ |
| Planck's law | $u(\nu) = \frac{8\pi h\nu^3}{c^3}\frac{1}{e^{h\nu/k_BT}-1}$ |
