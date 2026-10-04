---
title: Formalism of Quantum Mechanics - Postulates, Hilbert Space, Operators and the Uncertainty Principle
field: Physics
subfield: Quantum Mechanics
level: undergraduate to graduate
keywords: [Hilbert space, Dirac notation, bra-ket, inner product, Hermitian operator, eigenvalues, eigenvectors, observables, completeness, spectral theorem, measurement postulate, wavefunction collapse, commutator, canonical commutation relation, uncertainty principle, Robertson relation, energy-time uncertainty, unitary time evolution, Schrödinger picture, Heisenberg picture, density matrix, mixed states]
---

# Formalism of Quantum Mechanics: Postulates, Hilbert Space, Operators and the Uncertainty Principle

Wave mechanics (Schrödinger) and matrix mechanics (Heisenberg) turned out to be two representations of a single abstract structure: vectors in a complex vector space called a **Hilbert space**, acted on by **linear operators**. Paul Dirac's bra–ket notation makes this structure elegant and representation-independent. This framework is what quantum computing, quantum chemistry and quantum field theory are built on.

## 1. Hilbert Space and Dirac Notation

### State vectors
The state of a quantum system is a vector $|\psi\rangle$ ("ket") in a complex Hilbert space $\mathcal H$. Hilbert spaces can be:
- **Finite-dimensional:** spin of an electron (2D), a qubit (2D), polarization of a photon (2D), $n$ qubits ($2^n$-dimensional).
- **Infinite-dimensional:** a particle moving in space; the space of square-integrable functions $L^2$.

### Bras and inner products
Each ket has a dual "bra" $\langle\psi|$. The **inner product** $\langle\phi|\psi\rangle$ is a complex number with properties:
- $\langle\phi|\psi\rangle = \langle\psi|\phi\rangle^*$
- Linear in the ket: $\langle\phi|(a|\psi_1\rangle + b|\psi_2\rangle) = a\langle\phi|\psi_1\rangle + b\langle\phi|\psi_2\rangle$
- $\langle\psi|\psi\rangle \ge 0$, with equality only for the zero vector.

**Physical states are normalized:** $\langle\psi|\psi\rangle = 1$. Kets differing by a global phase represent the same physical state (strictly, states are rays in Hilbert space).

**Connection to wavefunctions:** $\psi(x) = \langle x|\psi\rangle$, and
$$\langle\phi|\psi\rangle = \int_{-\infty}^\infty\phi^*(x)\psi(x)\,dx$$
For column vectors in finite dimensions: $\langle\phi|\psi\rangle = \sum_i\phi_i^*\psi_i$ — the bra is the conjugate transpose of the ket.

### Bases and completeness
An **orthonormal basis** $\{|n\rangle\}$ satisfies $\langle m|n\rangle = \delta_{mn}$. Any state can be expanded:
$$|\psi\rangle = \sum_nc_n|n\rangle, \qquad c_n = \langle n|\psi\rangle$$
The **completeness relation** (resolution of the identity):
$$\sum_n|n\rangle\langle n| = \hat 1 \qquad\text{(continuous: } \int|x\rangle\langle x|\,dx = \hat 1\text{)}$$
Inserting the identity is the single most useful trick in quantum mechanics. For continuous bases, orthonormality becomes $\langle x|x'\rangle = \delta(x - x')$ (Dirac delta).

### Outer products and projectors
$|\phi\rangle\langle\psi|$ is an operator. The **projector** onto a normalized state, $\hat P_n = |n\rangle\langle n|$, satisfies $\hat P_n^2 = \hat P_n$.

## 2. Operators

A **linear operator** $\hat A$ maps kets to kets: $\hat A(a|\psi\rangle + b|\phi\rangle) = a\hat A|\psi\rangle + b\hat A|\phi\rangle$. In a basis it is a matrix: $A_{mn} = \langle m|\hat A|n\rangle$.

### Hermitian conjugate (adjoint)
$\hat A^\dagger$ is defined by $\langle\phi|\hat A^\dagger|\psi\rangle = \langle\psi|\hat A|\phi\rangle^*$. As a matrix, $A^\dagger = (A^T)^*$. Properties: $(\hat A\hat B)^\dagger = \hat B^\dagger\hat A^\dagger$; $(c\hat A)^\dagger = c^*\hat A^\dagger$.

### Hermitian (self-adjoint) operators
$\hat A^\dagger = \hat A$. **Observables are represented by Hermitian operators**, because Hermitian operators have:
1. **Real eigenvalues** (measurement results are real numbers).
2. **Orthogonal eigenvectors** for distinct eigenvalues.
3. A **complete** set of eigenvectors (spectral theorem; for infinite dimensions, with appropriate technical conditions): $\hat A = \sum_na_n|a_n\rangle\langle a_n|$.

**Proof of (1):** if $\hat A|a\rangle = a|a\rangle$, then $\langle a|\hat A|a\rangle = a\langle a|a\rangle$. For Hermitian $\hat A$, $\langle a|\hat A|a\rangle = \langle a|\hat A^\dagger|a\rangle = \langle a|\hat A|a\rangle^*$, so this quantity is real; since $\langle a|a\rangle > 0$ is real, $a = a^*$.

**Proof of (2):** $\langle a'|\hat A|a\rangle = a\langle a'|a\rangle$ and also $= a'\langle a'|a\rangle$ (acting to the left with the real eigenvalue $a'$). So $(a - a')\langle a'|a\rangle = 0$; if $a \ne a'$, $\langle a'|a\rangle = 0$.

**Is the momentum operator Hermitian?** $\hat p = -i\hbar\frac{d}{dx}$ includes an $i$, which is necessary: integrating by parts, $\int\phi^*(-i\hbar\psi')dx = \int(-i\hbar\phi')^*\psi\,dx$ (boundary terms vanish for normalizable functions). Without the $i$, $d/dx$ would be anti-Hermitian.

### Unitary operators
$\hat U^\dagger\hat U = \hat U\hat U^\dagger = \hat 1$. Unitary operators preserve inner products (probabilities) and represent time evolution, symmetry transformations (rotations, translations) and changes of basis. Every unitary can be written $\hat U = e^{i\hat K}$ with $\hat K$ Hermitian. In quantum computing, gates are unitary operators.

## 3. The Postulates of Quantum Mechanics

Standard textbook formulation (closed systems, pure states):

**Postulate 1 — State:** the state of an isolated physical system is completely described by a normalized vector $|\psi\rangle$ in a Hilbert space.

**Postulate 2 — Observables:** every measurable physical quantity $A$ is described by a Hermitian operator $\hat A$ acting on the Hilbert space.

**Postulate 3 — Measurement outcomes:** the only possible results of measuring $A$ are the eigenvalues $a_n$ of $\hat A$.

**Postulate 4 — Born rule:** if the system is in state $|\psi\rangle$, the probability of obtaining the (non-degenerate) eigenvalue $a_n$ is
$$P(a_n) = |\langle a_n|\psi\rangle|^2$$
For a degenerate eigenvalue, $P(a_n) = \langle\psi|\hat P_n|\psi\rangle$ where $\hat P_n$ projects onto its eigenspace. For continuous spectra, $|\langle a|\psi\rangle|^2$ is a probability density.

**Postulate 5 — State update (collapse):** immediately after a measurement yielding $a_n$, the state becomes the (normalized) projection of the previous state onto the eigenspace of $a_n$:
$$|\psi\rangle \to \frac{\hat P_n|\psi\rangle}{\sqrt{\langle\psi|\hat P_n|\psi\rangle}}$$
Repeating the same measurement immediately gives the same result with certainty.

**Postulate 6 — Time evolution:** between measurements, the state evolves according to the Schrödinger equation
$$i\hbar\frac{d}{dt}|\psi(t)\rangle = \hat H|\psi(t)\rangle$$

**Postulate 7 — Composite systems:** the Hilbert space of a composite system is the **tensor product** of the subsystems' spaces: $\mathcal H_{AB} = \mathcal H_A\otimes\mathcal H_B$. (This leads to entanglement.) For identical particles, the state must be symmetric (bosons) or antisymmetric (fermions) under exchange.

### Expectation values
$$\langle A\rangle = \langle\psi|\hat A|\psi\rangle = \sum_na_n|\langle a_n|\psi\rangle|^2$$

### Worked example 3.1 — Spin measurement
An electron's spin state is $|\psi\rangle = \frac{1}{\sqrt3}|\uparrow\rangle + \sqrt{\frac23}|\downarrow\rangle$ (eigenstates of $\hat S_z$ with eigenvalues $\pm\hbar/2$).
- $P(+\hbar/2) = 1/3$, $P(-\hbar/2) = 2/3$.
- $\langle S_z\rangle = \frac13\cdot\frac\hbar2 + \frac23\cdot\left(-\frac\hbar2\right) = -\frac\hbar6$.
- If the result is $+\hbar/2$, the state becomes $|\uparrow\rangle$; measuring $S_z$ again gives $+\hbar/2$ with certainty.

## 4. Commutators

The **commutator** of two operators is
$$[\hat A, \hat B] = \hat A\hat B - \hat B\hat A$$
Unlike numbers, operators generally do not commute — the order of operations matters.

**Useful identities:**
- $[\hat A, \hat B] = -[\hat B, \hat A]$
- $[\hat A, \hat B\hat C] = [\hat A, \hat B]\hat C + \hat B[\hat A, \hat C]$
- $[\hat A, [\hat B, \hat C]] + [\hat B, [\hat C, \hat A]] + [\hat C, [\hat A, \hat B]] = 0$ (Jacobi identity)
- $e^{\hat A}\hat Be^{-\hat A} = \hat B + [\hat A, \hat B] + \frac{1}{2!}[\hat A, [\hat A, \hat B]] + \cdots$ (Baker–Campbell–Hausdorff lemma)

### The canonical commutation relation
$$\boxed{[\hat x, \hat p] = i\hbar}$$
**Proof:** acting on a test function $f(x)$: $[\hat x, \hat p]f = x(-i\hbar f') - (-i\hbar)(xf)' = -i\hbar xf' + i\hbar(f + xf') = i\hbar f$.

In 3D: $[\hat x_i, \hat p_j] = i\hbar\delta_{ij}$; positions commute with each other, as do momenta.

This relation is arguably the defining feature of quantum mechanics. Dirac recognized it as the quantum counterpart of the classical Poisson bracket $\{x, p\} = 1$, via $\{A, B\} \to \frac{1}{i\hbar}[\hat A, \hat B]$.

Consequences: $[\hat x, \hat p^2] = 2i\hbar\hat p$; $[\hat p, f(\hat x)] = -i\hbar f'(\hat x)$; $[\hat x, g(\hat p)] = i\hbar g'(\hat p)$.

### Compatible observables
Two observables are **compatible** if their operators commute, $[\hat A, \hat B] = 0$. Then:
- They have a common set of eigenvectors (a simultaneous eigenbasis).
- They can be simultaneously measured with arbitrary precision; measuring one does not disturb the other's value.

A **complete set of commuting observables (CSCO)** uniquely labels each basis state. For the hydrogen atom (ignoring spin), $\{\hat H, \hat L^2, \hat L_z\}$ labels states by quantum numbers $(n, \ell, m)$.

**Incompatible observables** ($[\hat A, \hat B] \ne 0$) cannot in general have simultaneously definite values: $x$ and $p_x$; $L_x$ and $L_y$; $S_x$ and $S_z$.

## 5. The Uncertainty Principle

### The Robertson uncertainty relation
For any two observables and any state:
$$\boxed{\sigma_A\sigma_B \ge \frac12\left|\langle[\hat A, \hat B]\rangle\right|}$$

**Proof sketch:** define $\hat a = \hat A - \langle A\rangle$, $\hat b = \hat B - \langle B\rangle$, and $|f\rangle = \hat a|\psi\rangle$, $|g\rangle = \hat b|\psi\rangle$. Then $\sigma_A^2 = \langle f|f\rangle$, $\sigma_B^2 = \langle g|g\rangle$. By the Cauchy–Schwarz inequality, $\sigma_A^2\sigma_B^2 \ge |\langle f|g\rangle|^2 \ge (\text{Im}\langle f|g\rangle)^2 = \left(\frac{1}{2i}\langle[\hat A, \hat B]\rangle\right)^2$.

### Heisenberg's position–momentum uncertainty
With $[\hat x, \hat p] = i\hbar$:
$$\boxed{\sigma_x\sigma_p \ge \frac\hbar2}$$

**What it means:** it is a statement about the **state**, not about measurement clumsiness. No quantum state has both a sharply defined position and a sharply defined momentum. Heisenberg's original "microscope" argument (the photon used to observe an electron disturbs its momentum) captures the flavor, but the principle is more fundamental: it follows from the wave nature of matter and the Fourier relationship between position and momentum representations.

The equality holds only for **Gaussian** wave packets (minimum-uncertainty states), such as the ground state of the harmonic oscillator and coherent states.

### Applications and estimates
1. **Size and stability of atoms:** confining an electron within radius $r$ gives momentum $p \gtrsim \hbar/r$ and kinetic energy $\sim\frac{\hbar^2}{2mr^2}$. Total energy $E(r) \approx \frac{\hbar^2}{2mr^2} - \frac{ke^2}{r}$ is minimized at $r = \frac{\hbar^2}{mke^2} = a_0$ (the Bohr radius), giving $E = -13.6$ eV. The uncertainty principle prevents the electron from collapsing into the nucleus.
2. **Zero-point energy:** a confined particle cannot be at rest. The harmonic oscillator has minimum energy $\frac12\hbar\omega$, not zero. Helium stays liquid at absolute zero (at atmospheric pressure) because zero-point motion prevents it from solidifying.
3. **Electrons cannot be confined in nuclei:** confining an electron to ~10⁻¹⁴ m would require momentum ~20 MeV/c and kinetic energy ~20 MeV (relativistic), far exceeding typical nuclear binding — historical evidence (with others) that nuclei do not contain electrons.
4. **Single-slit diffraction:** a photon passing through a slit of width $a$ acquires transverse momentum uncertainty $\Delta p_y \sim \hbar/a$, so its angular spread is $\theta \sim \lambda/a$.

### Worked example 5.1
An electron is confined to a region of width 0.1 nm (atomic size). Minimum momentum uncertainty: $\sigma_p \ge \frac{\hbar}{2\sigma_x} = \frac{1.055\times10^{-34}}{2\times10^{-10}} \approx 5.3\times10^{-25}$ kg·m/s, corresponding to velocity uncertainty $\sim5.8\times10^5$ m/s and kinetic energy of order $\frac{\sigma_p^2}{2m} \approx 1$ eV — the scale of atomic energies.

For a 1 μg dust grain confined to 1 μm: $\sigma_v \ge 5.3\times10^{-20}$ m/s — utterly negligible.

### Energy–time uncertainty
$$\Delta E\,\Delta t \gtrsim \frac\hbar2$$
This is **not** a Robertson relation (time is a parameter, not an operator in non-relativistic QM). Its precise meaning (Mandelstam–Tamm): $\Delta t$ is the time for the expectation value of some observable to change by one standard deviation. Consequences:
- **Natural linewidth:** an excited state with lifetime $\tau$ has an energy spread $\Gamma \approx \hbar/\tau$, broadening spectral lines. Unstable particles have mass widths inversely proportional to their lifetimes (the Z boson's width of 2.5 GeV corresponds to a lifetime of ~$3\times10^{-25}$ s).
- **Virtual particles:** the range of a force carried by a massive particle is ~$\hbar/(mc)$. Yukawa (1935) used this to predict the pion mass (~140 MeV/c²) from the ~1.4 fm range of the nuclear force.
- **Short laser pulses** necessarily have broad frequency spectra.

## 6. Time Evolution

### The time-evolution operator
For a time-independent Hamiltonian, the solution of the Schrödinger equation is
$$|\psi(t)\rangle = \hat U(t)|\psi(0)\rangle, \qquad \boxed{\hat U(t) = e^{-i\hat Ht/\hbar}}$$
$\hat U$ is unitary (since $\hat H$ is Hermitian), so total probability is conserved. Expanding in energy eigenstates:
$$|\psi(t)\rangle = \sum_nc_ne^{-iE_nt/\hbar}|E_n\rangle$$

### Schrödinger and Heisenberg pictures
- **Schrödinger picture:** states evolve, $|\psi(t)\rangle = \hat U|\psi(0)\rangle$; operators are fixed.
- **Heisenberg picture:** states are fixed; operators evolve, $\hat A_H(t) = \hat U^\dagger\hat A\hat U$, obeying the **Heisenberg equation of motion**:
$$\frac{d\hat A_H}{dt} = \frac{i}{\hbar}[\hat H, \hat A_H] + \left(\frac{\partial\hat A}{\partial t}\right)_H$$
Both give identical predictions: $\langle\psi(t)|\hat A|\psi(t)\rangle = \langle\psi(0)|\hat A_H(t)|\psi(0)\rangle$.
- **Interaction (Dirac) picture:** a hybrid used in perturbation theory and quantum field theory.

**Conservation laws:** an observable with no explicit time dependence is conserved if and only if it commutes with the Hamiltonian: $[\hat H, \hat A] = 0 \Rightarrow \frac{d\langle A\rangle}{dt} = 0$. This is the quantum version of Noether's theorem: symmetries (unitary operators commuting with $\hat H$) correspond to conserved quantities (their Hermitian generators). Momentum generates translations ($\hat T(a) = e^{-i\hat pa/\hbar}$), angular momentum generates rotations, and the Hamiltonian generates time evolution.

## 7. Position and Momentum Representations

- Position eigenstates: $\hat x|x\rangle = x|x\rangle$; wavefunction $\psi(x) = \langle x|\psi\rangle$.
- Momentum eigenstates: $\hat p|p\rangle = p|p\rangle$; in position space, $\langle x|p\rangle = \frac{1}{\sqrt{2\pi\hbar}}e^{ipx/\hbar}$ (plane waves).
- Momentum-space wavefunction: $\phi(p) = \langle p|\psi\rangle = \frac{1}{\sqrt{2\pi\hbar}}\int e^{-ipx/\hbar}\psi(x)\,dx$.
- In momentum representation, $\hat p = p$ and $\hat x = i\hbar\frac{\partial}{\partial p}$.

Neither $|x\rangle$ nor $|p\rangle$ is normalizable; they are idealized limits (formally handled with rigged Hilbert spaces).

## 8. Mixed States and the Density Matrix

A **pure state** $|\psi\rangle$ represents maximal knowledge. When we have only statistical knowledge — an ensemble with probability $p_i$ of being in $|\psi_i\rangle$, or a subsystem of an entangled system — we use the **density operator**:
$$\hat\rho = \sum_ip_i|\psi_i\rangle\langle\psi_i|$$
Properties: Hermitian, positive semidefinite, $\text{Tr}\,\hat\rho = 1$.
- Expectation values: $\langle A\rangle = \text{Tr}(\hat\rho\hat A)$.
- Pure state iff $\text{Tr}(\hat\rho^2) = 1$; mixed if $< 1$.
- Time evolution (von Neumann equation): $i\hbar\frac{d\hat\rho}{dt} = [\hat H, \hat\rho]$.
- Von Neumann entropy: $S = -k_B\text{Tr}(\hat\rho\ln\hat\rho)$; zero for pure states.
- Thermal equilibrium: $\hat\rho = \frac{e^{-\hat H/k_BT}}{Z}$, connecting to statistical mechanics.

**Coherent superposition vs. mixture:** $\frac{1}{\sqrt2}(|\uparrow\rangle + |\downarrow\rangle)$ is a pure state (spin pointing along $+x$; measuring $S_x$ gives $+\hbar/2$ with certainty). A 50/50 mixture of $|\uparrow\rangle$ and $|\downarrow\rangle$ gives random $S_x$ results. They agree on $S_z$ statistics but differ in off-diagonal elements ("coherences") of $\hat\rho$:
$$\rho_{\text{pure}} = \frac12\begin{pmatrix}1 & 1\\ 1 & 1\end{pmatrix}, \qquad \rho_{\text{mixed}} = \frac12\begin{pmatrix}1 & 0\\ 0 & 1\end{pmatrix}$$
**Decoherence** — interaction with an environment — destroys off-diagonal elements, turning superpositions into effective mixtures. It explains why macroscopic superpositions are never observed, though by itself it does not select a single outcome.

## 9. Summary

| Concept | Formula |
|---|---|
| Inner product | $\langle\phi\vert\psi\rangle = \int\phi^*\psi\,dx$ |
| Completeness | $\sum_n\vert n\rangle\langle n\vert = \hat 1$ |
| Hermitian | $\hat A^\dagger = \hat A$; real eigenvalues |
| Unitary | $\hat U^\dagger\hat U = \hat 1$ |
| Born rule | $P(a_n) = \lvert\langle a_n\vert\psi\rangle\rvert^2$ |
| Expectation | $\langle A\rangle = \langle\psi\vert\hat A\vert\psi\rangle$ |
| Commutator | $[\hat A, \hat B] = \hat A\hat B - \hat B\hat A$ |
| Canonical | $[\hat x, \hat p] = i\hbar$ |
| Robertson | $\sigma_A\sigma_B \ge \frac12\lvert\langle[\hat A, \hat B]\rangle\rvert$ |
| Heisenberg | $\sigma_x\sigma_p \ge \hbar/2$ |
| Energy–time | $\Delta E\,\Delta t \gtrsim \hbar/2$ |
| Time evolution | $\hat U = e^{-i\hat Ht/\hbar}$ |
| Heisenberg equation | $d\hat A/dt = (i/\hbar)[\hat H, \hat A]$ |
| Density matrix | $\hat\rho = \sum p_i\vert\psi_i\rangle\langle\psi_i\vert$; $\langle A\rangle = \text{Tr}(\hat\rho\hat A)$ |
