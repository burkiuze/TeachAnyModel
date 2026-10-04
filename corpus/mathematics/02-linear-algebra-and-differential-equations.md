---
title: Linear Algebra and Differential Equations for Science
field: Mathematics
subfield: Linear Algebra and Differential Equations
level: undergraduate
keywords: [vectors, dot product, cross product, matrices, matrix multiplication, determinant, inverse matrix, systems of linear equations, Gaussian elimination, vector spaces, basis, linear independence, linear transformations, eigenvalues, eigenvectors, diagonalization, symmetric matrices, ordinary differential equations, separable equations, first-order linear ODE, integrating factor, second-order linear ODE, characteristic equation, harmonic oscillator, systems of ODEs, partial differential equations, heat equation, wave equation, Laplace equation, separation of variables, numerical methods, Euler method]
---

# Linear Algebra and Differential Equations for Science

Two branches of mathematics underpin quantitative science more than any others. **Linear algebra** handles systems of many variables — from balancing chemical equations to quantum mechanics (where states are vectors and observables are matrices), computer graphics, data analysis and machine learning. **Differential equations** express physical laws as relationships between quantities and their rates of change — Newton's second law, Maxwell's equations, the Schrödinger equation, chemical kinetics, population dynamics and epidemics are all differential equations.

## Part I — Linear Algebra

### 1. Vectors
A **vector** has magnitude and direction; in components, $\vec v = (v_1, v_2, \ldots, v_n)$.
- **Addition:** component-wise. **Scalar multiplication:** $c\vec v = (cv_1, \ldots, cv_n)$.
- **Magnitude (norm):** $|\vec v| = \sqrt{v_1^2 + \cdots + v_n^2}$.
- **Unit vector:** $\hat v = \vec v/|\vec v|$.

**Dot (scalar) product:**
$$\vec a\cdot\vec b = \sum_ia_ib_i = |\vec a||\vec b|\cos\theta$$
- Zero for perpendicular (orthogonal) vectors.
- Projection of $\vec a$ onto $\vec b$: $\frac{\vec a\cdot\vec b}{|\vec b|}$.
- Physics: work $W = \vec F\cdot\vec d$; power $P = \vec F\cdot\vec v$; flux $\vec E\cdot\vec A$.

**Cross (vector) product** (3D only):
$$\vec a\times\vec b = (a_2b_3 - a_3b_2,\; a_3b_1 - a_1b_3,\; a_1b_2 - a_2b_1), \qquad |\vec a\times\vec b| = |\vec a||\vec b|\sin\theta$$
- Perpendicular to both $\vec a$ and $\vec b$ (right-hand rule); magnitude = area of the parallelogram they span.
- Anticommutative: $\vec a\times\vec b = -\vec b\times\vec a$.
- Physics: torque $\vec\tau = \vec r\times\vec F$; angular momentum $\vec L = \vec r\times\vec p$; magnetic force $\vec F = q\vec v\times\vec B$.

**Example 1.1:** $\vec a = (1, 2, 3)$, $\vec b = (4, 5, 6)$: $\vec a\cdot\vec b = 4 + 10 + 18 = 32$; $\vec a\times\vec b = (12 - 15, 12 - 6, 5 - 8) = (-3, 6, -3)$.

### 2. Matrices
A **matrix** is a rectangular array of numbers; an $m\times n$ matrix has $m$ rows and $n$ columns.

**Matrix multiplication:** $(AB)_{ij} = \sum_kA_{ik}B_{kj}$ (requires columns of $A$ = rows of $B$).
- **Not commutative:** in general $AB \ne BA$. (Quantum mechanics hinges on this: $[\hat x, \hat p] = i\hbar$.)
- Associative and distributive.

**Example 2.1:**
$$\begin{pmatrix}1 & 2\\3 & 4\end{pmatrix}\begin{pmatrix}5 & 6\\7 & 8\end{pmatrix} = \begin{pmatrix}19 & 22\\43 & 50\end{pmatrix}, \qquad \begin{pmatrix}5 & 6\\7 & 8\end{pmatrix}\begin{pmatrix}1 & 2\\3 & 4\end{pmatrix} = \begin{pmatrix}23 & 34\\31 & 46\end{pmatrix}$$

**Special matrices:**
- **Identity** $I$: ones on the diagonal; $AI = IA = A$.
- **Transpose** $A^T$: rows ↔ columns; $(AB)^T = B^TA^T$.
- **Symmetric:** $A = A^T$ (covariance matrices, moment of inertia tensors, Hessians).
- **Orthogonal:** $Q^TQ = I$ (rotations and reflections; preserve lengths and angles).
- **Hermitian** (complex): $A = A^\dagger$ (conjugate transpose) — quantum observables.
- **Unitary:** $U^\dagger U = I$ — quantum time evolution and gates.
- **Diagonal, triangular, sparse** (most entries zero — common in large physical simulations).

### 3. Determinants and Inverses
**Determinant:**
$$\det\begin{pmatrix}a & b\\c & d\end{pmatrix} = ad - bc$$
For 3×3, expand by cofactors (or use the rule of Sarrus). Properties:
- $\det(AB) = \det A\det B$; $\det A^T = \det A$.
- Swapping two rows changes the sign; a row of zeros or two equal rows gives 0.
- Geometric meaning: the factor by which the linear transformation scales areas (2D) or volumes (3D); negative if orientation flips.
- $\det A = 0$ ⇔ $A$ is **singular** (not invertible) ⇔ its columns are linearly dependent.
- Applications: Jacobians in coordinate changes ($dx\,dy = r\,dr\,d\theta$), Slater determinants for fermion wavefunctions, Cramer's rule.

**Inverse:** $AA^{-1} = A^{-1}A = I$, existing iff $\det A \ne 0$. For 2×2:
$$\begin{pmatrix}a & b\\c & d\end{pmatrix}^{-1} = \frac{1}{ad - bc}\begin{pmatrix}d & -b\\-c & a\end{pmatrix}$$

### 4. Systems of Linear Equations
A system $A\vec x = \vec b$ can have **one** solution (if $\det A \ne 0$), **none** (inconsistent), or **infinitely many**.

**Gaussian elimination:** use row operations (swap rows, multiply a row by a nonzero constant, add a multiple of one row to another) to reach row-echelon form, then back-substitute. Computational cost ~$\frac23n^3$ operations for $n$ equations. (Known in China ~2000 years ago — *The Nine Chapters on the Mathematical Art*; named after Gauss.)

**Example 4.1:** solve $x + y + z = 6$, $2y + 5z = -4$, $2x + 5y - z = 27$.
R3 − 2R1: $3y - 3z = 15 \Rightarrow y - z = 5$. With $2y + 5z = -4$: $y = 5 + z \Rightarrow 10 + 2z + 5z = -4 \Rightarrow z = -2$, $y = 3$, $x = 6 - 3 + 2 = 5$. Solution $(5, 3, -2)$.

**Application — balancing chemical equations:** for $a\,\text{C}_3\text{H}_8 + b\,\text{O}_2 \to c\,\text{CO}_2 + d\,\text{H}_2\text{O}$: C: $3a = c$; H: $8a = 2d$; O: $2b = 2c + d$. Setting $a = 1$: $c = 3$, $d = 4$, $b = 5$.

**Other applications:** Kirchhoff's laws for circuits, structural analysis (truss forces), least-squares data fitting ($A^TA\vec x = A^T\vec b$ — linear regression), network flows, Leontief input–output economics, and finite-element methods for solving PDEs.

### 5. Vector Spaces, Basis and Linear Transformations
- A **vector space** is a set closed under addition and scalar multiplication (arrows in 3D, polynomials, functions, quantum states).
- Vectors are **linearly independent** if no one is a linear combination of the others.
- A **basis** is a linearly independent set that spans the space; the number of basis vectors is the **dimension**. The standard basis in 3D: $\hat i, \hat j, \hat k$. In quantum mechanics, energy eigenstates often form a basis.
- **Rank** of a matrix: number of linearly independent rows/columns. **Rank–nullity theorem:** rank + nullity = number of columns.
- **Inner product spaces:** generalize the dot product (for functions, $\langle f, g\rangle = \int f^*g\,dx$) and enable orthogonal expansions — Fourier series expand functions in an orthogonal basis of sines and cosines.
- A **linear transformation** $T(a\vec u + b\vec v) = aT(\vec u) + bT(\vec v)$ is represented by a matrix. Examples: rotation by angle $\theta$ in 2D, $R = \begin{pmatrix}\cos\theta & -\sin\theta\\\sin\theta & \cos\theta\end{pmatrix}$; scaling; shear; projection; reflection. Composing transformations = multiplying matrices (computer graphics uses 4×4 matrices for 3D transformations).

### 6. Eigenvalues and Eigenvectors
A nonzero vector $\vec v$ is an **eigenvector** of $A$ with **eigenvalue** $\lambda$ if
$$\boxed{A\vec v = \lambda\vec v}$$
— the transformation merely stretches $\vec v$ by $\lambda$ without changing its direction.

**Finding them:** solve the **characteristic equation** $\det(A - \lambda I) = 0$ for $\lambda$, then solve $(A - \lambda I)\vec v = 0$ for each $\lambda$.

**Example 6.1:** $A = \begin{pmatrix}4 & 1\\2 & 3\end{pmatrix}$. $\det\begin{pmatrix}4 - \lambda & 1\\2 & 3 - \lambda\end{pmatrix} = \lambda^2 - 7\lambda + 10 = (\lambda - 5)(\lambda - 2) = 0$.
$\lambda_1 = 5$: $\begin{pmatrix}-1 & 1\\2 & -2\end{pmatrix}\vec v = 0 \Rightarrow \vec v_1 = (1, 1)$.
$\lambda_2 = 2$: $\begin{pmatrix}2 & 1\\2 & 1\end{pmatrix}\vec v = 0 \Rightarrow \vec v_2 = (1, -2)$.
Checks: trace $= 4 + 3 = 7 = \lambda_1 + \lambda_2$; determinant $= 12 - 2 = 10 = \lambda_1\lambda_2$.

**Properties:**
- Sum of eigenvalues = trace; product = determinant.
- **Real symmetric (and Hermitian) matrices have real eigenvalues and orthogonal eigenvectors** (spectral theorem) — which is why quantum observables are Hermitian: measurement outcomes (eigenvalues) are real.
- **Diagonalization:** if $A$ has $n$ independent eigenvectors, $A = PDP^{-1}$ with $D$ diagonal (eigenvalues) and $P$'s columns the eigenvectors. Then $A^k = PD^kP^{-1}$ and $e^{At} = Pe^{Dt}P^{-1}$ — simplifying repeated transformations and solving linear ODE systems.

**Applications of eigenvalue problems:**
- **Quantum mechanics:** the time-independent Schrödinger equation $\hat H\psi = E\psi$ is an eigenvalue equation; energy levels are eigenvalues.
- **Vibrations and normal modes:** coupled oscillators, molecular vibrations (IR spectroscopy), building and bridge resonances: $(K - \omega^2M)\vec x = 0$.
- **Principal axes:** the inertia tensor's eigenvectors are the axes about which an object spins without wobbling; the stress tensor's eigenvectors give principal stresses.
- **Stability analysis:** eigenvalues of the Jacobian at an equilibrium determine whether perturbations grow or decay.
- **Markov chains:** steady-state distributions are eigenvectors with eigenvalue 1. Google's original **PageRank** algorithm ranks web pages by the dominant eigenvector of the link matrix.
- **Principal component analysis (PCA):** eigenvectors of the covariance matrix give the directions of greatest variance in data — used for dimensionality reduction in genomics, image analysis and machine learning. Closely related: the **singular value decomposition** $A = U\Sigma V^T$, used in data compression and recommendation systems.
- **Population models:** the Leslie matrix's dominant eigenvalue gives the long-term growth rate.

## Part II — Differential Equations

### 7. Basic Concepts
A **differential equation** relates a function to its derivatives.
- **Ordinary (ODE):** one independent variable (e.g. time). **Partial (PDE):** several (space and time).
- **Order:** highest derivative present.
- **Linear** if the unknown function and its derivatives appear linearly (no products, powers or nonlinear functions of them); otherwise **nonlinear**.
- A unique solution requires **initial conditions** (or boundary conditions); an $n$th-order ODE needs $n$ conditions.

### 8. First-Order ODEs

**Separable equations** $\frac{dy}{dx} = g(x)h(y)$: separate and integrate, $\int\frac{dy}{h(y)} = \int g(x)\,dx$.

**Example 8.1 — exponential decay:** $\frac{dN}{dt} = -\lambda N \Rightarrow \int\frac{dN}{N} = -\lambda\int dt \Rightarrow \ln N = -\lambda t + C \Rightarrow N = N_0e^{-\lambda t}$.

**Example 8.2 — logistic growth:** $\frac{dN}{dt} = rN\left(1 - \frac NK\right)$. Using partial fractions:
$$N(t) = \frac{K}{1 + \left(\frac{K - N_0}{N_0}\right)e^{-rt}}$$
Also describes autocatalytic reactions and the spread of innovations or epidemics (early phase).

**Example 8.3 — Newton's law of cooling:** $\frac{dT}{dt} = -k(T - T_{\text{env}}) \Rightarrow T = T_{\text{env}} + (T_0 - T_{\text{env}})e^{-kt}$.

**Example 8.4 — second-order kinetics:** $\frac{d[A]}{dt} = -k[A]^2 \Rightarrow \frac{1}{[A]} = \frac{1}{[A]_0} + kt$.

**Linear first-order equations** $\frac{dy}{dx} + P(x)y = Q(x)$: multiply by the **integrating factor** $\mu = e^{\int P\,dx}$, giving $\frac{d}{dx}(\mu y) = \mu Q$.

**Example 8.5 — RC circuit charging:** $R\frac{dq}{dt} + \frac qC = \mathcal E$. Integrating factor $e^{t/RC}$: $q = C\mathcal E(1 - e^{-t/RC})$.

**Example 8.6 — falling object with linear drag:** $m\frac{dv}{dt} = mg - bv \Rightarrow v(t) = \frac{mg}{b}(1 - e^{-bt/m})$, approaching terminal velocity $mg/b$.

### 9. Second-Order Linear ODEs with Constant Coefficients
$$ay'' + by' + cy = f(t)$$

**Homogeneous case ($f = 0$):** try $y = e^{rt}$ → **characteristic equation** $ar^2 + br + c = 0$:
1. **Two distinct real roots** $r_1, r_2$: $y = C_1e^{r_1t} + C_2e^{r_2t}$ (overdamped).
2. **Repeated root** $r$: $y = (C_1 + C_2t)e^{rt}$ (critically damped).
3. **Complex roots** $r = \alpha \pm i\beta$: $y = e^{\alpha t}(C_1\cos\beta t + C_2\sin\beta t)$ (underdamped/oscillatory).

**The harmonic oscillator:** $m\ddot x + kx = 0 \Rightarrow r = \pm i\omega$, $\omega = \sqrt{k/m}$: $x = A\cos(\omega t + \phi)$ — springs, pendulums (small angles), LC circuits, molecular vibrations, and (quantized) the electromagnetic field.

**Damped oscillator:** $m\ddot x + b\dot x + kx = 0$, with $r = -\gamma \pm\sqrt{\gamma^2 - \omega_0^2}$, $\gamma = b/2m$.

**Non-homogeneous ($f \ne 0$):** general solution = homogeneous solution + a **particular solution** (by undetermined coefficients or variation of parameters). For sinusoidal driving $F_0\cos\omega t$, the steady-state response is a sinusoid at the driving frequency with amplitude peaking near $\omega_0$ — **resonance**.

**Principle of superposition:** for linear homogeneous equations, any linear combination of solutions is a solution — fundamental to waves, circuits, and quantum mechanics.

### 10. Systems of ODEs
$$\frac{d\vec x}{dt} = A\vec x$$
Solutions combine eigenvectors: $\vec x(t) = \sum c_i\vec v_ie^{\lambda_it}$. The eigenvalues classify the equilibrium at the origin:

| Eigenvalues | Behavior |
|---|---|
| Both real negative | Stable node (decay) |
| Both real positive | Unstable node |
| Real, opposite signs | Saddle (unstable) |
| Complex, negative real part | Stable spiral (damped oscillation) |
| Complex, positive real part | Unstable spiral |
| Purely imaginary | Center (undamped oscillation) |

**Nonlinear systems** are analyzed by **linearizing** near equilibria (using the Jacobian matrix) and studying phase portraits.

**Examples:**
- **Lotka–Volterra predator–prey:** $\dot x = \alpha x - \beta xy$, $\dot y = \delta xy - \gamma y$ — closed orbits (populations cycle).
- **SIR epidemic model:** $\dot S = -\beta SI/N$, $\dot I = \beta SI/N - \gamma I$, $\dot R = \gamma I$. The **basic reproduction number** $R_0 = \beta/\gamma$: an epidemic grows if $R_0S/N > 1$; herd immunity threshold $1 - 1/R_0$.
- **Chemical kinetics networks** and enzyme kinetics (Michaelis–Menten derived via the steady-state approximation).
- **Radioactive decay chains** (Bateman equations).
- **Coupled oscillators and normal modes.**
- **Chaos:** nonlinear systems with three or more variables can be chaotic — the **Lorenz system** (1963), a simplified convection model: $\dot x = \sigma(y - x)$, $\dot y = x(\rho - z) - y$, $\dot z = xy - \beta z$. Sensitive dependence on initial conditions (the "butterfly effect") limits weather forecasting to about two weeks.

### 11. Partial Differential Equations
The great equations of mathematical physics:

| Equation | Form | Describes |
|---|---|---|
| **Heat (diffusion) equation** | $\frac{\partial u}{\partial t} = D\nabla^2u$ | Heat conduction, diffusion of molecules, Brownian motion probability, option pricing (Black–Scholes) |
| **Wave equation** | $\frac{\partial^2u}{\partial t^2} = c^2\nabla^2u$ | Vibrating strings, sound, light, seismic waves |
| **Laplace's equation** | $\nabla^2u = 0$ | Steady-state temperature, electrostatic potential in charge-free regions, ideal fluid flow |
| **Poisson's equation** | $\nabla^2\phi = -\rho/\varepsilon_0$ (or $4\pi G\rho$) | Electrostatics, Newtonian gravity |
| **Schrödinger equation** | $i\hbar\frac{\partial\psi}{\partial t} = -\frac{\hbar^2}{2m}\nabla^2\psi + V\psi$ | Quantum systems |
| **Navier–Stokes equations** | $\rho\left(\frac{\partial\vec v}{\partial t} + \vec v\cdot\nabla\vec v\right) = -\nabla p + \mu\nabla^2\vec v + \vec f$ | Fluid flow, weather, aerodynamics |
| **Maxwell's equations** | (four coupled PDEs) | Electromagnetism |

**Separation of variables:** assume $u(x, t) = X(x)T(t)$, reducing the PDE to ODEs. For the heat equation on a rod of length $L$ with ends held at zero temperature:
$$u(x, t) = \sum_{n=1}^\infty B_n\sin\left(\frac{n\pi x}{L}\right)e^{-D(n\pi/L)^2t}$$
with $B_n$ from the Fourier series of the initial temperature profile. Higher spatial modes decay faster — temperature profiles smooth out. For the wave equation on a string, the analogous modes oscillate at $f_n = \frac{nc}{2L}$ — musical harmonics.

**Diffusion scaling:** the typical distance diffused in time $t$ is $\sim\sqrt{Dt}$ (exactly $\langle x^2\rangle = 2Dt$ in 1D). For a small molecule in water ($D \sim 10^{-9}$ m²/s), crossing a 10 μm cell takes ~0.05 s, but crossing 1 cm takes ~14 hours — which is why large organisms need circulatory systems.

### 12. Numerical Methods
Most real-world differential equations have no closed-form solution and are solved numerically.
- **Euler's method:** $y_{n+1} = y_n + hf(t_n, y_n)$ — simple but inaccurate (error ∝ step size $h$) and can be unstable.
- **Runge–Kutta methods** (especially the classic fourth-order RK4, error ∝ $h^4$) — workhorses of scientific computing; adaptive step-size variants (RK45, Dormand–Prince — used in `scipy.integrate.solve_ivp` and MATLAB's `ode45`).
- **Symplectic integrators** (velocity Verlet, leapfrog) conserve energy over long times — used in molecular dynamics and planetary orbit simulations.
- **Stiff equations** (widely separated timescales, as in combustion chemistry) require implicit methods (backward Euler, BDF).
- **PDEs:** finite differences, finite elements (engineering structures, heat flow), finite volumes (fluid dynamics), spectral methods (weather and climate models).

**Example 12.1 (Euler's method):** $y' = y$, $y(0) = 1$, step $h = 0.1$, to $t = 1$: $y_{10} = 1.1^{10} \approx 2.594$ vs. exact $e \approx 2.718$ (4.6% error). With $h = 0.01$: $1.01^{100} \approx 2.705$ (0.5% error).

## 13. Summary

| Concept | Key formula |
|---|---|
| Dot product | $\vec a\cdot\vec b = \lvert a\rvert\lvert b\rvert\cos\theta$ |
| Cross product | $\lvert\vec a\times\vec b\rvert = \lvert a\rvert\lvert b\rvert\sin\theta$ |
| 2×2 determinant | $ad - bc$ |
| Inverse exists | $\det A \ne 0$ |
| Eigenvalue equation | $A\vec v = \lambda\vec v$; $\det(A - \lambda I) = 0$ |
| Trace/determinant | $\sum\lambda_i = \text{tr}A$; $\prod\lambda_i = \det A$ |
| Exponential decay | $y' = -ky \Rightarrow y = y_0e^{-kt}$ |
| Integrating factor | $\mu = e^{\int P\,dx}$ |
| Characteristic equation | $ar^2 + br + c = 0$ |
| Harmonic oscillator | $\ddot x + \omega^2x = 0 \Rightarrow x = A\cos(\omega t + \phi)$ |
| Heat equation | $u_t = D\nabla^2u$ |
| Wave equation | $u_{tt} = c^2\nabla^2u$ |
| Diffusion distance | $\sim\sqrt{2Dt}$ |
