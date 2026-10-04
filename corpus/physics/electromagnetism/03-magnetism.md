---
title: Magnetic Fields and Forces
field: Physics
subfield: Electromagnetism
level: high-school to undergraduate
keywords: [magnetic field, Lorentz force, cyclotron motion, mass spectrometer, Hall effect, force on a current-carrying wire, magnetic dipole moment, electric motor, Biot-Savart law, Ampere's law, solenoid, toroid, magnetic materials, ferromagnetism, paramagnetism, diamagnetism, Earth's magnetic field]
---

# Magnetic Fields and Forces

Magnetism was known in antiquity through lodestone (magnetite, Fe₃O₄) and was used in compasses in China by the 11th century. In 1820 Hans Christian Ørsted discovered that an electric current deflects a compass needle — the first link between electricity and magnetism. Within months André-Marie Ampère had formulated the laws of force between currents. We now know that **magnetic fields are produced by moving charges (currents) and by the intrinsic magnetic moments of elementary particles (spin)**, and that electricity and magnetism are two aspects of a single electromagnetic field.

## 1. The Magnetic Field and the Lorentz Force

A magnetic field $\vec B$ exerts a force on a **moving** charge:
$$\boxed{\vec F_B = q\vec v\times\vec B}, \qquad F_B = |q|vB\sin\theta$$
Together with the electric force, the total **Lorentz force** is
$$\boxed{\vec F = q(\vec E + \vec v\times\vec B)}$$

SI unit of $B$: the **tesla** (T = N/(A·m) = N·s/(C·m)). The gauss is also used: 1 T = 10⁴ G.

### Key properties of the magnetic force
1. It acts only on moving charges; a stationary charge feels no magnetic force.
2. It is perpendicular to both $\vec v$ and $\vec B$ (right-hand rule: fingers along $\vec v$, curl toward $\vec B$, thumb gives the force on a positive charge; reverse for negative).
3. **It does no work** ($\vec F\perp\vec v$), so it cannot change a particle's speed or kinetic energy — only its direction.
4. Charges moving parallel to $\vec B$ feel no force.

### Typical field strengths

| Source | $B$ |
|---|---|
| Human brain activity (measured by MEG) | ~$10^{-13}$–$10^{-12}$ T |
| Interstellar space | ~$10^{-10}$ T |
| Earth's surface | 25–65 μT |
| Refrigerator magnet | ~5–10 mT |
| Neodymium magnet surface | ~1–1.4 T |
| Clinical MRI scanner | 1.5–3 T (research up to 11.7 T) |
| LHC dipole magnets | 8.3 T |
| Strongest continuous lab field | ~45.5 T |
| Neutron star surface | ~$10^8$ T |
| Magnetar | ~$10^{10}$–$10^{11}$ T |

## 2. Motion of Charged Particles in Magnetic Fields

### Circular (cyclotron) motion
A charge moving perpendicular to a uniform $\vec B$ follows a circle, with the magnetic force providing the centripetal force:
$$|q|vB = \frac{mv^2}{r} \Rightarrow \boxed{r = \frac{mv}{|q|B} = \frac{p}{|q|B}}$$
The angular frequency, **cyclotron frequency**, is independent of speed and radius:
$$\omega_c = \frac{|q|B}{m}, \qquad f_c = \frac{|q|B}{2\pi m}$$

If the velocity has a component along $\vec B$, the path is a **helix**. Charged particles spiral along magnetic field lines — this is how Earth's field funnels solar-wind particles toward the poles, creating **auroras**, and traps particles in the **Van Allen belts**. Magnetic confinement fusion reactors (tokamaks) use the same principle.

**Worked example 2.1:** A proton moving at $10^6$ m/s perpendicular to a 0.5 T field:
$r = \frac{(1.673\times10^{-27})(10^6)}{(1.602\times10^{-19})(0.5)} \approx 2.09$ cm; $f_c = \frac{(1.602\times10^{-19})(0.5)}{2\pi(1.673\times10^{-27})} \approx 7.6$ MHz.

### Applications
- **Cyclotron** (Lawrence, 1932): particles spiral outward between two "dees" with an alternating voltage at $f_c$, gaining energy each half-turn. Used to produce medical isotopes and proton therapy beams. At relativistic speeds $f_c$ changes, requiring synchrocyclotrons or synchrotrons.
- **Mass spectrometer:** ions accelerated through voltage $V$ enter a magnetic field; $r = \frac1B\sqrt{\frac{2mV}{q}}$ separates them by mass-to-charge ratio. Used for isotope analysis, drug testing, proteomics and carbon dating.
- **Velocity selector:** crossed $\vec E$ and $\vec B$ fields let through only particles with $v = E/B$ (electric and magnetic forces cancel). J. J. Thomson (1897) used crossed fields to measure the electron's charge-to-mass ratio, discovering the electron.
- **Bubble chambers and particle detectors:** curvature of tracks in a magnetic field reveals charge sign and momentum.

### The Hall effect
When current flows through a conductor in a perpendicular magnetic field, the magnetic force pushes charge carriers to one side, creating a transverse **Hall voltage**:
$$V_H = \frac{IB}{nqt}$$
($t$ = thickness in the direction of $\vec B$). The sign of $V_H$ reveals the sign of the charge carriers — in some metals and in p-type semiconductors the carriers behave as positive "holes". Hall sensors measure magnetic fields and are used in phones (compass), car speed sensors, brushless motors and current sensors. At low temperatures and strong fields in 2D systems, the Hall resistance becomes quantized in units of $h/e^2$ (the **quantum Hall effect**, von Klitzing, Nobel 1985), now used as a resistance standard.

## 3. Force on a Current-Carrying Wire

A current is moving charges, so a wire carrying current $I$ in a field feels a force:
$$\boxed{\vec F = I\vec L\times\vec B}, \qquad F = ILB\sin\theta$$
For a curved wire: $d\vec F = I\,d\vec l\times\vec B$.

This is the basis of electric motors, loudspeakers (a coil in a permanent magnet's field pushes the cone), and railguns.

### Torque on a current loop
A loop of area $A$ carrying current $I$ in a uniform field experiences zero net force but a **torque**:
$$\boxed{\vec\tau = \vec\mu\times\vec B}, \qquad \vec\mu = NI\vec A$$
$\vec\mu$ is the **magnetic dipole moment** (A·m²), perpendicular to the loop by the right-hand rule (fingers along current, thumb along $\vec\mu$); $N$ is the number of turns. The potential energy is $U = -\vec\mu\cdot\vec B$, so the loop tends to align $\vec\mu$ with $\vec B$ — just as a compass needle does.

**DC electric motor:** a coil in a magnetic field experiences a torque; a **commutator** reverses the current every half-turn so the torque always acts in the same rotational sense. Modern brushless motors switch the current electronically. The **galvanometer** (the basis of analog meters) uses the torque on a coil balanced against a spring.

## 4. Sources of Magnetic Fields: The Biot–Savart Law

A small current element $I\,d\vec l$ produces a magnetic field at a point displaced by $\vec r$:
$$\boxed{d\vec B = \frac{\mu_0}{4\pi}\frac{I\,d\vec l\times\hat r}{r^2}}$$
where $\mu_0 = 4\pi\times10^{-7}$ T·m/A ≈ $1.2566\times10^{-6}$ T·m/A is the **permeability of free space**. (Since the 2019 SI redefinition, $\mu_0$ is measured rather than exact, but equals $4\pi\times10^{-7}$ to within about one part in $10^{10}$.)

### Important results
**Long straight wire** at distance $r$:
$$B = \frac{\mu_0I}{2\pi r}$$
Field lines are concentric circles around the wire; direction by the right-hand grip rule (thumb along current, fingers curl along $\vec B$). For 10 A at 1 cm: $B = 2\times10^{-4}$ T — about four times Earth's field.

**Center of a circular loop** of radius $R$ ($N$ turns): $B = \frac{\mu_0NI}{2R}$.

**On the axis of a loop** at distance $z$: $B = \frac{\mu_0IR^2}{2(R^2 + z^2)^{3/2}}$. Far away, $B \approx \frac{\mu_0}{2\pi}\frac{\mu}{z^3}$ — a dipole field, falling as $1/r^3$.

### Force between parallel wires
Wire 1 creates a field at wire 2, which feels a force. Per unit length:
$$\frac{F}{L} = \frac{\mu_0I_1I_2}{2\pi d}$$
**Parallel currents attract; antiparallel currents repel** (opposite to electric charges!). Until 2019 this relation defined the ampere: the current that produces a force of $2\times10^{-7}$ N per meter between two parallel wires 1 m apart.

## 5. Ampère's Law

> The line integral of $\vec B$ around any closed loop equals $\mu_0$ times the current passing through the loop.
$$\boxed{\oint\vec B\cdot d\vec l = \mu_0I_{\text{enc}}}$$
(Maxwell later added a displacement-current term; see the Maxwell's equations document.) Ampère's law plays the same role for magnetism that Gauss's law plays for electricity: always true, and a shortcut for symmetric current distributions.

**Example 5.1 – Long straight wire:** circle of radius $r$: $B(2\pi r) = \mu_0I \Rightarrow B = \mu_0I/(2\pi r)$ ✓.

**Example 5.2 – Inside a thick wire** of radius $R$ with uniform current: $B = \frac{\mu_0Ir}{2\pi R^2}$ for $r < R$ (grows linearly).

**Example 5.3 – Ideal solenoid** with $n$ turns per unit length: using a rectangular loop with one side inside,
$$B = \mu_0nI$$
uniform inside and (ideally) zero outside. A solenoid is the magnetic analog of a parallel-plate capacitor. With an iron core, the field is multiplied by the core's relative permeability (hundreds to thousands) — an **electromagnet**. Applications: relays, MRI magnets (superconducting solenoids), door locks, speakers, scrap-yard cranes.

**Example 5.4 – Toroid** with $N$ total turns: $B = \frac{\mu_0NI}{2\pi r}$ inside, zero outside. Tokamak fusion reactors use toroidal fields.

### Magnetic Gauss's law
$$\oint\vec B\cdot d\vec A = 0$$
There are **no magnetic monopoles** (isolated north or south poles) — magnetic field lines always form closed loops. Cutting a bar magnet in half yields two smaller magnets, each with both poles. Some grand unified theories predict monopoles, but none has ever been observed despite extensive searches.

## 6. Magnetism in Matter

At the atomic level, magnetic moments arise from electrons' orbital motion and, more importantly, from their intrinsic **spin**. The natural unit is the **Bohr magneton**, $\mu_B = \frac{e\hbar}{2m_e} = 9.274\times10^{-24}$ J/T.

In a material, the **magnetization** $\vec M$ (magnetic moment per unit volume) modifies the field: $\vec B = \mu_0(\vec H + \vec M)$, and for linear materials $\vec M = \chi_m\vec H$, so $\vec B = \mu_0(1 + \chi_m)\vec H = \mu\vec H$, with relative permeability $\mu_r = 1 + \chi_m$.

| Type | $\chi_m$ | Mechanism | Examples |
|---|---|---|---|
| Diamagnetic | small, negative (~$-10^{-5}$) | Induced orbital currents oppose applied field (Lenz's law); present in all materials | Water, copper, bismuth, carbon, superconductors ($\chi = -1$, perfect diamagnets) |
| Paramagnetic | small, positive (~$10^{-5}$–$10^{-3}$) | Permanent atomic moments partially align; thermal motion opposes ($\chi \propto 1/T$, Curie's law) | Aluminum, oxygen (liquid O₂ sticks to a magnet), platinum |
| Ferromagnetic | large, positive ($10^2$–$10^5$), nonlinear | Quantum exchange interaction aligns neighboring spins in **domains** | Iron, nickel, cobalt, gadolinium, NdFeB, magnetite |

**Diamagnetic levitation:** strong field gradients (~16 T) can levitate water-containing objects — famously, a live frog (Geim and Berry, Ig Nobel Prize 2000).

### Ferromagnetism in detail
- In ferromagnets, the **exchange interaction** (a quantum-mechanical effect arising from the Pauli principle and Coulomb repulsion) makes it energetically favorable for neighboring spins to align.
- An unmagnetized piece of iron consists of many **magnetic domains** (typically micrometers to millimeters), each fully magnetized but randomly oriented. An external field grows favorably oriented domains and rotates others.
- **Hysteresis:** magnetization depends on history. After the field is removed, a **remanent** magnetization remains (permanent magnet); a **coercive** field is needed to demagnetize. "Hard" magnets (NdFeB, SmCo, alnico) have wide hysteresis loops; "soft" magnets (silicon steel, ferrites) have narrow loops and are used in transformer cores to minimize energy loss.
- **Curie temperature:** above $T_C$, thermal agitation destroys ferromagnetic order and the material becomes paramagnetic. Iron: 770 °C; nickel: 358 °C; NdFeB: ~310–400 °C.
- Related orders: **antiferromagnetism** (neighboring spins antiparallel, e.g. MnO, chromium) and **ferrimagnetism** (unequal antiparallel moments, e.g. magnetite, ferrites).

**Magnetic data storage:** hard disk drives store bits as tiny magnetized regions read by giant-magnetoresistance (GMR) heads (Fert and Grünberg, Nobel 2007).

## 7. Earth's Magnetic Field

- Approximately a dipole tilted about 10° from the rotation axis, with surface strength 25–65 μT.
- Generated by a **geodynamo**: convection of molten iron in the outer core, combined with Earth's rotation, sustains electric currents and hence the field.
- Earth's **geographic North Pole is near a magnetic south pole** — that is why the north pole of a compass needle points north.
- The magnetic poles wander (the north magnetic pole has moved hundreds of kilometers in the last century), and the field has **reversed polarity** many times; the last full reversal (Brunhes–Matuyama) was about 780 000 years ago. Records of reversals frozen into seafloor basalt provided key evidence for seafloor spreading and plate tectonics.
- The **magnetosphere** deflects the solar wind, protecting the atmosphere from erosion and life from charged-particle radiation.
- Many animals (migratory birds, sea turtles, salmon, some bacteria containing magnetite chains) sense Earth's field for navigation.

## 8. Summary

| Concept | Formula |
|---|---|
| Lorentz force | $\vec F = q(\vec E + \vec v\times\vec B)$ |
| Cyclotron radius | $r = mv/(\lvert q\rvert B)$ |
| Cyclotron frequency | $\omega_c = \lvert q\rvert B/m$ |
| Force on wire | $\vec F = I\vec L\times\vec B$ |
| Magnetic moment | $\vec\mu = NI\vec A$; $\vec\tau = \vec\mu\times\vec B$; $U = -\vec\mu\cdot\vec B$ |
| Biot–Savart | $d\vec B = \frac{\mu_0}{4\pi}\frac{Id\vec l\times\hat r}{r^2}$ |
| Long wire | $B = \mu_0I/(2\pi r)$ |
| Loop center | $B = \mu_0NI/(2R)$ |
| Solenoid | $B = \mu_0nI$ |
| Parallel wires | $F/L = \mu_0I_1I_2/(2\pi d)$ |
| Ampère's law | $\oint\vec B\cdot d\vec l = \mu_0I_{\text{enc}}$ |
| No monopoles | $\oint\vec B\cdot d\vec A = 0$ |
| Hall voltage | $V_H = IB/(nqt)$ |
