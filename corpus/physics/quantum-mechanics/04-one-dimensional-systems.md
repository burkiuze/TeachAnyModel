---
title: Exactly Solvable One-Dimensional Quantum Systems - Wells, Barriers, Tunneling and the Harmonic Oscillator
field: Physics
subfield: Quantum Mechanics
level: undergraduate
keywords: [particle in a box, infinite square well, finite square well, potential step, reflection coefficient, transmission coefficient, quantum tunneling, potential barrier, alpha decay, scanning tunneling microscope, quantum harmonic oscillator, ladder operators, creation and annihilation operators, Hermite polynomials, zero-point energy, coherent states, delta function potential, quantum dots]
---

# Exactly Solvable One-Dimensional Quantum Systems

A handful of potentials can be solved exactly, and they form the backbone of quantum intuition. Each reveals a key quantum phenomenon: energy quantization, zero-point energy, penetration into classically forbidden regions, tunneling, and the algebraic structure of the harmonic oscillator. Real systems — electrons in nanostructures, vibrating molecules, alpha decay, scanning tunneling microscopes — are modeled with these solutions.

Throughout, we solve the time-independent Schrödinger equation
$$-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi$$

## 1. The Infinite Square Well (Particle in a Box)

$$V(x) = \begin{cases}0 & 0 < x < a\\ \infty & \text{otherwise}\end{cases}$$

### Solution
Outside the well $\psi = 0$. Inside, $\psi'' = -k^2\psi$ with $k = \sqrt{2mE}/\hbar$, so $\psi = A\sin kx + B\cos kx$. Boundary conditions:
- $\psi(0) = 0 \Rightarrow B = 0$
- $\psi(a) = 0 \Rightarrow \sin ka = 0 \Rightarrow ka = n\pi$, $n = 1, 2, 3, \ldots$ ($n = 0$ gives $\psi = 0$; negative $n$ give the same states)

Normalizing:
$$\boxed{\psi_n(x) = \sqrt{\frac2a}\sin\left(\frac{n\pi x}{a}\right), \qquad E_n = \frac{n^2\pi^2\hbar^2}{2ma^2} = \frac{n^2h^2}{8ma^2}}$$

### Key features
1. **Energy is quantized**, growing as $n^2$. Levels spread apart at higher energy.
2. **Zero-point energy:** the lowest energy $E_1 = \frac{\pi^2\hbar^2}{2ma^2} > 0$. A confined particle can never be at rest — consistent with the uncertainty principle.
3. **Smaller box → larger energies** ($E \propto 1/a^2$); heavier particle → smaller energies ($E \propto 1/m$).
4. **Nodes:** $\psi_n$ has $n - 1$ interior nodes. Wavefunctions alternate between even and odd about the center.
5. **Orthonormality:** $\int_0^a\psi_m\psi_n\,dx = \delta_{mn}$; completeness — any function on $[0, a]$ vanishing at the ends can be expanded as a Fourier sine series in $\psi_n$.
6. **Correspondence principle:** for large $n$, $|\psi_n|^2$ oscillates so rapidly that its average approaches the uniform classical distribution $1/a$.
7. **Expectation values:** $\langle x\rangle = a/2$; $\langle p\rangle = 0$; $\langle p^2\rangle = (n\pi\hbar/a)^2$; $\sigma_x\sigma_p = \frac\hbar2\sqrt{\frac{n^2\pi^2}{3} - 2}$, which equals $0.568\hbar$ for $n = 1$ — above the minimum $\hbar/2$.

### Numerical scale
An electron in a 1 nm box: $E_1 = \frac{(6.626\times10^{-34})^2}{8(9.11\times10^{-31})(10^{-9})^2} \approx 6.0\times10^{-20}$ J $\approx 0.376$ eV. The $1\to2$ transition ($3E_1 \approx 1.13$ eV) corresponds to a photon of ~1100 nm (infrared).

### Applications
- **Conjugated molecules:** π electrons in polyenes (e.g. β-carotene) behave approximately like particles in a 1D box the length of the conjugated chain. Longer chains have smaller HOMO–LUMO gaps and absorb longer wavelengths — β-carotene absorbs blue light and looks orange.
- **Quantum dots:** semiconductor nanocrystals (2–10 nm) confine electrons in 3D. Their emission color is tuned by size — smaller dots emit bluer light. Used in QLED displays and biological imaging (Nobel Chemistry 2023: Bawendi, Brus, Ekimov).
- **Quantum wells** in semiconductor lasers and LEDs.
- **Nuclear physics:** a crude model for nucleons confined in a nucleus.

### 3D box
For a cubic box of side $a$: $E = \frac{\pi^2\hbar^2}{2ma^2}(n_x^2 + n_y^2 + n_z^2)$. Different combinations can give the same energy — **degeneracy**, a consequence of symmetry. E.g. $(2,1,1)$, $(1,2,1)$, $(1,1,2)$ are three-fold degenerate. This model underlies the free-electron model of metals and the counting of states that gives the density of states $g(E) \propto\sqrt E$.

## 2. The Finite Square Well

$$V(x) = \begin{cases}-V_0 & |x| < a\\ 0 & |x| > a\end{cases}$$

For bound states ($-V_0 < E < 0$), define $k = \sqrt{2m(E + V_0)}/\hbar$ (inside) and $\kappa = \sqrt{-2mE}/\hbar$ (outside):
- Inside: oscillatory, $\cos kx$ (even) or $\sin kx$ (odd).
- Outside: decaying exponentials $e^{-\kappa|x|}$.

Matching $\psi$ and $\psi'$ at $x = a$ gives transcendental equations:
$$\text{Even: } \kappa = k\tan(ka), \qquad \text{Odd: } \kappa = -k\cot(ka)$$
With $z = ka$ and $z_0 = \frac a\hbar\sqrt{2mV_0}$, the even condition becomes $\tan z = \sqrt{(z_0/z)^2 - 1}$, solved graphically or numerically.

### Key features
1. **Finite number of bound states:** about $\lceil 2z_0/\pi\rceil$. Deeper or wider wells have more.
2. **At least one bound state always exists** in 1D (and 2D) for any attractive well, however shallow. (Not true in 3D, where a minimum depth is needed — this is why the deuteron has only one bound state and the diproton has none.)
3. **Wavefunctions penetrate into the classically forbidden region**, decaying over the **penetration depth** $\delta = 1/\kappa$. The particle has a nonzero probability of being found where its kinetic energy would be negative.
4. Energies are lower than those of an infinite well of the same width (the wavefunction "leaks", effectively widening the well).
5. Unbound states ($E > 0$) form a continuum. At special energies, transmission over the well is perfect — **resonant transmission** (seen in the Ramsauer–Townsend effect, in which low-energy electrons pass through noble-gas atoms almost without scattering).

## 3. The Potential Step

$$V(x) = \begin{cases}0 & x < 0\\ V_0 & x > 0\end{cases}$$
A particle with energy $E$ approaches from the left.

### Case $E > V_0$
Left: $\psi = e^{ik_1x} + re^{-ik_1x}$ (incident + reflected); right: $\psi = te^{ik_2x}$ (transmitted), with $k_1 = \sqrt{2mE}/\hbar$, $k_2 = \sqrt{2m(E - V_0)}/\hbar$. Continuity of $\psi$ and $\psi'$ gives
$$r = \frac{k_1 - k_2}{k_1 + k_2}, \qquad t = \frac{2k_1}{k_1 + k_2}$$
Reflection and transmission probabilities (from the probability current):
$$R = \left(\frac{k_1 - k_2}{k_1 + k_2}\right)^2, \qquad T = \frac{4k_1k_2}{(k_1 + k_2)^2}, \qquad R + T = 1$$
**Quantum surprise:** there is partial reflection even though the particle has enough energy to pass. Classically, $R = 0$. (Similarly, a particle hitting a downward step also partially reflects.) This is the matter-wave analog of partial reflection of light at a change in refractive index.

### Case $E < V_0$
On the right, $\psi = te^{-\kappa x}$ with $\kappa = \sqrt{2m(V_0 - E)}/\hbar$. Then $|r| = 1$: **total reflection** ($R = 1$), but the wavefunction penetrates into the step with decay length $1/\kappa$. No probability current flows to the right in steady state.

## 4. The Rectangular Barrier and Quantum Tunneling

$$V(x) = \begin{cases}V_0 & 0 < x < L\\ 0 & \text{otherwise}\end{cases}$$
For $E < V_0$, classically the particle is always reflected. Quantum mechanically, the wavefunction decays inside the barrier but is nonzero on the far side: the particle **tunnels** through.

Exact transmission coefficient:
$$T = \left[1 + \frac{V_0^2\sinh^2(\kappa L)}{4E(V_0 - E)}\right]^{-1}, \qquad \kappa = \frac{\sqrt{2m(V_0 - E)}}{\hbar}$$
For a thick or high barrier ($\kappa L \gg 1$):
$$\boxed{T \approx 16\frac{E}{V_0}\left(1 - \frac{E}{V_0}\right)e^{-2\kappa L}}$$
The exponential dependence makes tunneling **extremely sensitive** to barrier width, height and particle mass.

For arbitrary smooth barriers, the **WKB approximation** gives
$$T \approx \exp\left(-\frac2\hbar\int_{x_1}^{x_2}\sqrt{2m(V(x) - E)}\,dx\right)$$
integrated over the classically forbidden region.

### Worked example 4.1
**Problem:** An electron with $E = 1$ eV meets a barrier of height 5 eV and width 0.5 nm. Estimate $T$.
**Solution:** $\kappa = \frac{\sqrt{2(9.11\times10^{-31})(4\times1.602\times10^{-19})}}{1.055\times10^{-34}} \approx 1.02\times10^{10}$ m⁻¹. $2\kappa L \approx 10.2$. $T \approx 16(0.2)(0.8)e^{-10.2} \approx 2.56\times3.7\times10^{-5} \approx 9.5\times10^{-5}$.
Doubling the width to 1 nm reduces $T$ by a further factor of $e^{-10.2} \approx 3.7\times10^{-5}$, to ~$3.5\times10^{-9}$. A proton (1836 times heavier) facing the original barrier would have $\kappa$ larger by $\sqrt{1836} \approx 43$, giving $T \sim e^{-440}$ — effectively zero.

### Tunneling in nature and technology
- **Alpha decay** (Gamow; Gurney and Condon, 1928): an alpha particle inside a nucleus has energy (4–9 MeV) below the Coulomb barrier (~25–30 MeV for heavy nuclei) but tunnels out. Because $T$ depends exponentially on energy, small differences in alpha energy produce enormous differences in half-life — the **Geiger–Nuttall law**. Polonium-212 (8.95 MeV alphas) has a half-life of 0.3 μs; thorium-232 (4.08 MeV) has 14 billion years — a factor of over $10^{24}$ from roughly a factor of two in energy.
- **Nuclear fusion in stars:** protons in the Sun's core (~15 million K, average thermal energy ~1.3 keV) could never classically overcome their ~1 MeV Coulomb barrier; tunneling makes fusion possible (Gamow peak).
- **Scanning tunneling microscope (STM)** (Binnig and Rohrer, 1981; Nobel 1986): a sharp tip held ~0.5–1 nm from a surface; the tunneling current changes by about a factor of 10 for every 0.1 nm change in distance, giving atomic resolution. STMs can also move individual atoms (IBM's 1989 "IBM" spelled with 35 xenon atoms).
- **Tunnel diodes** (Esaki, Nobel 1973), **Josephson junctions** (Cooper pairs tunnel between superconductors; Josephson, Nobel 1973) — basis of SQUIDs, voltage standards and superconducting qubits.
- **Flash memory:** electrons tunnel through a thin oxide (Fowler–Nordheim tunneling) to charge or discharge a floating gate.
- **Field emission** of electrons from sharp tips in strong fields.
- **Chemistry and biology:** proton and electron tunneling in enzyme reactions; the ammonia molecule's nitrogen tunnels through the plane of hydrogens (inversion frequency 23.87 GHz, used in the first maser, 1954); kinetic isotope effects.
- **Transistor scaling limit:** as gate oxides thin to ~1 nm, leakage by tunneling becomes a serious problem, motivating high-κ dielectrics.

**How long does tunneling take?** The "tunneling time" is subtle; experiments with attosecond lasers on helium atoms (2019, Ramos et al.) suggest it is very short or effectively instantaneous, but there is no superluminal information transfer.

## 5. The Quantum Harmonic Oscillator

$$V(x) = \tfrac12m\omega^2x^2$$
The most important system in physics. Every potential near a stable minimum is approximately harmonic, so it describes molecular vibrations, lattice vibrations (phonons), the modes of the electromagnetic field (photons), and quantum fields in general.

### Energy levels
$$\boxed{E_n = \hbar\omega\left(n + \tfrac12\right), \qquad n = 0, 1, 2, \ldots}$$
- **Equally spaced** by $\hbar\omega$ — unlike the box ($n^2$) or hydrogen ($1/n^2$).
- **Zero-point energy** $E_0 = \frac12\hbar\omega$.

### Algebraic solution: ladder operators (Dirac's method)
Define the dimensionless **annihilation (lowering)** and **creation (raising)** operators:
$$\hat a = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat x + \frac{i\hat p}{m\omega}\right), \qquad \hat a^\dagger = \sqrt{\frac{m\omega}{2\hbar}}\left(\hat x - \frac{i\hat p}{m\omega}\right)$$
From $[\hat x, \hat p] = i\hbar$:
$$[\hat a, \hat a^\dagger] = 1, \qquad \hat H = \hbar\omega\left(\hat a^\dagger\hat a + \tfrac12\right) = \hbar\omega\left(\hat N + \tfrac12\right)$$
where $\hat N = \hat a^\dagger\hat a$ is the **number operator**. Using $[\hat N, \hat a^\dagger] = \hat a^\dagger$ and $[\hat N, \hat a] = -\hat a$:
- $\hat a^\dagger$ raises the energy by $\hbar\omega$: $\hat a^\dagger|n\rangle = \sqrt{n+1}\,|n+1\rangle$
- $\hat a$ lowers it by $\hbar\omega$: $\hat a|n\rangle = \sqrt n\,|n-1\rangle$
- The ladder must terminate at the bottom: $\hat a|0\rangle = 0$, which defines the ground state.
- $|n\rangle = \frac{(\hat a^\dagger)^n}{\sqrt{n!}}|0\rangle$.

Position and momentum in terms of ladder operators:
$$\hat x = \sqrt{\frac{\hbar}{2m\omega}}(\hat a + \hat a^\dagger), \qquad \hat p = i\sqrt{\frac{m\omega\hbar}{2}}(\hat a^\dagger - \hat a)$$
This makes matrix elements trivial: $\langle n'|\hat x|n\rangle$ is nonzero only for $n' = n \pm 1$ — the **selection rule** $\Delta n = \pm1$ for dipole transitions in harmonic vibrations.

In quantum field theory, the same algebra describes creating and destroying particles: $|n\rangle$ is a state with $n$ quanta (photons, phonons) in a mode.

### Wavefunctions
Solving $\hat a\psi_0 = 0$ (a first-order differential equation):
$$\psi_0(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}e^{-m\omega x^2/2\hbar}$$
— a Gaussian, a minimum-uncertainty state with $\sigma_x\sigma_p = \hbar/2$. In general, with $\xi = \sqrt{m\omega/\hbar}\,x$:
$$\psi_n(x) = \left(\frac{m\omega}{\pi\hbar}\right)^{1/4}\frac{1}{\sqrt{2^nn!}}H_n(\xi)e^{-\xi^2/2}$$
where $H_n$ are **Hermite polynomials**: $H_0 = 1$, $H_1 = 2\xi$, $H_2 = 4\xi^2 - 2$, $H_3 = 8\xi^3 - 12\xi$, ...

Properties: $\psi_n$ has $n$ nodes and parity $(-1)^n$; it extends beyond the classical turning points $x = \pm\sqrt{(2n+1)\hbar/(m\omega)}$; for large $n$, $|\psi_n|^2$ approaches the classical distribution, which peaks at the turning points where the classical particle moves slowest. In the ground state there is about a 16% probability of finding the particle outside the classically allowed region.

**Expectation values in $|n\rangle$:** $\langle x\rangle = \langle p\rangle = 0$; $\langle V\rangle = \langle T\rangle = \frac12E_n$ (virial theorem); $\sigma_x\sigma_p = (n + \frac12)\hbar$.

### Coherent states
Eigenstates of the annihilation operator, $\hat a|\alpha\rangle = \alpha|\alpha\rangle$:
$$|\alpha\rangle = e^{-|\alpha|^2/2}\sum_{n=0}^\infty\frac{\alpha^n}{\sqrt{n!}}|n\rangle$$
They are Gaussian wave packets that oscillate back and forth **without spreading**, following the classical trajectory exactly, with minimum uncertainty at all times. The number of quanta follows a Poisson distribution with mean $|\alpha|^2$. Laser light is well described by coherent states (Glauber, Nobel 2005). **Squeezed states** reduce uncertainty in one quadrature below the vacuum level at the expense of the other — used to improve LIGO's sensitivity.

### Applications
- **Molecular vibrations:** a diatomic molecule's bond acts like a spring with reduced mass $\mu = \frac{m_1m_2}{m_1 + m_2}$: $\omega = \sqrt{k/\mu}$. HCl vibrates at ~$8.66\times10^{13}$ Hz (absorbing infrared at ~2886 cm⁻¹, i.e. ~3.46 μm). Infrared spectroscopy identifies functional groups by their vibrational frequencies. Anharmonicity (Morse potential) makes levels converge at higher $n$, leading to dissociation.
- **Heat capacities of solids** (Einstein and Debye models).
- **Quantization of the electromagnetic field:** each mode is an oscillator; photons are its quanta; the vacuum has zero-point energy, leading to observable effects like the **Casimir force** between uncharged plates and the **Lamb shift**.
- **Trapped ions and atoms** in harmonic traps for quantum computing and atomic clocks.

## 6. The Delta-Function Potential

$$V(x) = -\alpha\delta(x), \qquad \alpha > 0$$
A useful idealization of a very short-range potential. There is exactly one bound state:
$$\psi(x) = \frac{\sqrt{m\alpha}}{\hbar}e^{-m\alpha|x|/\hbar^2}, \qquad E = -\frac{m\alpha^2}{2\hbar^2}$$
(from the derivative-jump condition $\Delta\psi' = -\frac{2m\alpha}{\hbar^2}\psi(0)$). For scattering states, the transmission coefficient is $T = \frac{1}{1 + m\alpha^2/(2\hbar^2E)}$. The Kronig–Penney model (a periodic array of barriers or delta functions) explains **energy bands and band gaps** in crystals.

## 7. Comparison of Energy Spectra

| System | Energy levels | Spacing | Ground-state energy |
|---|---|---|---|
| Infinite square well | $E_n = n^2\frac{\pi^2\hbar^2}{2ma^2}$, $n \ge 1$ | Increases | $\frac{\pi^2\hbar^2}{2ma^2}$ |
| Harmonic oscillator | $E_n = (n + \frac12)\hbar\omega$, $n \ge 0$ | Constant | $\frac12\hbar\omega$ |
| Hydrogen atom | $E_n = -13.6\text{ eV}/n^2$, $n \ge 1$ | Decreases | −13.6 eV |
| Free particle | Continuous $E = \hbar^2k^2/2m$ | — | 0 (not normalizable) |
| Delta well | One level $-m\alpha^2/2\hbar^2$ | — | $-m\alpha^2/2\hbar^2$ |

**General lesson:** the shape of the potential determines the level spacing. Potentials that widen faster than a parabola ($x^4$, box) have increasing spacing; potentials that widen more slowly (Coulomb $-1/r$) have decreasing spacing.

## 8. Summary of Key Formulas

| Result | Formula |
|---|---|
| Box energies | $E_n = n^2h^2/(8ma^2)$ |
| Box wavefunctions | $\psi_n = \sqrt{2/a}\sin(n\pi x/a)$ |
| Step reflection ($E > V_0$) | $R = [(k_1 - k_2)/(k_1 + k_2)]^2$ |
| Barrier tunneling | $T \approx 16\frac{E}{V_0}(1 - \frac{E}{V_0})e^{-2\kappa L}$ |
| Decay constant | $\kappa = \sqrt{2m(V_0 - E)}/\hbar$ |
| WKB tunneling | $T \approx \exp(-\frac2\hbar\int\sqrt{2m(V - E)}dx)$ |
| Oscillator energies | $E_n = \hbar\omega(n + \frac12)$ |
| Ladder operators | $[\hat a, \hat a^\dagger] = 1$; $\hat a^\dagger\vert n\rangle = \sqrt{n+1}\vert n+1\rangle$; $\hat a\vert n\rangle = \sqrt n\vert n-1\rangle$ |
| Oscillator ground state | $\psi_0 \propto e^{-m\omega x^2/2\hbar}$ |
| Delta-well bound state | $E = -m\alpha^2/(2\hbar^2)$ |
