---
title: Maxwell's Equations and Electromagnetic Waves
field: Physics
subfield: Electromagnetism
level: undergraduate
keywords: [Maxwell's equations, displacement current, wave equation, speed of light, electromagnetic wave, Poynting vector, intensity, radiation pressure, polarization, electromagnetic spectrum, divergence, curl, gauge, scalar potential, vector potential, Lorentz invariance]
---

# Maxwell's Equations and Electromagnetic Waves

Between 1861 and 1865 James Clerk Maxwell unified all known electric and magnetic phenomena into a single set of equations. In doing so he discovered that electric and magnetic fields can sustain each other as a wave traveling at a speed computed purely from electrical measurements — a speed that matched the measured speed of light. Maxwell concluded that **light is an electromagnetic wave**. This was the second great unification in physics (after Newton's) and one of the greatest intellectual achievements in history. Heinrich Hertz confirmed it experimentally in 1887 by generating and detecting radio waves.

## 1. Maxwell's Equations

### Integral form (in vacuum, with sources)

| Name | Equation | Physical meaning |
|---|---|---|
| Gauss's law | $\displaystyle\oint\vec E\cdot d\vec A = \frac{Q_{\text{enc}}}{\varepsilon_0}$ | Electric charges are sources/sinks of $\vec E$ |
| Gauss's law for magnetism | $\displaystyle\oint\vec B\cdot d\vec A = 0$ | No magnetic monopoles; $\vec B$ lines close on themselves |
| Faraday's law | $\displaystyle\oint\vec E\cdot d\vec l = -\frac{d\Phi_B}{dt}$ | Changing $\vec B$ creates circulating $\vec E$ |
| Ampère–Maxwell law | $\displaystyle\oint\vec B\cdot d\vec l = \mu_0I_{\text{enc}} + \mu_0\varepsilon_0\frac{d\Phi_E}{dt}$ | Currents and changing $\vec E$ create circulating $\vec B$ |

### Differential form
Using the divergence theorem and Stokes' theorem:
$$\boxed{\nabla\cdot\vec E = \frac{\rho}{\varepsilon_0}} \qquad \boxed{\nabla\cdot\vec B = 0}$$
$$\boxed{\nabla\times\vec E = -\frac{\partial\vec B}{\partial t}} \qquad \boxed{\nabla\times\vec B = \mu_0\vec J + \mu_0\varepsilon_0\frac{\partial\vec E}{\partial t}}$$

Together with the **Lorentz force law** $\vec F = q(\vec E + \vec v\times\vec B)$ and Newton's laws (or their relativistic versions), these equations describe all classical electromagnetic phenomena.

**Vector calculus reminders:**
- **Divergence** $\nabla\cdot\vec F$ measures the net outflow from a point (sources and sinks).
- **Curl** $\nabla\times\vec F$ measures circulation around a point.
- **Divergence theorem:** $\oint_S\vec F\cdot d\vec A = \int_V\nabla\cdot\vec F\,dV$.
- **Stokes' theorem:** $\oint_C\vec F\cdot d\vec l = \int_S(\nabla\times\vec F)\cdot d\vec A$.

### In matter
In materials, it is convenient to separate free charges and currents from bound ones using $\vec D = \varepsilon_0\vec E + \vec P$ and $\vec H = \vec B/\mu_0 - \vec M$:
$$\nabla\cdot\vec D = \rho_f, \quad \nabla\cdot\vec B = 0, \quad \nabla\times\vec E = -\frac{\partial\vec B}{\partial t}, \quad \nabla\times\vec H = \vec J_f + \frac{\partial\vec D}{\partial t}$$
For linear media, $\vec D = \varepsilon\vec E$ and $\vec B = \mu\vec H$.

## 2. The Displacement Current

Ampère's original law, $\oint\vec B\cdot d\vec l = \mu_0I_{\text{enc}}$, is inconsistent when currents change. Consider a capacitor being charged: an Amperian loop around the wire can bound a flat surface pierced by the wire (enclosing current $I$) or a bulging surface passing between the plates (enclosing no current). The two answers contradict each other.

Mathematically, taking the divergence of $\nabla\times\vec B = \mu_0\vec J$ gives $\nabla\cdot\vec J = 0$, which contradicts charge conservation $\nabla\cdot\vec J = -\partial\rho/\partial t$ whenever charge density changes.

Maxwell's fix was to add the **displacement current** term:
$$I_d = \varepsilon_0\frac{d\Phi_E}{dt}$$
Between the capacitor plates, the changing electric field produces a magnetic field exactly as if the conduction current continued through the gap. With this term, the equations are consistent with charge conservation. Crucially, it means **a changing electric field produces a magnetic field**, just as a changing magnetic field produces an electric field — the mutual generation that makes self-sustaining electromagnetic waves possible.

## 3. The Electromagnetic Wave Equation

In empty space ($\rho = 0$, $\vec J = 0$), take the curl of Faraday's law:
$$\nabla\times(\nabla\times\vec E) = -\frac{\partial}{\partial t}(\nabla\times\vec B) = -\mu_0\varepsilon_0\frac{\partial^2\vec E}{\partial t^2}$$
Using the identity $\nabla\times(\nabla\times\vec E) = \nabla(\nabla\cdot\vec E) - \nabla^2\vec E$ and $\nabla\cdot\vec E = 0$:
$$\boxed{\nabla^2\vec E = \mu_0\varepsilon_0\frac{\partial^2\vec E}{\partial t^2}}, \qquad \boxed{\nabla^2\vec B = \mu_0\varepsilon_0\frac{\partial^2\vec B}{\partial t^2}}$$
These are wave equations with propagation speed
$$\boxed{c = \frac{1}{\sqrt{\mu_0\varepsilon_0}}} = \frac{1}{\sqrt{(4\pi\times10^{-7})(8.854\times10^{-12})}} \approx 2.998\times10^8 \text{ m/s}$$

Maxwell wrote in 1862: "We can scarcely avoid the inference that light consists in the transverse undulations of the same medium which is the cause of electric and magnetic phenomena."

Since 1983, the meter has been defined by fixing the speed of light at exactly $c = 299\,792\,458$ m/s.

## 4. Plane Electromagnetic Waves

A sinusoidal plane wave traveling in the $+x$ direction:
$$\vec E = E_0\sin(kx - \omega t)\,\hat y, \qquad \vec B = B_0\sin(kx - \omega t)\,\hat z$$
with $\omega = ck$, $k = 2\pi/\lambda$, $c = f\lambda$.

### Properties
1. **Transverse:** both $\vec E$ and $\vec B$ are perpendicular to the direction of propagation (follows from $\nabla\cdot\vec E = \nabla\cdot\vec B = 0$).
2. **$\vec E\perp\vec B$**, and $\vec E\times\vec B$ points in the direction of propagation.
3. **In phase:** $\vec E$ and $\vec B$ reach maxima and zeros together.
4. **Amplitude ratio:** $E_0 = cB_0$. In SI units the magnetic field looks numerically tiny ($B = E/c$), but the electric and magnetic energy densities are equal.
5. **No medium required:** unlike sound, EM waves travel through vacuum. The 1887 Michelson–Morley experiment found no evidence of a "luminiferous aether", a puzzle resolved by Einstein's special relativity (1905).
6. All EM waves travel at $c$ in vacuum regardless of frequency, and regardless of the motion of the source or observer.

### In a medium
In a linear dielectric medium, the speed is $v = \frac{1}{\sqrt{\mu\varepsilon}} = \frac cn$, where the **refractive index** is $n = \sqrt{\varepsilon_r\mu_r} \approx \sqrt{\varepsilon_r}$ for non-magnetic materials (at the relevant frequency). Frequency dependence of $n$ (**dispersion**) separates white light into colors in a prism.

## 5. Energy and Momentum of Electromagnetic Waves

### Energy density
$$u = \tfrac12\varepsilon_0E^2 + \frac{B^2}{2\mu_0} = \varepsilon_0E^2 \quad (\text{since the two terms are equal for a wave})$$

### The Poynting vector
The flow of electromagnetic energy (power per unit area, W/m²) is given by the **Poynting vector** (John Henry Poynting, 1884):
$$\boxed{\vec S = \frac{1}{\mu_0}\vec E\times\vec B}$$
It points in the direction of energy flow.

**Poynting's theorem** expresses energy conservation for fields:
$$\frac{\partial u}{\partial t} + \nabla\cdot\vec S = -\vec J\cdot\vec E$$
(the rate of decrease of field energy equals the energy flowing out plus the work done on charges).

A remarkable application: in a DC circuit, energy flows from the battery to the resistor not *through* the wire but through the space around it, carried by the fields; the Poynting vector points into the resistor from the surrounding space.

### Intensity
The time-averaged magnitude of the Poynting vector is the **intensity**:
$$\boxed{I = \langle S\rangle = \frac{E_0B_0}{2\mu_0} = \frac{E_0^2}{2\mu_0c} = \tfrac12c\varepsilon_0E_0^2}$$
For a point source radiating power $P$ uniformly: $I = \frac{P}{4\pi r^2}$ (inverse-square law).

**Example:** sunlight above Earth's atmosphere has intensity ≈ 1361 W/m² (the **solar constant**). Then $E_0 = \sqrt{2I/(c\varepsilon_0)} = \sqrt{\frac{2\times1361}{(3\times10^8)(8.854\times10^{-12})}} \approx 1013$ V/m and $B_0 = E_0/c \approx 3.4$ μT. At the ground, on a clear day with the Sun overhead, about 1000 W/m² arrives.

### Momentum and radiation pressure
EM waves carry momentum: $p = U/c$ for energy $U$. When light is absorbed by a surface, it exerts **radiation pressure**:
$$P_{\text{rad}} = \frac Ic \;(\text{total absorption}), \qquad P_{\text{rad}} = \frac{2I}{c} \;(\text{perfect reflection at normal incidence})$$
Sunlight at Earth exerts about $4.5\times10^{-6}$ Pa on an absorbing surface — tiny, but significant over large areas and long times:
- **Solar sails** (e.g. JAXA's IKAROS, 2010; LightSail 2, 2019) propel spacecraft with sunlight alone.
- **Comet tails** point away from the Sun partly due to radiation pressure on dust.
- **Optical tweezers** (Ashkin, Nobel 2018) use focused laser light to trap and manipulate cells, bacteria and single molecules.
- **Laser cooling** of atoms uses photon momentum to slow atoms to microkelvin temperatures.
- Radiation pressure supports the outer layers of very massive stars (the Eddington limit).

## 6. Polarization

The direction of the electric field defines the wave's **polarization**.
- **Linear polarization:** $\vec E$ oscillates along a fixed line.
- **Circular polarization:** two perpendicular components of equal amplitude, 90° out of phase; $\vec E$ rotates. Used in 3D cinema glasses and satellite communications.
- **Elliptical polarization:** the general case.
- **Unpolarized light** (sunlight, light bulbs) consists of rapidly and randomly varying polarization directions.

### Malus's law
When polarized light of intensity $I_0$ passes through a polarizer whose axis makes angle $\theta$ with the polarization direction:
$$\boxed{I = I_0\cos^2\theta}$$
An ideal polarizer transmits half the intensity of unpolarized light. Two crossed polarizers (90°) block all light — but inserting a third at 45° between them lets $\frac18$ of the original unpolarized intensity through, a striking demonstration often used to illustrate quantum measurement.

### Polarization by reflection and scattering
- **Brewster's angle:** light reflected at $\tan\theta_B = n_2/n_1$ is completely polarized parallel to the surface (≈ 53° for air–water, ≈ 56° for air–glass). Polarized sunglasses block this horizontally polarized glare from roads and water.
- **Scattering:** sunlight scattered by air molecules is partially polarized, maximally at 90° from the Sun. Bees and many other insects navigate using sky polarization patterns.
- **Birefringence:** crystals like calcite have different refractive indices for different polarizations, producing double images. Stress in transparent plastics makes them birefringent — **photoelasticity** reveals stress patterns between crossed polarizers.
- **LCD screens** use liquid crystals between polarizers to control which pixels transmit light.

## 7. The Electromagnetic Spectrum

All EM waves are the same phenomenon at different frequencies. Photon energy $E = hf = hc/\lambda$ (with $hc \approx 1240$ eV·nm).

| Region | Wavelength | Frequency | Photon energy | Sources / uses |
|---|---|---|---|---|
| Radio | > 1 m | < 300 MHz | < 1.2 μeV | AM/FM radio, TV, radio astronomy, MRI |
| Microwave | 1 mm – 1 m | 300 MHz – 300 GHz | μeV – meV | Radar, microwave ovens (2.45 GHz), Wi-Fi, 5G, cosmic microwave background |
| Infrared | 700 nm – 1 mm | 300 GHz – 430 THz | meV – 1.8 eV | Thermal radiation, remote controls, night vision, fiber optics (1.55 μm) |
| Visible | 380 – 700 nm | 430 – 790 THz | 1.8 – 3.3 eV | Human vision; red ~700 nm, green ~530 nm, violet ~400 nm |
| Ultraviolet | 10 – 380 nm | 790 THz – 30 PHz | 3.3 – 124 eV | Sunburn, vitamin D synthesis, sterilization, fluorescence |
| X-rays | 0.01 – 10 nm | 30 PHz – 30 EHz | 124 eV – 124 keV | Medical imaging, crystallography, airport scanners |
| Gamma rays | < 0.01 nm | > 30 EHz | > 124 keV | Nuclear decay, cancer therapy, gamma-ray bursts |

(Boundaries are conventional and overlap; X-rays and gamma rays are often distinguished by origin — electronic vs. nuclear — rather than energy.)

**Atmospheric windows:** Earth's atmosphere is transparent to visible light and to radio waves (~1 cm to ~10 m) but opaque to most UV (absorbed by ozone), X-rays, gamma rays and much of the infrared. This is why X-ray, UV and far-infrared telescopes must be placed in space.

**Ionizing radiation:** photons above roughly 10 eV (far UV, X-rays, gamma rays) can ionize atoms and break chemical bonds, damaging DNA. Radio waves, microwaves and visible light are non-ionizing; their biological effects at normal intensities are primarily heating.

**Why we see "visible" light:** the Sun's emission peaks in this range, and the atmosphere and water are transparent there. Photon energies of 1.8–3.3 eV match electronic transitions in molecules like retinal, enabling vision without destroying the molecules.

## 8. Generation of Electromagnetic Waves

**Accelerating charges radiate.** A charge moving at constant velocity carries its field along but does not radiate; an accelerating charge emits EM waves. The power radiated by a non-relativistic accelerating charge is given by the **Larmor formula**:
$$P = \frac{q^2a^2}{6\pi\varepsilon_0c^3}$$
- **Antennas:** oscillating currents in a dipole antenna radiate at the oscillation frequency, most strongly perpendicular to the antenna and not at all along its axis. Efficient antennas have lengths comparable to half the wavelength.
- **Synchrotron radiation:** electrons circling in accelerators radiate intensely (a nuisance for particle physics, a powerful X-ray source for materials science and biology).
- **Bremsstrahlung** ("braking radiation"): electrons decelerating in matter emit X-rays (the basis of X-ray tubes).
- **Atoms and molecules** emit and absorb light in quantum transitions — fully explained only by quantum electrodynamics (QED).
- **The classical atom problem:** an electron orbiting a nucleus is accelerating and, classically, should radiate its energy away and spiral into the nucleus in about $10^{-11}$ s. The stability of atoms is one of the failures of classical physics that led to quantum mechanics.

## 9. Potentials and Gauge Freedom

Since $\nabla\cdot\vec B = 0$, we can write $\vec B = \nabla\times\vec A$ (vector potential). Faraday's law then gives $\vec E = -\nabla V - \frac{\partial\vec A}{\partial t}$ (scalar potential $V$). The potentials are not unique: the **gauge transformation**
$$\vec A \to \vec A + \nabla\chi, \qquad V \to V - \frac{\partial\chi}{\partial t}$$
leaves $\vec E$ and $\vec B$ unchanged for any function $\chi$. Choosing the **Lorenz gauge** ($\nabla\cdot\vec A + \frac{1}{c^2}\frac{\partial V}{\partial t} = 0$) turns Maxwell's equations into decoupled wave equations with sources:
$$\Box V = \frac{\rho}{\varepsilon_0}, \qquad \Box\vec A = \mu_0\vec J, \qquad \Box = \frac{1}{c^2}\frac{\partial^2}{\partial t^2} - \nabla^2$$

Gauge freedom, which might seem a mathematical curiosity, is the central organizing principle of modern particle physics: the Standard Model is a gauge theory. In quantum mechanics the potentials are physically significant — the **Aharonov–Bohm effect** (1959) shows electrons are affected by $\vec A$ even in regions where $\vec B = 0$.

## 10. Maxwell's Equations and Relativity

Maxwell's equations predict a single speed $c$ for light, independent of the source's motion — contradicting Galilean relativity, under which velocities simply add. Rather than modify Maxwell, Einstein (1905) modified our concepts of space and time: **special relativity**. Maxwell's equations are automatically consistent with relativity (they are **Lorentz invariant**). In relativity, $\vec E$ and $\vec B$ are components of a single **electromagnetic field tensor** $F^{\mu\nu}$; what one observer sees as a pure electric field, another moving observer sees as a mixture of electric and magnetic fields. Magnetism can be understood as a relativistic consequence of electrostatics plus the transformation of charge densities between frames.

## 11. Summary

| Equation | Differential form | Meaning |
|---|---|---|
| Gauss | $\nabla\cdot\vec E = \rho/\varepsilon_0$ | Charges source $\vec E$ |
| Gauss (magnetism) | $\nabla\cdot\vec B = 0$ | No monopoles |
| Faraday | $\nabla\times\vec E = -\partial\vec B/\partial t$ | Changing $\vec B$ → $\vec E$ |
| Ampère–Maxwell | $\nabla\times\vec B = \mu_0\vec J + \mu_0\varepsilon_0\partial\vec E/\partial t$ | Currents and changing $\vec E$ → $\vec B$ |

| Wave property | Formula |
|---|---|
| Speed of light | $c = 1/\sqrt{\mu_0\varepsilon_0} = 299\,792\,458$ m/s |
| Field ratio | $E = cB$ |
| Poynting vector | $\vec S = \vec E\times\vec B/\mu_0$ |
| Intensity | $I = \frac12c\varepsilon_0E_0^2$ |
| Radiation pressure | $I/c$ (absorbed), $2I/c$ (reflected) |
| Malus's law | $I = I_0\cos^2\theta$ |
| Brewster angle | $\tan\theta_B = n_2/n_1$ |
| Photon energy | $E = hf = hc/\lambda$ |
| Larmor power | $P = q^2a^2/(6\pi\varepsilon_0c^3)$ |
