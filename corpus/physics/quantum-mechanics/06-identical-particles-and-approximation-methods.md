---
title: Identical Particles and Approximation Methods in Quantum Mechanics
field: Physics
subfield: Quantum Mechanics
level: undergraduate to graduate
keywords: [identical particles, bosons, fermions, exchange symmetry, Pauli exclusion principle, Slater determinant, exchange interaction, helium atom, time-independent perturbation theory, degenerate perturbation theory, variational principle, WKB approximation, time-dependent perturbation theory, Fermi's golden rule, transition rates, Einstein coefficients, Born-Oppenheimer approximation, Hartree-Fock, density functional theory]
---

# Identical Particles and Approximation Methods in Quantum Mechanics

Only a handful of quantum problems — the box, the harmonic oscillator, hydrogen — can be solved exactly. Real atoms, molecules and solids require approximation methods. And as soon as there is more than one particle, a purely quantum phenomenon appears: **identical particles are fundamentally indistinguishable**, which leads to the Pauli exclusion principle, the structure of the periodic table, the stability of matter, chemical bonding, lasers and superconductivity.

## Part I — Identical Particles

### 1. Indistinguishability
Classically, two identical billiard balls can be tracked and labeled. Quantum mechanically, particles have no definite trajectories, and two electrons are **truly indistinguishable**: no measurement can tell which is "electron 1". Therefore physical predictions must be unchanged by swapping labels:
$$|\psi(x_1, x_2)|^2 = |\psi(x_2, x_1)|^2 \Rightarrow \psi(x_2, x_1) = \pm\psi(x_1, x_2)$$
(in 3D; in 2D, exotic "anyons" with other phases are possible and are studied for topological quantum computing).

### 2. Bosons and fermions
- **Bosons** — symmetric wavefunctions, $\psi(x_2, x_1) = +\psi(x_1, x_2)$. Integer spin. Examples: photons, gluons, W and Z bosons, Higgs boson, pions, ⁴He atoms, deuterons.
- **Fermions** — antisymmetric wavefunctions, $\psi(x_2, x_1) = -\psi(x_1, x_2)$. Half-integer spin. Examples: electrons, quarks, neutrinos, protons, neutrons, ³He atoms.

The **spin–statistics theorem** (Pauli, 1940), derived from relativistic quantum field theory, links spin to symmetry. Composite particles are bosons if they contain an even number of fermions, fermions if odd.

### 3. Constructing symmetric and antisymmetric states
For two non-interacting particles in single-particle states $\psi_a$ and $\psi_b$:
$$\psi_\pm(x_1, x_2) = \frac{1}{\sqrt2}\left[\psi_a(x_1)\psi_b(x_2) \pm \psi_b(x_1)\psi_a(x_2)\right]$$

For $N$ fermions, the antisymmetric state is a **Slater determinant**:
$$\Psi = \frac{1}{\sqrt{N!}}\begin{vmatrix}\psi_1(x_1) & \psi_2(x_1) & \cdots & \psi_N(x_1)\\ \psi_1(x_2) & \psi_2(x_2) & \cdots & \psi_N(x_2)\\ \vdots & & \ddots & \vdots\\ \psi_1(x_N) & \psi_2(x_N) & \cdots & \psi_N(x_N)\end{vmatrix}$$
(each $x_i$ includes spin). Swapping two particles swaps two rows, changing the sign.

### 4. The Pauli exclusion principle
If two fermions are put in the same single-particle state ($a = b$), the antisymmetric combination vanishes identically:
$$\psi_-(x_1, x_2) = \frac{1}{\sqrt2}[\psi_a(x_1)\psi_a(x_2) - \psi_a(x_1)\psi_a(x_2)] = 0$$
**No two identical fermions can occupy the same quantum state.** (A determinant with two equal columns is zero.) Pauli formulated the principle empirically in 1925 to explain atomic spectra and the periodic table (Nobel 1945).

**Consequences:**
- **Atomic shell structure** and the periodic table: electrons fill successive orbitals rather than all collapsing into 1s.
- **Stability and volume of matter:** Freeman Dyson and Andrew Lenard (1967) proved that without the exclusion principle, bulk matter would collapse. The incompressibility of solids traces back to Pauli.
- **Degeneracy pressure** supports white dwarfs and neutron stars.
- **Metals and semiconductors:** electrons fill bands up to the Fermi energy.
- **Nuclear shell structure** (magic numbers 2, 8, 20, 28, 50, 82, 126).

Bosons, by contrast, *prefer* to share states: the amplitude to add a boson to a state already containing $n$ bosons is enhanced by $\sqrt{n+1}$. This underlies **stimulated emission (lasers)**, **Bose–Einstein condensation**, superfluidity and superconductivity.

### 5. Exchange effects ("exchange force")
Symmetrization changes the average separation of particles even without any interaction:
$$\langle(x_1 - x_2)^2\rangle_\pm = \langle(x_1 - x_2)^2\rangle_{\text{dist}} \mp 2|\langle x\rangle_{ab}|^2$$
- Bosons (symmetric spatial state) are on average **closer** together.
- Fermions (antisymmetric spatial state) are on average **farther apart** — the "Fermi hole".

This is not a force in the usual sense; it is a statistical/geometric consequence of symmetry. For electrons, the total wavefunction (space × spin) must be antisymmetric. A spin **triplet** (symmetric spin) requires an antisymmetric spatial part, keeping electrons apart and lowering their Coulomb repulsion; a spin **singlet** allows a symmetric spatial part, with electrons closer together.
- **Hund's first rule** (maximize total spin) arises because parallel spins keep electrons apart, reducing repulsion.
- **Covalent bonding:** in H₂, the two electrons in a spin singlet occupy a symmetric spatial orbital concentrated between the nuclei, binding the molecule (Heitler and London, 1927).
- **Ferromagnetism:** the exchange interaction favors aligned spins in iron, cobalt and nickel (Heisenberg, 1928).

### 6. The helium atom
Helium (two electrons, $Z = 2$) cannot be solved exactly because of the electron–electron repulsion term. Its states split into:
- **Parahelium:** spin singlet, symmetric spatial wavefunction. Includes the ground state 1s².
- **Orthohelium:** spin triplet, antisymmetric spatial wavefunction. Lower energy than the corresponding parahelium state (electrons farther apart). The ground state cannot be ortho (both electrons in 1s would require a symmetric spatial state).

Since dipole transitions rarely flip spin, the two families behave almost like separate elements spectroscopically; in the 1920s they were thought to be two kinds of helium. Experimental ground-state energy: −79.0 eV (ionization energy of the first electron: 24.6 eV; of the second: 54.4 eV).

## Part II — Approximation Methods

### 7. Time-independent perturbation theory (non-degenerate)
Suppose $\hat H = \hat H^0 + \lambda\hat H'$, where $\hat H^0$ has known eigenstates $|n^0\rangle$ with energies $E_n^0$, and $\hat H'$ is a small perturbation. Expanding in powers of $\lambda$:

**First-order energy correction:**
$$\boxed{E_n^{(1)} = \langle n^0|\hat H'|n^0\rangle}$$
— the expectation value of the perturbation in the unperturbed state.

**First-order state correction:**
$$|n^{(1)}\rangle = \sum_{m\ne n}\frac{\langle m^0|\hat H'|n^0\rangle}{E_n^0 - E_m^0}|m^0\rangle$$

**Second-order energy correction:**
$$\boxed{E_n^{(2)} = \sum_{m\ne n}\frac{|\langle m^0|\hat H'|n^0\rangle|^2}{E_n^0 - E_m^0}}$$
Note: the second-order correction to the **ground state** is always negative (all denominators are negative). Levels "repel" each other.

Validity requires $|\langle m^0|\hat H'|n^0\rangle| \ll |E_n^0 - E_m^0|$.

**Example 7.1 — Anharmonic oscillator:** $\hat H' = \lambda\hat x^4$ added to a harmonic oscillator. Using $\hat x = \sqrt{\hbar/2m\omega}(\hat a + \hat a^\dagger)$: $E_0^{(1)} = \lambda\langle0|\hat x^4|0\rangle = \frac{3\lambda\hbar^2}{4m^2\omega^2}$.

**Example 7.2 — Helium ground state:** treating electron repulsion $\frac{e^2}{4\pi\varepsilon_0|\vec r_1 - \vec r_2|}$ as a perturbation on two hydrogen-like ($Z = 2$) electrons: $E^0 = 2\times(-13.6\times4) = -108.8$ eV; $E^{(1)} = \frac54Z\times13.6$ eV $= +34.0$ eV. Total ≈ −74.8 eV vs. experiment −79.0 eV (5% error — not bad for a perturbation that isn't small).

**Example 7.3 — Polarizability (quadratic Stark effect):** an atom in an electric field $\mathcal E$ has $\hat H' = e\mathcal Ez$. For a ground state with definite parity, the first-order shift vanishes; the second-order shift is $-\frac12\alpha_{\text{pol}}\mathcal E^2$, defining the atomic polarizability.

### 8. Degenerate perturbation theory
If several unperturbed states share the same energy, the formulas above blow up (zero denominators). Instead, diagonalize $\hat H'$ within the degenerate subspace: the "good" zeroth-order states are eigenvectors of the matrix $W_{ij} = \langle i^0|\hat H'|j^0\rangle$, and the first-order energy corrections are its eigenvalues. Symmetry usually identifies the good states: choose states that are eigenstates of an operator commuting with both $\hat H^0$ and $\hat H'$.

Examples: the linear Stark effect in hydrogen (mixing 2s and 2p₀ splits the $n = 2$ level), fine structure (good quantum numbers $j$, $m_j$ rather than $m_\ell$, $m_s$), and band gaps opening at Brillouin-zone boundaries in solids (nearly-free electron model).

### 9. The variational principle
For any normalized trial state $|\psi\rangle$:
$$\boxed{E_{\text{gs}} \le \langle\psi|\hat H|\psi\rangle}$$
The expectation value of the Hamiltonian is an **upper bound** on the ground-state energy.

**Proof:** expand $|\psi\rangle = \sum c_n|n\rangle$ in energy eigenstates; $\langle H\rangle = \sum|c_n|^2E_n \ge E_{\text{gs}}\sum|c_n|^2 = E_{\text{gs}}$.

**Method:** choose a trial function with adjustable parameters, compute $\langle H\rangle$, and minimize. The better the trial function, the closer the bound. Errors in the energy are second order in errors in the wavefunction, so even rough trial functions give good energies.

**Example 9.1 — Helium with screening:** use a product of hydrogen-like 1s orbitals with an effective charge $Z_{\text{eff}}$ as the variational parameter. Minimizing gives $Z_{\text{eff}} = Z - \frac{5}{16} = \frac{27}{16} \approx 1.69$ — each electron partially screens the nucleus from the other — and $E = -2\left(\frac{27}{16}\right)^2\times13.6$ eV $\approx -77.5$ eV, within 2% of experiment. More elaborate trial functions (Hylleraas, 1929; modern calculations with thousands of terms) agree with experiment to many significant figures.

**Example 9.2 — Harmonic oscillator with a Gaussian:** trial $\psi = Ae^{-bx^2}$ gives $\langle H\rangle = \frac{\hbar^2b}{2m} + \frac{m\omega^2}{8b}$, minimized at $b = \frac{m\omega}{2\hbar}$ with $\langle H\rangle = \frac12\hbar\omega$ — the exact answer, because the trial family contains the true ground state.

The variational principle underlies essentially all computational quantum chemistry and is the basis of the **variational quantum eigensolver (VQE)** in quantum computing.

### 10. The WKB approximation
For slowly varying potentials (wavelength changes little over one wavelength), write $\psi = e^{iS(x)/\hbar}$ and expand in $\hbar$. The leading approximation (Wentzel, Kramers, Brillouin, 1926):
$$\psi(x) \approx \frac{C}{\sqrt{p(x)}}\exp\left(\pm\frac{i}{\hbar}\int p(x)\,dx\right), \qquad p(x) = \sqrt{2m(E - V(x))}$$
- **Classically allowed regions:** oscillatory, with amplitude $\propto 1/\sqrt p$ — the particle is more likely to be found where it moves slowly, matching classical intuition.
- **Forbidden regions:** exponential decay $\propto\exp\left(-\frac1\hbar\int|p|\,dx\right)$, giving the tunneling formula $T \approx e^{-2\gamma}$, $\gamma = \frac1\hbar\int\sqrt{2m(V - E)}\,dx$ (used for alpha decay, field emission, fusion rates).
- **Bound states** (with connection formulas at turning points) — the Bohr–Sommerfeld quantization rule, corrected:
$$\oint p\,dx = 2\pi\hbar\left(n + \tfrac12\right)$$
This is exact for the harmonic oscillator and excellent for large $n$ in general.

WKB fails near classical turning points (where $p \to 0$); connection formulas using Airy functions bridge them.

### 11. Time-dependent perturbation theory
For $\hat H = \hat H^0 + \hat H'(t)$, expand $|\psi(t)\rangle = \sum_nc_n(t)e^{-iE_nt/\hbar}|n\rangle$. To first order, starting in state $|i\rangle$, the amplitude to be in $|f\rangle$ is
$$c_f^{(1)}(t) = -\frac i\hbar\int_0^t\langle f|\hat H'(t')|i\rangle e^{i\omega_{fi}t'}dt', \qquad \omega_{fi} = \frac{E_f - E_i}{\hbar}$$

**Sinusoidal perturbation** $\hat H' = \hat Ve^{-i\omega t} + \hat V^\dagger e^{i\omega t}$: transitions are significant only near resonance $\omega \approx \pm\omega_{fi}$ — **absorption** ($E_f = E_i + \hbar\omega$) and **stimulated emission** ($E_f = E_i - \hbar\omega$). The transition probability grows as $\frac{\sin^2[(\omega_{fi} - \omega)t/2]}{(\omega_{fi} - \omega)^2}$, sharply peaked with width $\sim 2\pi/t$ — energy conservation emerges over long times.

### 12. Fermi's golden rule
For transitions into a continuum of final states with density $\rho(E_f)$, the probability grows linearly in time, giving a constant **transition rate**:
$$\boxed{\Gamma_{i\to f} = \frac{2\pi}{\hbar}|\langle f|\hat H'|i\rangle|^2\rho(E_f)}$$
(Derived by Dirac; named "golden rule" by Fermi.) It is used to compute:
- Atomic decay rates and spectral line strengths.
- Beta decay rates (Fermi's theory of weak interactions, 1934).
- Scattering cross sections (equivalent to the first Born approximation).
- Absorption of light in semiconductors and solar cells.
- Electron–phonon scattering and electrical resistivity.

### 13. Interaction of atoms with light; Einstein coefficients
In the dipole approximation, the light–atom interaction is $\hat H' = -\hat{\vec d}\cdot\vec E(t)$, with $\hat{\vec d} = -e\hat{\vec r}$. Transition rates are proportional to $|\langle f|\hat{\vec r}|i\rangle|^2$, which vanish unless the **selection rules** are satisfied ($\Delta\ell = \pm1$, $\Delta m = 0, \pm1$, parity change).

Einstein (1917), using only thermal equilibrium arguments with Planck's law, showed that three processes must exist, with coefficients related by:
- Absorption rate $B_{12}\rho(\nu)$, stimulated emission $B_{21}\rho(\nu)$, spontaneous emission $A_{21}$.
- $g_1B_{12} = g_2B_{21}$ and $A_{21} = \frac{8\pi h\nu^3}{c^3}B_{21}$.

**Spontaneous emission** rate for a dipole transition:
$$A = \frac{\omega^3|\langle f|\hat{\vec d}|i\rangle|^2}{3\pi\varepsilon_0\hbar c^3}$$
The $\omega^3$ dependence explains why spontaneous emission dominates for UV/visible transitions (lifetimes ~ns) but is negligible for microwave/radio transitions (the 21 cm line: ~10⁷ years). Full understanding of spontaneous emission requires quantizing the electromagnetic field: it is emission stimulated by vacuum fluctuations.

### 14. Approximations for molecules and solids
- **Born–Oppenheimer approximation** (1927): nuclei are thousands of times heavier than electrons and move much more slowly. Solve for electrons with nuclei clamped at fixed positions; the electronic energy as a function of nuclear positions becomes the **potential energy surface** on which nuclei move. This justifies molecular structure, bond lengths, vibrational spectra and reaction pathways.
- **Hartree–Fock method:** approximate the many-electron wavefunction by a single Slater determinant and solve self-consistently for orbitals, each electron moving in the average field of the others plus exchange. Misses **electron correlation**, which post-Hartree–Fock methods (configuration interaction, coupled cluster — "CCSD(T)", the "gold standard" of quantum chemistry) recover.
- **Density functional theory (DFT):** Hohenberg and Kohn (1964) proved that the ground-state energy is a functional of the electron density alone; Kohn and Sham (1965) made it practical. DFT is the most widely used method in computational chemistry and materials science (Kohn and Pople, Nobel Chemistry 1998). Its accuracy depends on the approximate exchange–correlation functional (LDA, GGA such as PBE, hybrids such as B3LYP).
- **Bloch's theorem:** in a periodic crystal potential, eigenstates have the form $\psi_{\vec k}(\vec r) = e^{i\vec k\cdot\vec r}u_{\vec k}(\vec r)$ with $u$ periodic, leading to energy bands and band gaps (see the condensed-matter document).

## 15. Summary

| Method / Concept | Key formula |
|---|---|
| Exchange symmetry | $\psi(x_2, x_1) = \pm\psi(x_1, x_2)$ (boson +, fermion −) |
| Pauli exclusion | Antisymmetric state vanishes for identical occupation |
| 1st-order energy | $E_n^{(1)} = \langle n\vert H'\vert n\rangle$ |
| 2nd-order energy | $E_n^{(2)} = \sum_{m\ne n}\frac{\lvert\langle m\vert H'\vert n\rangle\rvert^2}{E_n - E_m}$ |
| Variational bound | $E_{\text{gs}} \le \langle\psi\vert H\vert\psi\rangle$ |
| Helium (variational) | $Z_{\text{eff}} = 27/16$, $E \approx -77.5$ eV (exp. −79.0 eV) |
| WKB tunneling | $T \approx \exp(-\frac2\hbar\int\sqrt{2m(V-E)}dx)$ |
| Bohr–Sommerfeld (WKB) | $\oint p\,dx = (n + \frac12)h$ |
| Fermi's golden rule | $\Gamma = \frac{2\pi}{\hbar}\lvert H'_{fi}\rvert^2\rho(E_f)$ |
| Einstein A coefficient | $A = \omega^3\lvert d_{fi}\rvert^2/(3\pi\varepsilon_0\hbar c^3)$ |
