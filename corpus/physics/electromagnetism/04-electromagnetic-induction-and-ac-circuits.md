---
title: Electromagnetic Induction, Inductance and AC Circuits
field: Physics
subfield: Electromagnetism
level: high-school to undergraduate
keywords: [magnetic flux, Faraday's law, Lenz's law, motional EMF, eddy currents, generator, self-inductance, mutual inductance, RL circuit, magnetic energy density, LC oscillation, alternating current, RMS, reactance, impedance, RLC resonance, power factor, transformer]
---

# Electromagnetic Induction, Inductance and AC Circuits

Ørsted showed that currents create magnetic fields. Michael Faraday asked the reverse question: can magnetic fields create currents? In 1831 he found the answer: yes — but only when the magnetic field **changes**. This discovery of **electromagnetic induction** made possible electric generators, transformers, and the entire electrical power grid, as well as induction cooktops, wireless charging, electric guitars and credit-card readers.

## 1. Magnetic Flux

The **magnetic flux** through a surface is
$$\Phi_B = \int\vec B\cdot d\vec A, \qquad \Phi_B = BA\cos\theta \;\text{(uniform field, flat surface)}$$
SI unit: the **weber** (Wb = T·m²).

Flux can change by changing $B$, changing the area $A$, or changing the angle $\theta$ between $\vec B$ and the surface normal.

## 2. Faraday's Law

> The induced EMF in a closed loop equals the negative rate of change of magnetic flux through it.
$$\boxed{\mathcal E = -\frac{d\Phi_B}{dt}} \qquad (\text{for } N \text{ turns: } \mathcal E = -N\frac{d\Phi_B}{dt})$$

In terms of fields, a changing magnetic field produces a **circulating electric field**:
$$\oint\vec E\cdot d\vec l = -\frac{d}{dt}\int\vec B\cdot d\vec A, \qquad \nabla\times\vec E = -\frac{\partial\vec B}{\partial t}$$
This induced electric field is **non-conservative**: its line integral around a closed loop is not zero, so it cannot be described by a scalar potential alone. It exists even with no wire present.

### Lenz's law
The minus sign in Faraday's law is **Lenz's law** (1834):
> The induced current flows in a direction such that its magnetic field opposes the *change* in flux that produced it.

Lenz's law is a consequence of energy conservation. If the induced current reinforced the change, it would increase the flux further, producing still more current — a runaway creation of energy from nothing.

**Examples:**
- Pushing a magnet's north pole toward a coil induces a current that makes the near face of the coil a north pole, repelling the magnet. You must do work to push the magnet in; that work becomes electrical energy.
- A magnet dropped through a copper pipe falls remarkably slowly: eddy currents induced in the pipe oppose its motion.
- **Jumping ring:** an aluminum ring on an iron core launches upward when AC is switched on in the coil below.

### Worked example 2.1
A 200-turn coil of area 0.01 m² sits perpendicular to a magnetic field that drops uniformly from 0.5 T to 0 in 0.1 s. Induced EMF: $\mathcal E = N\frac{\Delta\Phi}{\Delta t} = 200\times\frac{0.5\times0.01}{0.1} = 10$ V. If the coil's resistance is 5 Ω, the induced current is 2 A.

## 3. Motional EMF

A conducting rod of length $L$ moving with velocity $v$ perpendicular to a uniform field $B$: the free charges in the rod feel a magnetic force $qvB$ along the rod, separating charges until an electric field balances it. The resulting EMF is
$$\boxed{\mathcal E = BLv}$$
If the rod slides on rails forming a circuit with resistance $R$, current $I = BLv/R$ flows, and the rod experiences a retarding force $F = ILB = \frac{B^2L^2v}{R}$ (Lenz's law). Pulling the rod at constant speed requires power $Fv = \frac{B^2L^2v^2}{R} = I^2R$ — mechanical power is converted to electrical power and then to heat. Energy is conserved exactly.

**Example:** a jet with 60 m wingspan flying at 250 m/s through Earth's vertical field component of 50 μT develops $\mathcal E = 50\times10^{-6}\times60\times250 = 0.75$ V between wingtips.

### Electric generators
A coil of $N$ turns and area $A$ rotating at angular velocity $\omega$ in a uniform field $B$ has flux $\Phi = BA\cos\omega t$, so
$$\mathcal E = NBA\omega\sin\omega t$$
— a sinusoidal **alternating** EMF with peak value $\mathcal E_0 = NBA\omega$. Power plants (thermal, hydro, wind, nuclear) all use this principle, turning a rotor with a turbine. Grid frequency is 50 Hz in most of the world (Europe, Asia, Africa, Australia) and 60 Hz in the Americas (and parts of Japan, Korea, Taiwan, Saudi Arabia).

A generator is a motor run in reverse. Electric and hybrid cars use **regenerative braking**: the drive motor acts as a generator, converting kinetic energy back into stored electrical energy.

### Eddy currents
Changing flux through a bulk conductor induces swirling **eddy currents**. They dissipate energy as heat and oppose motion.
- **Useful:** induction cooktops (alternating field induces eddy currents in a ferromagnetic pan), induction furnaces, eddy-current brakes in trains and roller coasters (no wear, smooth), metal detectors, coin sorters in vending machines, and non-destructive crack testing.
- **Harmful:** energy losses in transformer and motor cores, reduced by building cores from thin insulated **laminations** or ferrite materials, which break up eddy-current paths.

## 4. Inductance

### Self-inductance
A changing current in a coil changes its own magnetic flux, inducing an EMF that opposes the change in current. The flux linkage is proportional to the current: $N\Phi_B = LI$, defining the **self-inductance** $L$:
$$\boxed{\mathcal E_L = -L\frac{dI}{dt}}$$
SI unit: the **henry** (H = V·s/A = Wb/A).

An inductor resists *changes* in current — it is the electrical analog of mass (inertia), just as a capacitor is analogous to a spring.

**Ideal solenoid** ($N$ turns, length $\ell$, area $A$): $B = \mu_0\frac N\ell I$, $\Phi = BA$, so
$$L = \frac{\mu_0N^2A}{\ell} = \mu_0n^2A\ell$$
An iron core multiplies $L$ by $\mu_r$.

**Danger of interrupting inductive currents:** opening a switch quickly makes $dI/dt$ huge, producing a large voltage spike that can cause arcing (sparks at switches). Car ignition coils exploit this deliberately to generate ~20–40 kV for spark plugs from a 12 V battery. Electronics use "flyback" diodes across relay coils to protect transistors.

### Mutual inductance
A changing current in coil 1 induces an EMF in a nearby coil 2:
$$\mathcal E_2 = -M\frac{dI_1}{dt}$$
$M$ (henries) depends on geometry and is symmetric ($M_{12} = M_{21}$). Basis of transformers, wireless phone chargers (Qi standard), RFID tags, electric toothbrush chargers, and pacemaker charging through the skin.

### Energy stored in an inductor
Building up current against the back-EMF requires work $dW = LI\,dI$:
$$\boxed{U_L = \tfrac12LI^2}$$
The energy resides in the magnetic field with **energy density**
$$\boxed{u_B = \frac{B^2}{2\mu_0}}$$
(compare $u_E = \frac12\varepsilon_0E^2$). A 3 T MRI magnet stores about 3.6 MJ/m³ in its bore field.

## 5. RL Circuits

**Current growth:** connecting an inductor $L$ and resistor $R$ in series to EMF $\mathcal E$:
$$\mathcal E - IR - L\frac{dI}{dt} = 0 \Rightarrow I(t) = \frac{\mathcal E}{R}\left(1 - e^{-t/\tau}\right), \qquad \tau = \frac LR$$
**Current decay:** removing the source (with a closed path): $I(t) = I_0e^{-t/\tau}$.

At $t = 0$ an inductor behaves like an open circuit (current cannot change instantly); after a long time in DC it behaves like a plain wire.

## 6. LC Oscillations

A charged capacitor connected to an inductor exchanges energy back and forth between electric and magnetic fields:
$$L\frac{d^2q}{dt^2} + \frac qC = 0 \Rightarrow q(t) = Q_0\cos(\omega_0t + \phi), \qquad \boxed{\omega_0 = \frac{1}{\sqrt{LC}}}$$
This is exactly the harmonic oscillator, with the correspondence:

| Mechanical | Electrical |
|---|---|
| Displacement $x$ | Charge $q$ |
| Velocity $v$ | Current $I$ |
| Mass $m$ | Inductance $L$ |
| Spring constant $k$ | $1/C$ |
| Damping $b$ | Resistance $R$ |
| Kinetic energy $\frac12mv^2$ | Magnetic energy $\frac12LI^2$ |
| Potential energy $\frac12kx^2$ | Electric energy $\frac{q^2}{2C}$ |

With resistance (RLC), oscillations decay with $\gamma = R/(2L)$ — exactly like a damped mechanical oscillator. LC circuits are the tuning elements of radios and the heart of many oscillators.

## 7. Alternating Current

### RMS values
For a sinusoidal voltage $v(t) = V_0\sin\omega t$, the average is zero but the average power is not. The **root-mean-square (rms)** value is the equivalent DC value delivering the same average power to a resistor:
$$V_{\text{rms}} = \frac{V_0}{\sqrt2}, \qquad I_{\text{rms}} = \frac{I_0}{\sqrt2}$$
Household "230 V" (Europe) or "120 V" (North America) are rms values; the peak voltages are about 325 V and 170 V respectively.

### Circuit elements in AC

| Element | Reactance/Impedance | Phase of current vs. voltage | Frequency behavior |
|---|---|---|---|
| Resistor | $R$ | In phase | Independent of $f$ |
| Inductor | $X_L = \omega L$ | Current **lags** voltage by 90° | Blocks high frequencies |
| Capacitor | $X_C = \dfrac{1}{\omega C}$ | Current **leads** voltage by 90° | Blocks low frequencies (and DC) |

Mnemonic: **"ELI the ICE man"** — in an inductor (L), EMF (E) leads current (I); in a capacitor (C), current (I) leads EMF (E).

Ideal inductors and capacitors dissipate no average power; energy is stored and returned each cycle.

### Series RLC circuit and impedance
For R, L and C in series driven by $V_0\sin\omega t$, phasor analysis gives the **impedance**
$$\boxed{Z = \sqrt{R^2 + (X_L - X_C)^2}}, \qquad I_0 = \frac{V_0}{Z}, \qquad \tan\phi = \frac{X_L - X_C}{R}$$
With complex numbers: $Z = R + i\omega L + \frac{1}{i\omega C} = R + i\left(\omega L - \frac{1}{\omega C}\right)$, and Ohm's law $\tilde V = \tilde I Z$ holds for complex amplitudes.

### Resonance
Current is maximal when $X_L = X_C$:
$$\boxed{\omega_0 = \frac{1}{\sqrt{LC}}, \qquad f_0 = \frac{1}{2\pi\sqrt{LC}}}$$
At resonance $Z = R$ (minimum), current is in phase with voltage, and the voltages across L and C — each possibly much larger than the source voltage — cancel. The sharpness is set by the quality factor $Q = \frac{\omega_0L}{R} = \frac1R\sqrt{\frac LC}$; the bandwidth is $\Delta\omega = \omega_0/Q$.

**Radio tuning:** turning the dial varies $C$, shifting $f_0$ to match one station's carrier frequency while rejecting others. For an FM station at 100 MHz with $L = 0.25$ μH: $C = \frac{1}{(2\pi f_0)^2L} \approx 10$ pF.

### AC power and power factor
$$P_{\text{avg}} = V_{\text{rms}}I_{\text{rms}}\cos\phi$$
$\cos\phi$ is the **power factor**. Only the resistive part dissipates power. Industrial loads with large motors (inductive) have low power factors, drawing extra current that causes line losses without doing useful work; utilities require **power-factor correction** with capacitor banks.

### Worked example 7.1
**Problem:** A series RLC circuit has $R = 100$ Ω, $L = 0.5$ H, $C = 10$ μF, driven at 230 V rms, 50 Hz. Find $Z$, $I_{\text{rms}}$, phase angle and average power.

**Solution:** $\omega = 2\pi\times50 = 314.2$ rad/s.
$X_L = 314.2\times0.5 = 157.1$ Ω; $X_C = \frac{1}{314.2\times10^{-5}} = 318.3$ Ω.
$Z = \sqrt{100^2 + (157.1 - 318.3)^2} = \sqrt{10\,000 + 25\,985} \approx 189.7$ Ω.
$I_{\text{rms}} = 230/189.7 \approx 1.21$ A.
$\tan\phi = -161.2/100 \Rightarrow \phi \approx -58.2°$ (capacitive: current leads voltage).
$P = I_{\text{rms}}^2R = 1.47\times100 \approx 147$ W (also $= 230\times1.21\times\cos58.2° \approx 147$ W).
Resonant frequency: $f_0 = \frac{1}{2\pi\sqrt{0.5\times10^{-5}}} \approx 71.2$ Hz.

## 8. Transformers

Two coils wound on a common iron core. An alternating current in the primary creates a changing flux that links the secondary. For an ideal transformer (no flux leakage or losses):
$$\boxed{\frac{V_s}{V_p} = \frac{N_s}{N_p}}, \qquad V_pI_p = V_sI_s \Rightarrow \frac{I_s}{I_p} = \frac{N_p}{N_s}$$
- **Step-up** ($N_s > N_p$): higher voltage, lower current — for long-distance transmission.
- **Step-down** ($N_s < N_p$): for distribution to homes and for device chargers.

Transformers **only work with AC** (a steady DC current produces no changing flux). This was a decisive factor in the "War of the Currents" in the late 1880s–1890s: Nikola Tesla and George Westinghouse's AC system defeated Thomas Edison's DC system for power distribution. (Today, high-voltage DC links are used for very long or undersea lines, using power electronics for conversion.)

Real transformers reach 95–99.7% efficiency; losses come from winding resistance (copper losses), eddy currents and hysteresis (core losses), and flux leakage.

A typical grid: generator (~10–25 kV) → step-up to 110–765 kV for transmission → substations step down to ~10–35 kV → local transformers step down to 230/400 V (or 120/240 V).

**Impedance transformation:** a transformer with turns ratio $n = N_p/N_s$ makes a load $R_L$ appear as $n^2R_L$ to the source — used for impedance matching in audio and RF.

## 9. Summary

| Concept | Formula |
|---|---|
| Magnetic flux | $\Phi_B = \int\vec B\cdot d\vec A$ |
| Faraday's law | $\mathcal E = -N\,d\Phi_B/dt$ |
| Motional EMF | $\mathcal E = BLv$ |
| Generator | $\mathcal E = NBA\omega\sin\omega t$ |
| Self-inductance | $\mathcal E = -L\,dI/dt$; solenoid $L = \mu_0N^2A/\ell$ |
| Inductor energy | $U = \frac12LI^2$; $u_B = B^2/2\mu_0$ |
| RL time constant | $\tau = L/R$ |
| LC frequency | $\omega_0 = 1/\sqrt{LC}$ |
| RMS | $V_{\text{rms}} = V_0/\sqrt2$ |
| Reactances | $X_L = \omega L$, $X_C = 1/(\omega C)$ |
| Impedance | $Z = \sqrt{R^2 + (X_L - X_C)^2}$ |
| AC power | $P = V_{\text{rms}}I_{\text{rms}}\cos\phi$ |
| Transformer | $V_s/V_p = N_s/N_p$ |
