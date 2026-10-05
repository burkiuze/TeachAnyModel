---
title: Time-Dependent Perturbation Theory, Transitions and Scattering
field: Physics
subfield: Quantum Mechanics
level: high-school to undergraduate
keywords: [time-dependent perturbation theory, interaction picture, Dyson series, transition probability, Rabi oscillations, Fermi's golden rule, density of states, electric dipole approximation, selection rules, Einstein coefficients, spontaneous emission, radiative lifetime, natural linewidth, Doppler broadening, Lorentzian line shape, sudden approximation, adiabatic theorem, Berry phase, Landau-Zener formula, cross section, differential cross section, Born approximation, Yukawa potential, Rutherford scattering, partial waves, phase shifts, optical theorem, scattering length, resonance, Breit-Wigner formula]
---

# Time-Dependent Perturbation Theory, Transitions and Scattering

Most of introductory quantum mechanics is about stationary states: the energy levels of a box, an oscillator or a hydrogen atom, each evolving only by an overall phase. Yet almost everything we actually *observe* is a change. An atom absorbs a photon and jumps to an excited level; an excited nucleus emits a gamma ray; a neutron strikes a uranium nucleus and is captured; an alpha particle bounces off a gold nucleus. Spectroscopy, lasers, MRI scanners, nuclear reactors and particle colliders all measure the *rates* at which quantum systems make transitions or scatter. A stationary state, by definition, never changes, so to explain these processes we need tools for systems whose Hamiltonian depends on time or whose initial state is not an eigenstate of the full Hamiltonian.

This chapter develops those tools. We start from the exact equations of motion in the interaction picture and derive first-order time-dependent perturbation theory. From it come transition probabilities, resonance, Rabi oscillations and **Fermi's golden rule**, the workhorse formula for transition rates. Applied to atoms in light, the golden rule yields the electric-dipole **selection rules**, the Einstein coefficients, spontaneous emission rates, radiative lifetimes and natural line widths. We then treat the two opposite limits of time dependence, the **sudden** and **adiabatic** approximations, including the Landau–Zener formula for avoided crossings. The second half turns to **scattering**: cross sections, the **Born approximation**, the **Rutherford formula**, partial waves and phase shifts, and **resonances**. Along the way we meet the history of these ideas, their applications, common misconceptions, practice problems and a summary of key equations.

The chapter assumes familiarity with the Schrödinger equation, Dirac notation, the harmonic oscillator and the hydrogen atom (earlier chapters of this series).

## 1. Time Evolution and the Interaction Picture

### 1.1 Why stationary states never make transitions

If $\hat H$ does not depend on time, an eigenstate $\lvert n\rangle$ with energy $E_n$ evolves as $\lvert n\rangle e^{-iE_nt/\hbar}$. All probabilities are constant, so nothing happens. A general state $\sum_n c_n e^{-iE_nt/\hbar}\lvert n\rangle$ has time-dependent expectation values, but the probabilities $\lvert c_n\rvert^2$ of finding each energy never change. A transition from one level to another therefore requires something extra: either a time-dependent term in the Hamiltonian (a light wave, a radio-frequency pulse, a passing charged particle) or a coupling to a continuum that the simple Hamiltonian ignored (the quantized electromagnetic field, which causes spontaneous emission).

We therefore split the Hamiltonian into a part we can solve exactly and a perturbation:
$$\hat H(t) = \hat H_0 + \hat V(t), \qquad \hat H_0\lvert n\rangle = E_n\lvert n\rangle$$
The eigenstates of $\hat H_0$ are the "levels" between which transitions occur.

### 1.2 Three pictures of time evolution

Quantum mechanics can place the time dependence in the states, in the operators, or split it between them. All three choices give identical predictions.

| Picture | States | Operators | Equation of motion |
|---|---|---|---|
| Schrödinger | evolve with the full $\hat H$ | fixed | $i\hbar\,\partial_t\lvert\psi_S\rangle = \hat H\lvert\psi_S\rangle$ |
| Heisenberg | fixed | evolve with the full $\hat H$ | $d\hat A_H/dt = (i/\hbar)[\hat H, \hat A_H]$ |
| Interaction (Dirac) | evolve with $\hat V_I(t)$ only | evolve with $\hat H_0$ | $i\hbar\,\partial_t\lvert\psi_I\rangle = \hat V_I(t)\lvert\psi_I\rangle$ |

The **interaction picture** removes the trivial, already-known evolution due to $\hat H_0$:
$$\lvert\psi_I(t)\rangle = e^{i\hat H_0t/\hbar}\lvert\psi_S(t)\rangle, \qquad \hat V_I(t) = e^{i\hat H_0t/\hbar}\,\hat V(t)\,e^{-i\hat H_0t/\hbar}$$
Differentiating the first definition and using the Schrödinger equation $i\hbar\,\partial_t\lvert\psi_S\rangle = (\hat H_0 + \hat V)\lvert\psi_S\rangle$ gives
$$i\hbar\,\partial_t\lvert\psi_I\rangle = -\hat H_0e^{i\hat H_0t/\hbar}\lvert\psi_S\rangle + e^{i\hat H_0t/\hbar}(\hat H_0 + \hat V)\lvert\psi_S\rangle = \hat V_I(t)\lvert\psi_I(t)\rangle$$
If $\hat V = 0$, the interaction-picture state is frozen. All change in $\lvert\psi_I\rangle$ is caused by the perturbation, which is exactly what we want to track.

### 1.3 Exact equations for the amplitudes

Expand the Schrödinger-picture state as
$$\lvert\psi_S(t)\rangle = \sum_n c_n(t)\,e^{-iE_nt/\hbar}\lvert n\rangle$$
so that $c_n(t) = \langle n\vert\psi_I(t)\rangle$. Without a perturbation the $c_n$ are constants. Taking the matrix element of the interaction-picture equation with $\langle f\rvert$ gives the exact coupled equations
$$i\hbar\,\frac{dc_f}{dt} = \sum_n V_{fn}(t)\,e^{i\omega_{fn}t}\,c_n(t), \qquad V_{fn}(t) = \langle f\vert\hat V(t)\vert n\rangle, \qquad \omega_{fn} = \frac{E_f - E_n}{\hbar}$$
Nothing has been approximated yet. For two levels these equations can sometimes be solved exactly (Section 3.2); in general we solve them by iteration.

### 1.4 The Dyson series

Integrating the interaction-picture equation from $t_0$ to $t$ and substituting the result back into itself repeatedly produces the **Dyson series** for the interaction-picture evolution operator:
$$\hat U_I(t,t_0) = 1 - \frac{i}{\hbar}\int_{t_0}^{t}dt_1\,\hat V_I(t_1) + \left(-\frac{i}{\hbar}\right)^2\int_{t_0}^{t}dt_1\int_{t_0}^{t_1}dt_2\,\hat V_I(t_1)\hat V_I(t_2) + \cdots$$
The terms have a vivid reading: the system interacts zero times, once, twice, and so on, propagating freely under $\hat H_0$ between interactions. The first-order term describes ordinary absorption and emission; the second-order term, which passes through intermediate states, describes two-photon absorption, Raman scattering and the decay of the metastable hydrogen 2s state. In quantum field theory, Feynman diagrams are pictures of the terms of exactly this series.

## 2. First-Order Perturbation Theory and Transition Probabilities

### 2.1 The first-order amplitude

Suppose the system starts in level $\lvert i\rangle$ at $t = 0$, so $c_n(0) = \delta_{ni}$. If the perturbation is weak, the amplitudes barely change, and on the right-hand side of the exact equation we may replace $c_n(t)$ by its initial value. For a final state $f \neq i$:
$$c_f^{(1)}(t) = -\frac{i}{\hbar}\int_0^t V_{fi}(t')\,e^{i\omega_{fi}t'}\,dt'$$
The **transition probability** is $P_{i\to f}(t) = \lvert c_f^{(1)}(t)\rvert^2$. The approximation is valid as long as $P_{i\to f} \ll 1$, so that the initial state is not noticeably depleted. Two general features are already visible. First, only the matrix element $V_{fi}$ connecting the two states matters, so if it vanishes the transition is "forbidden" at this order. Second, because $\hat V$ is Hermitian, $\lvert V_{if}\rvert = \lvert V_{fi}\rvert$ and the first-order probabilities satisfy $P_{i\to f} = P_{f\to i}$ for the same perturbation.

### 2.2 A constant perturbation switched on at t = 0

Let $\hat V$ be constant for $t > 0$. The integral is elementary:
$$c_f^{(1)}(t) = -\frac{i}{\hbar}V_{fi}\,\frac{e^{i\omega_{fi}t} - 1}{i\omega_{fi}}, \qquad \left\lvert e^{i\omega_{fi}t} - 1\right\rvert^2 = 4\sin^2\!\left(\frac{\omega_{fi}t}{2}\right)$$
so that
$$P_{i\to f}(t) = \frac{4\lvert V_{fi}\rvert^2}{\hbar^2\omega_{fi}^2}\sin^2\!\left(\frac{\omega_{fi}t}{2}\right)$$
The probability oscillates and never exceeds $4\lvert V_{fi}\rvert^2/(E_f - E_i)^2$, which is small when the coupling is weak compared with the level spacing. This is consistent with time-independent perturbation theory, where the perturbed state contains an admixture $V_{fi}/(E_i - E_f)$ of $\lvert f\rangle$; the oscillation is a ringing caused by the abrupt switch-on. For degenerate levels ($\omega_{fi} \to 0$) the formula becomes $P = \lvert V_{fi}\rvert^2t^2/\hbar^2$, growing quadratically.

### 2.3 Pulses and the Fourier-component rule

If the perturbation has the form $\hat V(t) = \hat W g(t)$ with $g(t) \to 0$ as $t \to \pm\infty$, the amplitude after the pulse is
$$c_f^{(1)}(\infty) = -\frac{i}{\hbar}W_{fi}\int_{-\infty}^{\infty}g(t)\,e^{i\omega_{fi}t}\,dt$$
The system responds only to the **Fourier component of the pulse at the transition frequency**. A pulse lasting a time $\tau$ contains frequencies up to roughly $1/\tau$. If $\omega_{fi}\tau \gg 1$ the Fourier component is tiny and the system is almost never excited: the change is *adiabatic*. If $\omega_{fi}\tau \ll 1$ the pulse acts as an instantaneous kick: the change is *sudden*. Section 8 develops both limits.

### Worked Example 2.1 – Kicking a trapped ion with a field pulse

**Problem:** A ⁴⁰Ca⁺ ion (mass $m = 6.64\times10^{-26}$ kg, charge $e$) sits in the ground state of an ion trap that acts as a harmonic oscillator of angular frequency $\omega = 2\pi\times1.00$ MHz along $x$. A uniform electric field pulse $\mathcal E(t) = \mathcal E_0e^{-t^2/\tau^2}$ with $\mathcal E_0 = 0.050$ V/m is applied along $x$. Find the probability that the ion ends in the first excited state for $\tau = 100$ ns and for $\tau = 1.00$ μs.

1. The perturbation is $\hat V(t) = -e\mathcal E(t)\hat x$. For the oscillator, $\langle1\vert\hat x\vert0\rangle = \sqrt{\hbar/(2m\omega)}$, and $\hat x$ connects $n = 0$ only to $n = 1$, so at first order only this transition occurs.
2. The Gaussian integral is $\int_{-\infty}^{\infty}e^{-t^2/\tau^2}e^{i\omega t}dt = \sqrt\pi\,\tau\,e^{-\omega^2\tau^2/4}$.
3. Hence
$$P_{0\to1} = \frac{e^2\mathcal E_0^2}{\hbar^2}\cdot\frac{\hbar}{2m\omega}\cdot\pi\tau^2e^{-\omega^2\tau^2/2} = \frac{\pi e^2\mathcal E_0^2\tau^2}{2m\hbar\omega}\,e^{-\omega^2\tau^2/2}$$
4. For $\tau = 100$ ns: $\omega\tau = 0.628$, the prefactor is $0.0229$ and the exponential is $0.821$, so $P = 0.0188$.
5. For $\tau = 1.00$ μs: $\omega\tau = 6.28$, the prefactor is $2.29$ but the exponential is $e^{-19.7} = 2.7\times10^{-9}$, so $P = 6.1\times10^{-9}$.

**Answer:** about 1.9% for the 100 ns pulse and about $6\times10^{-9}$ for the 1 μs pulse. The longer pulse delivers ten times the impulse, yet it barely excites the ion, because it changes slowly compared with the oscillation period and the ion follows the displaced trap minimum adiabatically. (For a driven oscillator the exact answer is a coherent state, and the first-order result equals the classical energy transferred divided by $\hbar\omega$.)

## 3. Harmonic Perturbations, Resonance and Rabi Oscillations

### 3.1 Absorption and stimulated emission

A monochromatic field produces a perturbation of the form $\hat V(t) = \hat F e^{-i\omega t} + \hat F^\dagger e^{i\omega t}$. The first-order amplitude is
$$c_f^{(1)}(t) = -\frac{1}{\hbar}\left[F_{fi}\,\frac{e^{i(\omega_{fi} - \omega)t} - 1}{\omega_{fi} - \omega} + F^\dagger_{fi}\,\frac{e^{i(\omega_{fi} + \omega)t} - 1}{\omega_{fi} + \omega}\right]$$
The first term becomes large when $\omega \approx \omega_{fi}$, that is $E_f = E_i + \hbar\omega$: **absorption**. The second becomes large when $\omega \approx -\omega_{fi}$, that is $E_f = E_i - \hbar\omega$: **stimulated emission**, in which the field drives the system down and the field gains a quantum. Near the absorption resonance, define the detuning $\Delta = \omega - \omega_{fi}$ and keep only the resonant term:
$$P_{i\to f}(t) \approx \frac{4\lvert F_{fi}\rvert^2}{\hbar^2}\,\frac{\sin^2(\Delta t/2)}{\Delta^2}$$
This function of $\Delta$ has a central peak of height $\lvert F_{fi}\rvert^2t^2/\hbar^2$ and first zeros at $\Delta = \pm2\pi/t$. As time goes on the peak grows taller and narrower, so the transition becomes increasingly selective in frequency, with a resolution of order $1/t$. This is the energy–time relation at work: to tell whether a drive is exactly on resonance, one has to wait. Because absorption and stimulated emission involve the same squared matrix element, a field drives both processes equally strongly per atom, which is why a laser medium amplifies light only when more atoms are in the upper level than in the lower (a **population inversion**).

### 3.2 The exact two-level solution: Rabi oscillations

For a two-level system driven near resonance, keeping only the resonant term (the **rotating-wave approximation**) leaves two coupled equations that can be solved exactly. Writing the coupling as $F_{fi} = \hbar\Omega/2$, where $\Omega$ is the **Rabi frequency**, the result is the **Rabi formula**:
$$P_{i\to f}(t) = \frac{\Omega^2}{\Omega^2 + \Delta^2}\,\sin^2\!\left(\frac{\sqrt{\Omega^2 + \Delta^2}\;t}{2}\right)$$
When $\Omega t \ll 1$ or $\Omega \ll \lvert\Delta\rvert$, this reduces to the first-order result above. On resonance, $P = \sin^2(\Omega t/2)$: the population oscillates completely between the two levels. A pulse with $\Omega t = \pi$ (a **π pulse**) inverts the population; a **π/2 pulse** creates an equal superposition. Rabi oscillations are how qubits are manipulated in trapped-ion, neutral-atom and superconducting quantum computers, and how nuclear spins are tipped in NMR and MRI. They also show the limits of a constant transition rate: a single discrete final state driven coherently oscillates rather than filling up linearly.

### Worked Example 3.1 – Spin flips in an MRI scanner

**Problem:** In a 1.5 T MRI scanner, protons (gyromagnetic ratio $\gamma = 2.675\times10^8$ s⁻¹ T⁻¹) are driven by a radio-frequency field whose rotating component has amplitude $B_1 = 10.0$ μT. (a) What radio frequency is resonant? (b) How long are the π/2 and π pulses? (c) With a field gradient of 10 mT/m along $z$, how far from the resonant slice is the detuning equal to $\Omega$, so that the maximum flip probability falls to one half?

1. Resonance (Larmor) frequency: $f_0 = \gamma B_0/2\pi = (42.58\ \text{MHz/T})(1.5\ \text{T}) = 63.9$ MHz.
2. For a spin-1/2 in a rotating field, the Rabi frequency is $\Omega = \gamma B_1 = (2.675\times10^8)(1.00\times10^{-5}) = 2675$ s⁻¹, i.e. $\Omega/2\pi = 426$ Hz.
3. π/2 pulse: $t = \pi/(2\Omega) = 0.587$ ms. π pulse: $t = \pi/\Omega = 1.17$ ms.
4. With $\Delta = \Omega$ the Rabi formula gives a maximum probability $\Omega^2/(\Omega^2 + \Delta^2) = 1/2$. The gradient shifts the local resonance by $(\gamma/2\pi)Gz$, so $z = 426\ \text{Hz}/(42.58\times10^6\ \text{Hz/T}\times0.010\ \text{T/m}) = 1.0\times10^{-3}$ m.
5. Check against first-order theory: after 0.100 ms on resonance, $\Omega t/2 = 0.134$; first order gives $(\Omega t/2)^2 = 0.0179$ and the exact $\sin^2(\Omega t/2) = 0.0178$.

**Answer:** 63.9 MHz; about 0.59 ms and 1.17 ms; about 1 mm. The frequency selectivity of resonant transitions is what lets MRI excite one thin slice of the body at a time.

## 4. Fermi's Golden Rule

### 4.1 From a discrete level to a continuum

In many processes the final state is not a single level but belongs to a continuum: an ionized electron can leave with any energy, an emitted photon can go in any direction, a scattered particle can emerge at any angle. Let $\rho(E_f)$ be the **density of final states**, the number of states per unit energy. Summing the constant-perturbation result of Section 2.2 over final states,
$$P(t) = \int\frac{4\lvert V_{fi}\rvert^2}{\hbar^2\omega_{fi}^2}\sin^2\!\left(\frac{\omega_{fi}t}{2}\right)\rho(E_f)\,dE_f$$
For large $t$ the function $\sin^2(xt/2)/x^2$ is a narrow spike at $x = 0$ of height $t^2/4$ and width of order $1/t$, with total area
$$\int_{-\infty}^{\infty}\frac{\sin^2(xt/2)}{x^2}\,dx = \frac{\pi t}{2}$$
It therefore acts like $(\pi t/2)\,\delta(x)$. With $dE_f = \hbar\,d\omega_{fi}$ and $\lvert V_{fi}\rvert^2\rho$ varying slowly across the spike,
$$P(t) = \frac{4\lvert V_{fi}\rvert^2\rho}{\hbar^2}\cdot\hbar\cdot\frac{\pi t}{2} = \frac{2\pi}{\hbar}\lvert V_{fi}\rvert^2\rho\,t$$
The probability grows *linearly* in time, so there is a constant **transition rate**:
$$\Gamma_{i\to f} = \frac{2\pi}{\hbar}\,\lvert V_{fi}\rvert^2\,\rho(E_f), \qquad E_f = E_i$$
This is **Fermi's golden rule**. For a harmonic perturbation the same steps give the rate with $F_{fi}$ in place of $V_{fi}$ and $E_f = E_i \pm \hbar\omega$. An equivalent form, convenient for summing over many final states, is $\Gamma = (2\pi/\hbar)\sum_f\lvert V_{fi}\rvert^2\delta(E_f - E_i)$. Energy conservation is not put in by hand; it emerges because, after a long time, only final states within about $2\pi\hbar/t$ of the initial energy can be reached.

### 4.2 Conditions of validity

The golden rule holds in a window of times. The time must be long enough that the spike (width about $2\pi\hbar/t$ in energy) is narrower than the energy scale over which $\lvert V_{fi}\rvert^2\rho$ changes, yet the derivation also assumes the initial state is not depleted. The Weisskopf–Wigner analysis (1930) shows that the rate remains valid well beyond this: the initial-state population decays exponentially, $e^{-\Gamma t}$, over many lifetimes. At extremely short times the probability grows as $t^2$ rather than $t$, which underlies the **quantum Zeno effect** (Misra and Sudarshan, 1977): sufficiently frequent measurements slow a decay. The rule does *not* apply to a single discrete final state driven coherently; that case gives Rabi oscillations.

### 4.3 Counting final states

For a free particle in a large box of side $L$ with periodic boundary conditions, the allowed wave vectors are $\mathbf k = (2\pi/L)(n_x, n_y, n_z)$, one state per volume $(2\pi/L)^3$ of $\mathbf k$-space. The number of states with $\lvert\mathbf k\rvert$ between $k$ and $k + dk$ and direction within the solid angle $d\Omega$ is $(L/2\pi)^3k^2\,dk\,d\Omega$. For a nonrelativistic particle with $E = \hbar^2k^2/2m$, $dk/dE = m/(\hbar^2k)$, so
$$\rho(E)\,d\Omega = \frac{L^3}{(2\pi)^3}\,\frac{mk}{\hbar^2}\,d\Omega$$
For photons, $E = \hbar ck$; including two polarizations and all directions gives $\rho(E) = L^3\omega^2/(\pi^2\hbar c^3)$. This is the same mode counting that enters Planck's radiation law. The box size $L$ always cancels from physical results, as we will see in the Born approximation.

## 5. Atoms and Light: The Electric-Dipole Approximation and Selection Rules

### 5.1 The interaction Hamiltonian

Visible light has a wavelength near 500 nm, while an atom is about 0.1 nm across. Over the atom the field is essentially uniform: with $k = 2\pi/\lambda$ and $a_0 = 0.0529$ nm, $ka_0 \approx 7\times10^{-4}$. The magnetic force on a bound electron is smaller than the electric force by a factor of order $v/c \approx \alpha \approx 1/137$. Keeping only the uniform electric field gives the **electric-dipole (E1) approximation**:
$$\hat V(t) = -\hat{\mathbf d}\cdot\boldsymbol{\mathcal E}(t), \qquad \hat{\mathbf d} = -e\hat{\mathbf r}$$
For a linearly polarized wave $\boldsymbol{\mathcal E} = \mathcal E_0\,\boldsymbol\epsilon\cos\omega t$, we have $\hat V = (e\mathcal E_0/2)(\boldsymbol\epsilon\cdot\hat{\mathbf r})(e^{-i\omega t} + e^{i\omega t})$, a harmonic perturbation with $\hat F = (e\mathcal E_0/2)\,\boldsymbol\epsilon\cdot\hat{\mathbf r}$.

### 5.2 Absorption rate in broadband light

Thermal light, or any light much broader than the atomic line, is an incoherent mixture of frequencies. Let $u(\omega)$ be the energy density per unit angular frequency. A single plane wave has average energy density $\varepsilon_0\mathcal E_0^2/2$, so the frequency slice $d\omega$ contributes $\mathcal E_0^2 \to (2/\varepsilon_0)\,u(\omega)\,d\omega$. Adding probabilities (not amplitudes) over frequencies and using the area of the resonance function from Section 4.1,
$$P = \frac{e^2\lvert\langle f\vert\boldsymbol\epsilon\cdot\hat{\mathbf r}\vert i\rangle\rvert^2}{\hbar^2}\cdot\frac{2u(\omega_{fi})}{\varepsilon_0}\cdot\frac{\pi t}{2}$$
For unpolarized light arriving from all directions, the average of $\lvert\boldsymbol\epsilon\cdot\mathbf r_{fi}\rvert^2$ is $\lvert\mathbf r_{fi}\rvert^2/3$, and the absorption rate is
$$W_{i\to f} = \frac{\pi e^2\lvert\langle f\vert\hat{\mathbf r}\vert i\rangle\rvert^2}{3\varepsilon_0\hbar^2}\,u(\omega_{fi}) \equiv B\,u(\omega_{fi})$$
This defines the **Einstein B coefficient** (here per unit angular frequency). Everything about the atom enters through the **dipole matrix element** $\mathbf d_{fi} = -e\langle f\vert\hat{\mathbf r}\vert i\rangle$.

### 5.3 Deriving the selection rules

The selection rules state when $\langle f\vert\hat{\mathbf r}\vert i\rangle$ vanishes by symmetry. Consider one-electron states $\lvert n\ell m\rangle$.

**Parity.** Under inversion $\mathbf r \to -\mathbf r$, the operator $\hat{\mathbf r}$ changes sign, while $\lvert n\ell m\rangle$ has parity $(-1)^\ell$. The integrand $\psi_f^*\,\mathbf r\,\psi_i$ therefore has parity $(-1)^{\ell_f + \ell_i + 1}$, and its integral over all space vanishes unless this is $+1$. **The parity must change.**

**Magnetic quantum number.** The commutators $[\hat L_z, \hat z] = 0$ and $[\hat L_z, \hat x \pm i\hat y] = \pm\hbar(\hat x \pm i\hat y)$ follow from $[\hat L_z, \hat x] = i\hbar\hat y$ and $[\hat L_z, \hat y] = -i\hbar\hat x$. Taking matrix elements between $\langle n'\ell'm'\rvert$ and $\lvert n\ell m\rangle$, and letting $\hat L_z$ act to the left and right:
$$(m' - m)\,\hbar\,\langle f\vert\hat z\vert i\rangle = 0, \qquad (m' - m \mp 1)\,\hbar\,\langle f\vert\hat x \pm i\hat y\vert i\rangle = 0$$
Light polarized along the quantization axis ("π light") drives only $\Delta m = 0$; circularly polarized ("σ±") light drives $\Delta m = \pm1$.

**Orbital angular momentum.** The components of $\mathbf r$ are proportional to $r\,Y_1^q(\theta, \phi)$ with $q = 0, \pm1$. The angular integral $\int Y_{\ell'}^{m'*}\,Y_1^q\,Y_\ell^m\,d\Omega$ vanishes unless $\ell'$ is one of the values obtained by adding angular momenta $\ell$ and 1, namely $\ell - 1$, $\ell$ or $\ell + 1$, and unless $m' = m + q$. Parity excludes $\ell' = \ell$. Hence $\Delta\ell = \pm1$: the photon carries away (or brings in) one unit of angular momentum.

**Spin.** The operator $\hat{\mathbf r}$ does not act on spin, so $\Delta S = 0$ and $\Delta m_s = 0$.

| Quantity | Electric-dipole rule | Origin |
|---|---|---|
| Parity | must change | $\hat{\mathbf r}$ is odd under inversion |
| Orbital $\ell$ (one electron) | $\Delta\ell = \pm1$ | photon carries one unit of angular momentum, plus parity |
| Magnetic $m$ | $\Delta m = 0$ (π light), $\pm1$ (σ light) | commutators with $\hat L_z$ |
| Total spin $S$ | $\Delta S = 0$ | dipole operator ignores spin |
| Total $J$ | $\Delta J = 0, \pm1$, but not $J = 0 \to J = 0$ | $\hat{\mathbf r}$ is a vector operator |
| Principal $n$ | any change allowed | radial integrals are generally nonzero |

### 5.4 Forbidden transitions still happen

"Forbidden" means forbidden at the electric-dipole level only. Higher terms in the expansion $e^{i\mathbf k\cdot\mathbf r} = 1 + i\mathbf k\cdot\mathbf r + \cdots$ give magnetic-dipole (M1) and electric-quadrupole (E2) transitions, typically slower than allowed E1 transitions at optical wavelengths by five or more orders of magnitude. Second-order processes allow two-photon decay. Examples include the hydrogen 2s level, which cannot reach 1s by one E1 photon ($\Delta\ell = 0$) and instead emits two photons with a lifetime of about 0.12 s; the 21 cm hyperfine line of hydrogen (M1), with a lifetime of about $1.1\times10^7$ years; and the green auroral line of atomic oxygen at 557.7 nm, an E2 transition from a level living roughly a second, which can only be seen because collisions in the thin upper atmosphere are rare. Spin-forbidden ("intercombination") lines become weakly allowed when spin–orbit coupling mixes singlet and triplet states, as in the strong 253.7 nm line of mercury and in the phosphorescence of glow-in-the-dark materials.

## 6. Spontaneous Emission and Radiative Lifetimes

### 6.1 Einstein's argument

An excited atom in empty space decays even with no light present. Einstein (1916–1917) showed, without any quantum electrodynamics and using only thermal equilibrium, that the rate of this **spontaneous emission** is fixed by the rate of absorption. Consider many atoms with a lower level 1 and an upper level 2 (take them nondegenerate for simplicity), separated by $\hbar\omega$, in blackbody radiation of spectral density $u(\omega)$. Three processes occur, with rates per atom $B_{12}u$ (absorption), $B_{21}u$ (stimulated emission) and $A$ (spontaneous emission). In equilibrium the upward and downward rates balance:
$$N_1B_{12}u = N_2\left(A + B_{21}u\right), \qquad \frac{N_2}{N_1} = e^{-\hbar\omega/k_BT}$$
Solving for the radiation density,
$$u(\omega) = \frac{A}{B_{12}e^{\hbar\omega/k_BT} - B_{21}}$$
This must equal Planck's law, $u(\omega) = (\hbar\omega^3/\pi^2c^3)/(e^{\hbar\omega/k_BT} - 1)$, at every temperature. That forces
$$B_{12} = B_{21} = B, \qquad A = \frac{\hbar\omega^3}{\pi^2c^3}\,B$$
With degenerate levels the first relation becomes $g_1B_{12} = g_2B_{21}$. Stimulated emission, the principle of the laser, was discovered in this argument: without it, Wien's law rather than Planck's would result.

### 6.2 The spontaneous emission rate

Combining Einstein's relation with the $B$ coefficient of Section 5.2:
$$A = \frac{\omega^3e^2\lvert\langle f\vert\hat{\mathbf r}\vert i\rangle\rvert^2}{3\pi\varepsilon_0\hbar c^3} = \frac{4\alpha\,\omega^3}{3c^2}\,\lvert\langle f\vert\hat{\mathbf r}\vert i\rangle\rvert^2$$
where $\alpha = e^2/(4\pi\varepsilon_0\hbar c) \approx 1/137.036$ is the fine-structure constant. Dirac (1927) obtained the same result directly by quantizing the electromagnetic field and applying the golden rule with the photon density of states; in that picture spontaneous emission is emission stimulated by the zero-point fluctuations of the field. The factor $\omega^3$ is decisive: for a fixed dipole moment, a transition at 500 nm decays $10^{18}$ times faster than one at 50 cm, since the wavelengths differ by a factor of $10^6$. The ratio of spontaneous to stimulated emission in thermal radiation is $A/(Bu) = e^{\hbar\omega/k_BT} - 1$, so spontaneous emission dominates for visible light at room temperature, while stimulated processes dominate for microwaves.

### 6.3 Lifetimes and branching ratios

If an excited level can decay to several lower levels with rates $A_k$, its population falls as $N(t) = N(0)e^{-t/\tau}$ with **radiative lifetime**
$$\tau = \frac{1}{\sum_kA_k}$$
and the fraction of decays through channel $k$ (the **branching ratio**) is $A_k/\sum_jA_j$. Non-radiative channels such as collisions add to the total rate and shorten the lifetime.

### Worked Example 6.1 – Lifetime of the hydrogen 2p state

**Problem:** Calculate the spontaneous emission rate and lifetime of the hydrogen 2p level, which decays to 1s by emitting the Lyman-α photon ($\lambda = 121.57$ nm).

1. Angular frequency: $\omega = 2\pi c/\lambda = 1.549\times10^{16}$ s⁻¹ (photon energy 10.20 eV).
2. Matrix element: for the $m = 0$ substate only $\hat z$ contributes, and the hydrogen wavefunctions give $\langle100\vert\hat z\vert210\rangle = (128\sqrt2/243)\,a_0 = 0.7449\,a_0 = 3.942\times10^{-11}$ m, so $\lvert\mathbf r_{fi}\rvert^2 = 1.554\times10^{-21}$ m². (The $m = \pm1$ substates give the same total, as rotational symmetry requires.)
3. Rate:
$$A = \frac{4\alpha\omega^3}{3c^2}\lvert\mathbf r_{fi}\rvert^2 = \frac{4(7.297\times10^{-3})(1.549\times10^{16})^3}{3(2.998\times10^8)^2}(1.554\times10^{-21}) = 6.26\times10^8\ \text{s}^{-1}$$
4. Lifetime: $\tau = 1/A = 1.60$ ns. The 2p level has no other significant decay channel. The only other lower-lying candidate, 2s, lies either above the level (2p₁/₂ sits about 1 GHz below 2s because of the Lamb shift) or only about 10 GHz below it (2p₃/₂), and for such a microwave transition the $\omega^3$ factor makes the rate utterly negligible.

**Answer:** $A \approx 6.26\times10^8$ s⁻¹ and $\tau \approx 1.60$ ns, in agreement with the accepted value of 1.596 ns.

| Transition | Wavelength | Type | Lifetime of upper level | Natural width $\Gamma/2\pi$ |
|---|---|---|---|---|
| H 2p → 1s (Lyman-α) | 121.6 nm | E1 | 1.60 ns | 99.7 MHz |
| Na 3p ²P₃/₂ → 3s (D2) | 589.0 nm | E1 | 16.2 ns | 9.8 MHz |
| Rb 5p ²P₃/₂ → 5s (D2) | 780.2 nm | E1 | 26.2 ns | 6.07 MHz |
| Cs 6p ²P₃/₂ → 6s (D2) | 852.3 nm | E1 | 30.5 ns | 5.22 MHz |
| H 2s → 1s | continuous (two photons) | 2E1 | 0.122 s | 1.3 Hz |
| H 1s hyperfine (21 cm line) | 21.1 cm | M1 | about $1.1\times10^7$ yr | negligible |

## 7. Line Widths and Line Shapes

### 7.1 Natural broadening

Because an excited level decays, it is not a perfectly sharp energy eigenstate. Weisskopf and Wigner (1930) showed that the upper-level amplitude decays as $c_2(t) = e^{-\Gamma t/2}$, with $\Gamma = 1/\tau$, so the emitted field oscillates as $e^{-i\omega_0t - \Gamma t/2}$ for $t \geq 0$. Its Fourier transform is
$$\tilde{\mathcal E}(\omega) \propto \int_0^{\infty}e^{i(\omega - \omega_0)t}e^{-\Gamma t/2}\,dt = \frac{1}{\Gamma/2 - i(\omega - \omega_0)}$$
and the spectral intensity is the normalized **Lorentzian**
$$I(\omega) = \frac{\Gamma/2\pi}{(\omega - \omega_0)^2 + \Gamma^2/4}$$
Its full width at half maximum is $\Gamma$ in angular frequency, so the **natural linewidth** is
$$\Delta\nu_{\text{nat}} = \frac{\Gamma}{2\pi} = \frac{1}{2\pi\tau}, \qquad \Delta E = \hbar\Gamma = \frac{\hbar}{\tau}$$
If the lower level also decays, its rate adds: $\Gamma = \Gamma_{\text{upper}} + \Gamma_{\text{lower}}$.

### 7.2 Other broadening mechanisms

| Mechanism | Physical cause | Line shape | Remarks |
|---|---|---|---|
| Natural | finite radiative lifetime | Lorentzian | fundamental lower limit; MHz range for strong optical lines |
| Doppler | thermal motion of emitters | Gaussian | usually dominant in low-pressure gases; about a GHz for light atoms at a few hundred kelvin |
| Collisional (pressure) | collisions interrupt or shift the phase of emission | Lorentzian | grows in proportion to pressure; important in dense gases and stellar atmospheres |
| Power (saturation) | strong driving shortens the effective lifetime | Lorentzian | grows with intensity |
| Transit time | atoms cross the beam in a finite time | depends on beam profile | important for fast atomic beams |

The Doppler width follows from the Maxwell distribution of the velocity component along the line of sight, which is Gaussian with standard deviation $\sqrt{k_BT/m}$. The shift $\nu - \nu_0 = \nu_0v_x/c$ maps it onto a Gaussian line of full width at half maximum
$$\Delta\nu_D = \frac{\nu_0}{c}\sqrt{\frac{8k_BT\ln2}{m}}$$
When Lorentzian and Gaussian broadening are both present, the observed shape is their convolution, the **Voigt profile**.

### Worked Example 7.1 – Natural versus Doppler width of the sodium D2 line

**Problem:** The sodium 3p ²P₃/₂ level has a lifetime of 16.2 ns and emits at 589.0 nm. Find the natural linewidth, the corresponding energy width and quality factor, and compare with the Doppler width in sodium vapour at 500 K (atomic mass 22.99 u).

1. Natural width: $\Delta\nu_{\text{nat}} = 1/(2\pi\times16.2\times10^{-9}\ \text{s}) = 9.82$ MHz.
2. Energy width: $\Delta E = h\,\Delta\nu = 4.06\times10^{-8}$ eV, compared with a photon energy of 2.105 eV.
3. Line frequency: $\nu_0 = c/\lambda = 5.090\times10^{14}$ Hz, so $Q = \nu_0/\Delta\nu_{\text{nat}} = 5.2\times10^7$.
4. Doppler width: $m = 22.99\times1.6605\times10^{-27} = 3.818\times10^{-26}$ kg; $\sqrt{8k_BT\ln2/m} = \sqrt{8(1.381\times10^{-23})(500)(0.693)/(3.818\times10^{-26})} = 1001$ m/s; $\Delta\nu_D = (5.090\times10^{14})(1001)/(2.998\times10^8) = 1.70$ GHz.
5. Ratio: $1.70\ \text{GHz}/9.82\ \text{MHz} \approx 173$.

**Answer:** the natural width is 9.8 MHz ($Q \approx 5\times10^7$), but thermal motion broadens the line about 170 times more, to 1.7 GHz. Seeing the natural width requires Doppler-free methods such as saturated-absorption spectroscopy, cold atoms or collimated atomic beams.

## 8. The Sudden and Adiabatic Approximations

When a Hamiltonian changes from $\hat H_a$ to $\hat H_b$, the outcome depends on how the duration $T$ of the change compares with the internal time scales $\hbar/\Delta E$ set by the level spacings $\Delta E$.

| | Sudden limit | Adiabatic limit |
|---|---|---|
| Condition | $T \ll \hbar/\Delta E$ | $T \gg \hbar/\Delta E$ (more precisely, the condition in Section 8.2) |
| What happens to the state | unchanged during the change | follows the instantaneous eigenstate |
| Final occupation probabilities | $\lvert\langle n_b\vert\psi_a\rangle\rvert^2$, spread over many levels | stays in the corresponding level $n$ |
| Energy | expectation value unchanged at the moment of change | follows $E_n(t)$; work is done on the system |

### 8.1 The sudden approximation

If the Hamiltonian changes in a time much shorter than $\hbar/\Delta E$, the evolution operator over that interval is essentially the identity, so the wavefunction has no time to respond: $\lvert\psi(0^+)\rangle = \lvert\psi(0^-)\rangle$. Afterwards the old state is expanded in the eigenstates of the new Hamiltonian, and the probability of finding level $n$ is $P_n = \lvert\langle n_b\vert\psi(0^-)\rangle\rvert^2$.

### Worked Example 8.1 – The atomic electron after tritium beta decay

**Problem:** A tritium atom (³H, electron in the 1s state) beta-decays to a ³He⁺ ion: the nuclear charge jumps from $Z = 1$ to $Z = 2$ while the electron is still in the old 1s orbital. Find the probability that the ion ends in its ground state, and check that the sudden approximation applies.

1. Time scales: the beta electron carries an average of about 5.7 keV ($v = 0.148c$) and crosses a distance $a_0$ in $a_0/v = 1.2\times10^{-18}$ s. The atomic time scale is $\hbar/(13.6\ \text{eV}) = 4.8\times10^{-17}$ s, about 40 times longer, so the change is sudden.
2. Hydrogen-like ground state: $\psi_{1s}^{(Z)} = (Z^3/\pi a_0^3)^{1/2}e^{-Zr/a_0}$.
3. Overlap for charges $Z$ and $Z'$:
$$\langle\psi^{(Z')}_{1s}\vert\psi^{(Z)}_{1s}\rangle = \frac{(ZZ')^{3/2}}{\pi a_0^3}\int_0^{\infty}e^{-(Z + Z')r/a_0}\,4\pi r^2\,dr = \frac{8(ZZ')^{3/2}}{(Z + Z')^3}$$
4. With $Z = 1$, $Z' = 2$: overlap $= 8\times2^{3/2}/27 = 0.838$, so $P_{1s} = 0.702$.
5. The same method gives $P_{2s} = 0.250$ and $P_{3s} = 0.013$. Only $s$ states are populated, because the old state is spherically symmetric; the remaining 3.5% goes to higher $s$ states and to ionization.

**Answer:** about 70% of the ions are left in the ground state and 25% in the 2s state. Precision experiments that weigh the neutrino using tritium beta decay, such as KATRIN, must account for this distribution of final atomic or molecular states, since every excitation steals energy from the beta electron.

### 8.2 The adiabatic theorem

At the other extreme, Born and Fock (1928) proved the **adiabatic theorem**: if $\hat H(t)$ changes slowly enough, a system that starts in a nondegenerate eigenstate $\lvert n(0)\rangle$ remains in the *instantaneous* eigenstate $\lvert n(t)\rangle$ of $\hat H(t)$, apart from a phase:
$$\lvert\psi(t)\rangle = e^{i\theta_n(t)}e^{i\gamma_n(t)}\lvert n(t)\rangle, \qquad \theta_n = -\frac{1}{\hbar}\int_0^tE_n(t')\,dt', \qquad \gamma_n = i\int_0^t\langle n\vert\partial_{t'}n\rangle\,dt'$$
To see why, expand $\lvert\psi\rangle = \sum_mc_me^{i\theta_m}\lvert m(t)\rangle$ in instantaneous eigenstates. Differentiating $\hat H\lvert n\rangle = E_n\lvert n\rangle$ and projecting onto $\langle m\rvert$ gives $\langle m\vert\dot n\rangle = \langle m\vert\dot{\hat H}\vert n\rangle/(E_n - E_m)$ for $m \neq n$. These couplings appear multiplied by the rapidly oscillating phase $e^{i(\theta_n - \theta_m)}$, so they average away unless they are large. The resulting condition is
$$\hbar\,\lvert\langle m\vert\dot{\hat H}\vert n\rangle\rvert \ll (E_n - E_m)^2 \quad \text{for all } m \neq n$$
"Slow" is therefore always relative to the energy gap. The second phase $\gamma_n$ is the **Berry phase** (1984): for a Hamiltonian taken around a closed loop in parameter space it depends only on the geometry of the loop, not on how fast it is traversed, and it is measurable in interference experiments. Adiabatic ideas underlie the Born–Oppenheimer approximation for molecules (electrons adjust adiabatically to slowly moving nuclei), adiabatic invariants (Ehrenfest, 1916), adiabatic rapid passage in NMR, and adiabatic quantum computing.

### 8.3 Landau–Zener transitions

A common situation is an **avoided crossing**. Two "diabatic" states have energies whose difference changes linearly in time, $E_1 - E_2 = \alpha t$, and they are coupled by a constant matrix element $V$. The true (adiabatic) levels never cross; the minimum gap is $2\lvert V\rvert$ at $t = 0$. If the system starts in the lower adiabatic level long before the crossing, the probability that it jumps across the gap (stays in the original diabatic state) is the **Landau–Zener formula** (1932):
$$P_{\text{LZ}} = \exp\!\left(-\frac{2\pi\lvert V\rvert^2}{\hbar\lvert\alpha\rvert}\right)$$
Slow sweeps give $P_{\text{LZ}} \to 0$ (adiabatic following); fast sweeps give $P_{\text{LZ}} \to 1$ (sudden passage). The formula is used for charge transfer in atomic collisions, nonadiabatic chemical reactions, sweeps of qubit frequencies, and the resonant conversion of solar neutrinos inside the Sun (the MSW effect).

### Worked Example 8.2 – Sweeping through an avoided crossing

**Problem:** Two levels of a qubit are coupled with $\lvert V\rvert = h\times0.50$ MHz (minimum gap $h\times1.0$ MHz). Their diabatic frequency difference is swept at a rate $\alpha = h\times1.0$ MHz/μs. What is the probability of a nonadiabatic transition? What if the sweep is 100 times faster?

1. Write $V = hf_V$ and $\alpha = hr$, with $f_V = 5.0\times10^5$ Hz and $r = 1.0\times10^{12}$ Hz/s.
2. The exponent becomes $\dfrac{2\pi h^2f_V^2}{(h/2\pi)\,h\,r} = \dfrac{4\pi^2f_V^2}{r} = \dfrac{4\pi^2(2.5\times10^{11})}{1.0\times10^{12}} = \pi^2 = 9.87$.
3. $P_{\text{LZ}} = e^{-9.87} = 5.2\times10^{-5}$.
4. At 100 MHz/μs the exponent is $0.0987$ and $P_{\text{LZ}} = 0.906$.

**Answer:** at 1 MHz/μs the system follows the adiabatic level with probability 0.99995; a sweep 100 times faster leaves it in the diabatic state 91% of the time. A factor of 100 in speed changes the outcome from almost perfectly adiabatic to almost perfectly sudden.

## 9. Scattering: Cross Sections

### 9.1 Definitions

In a scattering experiment a beam of particles with **flux** $\Phi$ (particles per unit area per unit time) strikes a target. For one target particle, the number scattered per unit time into a small solid angle $d\Omega$ around direction $(\theta, \phi)$ is proportional to the flux:
$$\frac{dN}{dt} = \Phi\,\frac{d\sigma}{d\Omega}\,d\Omega$$
The proportionality constant $d\sigma/d\Omega$ is the **differential cross section**, an area per unit solid angle. Integrating over all directions gives the **total cross section** $\sigma$. A target of thickness $x$ containing $n$ scatterers per unit volume removes a fraction $n\sigma x$ of the beam when this is small; in general the unscattered beam falls as $I = I_0e^{-n\sigma x}$, with mean free path $1/(n\sigma)$. Nuclear and particle physicists use the **barn**: 1 b $= 10^{-28}$ m² $= 100$ fm².

Classically, a particle with **impact parameter** $b$ is deflected through an angle $\theta(b)$, and particles passing through the ring of area $2\pi b\,db$ emerge into the solid angle $2\pi\sin\theta\,d\theta$:
$$\frac{d\sigma}{d\Omega} = \frac{b}{\sin\theta}\left\lvert\frac{db}{d\theta}\right\rvert$$
For a hard sphere of radius $a$, $b = a\cos(\theta/2)$ gives $d\sigma/d\Omega = a^2/4$ (isotropic) and $\sigma = \pi a^2$, the geometric area.

### 9.2 The quantum scattering problem

Quantum mechanically, we look for a stationary state of energy $E = \hbar^2k^2/2m$ which far from the target consists of an incident plane wave plus an outgoing spherical wave:
$$\psi(\mathbf r) \longrightarrow e^{ikz} + f(\theta, \phi)\,\frac{e^{ikr}}{r} \qquad (r \to \infty)$$
The incident wave carries flux $\hbar k/m$ per unit area; the scattered wave carries flux $(\hbar k/m)\lvert f\rvert^2/r^2$, so the number of particles crossing the area $r^2d\Omega$ per unit time is $(\hbar k/m)\lvert f\rvert^2d\Omega$. Dividing,
$$\frac{d\sigma}{d\Omega} = \lvert f(\theta, \phi)\rvert^2$$
The **scattering amplitude** $f$ contains all the physics; the remaining sections compute it.

| Process | Energy | Cross section |
|---|---|---|
| Thomson scattering of light by a free electron | photon energy much below 511 keV | 0.665 b |
| Neutron–proton elastic scattering (free proton) | thermal | about 20.4 b |
| Neutron capture ¹⁹⁷Au(n,γ) | thermal, 0.0253 eV | 98.7 b |
| Neutron-induced fission of ²³⁵U | thermal | about 585 b |
| ¹⁰B(n,α)⁷Li | thermal | about 3840 b |
| Neutron absorption by ¹³⁵Xe | thermal | about $2.6\times10^6$ b |
| Resonant scattering of 589 nm light by a Na atom (two-level limit) | on resonance | $1.7\times10^{15}$ b |

The table spans fifteen orders of magnitude. A cross section is an *effective* area for a particular process, not the physical size of the target.

## 10. The Born Approximation

### 10.1 Derivation from the golden rule

Treat the potential $V(\mathbf r)$ as a perturbation causing transitions between free-particle plane waves in a box of volume $L^3$: $\lvert\mathbf k\rangle = L^{-3/2}e^{i\mathbf k\cdot\mathbf r}$. The matrix element between the incident wave $\mathbf k$ and a scattered wave $\mathbf k'$ (with $\lvert\mathbf k'\rvert = \lvert\mathbf k\rvert$ for elastic scattering) is
$$V_{\mathbf k'\mathbf k} = \frac{1}{L^3}\int e^{-i\mathbf k'\cdot\mathbf r}\,V(\mathbf r)\,e^{i\mathbf k\cdot\mathbf r}\,d^3r = \frac{\tilde V(\mathbf q)}{L^3}, \qquad \tilde V(\mathbf q) = \int e^{-i\mathbf q\cdot\mathbf r}\,V(\mathbf r)\,d^3r$$
where $\hbar\mathbf q = \hbar(\mathbf k' - \mathbf k)$ is the **momentum transfer**, of magnitude $q = 2k\sin(\theta/2)$. Fermi's golden rule with the density of states of Section 4.3 gives the rate into $d\Omega$:
$$d\Gamma = \frac{2\pi}{\hbar}\,\frac{\lvert\tilde V(\mathbf q)\rvert^2}{L^6}\,\frac{L^3mk}{8\pi^3\hbar^2}\,d\Omega$$
The incident flux is the density $1/L^3$ times the speed $\hbar k/m$. Dividing the rate by the flux, the box size cancels:
$$\frac{d\sigma}{d\Omega} = \left(\frac{m}{2\pi\hbar^2}\right)^2\lvert\tilde V(\mathbf q)\rvert^2, \qquad f_{\text{Born}}(\theta) = -\frac{m}{2\pi\hbar^2}\,\tilde V(\mathbf q)$$
This is the **first Born approximation** (Born, 1926). The same result follows from the exact integral equation for scattering (the Lippmann–Schwinger equation, 1950), whose first iteration replaces the true wavefunction inside the potential by the incident plane wave. The key insight is that **the scattering amplitude is the Fourier transform of the potential**: scattering at large momentum transfer probes structure at short distances, roughly $1/q$. This is the principle behind X-ray, electron and neutron diffraction, and behind measurements of nuclear and proton sizes.

### 10.2 Central potentials and the Yukawa potential

For a spherically symmetric potential, choose $\mathbf q$ along the polar axis; the angular integral $\int_0^\pi e^{-iqr\cos\theta'}\,2\pi\sin\theta'\,d\theta' = 4\pi\sin(qr)/(qr)$ gives
$$\tilde V(q) = \frac{4\pi}{q}\int_0^{\infty}r\,V(r)\sin(qr)\,dr$$
For the **Yukawa potential** $V(r) = \beta e^{-\mu r}/r$, the integral is $\int_0^\infty e^{-\mu r}\sin(qr)\,dr = q/(q^2 + \mu^2)$, so
$$\tilde V(q) = \frac{4\pi\beta}{q^2 + \mu^2}, \qquad \frac{d\sigma}{d\Omega} = \left(\frac{2m\beta}{\hbar^2}\right)^2\frac{1}{\left[4k^2\sin^2(\theta/2) + \mu^2\right]^2}$$
Yukawa (1935) proposed this form for the nuclear force carried by a massive particle, with range $1/\mu = \hbar/(m_\pi c) \approx 1.41$ fm for the pion. The same form describes a Coulomb potential screened by surrounding charges.

### 10.3 When is the Born approximation valid?

The approximation requires the scattered wave inside the potential to be small compared with the incident one. For a potential of strength $V_0$ and range $a$, a rough criterion at low energy is $\lvert V_0\rvert \ll \hbar^2/(ma^2)$ (the potential is too weak to bind a state), and at high energy ($ka \gg 1$) it is $\lvert V_0\rvert a/(\hbar v) \ll 1$. The approximation therefore improves with increasing energy. For Coulomb scattering the relevant parameter is $\eta = Z_1Z_2e^2/(4\pi\varepsilon_0\hbar v) = Z_1Z_2\,\alpha\,c/v$, and the Born approximation formally requires $\eta \ll 1$.

## 11. Rutherford Scattering

Letting $\mu \to 0$ in the Yukawa result with $\beta = Z_1Z_2e^2/(4\pi\varepsilon_0)$ and $E = \hbar^2k^2/2m$ gives $2m\beta/(\hbar^2\cdot4k^2\sin^2(\theta/2)) = \beta/(4E\sin^2(\theta/2))$, and hence the **Rutherford formula**:
$$\frac{d\sigma}{d\Omega} = \left(\frac{Z_1Z_2e^2}{16\pi\varepsilon_0E}\right)^2\frac{1}{\sin^4(\theta/2)}$$
Several features deserve comment:

- **A remarkable coincidence.** Rutherford derived this formula in 1911 from classical hyperbolic orbits. The Born approximation gives exactly the same result, and so does the exact quantum solution of the Coulomb problem (Gordon, 1928), whose amplitude differs from the Born amplitude only by a phase. The Coulomb potential is the only common case where classical and quantum cross sections agree exactly.
- **Infinite total cross section.** The $\sin^{-4}(\theta/2)$ divergence at small angles reflects the infinite range of the Coulomb force. In real matter, atomic electrons screen the nucleus (effectively a Yukawa potential with $\mu \neq 0$) and remove the divergence.
- **Strong energy dependence.** The cross section scales as $1/E^2$, so slower particles scatter much more.
- **Identical particles** (for example alpha particles on helium) show quantum interference between the two indistinguishable outcomes; Mott (1930) worked out the modified formula.
- **Deviations reveal the nucleus.** When the distance of closest approach becomes comparable to the nuclear radius, the strong force acts and the cross section departs from Rutherford's prediction. Such departures gave early estimates of nuclear sizes.

### Worked Example 11.1 – Alpha particles on gold

**Problem:** Alpha particles of kinetic energy 7.7 MeV (similar to those used by Geiger and Marsden) strike a gold foil ($Z = 79$, density 19.32 g/cm³, molar mass 196.97 g/mol) 1.0 μm thick. A detector of area 1.0 cm² is placed 10 cm from the foil at $\theta = 90°$. (a) Find the distance of closest approach in a head-on collision. (b) Find $d\sigma/d\Omega$ at 90° and at 10°. (c) For a beam of $1.0\times10^6$ alpha particles per second, find the count rate. (d) Is the Born approximation formally valid? Use $e^2/(4\pi\varepsilon_0) = 1.440$ MeV·fm and neglect the recoil of the gold nucleus.

1. Coupling strength: $\beta = Z_1Z_2e^2/(4\pi\varepsilon_0) = 2\times79\times1.440 = 227.5$ MeV·fm.
2. Closest approach (head-on, all kinetic energy converted to potential energy): $d = \beta/E = 227.5/7.7 = 29.5$ fm. A gold nucleus has a radius of about $1.2A^{1/3} = 7.0$ fm, so the alpha never touches it and the force is pure Coulomb.
3. Prefactor: $(\beta/4E)^2 = (227.5/30.8)^2 = (7.39\ \text{fm})^2 = 54.6$ fm².
4. At 90°: $\sin^4(45°) = 0.25$, so $d\sigma/d\Omega = 218$ fm²/sr $= 2.18$ b/sr. At 10°: $\sin^4(5°) = 5.77\times10^{-5}$, giving $9.46\times10^3$ b/sr, about 4300 times larger.
5. Target density: $n = (19.32\times10^3\ \text{kg/m}^3)(6.022\times10^{23})/(0.19697\ \text{kg/mol}) = 5.91\times10^{28}$ m⁻³, so the areal density is $nx = 5.91\times10^{22}$ m⁻².
6. Solid angle of detector: $\Delta\Omega = 1.0\times10^{-4}\ \text{m}^2/(0.10\ \text{m})^2 = 0.010$ sr.
7. Fraction counted: $nx\,(d\sigma/d\Omega)\,\Delta\Omega = (5.91\times10^{22})(2.18\times10^{-28})(0.010) = 1.29\times10^{-7}$. Count rate: $0.13$ s⁻¹, about 460 per hour.
8. Born validity: the alpha speed is $v/c = \sqrt{2E/m_\alpha c^2} = \sqrt{2(7.7)/3727} = 0.064$, so $\eta = 158\,\alpha\,c/v = 17.9 \gg 1$.

**Answer:** (a) 29.5 fm; (b) 2.18 b/sr at 90° and $9.5\times10^3$ b/sr at 10°; (c) about 0.13 counts per second; (d) no, since $\eta \approx 18$, yet the Born result is exact for the pure Coulomb potential. A large $\eta$ actually means the motion is nearly classical, which is why Rutherford's classical calculation works so well.

## 12. Partial Waves and Phase Shifts

For a central potential, angular momentum is conserved, so it is natural to decompose the incident plane wave into components of definite orbital angular momentum $\ell$ (the **partial waves** $\ell = 0, 1, 2, \ldots$, called s, p, d, ...). Far from the target, each partial wave is a superposition of an incoming and an outgoing spherical wave. In elastic scattering, probability conservation means the potential cannot change the *amount* of outgoing wave in each $\ell$; it can only shift its phase. The radial wavefunction far away behaves as $\sin(kr - \ell\pi/2 + \delta_\ell)/r$, where $\delta_\ell$ is the **phase shift**. All of elastic scattering is encoded in the set of phase shifts:
$$f(\theta) = \frac{1}{k}\sum_{\ell=0}^{\infty}(2\ell + 1)\,e^{i\delta_\ell}\sin\delta_\ell\,P_\ell(\cos\theta), \qquad \sigma = \frac{4\pi}{k^2}\sum_{\ell=0}^{\infty}(2\ell + 1)\sin^2\delta_\ell$$
Qualitative lessons follow without solving any equations:

- **Which partial waves matter.** Semiclassically, a particle with angular momentum $\hbar\ell$ passes at impact parameter $b \approx \ell/k$. A potential of range $a$ affects only $\ell \lesssim ka$. At low energy ($ka \ll 1$) only the s-wave scatters, and the scattering is isotropic.
- **Sign of the phase shift.** An attractive potential pulls the wave in and gives $\delta_\ell > 0$; a repulsive one pushes it out and gives $\delta_\ell < 0$.
- **Unitarity limit.** Since $\sin^2\delta_\ell \leq 1$, each partial wave contributes at most $4\pi(2\ell + 1)/k^2$.
- **Scattering length.** At low energy $\delta_0 \approx -ka_s$, defining the **scattering length** $a_s$, and $\sigma \to 4\pi a_s^2$.
- **Hard sphere.** For an impenetrable sphere of radius $a$, the s-wave radial function must vanish at $r = a$, so $u(r) \propto \sin[k(r - a)]$ and $\delta_0 = -ka$. At low energy $\sigma = 4\pi a^2$, *four times* the classical value; at high energy $\sigma \to 2\pi a^2$, twice the geometric area, because the diffracted wave that forms the shadow counts as scattering.
- **Optical theorem.** Comparing the two formulas above gives $\sigma = (4\pi/k)\,\mathrm{Im}\,f(0)$: the total cross section is fixed by the forward amplitude, which interferes destructively with the incident wave to remove flux from the beam.
- **Ramsauer–Townsend effect.** For slow electrons on argon, krypton or xenon, the s-wave phase shift passes through $\pi$ at an energy below about 1 eV, so $\sin^2\delta_0 = 0$ and the atoms become nearly transparent, something no classical model can explain.

### Worked Example 12.1 – Low-energy neutron–proton scattering

**Problem:** Slow neutrons scatter from free protons. The neutron and proton spins can combine to total spin $S = 0$ (singlet, 1 state) or $S = 1$ (triplet, 3 states), with scattering lengths $a_s = -23.74$ fm and $a_t = 5.42$ fm. Find the total cross section for unpolarized thermal neutrons (0.0253 eV), and check that only the s-wave matters.

1. Thermal neutron wave number: $k = \sqrt{2m_nE}/\hbar = 3.49\times10^{10}$ m⁻¹ (wavelength 0.180 nm). With a force range of about 2 fm, $ka \approx 7\times10^{-5} \ll 1$: pure s-wave.
2. For unpolarized beams and targets, the four spin states are equally likely: weight $1/4$ for the singlet, $3/4$ for the triplet.
3. $\sigma = 4\pi\left(\tfrac14a_s^2 + \tfrac34a_t^2\right) = \pi\left(a_s^2 + 3a_t^2\right) = \pi(563.6 + 88.1)\ \text{fm}^2 = 2047\ \text{fm}^2$.
4. Convert: $2047\ \text{fm}^2 = 20.5$ b.

**Answer:** about 20.5 b, in good agreement with the measured value of about 20.4 b. The singlet contributes 17.7 b and the triplet only 2.8 b. The large negative singlet scattering length reflects a singlet state that just fails to be bound (a "virtual state"), while the triplet channel contains the real bound state, the deuteron. Phase-shift analysis of this kind is how nuclear forces are extracted from scattering data.

## 13. Resonances

Sometimes the potential almost binds a state at positive energy, for example a state trapped behind a centrifugal or Coulomb barrier. Near that energy $E_R$, the incoming wave can build up inside the potential, and the phase shift rises rapidly through $\pi/2$. Near the resonance $\tan\delta_\ell \approx (\Gamma/2)/(E_R - E)$, so $\sin^2\delta_\ell = (\Gamma^2/4)/[(E - E_R)^2 + \Gamma^2/4]$ and the partial cross section takes the **Breit–Wigner** form (Breit and Wigner, 1936):
$$\sigma_\ell(E) = \frac{4\pi}{k^2}(2\ell + 1)\,\frac{\Gamma^2/4}{(E - E_R)^2 + \Gamma^2/4}$$
The peak reaches the unitarity limit and has full width at half maximum $\Gamma$. The particle is temporarily captured in a **quasi-bound state** whose lifetime is
$$\tau = \frac{\hbar}{\Gamma}$$
This is the same Lorentzian as the natural line shape of Section 7. An excited atom *is* a resonance in photon–atom scattering, and an unstable particle *is* a resonance in the scattering of its decay products. With particle spins and several decay channels, the general formula for a process $a \to b$ through the resonance is
$$\sigma_{a\to b}(E) = \frac{\pi}{k^2}\,g\,\frac{\Gamma_a\Gamma_b}{(E - E_R)^2 + \Gamma^2/4}, \qquad g = \frac{2J + 1}{(2s_1 + 1)(2s_2 + 1)}$$
where $\Gamma_a$ and $\Gamma_b$ are partial widths, $J$ is the resonance spin and $s_1$, $s_2$ are the spins of the colliding particles. Resonances are everywhere: neutron resonances in heavy nuclei (²³⁸U has a strong one at 6.67 eV), the Hoyle state of carbon-12 at 7.654 MeV through which stars make carbon, the Δ(1232) in pion–nucleon scattering, and the Z boson in electron–positron collisions.

### Worked Example 13.1 – Resonances from atoms to the Z boson

**Problem:** (a) The Z boson appears as a resonance at 91.19 GeV with width $\Gamma = 2.495$ GeV. Find its lifetime. (b) Find the peak resonant cross section of a sodium atom for 589.0 nm light, treating the D2 cycling transition as a two-level system (lower level $J = 0$, upper level $J = 1$, photon with two polarization states), and compare it with the size of the atom.

1. (a) $\tau = \hbar/\Gamma = (6.582\times10^{-25}\ \text{GeV·s})/(2.495\ \text{GeV}) = 2.64\times10^{-25}$ s. Even at the speed of light it would travel only $c\tau = 7.9\times10^{-17}$ m before decaying, so it is detected only as a peak in the cross section as the collision energy is scanned.
2. (b) Purely elastic scattering: $\Gamma_a = \Gamma_b = \Gamma$, so at $E = E_R$ the general formula gives $\sigma_0 = 4\pi g/k^2$.
3. Statistical factor: $g = 3/(1\times2) = 3/2$, so $\sigma_0 = 6\pi/k^2 = 6\pi\lambda^2/(4\pi^2) = 3\lambda^2/(2\pi)$.
4. Numerically, $\sigma_0 = 3(589.0\times10^{-9}\ \text{m})^2/(2\pi) = 1.66\times10^{-13}$ m², equivalent to a disk of radius $\sqrt{\sigma_0/\pi} = 230$ nm.

**Answer:** (a) $2.6\times10^{-25}$ s; (b) $1.7\times10^{-13}$ m², about a million times the geometric cross section of an atom only a few tenths of a nanometre across. On resonance, an atom "looks" as large as the wavelength of light, which is why a cloud of a few million cold atoms casts a clearly visible shadow and why laser cooling is so effective. The measured Z width also counts its invisible decays into neutrinos; experiments at CERN's LEP collider (from 1989) found it consistent with exactly three light neutrino species (about 2.98 from the fits).

## 14. Historical Development

| Year | People | Contribution |
|---|---|---|
| 1909 | Hans Geiger, Ernest Marsden | about 1 in 8000 alpha particles bounces back from thin metal foils |
| 1911 | Ernest Rutherford | nuclear model of the atom and the $\sin^{-4}(\theta/2)$ scattering law |
| 1913 | Geiger, Marsden | detailed confirmation of the angular, thickness and energy dependence |
| 1916 | Paul Ehrenfest | adiabatic invariants as a guide to quantization |
| 1916–1917 | Albert Einstein | A and B coefficients; prediction of stimulated emission |
| 1921–1922 | Carl Ramsauer; John Townsend and V. A. Bailey | anomalous transparency of noble gases to slow electrons |
| 1926 | Max Born | quantum theory of collisions, the Born approximation and the probability interpretation |
| 1926–1927 | Paul Dirac | time-dependent perturbation theory; quantized radiation field and the A coefficient |
| 1927 | Hilding Faxén, Johan Holtsmark | partial-wave and phase-shift method |
| 1928 | Born, Vladimir Fock | proof of the adiabatic theorem |
| 1930 | Victor Weisskopf, Eugene Wigner | theory of natural line width and exponential decay |
| 1931 | Maria Goeppert Mayer | theory of two-photon absorption and emission |
| 1932 | Lev Landau, Clarence Zener (also Stueckelberg, Majorana) | transitions at avoided crossings |
| 1934 | Enrico Fermi | theory of beta decay built on the transition-rate formula |
| 1936 | Gregory Breit, Wigner | resonance formula for nuclear reactions |
| 1937–1938 | Isidor Rabi | Rabi formula; molecular-beam magnetic resonance (Nobel Prize 1944) |
| 1946 | Edward Purcell; Felix Bloch | NMR in bulk matter; Purcell also predicts that a resonant cavity changes spontaneous emission rates |
| 1950 | Fermi; Bernard Lippmann, Julian Schwinger | the name "golden rule" in Fermi's lecture notes; integral equation of scattering |
| 1950s | Robert Hofstadter | electron scattering reveals the sizes of nuclei and nucleons (Nobel Prize 1961) |
| 1960 | Theodore Maiman | first laser, using ruby |
| 1984 | Michael Berry | geometric phase in adiabatic evolution |
| 1989 | LEP experiments at CERN | Z resonance line shape fixes the number of light neutrino species at three |

Two threads run through this history. Scattering, from Rutherford's gold foil to today's colliders, has been the main way to see structure too small for any microscope. Transition rates, from Einstein's coefficients to Fermi's beta decay theory, turned quantum mechanics from a theory of energy levels into a theory of processes. Born's 1926 collision paper links the two: in analysing scattering he introduced both the approximation that bears his name and the statistical interpretation of the wavefunction.

## 15. Applications

- **Lasers and optical amplifiers.** Stimulated emission, population inversion and lifetimes govern every laser. Solid-state laser media store energy in long-lived upper levels (about 0.23 ms in Nd:YAG and about 3 ms in ruby), while diode lasers rely on fast radiative recombination.
- **Atomic clocks and spectroscopy.** Narrow lines give precise frequencies. The SI second is defined by the 9 192 631 770 Hz hyperfine transition of caesium-133, and optical clocks use forbidden transitions with lifetimes of seconds or longer because their natural widths are tiny.
- **Medicine.** MRI uses resonant Rabi rotations of proton spins (Worked Example 3.1). Fluorescence lifetime imaging distinguishes tissues and molecular environments through excited-state lifetimes of a few nanoseconds. X-ray imaging contrast comes from photon cross sections: the photoelectric cross section rises steeply with atomic number and falls steeply with photon energy, so bone (calcium) and iodine or barium contrast agents absorb much more than soft tissue. Boron neutron capture therapy exploits the 3840 b cross section of ¹⁰B.
- **Nuclear reactors.** Reactor design is cross-section bookkeeping: fission (585 b for thermal neutrons on ²³⁵U), moderation by elastic scattering, and parasitic absorption (¹³⁵Xe, with millions of barns, can shut down a reactor after a power reduction). As fuel heats up, Doppler broadening of the ²³⁸U capture resonances increases neutron absorption, an inherent safety feedback.
- **Semiconductors and solar cells.** Golden-rule absorption rates depend on the joint density of states and on momentum conservation. In direct-gap materials (GaAs, GaN) electrons and holes recombine by emitting a photon directly, so they make efficient LEDs and lasers; in indirect-gap silicon a phonon must also participate (a second-order process), so silicon emits light poorly.
- **Materials analysis.** Rutherford backscattering spectrometry with MeV helium ions measures the composition and thickness of thin films; X-ray, electron and neutron diffraction use the Fourier-transform property of the Born approximation to determine crystal structures.
- **Particle physics.** The event rate in a collider is luminosity times cross section; new particles appear as Breit–Wigner peaks, as the Z and the Higgs boson did.
- **Nature.** The sky is blue because the cross section for scattering light by molecules grows as $\omega^4$; the green and red auroral colours come from forbidden transitions of atomic oxygen; the 21 cm line, despite its 11-million-year lifetime, maps hydrogen throughout the galaxy because there is so much hydrogen.

## 16. Common Misconceptions

- **"A quantum jump is an instantaneous event triggered at a definite moment."** In the theory, amplitudes in other states build up continuously, quadratically at first and then (for a continuum) linearly. The outcome of a measurement is discrete, but the evolution of the state is smooth.
- **"Fermi's golden rule gives a probability."** It gives a *rate*, valid only for transitions into a continuum and only in a window of times. A single discrete level driven by monochromatic light shows Rabi oscillations, not a constant rate.
- **"Forbidden transitions never happen."** They are forbidden only at the electric-dipole level. They proceed via magnetic-dipole, electric-quadrupole or two-photon processes, or through collisions, just much more slowly.
- **"Spontaneous emission is a fixed property of an isolated atom."** The rate depends on the density of photon modes available. Inside a resonant cavity it can be enhanced (the Purcell effect) or suppressed; in a photonic band gap it can be nearly switched off.
- **"The natural linewidth is an experimental imperfection."** It is intrinsic, set by the lifetime through $\Delta E = \hbar/\tau$. Observed lines are usually much wider, because Doppler and collisional broadening are added on top.
- **"The cross section is the physical size of the target."** It is an effective area for a specific process and energy. For slow particles a hard sphere has $\sigma = 4\pi a^2$, not $\pi a^2$; a resonant atom presents an area a million times its size; a neutrino passes through the Earth almost unhindered.
- **"Sudden approximation means the state changes suddenly."** The opposite: the *Hamiltonian* changes suddenly and the *state* has no time to change at all.
- **"Adiabatic means no heat flows."** In thermodynamics it does; in quantum mechanics it means slow compared with $\hbar/\Delta E$. The two meanings are related (a slowly expanded box keeps its quantum number, like the reversible adiabatic expansion of a gas) but not identical.
- **"The Born approximation is a classical approximation."** It is a weak-potential, quantum approximation. Its agreement with the classical Rutherford formula is a special property of the Coulomb potential.

## 17. Connections to Other Topics

- **Earlier chapters of this series.** The interaction picture extends the Schrödinger and Heisenberg pictures of chapter 3; the oscillator matrix elements come from chapter 4; selection rules rely on spherical harmonics and angular momentum addition from chapter 5; the golden rule refines the brief treatment in chapter 6; Rabi pulses are the single-qubit gates of chapter 7, and decoherence is coupling to a continuum, much like spontaneous emission.
- **Statistical mechanics.** Einstein's derivation is an application of detailed balance, which also links forward and reverse reaction rates in chemistry.
- **Chemistry and spectroscopy.** The Beer–Lambert law of absorption, $I = I_0e^{-n\sigma\ell}$, is the cross-section concept in another form; UV–visible, infrared and Raman selection rules all follow from the same symmetry arguments; Landau–Zener transitions occur at avoided crossings of molecular potential energy surfaces.
- **Nuclear and particle physics.** Fermi's beta decay theory, neutron cross sections, Breit–Wigner resonances and form factors from electron scattering are direct applications; Feynman diagrams are terms of the Dyson series.
- **Condensed matter.** Electrical resistance comes from golden-rule scattering of electrons by phonons and impurities; optical absorption in semiconductors depends on band structure through the density of states.
- **Classical waves and optics.** The Born approximation corresponds to single scattering in optics and to the Fourier-optics description of diffraction; the optical theorem is the reason a large opaque disk removes twice its area from a beam.
- **Astrophysics.** Stellar opacities, the 21 cm line, interstellar forbidden lines and the triple-alpha process through the Hoyle resonance all rely on transition rates and resonances.

## 18. Practice Problems

1. **(Easy)** The sodium 3p ²P₃/₂ level has a lifetime of 16.2 ns and decays by emitting 589.0 nm light. Find the natural linewidth in hertz, the energy width in eV, and the quality factor $\nu_0/\Delta\nu$.
2. **(Easy)** Ignoring spin, which of these hydrogen transitions are allowed in the electric-dipole approximation: (a) 3d → 2p; (b) 3d → 1s; (c) 3s → 2p; (d) 2s → 1s; (e) 4f → 3d; (f) 3p → 2p; (g) 4p → 1s?
3. **(Easy)** A gold foil 25 μm thick (density 19.32 g/cm³, molar mass 196.97 g/mol) is placed in a thermal neutron flux of $1.0\times10^{12}$ neutrons per cm² per second. The capture cross section is 98.7 b. Find the capture rate per cm² of foil and the number of ¹⁹⁸Au nuclei produced in one hour (half-life 2.69 d).
4. **(Medium)** Alpha particles of 5.0 MeV scatter from gold. (a) Find the head-on distance of closest approach. (b) Find $d\sigma/d\Omega$ at 90°. (c) By what factor does the count rate at 10° exceed that at 90°? (d) Estimate the alpha energy at which head-on collisions reach the nuclear surface, taking the sum of the radii as $1.2(4^{1/3} + 197^{1/3})$ fm and ignoring recoil.
5. **(Medium)** A particle is in the ground state of an infinite square well of width $L$ (walls at $x = 0$ and $x = L$). The right wall is suddenly moved to $x = 2L$. Find the probabilities of finding the particle in the ground state and in the first excited state of the new well. What would happen if the wall were moved very slowly instead?
6. **(Medium)** Estimate the spontaneous emission rate and lifetime for an electric-dipole transition at 500 nm whose matrix element is $\lvert\langle f\vert\hat{\mathbf r}\vert i\rangle\rvert = a_0$.
7. **(Medium)** The Δ(1232) resonance in pion–nucleon scattering has a width of about 117 MeV. (a) Find its lifetime and the distance light travels in that time. (b) Using the Breit–Wigner formula with constant width, at which energies does the cross section fall to half and to one tenth of its peak value?
8. **(Medium–hard)** In Worked Example 8.2, what is the fastest sweep rate (in MHz/μs) that still gives at least 99% adiabatic following?
9. **(Hard)** A charged particle in a harmonic trap (mass $m$, angular frequency $\omega$) starts in the ground state. A constant force $F$ acts from $t = 0$ to $t = T$. Use first-order perturbation theory to find the probability of excitation to $n = 1$. Evaluate it for the ⁴⁰Ca⁺ ion of Worked Example 2.1 ($\omega = 2\pi\times1.00$ MHz, $F = e\times0.050$ V/m) for $T = 0.25$ μs, 0.50 μs and 1.00 μs, and interpret the last result.
10. **(Hard)** Use the Born approximation to find the differential and total cross sections for the Gaussian potential $V(r) = V_0e^{-r^2/b^2}$. Find the low-energy limit and the corresponding scattering length.

### Solutions

**1.** $\Delta\nu = 1/(2\pi\tau) = 1/(2\pi\times16.2\times10^{-9}\ \text{s}) = 9.82$ MHz. $\Delta E = h\Delta\nu = (4.136\times10^{-15}\ \text{eV·s})(9.82\times10^6\ \text{Hz}) = 4.06\times10^{-8}$ eV. With $\nu_0 = c/\lambda = 5.09\times10^{14}$ Hz, $Q = 5.2\times10^7$. **Answer:** 9.8 MHz, $4.1\times10^{-8}$ eV, $Q \approx 5\times10^7$.

**2.** Apply $\Delta\ell = \pm1$ (any $\Delta n$). (a) $\ell$: 2 → 1, allowed. (b) 2 → 0, forbidden (an E2 transition). (c) 0 → 1, allowed. (d) 0 → 0, forbidden (parity unchanged; decays by two-photon emission). (e) 3 → 2, allowed. (f) 1 → 1, forbidden (parity unchanged). (g) 1 → 0, allowed (it is the Lyman-γ line). **Answer:** a, c, e and g are allowed; b, d and f are forbidden.

**3.** Number density: $n = 19.32 \times 6.022\times10^{23}/196.97 = 5.91\times10^{22}$ cm⁻³. Areal density: $nx = 5.91\times10^{22} \times 2.5\times10^{-3}\ \text{cm} = 1.48\times10^{20}$ cm⁻². Capture probability per neutron: $nx\sigma = 1.48\times10^{20}\times98.7\times10^{-24} = 0.0146$, small enough for the thin-target formula (the exact $1 - e^{-0.0146} = 0.0145$). Rate: $1.0\times10^{12} \times 0.0146 = 1.46\times10^{10}$ captures per second per cm². In one hour: $1.46\times10^{10}\times3600 = 5.2\times10^{13}$ nuclei; only about 0.5% of them decay during the hour, since one hour is about 1.5% of the half-life. **Answer:** $1.5\times10^{10}$ s⁻¹ cm⁻²; about $5.2\times10^{13}$ ¹⁹⁸Au nuclei per cm².

**4.** (a) $d = 227.5\ \text{MeV·fm}/5.0\ \text{MeV} = 45.5$ fm. (b) $(\beta/4E)^2 = (227.5/20.0)^2 = 129.4$ fm², and dividing by $\sin^4 45° = 0.25$ gives 518 fm²/sr $= 5.18$ b/sr. (c) The ratio is $\sin^4(45°)/\sin^4(5°) = 0.25/5.77\times10^{-5} = 4.33\times10^3$. (d) Sum of radii $= 1.2(1.587 + 5.819) = 8.89$ fm; setting $\beta/E = 8.89$ fm gives $E = 25.6$ MeV. **Answer:** 45.5 fm; 5.2 b/sr; about 4300; roughly 26 MeV (above this energy, deviations from the Rutherford formula appear at large angles).

**5.** Old ground state: $\psi_1 = \sqrt{2/L}\,\sin(\pi x/L)$ for $0 < x < L$. New eigenstates: $\phi_n = \sqrt{1/L}\,\sin(n\pi x/2L)$ for $0 < x < 2L$. Ground state: substituting $y = \pi x/L$,
$$\langle\phi_1\vert\psi_1\rangle = \frac{\sqrt2}{\pi}\int_0^{\pi}\sin y\,\sin\frac{y}{2}\,dy = \frac{\sqrt2}{\pi}\cdot\frac12\left[\int_0^\pi\cos\frac y2\,dy - \int_0^\pi\cos\frac{3y}{2}\,dy\right] = \frac{\sqrt2}{\pi}\cdot\frac12\left[2 + \frac23\right] = \frac{4\sqrt2}{3\pi}$$
so $P_1 = 32/(9\pi^2) = 0.360$. First excited state: $\phi_2 = \sqrt{1/L}\,\sin(\pi x/L)$ has the same shape as $\psi_1$ on $(0, L)$, so $\langle\phi_2\vert\psi_1\rangle = (\sqrt2/L)\int_0^L\sin^2(\pi x/L)\,dx = 1/\sqrt2$ and $P_2 = 0.500$. (The rest is spread over higher odd states, 13.0% in $n = 3$.) The energy expectation value is unchanged at the moment of expansion, $\pi^2\hbar^2/(2mL^2)$, four times the new ground-state energy. If the wall moved slowly, the adiabatic theorem says the particle would end in the new ground state with certainty, its energy falling by a factor of 4 as it does work on the moving wall. **Answer:** $P_1 = 0.360$, $P_2 = 0.500$; slow expansion gives $P_1 = 1$.

**6.** $\omega = 2\pi c/\lambda = 3.77\times10^{15}$ s⁻¹. $A = 4\alpha\omega^3a_0^2/(3c^2) = 4(7.297\times10^{-3})(3.77\times10^{15})^3(5.29\times10^{-11})^2/[3(3.00\times10^8)^2] = 1.6\times10^7$ s⁻¹, giving $\tau = 62$ ns. **Answer:** $A \approx 1.6\times10^7$ s⁻¹, $\tau \approx 60$ ns, the typical order of magnitude for allowed visible transitions (compare the table in Section 6).

**7.** (a) $\tau = \hbar/\Gamma = (6.582\times10^{-22}\ \text{MeV·s})/(117\ \text{MeV}) = 5.6\times10^{-24}$ s; $c\tau = 1.7\times10^{-15}$ m $= 1.7$ fm, about the size of a proton. (b) The Breit–Wigner factor $(\Gamma^2/4)/[(E - E_R)^2 + \Gamma^2/4]$ equals 1/2 when $\lvert E - E_R\rvert = \Gamma/2 = 58.5$ MeV, and 1/10 when $(E - E_R)^2 = 9\Gamma^2/4$, i.e. $\lvert E - E_R\rvert = 1.5\Gamma = 175.5$ MeV. **Answer:** $5.6\times10^{-24}$ s and 1.7 fm; half maximum at about 1174 and 1291 MeV, one tenth at about 1057 and 1408 MeV (centre-of-mass energies).

**8.** We need $P_{\text{LZ}} \leq 0.01$, i.e. $4\pi^2f_V^2/r \geq \ln100 = 4.605$. Hence $r \leq 4\pi^2(5.0\times10^5)^2/4.605 = 2.14\times10^{12}$ Hz/s. **Answer:** about 2.1 MHz/μs.

**9.** With $\hat V = -F\hat x$ for $0 < t < T$ and $\langle1\vert\hat x\vert0\rangle = \sqrt{\hbar/2m\omega}$:
$$c_1 = \frac{iF}{\hbar}\sqrt{\frac{\hbar}{2m\omega}}\int_0^Te^{i\omega t}\,dt = \frac{iF}{\hbar}\sqrt{\frac{\hbar}{2m\omega}}\;\frac{e^{i\omega T} - 1}{i\omega}, \qquad P_{0\to1} = \frac{2F^2}{m\hbar\omega^3}\sin^2\!\left(\frac{\omega T}{2}\right)$$
Numerically $2F^2/(m\hbar\omega^3) = 0.0739$, so $P = 0.037$ for $T = 0.25$ μs (a quarter period), $0.074$ for $T = 0.50$ μs (half a period) and $0$ for $T = 1.00$ μs (a full period). **Answer:** 0.037, 0.074 and 0. A force switched off after exactly one period leaves a classical oscillator at rest at its original position, and the quantum amplitude vanishes for the same reason: the Fourier component of the pulse at $\omega$ is zero.

**10.** The Fourier transform factorizes into three Gaussian integrals: $\tilde V(q) = V_0(\pi b^2)^{3/2}e^{-q^2b^2/4}$. Then
$$f(\theta) = -\frac{m}{2\pi\hbar^2}\tilde V(q) = -\frac{\sqrt\pi\,mV_0b^3}{2\hbar^2}\,e^{-q^2b^2/4}, \qquad \frac{d\sigma}{d\Omega} = \frac{\pi m^2V_0^2b^6}{4\hbar^4}\,e^{-k^2b^2(1 - \cos\theta)}$$
using $q^2 = 2k^2(1 - \cos\theta)$. Integrating with $x = \cos\theta$: $\int_{-1}^{1}e^{-k^2b^2(1 - x)}dx = (1 - e^{-2k^2b^2})/(k^2b^2)$, so
$$\sigma = \frac{\pi^2m^2V_0^2b^6}{2\hbar^4}\,\frac{1 - e^{-2k^2b^2}}{k^2b^2}$$
For $kb \ll 1$ the scattering is isotropic and $\sigma \to \pi^2m^2V_0^2b^6/\hbar^4$. Comparing with $\sigma = 4\pi a_s^2$ and $f(0) = -a_s$ gives the scattering length $a_s = \sqrt\pi\,mV_0b^3/(2\hbar^2)$ (positive for a repulsive potential). At high energy the cross section falls as $1/k^2 \propto 1/E$ and the scattering concentrates within angles of order $1/(kb)$. **Answer:** as above; the result is reliable only when $\lvert V_0\rvert \ll \hbar^2/(mb^2)$.

## 19. Summary

Transitions between quantum states require a time-dependent perturbation or coupling to a continuum. In the interaction picture the exact amplitude equations are $i\hbar\dot c_f = \sum_nV_{fn}e^{i\omega_{fn}t}c_n$; iterating them gives the Dyson series, whose first term is first-order perturbation theory. Transition probabilities are governed by the Fourier component of the perturbation at the transition frequency, which explains resonance, the energy–time trade-off and the contrast between sudden and adiabatic changes. A coherently driven two-level system Rabi-oscillates, while a transition into a continuum proceeds at the constant rate given by Fermi's golden rule.

For atoms in light, the electric-dipole approximation produces the selection rules (parity change, $\Delta\ell = \pm1$, $\Delta m = 0, \pm1$, $\Delta S = 0$), and Einstein's equilibrium argument links absorption, stimulated emission and spontaneous emission. Spontaneous rates scale as $\omega^3\lvert\mathbf d_{fi}\rvert^2$, giving nanosecond lifetimes for strong optical lines, and every finite lifetime implies a Lorentzian natural linewidth $\Gamma = 1/\tau$, usually hidden beneath Doppler and collisional broadening. Sudden changes leave the state untouched and spread it over the new levels; slow changes carry it along an instantaneous eigenstate, and the Landau–Zener formula interpolates between the two.

Scattering is quantified by cross sections, $d\sigma/d\Omega = \lvert f\rvert^2$. The Born approximation makes the amplitude the Fourier transform of the potential and, for the Coulomb potential, reproduces Rutherford's formula exactly. Partial-wave phase shifts organize scattering by angular momentum, explain why slow particles scatter isotropically, and lead to the optical theorem and the unitarity limit. Resonances, where a phase shift sweeps through $\pi/2$, give Breit–Wigner peaks whose width is the inverse lifetime of a quasi-bound state, the same physics as the natural linewidth of an atomic line.

### Key equations

- Interaction picture: $\lvert\psi_I\rangle = e^{i\hat H_0t/\hbar}\lvert\psi_S\rangle$, $\quad i\hbar\,\partial_t\lvert\psi_I\rangle = \hat V_I(t)\lvert\psi_I\rangle$
- First-order amplitude: $c_f^{(1)}(t) = -\dfrac{i}{\hbar}\displaystyle\int_0^tV_{fi}(t')\,e^{i\omega_{fi}t'}\,dt'$
- Constant perturbation: $P_{i\to f} = \dfrac{4\lvert V_{fi}\rvert^2}{\hbar^2\omega_{fi}^2}\sin^2(\omega_{fi}t/2)$
- Rabi formula: $P = \dfrac{\Omega^2}{\Omega^2 + \Delta^2}\sin^2\!\left(\tfrac12\sqrt{\Omega^2 + \Delta^2}\,t\right)$
- Fermi's golden rule: $\Gamma_{i\to f} = \dfrac{2\pi}{\hbar}\lvert V_{fi}\rvert^2\rho(E_f)$
- Dipole interaction: $\hat V = -\hat{\mathbf d}\cdot\boldsymbol{\mathcal E}$, $\quad\hat{\mathbf d} = -e\hat{\mathbf r}$
- Einstein relations: $g_1B_{12} = g_2B_{21}$, $\quad A = \dfrac{\hbar\omega^3}{\pi^2c^3}B_{21}$
- Spontaneous emission: $A = \dfrac{\omega^3\lvert\mathbf d_{fi}\rvert^2}{3\pi\varepsilon_0\hbar c^3} = \dfrac{4\alpha\omega^3}{3c^2}\lvert\mathbf r_{fi}\rvert^2$, $\quad\tau = 1/\sum A_k$
- Natural linewidth: $\Delta\nu = \dfrac{1}{2\pi\tau}$; Doppler width: $\Delta\nu_D = \dfrac{\nu_0}{c}\sqrt{\dfrac{8k_BT\ln2}{m}}$
- Sudden approximation: $P_n = \lvert\langle n_{\text{new}}\vert\psi_{\text{old}}\rangle\rvert^2$
- Adiabatic condition: $\hbar\lvert\langle m\vert\dot{\hat H}\vert n\rangle\rvert \ll (E_n - E_m)^2$; Landau–Zener: $P_{\text{LZ}} = e^{-2\pi\lvert V\rvert^2/(\hbar\lvert\alpha\rvert)}$
- Cross section: $d\sigma/d\Omega = \lvert f(\theta,\phi)\rvert^2$; thin target fraction $n\sigma x$
- Born approximation: $f = -\dfrac{m}{2\pi\hbar^2}\displaystyle\int e^{-i\mathbf q\cdot\mathbf r}V(\mathbf r)\,d^3r$, $\quad q = 2k\sin(\theta/2)$
- Rutherford: $\dfrac{d\sigma}{d\Omega} = \left(\dfrac{Z_1Z_2e^2}{16\pi\varepsilon_0E}\right)^2\dfrac{1}{\sin^4(\theta/2)}$
- Partial waves: $\sigma = \dfrac{4\pi}{k^2}\sum_\ell(2\ell + 1)\sin^2\delta_\ell$; optical theorem: $\sigma = \dfrac{4\pi}{k}\,\mathrm{Im}\,f(0)$
- Breit–Wigner: $\sigma_\ell = \dfrac{4\pi}{k^2}(2\ell + 1)\dfrac{\Gamma^2/4}{(E - E_R)^2 + \Gamma^2/4}$, $\quad\tau = \hbar/\Gamma$
