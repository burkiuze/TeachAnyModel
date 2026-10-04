---
title: Mechanical Waves and Sound
field: Physics
subfield: Waves and Optics
level: high-school to undergraduate
keywords: [wave, transverse, longitudinal, wavelength, frequency, wave speed, wave equation, superposition, interference, standing waves, harmonics, resonance, sound, decibel, Doppler effect, beats, shock wave, Mach number, ultrasound, acoustics]
---

# Mechanical Waves and Sound

A **wave** is a disturbance that propagates through space and time, transporting **energy and momentum without transporting matter**. When a stadium crowd does "the wave", each person merely stands and sits, yet the pattern sweeps around the stadium. Mechanical waves (sound, water waves, seismic waves, waves on strings) require a medium; electromagnetic waves do not. Quantum mechanics reveals that matter itself has wave properties.

## 1. Types of Waves

- **Transverse waves:** the medium oscillates perpendicular to the direction of propagation (waves on a string, S-waves in earthquakes, electromagnetic waves).
- **Longitudinal waves:** the medium oscillates parallel to the direction of propagation, as compressions and rarefactions (sound in air, P-waves in earthquakes, a pushed Slinky).
- **Surface waves:** combinations, like water waves where particles move in roughly circular paths.

Fluids (liquids and gases) cannot support shear, so they transmit only longitudinal mechanical waves. This is how seismologists discovered Earth's liquid outer core: **S-waves** (transverse) do not pass through it, creating an "S-wave shadow zone".

## 2. Describing Waves

A sinusoidal (harmonic) traveling wave moving in the $+x$ direction:
$$y(x, t) = A\sin(kx - \omega t + \phi)$$

| Quantity | Symbol | Definition |
|---|---|---|
| Amplitude | $A$ | Maximum displacement |
| Wavelength | $\lambda$ | Distance between successive crests |
| Wave number | $k = 2\pi/\lambda$ | rad/m |
| Period | $T$ | Time for one oscillation at a point |
| Frequency | $f = 1/T$ | Hz |
| Angular frequency | $\omega = 2\pi f$ | rad/s |
| Wave speed | $v = \lambda f = \omega/k$ | Speed of the pattern (phase velocity) |

A wave moving in the $-x$ direction is $y = A\sin(kx + \omega t)$. Any function of the form $f(x - vt)$ is a wave traveling at speed $v$ without changing shape.

**Important:** the wave speed is determined by the **medium**; the frequency is determined by the **source**. When a wave passes from one medium to another, its frequency stays the same while its speed and wavelength change.

### The wave equation
All such waves satisfy the linear **wave equation**:
$$\boxed{\frac{\partial^2y}{\partial x^2} = \frac{1}{v^2}\frac{\partial^2y}{\partial t^2}}$$

**Derivation for a string** with tension $T$ and linear mass density $\mu$: a small segment $dx$ experiences a net vertical force $T\frac{\partial^2y}{\partial x^2}dx$ (from the difference in slope at its ends). Newton's second law: $T\frac{\partial^2y}{\partial x^2}dx = \mu\,dx\frac{\partial^2y}{\partial t^2}$, so
$$v = \sqrt{\frac{T}{\mu}}$$

### Wave speeds in general
Wave speed $= \sqrt{\frac{\text{restoring (elastic) property}}{\text{inertial property}}}$:
- String: $v = \sqrt{T/\mu}$
- Sound in a fluid: $v = \sqrt{B/\rho}$ ($B$ = bulk modulus)
- Sound in a solid rod: $v = \sqrt{Y/\rho}$ ($Y$ = Young's modulus)
- Sound in an ideal gas: $v = \sqrt{\gamma RT/M}$
- Deep-water surface waves: $v = \sqrt{g\lambda/(2\pi)}$ (dispersive: longer waves travel faster)
- Shallow-water waves (depth $h \ll \lambda$): $v = \sqrt{gh}$ — why tsunamis travel at ~700 km/h across deep ocean ($h \approx 4$ km) and slow down, growing taller, as they reach shore.

### Energy transport
The power carried by a sinusoidal wave on a string is
$$P = \tfrac12\mu v\omega^2A^2$$
Wave power is proportional to the **square of the amplitude** and the **square of the frequency** — a general result for waves.

## 3. Superposition and Interference

For linear waves, the **principle of superposition** holds: when two or more waves overlap, the resulting displacement is the sum of the individual displacements. Afterwards, the waves continue unchanged.

**Interference** of two waves of equal amplitude and frequency with phase difference $\phi$:
$$y = 2A\cos\left(\frac\phi2\right)\sin\left(kx - \omega t + \frac\phi2\right)$$
- **Constructive interference:** $\phi = 0, 2\pi, 4\pi, \ldots$ (path difference $= m\lambda$) → amplitude $2A$.
- **Destructive interference:** $\phi = \pi, 3\pi, \ldots$ (path difference $= (m + \frac12)\lambda$) → amplitude 0.

**Noise-canceling headphones** record ambient sound and emit an inverted (antiphase) copy, canceling it by destructive interference — most effective for low-frequency steady noise like engine hum.

### Reflection
- A wave reflecting from a **fixed end** (or a denser medium) is inverted (phase shift of $\pi$).
- A wave reflecting from a **free end** (or a less dense medium) is not inverted.
- At a boundary between media, part of the wave is transmitted and part reflected.

## 4. Standing Waves and Resonance

Two identical waves traveling in opposite directions superpose into a **standing wave**:
$$y = 2A\sin(kx)\cos(\omega t)$$
Points with $\sin kx = 0$ never move (**nodes**), spaced $\lambda/2$ apart; points midway oscillate with maximum amplitude (**antinodes**). Energy does not propagate.

### String fixed at both ends (guitar, violin, piano)
Nodes at both ends require $L = n\frac{\lambda}{2}$:
$$\boxed{f_n = \frac{nv}{2L} = \frac{n}{2L}\sqrt{\frac{T}{\mu}}, \qquad n = 1, 2, 3, \ldots}$$
$f_1$ is the **fundamental**; $f_n = nf_1$ are the **harmonics** (overtones). Musicians change pitch by changing length (fretting), tension (tuning pegs), or mass density (thicker strings for lower notes).

### Air columns (wind instruments, organ pipes)
- **Open at both ends** (flute): antinodes at both ends; $f_n = \frac{nv}{2L}$, all harmonics.
- **Closed at one end** (clarinet approximately, a bottle): node at the closed end, antinode at the open end; $L = n\frac{\lambda}{4}$ with $n$ odd:
$$f_n = \frac{nv}{4L}, \qquad n = 1, 3, 5, \ldots$$
Only odd harmonics; the fundamental is an octave lower than an open pipe of the same length. The human ear canal (~2.5 cm, closed by the eardrum) resonates near 3.4 kHz, where our hearing is most sensitive.

### Timbre
The same note on a violin and a flute sounds different because of their different mixtures of harmonics (**timbre**). Fourier's theorem states that any periodic waveform can be expressed as a sum of sinusoids at the fundamental frequency and its harmonics.

### Worked example 4.1
A guitar string 0.65 m long has a fundamental of 110 Hz (A2). Wave speed: $v = 2Lf_1 = 2\times0.65\times110 = 143$ m/s. If the linear density is $\mu = 5\times10^{-3}$ kg/m, the tension is $T = \mu v^2 = 5\times10^{-3}\times143^2 \approx 102$ N. Pressing the string at the 12th fret (half the length) doubles the frequency to 220 Hz — one octave higher.

## 5. Sound

Sound is a longitudinal pressure wave. Human hearing spans about **20 Hz to 20 kHz** (the upper limit falls with age). Below 20 Hz is **infrasound** (elephants, whales, earthquakes, volcanoes); above 20 kHz is **ultrasound** (bats, dolphins, medical imaging).

### Speed of sound

| Medium | Speed (m/s) |
|---|---|
| Air, 0 °C | 331 |
| Air, 20 °C | 343 |
| Helium, 20 °C | 1007 |
| Water, 25 °C | 1497 |
| Seawater | ~1530 |
| Human soft tissue | ~1540 |
| Bone | ~3000–4000 |
| Steel | ~5900 (longitudinal, bulk) |
| Diamond | ~12 000 |

In air, $v \approx 331 + 0.6T_C$ m/s. Sound speed depends on temperature but not on pressure (for an ideal gas). Breathing helium raises vocal-tract resonance frequencies (though not the vocal cord frequency), making the voice sound high-pitched.

**Lightning distance rule:** sound travels about 1 km in 3 seconds; count the seconds between flash and thunder and divide by 3 for kilometers.

### Intensity and decibels
Intensity $I$ (W/m²) is power per unit area. The ear responds roughly logarithmically, so we use the **sound intensity level**:
$$\boxed{\beta = 10\log_{10}\frac{I}{I_0}} \;\text{dB}, \qquad I_0 = 10^{-12}\text{ W/m}^2 \;(\text{threshold of hearing})$$

| Sound | Level (dB) | Intensity (W/m²) |
|---|---|---|
| Threshold of hearing | 0 | $10^{-12}$ |
| Rustling leaves | 20 | $10^{-10}$ |
| Quiet library | 40 | $10^{-8}$ |
| Normal conversation | 60 | $10^{-6}$ |
| Busy traffic | 80 | $10^{-4}$ |
| Rock concert, chainsaw | 110 | $10^{-1}$ |
| Threshold of pain | 120–130 | 1–10 |
| Jet engine at 30 m | 150 | $10^3$ |

Rules of thumb: +10 dB = 10× intensity (perceived as roughly "twice as loud"); +3 dB ≈ 2× intensity; doubling distance from a point source reduces the level by about 6 dB. Prolonged exposure above ~85 dB risks permanent hearing damage (destruction of hair cells in the cochlea).

**Adding sources:** two 80 dB machines together produce 83 dB, not 160 dB.

## 6. Beats

Two sounds with slightly different frequencies $f_1$ and $f_2$ interfere alternately constructively and destructively, producing a periodic swelling in loudness:
$$f_{\text{beat}} = |f_1 - f_2|$$
Musicians tune instruments by adjusting until the beats disappear. Two tuning forks at 440 Hz and 444 Hz produce 4 beats per second.

## 7. The Doppler Effect

When a source and observer move relative to the medium, the observed frequency differs from the emitted frequency (Christian Doppler, 1842):
$$\boxed{f' = f\,\frac{v \pm v_o}{v \mp v_s}}$$
Use the **upper signs when source and observer approach** each other (frequency increases) and lower signs when they recede. $v$ is the wave speed in the medium; $v_o$ and $v_s$ are the observer's and source's speeds relative to the medium.

The familiar drop in pitch as an ambulance passes is the Doppler effect.

**Worked example 7.1:** an ambulance siren at 700 Hz approaches a stationary listener at 30 m/s ($v = 343$ m/s): $f' = 700\times\frac{343}{343 - 30} \approx 767$ Hz. After passing: $f' = 700\times\frac{343}{373} \approx 644$ Hz.

**Applications:**
- **Doppler radar** for weather (measuring wind speeds in storms) and police speed guns.
- **Doppler ultrasound** measures blood flow speed and direction (and fetal heartbeats).
- **Astronomy:** the electromagnetic Doppler effect (which depends only on relative velocity, $f' = f\sqrt{\frac{1+\beta}{1-\beta}}$ for approach with $\beta = v/c$) reveals stellar motions, exoplanets (radial-velocity "wobble" method), binary stars, galaxy rotation, and the **redshift** of distant galaxies (cosmic expansion).
- **Bats and dolphins** use Doppler-shifted echoes to track prey.

### Shock waves and sonic booms
When a source moves faster than the wave speed ($v_s > v$), wavefronts pile up into a cone — a **shock wave**. The cone half-angle $\theta$ satisfies
$$\sin\theta = \frac{v}{v_s} = \frac{1}{M}$$
where $M = v_s/v$ is the **Mach number**. Supersonic aircraft drag a continuous sonic boom along the ground beneath them. The crack of a whip is a small sonic boom (the tip exceeds the speed of sound). Boat wakes are an analogous effect for water waves. **Cherenkov radiation** — the blue glow in nuclear reactor pools — is the optical analog: charged particles traveling faster than light's speed *in water* ($c/n$).

## 8. Acoustics and Ultrasound Applications

- **Echolocation and sonar:** measuring echo delay gives distance ($d = vt/2$). Submarines, fishing boats, and seafloor mapping use sonar.
- **Medical ultrasound** (typically 2–15 MHz): reflections from tissue boundaries form images. Higher frequency gives finer resolution (shorter wavelength) but less penetration. A coupling gel eliminates air gaps, since the huge **acoustic impedance** mismatch ($Z = \rho v$) between air and skin would reflect almost all the sound.
- **Lithotripsy:** focused shock waves shatter kidney stones without surgery.
- **Ultrasonic cleaning:** cavitation bubbles scrub surfaces.
- **Architectural acoustics:** reverberation time $T_{60} \approx 0.161\frac{V}{A_{\text{abs}}}$ (Sabine's formula, $V$ in m³, $A_{\text{abs}}$ in m² of equivalent absorption) — concert halls aim for ~1.8–2.2 s, lecture halls ~0.7–1 s.
- **Seismology:** P-waves (~6 km/s in crust) arrive before S-waves (~3.5 km/s); the delay between arrivals gives distance to the earthquake, and three stations triangulate the epicenter.

## 9. Group Velocity and Dispersion

When wave speed depends on frequency (**dispersion**), a wave packet's envelope travels at the **group velocity**
$$v_g = \frac{d\omega}{dk}$$
which can differ from the phase velocity $v_p = \omega/k$. Energy and information travel at the group velocity. Deep-water waves have $v_g = \frac12v_p$ — individual crests appear at the back of a group, move through it and vanish at the front. In quantum mechanics, a free particle's group velocity equals its classical velocity.

## 10. Summary

| Concept | Formula |
|---|---|
| Wave speed | $v = f\lambda = \omega/k$ |
| Traveling wave | $y = A\sin(kx - \omega t)$ |
| Wave equation | $\partial^2y/\partial x^2 = (1/v^2)\partial^2y/\partial t^2$ |
| String speed | $v = \sqrt{T/\mu}$ |
| Sound in gas | $v = \sqrt{\gamma RT/M}$ |
| String / open pipe harmonics | $f_n = nv/(2L)$ |
| Closed pipe harmonics | $f_n = nv/(4L)$, $n$ odd |
| Decibels | $\beta = 10\log_{10}(I/I_0)$ |
| Beats | $f_{\text{beat}} = \lvert f_1 - f_2\rvert$ |
| Doppler (sound) | $f' = f(v \pm v_o)/(v \mp v_s)$ |
| Mach cone | $\sin\theta = v/v_s$ |
| Group velocity | $v_g = d\omega/dk$ |
