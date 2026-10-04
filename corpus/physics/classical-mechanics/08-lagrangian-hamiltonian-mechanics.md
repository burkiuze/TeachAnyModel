---
title: Lagrangian and Hamiltonian Mechanics
field: Physics
subfield: Classical Mechanics
level: undergraduate to graduate
keywords: [Lagrangian, Hamiltonian, principle of least action, Euler-Lagrange equation, generalized coordinates, constraints, Noether's theorem, conjugate momentum, cyclic coordinate, phase space, Poisson bracket, Hamilton's equations, Liouville's theorem, canonical transformation]
---

# Lagrangian and Hamiltonian Mechanics

Newton's laws are formulated in terms of forces and vectors in Cartesian coordinates. For systems with constraints (a bead on a wire, a double pendulum, a rolling sphere) or with many degrees of freedom, this becomes cumbersome. In the 18th and 19th centuries, Euler, Lagrange, Hamilton and others reformulated mechanics in terms of **energy** and a **variational principle**. These "analytical mechanics" formulations are equivalent to Newton's laws for classical systems, but they:
- work in any coordinate system,
- automatically handle constraint forces,
- make the connection between symmetries and conservation laws transparent (Noether's theorem),
- and form the direct foundation of quantum mechanics, statistical mechanics and field theory.

## 1. Generalized Coordinates and Constraints

A system of $N$ particles in 3D has $3N$ Cartesian coordinates. **Constraints** reduce the number of independent coordinates. The number of independent coordinates needed to specify the configuration is the number of **degrees of freedom** $n$.

- A simple pendulum in a plane: 2 Cartesian coordinates $(x, y)$, one constraint $x^2 + y^2 = L^2$ → 1 degree of freedom, the angle $\theta$.
- A rigid body: 6 degrees of freedom (3 translations, 3 rotations).
- A double pendulum: 2 degrees of freedom $(\theta_1, \theta_2)$.

**Generalized coordinates** $q_1, \ldots, q_n$ are any set of independent parameters that specify the configuration. They need not have units of length (angles, for example). Their time derivatives $\dot q_i$ are **generalized velocities**.

**Holonomic constraints** can be written as equations among coordinates and time, $f(q, t) = 0$. Non-holonomic constraints (e.g. rolling without slipping in 2D, involving velocities that cannot be integrated) require extra techniques such as Lagrange multipliers.

## 2. The Lagrangian and Hamilton's Principle

The **Lagrangian** of a system is
$$\boxed{L(q, \dot q, t) = T - V}$$
the kinetic energy minus the potential energy, expressed in generalized coordinates.

The **action** is the time integral of the Lagrangian along a path $q(t)$ from time $t_1$ to $t_2$:
$$S[q] = \int_{t_1}^{t_2} L(q, \dot q, t)\,dt$$

**Hamilton's principle (principle of stationary action):** of all possible paths between fixed endpoints $q(t_1)$ and $q(t_2)$, the path actually followed makes the action **stationary** (usually a minimum, hence "least action"):
$$\delta S = 0$$

This is a profoundly different way of looking at motion: instead of a step-by-step causal law ("force causes acceleration"), the whole path is selected by a global principle. In quantum mechanics, Feynman's path-integral formulation shows how this arises: a particle explores all paths, each contributing a phase $e^{iS/\hbar}$; paths near the stationary one interfere constructively, and in the classical limit ($S \gg \hbar$) only they survive.

## 3. The Euler–Lagrange Equations

Requiring $\delta S = 0$ for arbitrary variations $\delta q(t)$ that vanish at the endpoints leads to:
$$\boxed{\frac{d}{dt}\left(\frac{\partial L}{\partial \dot q_i}\right) - \frac{\partial L}{\partial q_i} = 0, \qquad i = 1, \ldots, n}$$

### Derivation (one coordinate)
$$\delta S = \int_{t_1}^{t_2}\left(\frac{\partial L}{\partial q}\delta q + \frac{\partial L}{\partial\dot q}\delta\dot q\right)dt$$
Integrate the second term by parts using $\delta\dot q = \frac{d}{dt}\delta q$:
$$\int\frac{\partial L}{\partial\dot q}\frac{d}{dt}\delta q\,dt = \left[\frac{\partial L}{\partial\dot q}\delta q\right]_{t_1}^{t_2} - \int\frac{d}{dt}\left(\frac{\partial L}{\partial\dot q}\right)\delta q\,dt$$
The boundary term vanishes because $\delta q(t_1) = \delta q(t_2) = 0$. Hence
$$\delta S = \int_{t_1}^{t_2}\left[\frac{\partial L}{\partial q} - \frac{d}{dt}\frac{\partial L}{\partial\dot q}\right]\delta q\,dt = 0$$
for all $\delta q$, so the bracket must vanish (fundamental lemma of the calculus of variations).

### Check: recovering Newton's law
For a particle in 1D with potential $V(x)$: $L = \frac12 m\dot x^2 - V(x)$.
$\frac{\partial L}{\partial\dot x} = m\dot x$, $\frac{\partial L}{\partial x} = -V'(x)$.
Euler–Lagrange: $m\ddot x + V'(x) = 0$, i.e. $m\ddot x = F$. ✓

## 4. Worked Examples

### Example 4.1 – Simple pendulum
Coordinates: $x = L\sin\theta$, $y = -L\cos\theta$. Then
$T = \frac12 mL^2\dot\theta^2$, $V = -mgL\cos\theta$,
$$\mathcal{L} = \tfrac12 mL^2\dot\theta^2 + mgL\cos\theta$$
$\frac{\partial\mathcal L}{\partial\dot\theta} = mL^2\dot\theta$; $\frac{\partial\mathcal L}{\partial\theta} = -mgL\sin\theta$.
Equation of motion: $mL^2\ddot\theta + mgL\sin\theta = 0 \Rightarrow \ddot\theta = -\frac{g}{L}\sin\theta$.
The string tension never appeared — constraint forces that do no work drop out automatically.

### Example 4.2 – Particle in a central potential (polar coordinates)
$$L = \tfrac12 m(\dot r^2 + r^2\dot\phi^2) - V(r)$$
- $\phi$ equation: $\frac{d}{dt}(mr^2\dot\phi) = 0$ ⇒ angular momentum $\ell = mr^2\dot\phi$ is conserved (because $L$ does not depend on $\phi$).
- $r$ equation: $m\ddot r - mr\dot\phi^2 + V'(r) = 0$, i.e.
$$m\ddot r = -V'(r) + \frac{\ell^2}{mr^3}$$
The radial motion behaves like 1D motion in an **effective potential** $V_{\text{eff}}(r) = V(r) + \frac{\ell^2}{2mr^2}$, where the second term is the "centrifugal barrier". For gravity, $V = -GMm/r$, analysis of $V_{\text{eff}}$ shows bound elliptical orbits for $E < 0$ and reproduces Kepler's laws.

### Example 4.3 – Atwood machine
Masses $m_1$, $m_2$ connected over a pulley; if $m_1$ is at depth $x$ below the pulley, $m_2$ is at depth $\ell - x$.
$T = \frac12(m_1 + m_2)\dot x^2$, $V = -m_1gx - m_2g(\ell - x)$.
$\mathcal{L} = \frac12(m_1+m_2)\dot x^2 + (m_1 - m_2)gx + \text{const}$.
Euler–Lagrange: $(m_1 + m_2)\ddot x = (m_1 - m_2)g$. One line, no tension needed.

### Example 4.4 – Bead on a rotating hoop
A bead of mass $m$ slides without friction on a circular hoop of radius $R$ rotating about its vertical diameter at constant angular velocity $\Omega$. With $\theta$ measured from the bottom:
$$\mathcal L = \tfrac12 mR^2(\dot\theta^2 + \Omega^2\sin^2\theta) + mgR\cos\theta$$
Equation of motion: $\ddot\theta = \sin\theta\left(\Omega^2\cos\theta - \frac{g}{R}\right)$.
Equilibria: $\theta = 0$ (bottom) is stable if $\Omega^2 < g/R$. When $\Omega^2 > g/R$ the bottom becomes unstable and new stable equilibria appear at $\cos\theta_0 = g/(R\Omega^2)$. This is a simple example of a **bifurcation** and of **spontaneous symmetry breaking**: the system is symmetric under $\theta \to -\theta$, but the bead must pick one side.

## 5. Generalized Momentum, Cyclic Coordinates and Noether's Theorem

The **generalized (canonical) momentum** conjugate to $q_i$ is
$$p_i = \frac{\partial L}{\partial\dot q_i}$$
For Cartesian coordinates this is ordinary momentum $m\dot x$; for an angle, it is angular momentum. (In electromagnetism, the canonical momentum of a charged particle is $\vec p = m\vec v + q\vec A$, not just $m\vec v$.)

If $L$ does not depend on some coordinate $q_k$ (a **cyclic** or **ignorable** coordinate), then $\frac{\partial L}{\partial q_k} = 0$ and the Euler–Lagrange equation gives
$$\frac{dp_k}{dt} = 0 \Rightarrow p_k = \text{constant}$$

**Noether's theorem (Emmy Noether, 1918):** every continuous symmetry of the action corresponds to a conserved quantity.

| Symmetry | Conserved quantity |
|---|---|
| Translation in space ($L$ independent of position) | Linear momentum |
| Rotation in space ($L$ independent of orientation) | Angular momentum |
| Translation in time ($L$ has no explicit $t$ dependence) | Energy |
| Phase rotation of a quantum field ($\psi \to e^{i\alpha}\psi$) | Electric charge |

Noether's theorem is among the most important results in theoretical physics; it explains *why* conservation laws exist and guides the construction of modern theories such as the Standard Model of particle physics.

### Energy function
If $L$ has no explicit time dependence, the quantity
$$h = \sum_i \dot q_i\frac{\partial L}{\partial\dot q_i} - L$$
is conserved. When the kinetic energy is a quadratic form in the velocities and the coordinates don't depend explicitly on time, $h = T + V$, the total energy.

## 6. Hamiltonian Mechanics

### The Hamiltonian
Hamilton reformulated mechanics using coordinates $q_i$ and momenta $p_i$ as independent variables. The **Hamiltonian** is obtained from the Lagrangian by a **Legendre transformation**:
$$\boxed{H(q, p, t) = \sum_i p_i\dot q_i - L}$$
where every $\dot q_i$ is expressed in terms of $q$ and $p$. For most mechanical systems, $H = T + V$ — the total energy written in terms of positions and momenta.

### Hamilton's equations
$$\boxed{\dot q_i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q_i}}$$
These are $2n$ **first-order** equations, replacing $n$ second-order Euler–Lagrange equations. Also $\frac{dH}{dt} = \frac{\partial H}{\partial t}$: if $H$ has no explicit time dependence, energy is conserved.

### Example 6.1 – Harmonic oscillator
$H = \frac{p^2}{2m} + \frac12 kx^2$.
$\dot x = \partial H/\partial p = p/m$; $\dot p = -\partial H/\partial x = -kx$.
Combining: $m\ddot x = -kx$. ✓
In phase space $(x, p)$ the trajectories are ellipses $\frac{p^2}{2mE} + \frac{x^2}{2E/k} = 1$, whose area is $2\pi E/\omega$. In old quantum theory, quantizing this area in units of Planck's constant $h$ gave $E = nh\nu$ — a historical step toward quantum mechanics.

### Phase space
The $2n$-dimensional space of all $(q, p)$ is **phase space**. Each point represents a complete state of the system; Hamilton's equations define a flow in it. Trajectories in phase space never cross (for time-independent $H$) because the state at one instant uniquely determines the future.

**Liouville's theorem:** the Hamiltonian flow preserves phase-space volume. A cloud of initial conditions may stretch and fold, but its volume remains constant — phase space behaves like an incompressible fluid. This theorem is foundational for statistical mechanics (it justifies the uniform probability density over the energy surface in the microcanonical ensemble) and explains why you cannot use a passive optical system to make light brighter than its source.

### Poisson brackets
For functions $f(q, p)$ and $g(q, p)$, the **Poisson bracket** is
$$\{f, g\} = \sum_i\left(\frac{\partial f}{\partial q_i}\frac{\partial g}{\partial p_i} - \frac{\partial f}{\partial p_i}\frac{\partial g}{\partial q_i}\right)$$
Properties: $\{q_i, p_j\} = \delta_{ij}$, $\{q_i, q_j\} = \{p_i, p_j\} = 0$.

The time evolution of any quantity is
$$\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}$$
So a quantity with no explicit time dependence is conserved if and only if its Poisson bracket with $H$ vanishes.

**Bridge to quantum mechanics:** Dirac recognized that quantum mechanics can be obtained by replacing Poisson brackets with commutators:
$$\{f, g\} \;\longrightarrow\; \frac{1}{i\hbar}[\hat f, \hat g]$$
In particular $\{x, p\} = 1$ becomes $[\hat x, \hat p] = i\hbar$, the canonical commutation relation, and $\frac{df}{dt} = \{f, H\}$ becomes the Heisenberg equation of motion $\frac{d\hat f}{dt} = \frac{i}{\hbar}[\hat H, \hat f]$.

### Canonical transformations and Hamilton–Jacobi theory
Transformations $(q, p) \to (Q, P)$ that preserve the form of Hamilton's equations are **canonical**. The goal is often to find coordinates in which the Hamiltonian is simple — ideally, where all $Q_i$ are cyclic, so all $P_i$ are constants (**action–angle variables**). The **Hamilton–Jacobi equation**
$$H\left(q, \frac{\partial S}{\partial q}, t\right) + \frac{\partial S}{\partial t} = 0$$
for Hamilton's principal function $S$ is the most powerful method for exactly solvable problems and is the classical limit of the Schrödinger equation (via $\psi \sim e^{iS/\hbar}$, the WKB approximation).

## 7. Integrability and Chaos

A system with $n$ degrees of freedom is **integrable** if it has $n$ independent conserved quantities in involution (mutually vanishing Poisson brackets). Its motion is then regular — quasi-periodic on invariant tori in phase space. Examples: the harmonic oscillator, the Kepler problem, the free rigid body.

Most systems are **not** integrable. The **double pendulum** and the **three-body problem** exhibit **deterministic chaos**: exponential sensitivity to initial conditions (positive Lyapunov exponents), making long-term prediction impossible in practice even though the equations are deterministic. Poincaré discovered this in the 1880s–1890s while studying the three-body problem. The KAM (Kolmogorov–Arnold–Moser) theorem shows that weakly perturbed integrable systems retain most of their regular tori, with chaos appearing in thin layers that grow as the perturbation increases.

## 8. Comparison of Formulations

| Feature | Newtonian | Lagrangian | Hamiltonian |
|---|---|---|---|
| Basic quantity | Force $\vec F$ | $L = T - V$ | $H = T + V$ (usually) |
| Variables | $\vec r$, $\vec v$ | $q$, $\dot q$ | $q$, $p$ |
| Equations | $\vec F = m\vec a$ ($3N$ second-order) | Euler–Lagrange ($n$ second-order) | Hamilton ($2n$ first-order) |
| Constraints | Explicit constraint forces | Eliminated via generalized coordinates | Eliminated |
| Symmetries | Not manifest | Cyclic coordinates, Noether | Poisson brackets, canonical transformations |
| Best for | Simple problems, intuition | Constrained systems, field theory | Phase space, statistical mechanics, quantum mechanics |

## 9. Summary of Key Equations

$$L = T - V, \qquad S = \int L\,dt, \qquad \delta S = 0$$
$$\frac{d}{dt}\frac{\partial L}{\partial\dot q_i} - \frac{\partial L}{\partial q_i} = 0, \qquad p_i = \frac{\partial L}{\partial\dot q_i}$$
$$H = \sum p_i\dot q_i - L, \qquad \dot q_i = \frac{\partial H}{\partial p_i}, \qquad \dot p_i = -\frac{\partial H}{\partial q_i}$$
$$\frac{df}{dt} = \{f, H\} + \frac{\partial f}{\partial t}, \qquad \{q_i, p_j\} = \delta_{ij}$$
