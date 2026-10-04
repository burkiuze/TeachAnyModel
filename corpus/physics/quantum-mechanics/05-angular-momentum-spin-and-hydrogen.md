---
title: Angular Momentum, Spin and the Hydrogen Atom
field: Physics
subfield: Quantum Mechanics
level: undergraduate
keywords: [orbital angular momentum, spherical harmonics, quantum numbers, hydrogen atom, radial equation, Laguerre polynomials, atomic orbitals, degeneracy, spin, Stern-Gerlach experiment, Pauli matrices, spinor, magnetic moment, g-factor, addition of angular momentum, Clebsch-Gordan coefficients, fine structure, Zeeman effect, hyperfine structure, 21 cm line, Lamb shift]
---

# Angular Momentum, Spin and the Hydrogen Atom

The hydrogen atom is the Rosetta Stone of quantum mechanics: the simplest atom, exactly solvable, and the template for understanding all of chemistry. Its solution requires the quantum theory of angular momentum, which also introduces **spin** — an intrinsic angular momentum with no classical counterpart.

## 1. Orbital Angular Momentum

The angular momentum operator is $\hat{\vec L} = \hat{\vec r}\times\hat{\vec p}$, with components
$$\hat L_x = \hat y\hat p_z - \hat z\hat p_y, \quad \hat L_y = \hat z\hat p_x - \hat x\hat p_z, \quad \hat L_z = \hat x\hat p_y - \hat y\hat p_x$$

### Commutation relations
From $[\hat x_i, \hat p_j] = i\hbar\delta_{ij}$:
$$\boxed{[\hat L_x, \hat L_y] = i\hbar\hat L_z, \quad [\hat L_y, \hat L_z] = i\hbar\hat L_x, \quad [\hat L_z, \hat L_x] = i\hbar\hat L_y}$$
or compactly $[\hat L_i, \hat L_j] = i\hbar\epsilon_{ijk}\hat L_k$. The components do **not** commute with each other, so no two components can be simultaneously definite (except when $L = 0$). However, each component commutes with the square of the total angular momentum:
$$[\hat L^2, \hat L_i] = 0$$
So we can simultaneously specify $L^2$ and **one** component, conventionally $L_z$.

### Eigenvalues (algebraic method)
Using ladder operators $\hat L_\pm = \hat L_x \pm i\hat L_y$, which raise or lower $m$ by one unit, one proves for any operators obeying these commutation relations:
$$\boxed{\hat L^2|\ell, m\rangle = \hbar^2\ell(\ell + 1)|\ell, m\rangle, \qquad \hat L_z|\ell, m\rangle = \hbar m|\ell, m\rangle}$$
with $m = -\ell, -\ell + 1, \ldots, \ell - 1, \ell$ ($2\ell + 1$ values). For orbital angular momentum, $\ell = 0, 1, 2, \ldots$ (integers only, because wavefunctions must be single-valued under a $2\pi$ rotation). The general algebra also allows half-integer values — realized by spin.

**Remarkable consequences:**
- The magnitude is $|L| = \hbar\sqrt{\ell(\ell + 1)}$, always **larger** than the maximum $L_z = \ell\hbar$. The angular momentum vector can never point exactly along the $z$-axis — that would make $L_x$ and $L_y$ both definite (zero), violating the uncertainty relation. The **vector model** pictures $\vec L$ precessing on a cone around $z$.
- **Space quantization:** the projection of $\vec L$ on any axis can take only $2\ell + 1$ discrete values.

### Spherical harmonics
In spherical coordinates, $\hat L_z = -i\hbar\frac{\partial}{\partial\phi}$ and $\hat L^2 = -\hbar^2\left[\frac{1}{\sin\theta}\frac{\partial}{\partial\theta}\left(\sin\theta\frac{\partial}{\partial\theta}\right) + \frac{1}{\sin^2\theta}\frac{\partial^2}{\partial\phi^2}\right]$. The simultaneous eigenfunctions are the **spherical harmonics** $Y_\ell^m(\theta, \phi) \propto P_\ell^m(\cos\theta)e^{im\phi}$:

| $\ell$ | $m$ | $Y_\ell^m$ |
|---|---|---|
| 0 | 0 | $\sqrt{\frac{1}{4\pi}}$ |
| 1 | 0 | $\sqrt{\frac{3}{4\pi}}\cos\theta$ |
| 1 | ±1 | $\mp\sqrt{\frac{3}{8\pi}}\sin\theta\,e^{\pm i\phi}$ |
| 2 | 0 | $\sqrt{\frac{5}{16\pi}}(3\cos^2\theta - 1)$ |
| 2 | ±1 | $\mp\sqrt{\frac{15}{8\pi}}\sin\theta\cos\theta\,e^{\pm i\phi}$ |
| 2 | ±2 | $\sqrt{\frac{15}{32\pi}}\sin^2\theta\,e^{\pm2i\phi}$ |

They are orthonormal over the sphere, complete, and have parity $(-1)^\ell$. Spherical harmonics appear wherever there is spherical symmetry: atomic orbitals, gravitational and magnetic field models of Earth, the cosmic microwave background power spectrum, 3D computer graphics lighting, and antenna radiation patterns.

## 2. Central Potentials

For any spherically symmetric potential $V(r)$, the Hamiltonian commutes with $\hat L^2$ and $\hat L_z$. Separating $\psi(r, \theta, \phi) = R(r)Y_\ell^m(\theta, \phi)$ and writing $u(r) = rR(r)$ gives the **radial equation**:
$$-\frac{\hbar^2}{2m}\frac{d^2u}{dr^2} + \left[V(r) + \frac{\hbar^2\ell(\ell + 1)}{2mr^2}\right]u = Eu$$
This is a 1D Schrödinger equation with an **effective potential** including the **centrifugal barrier** $\frac{\hbar^2\ell(\ell+1)}{2mr^2}$, which keeps particles with $\ell > 0$ away from the origin. Since the energy doesn't depend on $m$ (the potential has no preferred direction), each level is at least $(2\ell + 1)$-fold degenerate.

## 3. The Hydrogen Atom

### Setting up
An electron (charge $-e$) bound to a proton by the Coulomb potential
$$V(r) = -\frac{e^2}{4\pi\varepsilon_0r}$$
(Using the reduced mass $\mu = \frac{m_em_p}{m_e + m_p}$ accounts for proton motion; it differs from $m_e$ by 0.05%.)

### Solution sketch
The radial equation, after introducing $\rho = r/a_0$ and analyzing behavior at small and large $r$, gives $u(\rho) = \rho^{\ell+1}e^{-\rho/n}v(\rho)$. Normalizability requires the power series for $v$ to terminate, which happens only when
$$n = n_r + \ell + 1, \qquad n_r = 0, 1, 2, \ldots$$
The polynomials are **associated Laguerre polynomials**.

### Energy levels
$$\boxed{E_n = -\frac{\mu e^4}{2(4\pi\varepsilon_0)^2\hbar^2}\frac{1}{n^2} = -\frac{13.6\text{ eV}}{n^2} = -\frac{\alpha^2\mu c^2}{2n^2}}$$
exactly Bohr's result — now derived, not postulated.

### Quantum numbers

| Quantum number | Name | Allowed values | Determines |
|---|---|---|---|
| $n$ | Principal | 1, 2, 3, ... | Energy, size |
| $\ell$ | Orbital (azimuthal) | 0, 1, ..., $n - 1$ | Shape, $L^2 = \hbar^2\ell(\ell+1)$ |
| $m_\ell$ | Magnetic | $-\ell$, ..., $+\ell$ | Orientation, $L_z = m_\ell\hbar$ |
| $m_s$ | Spin magnetic | $\pm\frac12$ | Spin orientation |

Spectroscopic notation: $\ell = 0, 1, 2, 3, 4$ ↔ **s, p, d, f, g** (from "sharp", "principal", "diffuse", "fundamental", then alphabetical).

### Degeneracy
For each $n$ there are $n$ values of $\ell$, each with $2\ell + 1$ values of $m$: total $\sum_{\ell=0}^{n-1}(2\ell+1) = n^2$ spatial states, or $2n^2$ including spin. The degeneracy in $\ell$ (states with different $\ell$ but the same $n$ have the same energy) is special to the $1/r$ potential — an "accidental" degeneracy due to a hidden symmetry (conservation of the Laplace–Runge–Lenz vector, the same symmetry that makes classical Kepler orbits closed). In multi-electron atoms, screening breaks it.

### Wavefunctions
$\psi_{n\ell m}(r, \theta, \phi) = R_{n\ell}(r)Y_\ell^m(\theta, \phi)$. The first few radial functions ($a_0$ = Bohr radius):
$$R_{10} = 2a_0^{-3/2}e^{-r/a_0}$$
$$R_{20} = \frac{1}{\sqrt2}a_0^{-3/2}\left(1 - \frac{r}{2a_0}\right)e^{-r/2a_0}$$
$$R_{21} = \frac{1}{\sqrt{24}}a_0^{-3/2}\frac{r}{a_0}e^{-r/2a_0}$$

**Ground state (1s):** $\psi_{100} = \frac{1}{\sqrt{\pi a_0^3}}e^{-r/a_0}$.
- The probability density $|\psi|^2$ is maximal at the nucleus.
- The **radial probability density** $P(r) = r^2|R|^2 = \frac{4r^2}{a_0^3}e^{-2r/a_0}$ peaks at $r = a_0$ — the Bohr radius is the most probable distance.
- $\langle r\rangle = \frac32a_0$; $\langle 1/r\rangle = 1/a_0$; $\langle V\rangle = -27.2$ eV $= 2E_1$; $\langle T\rangle = 13.6$ eV $= -E_1$ (virial theorem).
- In general, $\langle r\rangle_{n\ell} = \frac{a_0}{2}[3n^2 - \ell(\ell+1)]$; sizes grow as $n^2$. Highly excited **Rydberg atoms** ($n \sim 100$) are micrometers across.

**Nodes:** $\psi_{n\ell m}$ has $n - \ell - 1$ radial nodes and $\ell$ angular nodes (nodal planes or cones), $n - 1$ in total.

### Atomic orbitals
Chemists use real linear combinations of $Y_\ell^{\pm m}$:
- **s orbitals** ($\ell = 0$): spherically symmetric.
- **p orbitals** ($\ell = 1$): dumbbell-shaped $p_x$, $p_y$, $p_z$ with a nodal plane through the nucleus. $p_z \propto \cos\theta$; $p_x, p_y$ from $\frac{1}{\sqrt2}(Y_1^{-1} \mp Y_1^1)$.
- **d orbitals** ($\ell = 2$): five orbitals ($d_{xy}$, $d_{yz}$, $d_{xz}$, $d_{x^2-y^2}$, $d_{z^2}$), mostly four-lobed; crucial in transition-metal chemistry.
- **f orbitals** ($\ell = 3$): seven orbitals; lanthanides and actinides.

Orbitals are not paths; they are probability amplitude distributions. "Electron clouds" are visualizations of $|\psi|^2$.

### Spectral transitions and selection rules
Photon emission or absorption (electric dipole) requires
$$\Delta\ell = \pm1, \qquad \Delta m_\ell = 0, \pm1$$
(the photon carries one unit of angular momentum, and parity must change). The 2s state cannot decay to 1s by single-photon dipole emission; it is **metastable** (lifetime ~0.12 s, decaying by two-photon emission), compared with 1.6 ns for 2p.

### Hydrogen-like ions
For nuclear charge $Z$: $E_n = -13.6Z^2/n^2$ eV and $a = a_0/Z$. He⁺ ground state: −54.4 eV.

## 4. Spin

### The Stern–Gerlach experiment (1922)
Otto Stern and Walther Gerlach sent a beam of silver atoms through an inhomogeneous magnetic field. A magnetic moment $\vec\mu$ in a field gradient feels a force $F_z = \mu_z\frac{\partial B_z}{\partial z}$. Classically, randomly oriented moments would spread the beam into a continuous smear. Instead, the beam split into **exactly two** spots.

Silver has one unpaired outer electron in an s state ($\ell = 0$, no orbital moment). Two spots imply an angular momentum with $2s + 1 = 2$, i.e. $s = \frac12$ — impossible for orbital angular momentum. In 1925 Uhlenbeck and Goudsmit proposed that the electron has an **intrinsic angular momentum**: spin.

**Sequential Stern–Gerlach experiments** reveal quantum measurement in its purest form:
1. Select spin-up along $z$; measure $z$ again → always up.
2. Select up along $z$, then measure along $x$ → 50% up, 50% down.
3. Select $z$-up, then $x$-up, then measure $z$ again → 50/50. The $x$ measurement erased the earlier $z$ information. $S_x$ and $S_z$ are incompatible observables.

### Spin-½ formalism
Spin is not literal rotation (a point-like electron spinning fast enough to have angular momentum $\hbar/2$ would require surface speeds far exceeding $c$). It is an intrinsic quantum property, as fundamental as charge and mass. Dirac's relativistic equation (1928) predicts it naturally.

Spin operators obey the same algebra as orbital angular momentum, $[\hat S_i, \hat S_j] = i\hbar\epsilon_{ijk}\hat S_k$, with
$$S^2 = \hbar^2s(s+1) = \frac34\hbar^2, \qquad S_z = m_s\hbar = \pm\frac\hbar2$$

The state space is two-dimensional. In the basis $|\uparrow\rangle = \begin{pmatrix}1\\0\end{pmatrix}$, $|\downarrow\rangle = \begin{pmatrix}0\\1\end{pmatrix}$, a general state (**spinor**) is
$$|\chi\rangle = a|\uparrow\rangle + b|\downarrow\rangle, \qquad |a|^2 + |b|^2 = 1$$
Spin operators are $\hat S_i = \frac\hbar2\sigma_i$, with the **Pauli matrices**:
$$\sigma_x = \begin{pmatrix}0 & 1\\ 1 & 0\end{pmatrix}, \qquad \sigma_y = \begin{pmatrix}0 & -i\\ i & 0\end{pmatrix}, \qquad \sigma_z = \begin{pmatrix}1 & 0\\ 0 & -1\end{pmatrix}$$
Properties: $\sigma_i^2 = I$; $\sigma_x\sigma_y = i\sigma_z$ (cyclic); $\{\sigma_i, \sigma_j\} = 2\delta_{ij}I$; eigenvalues ±1; Hermitian, unitary, traceless.

Eigenstates of $S_x$: $|\pm x\rangle = \frac{1}{\sqrt2}(|\uparrow\rangle \pm |\downarrow\rangle)$. Eigenstates of $S_y$: $|\pm y\rangle = \frac{1}{\sqrt2}(|\uparrow\rangle \pm i|\downarrow\rangle)$.

**Bloch sphere:** every pure spin-½ state can be written $|\chi\rangle = \cos\frac\theta2|\uparrow\rangle + e^{i\phi}\sin\frac\theta2|\downarrow\rangle$ and corresponds to a point on a unit sphere — the spin "points" in direction $(\theta, \phi)$. This is also the standard picture of a **qubit**.

**Rotation by 360° changes the sign:** a spinor rotated by $2\pi$ acquires a factor of −1; it takes $4\pi$ to return to the original state. This has been confirmed in neutron interferometry experiments (1975).

### Spin and magnetic moment
The electron's spin magnetic moment is
$$\vec\mu_s = -g_s\frac{e}{2m_e}\vec S, \qquad g_s \approx 2.00231930436$$
Dirac's theory predicts $g = 2$ exactly; the small anomaly $a_e = (g - 2)/2 \approx 0.00115965218$ comes from quantum electrodynamics (QED) and is calculated and measured to better than one part in $10^{12}$ — the most precisely verified prediction in all of science. The muon's anomaly is a sensitive probe for new physics.

Orbital moment: $\vec\mu_L = -\frac{e}{2m_e}\vec L$ ($g_\ell = 1$); its natural unit is the **Bohr magneton** $\mu_B = \frac{e\hbar}{2m_e} = 9.274\times10^{-24}$ J/T $= 5.788\times10^{-5}$ eV/T.

### Spin precession and magnetic resonance
In a magnetic field $B\hat z$, the spin Hamiltonian is $\hat H = -\vec\mu\cdot\vec B = \omega_L\hat S_z$, and the spin expectation value precesses about $\hat z$ at the **Larmor frequency** $\omega_L = \gamma B$. For electrons, $f \approx 28$ GHz/T; for protons, $f = 42.58$ MHz/T. Applying an oscillating field at this frequency flips spins — **magnetic resonance**. Proton NMR is the basis of **MRI** (a 3 T scanner operates at ~128 MHz) and of NMR spectroscopy in chemistry; electron spin resonance (ESR/EPR) studies radicals and is used in some quantum technologies.

## 5. Addition of Angular Momentum

Combining two angular momenta $\vec J_1$ and $\vec J_2$, the total $\vec J = \vec J_1 + \vec J_2$ has quantum numbers
$$j = |j_1 - j_2|, |j_1 - j_2| + 1, \ldots, j_1 + j_2, \qquad m = m_1 + m_2$$
The total number of states is conserved: $(2j_1 + 1)(2j_2 + 1) = \sum_j(2j + 1)$.

### Two spin-½ particles
$\frac12\otimes\frac12 = 0\oplus1$: four states split into
- **Triplet** ($s = 1$, symmetric under exchange):
$$|1, 1\rangle = |\uparrow\uparrow\rangle, \quad |1, 0\rangle = \frac{1}{\sqrt2}(|\uparrow\downarrow\rangle + |\downarrow\uparrow\rangle), \quad |1, -1\rangle = |\downarrow\downarrow\rangle$$
- **Singlet** ($s = 0$, antisymmetric):
$$|0, 0\rangle = \frac{1}{\sqrt2}(|\uparrow\downarrow\rangle - |\downarrow\uparrow\rangle)$$

The singlet is the prototypical **entangled** state (used in Bell tests). The triplet–singlet distinction governs the chemistry of the H₂ bond (the bonding orbital holds an electron pair in a spin singlet), ortho- and para-hydrogen, helium's spectrum (parahelium and orthohelium), and magnetism.

The expansion coefficients relating the coupled basis $|j, m\rangle$ to the product basis $|j_1m_1\rangle|j_2m_2\rangle$ are the **Clebsch–Gordan coefficients**.

### Spin–orbit coupling: $\vec J = \vec L + \vec S$
For one electron with orbital $\ell$, $j = \ell \pm \frac12$ (for $\ell > 0$). Term symbols: $^{2S+1}L_J$, e.g. $^2P_{3/2}$, $^2P_{1/2}$.

## 6. Fine Structure, Hyperfine Structure and Beyond

The simple Coulomb model is very accurate but not exact. Corrections, in decreasing size:

### Fine structure (order $\alpha^2E_n \approx 10^{-4}$ eV)
1. **Relativistic kinetic energy correction.**
2. **Spin–orbit coupling:** in the electron's rest frame, the orbiting proton produces a magnetic field that interacts with the electron's spin magnetic moment: $\hat H_{SO} \propto \frac{1}{r^3}\vec L\cdot\vec S$.
3. **Darwin term** (for s states).

Combined (from the Dirac equation):
$$E_{nj} = -\frac{13.6\text{ eV}}{n^2}\left[1 + \frac{\alpha^2}{n^2}\left(\frac{n}{j + \frac12} - \frac34\right)\right]$$
Energy depends on $n$ and $j$ only. Example: the **sodium D lines** at 589.0 and 589.6 nm come from 3p₃/₂ and 3p₁/₂ → 3s₁/₂ (fine structure in a multi-electron atom); in hydrogen, H-α splits into closely spaced components.

The **fine-structure constant** $\alpha = \frac{e^2}{4\pi\varepsilon_0\hbar c} \approx \frac{1}{137.036}$ is dimensionless and sets the strength of electromagnetism. Why it has this value is unknown; Feynman called it "one of the greatest damn mysteries of physics".

### Lamb shift (order $\alpha^3$)
Dirac theory predicts that 2s₁/₂ and 2p₁/₂ are degenerate. In 1947 Willis Lamb and Robert Retherford measured a splitting of ~1058 MHz (~4.4 μeV). It arises from the electron's interaction with vacuum fluctuations of the electromagnetic field — a triumph of QED (Bethe, Feynman, Schwinger, Tomonaga).

### Hyperfine structure (order $\alpha^2\frac{m_e}{m_p}E_n \approx 10^{-6}$ eV)
Interaction between the electron's and proton's magnetic moments. The hydrogen ground state splits into $F = 1$ (spins parallel) and $F = 0$ (antiparallel), separated by $5.87$ μeV. Transitions emit the famous **21 cm line** (1420.405751 MHz). Though each atom flips only about once every ~10 million years, the vast amounts of hydrogen in space make this line the primary tool for mapping neutral hydrogen in the Milky Way and other galaxies (first detected 1951). It appears in the diagram on the Pioneer plaques and Voyager Golden Records as a universal unit of time and length.

The cesium-133 hyperfine transition (9 192 631 770 Hz exactly) **defines the SI second**.

### External fields
- **Zeeman effect** (magnetic field): levels split according to $m_j$. Normal Zeeman effect (spin ignored): three equally spaced lines, $\Delta E = \mu_BBm_\ell$. Anomalous Zeeman effect (with spin): more complex patterns via the Landé $g_J$ factor, $\Delta E = g_J\mu_BBm_j$. Astronomers measure sunspot magnetic fields (~0.1–0.4 T) from Zeeman splitting (George Ellery Hale, 1908).
- **Stark effect** (electric field): hydrogen shows a linear Stark effect because of its $\ell$ degeneracy; most atoms show a quadratic effect.

## 7. Multi-Electron Atoms (Preview)

For atoms with more than one electron, electron–electron repulsion makes exact solutions impossible, but the hydrogen-like orbital picture survives approximately:
- Each electron occupies an orbital labeled $n\ell m_\ell m_s$.
- **Pauli exclusion principle:** no two electrons can share all four quantum numbers (a consequence of fermion antisymmetry).
- **Screening:** inner electrons shield outer ones from the full nuclear charge; s orbitals penetrate closer to the nucleus than p or d, so for the same $n$, $E_s < E_p < E_d$. This breaks the $\ell$ degeneracy and produces the **Aufbau (Madelung) ordering**: 1s, 2s, 2p, 3s, 3p, 4s, 3d, 4p, 5s, 4d, 5p, 6s, 4f, 5d, 6p, 7s, 5f, 6d, 7p.
- **Hund's rules** determine ground-state spin and orbital configurations: maximize total spin $S$, then total $L$; for $J$, less than half-filled shells have $J = |L - S|$, more than half-filled $J = L + S$.
- The structure of the **periodic table** follows: periods correspond to filling shells; groups share valence configurations; shell capacities $2n^2$ (2, 8, 18, 32) and subshell capacities $2(2\ell + 1)$ (s: 2, p: 6, d: 10, f: 14) explain the block structure.

See the chemistry documents on atomic structure for details.

## 8. Summary

| Concept | Formula |
|---|---|
| Angular momentum algebra | $[\hat L_i, \hat L_j] = i\hbar\epsilon_{ijk}\hat L_k$ |
| Eigenvalues | $L^2 = \hbar^2\ell(\ell+1)$; $L_z = m\hbar$, $\lvert m\rvert \le \ell$ |
| Hydrogen energies | $E_n = -13.6\text{ eV}/n^2$ |
| Degeneracy | $n^2$ (×2 with spin) |
| Bohr radius | $a_0 = 4\pi\varepsilon_0\hbar^2/(m_ee^2) = 0.0529$ nm |
| Ground state | $\psi_{100} = e^{-r/a_0}/\sqrt{\pi a_0^3}$ |
| Selection rules | $\Delta\ell = \pm1$, $\Delta m = 0, \pm1$ |
| Spin-½ | $\hat S_i = \frac\hbar2\sigma_i$; $S_z = \pm\hbar/2$ |
| Electron $g$-factor | $g_s \approx 2.00232$ |
| Bohr magneton | $\mu_B = e\hbar/(2m_e) = 9.274\times10^{-24}$ J/T |
| Adding angular momenta | $j = \lvert j_1 - j_2\rvert, \ldots, j_1 + j_2$ |
| Singlet | $(\vert\uparrow\downarrow\rangle - \vert\downarrow\uparrow\rangle)/\sqrt2$ |
| Fine-structure constant | $\alpha \approx 1/137.036$ |
| Hydrogen 21 cm line | 1420.406 MHz |
