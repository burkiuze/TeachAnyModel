---
title: Oscillations - Simple Harmonic, Damped and Driven Motion
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [simple harmonic motion, spring-mass system, pendulum, physical pendulum, angular frequency, period, damping, quality factor, driven oscillator, resonance, coupled oscillators, normal modes]
---

# Oscillations: Simple Harmonic, Damped and Driven Motion

Oscillations — repetitive motions about an equilibrium — appear at every scale of nature: vibrating atoms in a crystal, a swinging pendulum, a guitar string, alternating current in a circuit, the quartz crystal in a watch, and the oscillating electric and magnetic fields of light. Remarkably, nearly all of them are described by the same mathematics: the harmonic oscillator. As shown in the energy chapter, small displacements about *any* stable equilibrium produce simple harmonic motion, which is why the harmonic oscillator is arguably the most important model system in all of physics, from classical mechanics to quantum field theory.

## 1. Simple Harmonic Motion (SHM)

A system executes **simple harmonic motion** when the restoring force (or torque) is proportional to the displacement from equilibrium and opposite in direction:
$$F = -kx$$

### Spring–mass system
For a mass $m$ on an ideal spring of constant $k$ on a frictionless surface, Newton's second law gives
$$m\frac{d^2x}{dt^2} = -kx \quad\Longrightarrow\quad \boxed{\frac{d^2x}{dt^2} + \omega_0^2 x = 0}, \qquad \omega_0 = \sqrt{\frac{k}{m}}$$

This is the **harmonic oscillator equation**. Its general solution is
$$x(t) = A\cos(\omega_0 t + \phi)$$
where:
- $A$ = **amplitude** (maximum displacement), set by initial conditions
- $\omega_0$ = **angular frequency** (rad/s), set by the system's physical properties
- $\phi$ = **phase constant**, set by initial conditions
- $\omega_0 t + \phi$ = **phase**

Equivalently $x(t) = C_1\cos\omega_0 t + C_2\sin\omega_0 t$ with $C_1 = x(0)$ and $C_2 = v(0)/\omega_0$; then $A = \sqrt{C_1^2 + C_2^2}$.

**Period and frequency:**
$$T = \frac{2\pi}{\omega_0} = 2\pi\sqrt{\frac{m}{k}}, \qquad f = \frac{1}{T} = \frac{1}{2\pi}\sqrt{\frac{k}{m}}$$

**The period does not depend on the amplitude.** This property (**isochronism**) is what makes harmonic oscillators useful as clocks.

### Velocity and acceleration
$$v(t) = -A\omega_0\sin(\omega_0 t + \phi), \qquad a(t) = -A\omega_0^2\cos(\omega_0 t + \phi) = -\omega_0^2 x$$
- Maximum speed $v_{\max} = A\omega_0$, at the equilibrium position ($x = 0$).
- Maximum acceleration $a_{\max} = A\omega_0^2$, at the turning points ($x = \pm A$), where the speed is zero.
- Velocity leads displacement by $90°$; acceleration is $180°$ out of phase with displacement.

Speed as a function of position: $v = \pm\omega_0\sqrt{A^2 - x^2}$.

### Energy in SHM
$$K = \tfrac12 mv^2 = \tfrac12 kA^2\sin^2(\omega_0 t + \phi), \qquad U = \tfrac12 kx^2 = \tfrac12 kA^2\cos^2(\omega_0 t + \phi)$$
$$\boxed{E = K + U = \tfrac12 kA^2 = \tfrac12 m v_{\max}^2}$$
Energy sloshes back and forth between kinetic and potential forms at twice the oscillation frequency, while the total remains constant. Averaged over a cycle, $\langle K\rangle = \langle U\rangle = E/2$.

### Connection to uniform circular motion
SHM is the projection onto a diameter of uniform circular motion with angular velocity $\omega_0$ on a circle of radius $A$. This is why the same $\omega$ appears in both, and why complex exponentials $x = \text{Re}[Ae^{i(\omega t + \phi)}]$ are such a convenient way to handle oscillations.

### Vertical spring
Hanging a mass on a vertical spring shifts the equilibrium position down by $\Delta L = mg/k$, but oscillations about the new equilibrium are still SHM with the same $\omega_0 = \sqrt{k/m}$. Gravity only shifts the equilibrium.

### Springs in combination
- **Series:** $\frac{1}{k_{\text{eff}}} = \frac{1}{k_1} + \frac{1}{k_2}$ (softer)
- **Parallel:** $k_{\text{eff}} = k_1 + k_2$ (stiffer)
- Cutting a spring in half doubles its spring constant.

### Worked example 1.1
**Problem:** A $0.5$ kg mass on a spring with $k = 200$ N/m is pulled $0.1$ m from equilibrium and released from rest. Find $\omega_0$, $T$, $v_{\max}$, $a_{\max}$, $E$, and the speed when $x = 0.06$ m.

**Solution:**
$\omega_0 = \sqrt{200/0.5} = 20$ rad/s; $T = 2\pi/20 \approx 0.314$ s; $f \approx 3.18$ Hz.
$v_{\max} = A\omega_0 = 0.1 \times 20 = 2$ m/s; $a_{\max} = A\omega_0^2 = 0.1 \times 400 = 40$ m/s².
$E = \frac12 (200)(0.01) = 1$ J.
At $x = 0.06$ m: $v = 20\sqrt{0.01 - 0.0036} = 20 \times 0.08 = 1.6$ m/s.
Equation of motion: $x(t) = 0.1\cos(20t)$ m.

## 2. Pendulums

### Simple pendulum
A point mass $m$ on a massless string of length $L$, displaced by angle $\theta$. The restoring torque is $\tau = -mgL\sin\theta$, and $I = mL^2$:
$$mL^2\ddot\theta = -mgL\sin\theta \Rightarrow \ddot\theta + \frac{g}{L}\sin\theta = 0$$
This equation is **nonlinear**. For small angles, $\sin\theta \approx \theta$ (in radians), giving SHM:
$$\ddot\theta + \frac{g}{L}\theta = 0, \qquad \boxed{T = 2\pi\sqrt{\frac{L}{g}}}$$

The period is independent of the mass and (for small amplitudes) of the amplitude. Galileo reportedly noticed this while watching a swinging chandelier in the Pisa cathedral, timing it with his pulse. A pendulum of length about 0.994 m has a period of 2 s (a "seconds pendulum", each swing taking 1 s).

**Small-angle accuracy:** the small-angle approximation is good to 0.2% at $10°$ and 1.7% at $30°$. The exact period, as a series in amplitude $\theta_0$:
$$T = 2\pi\sqrt{\frac{L}{g}}\left(1 + \frac{1}{16}\theta_0^2 + \frac{11}{3072}\theta_0^4 + \cdots\right)$$
Large-amplitude pendulums are slower; at $\theta_0 = 90°$, $T$ is about 18% longer than the small-angle value.

**Measuring $g$:** rearranging, $g = 4\pi^2 L/T^2$. Pendulums were the standard method for measuring local gravity for centuries.

### Physical (compound) pendulum
A rigid body of mass $m$ swinging about a pivot a distance $d$ from its center of mass, with moment of inertia $I$ about the pivot:
$$T = 2\pi\sqrt{\frac{I}{mgd}}$$
Example: a uniform rod of length $L$ pivoted at one end: $I = \frac13 mL^2$, $d = L/2$, so $T = 2\pi\sqrt{\frac{2L}{3g}}$ — equivalent to a simple pendulum of length $2L/3$. This explains why your legs swing at a natural walking rhythm, and why animals with longer legs walk with slower strides.

### Torsion pendulum
A disk suspended by a wire twisted by angle $\theta$ experiences restoring torque $\tau = -\kappa\theta$: $T = 2\pi\sqrt{I/\kappa}$. Used in mechanical watches (balance wheel with a hairspring) and in the Cavendish experiment.

## 3. Damped Oscillations

Real oscillators lose energy to friction or drag. For a damping force proportional to velocity, $F_d = -bv$:
$$m\ddot x + b\dot x + kx = 0 \quad\Longrightarrow\quad \ddot x + 2\gamma\dot x + \omega_0^2 x = 0, \qquad \gamma = \frac{b}{2m}$$

Trying $x = e^{st}$ gives $s^2 + 2\gamma s + \omega_0^2 = 0$, so $s = -\gamma \pm\sqrt{\gamma^2 - \omega_0^2}$. Three regimes:

**1. Underdamped ($\gamma < \omega_0$):** oscillation with exponentially decaying amplitude
$$x(t) = A_0 e^{-\gamma t}\cos(\omega_d t + \phi), \qquad \omega_d = \sqrt{\omega_0^2 - \gamma^2}$$
The damped frequency $\omega_d$ is slightly lower than $\omega_0$. Energy decays as $E \propto e^{-2\gamma t}$.

**2. Critically damped ($\gamma = \omega_0$):** returns to equilibrium as fast as possible without oscillating:
$$x(t) = (C_1 + C_2t)e^{-\omega_0 t}$$
Used in car suspensions (approximately), door closers, and analog meter needles.

**3. Overdamped ($\gamma > \omega_0$):** returns slowly without oscillating, as a sum of two decaying exponentials. Like a pendulum in honey.

### Quality factor
The **quality factor** $Q$ measures how lightly damped an oscillator is:
$$Q = \frac{\omega_0}{2\gamma} = 2\pi\frac{\text{energy stored}}{\text{energy lost per cycle}}$$
(the second form holds for $Q \gg 1$). Roughly, $Q/\pi$ is the number of oscillations for the amplitude to fall by a factor of $e$.

| Oscillator | Typical $Q$ |
|---|---|
| Car shock absorber | ~0.5 (near critical) |
| Guitar string | ~$10^3$ |
| Tuning fork | ~$10^3$–$10^4$ |
| Quartz crystal in a watch | ~$10^4$–$10^6$ |
| Superconducting microwave cavity | ~$10^{10}$ |
| Optical atomic clock transition | ~$10^{17}$ |

## 4. Driven Oscillations and Resonance

Apply a sinusoidal driving force $F_0\cos\omega t$:
$$m\ddot x + b\dot x + kx = F_0\cos\omega t$$

After transients die away (in a time ~$1/\gamma$), the system oscillates at the **driving frequency** $\omega$ (not its natural frequency) with steady-state amplitude
$$\boxed{A(\omega) = \frac{F_0/m}{\sqrt{(\omega_0^2 - \omega^2)^2 + 4\gamma^2\omega^2}}}$$
and phase lag
$$\tan\delta = \frac{2\gamma\omega}{\omega_0^2 - \omega^2}$$

**Resonance:** the amplitude is largest when the driving frequency is close to the natural frequency. For light damping, the peak occurs at $\omega_r = \sqrt{\omega_0^2 - 2\gamma^2} \approx \omega_0$ with height $A_{\max} \approx \frac{F_0}{2m\gamma\omega_0} = \frac{QF_0}{k}$ — that is, $Q$ times the static displacement.

Phase behavior:
- $\omega \ll \omega_0$: the mass follows the force in phase ($\delta \approx 0$); amplitude ≈ $F_0/k$.
- $\omega = \omega_0$: displacement lags force by exactly $90°$; velocity is in phase with force, so power transfer is maximal.
- $\omega \gg \omega_0$: displacement is $180°$ out of phase; amplitude falls as $1/\omega^2$.

**Resonance width:** the full width of the power resonance curve at half maximum is $\Delta\omega \approx 2\gamma = \omega_0/Q$. High-$Q$ systems have sharp, tall resonances — essential for radio tuning and frequency standards.

### Examples of resonance
- **Pushing a child on a swing** at its natural frequency.
- **Tuning a radio:** an LC circuit's resonance selects one station's frequency.
- **Musical instruments:** strings, air columns and soundboards resonate at specific frequencies.
- **Tacoma Narrows Bridge collapse (1940):** often cited as simple resonance, but more accurately caused by aeroelastic flutter — a self-excited oscillation in which the wind fed energy into a twisting mode. Still, it illustrates the danger of structural oscillations.
- **Millennium Bridge, London (2000):** pedestrians unconsciously synchronized their steps with the bridge's lateral sway, a feedback effect; dampers were installed.
- **Soldiers break step** when crossing bridges to avoid driving resonances.
- **MRI and NMR:** nuclear spins absorb radio-frequency energy at their Larmor resonance.
- **Microwave ovens** heat food at 2.45 GHz; this is not a sharp molecular resonance of water but a frequency at which water absorbs efficiently via dielectric loss while still penetrating centimeters into food.
- **Earthquake engineering:** buildings are designed so their natural frequencies avoid the dominant frequencies of ground shaking; tuned mass dampers (e.g. the 660-tonne pendulum in Taipei 101) counteract sway.

## 5. Coupled Oscillators and Normal Modes

Two identical masses $m$, each attached to a wall by a spring $k$ and to each other by a coupling spring $k'$:
$$m\ddot x_1 = -kx_1 - k'(x_1 - x_2), \qquad m\ddot x_2 = -kx_2 - k'(x_2 - x_1)$$

Adding and subtracting the equations decouples them into **normal modes**:
- **Symmetric mode** ($x_1 = x_2$, masses move together): coupling spring never stretched, $\omega_1 = \sqrt{k/m}$.
- **Antisymmetric mode** ($x_1 = -x_2$, masses move oppositely): $\omega_2 = \sqrt{(k + 2k')/m}$.

Any motion is a superposition of normal modes. If one mass is displaced initially, energy beats back and forth between the two masses at the difference frequency $\omega_2 - \omega_1$ — a phenomenon visible in two pendulums connected by a weak spring (or Wilberforce pendulums).

**Generalization:** a system with $N$ degrees of freedom near equilibrium has $N$ normal modes, found as eigenvectors of a matrix problem $(\mathbf K - \omega^2\mathbf M)\vec a = 0$. In the limit of infinitely many coupled oscillators we get **waves** on a string, and in a crystal lattice, quantized normal modes are **phonons**. Molecules have $3N - 6$ vibrational normal modes ($3N - 5$ if linear), which are measured by infrared and Raman spectroscopy.

## 6. Anharmonic Oscillations and Beyond

When the restoring force is not linear (large-amplitude pendulum, real molecular bonds), oscillations become **anharmonic**:
- The period depends on amplitude.
- Harmonics (multiples of the fundamental frequency) appear.
- For real molecular bonds (well approximated by the Morse potential), anharmonicity leads to bond dissociation and to thermal expansion of solids.
- Strongly driven nonlinear oscillators (e.g. a driven damped pendulum or the Duffing oscillator) can display **chaos**: extreme sensitivity to initial conditions.

**Quantum harmonic oscillator:** in quantum mechanics, the energy of a harmonic oscillator is quantized: $E_n = \hbar\omega(n + \frac12)$, with a nonzero ground-state (zero-point) energy $\frac12\hbar\omega$.

## 7. Summary

| System | Angular frequency / Period |
|---|---|
| Spring–mass | $\omega_0 = \sqrt{k/m}$, $T = 2\pi\sqrt{m/k}$ |
| Simple pendulum (small angle) | $\omega_0 = \sqrt{g/L}$, $T = 2\pi\sqrt{L/g}$ |
| Physical pendulum | $T = 2\pi\sqrt{I/(mgd)}$ |
| Torsion pendulum | $T = 2\pi\sqrt{I/\kappa}$ |
| LC circuit (electrical analog) | $\omega_0 = 1/\sqrt{LC}$ |
| Damped | $\omega_d = \sqrt{\omega_0^2 - \gamma^2}$, $\gamma = b/2m$ |
| Quality factor | $Q = \omega_0/(2\gamma)$ |
| Driven amplitude | $A = \frac{F_0/m}{\sqrt{(\omega_0^2-\omega^2)^2 + 4\gamma^2\omega^2}}$ |

**Key ideas:**
1. Linear restoring force ⇒ SHM with amplitude-independent period.
2. Total energy $\frac12 kA^2$ is constant without damping.
3. Damping reduces amplitude exponentially; $Q$ quantifies how slowly.
4. Driving near the natural frequency produces resonance with amplitude ~$Q$ times the static response.
5. Coupled systems oscillate in normal modes; infinitely many coupled oscillators make waves.
