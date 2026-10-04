---
title: Special Relativity
field: Physics
subfield: Relativity
level: high-school to undergraduate
keywords: [special relativity, Einstein, postulates, speed of light, time dilation, length contraction, relativity of simultaneity, Lorentz transformation, Lorentz factor, spacetime interval, Minkowski diagram, light cone, twin paradox, relativistic velocity addition, relativistic momentum, E=mc^2, rest energy, four-vectors, muon decay]
---

# Special Relativity

In 1905, his "miracle year", Albert Einstein published a paper titled *On the Electrodynamics of Moving Bodies*. Starting from two simple postulates, he showed that our everyday notions of absolute time and absolute space are wrong: time intervals and lengths depend on the observer's motion, simultaneity is relative, and mass and energy are equivalent. Special relativity has been confirmed by countless experiments and is built into particle accelerators, GPS, nuclear physics and quantum field theory.

## 1. The Problem: Maxwell vs. Galileo

In **Galilean relativity**, velocities simply add: if a train moves at $v$ and you walk forward at $u$ inside it, your speed relative to the ground is $u + v$. The laws of mechanics are the same in all inertial frames.

But Maxwell's equations predict that light travels at $c = 1/\sqrt{\mu_0\varepsilon_0}$, with no reference to any frame. If Galilean addition held, light speed would differ between frames, and Maxwell's equations would hold only in one special frame — presumably the rest frame of the "luminiferous aether". The **Michelson–Morley experiment** (1887) searched for Earth's motion through this aether and found nothing. Lorentz and FitzGerald proposed ad hoc contractions of moving objects to explain the null result. Einstein instead questioned the nature of time itself.

## 2. Einstein's Postulates

1. **Principle of relativity:** the laws of physics are the same in all inertial reference frames. No experiment can detect absolute uniform motion.
2. **Constancy of the speed of light:** the speed of light in vacuum has the same value $c$ in all inertial frames, independent of the motion of the source or the observer.
$$c = 299\,792\,458 \text{ m/s (exact)}$$

The second postulate is deeply counterintuitive: if you chase a light beam at $0.9c$, you still measure it receding from you at $c$. Everything that follows is a logical consequence of taking these two postulates seriously.

## 3. Relativity of Simultaneity

Events that are simultaneous in one frame are **not** simultaneous in another frame moving relative to the first (unless they occur at the same place).

**Einstein's train thought experiment:** lightning strikes both ends of a moving train at the same time according to an observer on the platform standing midway between the strikes. A passenger at the middle of the train moves toward the front strike's light and away from the rear strike's light, so the passenger receives the front flash first. Since light travels at $c$ in the train's frame too, and the passenger is equidistant from the two ends, the passenger concludes the front strike happened **first**. Neither observer is wrong; simultaneity is frame-dependent.

This undermines the idea of a universal "now" and is the root of the other relativistic effects.

## 4. Time Dilation

**Light clock:** a light pulse bounces between two mirrors separated by $L$. In the clock's rest frame, one tick takes $\Delta t_0 = 2L/c$. For an observer who sees the clock moving at speed $v$, the light follows a longer diagonal path. Since light still travels at $c$, each tick takes longer. Using Pythagoras: $(c\Delta t/2)^2 = L^2 + (v\Delta t/2)^2$, which gives
$$\boxed{\Delta t = \gamma\Delta t_0}, \qquad \boxed{\gamma = \frac{1}{\sqrt{1 - v^2/c^2}}}$$
$\gamma \ge 1$ is the **Lorentz factor**. $\Delta t_0$ is the **proper time** — the time interval measured by a clock present at both events (at rest relative to them).

**Moving clocks run slow.** This is a property of time itself, not of clock mechanisms: it applies equally to atomic clocks, biological aging and radioactive decay.

| $v/c$ | $\gamma$ |
|---|---|
| 0.01 | 1.00005 |
| 0.1 | 1.005 |
| 0.5 | 1.155 |
| 0.8 | 1.667 |
| 0.9 | 2.294 |
| 0.99 | 7.09 |
| 0.999 | 22.4 |
| 0.9999 | 70.7 |
| LHC protons (6.8 TeV) | ~7250 |

For everyday speeds, $\gamma \approx 1 + \frac12\frac{v^2}{c^2}$ — the effect is minuscule. A passenger on a 900 km/h airliner ages only about 1.25 nanoseconds per hour less than people on the ground (ignoring gravitational effects).

### Experimental evidence: cosmic-ray muons
Muons are produced ~10–15 km up in the atmosphere by cosmic rays. Their mean lifetime at rest is $\tau_0 = 2.2$ μs. Even at nearly $c$, without time dilation they would travel only about 660 m on average before decaying, so few should reach the ground. Yet many do. At $v = 0.995c$, $\gamma \approx 10$: in Earth's frame their lifetime is ~22 μs, allowing ~6.6 km of travel on average. (Rossi and Hall, 1941; Frisch and Smith, 1963.) In storage rings at CERN, muons circling at $\gamma \approx 29.3$ lived 29.3 times longer, confirming time dilation to 0.1%.

Other confirmations: the Hafele–Keating experiment (1971) flew atomic clocks around the world; particle lifetimes in accelerators; and GPS (see the general relativity document for the combined effect).

## 5. Length Contraction

An object moving at speed $v$ is shortened along its direction of motion:
$$\boxed{L = \frac{L_0}{\gamma} = L_0\sqrt{1 - v^2/c^2}}$$
$L_0$ is the **proper length**, measured in the object's rest frame. Dimensions perpendicular to the motion are unchanged.

**Consistency with time dilation (muons):** in the muon's own frame, its lifetime is just 2.2 μs, but the atmosphere rushes toward it at $0.995c$, contracted by $\gamma \approx 10$ — so the 10 km of atmosphere is only ~1 km thick. Both frames agree the muon reaches the ground.

**Ladder (barn–pole) paradox:** a ladder longer than a barn can, in the barn's frame, fit inside it momentarily when moving fast enough. In the ladder's frame, the barn is even shorter. The resolution is the relativity of simultaneity: "both doors closed at the same time" is true in one frame but not the other.

**Visual appearance:** due to light-travel-time effects, a fast-moving sphere appears rotated rather than flattened (Terrell–Penrose effect) — length contraction is real but is not what a camera directly "sees".

## 6. The Lorentz Transformation

Frame $S'$ moves at velocity $v$ along the $x$-axis relative to frame $S$, with origins coinciding at $t = t' = 0$. Coordinates of an event transform as:
$$\boxed{x' = \gamma(x - vt), \quad y' = y, \quad z' = z, \quad t' = \gamma\left(t - \frac{vx}{c^2}\right)}$$
Inverse: $x = \gamma(x' + vt')$, $t = \gamma(t' + vx'/c^2)$.

- For $v \ll c$, $\gamma \to 1$ and $vx/c^2 \to 0$, recovering the Galilean transformation $x' = x - vt$, $t' = t$.
- The term $-vx/c^2$ in $t'$ encodes the relativity of simultaneity: events with the same $t$ but different $x$ have different $t'$.
- Time dilation and length contraction follow directly.

### Relativistic velocity addition
If an object moves at $u'$ in frame $S'$ (along $x$), its velocity in $S$ is
$$\boxed{u = \frac{u' + v}{1 + u'v/c^2}}$$
- If $u' = c$, then $u = c$: light speed is invariant.
- Combining speeds below $c$ always gives a speed below $c$. A spaceship moving at $0.8c$ fires a probe forward at $0.8c$ relative to itself; Earth measures the probe at $\frac{1.6c}{1.64} \approx 0.976c$, not $1.6c$.

## 7. Spacetime

Hermann Minkowski (1908): "Henceforth space by itself, and time by itself, are doomed to fade away into mere shadows, and only a kind of union of the two will preserve an independent reality."

### The spacetime interval
Different observers disagree on distances and times between events, but they all agree on the **spacetime interval**:
$$\boxed{(\Delta s)^2 = (c\Delta t)^2 - (\Delta x)^2 - (\Delta y)^2 - (\Delta z)^2}$$
(sign convention $+---$; some texts use $-+++$). It is invariant under Lorentz transformations, just as distance is invariant under rotations.

| Interval type | Condition | Meaning |
|---|---|---|
| Timelike | $(\Delta s)^2 > 0$ | Events can be causally connected; there is a frame where they occur at the same place; $\Delta s/c$ is the proper time between them |
| Lightlike (null) | $(\Delta s)^2 = 0$ | Connected by a light signal |
| Spacelike | $(\Delta s)^2 < 0$ | No causal connection possible; their time order depends on the frame |

### Light cones and causality
On a **Minkowski (spacetime) diagram**, with time vertical and space horizontal (units with $c = 1$), light travels on 45° lines. The **light cone** of an event divides spacetime into its causal future, causal past, and "elsewhere" (spacelike-separated events). Because the time ordering of timelike-separated events is the same in all frames, **causality is preserved**. Faster-than-light signaling would allow some observers to see effects precede causes — this is why nothing (no information, matter or energy) can travel faster than light.

### Proper time and the twin paradox
For a path through spacetime, the **proper time** experienced by a clock following it is
$$\tau = \int\sqrt{1 - v(t)^2/c^2}\,dt$$
Among all paths between two timelike-separated events, the straight (unaccelerated, inertial) worldline has the **longest** proper time.

**Twin paradox:** one twin travels to a star at high speed and returns; the other stays on Earth. The traveler ages less. It seems symmetric — from the traveler's view, Earth moved — but it is not: the traveler changes inertial frames (accelerates) at the turnaround, while the Earth twin remains inertial. Example: a round trip to a star 10 light-years away at $0.8c$ takes 25 years for the Earth twin but only $25/\gamma = 15$ years for the traveler.

## 8. Relativistic Momentum and Energy

To keep momentum conserved in all frames, momentum must be redefined:
$$\boxed{\vec p = \gamma m\vec v}$$
where $m$ is the (invariant) mass. As $v \to c$, $p \to \infty$: no finite force can accelerate a massive object to $c$.

(Older texts use "relativistic mass" $\gamma m$; modern physics uses only the invariant mass $m$ and puts $\gamma$ in the formulas.)

### Energy
The total energy of a free particle is
$$\boxed{E = \gamma mc^2}$$
Even at rest ($\gamma = 1$), a particle has **rest energy**
$$\boxed{E_0 = mc^2}$$
The kinetic energy is the difference:
$$K = (\gamma - 1)mc^2$$
For $v \ll c$: $\gamma - 1 \approx \frac12\frac{v^2}{c^2}$, so $K \approx \frac12mv^2$ — the classical result emerges as an approximation.

### Energy–momentum relation
$$\boxed{E^2 = (pc)^2 + (mc^2)^2}$$
- For massless particles (photons, and gluons): $E = pc$. They must travel at exactly $c$.
- Also useful: $\vec v = \frac{\vec pc^2}{E}$.

### Mass–energy equivalence: $E = mc^2$
Mass is a form of energy. Since $c^2 = 9\times10^{16}$ J/kg, a tiny mass corresponds to enormous energy: 1 gram ↔ $9\times10^{13}$ J ≈ 21 kilotons of TNT (roughly the energy of the Nagasaki bomb).

- **Nuclear binding:** the mass of a nucleus is less than the sum of its nucleons' masses. The **mass defect** $\Delta m$ times $c^2$ is the binding energy. Fission of uranium-235 converts about 0.1% of the mass into energy; fusion of hydrogen into helium converts about 0.7%.
- **The Sun** converts about 4.3 million tonnes of mass into energy each second ($P = 3.83\times10^{26}$ W, so $\Delta m/\Delta t = P/c^2 \approx 4.3\times10^9$ kg/s).
- **Pair annihilation:** an electron and positron annihilate into gamma rays carrying $2\times0.511$ MeV (the basis of PET scans).
- **Pair production:** a photon with $E > 2m_ec^2 = 1.022$ MeV can create an electron–positron pair near a nucleus.
- **Chemistry:** chemical reactions also change mass, but by only ~1 part in $10^{10}$ — unmeasurably small. A charged battery is heavier than a discharged one by ~$10^{-13}$ of its mass.
- **Proton mass:** about 99% of the proton's mass comes not from the Higgs-generated quark masses but from the energy of the gluon fields and quark motion inside it (via $E = mc^2$).

### Units in particle physics
Energies in electron volts (eV, keV, MeV, GeV, TeV); masses in eV/c²; momenta in eV/c. Electron: 0.511 MeV/c²; proton: 938.3 MeV/c²; neutron: 939.6 MeV/c²; Higgs boson: ~125 GeV/c².

### Worked example 8.1
**Problem:** An electron is accelerated through a potential difference of 1 MV. Find its kinetic energy, total energy, $\gamma$, speed and momentum.
**Solution:** $K = 1$ MeV. $E = K + mc^2 = 1.511$ MeV. $\gamma = E/(mc^2) = 1.511/0.511 \approx 2.957$.
$v/c = \sqrt{1 - 1/\gamma^2} = \sqrt{1 - 0.1144} \approx 0.941$.
$pc = \sqrt{E^2 - (mc^2)^2} = \sqrt{2.283 - 0.261} \approx 1.422$ MeV, so $p \approx 1.42$ MeV/c.
(The classical formula would give $v = \sqrt{2K/m} \approx 1.98c$ — impossible.)

## 9. Four-Vectors (Brief Introduction)

Relativity is most elegantly expressed with **four-vectors**, whose "length" is Lorentz invariant:
- **Position:** $x^\mu = (ct, x, y, z)$
- **Four-velocity:** $u^\mu = \gamma(c, \vec v)$, with $u^\mu u_\mu = c^2$
- **Four-momentum:** $p^\mu = (E/c, \vec p)$, with $p^\mu p_\mu = m^2c^2$ — this is $E^2 = p^2c^2 + m^2c^4$
- **Four-current:** $J^\mu = (c\rho, \vec J)$; charge conservation is $\partial_\mu J^\mu = 0$

Conservation of four-momentum in collisions combines energy and momentum conservation. The **invariant mass** of a system of particles, $M^2c^4 = (\sum E)^2 - (\sum\vec p)^2c^2$, is how new particles like the Higgs boson are discovered: reconstructing it from decay products reveals a peak at the parent particle's mass.

**Relativistic Doppler effect:** for a source receding at speed $v$ (along the line of sight), $f_{\text{obs}} = f_{\text{src}}\sqrt{\frac{1 - \beta}{1 + \beta}}$, $\beta = v/c$. There is also a **transverse Doppler effect** (pure time dilation) with no classical counterpart.

## 10. Common Misconceptions

1. **"Relativity says everything is relative."** No — it is built on invariants: the speed of light, the spacetime interval, proper time, rest mass, and the laws of physics themselves.
2. **"Time dilation is an illusion caused by signal delays."** No — it remains after correcting for light-travel time and has physical consequences (muons survive, twins age differently).
3. **"Nothing can go faster than light, period."** No *information, matter or energy* can travel faster than light locally. But the expansion of space can carry distant galaxies away faster than $c$; shadows and laser spots can sweep across surfaces faster than $c$; and phase velocities can exceed $c$. None of these carry information superluminally.
4. **"Quantum entanglement allows faster-than-light communication."** No — the no-signaling theorem forbids it.
5. **"Mass increases with speed."** Only in the outdated "relativistic mass" language; the invariant mass is constant. It is momentum and energy that grow without bound.
6. **"Special relativity can't handle acceleration."** It can; only gravity requires general relativity.

## 11. Summary

| Concept | Formula |
|---|---|
| Lorentz factor | $\gamma = 1/\sqrt{1 - v^2/c^2}$ |
| Time dilation | $\Delta t = \gamma\Delta t_0$ |
| Length contraction | $L = L_0/\gamma$ |
| Lorentz transformation | $x' = \gamma(x - vt)$, $t' = \gamma(t - vx/c^2)$ |
| Velocity addition | $u = (u' + v)/(1 + u'v/c^2)$ |
| Spacetime interval | $(\Delta s)^2 = c^2\Delta t^2 - \Delta x^2 - \Delta y^2 - \Delta z^2$ |
| Momentum | $\vec p = \gamma m\vec v$ |
| Total energy | $E = \gamma mc^2$ |
| Rest energy | $E_0 = mc^2$ |
| Kinetic energy | $K = (\gamma - 1)mc^2$ |
| Energy–momentum | $E^2 = (pc)^2 + (mc^2)^2$ |
| Photon | $E = pc = hf$ |
| Relativistic Doppler | $f = f_0\sqrt{(1-\beta)/(1+\beta)}$ (receding) |
