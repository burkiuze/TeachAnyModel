---
title: The Wavefunction and the Schrödinger Equation
field: Physics
subfield: Quantum Mechanics
level: undergraduate
keywords: [wavefunction, Schrödinger equation, Born rule, probability density, normalization, probability current, expectation value, momentum operator, Hamiltonian, time-independent Schrödinger equation, stationary states, separation of variables, superposition, wave packet, Ehrenfest theorem, boundary conditions, free particle]
---

# The Wavefunction and the Schrödinger Equation

In classical mechanics the state of a particle is its position and momentum; Newton's second law predicts how they change. In quantum mechanics the state is a **wavefunction** $\Psi(\vec r, t)$, and the **Schrödinger equation** predicts how it changes. The wavefunction does not tell us where the particle *is*, but the probabilities of where it will be *found*.

## 1. The Wavefunction

For a single particle in one dimension, the state is described by a complex-valued function $\Psi(x, t)$.

### The Born rule
$$\boxed{P(x, t)\,dx = |\Psi(x, t)|^2dx = \Psi^*\Psi\,dx}$$
is the probability of finding the particle between $x$ and $x + dx$ at time $t$ if its position is measured. $|\Psi|^2$ is the **probability density** (units of 1/length in 1D). The wavefunction itself is a **probability amplitude**; it is complex and not directly observable.

The probability of finding the particle between $a$ and $b$:
$$P_{ab} = \int_a^b|\Psi(x, t)|^2dx$$

### Normalization
The particle must be somewhere:
$$\int_{-\infty}^{\infty}|\Psi(x, t)|^2dx = 1$$
Any square-integrable function can be normalized by multiplying by a constant. The Schrödinger equation preserves normalization over time (as we show below), so normalizing once suffices.

**Global phase:** $\Psi$ and $e^{i\alpha}\Psi$ (with constant real $\alpha$) describe the same physical state, since all probabilities are unchanged. *Relative* phases between components of a superposition, however, are physically meaningful — they produce interference.

### Requirements on physical wavefunctions
1. Single-valued.
2. Square-integrable (normalizable) — though idealized non-normalizable states such as plane waves are useful.
3. Continuous everywhere.
4. Its derivative $\partial\Psi/\partial x$ is continuous wherever the potential is finite.

### Example: normalizing a Gaussian
$\Psi(x) = Ae^{-x^2/(2\sigma^2)}$. Then $\int|A|^2e^{-x^2/\sigma^2}dx = |A|^2\sigma\sqrt\pi = 1$, so $A = (\pi\sigma^2)^{-1/4}$.

## 2. The Time-Dependent Schrödinger Equation

In 1926 Erwin Schrödinger postulated the equation governing the evolution of $\Psi$. For a particle of mass $m$ in a potential $V(x, t)$:
$$\boxed{i\hbar\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\frac{\partial^2\Psi}{\partial x^2} + V(x, t)\Psi}$$
In three dimensions:
$$i\hbar\frac{\partial\Psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\Psi + V\Psi \qquad\text{or compactly}\qquad i\hbar\frac{\partial\Psi}{\partial t} = \hat H\Psi$$
where the **Hamiltonian operator** is $\hat H = \frac{\hat p^2}{2m} + V = -\frac{\hbar^2}{2m}\nabla^2 + V$.

### Motivation (not a derivation)
The Schrödinger equation is a postulate, justified by its agreement with experiment. It can be motivated as follows. A free particle with definite momentum $p = \hbar k$ and energy $E = \hbar\omega$ (de Broglie and Planck–Einstein relations) should be a plane wave $\Psi = Ae^{i(kx - \omega t)}$. Then
$$-i\hbar\frac{\partial}{\partial x}\Psi = \hbar k\Psi = p\Psi, \qquad i\hbar\frac{\partial}{\partial t}\Psi = \hbar\omega\Psi = E\Psi$$
Replacing $p \to -i\hbar\partial_x$ and $E \to i\hbar\partial_t$ in the classical energy relation $E = \frac{p^2}{2m} + V$ yields the Schrödinger equation.

### Key properties
1. **First order in time:** knowing $\Psi(x, 0)$ determines $\Psi(x, t)$ for all later times. The evolution is **deterministic** — randomness enters only at measurement.
2. **Linear:** if $\Psi_1$ and $\Psi_2$ are solutions, so is $c_1\Psi_1 + c_2\Psi_2$. This is the **superposition principle**, the root of interference and entanglement.
3. **Complex:** the $i$ is essential; solutions are necessarily complex.
4. **Unitary:** the total probability is conserved.
5. **Non-relativistic:** it treats space and time asymmetrically. Relativistic generalizations are the Klein–Gordon equation (spin 0) and the Dirac equation (spin ½).

## 3. Conservation of Probability and the Probability Current

Differentiate the probability density and use the Schrödinger equation and its complex conjugate:
$$\frac{\partial|\Psi|^2}{\partial t} = \frac{i\hbar}{2m}\left(\Psi^*\frac{\partial^2\Psi}{\partial x^2} - \Psi\frac{\partial^2\Psi^*}{\partial x^2}\right) = -\frac{\partial j}{\partial x}$$
(the potential terms cancel because $V$ is real). The **probability current** is
$$\boxed{j(x, t) = \frac{\hbar}{2mi}\left(\Psi^*\frac{\partial\Psi}{\partial x} - \Psi\frac{\partial\Psi^*}{\partial x}\right) = \frac\hbar m\text{Im}\left(\Psi^*\frac{\partial\Psi}{\partial x}\right)}$$
This gives the **continuity equation** $\frac{\partial\rho}{\partial t} + \frac{\partial j}{\partial x} = 0$, exactly analogous to charge conservation. Probability flows like a fluid. Integrating over all space with $\Psi \to 0$ at infinity shows $\frac{d}{dt}\int|\Psi|^2dx = 0$.

For a plane wave $Ae^{ikx}$: $j = |A|^2\frac{\hbar k}{m} = |A|^2v$ — density times velocity, as expected. The probability current is essential for computing reflection and transmission coefficients in scattering problems.

## 4. Expectation Values and Operators

### Expectation value of position
The **expectation value** is the average of many measurements on identically prepared systems (not the average of repeated measurements on one system, since measurement changes the state):
$$\langle x\rangle = \int_{-\infty}^\infty x|\Psi(x, t)|^2dx$$

### Momentum
Momentum cannot be computed as $\int p|\Psi|^2dx$ because $\Psi(x)$ does not specify momentum as a function of position. Instead, one finds (from $m\,d\langle x\rangle/dt$):
$$\langle p\rangle = \int\Psi^*\left(-i\hbar\frac{\partial}{\partial x}\right)\Psi\,dx$$
In quantum mechanics, observables are represented by **operators**:

| Observable | Operator (position representation) |
|---|---|
| Position $x$ | $\hat x = x$ |
| Momentum $p$ | $\hat p = -i\hbar\dfrac{\partial}{\partial x}$ (3D: $-i\hbar\nabla$) |
| Kinetic energy $T$ | $\hat T = -\dfrac{\hbar^2}{2m}\dfrac{\partial^2}{\partial x^2}$ |
| Potential energy $V$ | $V(x)$ |
| Total energy (Hamiltonian) | $\hat H = \hat T + V$ |
| Angular momentum $\vec L$ | $\hat{\vec L} = \hat{\vec r}\times\hat{\vec p} = -i\hbar\,\vec r\times\nabla$ |

General rule: $\langle Q\rangle = \int\Psi^*\hat Q\Psi\,dx$.

### Standard deviation (uncertainty)
$$\sigma_Q = \sqrt{\langle Q^2\rangle - \langle Q\rangle^2}$$

### Ehrenfest's theorem
Expectation values obey classical-looking equations:
$$\frac{d\langle x\rangle}{dt} = \frac{\langle p\rangle}{m}, \qquad \frac{d\langle p\rangle}{dt} = -\left\langle\frac{\partial V}{\partial x}\right\rangle$$
This is how classical mechanics emerges: for a narrow wave packet in a slowly varying potential, $\langle\partial V/\partial x\rangle \approx \partial V(\langle x\rangle)/\partial x$, and the packet's center moves along the classical trajectory. (For harmonic and linear potentials the correspondence is exact.)

## 5. The Time-Independent Schrödinger Equation

When the potential does not depend on time, $V = V(x)$, we look for **separable solutions** $\Psi(x, t) = \psi(x)\varphi(t)$. Substituting and dividing by $\psi\varphi$:
$$i\hbar\frac{1}{\varphi}\frac{d\varphi}{dt} = \frac1\psi\left[-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V\psi\right] = E$$
The left side depends only on $t$, the right only on $x$, so both equal a constant, which we call $E$. The time part gives $\varphi(t) = e^{-iEt/\hbar}$, and the spatial part gives the **time-independent Schrödinger equation (TISE)**:
$$\boxed{-\frac{\hbar^2}{2m}\frac{d^2\psi}{dx^2} + V(x)\psi = E\psi}, \qquad \hat H\psi = E\psi$$

This is an **eigenvalue equation**: $\psi$ is an **eigenfunction** of the Hamiltonian, and $E$ is the energy **eigenvalue**. Boundary conditions (normalizability, continuity) typically allow solutions only for specific values of $E$ — this is the mathematical origin of **energy quantization**. Quantization is not an extra postulate; it arises just as a guitar string can only vibrate at discrete frequencies.

### Stationary states
The separable solutions $\Psi_n(x, t) = \psi_n(x)e^{-iE_nt/\hbar}$ are **stationary states**:
- Their probability density $|\Psi_n|^2 = |\psi_n|^2$ is time-independent.
- All expectation values are constant in time (and $\langle p\rangle = 0$ for bound states).
- They have **definite energy**: every energy measurement yields $E_n$, with $\sigma_H = 0$.

### General solution
Because the equation is linear, the general solution is a superposition of stationary states:
$$\boxed{\Psi(x, t) = \sum_n c_n\psi_n(x)e^{-iE_nt/\hbar}}$$
The coefficients are found from the initial state using orthonormality of the eigenfunctions ($\int\psi_m^*\psi_n\,dx = \delta_{mn}$):
$$c_n = \int\psi_n^*(x)\Psi(x, 0)\,dx$$
**Interpretation:** $|c_n|^2$ is the probability that an energy measurement yields $E_n$, with $\sum|c_n|^2 = 1$ and $\langle H\rangle = \sum|c_n|^2E_n$.

A superposition of states with different energies is **not** stationary: $|\Psi|^2$ oscillates at the **Bohr frequencies** $\omega_{mn} = (E_m - E_n)/\hbar$. This is how quantum systems "move", and it connects to the frequencies of emitted light in atomic transitions.

### Properties of bound-state solutions in 1D
1. **Energy must exceed the minimum of $V$** — otherwise $\psi$ and $\psi''$ have the same sign everywhere and $\psi$ cannot be normalized.
2. **Bound states are non-degenerate in 1D** (each energy has one eigenfunction, up to a constant).
3. **The $n$-th eigenfunction has $n - 1$ nodes** (zeros, excluding the boundaries) — the node theorem. The ground state has no nodes.
4. **Real eigenfunctions:** for real $V$, eigenfunctions can always be chosen real.
5. **Parity:** if $V(x) = V(-x)$, eigenfunctions can be chosen even or odd; in 1D they alternate even, odd, even, ...
6. In classically allowed regions ($E > V$), $\psi$ oscillates (curving toward the axis); in classically forbidden regions ($E < V$), $\psi$ decays or grows exponentially. A particle has nonzero probability of being found in classically forbidden regions — the basis of tunneling.

## 6. The Free Particle and Wave Packets

For $V = 0$, the TISE gives $\psi_k(x) = e^{ikx}$ with $E = \frac{\hbar^2k^2}{2m}$, any real $k$. The stationary states are plane waves
$$\Psi_k(x, t) = e^{i(kx - \hbar k^2t/2m)}$$
They are **not normalizable** — a particle with perfectly definite momentum has completely undefined position — so they do not represent physical states on their own. Physical free particles are **wave packets**, superpositions of plane waves:
$$\Psi(x, t) = \frac{1}{\sqrt{2\pi}}\int_{-\infty}^\infty\phi(k)e^{i(kx - \hbar k^2t/2m)}dk, \qquad \phi(k) = \frac{1}{\sqrt{2\pi}}\int\Psi(x, 0)e^{-ikx}dx$$
$\phi(k)$ is the Fourier transform of the initial wavefunction; $|\phi(k)|^2$ is the probability density in $k$ (momentum $p = \hbar k$) space.

### Phase vs. group velocity
The dispersion relation $\omega = \hbar k^2/(2m)$ gives
$$v_{\text{phase}} = \frac\omega k = \frac{\hbar k}{2m} = \frac v2, \qquad v_{\text{group}} = \frac{d\omega}{dk} = \frac{\hbar k}{m} = v_{\text{classical}}$$
The packet as a whole moves at the classical velocity.

### Spreading of a Gaussian packet
A free Gaussian wave packet with initial width $\sigma_0$ spreads over time:
$$\sigma(t) = \sigma_0\sqrt{1 + \left(\frac{\hbar t}{2m\sigma_0^2}\right)^2}$$
The narrower the initial packet, the faster it spreads (larger momentum spread). An electron localized to 1 Å has a velocity spread of about $6\times10^5$ m/s and spreads to ~1 cm in under 20 nanoseconds; a 1 g ball localized to 1 μm would take longer than the age of the universe to spread noticeably.

### Position–momentum Fourier relationship
Position and momentum wavefunctions are Fourier transforms of each other: $\phi(p) = \frac{1}{\sqrt{2\pi\hbar}}\int\psi(x)e^{-ipx/\hbar}dx$. A narrow function in $x$ has a broad transform in $p$, and vice versa — the mathematical root of the **Heisenberg uncertainty principle** $\sigma_x\sigma_p \ge \hbar/2$. Gaussians achieve the minimum.

## 7. Boundary Conditions at Potential Discontinuities

When solving the TISE piecewise (e.g. for step potentials):
1. $\psi$ is always continuous.
2. $d\psi/dx$ is continuous where $V$ is finite (even if $V$ jumps).
3. At an infinite potential wall, $\psi = 0$ (and $d\psi/dx$ may be discontinuous).
4. For a delta-function potential $V = -\alpha\delta(x)$, $d\psi/dx$ jumps by $-\frac{2m\alpha}{\hbar^2}\psi(0)$.

## 8. Worked Example: Expectation Values in a Superposition

**Problem:** A particle in an infinite square well of width $a$ (eigenfunctions $\psi_n = \sqrt{2/a}\sin(n\pi x/a)$, energies $E_n = n^2E_1$) starts in the state $\Psi(x, 0) = \frac{1}{\sqrt2}(\psi_1 + \psi_2)$. Find $\Psi(x, t)$, the probability density, and $\langle H\rangle$.

**Solution:**
$$\Psi(x, t) = \frac{1}{\sqrt2}\left(\psi_1e^{-iE_1t/\hbar} + \psi_2e^{-iE_2t/\hbar}\right)$$
$$|\Psi|^2 = \frac12\left[\psi_1^2 + \psi_2^2 + 2\psi_1\psi_2\cos\left(\frac{(E_2 - E_1)t}{\hbar}\right)\right]$$
The probability density sloshes back and forth in the well at angular frequency $\omega = (E_2 - E_1)/\hbar = 3E_1/\hbar$.
Energy measurements give $E_1$ or $E_2$, each with probability ½. $\langle H\rangle = \frac12(E_1 + 4E_1) = \frac52E_1$ — a value that is never obtained in any single measurement.
One can show $\langle x\rangle = \frac a2 - \frac{16a}{9\pi^2}\cos\left(\frac{3E_1t}{\hbar}\right)$, oscillating with amplitude about $0.18a$.

## 9. Interpretation Notes

- The wavefunction is a complete description of the state according to standard quantum mechanics, but it encodes probabilities, not certainties.
- Before measurement, a particle in a superposition does not have a definite position (in the standard interpretation) — it is not merely that we don't know it. The **Bell inequality** experiments rule out a broad class of "hidden" definite values (local hidden variables).
- Upon measurement, the outcome is random, with probabilities given by the Born rule, and the wavefunction is updated ("collapses") to be consistent with the outcome. How and whether collapse happens physically — the **measurement problem** — is a matter of interpretation (Copenhagen, many-worlds, pilot-wave/Bohmian mechanics, objective collapse, QBism, and others), all of which make the same predictions for standard experiments.

## 10. Summary

| Concept | Formula |
|---|---|
| Born rule | $P(x)dx = \lvert\Psi\rvert^2dx$ |
| Normalization | $\int\lvert\Psi\rvert^2dx = 1$ |
| TDSE | $i\hbar\,\partial_t\Psi = \hat H\Psi$ |
| Hamiltonian | $\hat H = -\frac{\hbar^2}{2m}\nabla^2 + V$ |
| TISE | $\hat H\psi = E\psi$ |
| Stationary state | $\Psi_n = \psi_ne^{-iE_nt/\hbar}$ |
| General solution | $\Psi = \sum c_n\psi_ne^{-iE_nt/\hbar}$, $c_n = \langle\psi_n\vert\Psi(0)\rangle$ |
| Momentum operator | $\hat p = -i\hbar\,\partial_x$ |
| Expectation value | $\langle Q\rangle = \int\Psi^*\hat Q\Psi\,dx$ |
| Probability current | $j = \frac\hbar m\text{Im}(\Psi^*\partial_x\Psi)$ |
| Ehrenfest | $d\langle p\rangle/dt = -\langle\partial_xV\rangle$ |
| Free-particle energy | $E = \hbar^2k^2/2m$ |
| Gaussian spreading | $\sigma(t) = \sigma_0\sqrt{1 + (\hbar t/2m\sigma_0^2)^2}$ |
