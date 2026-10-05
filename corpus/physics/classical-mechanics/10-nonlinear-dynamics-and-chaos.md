---
title: Nonlinear Dynamics and Chaos
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [nonlinear dynamics, chaos theory, phase space, phase portrait, fixed point, linear stability, Jacobian matrix, limit cycle, van der Pol oscillator, Poincare-Bendixson theorem, bifurcation, saddle-node bifurcation, pitchfork bifurcation, Hopf bifurcation, driven damped pendulum, logistic map, period doubling, Feigenbaum constants, universality, Lyapunov exponent, predictability, butterfly effect, strange attractor, Lorenz system, Henon map, fractal dimension, Kaplan-Yorke dimension, Poincare section, Hamiltonian chaos, KAM theorem, standard map, solar system chaos]
---

# Nonlinear Dynamics and Chaos

For most of the history of physics, the systems that could be solved were linear: the ideal spring, the small-angle pendulum, the planet orbiting a single star. Their behavior is regular, and a small error in the starting conditions produces only a small error in the prediction. Yet a real pendulum swinging through large angles, a dripping faucet, convecting air in the atmosphere, a beating heart and a population of insects are all **nonlinear**, and many of them behave in ways that look random even though their governing laws contain no randomness at all. This behavior is called **deterministic chaos**.

The discovery that simple deterministic equations can produce motion that is effectively unpredictable over long times was one of the major scientific developments of the 20th century. It changed how physicists think about predictability, how meteorologists forecast the weather, how engineers design oscillators and how ecologists interpret fluctuating populations.

This chapter builds the subject from the ground up. It covers:

- **phase space** and **phase portraits**, the geometric language of dynamics;
- **fixed points** and their **linear stability**;
- **limit cycles**, the self-sustained oscillations of nonlinear systems;
- **bifurcations** (saddle-node, transcritical, pitchfork and Hopf), where the qualitative behavior changes as a parameter is varied;
- the **driven damped pendulum**, a mechanical system that becomes chaotic;
- the **logistic map**, **period doubling** and the universal **Feigenbaum constants**;
- **Lyapunov exponents**, which measure sensitivity to initial conditions;
- **strange attractors**, the **Lorenz system** and **fractal dimension**;
- **predictability** and the weather;
- **Poincaré sections**;
- **Hamiltonian chaos** and the **KAM theorem**;
- chaos in nature and technology, its history, common misconceptions and connections to other fields.

The chapter assumes familiarity with Newton's laws, simple harmonic and damped oscillations, and basic calculus. Some linear algebra (eigenvalues of a 2×2 matrix) is used and explained as it appears.

## 1. Linear versus Nonlinear Systems

A system of differential equations is **linear** if the unknown functions and their derivatives appear only to the first power and are not multiplied together. The damped, driven harmonic oscillator
$$m\ddot x + b\dot x + kx = F_0\cos\omega t$$
is linear. Linear systems obey the **superposition principle**: if $x_1(t)$ and $x_2(t)$ are solutions of the homogeneous equation, so is $c_1x_1 + c_2x_2$. Superposition allows any linear problem to be broken into simple pieces (normal modes, Fourier components) that are solved separately and added back together. This is why linear physics is so tractable.

A system is **nonlinear** if superposition fails. The full pendulum equation
$$\ddot\theta + \frac{g}{L}\sin\theta = 0$$
is nonlinear because $\sin(\theta_1 + \theta_2) \neq \sin\theta_1 + \sin\theta_2$. Nonlinear terms such as $x^2$, $x\dot x$, $\sin x$ or $xy$ appear naturally whenever a restoring force is not exactly proportional to displacement, when friction depends on speed in a complicated way, when a population limits its own growth, or when a fluid carries its own velocity field along (the term $(\mathbf v\cdot\nabla)\mathbf v$ in fluid mechanics).

Nonlinear systems can show behavior that linear systems never do:

- **multiple equilibria** (a pendulum can hang down or balance upright);
- **self-sustained oscillations** of fixed amplitude, independent of starting conditions;
- **sudden qualitative changes** (bifurcations) as a parameter is varied smoothly;
- **chaos**: bounded, aperiodic motion with sensitive dependence on initial conditions.

Because nonlinear equations rarely have closed-form solutions, the subject relies on three complementary tools: **geometry** (phase portraits), **local analysis** (linearization near special solutions) and **computation** (numerical integration). All simulation results quoted in this chapter for differential equations were obtained by fourth-order Runge–Kutta integration; results for maps come from direct iteration.

## 2. Phase Space and Phase Portraits

### State variables and flows

The **state** of a mechanical system is the minimal set of numbers that, together with the equations of motion, determines its entire future. For a particle moving in one dimension under a force depending on position and velocity, the state is $(x, v)$. For a pendulum it is $(\theta, \omega)$ with $\omega = \dot\theta$. The space of all possible states is called **phase space**, and its dimension is the number of state variables.

Any system of ordinary differential equations can be written in first-order form
$$\dot{\mathbf x} = \mathbf F(\mathbf x), \qquad \mathbf x = (x_1, x_2, \ldots, x_n).$$
For example, the pendulum becomes $\dot\theta = \omega$, $\dot\omega = -(g/L)\sin\theta$. The function $\mathbf F$ assigns a velocity vector to every point of phase space; it is a **vector field**, and the solutions are curves that are everywhere tangent to it. The collection of all solution curves is called the **flow**, and a picture of representative trajectories is a **phase portrait**.

A system with no explicit time dependence in $\mathbf F$ is called **autonomous**. A driven system such as $\ddot x + b\dot x + kx = F_0\cos\omega t$ can be made autonomous by adding the drive phase $\psi = \omega t$ as an extra variable with $\dot\psi = \omega$. The driven oscillator therefore has a three-dimensional phase space $(x, v, \psi)$.

### One-dimensional flows

The simplest case is a single equation $\dot x = f(x)$. Its phase space is a line. Wherever $f(x) > 0$, the state moves to the right; wherever $f(x) < 0$, it moves to the left; where $f(x) = 0$ it stays put. Sketching the graph of $f$ immediately gives the full qualitative behavior. Trajectories on a line can only move monotonically toward a fixed point or off to infinity. **A one-dimensional autonomous flow can never oscillate**, let alone be chaotic, because a trajectory cannot pass through a point twice in opposite directions.

### The pendulum phase portrait

For the undamped pendulum, multiply $\ddot\theta = -\omega_0^2\sin\theta$ (with $\omega_0^2 = g/L$) by $\dot\theta$ and integrate once. This gives the conserved energy per unit $mL^2$:
$$E = \tfrac12\dot\theta^2 - \omega_0^2\cos\theta = \text{constant}.$$
Each trajectory lies on a level curve of $E$:

1. **Librations** ($-\omega_0^2 < E < \omega_0^2$): closed loops around $(\theta, \dot\theta) = (0, 0)$, the familiar back-and-forth swinging. Near the bottom the loops are ellipses (simple harmonic motion); for larger amplitudes they become distorted and the period lengthens.
2. **Rotations** ($E > \omega_0^2$): wavy curves that never cross $\dot\theta = 0$. The pendulum whirls over the top.
3. **The separatrix** ($E = \omega_0^2$): the curve that separates the two kinds of motion. Setting $E = \omega_0^2$ gives $\tfrac12\dot\theta^2 = \omega_0^2(1 + \cos\theta) = 2\omega_0^2\cos^2(\theta/2)$, so
$$\dot\theta = \pm2\omega_0\cos(\theta/2).$$
A pendulum on the separatrix approaches the inverted position $\theta = \pi$ asymptotically, taking infinite time to get there.

The point $(0, 0)$ is surrounded by closed orbits and is called a **center**; the point $(\pi, 0)$, where the separatrices cross, is a **saddle**. Adding friction changes the picture qualitatively: energy steadily decreases, closed loops become inward spirals, and almost every trajectory ends at the bottom.

### What trajectories can and cannot do

The existence-and-uniqueness theorem for ordinary differential equations (valid when $\mathbf F$ is smooth) has a powerful geometric consequence: **trajectories in the phase space of an autonomous system cannot cross**. If two trajectories met at a point, that point would have two different futures. In a two-dimensional phase plane this is very restrictive: a trajectory confined to a bounded region is trapped between other trajectories and can only approach a fixed point, a closed orbit, or a chain of fixed points joined by trajectories. In three or more dimensions trajectories can pass over and under one another, which leaves room for the endless, non-repeating weaving of chaos. This is why chaos in continuous-time autonomous systems requires **at least three** phase-space dimensions, while iterated maps (discrete time) can be chaotic in just one dimension.

## 3. Fixed Points and Linear Stability

### Fixed points of one-dimensional flows and maps

A **fixed point** (equilibrium) $x^*$ of $\dot x = f(x)$ satisfies $f(x^*) = 0$. To test its stability, write $x = x^* + \eta$ with $\eta$ small and Taylor-expand:
$$\dot\eta = f(x^* + \eta) = f(x^*) + f'(x^*)\eta + O(\eta^2) \approx f'(x^*)\eta.$$
The solution is $\eta(t) = \eta_0e^{f'(x^*)t}$. Therefore:

- if $f'(x^*) < 0$ the perturbation decays and the fixed point is **stable**, with characteristic time $1/\lvert f'(x^*)\rvert$;
- if $f'(x^*) > 0$ the perturbation grows and the fixed point is **unstable**;
- if $f'(x^*) = 0$ the linear test is inconclusive and higher-order terms decide.

For a **map** (discrete-time system) $x_{n+1} = f(x_n)$, a fixed point satisfies $x^* = f(x^*)$. The same expansion gives $\eta_{n+1} \approx f'(x^*)\eta_n$, so $\eta_n = [f'(x^*)]^n\eta_0$. The fixed point is stable if $\lvert f'(x^*)\rvert < 1$ and unstable if $\lvert f'(x^*)\rvert > 1$. The number $f'(x^*)$ is called the **multiplier**. A negative multiplier means the deviation alternates in sign from one step to the next.

### Two-dimensional linearization

For a planar system $\dot x = f(x, y)$, $\dot y = g(x, y)$ with fixed point $(x^*, y^*)$, write $x = x^* + u$, $y = y^* + v$ and keep first-order terms:
$$\begin{pmatrix}\dot u\\ \dot v\end{pmatrix} = J\begin{pmatrix}u\\ v\end{pmatrix}, \qquad J = \begin{pmatrix}\partial f/\partial x & \partial f/\partial y\\ \partial g/\partial x & \partial g/\partial y\end{pmatrix}_{(x^*, y^*)}.$$
The matrix $J$ is the **Jacobian**. Trying solutions of the form $\mathbf u = \mathbf u_0e^{\lambda t}$ gives the eigenvalue problem $J\mathbf u_0 = \lambda\mathbf u_0$, which has nonzero solutions only when $\det(J - \lambda I) = 0$. For $J = \begin{pmatrix}a & b\\ c & d\end{pmatrix}$ this is
$$\lambda^2 - \tau\lambda + \Delta = 0, \qquad \tau = a + d = \operatorname{tr}J, \qquad \Delta = ad - bc = \det J,$$
with roots
$$\lambda_{1,2} = \frac{\tau \pm \sqrt{\tau^2 - 4\Delta}}{2}.$$
Since $\lambda_1 + \lambda_2 = \tau$ and $\lambda_1\lambda_2 = \Delta$, the trace and determinant alone determine the type of fixed point. A general perturbation is a combination of the two eigen-solutions, so it decays if both eigenvalues have negative real parts and grows if either has a positive real part.

### Classification by trace and determinant

| Condition | Eigenvalues | Type of fixed point |
|---|---|---|
| $\Delta < 0$ | real, opposite signs | saddle (always unstable) |
| $\Delta > 0$, $\tau^2 > 4\Delta$, $\tau < 0$ | real, both negative | stable node |
| $\Delta > 0$, $\tau^2 > 4\Delta$, $\tau > 0$ | real, both positive | unstable node |
| $\Delta > 0$, $\tau^2 < 4\Delta$, $\tau < 0$ | complex, negative real part | stable spiral (focus) |
| $\Delta > 0$, $\tau^2 < 4\Delta$, $\tau > 0$ | complex, positive real part | unstable spiral |
| $\Delta > 0$, $\tau = 0$ | purely imaginary | center (in the linear approximation) |

The **Hartman–Grobman theorem** guarantees that near a **hyperbolic** fixed point (no eigenvalue with zero real part), the nonlinear flow looks like its linearization, up to a continuous deformation of the coordinates. Saddles, nodes and spirals are therefore robust. Centers are not: weak nonlinear terms can turn a linear center into a slow spiral in either direction. The undamped pendulum's center at $(0, 0)$ survives only because energy conservation forces the orbits to close.

### Worked Example 3.1: Stability of a damped pendulum

**Problem:** A pendulum of length $L = 0.50$ m swings in air with a damping term, so that $\ddot\theta + b\dot\theta + (g/L)\sin\theta = 0$ with $b = 0.80$ s⁻¹ and $g = 9.81$ m/s². Classify the fixed points at $\theta = 0$ and $\theta = \pi$, and find the period and decay time of small oscillations.

**Solution:**

1. Write the system in first-order form: $\dot\theta = \omega$, $\dot\omega = -\omega_0^2\sin\theta - b\omega$, with $\omega_0^2 = g/L = 19.62$ s⁻².
2. Fixed points require $\omega = 0$ and $\sin\theta = 0$: $(0, 0)$ and $(\pi, 0)$.
3. The Jacobian is $J = \begin{pmatrix}0 & 1\\ -\omega_0^2\cos\theta & -b\end{pmatrix}$.
4. At $(0, 0)$: $\tau = -0.80$ s⁻¹ and $\Delta = 19.62$ s⁻². Since $\tau^2 - 4\Delta = 0.64 - 78.48 < 0$, the eigenvalues are complex: $\lambda = -0.40 \pm 4.41i$ s⁻¹. With $\tau < 0$ this is a **stable spiral**.
5. The imaginary part gives the angular frequency of the decaying oscillation, $4.41$ rad/s, so the period is $2\pi/4.41 = 1.42$ s. The real part gives the amplitude decay time $1/0.40 = 2.5$ s.
6. At $(\pi, 0)$: $\cos\pi = -1$, so $\Delta = -19.62$ s⁻² $< 0$, a **saddle**. The eigenvalues are $\lambda = \tfrac12\left(-0.80 \pm\sqrt{0.64 + 78.48}\right) = +4.05$ s⁻¹ and $-4.85$ s⁻¹.

**Answer:** The hanging position is a stable spiral (period 1.42 s, decay time 2.5 s); the inverted position is a saddle from which small disturbances grow by a factor $e$ every $1/4.05 = 0.25$ s.

## 4. Limit Cycles

A **limit cycle** is an *isolated* closed trajectory: neighboring trajectories are not closed but spiral toward it (stable limit cycle) or away from it (unstable limit cycle). Limit cycles are fundamentally nonlinear. A linear system can have closed orbits, but they come in continuous families (like the ellipses of a frictionless oscillator), and the amplitude of the motion is set by the initial conditions. A stable limit cycle instead has an amplitude and period fixed by the system itself. If the system is disturbed, it returns to the same oscillation.

This is exactly what is needed for a reliable clock. Pendulum clocks with an escapement, the heartbeat, the firing of pacemaker neurons, the squeal of a brake, the singing of a wine glass rubbed with a wet finger and the steady tone of a bowed violin string are all limit cycles. In each case an energy source pumps energy in when the amplitude is small, and dissipation removes more energy than is supplied when the amplitude is large.

### The van der Pol oscillator

The prototype was studied by the Dutch engineer Balthasar van der Pol in the 1920s while modeling vacuum-tube circuits:
$$\ddot x - \mu(1 - x^2)\dot x + x = 0, \qquad \mu > 0.$$
The middle term is a nonlinear damping. For $\lvert x\rvert < 1$ the damping coefficient $-\mu(1 - x^2)$ is negative (energy is pumped in); for $\lvert x\rvert > 1$ it is positive (energy is removed). Small oscillations therefore grow and large ones shrink.

Linearizing about the origin gives $J = \begin{pmatrix}0 & 1\\ -1 & \mu\end{pmatrix}$, with $\tau = \mu > 0$ and $\Delta = 1$. The origin is an unstable spiral for $0 < \mu < 2$ and an unstable node for $\mu > 2$. Trajectories leave it, but far from the origin the damping is positive and trajectories move inward. They are caught in between, on the limit cycle.

### Energy-balance derivation of the limit-cycle amplitude

For small $\mu$ the motion is nearly sinusoidal, $x \approx A\cos t$. Define $E = \tfrac12(\dot x^2 + x^2)$. Using the equation of motion,
$$\frac{dE}{dt} = \dot x\ddot x + x\dot x = \dot x\left[\mu(1 - x^2)\dot x - x\right] + x\dot x = \mu(1 - x^2)\dot x^2.$$
Substitute $x = A\cos t$, $\dot x = -A\sin t$ and average over one cycle, using $\langle\sin^2t\rangle = \tfrac12$ and $\langle\cos^2t\sin^2t\rangle = \tfrac18$:
$$\left\langle\frac{dE}{dt}\right\rangle = \mu\left(\frac{A^2}{2} - \frac{A^4}{8}\right).$$
A steady oscillation requires zero net energy gain per cycle, so $A^2 = 4$, giving
$$A = 2.$$
Because $E \approx A^2/2$, the same calculation gives the slow evolution of the amplitude:
$$\frac{dA}{dt} = \frac{\mu A}{2}\left(1 - \frac{A^2}{4}\right).$$
This one-dimensional flow has an unstable fixed point at $A = 0$ and a stable one at $A = 2$: the limit cycle is stable. Numerical integration confirms the result, giving a peak amplitude of 2.000 and period 6.287 for $\mu = 0.1$ (close to $2\pi = 6.283$), and amplitude 2.009 and period 6.663 for $\mu = 1$. For large $\mu$ the motion becomes a **relaxation oscillation**: slow creeping phases alternate with rapid jumps, and the period grows roughly in proportion to $\mu$ (19.08 for $\mu = 10$).

### The Poincaré–Bendixson theorem

How can one be sure a limit cycle exists without solving the equations? In the plane there is a powerful answer. The **Poincaré–Bendixson theorem** states: if a trajectory of a smooth planar autonomous system stays forever in a closed, bounded region that contains no fixed points, then the trajectory approaches a closed orbit. The usual application is to construct a **trapping region**, such as an annulus whose boundary the flow crosses only inward, with the unstable fixed point excluded from the middle.

The theorem has a striking corollary: **chaos is impossible in a two-dimensional autonomous flow.** Every bounded trajectory in the plane ends at a fixed point, a closed orbit or a chain of fixed points connected by trajectories. Chaos needs the extra room of a third dimension.

### Worked Example 4.1: Start-up of an electronic oscillator

**Problem:** An electronic oscillator is described in dimensional form by $\ddot V - \mu\omega_0(1 - V^2/V_0^2)\dot V + \omega_0^2V = 0$ with $\omega_0 = 2\pi\times1.00$ kHz, $\mu = 0.10$ and $V_0 = 1.5$ V. (a) What is the steady amplitude of the output? (b) The oscillation starts from electronic noise of amplitude about 1 mV. Estimate how long it takes to grow to about 1 V.

**Solution:**

1. With $x = V/V_0$ and $s = \omega_0t$, the equation becomes the standard van der Pol equation with $\mu = 0.10$, a small value, so the energy-balance result applies.
2. (a) The dimensionless amplitude is 2, so the voltage amplitude is $2V_0 = 3.0$ V.
3. (b) While the amplitude is small, $dA/ds \approx (\mu/2)A$, so the amplitude grows as $e^{(\mu/2)s} = e^{(\mu\omega_0/2)t}$.
4. The growth rate is $\mu\omega_0/2 = 0.10\times6283/2 = 314$ s⁻¹, an e-folding time of $3.2$ ms.
5. Growing by a factor 1000 requires $t = \ln(1000)/314\text{ s}^{-1} = 22$ ms. (As the amplitude approaches 3 V the growth slows, but 1 V is still in the nearly exponential regime.)

**Answer:** The output settles at 3.0 V amplitude, and it takes roughly 20 ms to grow from noise to volt-level oscillation. The final amplitude does not depend on how the oscillation started, which is the defining property of a limit cycle.

## 5. Bifurcations

As a control parameter changes smoothly, the behavior of a nonlinear system usually changes smoothly too. At special parameter values, however, fixed points or limit cycles are created, destroyed or change stability. These qualitative changes are **bifurcations**. Near a bifurcation, very different physical systems can be reduced to the same simple **normal form**, which is why a handful of bifurcation types appear again and again in nature.

A **bifurcation diagram** plots the long-term states of a system (fixed-point positions or oscillation amplitudes) against the control parameter, conventionally with solid lines for stable states and dashed lines for unstable ones.

### Saddle-node bifurcation

The normal form is
$$\dot x = r + x^2.$$
For $r < 0$ there are two fixed points, $x^* = \pm\sqrt{-r}$. Since $f'(x) = 2x$, the negative one is stable and the positive one unstable. As $r$ increases toward zero, they move together; at $r = 0$ they merge into a single half-stable point; for $r > 0$ there are no fixed points at all, and $x$ increases without limit. Fixed points are created or destroyed in pairs "out of thin air". Saddle-node bifurcations explain sudden jumps and collapses: a system resting at a stable state finds that state disappearing beneath it, and it moves rapidly somewhere else.

A useful feature near (but just past) a saddle-node is the **bottleneck**: the trajectory slows down where the fixed points used to be. The time spent passing through scales as $\pi/\sqrt{r}$, which is the integral $\int_{-\infty}^{\infty}dx/(r + x^2)$.

### Worked Example 5.1: Fishery collapse

**Problem:** A fish stock with logistic growth and constant harvesting obeys $\dot N = rN(1 - N/K) - H$, with intrinsic growth rate $r = 0.40$ per year and carrying capacity $K = 50\,000$ tonnes. (a) Find the equilibria for a harvest of $H = 4200$ tonnes per year and their stability. (b) Find the critical harvest above which the population collapses.

**Solution:**

1. Equilibria satisfy $rN(1 - N/K) = H$, a quadratic: $N^2 - KN + HK/r = 0$, so $N^* = \tfrac{K}{2}\left(1 \pm\sqrt{1 - 4H/(rK)}\right)$.
2. With $4H/(rK) = 4\times4200/(0.40\times50\,000) = 0.84$, the square root is $\sqrt{0.16} = 0.40$, giving $N^* = 35\,000$ t and $N^* = 15\,000$ t.
3. Stability: $f'(N) = r(1 - 2N/K)$. At $35\,000$ t, $f' = 0.40(1 - 1.4) = -0.16$ per year (stable; recovery time about $1/0.16 = 6.3$ years). At $15\,000$ t, $f' = +0.16$ per year (unstable; a stock pushed below this level declines to extinction).
4. The two equilibria merge when $1 - 4H/(rK) = 0$, i.e. at $H_c = rK/4 = 0.40\times50\,000/4 = 5000$ tonnes per year. This is a saddle-node bifurcation.

**Answer:** For $H = 4200$ t/yr the stock settles at $35\,000$ t, with a threshold at $15\,000$ t. If the harvest exceeds $5000$ t/yr (the "maximum sustainable yield"), no equilibrium exists and the stock collapses. Note the warning sign before collapse: as $H \to H_c$ the restoring rate $\lvert f'\rvert$ shrinks, so recovery from disturbances becomes slower and slower. This **critical slowing down** is studied as an early-warning signal of abrupt transitions in ecosystems and climate.

### Transcritical bifurcation

The normal form $\dot x = rx - x^2$ has fixed points $x^* = 0$ and $x^* = r$ for all $r$. They exchange stability as they pass through each other at $r = 0$: for $r < 0$ the origin is stable, and for $r > 0$ the point $x^* = r$ is stable. This is the natural bifurcation when a trivial state (zero population, zero light) always exists. A simple model of a **laser** shows it: below the pumping threshold the photon number in the cavity stays near zero; above threshold the "off" state becomes unstable and coherent laser light builds up, with intensity growing linearly with pump strength above threshold.

### Pitchfork bifurcation

Systems with a left-right symmetry ($x \to -x$) typically show a **pitchfork** bifurcation. The supercritical normal form is
$$\dot x = rx - x^3.$$
For $r < 0$ the only fixed point is $x^* = 0$, and it is stable ($f'(0) = r < 0$). For $r > 0$ the origin becomes unstable and two new stable fixed points appear at $x^* = \pm\sqrt r$, where $f'(\pm\sqrt r) = r - 3r = -2r < 0$. The symmetric state gives way to one of two mirror-image states; which one is chosen depends on tiny imperfections or noise. This is **spontaneous symmetry breaking**. The amplitude grows as $\sqrt r$, a square-root law characteristic of many continuous phase transitions.

In the **subcritical** form, $\dot x = rx + x^3 - x^5$, the cubic term destabilizes rather than saturates. The new branches are unstable and bend backward, and the system jumps to a distant large-amplitude state when $r$ passes zero. Reversing $r$ does not return it at the same point. Such **hysteresis** is common in buckling and in the onset of some fluid instabilities.

### Worked Example 5.2: Bead on a rotating hoop

**Problem:** A bead slides on a vertical circular hoop of radius $R = 0.20$ m that spins about its vertical diameter with angular speed $\Omega$. Let $\theta$ be the bead's angle from the bottom. Find the critical spin rate at which the bottom position becomes unstable, and the equilibrium angle and small-oscillation frequency for $\Omega = 10.0$ rad/s.

**Solution:**

1. In the rotating frame, the bead feels gravity and the centrifugal force $mR\Omega^2\sin\theta$ directed horizontally outward. The tangential equation of motion (ignoring friction) is
$$mR\ddot\theta = -mg\sin\theta + mR\Omega^2\sin\theta\cos\theta.$$
2. Fixed points: $\sin\theta = 0$ (bottom, $\theta = 0$) or $\cos\theta^* = g/(R\Omega^2)$, which exists only when $\Omega^2 > g/R$.
3. Linearizing about $\theta = 0$: $\ddot\theta = -(g/R - \Omega^2)\theta$. The bottom is stable for $\Omega < \Omega_c = \sqrt{g/R}$ and unstable above it.
4. $\Omega_c = \sqrt{9.81/0.20} = 7.00$ rad/s, which is 66.9 revolutions per minute.
5. For $\Omega = 10.0$ rad/s: $\cos\theta^* = 9.81/(0.20\times100) = 0.4905$, so $\theta^* = \pm60.6°$.
6. Linearizing about $\theta^*$: the derivative of the right-hand side divided by $mR$ is $-(g/R)\cos\theta + \Omega^2\cos2\theta$. Substituting $g/R = \Omega^2\cos\theta^*$ gives $\Omega^2(\cos^2\theta^* - 1) = -\Omega^2\sin^2\theta^*$. The new equilibria are stable, with small-oscillation frequency $\Omega\sin\theta^* = 10.0\times0.871 = 8.71$ rad/s.

**Answer:** The critical spin rate is 7.00 rad/s. Above it, the bead moves off-center to $\pm60.6°$ (at 10.0 rad/s) and oscillates there at 8.71 rad/s. The two symmetric branches $\theta^* = \pm\arccos(g/R\Omega^2)$ form a supercritical pitchfork: just above $\Omega_c$, $\theta^*$ grows like the square root of $\Omega - \Omega_c$.

### Hopf bifurcation

The bifurcations above involve fixed points along a line. In two or more dimensions, a fixed point can also lose stability by having a pair of **complex-conjugate eigenvalues** cross the imaginary axis. This is a **Hopf bifurcation**, and it gives birth to a limit cycle. The supercritical normal form in polar coordinates is
$$\dot r = \mu r - r^3, \qquad \dot\theta = \omega.$$
In Cartesian coordinates, $\dot x = \mu x - \omega y - x(x^2 + y^2)$ and $\dot y = \omega x + \mu y - y(x^2 + y^2)$. The Jacobian at the origin is $\begin{pmatrix}\mu & -\omega\\ \omega & \mu\end{pmatrix}$, with eigenvalues $\lambda = \mu \pm i\omega$. For $\mu < 0$ the origin is a stable spiral. At $\mu = 0$ the eigenvalues cross the imaginary axis. For $\mu > 0$ the origin is an unstable spiral and the radial equation has a stable fixed point at $r = \sqrt\mu$: a circular limit cycle of radius $\sqrt\mu$ and period $2\pi/\omega$.

Key features of a supercritical Hopf bifurcation:

- the oscillation amplitude grows from zero as $\sqrt{\mu - \mu_c}$;
- the frequency at onset is finite and equal to the imaginary part of the eigenvalues;
- small oscillations near onset are nearly sinusoidal.

A concrete mechanical-electrical example is the oscillator $\ddot x - (\varepsilon - x^2)\dot x + x = 0$. Substituting $x = \sqrt\varepsilon\,u$ turns it into the van der Pol equation with $\mu = \varepsilon$, whose limit cycle has $u$-amplitude 2. So for $\varepsilon > 0$ the $x$-amplitude is $2\sqrt\varepsilon$, growing from zero exactly as predicted. The **subcritical** Hopf bifurcation ($\dot r = \mu r + r^3 - r^5$) instead produces a sudden jump to large-amplitude oscillation and hysteresis, and it is the more dangerous type in engineering: aircraft wing flutter and some combustion instabilities can switch on abruptly.

Hopf bifurcations are everywhere: the onset of periodic vortex shedding behind a cylinder in a flow (at a Reynolds number around 47), the start of oscillation in the Belousov–Zhabotinsky chemical reaction, the onset of repetitive firing in many neuron models, and the transition from steady to oscillating output in lasers and electronic circuits.

## 6. The Driven Damped Pendulum

### Equation of motion

Consider a pendulum of mass $m$ and length $L$ with linear damping, driven by a periodic force $F(t) = F_0\cos\omega t$ applied tangentially at the bob. The torque balance about the pivot gives $mL^2\ddot\phi = -bL^2\dot\phi - mgL\sin\phi + LF_0\cos\omega t$. Dividing by $mL^2$ and defining $2\beta = b/m$, $\omega_0^2 = g/L$ and the **drive strength** $\gamma = F_0/(mg)$,
$$\ddot\phi + 2\beta\dot\phi + \omega_0^2\sin\phi = \gamma\omega_0^2\cos\omega t.$$
The dimensionless $\gamma$ is the ratio of the drive force amplitude to the weight. The state space is three-dimensional, $(\phi, \dot\phi, \omega t \bmod 2\pi)$, so the Poincaré–Bendixson obstacle does not apply and chaos is possible.

### From linear response to chaos

A standard set of parameters, used in many textbooks and simulations, is a drive frequency $\omega = 2\pi$ (drive period $T = 1$ time unit), natural frequency $\omega_0 = 1.5\omega$ and damping $\beta = \omega_0/4$. Starting from $\phi(0) = -\pi/2$, $\dot\phi(0) = 0$ and recording $\phi$ once per drive period after transients have died away, numerical integration shows the following sequence as $\gamma$ is increased:

| Drive strength $\gamma$ | Long-term behavior |
|---|---|
| 0.2 | small, nearly sinusoidal oscillation at the drive frequency (linear response) |
| 0.9 | large oscillation (amplitude about 2.5 rad, or 143°), clearly non-sinusoidal, still period 1 |
| 1.0663 | period doubling: the motion now repeats every 2 drive periods |
| 1.0793 | second doubling: period 4 |
| 1.0821 | period 8 |
| 1.0827 | period 16 |
| about 1.0829 | accumulation of doublings, onset of chaos |
| 1.105 | chaotic: the stroboscopic values of $\phi$ wander irregularly and never repeat |

The intervals between successive doublings shrink rapidly: $1.0793 - 1.0663 = 0.0130$, then $0.0028$, then $0.0006$. Each interval is roughly 4.7 times shorter than the last, a ratio we will meet again in Section 8. Beyond the onset of chaos there are **periodic windows** and regions where different attractors coexist, so the long-term motion can depend on the initial conditions as well as on $\gamma$.

### Worked Example 6.1: Building a chaotic pendulum

**Problem:** Design a laboratory pendulum with the standard parameters above using a drive frequency of 1.00 Hz. Find (a) the length, (b) the damping rate and quality factor, (c) the drive force amplitude needed for chaos with a 50 g bob, and (d) compare the linear-theory amplitude at $\gamma = 0.2$ with the simulated value of $\phi$ at the stroboscopic times, which is 0.267 rad.

**Solution:**

1. Drive: $\omega = 2\pi\times1.00 = 6.283$ rad/s, so $\omega_0 = 1.5\omega = 3\pi = 9.425$ rad/s.
2. (a) $L = g/\omega_0^2 = 9.81/88.83 = 0.110$ m, about 11 cm.
3. (b) $\beta = \omega_0/4 = 2.356$ s⁻¹; the quality factor is $Q = \omega_0/(2\beta) = 2$, a heavily damped pendulum (free oscillations die within a couple of swings).
4. (c) Chaos sets in near $\gamma = 1.083$, so $F_0 = \gamma mg = 1.083\times0.050\times9.81 = 0.531$ N, slightly more than the bob's weight.
5. (d) The small-angle steady-state amplitude is
$$A = \frac{\gamma\omega_0^2}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\beta^2\omega^2}} = \frac{0.2\times9\pi^2}{\sqrt{34}\,\pi^2} = 0.309\text{ rad}\ (17.7°),$$
with phase lag $\delta = \arctan[2\beta\omega/(\omega_0^2 - \omega^2)] = \arctan(3/5) = 0.540$ rad. At the stroboscopic times ($\omega t = 2\pi n$) linear theory predicts $\phi = A\cos\delta = 0.265$ rad.

**Answer:** $L = 11.0$ cm, $\beta = 2.36$ s⁻¹ with $Q = 2$, and $F_0 \approx 0.53$ N. At $\gamma = 0.2$ linear theory (0.265 rad) agrees with the full nonlinear simulation (0.267 rad) to within 1%, the small difference coming from $\sin\phi \neq \phi$. At $\gamma > 1$ the motion is no longer small and linear theory fails completely. Because the phase-space divergence of this system is $-2\beta$, any area of initial conditions in the stroboscopic section shrinks by a factor $e^{-2\beta T} = e^{-1.5\pi} = 0.0090$ every drive period, so the long-term motion is confined to an attractor of zero area.

## 7. The Logistic Map and Period Doubling

Chaos is easiest to study in **maps**, where time advances in discrete steps. The most famous example is the **logistic map**, popularized by the ecologist Robert May in 1976 as a model of populations with non-overlapping generations (many insects, for example):
$$x_{n+1} = rx_n(1 - x_n), \qquad 0 \le x_n \le 1, \quad 0 \le r \le 4.$$
Here $x_n$ is the population in year $n$ as a fraction of a maximum, and $r$ is the growth rate. The factor $(1 - x_n)$ represents crowding: large populations produce proportionally fewer offspring.

### Fixed points and their stability

Fixed points satisfy $x^* = rx^*(1 - x^*)$, giving $x^* = 0$ and $x^* = 1 - 1/r$ (which lies in $[0, 1]$ for $r \ge 1$). The derivative is $f'(x) = r(1 - 2x)$.

- At $x^* = 0$: $f'(0) = r$. Stable for $r < 1$ (the population dies out).
- At $x^* = 1 - 1/r$: $f'(x^*) = r\left(1 - 2 + 2/r\right) = 2 - r$. Stability requires $\lvert 2 - r\rvert < 1$, i.e. $1 < r < 3$.

At $r = 3$ the multiplier passes through $-1$. The population then overshoots and undershoots alternately with growing amplitude, until nonlinearity stabilizes a **period-2 cycle**. This is a **period-doubling** (flip) bifurcation.

### The period-2 orbit

A period-2 orbit consists of two points $p$ and $q$ with $f(p) = q$ and $f(q) = p$; each is a fixed point of the second iterate $f^2$. Writing out $f(f(x)) = x$ gives a quartic equation. Its roots include the two fixed points of $f$, so dividing out the factor $x\left[rx - (r - 1)\right]$ leaves the quadratic
$$r^2x^2 - r(r + 1)x + (r + 1) = 0,$$
whose roots are
$$p, q = \frac{(r + 1) \pm \sqrt{(r + 1)(r - 3)}}{2r}.$$
These are real only for $r > 3$, confirming that the 2-cycle is born at $r = 3$. From the quadratic, $p + q = (r + 1)/r$ and $pq = (r + 1)/r^2$.

By the chain rule, the multiplier of the 2-cycle is
$$(f^2)'(p) = f'(p)f'(q) = r^2(1 - 2p)(1 - 2q) = r^2\left[1 - 2(p + q) + 4pq\right] = -r^2 + 2r + 4.$$
At $r = 3$ this equals $+1$ (the cycle is born), and it decreases as $r$ grows. The cycle loses stability when the multiplier reaches $-1$, i.e. $r^2 - 2r - 5 = 0$:
$$r = 1 + \sqrt6 = 3.449490.$$
There the 2-cycle itself period-doubles into a 4-cycle.

### The cascade and beyond

The process repeats without end, at parameter values that crowd together geometrically. The values below were computed by solving numerically for the parameter at which each $2^{k-1}$-cycle has multiplier $-1$.

| $k$ | Period born at $r_k$ | $r_k$ | $r_k - r_{k-1}$ | Ratio $\delta_k = (r_k - r_{k-1})/(r_{k+1} - r_k)$ |
|---|---|---|---|---|
| 1 | 2 | 3.000000 | — | — |
| 2 | 4 | 3.449490 | 0.449490 | 4.7515 |
| 3 | 8 | 3.544090 | 0.094601 | 4.6563 |
| 4 | 16 | 3.564407 | 0.020317 | 4.6682 |
| 5 | 32 | 3.568759 | 0.004352 | 4.6687 |
| 6 | 64 | 3.569692 | 0.000932 | 4.6691 |
| 7 | 128 | 3.569891 | 0.000200 | — |
| $\infty$ | chaos begins | 3.569946 | | limit 4.6692 |

Beyond the accumulation point $r_\infty = 3.569946$ the logistic map is chaotic for many (but not all) values of $r$. The bifurcation diagram, which plots the long-term values of $x_n$ against $r$, shows bands of chaos interrupted by **periodic windows**. The most visible is the **period-3 window**, which opens at $r = 1 + \sqrt8 = 3.828427$ through a saddle-node bifurcation of $f^3$. Just below this value the orbit shows **intermittency**: long stretches of nearly periodic behavior (the bottleneck of a near saddle-node) interrupted by chaotic bursts. Inside the window, the 3-cycle itself period-doubles to 6, 12, 24, and so on.

The appearance of period 3 is significant. In 1975 Tien-Yien Li and James Yorke proved that a continuous map of an interval with a period-3 orbit also has orbits of every other period, as well as uncountably many aperiodic orbits; their paper "Period Three Implies Chaos" introduced the word *chaos* into mathematics. (A more general ordering of periods had been found by Oleksandr Sharkovsky in 1964.)

At $r = 4$ the map is chaotic over the whole interval $[0, 1]$ and can be solved exactly. Substituting $x_n = \sin^2(\pi\theta_n)$ gives $x_{n+1} = 4\sin^2(\pi\theta_n)\cos^2(\pi\theta_n) = \sin^2(2\pi\theta_n)$, so
$$x_n = \sin^2\left(2^n\pi\theta_0\right).$$
Each step doubles $\theta$, which in binary notation shifts its digits one place to the left and discards the integer part. The long-term state is determined by ever more distant binary digits of the initial condition. Any finite-precision knowledge of $x_0$ is used up after a finite number of steps.

### Worked Example 7.1: Alternating insect populations

**Problem:** An insect population is modeled by the logistic map with $r = 3.2$. (a) Show that the nonzero fixed point is unstable. (b) Find the 2-cycle and check its stability. (c) If the maximum population is 10 000 insects per hectare, describe the observed populations.

**Solution:**

1. (a) $x^* = 1 - 1/3.2 = 0.6875$, with multiplier $2 - r = -1.2$. Since $\lvert -1.2\rvert > 1$, the fixed point is unstable; deviations grow by 20% per generation while flipping sign.
2. (b) $\sqrt{(r + 1)(r - 3)} = \sqrt{4.2\times0.2} = 0.9165$, so $p, q = (4.2 \pm 0.9165)/6.4 = 0.7995$ and $0.5130$.
3. Check: $3.2\times0.7995\times(1 - 0.7995) = 0.5130$ and $3.2\times0.5130\times0.4870 = 0.7995$. ✓
4. Multiplier: $-r^2 + 2r + 4 = -10.24 + 6.4 + 4 = 0.16$. Since $\lvert 0.16\rvert < 1$, the 2-cycle is stable, and deviations shrink by a factor of 0.16 every two generations.
5. (c) Multiply by 10 000: the populations alternate between about 7990 and 5130 insects per hectare.

**Answer:** The population settles into a boom-and-bust cycle of period two years, alternating between roughly 8000 and 5100 insects per hectare, even though the environment is perfectly constant. Fluctuations do not require external causes.

## 8. Feigenbaum Constants and Universality

In 1975 Mitchell Feigenbaum, then at Los Alamos National Laboratory, was computing the period-doubling parameter values of the logistic map with a programmable pocket calculator. He noticed that they converged geometrically, with the ratio of successive intervals approaching a fixed number:
$$\delta = \lim_{k\to\infty}\frac{r_k - r_{k-1}}{r_{k+1} - r_k} = 4.669201609\ldots$$
He then found the *same* number for the map $x_{n+1} = r\sin(\pi x_n)$ and, in fact, for every smooth one-dimensional map with a single quadratic maximum. A second constant describes the shrinking of the structures in the $x$ direction: each new generation of the cycle is a copy of the previous one reduced in scale by
$$\alpha = 2.502907875\ldots$$
(with alternating orientation). The constants are **universal**: they do not depend on the details of the map, only on the shape of its maximum (quadratic). Feigenbaum explained this with a **renormalization** argument, borrowing ideas from the theory of phase transitions: near $r_\infty$, the doubly iterated map, rescaled by $\alpha$, looks like the original map, and $\delta$ is an eigenvalue of this rescaling operation. His results were published in 1978.

| Constant | Value | Meaning |
|---|---|---|
| $\delta$ | 4.669201609 | ratio of successive period-doubling parameter intervals |
| $\alpha$ | 2.502907875 | scaling factor of the orbit structure between doublings |
| $r_\infty$ (logistic map) | 3.569945672 | accumulation point of the cascade (not universal) |

Universality has a remarkable consequence: experiments on systems with infinitely many degrees of freedom show the same numbers. In 1980 Albert Libchaber and Jean Maurer observed period doubling in a small convection cell of liquid helium, and in 1981 Paul Linsay saw it in a driven electrical circuit containing a varactor diode. In these and later experiments on fluids, lasers, circuits and chemical reactions, measured values of $\delta$ agreed with 4.669 within their experimental uncertainties. The driven pendulum of Section 6 obeys it too.

### Worked Example 8.1: Predicting the onset of chaos

**Problem:** (a) Using only $r_1 = 3$, $r_2 = 1 + \sqrt6$, $r_3 = 3.544090$ and $\delta$, estimate the accumulation point $r_\infty$ of the logistic map. (b) For the driven pendulum, the first two doublings occur at $\gamma_1 = 1.0663$ and $\gamma_2 = 1.0793$. Predict $\gamma_3$ and the onset of chaos.

**Solution:**

1. If the intervals shrink by a factor $\delta$ each time, the remaining distance beyond $r_n$ is the geometric series
$$r_\infty - r_n = (r_n - r_{n-1})\left(\frac1\delta + \frac1{\delta^2} + \cdots\right) = \frac{r_n - r_{n-1}}{\delta - 1}.$$
2. (a) With $r_3 - r_2 = 3.544090 - 3.449490 = 0.094600$: $r_\infty \approx 3.544090 + 0.094600/3.669202 = 3.544090 + 0.025782 = 3.569872$.
3. The exact value is 3.569946, so the error is only $7\times10^{-5}$.
4. (b) $\gamma_3 \approx \gamma_2 + (\gamma_2 - \gamma_1)/\delta = 1.0793 + 0.0130/4.6692 = 1.0821$.
5. $\gamma_\infty \approx \gamma_2 + (\gamma_2 - \gamma_1)/(\delta - 1) = 1.0793 + 0.0130/3.6692 = 1.0828$.

**Answer:** $r_\infty \approx 3.56987$ (true value 3.56995). For the pendulum, $\gamma_3 \approx 1.0821$, matching the simulated value, and chaos is predicted near $\gamma \approx 1.083$. A single universal number lets us predict the behavior of a mechanical system from a one-line population model.

## 9. Lyapunov Exponents

### Definition for maps and flows

The defining property of chaos is **sensitive dependence on initial conditions**: nearby trajectories separate exponentially fast. The rate is measured by the **Lyapunov exponent**, named after the Russian mathematician Aleksandr Lyapunov, whose 1892 thesis founded the mathematical theory of stability.

For a one-dimensional map, consider two starting points separated by a tiny $\delta_0$. After one step the separation is $\delta_1 \approx f'(x_0)\delta_0$; after $n$ steps, by the chain rule,
$$\delta_n \approx \delta_0\prod_{i=0}^{n-1}f'(x_i).$$
If $\lvert\delta_n\rvert \approx \lvert\delta_0\rvert e^{n\lambda}$, then taking logarithms gives
$$\lambda = \lim_{n\to\infty}\frac1n\sum_{i=0}^{n-1}\ln\lvert f'(x_i)\rvert.$$
For a stable fixed point this reduces to $\ln\lvert f'(x^*)\rvert < 0$; for a stable $p$-cycle it is $\tfrac1p\ln\lvert\text{multiplier}\rvert < 0$. A **positive** Lyapunov exponent on a bounded attractor is the standard working definition of chaos.

For a continuous-time flow in $n$ dimensions there are $n$ Lyapunov exponents $\lambda_1 \ge \lambda_2 \ge \cdots \ge \lambda_n$, describing the average stretching or contraction rates along different directions of an infinitesimal ball of initial conditions as it is carried along the trajectory. The largest one is
$$\lambda_1 = \lim_{t\to\infty}\frac1t\ln\frac{\lVert\delta\mathbf x(t)\rVert}{\lVert\delta\mathbf x(0)\rVert}$$
for almost every small initial separation. Three facts are useful:

- for a bounded trajectory of a flow that does not settle onto a fixed point, one exponent is exactly zero (a displacement *along* the trajectory neither grows nor decays on average);
- the sum of all the exponents equals the time-averaged divergence $\nabla\cdot\mathbf F$, i.e. the rate of change of phase-space volume;
- in practice $\lambda_1$ is computed by following two nearby trajectories and periodically rescaling their separation (the method of Benettin and co-workers).

The values below were computed for the logistic map by averaging $\ln\lvert r(1 - 2x_n)\rvert$ over $10^6$ iterations.

| $r$ | Behavior | $\lambda$ |
|---|---|---|
| 2.5 | stable fixed point | $-0.693$ (exactly $\ln0.5$) |
| 3.2 | stable 2-cycle | $-0.916$ (exactly $\tfrac12\ln0.16$) |
| 3.5 | stable 4-cycle | $-0.873$ |
| 3.7 | chaotic | $+0.355$ |
| 3.83 | period-3 window | $-0.370$ |
| 3.9 | chaotic | $+0.496$ |
| 4.0 | fully chaotic | $+0.693$ (exactly $\ln2$) |

### Exact result for the logistic map at r = 4

Using the solution $x_n = \sin^2(2^n\pi\theta_0)$, the variable $\theta$ is doubled at each step, so tiny differences in $\theta_0$ double each iteration. Because the change of variables is smooth almost everywhere, the Lyapunov exponent is
$$\lambda = \ln2 = 0.693 \text{ per iteration},$$
in agreement with the numerical value. Each iteration costs exactly one binary digit (bit) of knowledge about the initial state.

### The predictability horizon

Suppose the initial state is known to within $\delta_0$ and predictions are useful as long as the error is smaller than some tolerance $\Delta$. Setting $\delta_0e^{\lambda t} = \Delta$ gives the **predictability horizon**
$$t_{\text{pred}} \approx \frac1\lambda\ln\frac{\Delta}{\delta_0}.$$
The quantity $1/\lambda$ is called the **Lyapunov time**. The crucial point is the *logarithm*: improving the initial accuracy by a factor of 1000 adds only $\ln(1000)/\lambda \approx 6.9/\lambda$ to the horizon. Long-term prediction of a chaotic system is not just difficult; for practical purposes it is impossible.

### Worked Example 9.1: How far ahead can we predict?

**Problem:** (a) The logistic map at $r = 4$ is computed in double precision, which stores numbers with a relative error of about $10^{-16}$. After how many iterations does the computed orbit lose all connection with the true orbit from the same initial value? (b) For the Lorenz system (Section 10, $\lambda_1 = 0.906$ per time unit), how long can an initial error of $10^{-6}$ be tolerated if the attractor has size of order 10 and predictions fail when errors reach about 1? How much is gained by reducing the initial error to $10^{-9}$?

**Solution:**

1. (a) Errors double each step, so we need $10^{-16}\times2^n \approx 1$: $n = \ln(10^{16})/\ln2 = 36.84/0.693 = 53$ iterations. This matches the 53-bit precision of a double-precision number.
2. (b) $t_{\text{pred}} = \ln(1/10^{-6})/0.906 = 13.82/0.906 = 15.3$ time units.
3. With $\delta_0 = 10^{-9}$: $t_{\text{pred}} = 20.72/0.906 = 22.9$ time units.

**Answer:** (a) About 53 iterations. (b) About 15 time units; a thousandfold improvement in initial accuracy extends the forecast by only 7.6 time units, about 50% longer. The individual numerical orbit is wrong after 53 steps, but its *statistical* properties (the distribution of $x$ values, the Lyapunov exponent) remain correct, which is why simulations of chaotic systems are still useful.

## 10. Strange Attractors and the Lorenz System

### The Lorenz equations

In 1963 the meteorologist Edward Lorenz of the Massachusetts Institute of Technology published "Deterministic Nonperiodic Flow", a study of a drastically simplified model of convection, in which a fluid layer is heated from below. Starting from a model by Barry Saltzman, he kept only three variables:
$$\dot x = \sigma(y - x), \qquad \dot y = x(\rho - z) - y, \qquad \dot z = xy - \beta z.$$
Here $x$ is proportional to the intensity of the convective rolling motion, $y$ to the temperature difference between rising and sinking fluid, and $z$ to the distortion of the vertical temperature profile from a straight line. The parameter $\sigma$ is the Prandtl number of the fluid, $\rho$ is the Rayleigh number divided by its critical value for the onset of convection, and $\beta$ depends on the geometry of the rolls. Lorenz chose $\sigma = 10$, $\beta = 8/3$ and $\rho = 28$, which remain the standard values. The same equations describe a single-mode laser (as Hermann Haken showed in 1975) and a leaky water wheel (the Malkus water wheel).

### Fixed points and their stability

Setting the right-hand sides to zero: the first equation gives $y = x$; the third gives $z = x^2/\beta$; substituting into the second gives $x(\rho - 1 - x^2/\beta) = 0$. Thus:

- the origin $(0, 0, 0)$ (no convection) exists for all $\rho$;
- for $\rho > 1$, two more fixed points appear, $C_\pm = \left(\pm\sqrt{\beta(\rho - 1)}, \pm\sqrt{\beta(\rho - 1)}, \rho - 1\right)$, representing steady convection rolls turning clockwise or counterclockwise.

At the origin the Jacobian gives $\lambda = -\beta$ and $\lambda^2 + (\sigma + 1)\lambda - \sigma(\rho - 1) = 0$. For $\rho < 1$ all three eigenvalues are negative and the origin is stable (heat is carried by conduction alone). At $\rho = 1$ one eigenvalue crosses zero, and the symmetric pair $C_\pm$ is born in a **pitchfork bifurcation** (the onset of convection). The fixed points $C_\pm$ have characteristic equation
$$\lambda^3 + (\sigma + \beta + 1)\lambda^2 + \beta(\sigma + \rho)\lambda + 2\sigma\beta(\rho - 1) = 0,$$
and they lose stability in a **subcritical Hopf bifurcation** at
$$\rho_H = \frac{\sigma(\sigma + \beta + 3)}{\sigma - \beta - 1} = 24.74$$
for the standard $\sigma$ and $\beta$. For $\rho = 28 > \rho_H$ every fixed point is unstable, yet trajectories remain bounded. One can show that the function $V = \rho x^2 + \sigma y^2 + \sigma(z - 2\rho)^2$ satisfies $\dot V = -2\sigma\left[\rho x^2 + y^2 + \beta(z - \rho)^2 - \beta\rho^2\right]$, which is negative outside a fixed ellipsoid, so all trajectories eventually enter a bounded region and stay there. They have nowhere to settle, and they never repeat.

### Volume contraction

The divergence of the Lorenz vector field is
$$\nabla\cdot\mathbf F = \frac{\partial\dot x}{\partial x} + \frac{\partial\dot y}{\partial y} + \frac{\partial\dot z}{\partial z} = -\sigma - 1 - \beta,$$
a negative constant. By Liouville's formula, any volume of initial conditions shrinks as $V(t) = V(0)e^{-(\sigma + 1 + \beta)t}$. The system is **dissipative**, and all trajectories end up on a set of **zero volume**: an **attractor**. Since the attractor contains no stable fixed point or cycle, and nearby trajectories on it separate exponentially, it is a **strange attractor**. The term was introduced by David Ruelle and Floris Takens in 1971.

### Structure of the attractor

The Lorenz attractor looks like a pair of butterfly wings. A trajectory spirals outward around $C_+$ for a few turns, then switches unpredictably to spiral around $C_-$, then back, in an irregular sequence. The attractor must reconcile two seemingly contradictory requirements: volumes shrink to zero, yet nearby trajectories separate. It does so by **stretching and folding**. Like dough being kneaded, the flow stretches a blob of states in one direction (giving sensitive dependence), squeezes it more strongly in another (giving volume contraction), and folds it back onto itself (keeping it bounded). Repeating this process infinitely often produces a layered structure with infinitely many sheets, a **fractal** (Section 11).

Lorenz found a neat way to see the determinism in this apparently random motion. He recorded the successive maxima $z_n$ of $z(t)$ and plotted $z_{n+1}$ against $z_n$. The points fall on a thin, tent-shaped curve: the **Lorenz map**. The slope of this curve has magnitude greater than 1 everywhere, so (by the stability criterion for maps) none of its periodic orbits can be stable. This is a first example of reducing a continuous flow to a map.

Two other classic examples complete the picture:

- The **Rössler system** (Otto Rössler, 1976), $\dot x = -y - z$, $\dot y = x + ay$, $\dot z = b + z(x - c)$, with $a = b = 0.2$ and $c = 5.7$, has a single folded band and shows the stretch-and-fold mechanism very clearly.
- The **Hénon map** (Michel Hénon, 1976), $x_{n+1} = 1 - ax_n^2 + y_n$, $y_{n+1} = bx_n$, with $a = 1.4$ and $b = 0.3$, was designed as a simple model of a Poincaré section of the Lorenz flow. Its Jacobian determinant is the constant $-b$, so areas shrink by a factor of 0.3 at every step. Its Lyapunov exponents are about $+0.42$ and $-1.62$.

### Worked Example 10.1: Anatomy of the Lorenz attractor

**Problem:** For $\sigma = 10$, $\beta = 8/3$ and $\rho = 28$: (a) locate the fixed points $C_\pm$; (b) find the eigenvalues at the origin; (c) given that the eigenvalues at $C_\pm$ are $-13.85$ and $0.094 \pm 10.19i$, describe the motion near $C_\pm$; (d) by what factor does a volume of initial conditions shrink in one time unit?

**Solution:**

1. (a) $\sqrt{\beta(\rho - 1)} = \sqrt{(8/3)\times27} = \sqrt{72} = 8.485$, so $C_\pm = (\pm8.485, \pm8.485, 27)$.
2. (b) $\lambda = -8/3 = -2.667$, and from $\lambda^2 + 11\lambda - 270 = 0$: $\lambda = \tfrac12(-11 \pm\sqrt{121 + 1080}) = +11.83$ and $-22.83$. The origin is a saddle with one unstable direction and two stable ones.
3. (c) The real eigenvalue $-13.85$ pulls trajectories quickly onto a two-dimensional surface; the complex pair has a small positive real part, so on that surface trajectories spiral *outward* slowly, with angular frequency 10.19 per time unit (about $2\pi/10.19 = 0.62$ time units per loop), growing by a factor $e^{0.094\times0.62} = 1.06$ per turn.
4. (d) The factor is $e^{-(\sigma + 1 + \beta)} = e^{-13.67} = 1.16\times10^{-6}$.

**Answer:** $C_\pm = (\pm8.49, \pm8.49, 27)$; the origin is a saddle with eigenvalues $11.83$, $-22.83$ and $-2.67$; near $C_\pm$ trajectories spiral outward by about 6% per loop until they are thrown to the other wing; and any blob of initial conditions shrinks in volume a millionfold in each time unit, which is why the attractor has zero volume. The Lyapunov spectrum is approximately $(0.906, 0, -14.572)$; check that the sum, $-13.666$, equals the divergence $-(\sigma + 1 + \beta) = -13.667$.

## 11. Fractal Dimension

### Box-counting dimension

Ordinary geometric objects have integer dimension: a point 0, a line 1, a surface 2. One way to define dimension is by counting. Cover the object with boxes of side $\varepsilon$ and let $N(\varepsilon)$ be the number of boxes needed. For a line segment of length $\ell$, $N = \ell/\varepsilon$; for a square of area $S$, $N = S/\varepsilon^2$. In general $N(\varepsilon) \propto \varepsilon^{-D}$, which motivates the **box-counting dimension**
$$D = \lim_{\varepsilon\to0}\frac{\ln N(\varepsilon)}{\ln(1/\varepsilon)}.$$
For **self-similar** sets made of $N$ copies of themselves, each scaled down by a factor $s$, this gives $D = \ln N/\ln s$.

The **middle-thirds Cantor set** is the classic example. Start with the interval $[0, 1]$, remove the open middle third, then remove the middle third of each remaining piece, and repeat forever. After $k$ steps there are $2^k$ pieces of length $3^{-k}$. With $\varepsilon = 3^{-k}$, $N = 2^k$, so
$$D = \frac{\ln2^k}{\ln3^k} = \frac{\ln2}{\ln3} = 0.6309.$$
The set has zero total length but uncountably many points: it is "more than a set of points but less than a line". The cross-section of a strange attractor in its contracting direction typically has a Cantor-like structure, for exactly the stretch-and-fold reason described above.

| Set | Construction or source | Dimension $D$ |
|---|---|---|
| Middle-thirds Cantor set | 2 copies scaled by 1/3 | $\ln2/\ln3 = 0.6309$ |
| Koch curve | 4 copies scaled by 1/3 | $\ln4/\ln3 = 1.2619$ |
| Sierpinski triangle | 3 copies scaled by 1/2 | $\ln3/\ln2 = 1.5850$ |
| Menger sponge | 20 copies scaled by 1/3 | $\ln20/\ln3 = 2.7268$ |
| Hénon attractor ($a = 1.4$, $b = 0.3$) | numerical | about 1.26 |
| Lorenz attractor (standard parameters) | numerical | about 2.06 |
| West coast of Britain | measured with rulers of different lengths | about 1.25 |

The coastline example comes from Benoit Mandelbrot's 1967 paper "How Long Is the Coast of Britain?", which built on measurements collected by Lewis Fry Richardson. Mandelbrot coined the word **fractal** in 1975. Fractals in nature are only statistically self-similar and only over a limited range of scales, but the concept describes coastlines, river networks, lungs, blood vessels and clouds far better than smooth curves do.

### Dimension from Lyapunov exponents

James Kaplan and James Yorke proposed estimating an attractor's dimension from its Lyapunov exponents. If $j$ is the largest integer for which $\lambda_1 + \cdots + \lambda_j \ge 0$, then
$$D_{KY} = j + \frac{\lambda_1 + \cdots + \lambda_j}{\lvert\lambda_{j+1}\rvert}.$$
The idea is that $j$ directions are not contracted overall, and the next direction is only partly filled. For the Lorenz attractor, $\lambda_1 + \lambda_2 = 0.906 \ge 0$ but adding $\lambda_3$ gives a negative sum, so $j = 2$ and $D_{KY} = 2 + 0.906/14.572 = 2.062$. For the Hénon map, $D_{KY} = 1 + 0.419/1.623 = 1.258$. Both agree well with direct box-counting estimates.

### Worked Example 11.1: Measuring a fractal coastline

**Problem:** A stretch of coastline has fractal dimension $D = 1.25$. Surveyed with a 100 km ruler, it measures 2800 km. (a) What length is obtained with a 10 km ruler? (b) What happens as the ruler length approaches zero?

**Solution:**

1. A ruler of length $\varepsilon$ requires $N(\varepsilon) \propto \varepsilon^{-D}$ steps, so the measured length is $L(\varepsilon) = N\varepsilon \propto \varepsilon^{1 - D}$.
2. Ratio: $L(10)/L(100) = (10/100)^{1 - 1.25} = 10^{0.25} = 1.778$.
3. (a) $L(10\text{ km}) = 2800\times1.778 = 4980$ km.
4. (b) Since $1 - D < 0$, $L(\varepsilon) \to \infty$ as $\varepsilon \to 0$, until the fractal scaling breaks down at the scale of individual rocks and sand grains.

**Answer:** About 4980 km. The "length" of a fractal coastline depends on the ruler; the meaningful, scale-independent quantity is its dimension. Each halving of the ruler multiplies the length by $2^{0.25} = 1.19$.

## 12. Sensitive Dependence and Weather Prediction

Lorenz discovered sensitive dependence by accident in 1961, while running a 12-variable weather model on a Royal McBee computer. Wanting to re-examine part of a run, he restarted it from numbers printed earlier. The printout showed three decimal places (for example 0.506), while the computer stored six (0.506127). The new run matched the old one at first, then drifted further and further from it, until the two simulated weather patterns bore no resemblance to each other. A rounding error of a few parts in ten thousand had grown to dominate the solution. Lorenz realized this was not a computer fault but a property of the equations, and the 1963 paper followed. In a 1972 talk, given the title "Predictability: Does the Flap of a Butterfly's Wings in Brazil Set Off a Tornado in Texas?", the idea acquired its popular name, the **butterfly effect**. Henri Poincaré had stated the principle clearly as early as 1908: a tiny cause we fail to notice can determine a large effect we cannot fail to see, so prediction becomes impossible.

Modern weather forecasting deals with chaos in several ways:

1. **Better initial conditions.** Satellites, radiosondes, aircraft and surface stations feed **data assimilation** systems that estimate the current state of the atmosphere as accurately as possible.
2. **Better models and computers.** Forecast skill has improved by roughly one day per decade: a six-day forecast today is about as accurate as a five-day forecast was ten years earlier.
3. **Ensemble forecasting.** Instead of one forecast, the model is run many times from slightly different initial states consistent with the observational uncertainty. Ensemble systems became operational at the European Centre for Medium-Range Weather Forecasts (ECMWF) and the US National Centers for Environmental Prediction in 1992. The ECMWF ensemble uses 51 members (one control run and 50 perturbed runs). The spread of the ensemble measures how predictable the weather is on a given day, and the fraction of members predicting rain gives a probability of precipitation.

Lorenz's own estimate, refined since, is that the large-scale atmosphere has a practical predictability limit of roughly **two weeks**, because errors at small scales grow quickly and pass their uncertainty to larger scales. Today's deterministic forecasts are skillful out to about a week to ten days.

**Weather versus climate.** Chaos limits the prediction of *a particular trajectory* (tomorrow's weather), but not the prediction of the *attractor's statistics* (the climate). A forecast for 15 July in 30 years is impossible; a statement about the average July temperature in that decade under a given greenhouse-gas scenario is a different kind of problem, closer to asking how the shape of the attractor shifts when the parameters change.

**An illustrative estimate.** Suppose small forecast errors double every 2 days (the Lyapunov exponent is then $\lambda = \ln2/(2\text{ days}) = 0.347$ per day) and the initial error is 1% of the natural variability. The forecast loses all skill when the error reaches 100%, after $\ln(100)/0.347 = 13.3$ days. Making the observations ten times more accurate adds only $\ln(10)/0.347 = 6.6$ days. In the real atmosphere, the fastest error growth occurs at the smallest scales, so the returns from better observations are even smaller than this simple exponential estimate suggests.

## 13. Poincaré Sections

Trajectories in three dimensions are hard to visualize. Poincaré's solution was to look not at the whole trajectory but only at the points where it pierces a chosen surface. This reduces a continuous flow in $n$ dimensions to a **map** in $n - 1$ dimensions.

**Definition.** Choose a surface $S$ in phase space that trajectories cross transversally. If a trajectory crosses $S$ (in a chosen direction) at the point $\mathbf x_k$, the next crossing is $\mathbf x_{k+1} = P(\mathbf x_k)$. The function $P$ is the **Poincaré map** (or first-return map), and the set of points $\{\mathbf x_k\}$ is a **Poincaré section**.

For periodically driven systems there is a natural choice: sample the state once every drive period, $t = nT$. This **stroboscopic map** is what was used for the driven pendulum in Section 6.

What the section reveals:

| Motion | Poincaré section |
|---|---|
| Periodic, same period as the drive (period 1) | a single fixed point |
| Period $n$ | $n$ points visited in rotation |
| Quasi-periodic (two incommensurate frequencies) | points filling a closed curve |
| Chaotic, dissipative | a fractal set with fine layered structure |
| Chaotic, Hamiltonian | points scattered over an area-filling region |

The stability of a periodic orbit becomes the stability of a fixed point of $P$: linearizing gives $\delta\mathbf x_{k+1} = DP\,\delta\mathbf x_k$, and the orbit is stable if all eigenvalues of the matrix $DP$ (the **Floquet multipliers**) have magnitude less than 1. A period-doubling bifurcation occurs when a multiplier passes through $-1$, a saddle-node when one passes through $+1$, and a Neimark–Sacker (secondary Hopf) bifurcation, which creates quasi-periodic motion, when a complex pair crosses the unit circle.

For a dissipative flow the Poincaré map contracts area. For the driven pendulum the divergence of the flow is $-2\beta$, so the determinant of $DP$ is $e^{-2\beta T}$ (Worked Example 6.1). For a Hamiltonian system the Poincaré map preserves area exactly, which leads to the very different picture of Section 14.

Poincaré sections also connect theory with experiment. From a single measured time series (for example, the voltage in a circuit or the times between drops from a faucet), plotting each value against the previous one reconstructs a section of the underlying attractor. The method of **delay coordinates**, justified by a theorem of Floris Takens (1981), is used to detect low-dimensional chaos in laboratory data.

## 14. Hamiltonian Chaos and KAM Theory

### Liouville's theorem

Systems without friction, such as planets, particles in accelerators and stars in galaxies, are described by Hamilton's equations, $\dot q_i = \partial H/\partial p_i$ and $\dot p_i = -\partial H/\partial q_i$. The divergence of this flow is
$$\sum_i\left(\frac{\partial\dot q_i}{\partial q_i} + \frac{\partial\dot p_i}{\partial p_i}\right) = \sum_i\left(\frac{\partial^2H}{\partial q_i\partial p_i} - \frac{\partial^2H}{\partial p_i\partial q_i}\right) = 0.$$
Phase-space volume is therefore conserved (**Liouville's theorem**). Consequences:

- there are **no attractors**: no stable nodes, spirals or limit cycles, and no strange attractors;
- fixed points have eigenvalues in pairs $\pm\lambda$, so in one degree of freedom they are either centers or saddles;
- Lyapunov exponents come in pairs that sum to zero;
- Hamiltonian chaos fills regions of phase space of full dimension, rather than collapsing onto a fractal set.

### Integrable systems and invariant tori

A system with $N$ degrees of freedom is **integrable** if it has $N$ independent conserved quantities that are compatible with each other (their Poisson brackets vanish). Examples are the Kepler problem, a free rigid body and any one-degree-of-freedom system with conserved energy. Integrable systems can be written in **action-angle variables** $(I_i, \theta_i)$, in which $H = H(I)$, the actions are constant and the angles advance uniformly, $\theta_i = \omega_i(I)t + \theta_{i,0}$. Each trajectory is confined to an $N$-dimensional **invariant torus** labeled by the actions. For two degrees of freedom, the torus is a doughnut surface with two frequencies $\omega_1$ and $\omega_2$. If $\omega_1/\omega_2$ is rational, every orbit on the torus is closed (a **resonant** torus); if it is irrational, each orbit winds around forever and covers the torus densely (**quasi-periodic** motion). A Poincaré section of a torus is a closed curve.

### Perturbations, resonances and the KAM theorem

Most systems are not integrable. A natural question, raised by the three-body problem, is what happens to the tori when an integrable system is perturbed, $H = H_0(I) + \varepsilon H_1(I, \theta)$. Attempts to solve this by power series in $\varepsilon$ produce terms with denominators $m_1\omega_1 + m_2\omega_2$ for integers $m_1$ and $m_2$. Near resonant tori these **small divisors** vanish and the series diverge. Poincaré concluded that the series generally fail.

The answer came from Andrey Kolmogorov (announced in 1954), with proofs by Vladimir Arnold (1963) and Jürgen Moser (1962): the **KAM theorem**. Roughly stated, for a sufficiently small perturbation of a non-degenerate integrable system, *most* invariant tori survive, slightly deformed. The survivors are those whose frequency ratios are "sufficiently irrational", meaning that they stay far from all rationals $p/q$ in the sense $\lvert\omega_1/\omega_2 - p/q\rvert > K(\varepsilon)/q^{5/2}$ for all integers $p$ and $q$. The tori near low-order resonances are destroyed. In their place, the **Poincaré–Birkhoff theorem** shows that a chain of alternating stable (elliptic) and unstable (hyperbolic) periodic orbits appears; the elliptic points are surrounded by small islands of regular motion, and thin **chaotic layers** form around the hyperbolic points.

The resulting phase portrait is a **mixed phase space**: islands of regular motion in a chaotic sea, with smaller islands around the larger ones at all scales. As $\varepsilon$ increases, more and more tori break. The tori with the "most irrational" frequency ratio (related to the golden mean, whose continued fraction is $[1; 1, 1, 1, \ldots]$) tend to be the last to go. For two degrees of freedom, surviving tori are two-dimensional surfaces in a three-dimensional energy shell and act as impenetrable barriers to chaotic motion. For three or more degrees of freedom they no longer divide the energy shell, and chaotic orbits can slowly wander along resonances throughout phase space, a process called **Arnold diffusion** (1964).

In 1964 the astronomers Michel Hénon and Carl Heiles studied the motion of a star in a model galactic potential, $H = \tfrac12(p_x^2 + p_y^2) + \tfrac12(x^2 + y^2) + x^2y - \tfrac13y^3$. At energy $E = 1/12$ their Poincaré sections were almost entirely regular closed curves; at $E = 1/8$ a large chaotic sea appeared; and near the escape energy $E = 1/6$ almost all orbits were chaotic. This was one of the first numerical demonstrations of the KAM picture.

### The standard map

The simplest model of Hamiltonian chaos is the **kicked rotor**: a freely rotating arm that receives a sharp torque impulse proportional to $\sin\theta$ once per period. Between kicks the angle advances in proportion to the angular momentum. In suitable units this gives the **standard map** (Chirikov–Taylor map):
$$p_{n+1} = p_n + K\sin\theta_n, \qquad \theta_{n+1} = \theta_n + p_{n+1} \pmod{2\pi}.$$
Its Jacobian matrix is $\begin{pmatrix}1 + K\cos\theta & 1\\ K\cos\theta & 1\end{pmatrix}$ in the variables $(\theta, p)$, with determinant exactly 1: the map preserves area, as a Poincaré map of a Hamiltonian system must. For $K = 0$ all orbits lie on horizontal lines (invariant circles). As $K$ increases, resonant circles break into island chains and chaotic layers. The last invariant circles that span the whole angle range, which block chaotic orbits from diffusing to arbitrarily large momentum, are destroyed at $K_c \approx 0.9716$ (John Greene, 1979). For $K > K_c$ the momentum can wander without bound. The standard map describes particles in accelerators and plasma devices, and its quantum version is a basic model in the study of quantum chaos.

### Chaos in the solar system

The solar system is the original arena of Hamiltonian dynamics, and it turns out to be chaotic on long time scales:

- **Hyperion**, an irregularly shaped moon of Saturn, tumbles chaotically. Jack Wisdom, Stanton Peale and François Mignard predicted this in 1984, and later observations have supported it.
- **Kirkwood gaps** in the asteroid belt, near orbital periods that are simple fractions of Jupiter's period, were explained in the early 1980s by Wisdom, who showed that orbits near the 3:1 resonance are chaotic and can have their eccentricities pumped up until they cross the orbit of Mars and are removed.
- Numerical integrations by Gerald Sussman and Wisdom (1988) found Pluto's orbit chaotic with a Lyapunov time of about 20 million years, and Jacques Laskar (1989) found the inner solar system chaotic with a Lyapunov time of about 5 million years. Positions of the inner planets therefore cannot be predicted beyond roughly 100 million years, even though the solar system is about 4.6 billion years old. Later work by Laskar and Mickaël Gastineau (2009) estimated a probability of about 1% that Mercury's orbit becomes unstable within the next 5 billion years.

## 15. Chaos in Nature and Technology

Chaos and nonlinear dynamics are not curiosities; they appear across science and engineering.

**Fluids and the atmosphere.** Convection, turbulence and weather are the original chaotic systems. The **Ruelle–Takens** scenario (1971) proposed that turbulence begins after only a few instabilities, with a strange attractor appearing after quasi-periodic motion. Jerry Gollub and Harry Swinney's 1975 experiments on fluid between rotating cylinders supported this route. Experiments since have identified three main routes to chaos: **period doubling**, **quasi-periodicity** (breakdown of a torus) and **intermittency**.

**Chemistry.** The Belousov–Zhabotinsky reaction, discovered by Boris Belousov in the early 1950s and developed by Anatol Zhabotinsky in the 1960s, oscillates in color between red and blue. In a continuously stirred reactor it shows limit cycles, period doubling and chaos.

**Biology and medicine.** The heart is a nonlinear oscillator. Alternating long and short beats (**alternans**) are a period-doubling phenomenon associated with risk of arrhythmia, and ventricular fibrillation involves the breakup of spiral waves of electrical activity into disordered patterns. Experiments in the early 1980s on periodically stimulated chick-heart cell aggregates showed phase locking, period doubling and irregular dynamics. In population biology, controlled laboratory experiments on flour beetles (*Tribolium*), published in 1997, showed transitions from stable to periodic to chaotic population dynamics as predicted by a nonlinear model.

**Electronics and lasers.** Simple circuits, such as Leon Chua's circuit (1983) with one nonlinear resistor, produce chaos and are used as teaching tools. Some lasers become chaotic when subjected to optical feedback or modulation. Switching power converters can period-double and become chaotic, which engineers must design around.

**Controlling and using chaos.** Edward Ott, Celso Grebogi and James Yorke showed in 1990 that tiny, well-timed parameter adjustments can stabilize one of the infinitely many unstable periodic orbits embedded in a chaotic attractor (the **OGY method**); the method was soon demonstrated in a vibrating magnetoelastic ribbon, and in 1992 in heart tissue. Louis Pecora and Thomas Carroll showed in 1990 that two chaotic systems can **synchronize** when suitably coupled, which led to proposals for communication schemes that hide a message in a chaotic carrier. Chaotic advection is used to mix fluids efficiently, including in microfluidic devices where turbulence is absent.

**Spaceflight.** The sensitivity of chaotic trajectories can be turned into an advantage: a tiny thrust applied at the right moment can make a large change in the final destination. The spacecraft ISEE-3 was redirected in 1982–1983 using a series of lunar flybys and, renamed the International Cometary Explorer, flew through the tail of comet Giacobini–Zinner in 1985. In 1991 the Japanese probe Hiten reached the Moon on a low-energy trajectory exploiting the chaotic dynamics of the Earth–Moon–Sun system.

**Mechanics everywhere.** The double pendulum, a magnetic pendulum over several magnets, a ball bouncing on a vibrating table and a dripping faucet all show chaos in a tabletop setting. The Rikitake two-disk dynamo (1958), a simple model of the Earth's magnetic field, shows chaotic reversals of polarity.

## 16. Historical Development

| Year | People | Development |
|---|---|---|
| 1687 | Isaac Newton | *Principia*: two-body problem solved exactly; three-body problem left open |
| 1881–1886 | Henri Poincaré | Qualitative theory of differential equations: phase portraits, limit cycles |
| 1890 | Henri Poincaré | Prize memoir on the three-body problem (King Oscar II prize, 1889); after correcting an error he discovered the homoclinic tangle, the geometric root of chaos |
| 1892 | Aleksandr Lyapunov | General theory of the stability of motion |
| 1892–1899 | Henri Poincaré | *New Methods of Celestial Mechanics*, three volumes |
| 1898 | Jacques Hadamard | Sensitive dependence for geodesic motion on negatively curved surfaces |
| 1926–1927 | Balthasar van der Pol | Relaxation oscillations; with Jan van der Mark, irregular "noise" in a driven neon-bulb circuit |
| 1942 | Eberhard Hopf | Bifurcation of periodic solutions from a steady state |
| 1954–1963 | Kolmogorov, Moser, Arnold | KAM theorem |
| early 1960s | Stephen Smale | Horseshoe map: rigorous stretch-and-fold mechanism |
| 1963 | Edward Lorenz | "Deterministic Nonperiodic Flow" |
| 1964 | Michel Hénon, Carl Heiles | Chaos in a model galactic potential |
| 1964 | Oleksandr Sharkovsky | Ordering of periods for maps of an interval |
| 1967 | Benoit Mandelbrot | "How Long Is the Coast of Britain?"; "fractal" coined in 1975 |
| 1971 | David Ruelle, Floris Takens | "Strange attractor"; new scenario for turbulence |
| 1975 | Tien-Yien Li, James Yorke | "Period Three Implies Chaos" |
| 1976 | Robert May; Michel Hénon; Otto Rössler | Logistic map review in *Nature*; Hénon map; Rössler system |
| 1978 | Mitchell Feigenbaum | Universality of period doubling (discovered 1975) |
| 1979 | Boris Chirikov; John Greene | Resonance overlap and the standard map; critical value of $K$ |
| 1980–1981 | Libchaber and Maurer; Linsay | Experimental period doubling in helium convection and in a circuit |
| 1984 | Wisdom, Peale, Mignard | Chaotic tumbling of Hyperion |
| 1988–1989 | Sussman and Wisdom; Laskar | Chaos in the orbits of Pluto and of the inner planets |
| 1990 | Ott, Grebogi, Yorke; Pecora and Carroll | Control of chaos; synchronization of chaos |
| 1992 | ECMWF and NCEP | Operational ensemble weather forecasting |

The modern subject grew from two roots that developed separately for most of the century: the mathematical theory of dynamical systems (Poincaré, Lyapunov, Birkhoff, the Russian school of Andronov, Kolmogorov and Arnold, and Smale) and the physicists' and engineers' encounters with irregular behavior (van der Pol, Lorenz, Hénon). Cheap computers in the 1970s let the two meet, because they made it easy to iterate maps and integrate equations and to *see* the attractors.

## 17. Common Misconceptions

1. **"Chaos means randomness."** Chaotic systems are completely deterministic: the same initial state always gives the same future. They only *look* random because tiny differences in the initial state are amplified exponentially. Truly random (stochastic) systems have no such underlying rule.
2. **"Chaotic systems are unpredictable."** They are predictable for short times, up to roughly a few Lyapunov times. Weather forecasts for tomorrow are good; it is the long-range forecast that fails.
3. **"With precise enough measurements we could predict forever."** The predictability horizon grows only logarithmically with precision. Each tenfold improvement adds the same fixed amount of time, so no finite precision suffices for arbitrarily long prediction.
4. **"Complex behavior requires complicated equations."** The one-variable logistic map and the three-variable Lorenz equations produce chaos. Conversely, systems with many variables can be perfectly regular.
5. **"Every nonlinear system is chaotic."** Most nonlinear systems in one or two dimensions cannot be chaotic at all (Poincaré–Bendixson), and many higher-dimensional ones settle into fixed points or cycles for most parameter values. Chaos needs at least three dimensions in a continuous autonomous flow.
6. **"The butterfly effect means a butterfly can cause a tornado."** The metaphor describes sensitivity of a forecast to tiny uncertainties, not a mechanism by which small things routinely drive big ones. It means we cannot tell, from the initial data, which of many possible futures will occur.
7. **"Since weather is chaotic, climate cannot be predicted."** Climate is the statistics of the attractor, which can be stable and computable even when individual trajectories are not.
8. **"Linearization tells you everything."** It describes behavior only near hyperbolic fixed points. It cannot decide the fate of centers, it misses limit cycles and coexisting attractors, and it says nothing about global behavior far from equilibrium.
9. **"Computer simulations of chaotic systems are meaningless because round-off errors grow."** Individual long-time trajectories are indeed inaccurate, but statistical properties such as the attractor's shape, its dimension and its Lyapunov exponents are robust. For uniformly hyperbolic systems, and in practice for many others, **shadowing** results guarantee that the computed orbit stays close to some true orbit of the system.
10. **"An attractor's dimension must be a whole number."** Strange attractors typically have non-integer (fractal) dimension, such as about 2.06 for the Lorenz attractor.
11. **"Frictionless systems cannot be chaotic, or must be fully chaotic."** Hamiltonian systems can be chaotic but cannot have attractors. Typically they show a mixed phase space, with regular islands coexisting with chaotic regions.

## 18. Connections to Other Topics

- **Oscillations:** the linear theory of damped and driven oscillators is the starting point for limit cycles, nonlinear resonance and the driven pendulum.
- **Lagrangian and Hamiltonian mechanics:** phase space, canonical variables, action-angle variables, Liouville's theorem and integrability are the foundations of Hamiltonian chaos and KAM theory.
- **Gravitation and orbits:** the integrable Kepler problem contrasts with the non-integrable three-body problem, the historical birthplace of chaos.
- **Fluid mechanics:** the Navier–Stokes equations are nonlinear, and convection, vortex shedding and turbulence are central applications. The Lorenz system is a truncated convection model.
- **Thermodynamics and statistical mechanics:** chaos and mixing help explain why systems with many particles explore their phase space and approach equilibrium, linking mechanics to the assumptions of statistical mechanics. Bifurcations resemble phase transitions, with order parameters and square-root scaling, and Feigenbaum's renormalization method came from phase-transition theory.
- **Quantum mechanics:** "quantum chaos" studies quantum systems whose classical limits are chaotic; their energy-level statistics follow random-matrix theory rather than the patterns of integrable systems.
- **Chemical kinetics:** nonlinear rate laws with feedback produce oscillating reactions such as the Belousov–Zhabotinsky reaction.
- **Ecology and epidemiology:** logistic growth, predator–prey cycles (Lotka–Volterra) and harvesting models are nonlinear dynamical systems.
- **Mathematics:** differential equations, linear algebra (eigenvalues), topology, measure theory, fractal geometry and numerical analysis all meet in dynamical systems theory.
- **Earth and atmospheric science:** numerical weather prediction, ensemble forecasting, climate tipping points and geomagnetic reversals.
- **Engineering:** oscillator design, control theory, structural buckling, flutter and the stability of power grids.

## 19. Practice Problems

1. **(Basic)** A skydiver of mass 80 kg falls with air drag $F = kv^2$, where $k = 0.25$ kg/m, so $\dot v = g - (k/m)v^2$. Find the fixed point, show it is stable, and find the characteristic time for approach to it.
2. **(Basic)** The Lotka–Volterra predator–prey model is $\dot x = x(\alpha - by)$, $\dot y = y(cx - \gamma)$, where $x$ is prey and $y$ is predators. Find the coexistence fixed point, linearize, and classify it. Estimate the period of small population cycles for $\alpha = 0.8$ per year and $\gamma = 0.5$ per year.
3. **(Basic)** For a bead on a hoop of radius $R = 0.10$ m spinning at angular speed $\Omega$ (Worked Example 5.2), find the critical speed in rad/s and in rpm. At $\Omega = 2\Omega_c$, find the equilibrium angle and small-oscillation frequency.
4. **(Intermediate)** For the logistic map with $r = 2.8$, find the nonzero fixed point and its multiplier. Describe how a small deviation evolves and estimate how many generations are needed to reduce it by a factor of 1000.
5. **(Intermediate)** In an experiment on a driven nonlinear circuit, period doubling to period 2 occurs at a drive voltage of 1.200 V and to period 4 at 1.520 V. Use Feigenbaum's constant to predict the voltage of the next doubling and the onset of chaos.
6. **(Intermediate)** Taking the Lyapunov time of the inner solar system to be 5 million years, estimate how long it takes an uncertainty of 15 m in the Earth's position to grow to $1.5\times10^{11}$ m (about 1 AU).
7. **(Intermediate)** For the Lorenz system with $\sigma = 10$ and $\beta = 8/3$ at $\rho = 10$: find the fixed points $C_\pm$, decide whether they are stable (using $\rho_H$), and find the factor by which a volume of initial conditions shrinks in 0.5 time units.
8. **(Intermediate)** (a) Find the box-counting dimension of the Sierpinski carpet (divide a square into 9 equal squares, remove the center one, repeat on each remaining square). (b) The Hénon map ($a = 1.4$, $b = 0.3$) has largest Lyapunov exponent 0.419. Find the second exponent and the Kaplan–Yorke dimension.
9. **(Advanced)** For the standard map $p_{n+1} = p_n + K\sin\theta_n$, $\theta_{n+1} = \theta_n + p_{n+1}$ with $K > 0$, show that the map preserves area, find the fixed points with $p = 0$, and determine for what range of $K$ each is stable. (Hint: for an area-preserving 2D map, a fixed point is elliptic, i.e. stable, if the trace of the Jacobian lies strictly between $-2$ and $2$, and hyperbolic if its magnitude exceeds 2.)
10. **(Advanced)** For the logistic map with $r = 3.3$, find the two points of the 2-cycle, verify that they map into each other, compute the cycle's multiplier and its Lyapunov exponent, and state the range of $r$ for which the 2-cycle is stable.

### Solutions

**1.** Setting $\dot v = 0$: $v^* = \sqrt{mg/k} = \sqrt{80\times9.81/0.25} = \sqrt{3139} = 56.0$ m/s (the terminal speed). With $f(v) = g - (k/m)v^2$, $f'(v^*) = -2(k/m)v^* = -2\times(0.25/80)\times56.0 = -0.350$ s⁻¹. Since it is negative, the fixed point is stable. The characteristic time is $1/0.350 = 2.86$ s: velocity deviations from terminal speed shrink by a factor $e$ every 2.9 s.

**2.** Setting both rates to zero with $x, y \neq 0$: $x^* = \gamma/c$ and $y^* = \alpha/b$. The Jacobian is $\begin{pmatrix}\alpha - by & -bx\\ cy & cx - \gamma\end{pmatrix}$; at the fixed point it is $\begin{pmatrix}0 & -b\gamma/c\\ c\alpha/b & 0\end{pmatrix}$, with $\tau = 0$ and $\Delta = \alpha\gamma > 0$. The eigenvalues are $\pm i\sqrt{\alpha\gamma}$: a linear center. (The linear test alone is inconclusive, but the full model has a conserved quantity, $V = cx - \gamma\ln x + by - \alpha\ln y$, so the orbits really are closed.) The period of small cycles is $2\pi/\sqrt{\alpha\gamma} = 2\pi/\sqrt{0.40} = 9.9$ years, close to the roughly ten-year cycles seen in some predator-prey populations.

**3.** $\Omega_c = \sqrt{g/R} = \sqrt{9.81/0.10} = 9.90$ rad/s, which is $9.90\times60/(2\pi) = 94.6$ rpm. At $\Omega = 2\Omega_c$: $\cos\theta^* = g/(R\Omega^2) = 1/4$, so $\theta^* = 75.5°$. The small-oscillation frequency is $\Omega\sin\theta^* = 19.81\times0.968 = 19.2$ rad/s.

**4.** $x^* = 1 - 1/2.8 = 0.643$. Multiplier $2 - r = -0.8$; since $\lvert -0.8\rvert < 1$ the fixed point is stable. A deviation flips sign each generation and shrinks by 20% (oscillatory convergence, "damped overshoot"). Reduction by 1000 requires $0.8^n = 10^{-3}$, so $n = \ln1000/\ln1.25 = 6.908/0.2231 = 31$ generations. This slow convergence reflects the nearness of the period-doubling point $r = 3$.

**5.** Next doubling: $V_3 \approx V_2 + (V_2 - V_1)/\delta = 1.520 + 0.320/4.669 = 1.589$ V. Onset of chaos: $V_\infty \approx V_2 + (V_2 - V_1)/(\delta - 1) = 1.520 + 0.320/3.669 = 1.607$ V. (These estimates assume the doublings are already in the universal geometric regime; in practice the first ratios differ somewhat from $\delta$, as the logistic-map table shows.)

**6.** The error grows as $e^{t/T_L}$, so $t = T_L\ln(\Delta/\delta_0) = 5\text{ Myr}\times\ln(1.5\times10^{11}/15) = 5\text{ Myr}\times\ln(10^{10}) = 5\times23.0 = 115$ Myr. An error of the size of a building grows to the size of Earth's orbit in roughly 100 million years, which is why the planets' positions cannot be computed over geological time spans longer than that.

**7.** $C_\pm = (\pm\sqrt{\beta(\rho - 1)}, \pm\sqrt{\beta(\rho - 1)}, \rho - 1) = (\pm\sqrt{24}, \pm\sqrt{24}, 9) = (\pm4.90, \pm4.90, 9)$. Since $\rho = 10 < \rho_H = 24.74$, $C_\pm$ are stable (steady convection). The volume factor is $e^{-(\sigma + 1 + \beta)\times0.5} = e^{-13.667\times0.5} = e^{-6.83} = 1.08\times10^{-3}$.

**8.** (a) The carpet consists of 8 copies scaled by 1/3: $D = \ln8/\ln3 = 2.0794/1.0986 = 1.893$. (b) The exponents sum to the logarithm of the constant area factor: $\lambda_1 + \lambda_2 = \ln\lvert -b\rvert = \ln0.3 = -1.204$, so $\lambda_2 = -1.204 - 0.419 = -1.623$. Then $j = 1$ and $D_{KY} = 1 + 0.419/1.623 = 1.258$, consistent with the box-counting value of about 1.26.

**9.** The Jacobian is $J = \begin{pmatrix}\partial\theta'/\partial\theta & \partial\theta'/\partial p\\ \partial p'/\partial\theta & \partial p'/\partial p\end{pmatrix} = \begin{pmatrix}1 + K\cos\theta & 1\\ K\cos\theta & 1\end{pmatrix}$, so $\det J = (1 + K\cos\theta) - K\cos\theta = 1$: area is preserved. Fixed points with $p = 0$ require $K\sin\theta = 0$ (so that $p$ is unchanged) and $\theta_{n+1} = \theta_n$, which holds since $p_{n+1} = 0$: $\theta = 0$ and $\theta = \pi$. The trace is $\operatorname{tr}J = 2 + K\cos\theta$. At $\theta = 0$: trace $= 2 + K > 2$ for every $K > 0$, so the point is **hyperbolic** (unstable) for all $K > 0$. At $\theta = \pi$: trace $= 2 - K$, which lies between $-2$ and 2 when $0 < K < 4$. So $(\pi, 0)$ is **elliptic** (stable, surrounded by a regular island) for $0 < K < 4$ and becomes hyperbolic for $K > 4$, via a period-doubling bifurcation (the trace passes through $-2$, so an eigenvalue passes through $-1$).

**10.** $\sqrt{(r + 1)(r - 3)} = \sqrt{4.3\times0.3} = \sqrt{1.29} = 1.1358$, so $p, q = (4.3 \pm 1.1358)/6.6 = 0.8236$ and $0.4794$. Check: $3.3\times0.8236\times0.1764 = 0.4794$ and $3.3\times0.4794\times0.5206 = 0.8236$. ✓ The multiplier is $-r^2 + 2r + 4 = -10.89 + 6.6 + 4 = -0.29$, of magnitude less than 1, so the cycle is stable (deviations shrink by a factor of 0.29 and change sign every two steps). The Lyapunov exponent is $\tfrac12\ln0.29 = -0.619$ per iteration. The 2-cycle is stable for $3 < r < 1 + \sqrt6 = 3.449$, the range in which $\lvert -r^2 + 2r + 4\rvert < 1$.

## 20. Summary

- **Nonlinear** systems violate superposition and can show multiple equilibria, self-sustained oscillations, sudden transitions and chaos.
- **Phase space** is the space of states; the dynamics is a flow, and trajectories of autonomous systems never cross. Chaos in continuous flows requires at least three dimensions; maps can be chaotic in one.
- **Fixed points** are classified by linearization: in 1D flows by the sign of $f'(x^*)$, in maps by whether $\lvert f'(x^*)\rvert < 1$, in 2D by the trace and determinant of the Jacobian.
- **Limit cycles** are isolated closed orbits with an amplitude fixed by the system; the van der Pol oscillator has amplitude 2 for small $\mu$. The **Poincaré–Bendixson theorem** rules out chaos in the plane.
- **Bifurcations** change the qualitative behavior: saddle-node (creation or destruction of equilibria and sudden collapses), transcritical (exchange of stability), pitchfork (symmetry breaking) and Hopf (birth of oscillations, amplitude growing as a square root).
- The **driven damped pendulum** and the **logistic map** reach chaos through a **period-doubling cascade** whose spacing is governed by the universal **Feigenbaum constant** $\delta = 4.6692$, with spatial scaling factor $\alpha = 2.5029$.
- **Lyapunov exponents** measure exponential divergence; a positive largest exponent signals chaos, and the predictability horizon grows only logarithmically with initial precision.
- Dissipative chaotic systems settle onto **strange attractors** with **fractal** geometry, produced by stretching and folding. The **Lorenz attractor** (dimension about 2.06) is the archetype, and it showed that weather has a finite predictability horizon of about two weeks.
- **Poincaré sections** reduce flows to maps and reveal periodic, quasi-periodic and chaotic motion at a glance.
- **Hamiltonian systems** conserve phase-space volume and have no attractors; the **KAM theorem** shows that most invariant tori survive small perturbations, producing mixed phase spaces of regular islands in a chaotic sea. The solar system itself is chaotic on time scales of millions of years.

### Key equations

| Quantity | Equation |
|---|---|
| Stability, 1D flow | $\dot\eta = f'(x^*)\eta$; stable if $f'(x^*) < 0$ |
| Stability, 1D map | $\eta_{n+1} = f'(x^*)\eta_n$; stable if $\lvert f'(x^*)\rvert < 1$ |
| 2D eigenvalues | $\lambda = \tfrac12\left(\tau \pm\sqrt{\tau^2 - 4\Delta}\right)$, $\tau = \operatorname{tr}J$, $\Delta = \det J$ |
| Pendulum separatrix | $\dot\theta = \pm2\omega_0\cos(\theta/2)$ |
| Van der Pol oscillator | $\ddot x - \mu(1 - x^2)\dot x + x = 0$, amplitude $\approx 2$ |
| Saddle-node normal form | $\dot x = r + x^2$ |
| Transcritical normal form | $\dot x = rx - x^2$ |
| Pitchfork normal form | $\dot x = rx - x^3$, $x^* = \pm\sqrt r$ |
| Hopf normal form | $\dot r = \mu r - r^3$, $\dot\theta = \omega$, radius $\sqrt\mu$ |
| Driven damped pendulum | $\ddot\phi + 2\beta\dot\phi + \omega_0^2\sin\phi = \gamma\omega_0^2\cos\omega t$ |
| Logistic map | $x_{n+1} = rx_n(1 - x_n)$, $x^* = 1 - 1/r$, multiplier $2 - r$ |
| Logistic 2-cycle multiplier | $-r^2 + 2r + 4$; stable for $3 < r < 1 + \sqrt6$ |
| Feigenbaum constants | $\delta = 4.669201609$, $\alpha = 2.502907875$ |
| Accumulation estimate | $r_\infty \approx r_n + (r_n - r_{n-1})/(\delta - 1)$ |
| Lyapunov exponent (map) | $\lambda = \lim_{n\to\infty}\frac1n\sum\ln\lvert f'(x_i)\rvert$ |
| Predictability horizon | $t_{\text{pred}} \approx \lambda^{-1}\ln(\Delta/\delta_0)$ |
| Lorenz system | $\dot x = \sigma(y - x)$, $\dot y = x(\rho - z) - y$, $\dot z = xy - \beta z$ |
| Lorenz volume contraction | $V(t) = V(0)e^{-(\sigma + 1 + \beta)t}$ |
| Lorenz Hopf threshold | $\rho_H = \sigma(\sigma + \beta + 3)/(\sigma - \beta - 1)$ |
| Box-counting dimension | $D = \lim_{\varepsilon\to0}\ln N(\varepsilon)/\ln(1/\varepsilon)$ |
| Kaplan–Yorke dimension | $D_{KY} = j + (\lambda_1 + \cdots + \lambda_j)/\lvert\lambda_{j+1}\rvert$ |
| Liouville's theorem | $\nabla\cdot\mathbf F = 0$ for Hamiltonian flows |
| Standard map | $p_{n+1} = p_n + K\sin\theta_n$, $\theta_{n+1} = \theta_n + p_{n+1}$ |
