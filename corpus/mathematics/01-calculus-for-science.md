---
title: Calculus for Science - Limits, Derivatives, Integrals, Series and Multivariable Calculus
field: Mathematics
subfield: Calculus
level: high-school to undergraduate
keywords: [limits, continuity, derivative, differentiation rules, chain rule, implicit differentiation, applications of derivatives, optimization, related rates, integral, fundamental theorem of calculus, integration techniques, substitution, integration by parts, applications of integrals, Taylor series, Maclaurin series, approximations, partial derivatives, gradient, multiple integrals, vector calculus, divergence, curl, line integrals]
---

# Calculus for Science: Limits, Derivatives, Integrals, Series and Multivariable Calculus

Calculus is the mathematics of change and accumulation. Developed independently by **Isaac Newton** (who called it the "method of fluxions", from the 1660s) and **Gottfried Wilhelm Leibniz** (who published first, in 1684, and whose notation — $dy/dx$ and $\int$ — we still use), it became the language of physics and is indispensable in chemistry, biology, engineering, economics and data science. Newton invented it largely to formulate his laws of motion and gravitation.

The two central ideas are:
- **The derivative:** the instantaneous rate of change (slope of a curve).
- **The integral:** accumulation (area under a curve).
The **Fundamental Theorem of Calculus** reveals that they are inverse operations.

## 1. Limits and Continuity

The **limit** $\lim_{x\to a}f(x) = L$ means $f(x)$ can be made arbitrarily close to $L$ by taking $x$ sufficiently close to $a$ (but not equal to $a$). Formally (Cauchy–Weierstrass ε–δ definition): for every $\varepsilon > 0$ there exists $\delta > 0$ such that $0 < |x - a| < \delta \Rightarrow |f(x) - L| < \varepsilon$.

**Important limits:**
$$\lim_{x\to0}\frac{\sin x}{x} = 1, \qquad \lim_{x\to0}\frac{e^x - 1}{x} = 1, \qquad \lim_{n\to\infty}\left(1 + \frac1n\right)^n = e \approx 2.71828, \qquad \lim_{x\to\infty}\frac1x = 0$$

The number $e$ arises naturally from continuous compounding: $1 invested at 100% annual interest compounded continuously grows to $e \approx \$2.718$ after one year.

**Continuity:** $f$ is continuous at $a$ if $\lim_{x\to a}f(x) = f(a)$. Polynomials, exponentials, sine and cosine are continuous everywhere. The **intermediate value theorem** guarantees that a continuous function taking values $f(a)$ and $f(b)$ takes every value in between (useful for proving roots exist).

**L'Hôpital's rule:** for indeterminate forms $0/0$ or $\infty/\infty$, $\lim\frac{f(x)}{g(x)} = \lim\frac{f'(x)}{g'(x)}$ (if the latter exists).

## 2. The Derivative

### Definition
$$f'(x) = \frac{df}{dx} = \lim_{h\to0}\frac{f(x + h) - f(x)}{h}$$
Geometrically: the slope of the tangent line. Physically: an instantaneous rate — velocity is the derivative of position ($v = dx/dt$), acceleration is the derivative of velocity, current is the derivative of charge ($I = dQ/dt$), reaction rate is the derivative of concentration, marginal cost is the derivative of total cost.

**Example from the definition:** for $f(x) = x^2$:
$\frac{(x + h)^2 - x^2}{h} = \frac{2xh + h^2}{h} = 2x + h \to 2x$.

### Differentiation rules

| Rule | Formula |
|---|---|
| Constant | $\frac{d}{dx}c = 0$ |
| Power | $\frac{d}{dx}x^n = nx^{n-1}$ (any real $n$) |
| Constant multiple | $(cf)' = cf'$ |
| Sum | $(f + g)' = f' + g'$ |
| Product | $(fg)' = f'g + fg'$ |
| Quotient | $\left(\frac fg\right)' = \frac{f'g - fg'}{g^2}$ |
| Chain | $\frac{d}{dx}f(g(x)) = f'(g(x))\,g'(x)$, or $\frac{dy}{dx} = \frac{dy}{du}\frac{du}{dx}$ |

### Derivatives of common functions

| $f(x)$ | $f'(x)$ |
|---|---|
| $e^x$ | $e^x$ (the only function, up to a constant multiple, equal to its own derivative) |
| $a^x$ | $a^x\ln a$ |
| $\ln x$ | $1/x$ |
| $\log_a x$ | $\frac{1}{x\ln a}$ |
| $\sin x$ | $\cos x$ |
| $\cos x$ | $-\sin x$ |
| $\tan x$ | $\sec^2x$ |
| $\arcsin x$ | $\frac{1}{\sqrt{1 - x^2}}$ |
| $\arctan x$ | $\frac{1}{1 + x^2}$ |
| $\sinh x$ | $\cosh x$ |

(Trigonometric derivatives require angles in **radians**.)

### Worked examples
1. $\frac{d}{dx}(3x^4 - 5x^2 + 7) = 12x^3 - 10x$.
2. $\frac{d}{dx}(x^2e^x) = 2xe^x + x^2e^x = xe^x(2 + x)$ (product rule).
3. $\frac{d}{dx}\sin(3x^2) = \cos(3x^2)\cdot6x$ (chain rule).
4. $\frac{d}{dx}e^{-kt} = -ke^{-kt}$ (radioactive decay rate).
5. $\frac{d}{dx}\ln(x^2 + 1) = \frac{2x}{x^2 + 1}$.
6. **Implicit differentiation:** for $x^2 + y^2 = 25$, differentiate both sides: $2x + 2y\frac{dy}{dx} = 0 \Rightarrow \frac{dy}{dx} = -\frac xy$. At (3, 4), slope = −3/4.
7. **Logarithmic differentiation:** for $y = x^x$: $\ln y = x\ln x \Rightarrow \frac{y'}{y} = \ln x + 1 \Rightarrow y' = x^x(\ln x + 1)$.

### Higher derivatives
$f''(x)$ describes **concavity**: $f'' > 0$ concave up (like a cup), $f'' < 0$ concave down. Inflection points occur where concavity changes. In physics, $\frac{d^2x}{dt^2}$ is acceleration; Newton's second law $F = m\frac{d^2x}{dt^2}$ is a second-order differential equation.

## 3. Applications of Derivatives

### Optimization
At a local maximum or minimum of a differentiable function, $f'(x) = 0$ (critical point). Second-derivative test: $f'' > 0$ → minimum; $f'' < 0$ → maximum. For a closed interval, also check endpoints.

**Example 3.1 — Maximum area:** a farmer has 100 m of fence to enclose a rectangle. Area $A = x(50 - x)$; $A' = 50 - 2x = 0 \Rightarrow x = 25$ m. A square of 625 m² maximizes area.

**Example 3.2 — Projectile range:** $R(\theta) = \frac{v_0^2\sin2\theta}{g}$; $R'(\theta) = \frac{2v_0^2\cos2\theta}{g} = 0 \Rightarrow \theta = 45°$.

**Example 3.3 — Minimizing surface area of a can** with volume $V$: $A = 2\pi r^2 + 2\pi rh$, $h = V/(\pi r^2)$, so $A = 2\pi r^2 + 2V/r$. $A' = 4\pi r - 2V/r^2 = 0 \Rightarrow r^3 = V/(2\pi)$, giving $h = 2r$ — height equals diameter.

Optimization principles appear throughout science: Fermat's principle of least time in optics, minimum potential energy at equilibrium, maximum entropy, the principle of least action, and gradient descent in machine learning.

### Related rates
**Example 3.4:** a spherical balloon is inflated at 100 cm³/s. How fast does its radius grow when $r = 10$ cm? $V = \frac43\pi r^3 \Rightarrow \frac{dV}{dt} = 4\pi r^2\frac{dr}{dt} \Rightarrow \frac{dr}{dt} = \frac{100}{4\pi(100)} \approx 0.080$ cm/s.

### Linear approximation and differentials
Near $x = a$: $f(x) \approx f(a) + f'(a)(x - a)$. Example: $\sqrt{4.1} \approx 2 + \frac{1}{4}(0.1) = 2.025$ (exact 2.0248...). Error propagation in measurements uses differentials: if $y = f(x)$, then $\delta y \approx |f'(x)|\delta x$.

### Newton's method
To solve $f(x) = 0$, iterate $x_{n+1} = x_n - \frac{f(x_n)}{f'(x_n)}$. Converges very fast (quadratically) near a simple root. Example: $\sqrt2$ from $f(x) = x^2 - 2$, starting at $x_0 = 1$: 1.5, 1.41667, 1.4142157, 1.41421356...

## 4. The Integral

### Definite integral as accumulated area
$$\int_a^bf(x)\,dx = \lim_{n\to\infty}\sum_{i=1}^nf(x_i^*)\Delta x$$
(Riemann sum). Represents signed area under the curve; physically, accumulation: displacement = $\int v\,dt$, work = $\int F\,dx$, charge = $\int I\,dt$, total drug exposure = $\int C(t)\,dt$ (area under the curve, AUC, in pharmacology).

### Antiderivatives (indefinite integrals)
$F$ is an antiderivative of $f$ if $F' = f$: $\int f(x)\,dx = F(x) + C$.

| $\int f(x)\,dx$ | Result |
|---|---|
| $\int x^n\,dx$ ($n \ne -1$) | $\frac{x^{n+1}}{n+1} + C$ |
| $\int\frac1x\,dx$ | $\ln\lvert x\rvert + C$ |
| $\int e^{ax}\,dx$ | $\frac1ae^{ax} + C$ |
| $\int\sin x\,dx$ | $-\cos x + C$ |
| $\int\cos x\,dx$ | $\sin x + C$ |
| $\int\sec^2x\,dx$ | $\tan x + C$ |
| $\int\frac{1}{1 + x^2}\,dx$ | $\arctan x + C$ |
| $\int\frac{1}{\sqrt{1 - x^2}}\,dx$ | $\arcsin x + C$ |

### The Fundamental Theorem of Calculus
**Part 1:** if $F(x) = \int_a^xf(t)\,dt$, then $F'(x) = f(x)$ — integration and differentiation are inverse processes.
**Part 2:** if $F' = f$, then
$$\boxed{\int_a^bf(x)\,dx = F(b) - F(a)}$$
This transformed calculation of areas, volumes and accumulations from laborious summations into straightforward antidifferentiation.

**Example:** $\int_0^2x^2\,dx = \frac{x^3}{3}\Big|_0^2 = \frac83$.

### Integration techniques
- **Substitution** (reverse chain rule): $\int f(g(x))g'(x)\,dx = \int f(u)\,du$. Example: $\int2xe^{x^2}dx$, with $u = x^2$: $= e^{x^2} + C$.
- **Integration by parts** (reverse product rule): $\int u\,dv = uv - \int v\,du$. Example: $\int xe^x\,dx = xe^x - \int e^x\,dx = e^x(x - 1) + C$. Mnemonic for choosing $u$: **LIATE** (Logarithmic, Inverse trig, Algebraic, Trigonometric, Exponential).
- **Partial fractions:** $\int\frac{1}{x^2 - 1}dx = \frac12\int\left(\frac{1}{x - 1} - \frac{1}{x + 1}\right)dx = \frac12\ln\left|\frac{x - 1}{x + 1}\right| + C$. Used in kinetics (integrating second-order rate laws) and logistic growth.
- **Trigonometric substitution:** for $\sqrt{a^2 - x^2}$, let $x = a\sin\theta$, etc.
- **Numerical integration** (trapezoidal rule, Simpson's rule, Monte Carlo) when no closed form exists — e.g. $\int e^{-x^2}dx$ has no elementary antiderivative, although $\int_{-\infty}^\infty e^{-x^2}dx = \sqrt\pi$ (the Gaussian integral, central to probability and quantum mechanics).

### Applications of integration
- **Area between curves:** $\int_a^b[f(x) - g(x)]\,dx$.
- **Volumes of revolution:** disk method $V = \pi\int_a^b[f(x)]^2dx$. Example: sphere of radius $R$: $V = \pi\int_{-R}^R(R^2 - x^2)dx = \frac43\pi R^3$.
- **Average value:** $\bar f = \frac{1}{b - a}\int_a^bf(x)\,dx$. (RMS values in AC circuits.)
- **Work:** stretching a spring: $W = \int_0^xkx'dx' = \frac12kx^2$.
- **Center of mass, moments of inertia:** $I = \int r^2\,dm$.
- **Probability:** for a probability density $p(x)$, $P(a \le X \le b) = \int_a^bp(x)\,dx$; expectation $E[X] = \int xp(x)\,dx$.
- **Arc length:** $L = \int_a^b\sqrt{1 + [f'(x)]^2}\,dx$.
- **Improper integrals:** escape velocity work $\int_R^\infty\frac{GMm}{r^2}dr = \frac{GMm}{R}$.

## 5. Exponential and Logarithmic Functions in Science

The equation $\frac{dy}{dt} = ky$ (rate proportional to amount) has solution $y = y_0e^{kt}$:
- $k > 0$: **exponential growth** — bacterial populations, compound interest, early epidemics, nuclear chain reactions. Doubling time $t_d = \ln2/k$.
- $k < 0$: **exponential decay** — radioactive decay, first-order chemical reactions, drug elimination, capacitor discharge, Newton's law of cooling, light absorption (Beer–Lambert). Half-life $t_{1/2} = \ln2/|k|$.

**Logarithms** convert multiplication into addition and compress wide ranges: pH, decibels, Richter/moment magnitude, stellar magnitudes, the Arrhenius plot ($\ln k$ vs $1/T$). Key identities: $\ln(ab) = \ln a + \ln b$; $\ln(a^n) = n\ln a$; $\log_ax = \frac{\ln x}{\ln a}$; $e^{\ln x} = x$.

## 6. Sequences and Series

### Geometric series
$$\sum_{n=0}^\infty ar^n = \frac{a}{1 - r}\quad(|r| < 1)$$
Example: $1 + \frac12 + \frac14 + \cdots = 2$ — resolving Zeno's paradox of Achilles and the tortoise. Applications: repeated drug dosing (steady-state levels), bouncing balls, multiple reflections.

### Convergence
The **harmonic series** $\sum\frac1n$ diverges (slowly — the partial sum reaches only ~14.4 after a million terms), while $\sum\frac{1}{n^2} = \frac{\pi^2}{6}$ (Euler's solution of the Basel problem, 1734). Tests: comparison, ratio, root, integral, alternating series.

### Taylor and Maclaurin series
A smooth function can be expanded around $x = a$:
$$f(x) = \sum_{n=0}^\infty\frac{f^{(n)}(a)}{n!}(x - a)^n = f(a) + f'(a)(x - a) + \frac{f''(a)}{2!}(x - a)^2 + \cdots$$
(Maclaurin series: $a = 0$.)

| Function | Maclaurin series | Converges for |
|---|---|---|
| $e^x$ | $1 + x + \frac{x^2}{2!} + \frac{x^3}{3!} + \cdots$ | All $x$ |
| $\sin x$ | $x - \frac{x^3}{3!} + \frac{x^5}{5!} - \cdots$ | All $x$ |
| $\cos x$ | $1 - \frac{x^2}{2!} + \frac{x^4}{4!} - \cdots$ | All $x$ |
| $\ln(1 + x)$ | $x - \frac{x^2}{2} + \frac{x^3}{3} - \cdots$ | $-1 < x \le 1$ |
| $\frac{1}{1 - x}$ | $1 + x + x^2 + x^3 + \cdots$ | $\lvert x\rvert < 1$ |
| $(1 + x)^n$ | $1 + nx + \frac{n(n-1)}{2!}x^2 + \cdots$ (binomial series) | $\lvert x\rvert < 1$ |

**Approximations used constantly in physics:**
- **Small-angle approximation:** $\sin\theta \approx \theta$, $\cos\theta \approx 1 - \theta^2/2$, $\tan\theta \approx \theta$ (pendulum, optics, diffraction).
- **Binomial approximation:** $(1 + x)^n \approx 1 + nx$ for small $x$. Relativistic kinetic energy: $(\gamma - 1)mc^2 \approx \frac12mv^2$ since $\gamma = (1 - v^2/c^2)^{-1/2} \approx 1 + \frac{v^2}{2c^2}$.
- **Potential near equilibrium:** $U(x) \approx U(x_0) + \frac12U''(x_0)(x - x_0)^2$ — the origin of simple harmonic motion everywhere.
- **Gravitational potential energy near the surface:** $-\frac{GMm}{R + h} \approx -\frac{GMm}{R} + mgh$.
- **Euler's formula:** combining the series of $e^{ix}$, $\cos x$ and $\sin x$:
$$e^{ix} = \cos x + i\sin x, \qquad e^{i\pi} + 1 = 0$$
— Euler's identity, linking five fundamental constants. Complex exponentials simplify oscillations, waves, AC circuits and quantum mechanics.

**Fourier series:** periodic functions can be expanded in sines and cosines, $f(x) = \frac{a_0}{2} + \sum[a_n\cos(nx) + b_n\sin(nx)]$ (Joseph Fourier, 1807, studying heat flow). The **Fourier transform** generalizes this to non-periodic functions and is fundamental in signal processing, spectroscopy (FT-NMR, FTIR), crystallography, image compression (JPEG uses the related discrete cosine transform), and quantum mechanics (position ↔ momentum).

## 7. Multivariable Calculus

### Partial derivatives
For $f(x, y)$, the partial derivative $\frac{\partial f}{\partial x}$ treats $y$ as constant. Example: $f = x^2y + \sin y$: $f_x = 2xy$, $f_y = x^2 + \cos y$. Mixed partials are equal for smooth functions: $f_{xy} = f_{yx}$ (Clairaut's theorem) — the basis of thermodynamic Maxwell relations.

**Total differential:** $df = \frac{\partial f}{\partial x}dx + \frac{\partial f}{\partial y}dy$. For the ideal gas $V(T, P) = nRT/P$: $dV = \frac{nR}{P}dT - \frac{nRT}{P^2}dP$.

**Error propagation:** for $q = f(x, y)$ with independent uncertainties, $\sigma_q^2 \approx \left(\frac{\partial f}{\partial x}\right)^2\sigma_x^2 + \left(\frac{\partial f}{\partial y}\right)^2\sigma_y^2$.

### The gradient
$$\nabla f = \left(\frac{\partial f}{\partial x}, \frac{\partial f}{\partial y}, \frac{\partial f}{\partial z}\right)$$
points in the direction of steepest increase; its magnitude is the rate of increase. It is perpendicular to level curves/surfaces (contour lines). Physics: force is the negative gradient of potential energy, $\vec F = -\nabla U$; electric field $\vec E = -\nabla V$; heat flows down temperature gradients (Fourier's law $\vec q = -k\nabla T$); diffusion down concentration gradients (Fick's law). **Gradient descent** — repeatedly stepping opposite to the gradient — is how neural networks are trained.

**Constrained optimization (Lagrange multipliers):** to extremize $f$ subject to $g = 0$, solve $\nabla f = \lambda\nabla g$. Used to derive the Boltzmann distribution (maximizing entropy subject to fixed energy and particle number).

### Multiple integrals
$$\iint_Rf(x, y)\,dA, \qquad \iiint_Vf(x, y, z)\,dV$$
compute total mass, charge, probability, volume. Coordinate systems:
- Polar: $dA = r\,dr\,d\theta$. Example: $\int_{-\infty}^\infty e^{-x^2}dx = \sqrt\pi$ is proved by squaring and switching to polar coordinates.
- Cylindrical: $dV = r\,dr\,d\theta\,dz$.
- Spherical: $dV = r^2\sin\theta\,dr\,d\theta\,d\phi$ (used for atoms, planets, radiation).

### Vector calculus
Operators on vector fields $\vec F$:
- **Divergence** $\nabla\cdot\vec F$: net outflow (source strength) per volume.
- **Curl** $\nabla\times\vec F$: circulation (rotation) per area.
- **Laplacian** $\nabla^2f = \nabla\cdot\nabla f$: appears in the heat equation, wave equation, Schrödinger equation, and Poisson's equation for gravity and electrostatics.

**Integral theorems** (generalizations of the Fundamental Theorem):
- **Gradient theorem:** $\int_A^B\nabla f\cdot d\vec r = f(B) - f(A)$ (conservative forces; path-independence).
- **Green's theorem** (2D): $\oint_C(P\,dx + Q\,dy) = \iint_R\left(\frac{\partial Q}{\partial x} - \frac{\partial P}{\partial y}\right)dA$.
- **Stokes' theorem:** $\oint_C\vec F\cdot d\vec l = \iint_S(\nabla\times\vec F)\cdot d\vec A$.
- **Divergence (Gauss's) theorem:** $\oiint_S\vec F\cdot d\vec A = \iiint_V(\nabla\cdot\vec F)\,dV$.
These convert Maxwell's equations between integral and differential forms and underlie conservation laws (continuity equations: $\frac{\partial\rho}{\partial t} + \nabla\cdot\vec J = 0$).

## 8. Summary

| Concept | Key formula |
|---|---|
| Derivative | $f'(x) = \lim_{h\to0}\frac{f(x+h) - f(x)}{h}$ |
| Power rule | $(x^n)' = nx^{n-1}$ |
| Chain rule | $(f\circ g)' = f'(g)\,g'$ |
| Product rule | $(fg)' = f'g + fg'$ |
| FTC | $\int_a^bf\,dx = F(b) - F(a)$ |
| By parts | $\int u\,dv = uv - \int v\,du$ |
| Exponential growth/decay | $y = y_0e^{kt}$; $t_{1/2} = \ln2/\lvert k\rvert$ |
| Taylor series | $f(x) = \sum f^{(n)}(a)(x-a)^n/n!$ |
| Euler's formula | $e^{ix} = \cos x + i\sin x$ |
| Gradient | $\nabla f$ points uphill; $\vec F = -\nabla U$ |
| Divergence theorem | $\oint\vec F\cdot d\vec A = \int\nabla\cdot\vec F\,dV$ |
| Stokes' theorem | $\oint\vec F\cdot d\vec l = \int(\nabla\times\vec F)\cdot d\vec A$ |
