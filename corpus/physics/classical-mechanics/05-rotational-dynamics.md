---
title: Rotational Motion, Torque and Angular Momentum
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [torque, moment of inertia, angular momentum, rotational kinetic energy, parallel axis theorem, rolling motion, static equilibrium, gyroscope, precession, conservation of angular momentum]
---

# Rotational Motion, Torque and Angular Momentum

Rotation is everywhere: wheels, planets, spinning electrons (in a quantum sense), figure skaters, turbines and hard drives. Rotational dynamics mirrors linear dynamics almost perfectly — every linear quantity has a rotational counterpart. Learning the dictionary between them is the key to this topic.

## 1. Rotational Kinematics (Review)

For a rigid body rotating about a fixed axis, every point moves in a circle and shares the same angular variables:
- Angular position $\theta$ (rad)
- Angular velocity $\omega = d\theta/dt$ (rad/s)
- Angular acceleration $\alpha = d\omega/dt$ (rad/s²)

A point at distance $r$ from the axis has
$$s = r\theta, \qquad v = r\omega, \qquad a_t = r\alpha, \qquad a_c = r\omega^2$$

(These require $\theta$ in **radians**. One revolution $= 2\pi$ rad $= 360°$; 1 rad ≈ 57.3°. A rotation rate in rpm converts as $\omega = 2\pi \cdot \text{rpm}/60$.)

Angular velocity is a vector along the rotation axis, with direction given by the **right-hand rule**: curl the fingers of your right hand in the direction of rotation and your thumb points along $\vec\omega$.

## 2. Torque

A force's ability to cause rotation depends not only on its magnitude but on where and in what direction it is applied. That is why door handles are placed far from the hinges.

The **torque** of a force $\vec F$ applied at position $\vec r$ (measured from the pivot or axis) is
$$\boxed{\vec\tau = \vec r \times \vec F}, \qquad \tau = rF\sin\phi$$
where $\phi$ is the angle between $\vec r$ and $\vec F$. SI unit: N·m (not written as joules, even though dimensionally identical, because torque is not energy).

Equivalent ways to compute the magnitude:
- $\tau = r_\perp F$ where $r_\perp = r\sin\phi$ is the **lever arm** (moment arm): the perpendicular distance from the axis to the line of action of the force.
- $\tau = r F_\perp$ where $F_\perp = F\sin\phi$ is the component of force perpendicular to $\vec r$.

A force whose line of action passes through the axis produces no torque. Pushing on a door at its hinge does nothing.

**Sign convention for 2D problems:** counterclockwise torques positive, clockwise negative (or vice versa, consistently).

## 3. Moment of Inertia

Applying Newton's second law to each particle of a rigid body rotating about a fixed axis: the tangential force on particle $i$ is $F_i = m_i a_{t,i} = m_i r_i \alpha$, and its torque is $\tau_i = r_i F_i = m_i r_i^2 \alpha$. Summing:
$$\tau_{\text{net}} = \left(\sum_i m_i r_i^2\right)\alpha$$

The quantity in parentheses is the **moment of inertia**:
$$\boxed{I = \sum_i m_i r_i^2 = \int r^2\,dm}$$
SI unit: kg·m². Moment of inertia is the rotational analogue of mass: it measures resistance to angular acceleration. It depends not just on mass but on **how the mass is distributed relative to the axis** — mass far from the axis contributes much more (quadratically).

### Moments of inertia of common uniform bodies (mass $M$)

| Body | Axis | $I$ |
|---|---|---|
| Point mass at distance $R$ | — | $MR^2$ |
| Thin ring / hollow cylinder (radius $R$) | Central axis | $MR^2$ |
| Solid disk / solid cylinder (radius $R$) | Central axis | $\frac12 MR^2$ |
| Thick-walled hollow cylinder (radii $R_1$, $R_2$) | Central axis | $\frac12 M(R_1^2 + R_2^2)$ |
| Solid sphere (radius $R$) | Through center | $\frac25 MR^2$ |
| Thin spherical shell (radius $R$) | Through center | $\frac23 MR^2$ |
| Thin rod (length $L$) | Through center, perpendicular | $\frac{1}{12} ML^2$ |
| Thin rod (length $L$) | Through one end, perpendicular | $\frac13 ML^2$ |
| Rectangular plate ($a \times b$) | Through center, perpendicular to plate | $\frac{1}{12}M(a^2 + b^2)$ |

### Derivation example: uniform rod about its center
Linear density $\lambda = M/L$, $dm = \lambda\,dx$:
$$I = \int_{-L/2}^{L/2} x^2 \lambda\,dx = \lambda \frac{x^3}{3}\Big|_{-L/2}^{L/2} = \lambda\frac{L^3}{12} = \frac{1}{12}ML^2$$

### Derivation example: solid disk
Divide into thin rings of radius $r$, width $dr$. Surface density $\sigma = M/(\pi R^2)$, ring mass $dm = \sigma\,2\pi r\,dr$:
$$I = \int_0^R r^2 \sigma 2\pi r\,dr = 2\pi\sigma\frac{R^4}{4} = \frac12 MR^2$$

### Parallel-axis theorem
If $I_{\text{cm}}$ is the moment of inertia about an axis through the center of mass, then about a parallel axis a distance $d$ away:
$$\boxed{I = I_{\text{cm}} + Md^2}$$
Check: rod about its end, $I = \frac{1}{12}ML^2 + M(L/2)^2 = \frac13 ML^2$ ✓. The moment of inertia is always smallest about an axis through the center of mass.

### Perpendicular-axis theorem (flat bodies only)
For a planar object in the $xy$-plane: $I_z = I_x + I_y$. Example: a thin disk about a diameter has $I = \frac14 MR^2$, because $I_z = \frac12 MR^2 = 2I_{\text{diam}}$.

## 4. Newton's Second Law for Rotation

$$\boxed{\tau_{\text{net}} = I\alpha}$$
(about a fixed axis, or about the center of mass even if it accelerates).

### Worked example 4.1 – Pulley with mass
**Problem:** A block of mass $m = 2$ kg hangs from a light string wrapped around a solid disk pulley of mass $M = 4$ kg and radius $R = 0.1$ m that rotates freely on a fixed axle. Find the block's acceleration and the string tension. ($g = 10$ m/s²)

**Solution:**
- Block: $mg - T = ma$
- Pulley: $TR = I\alpha = \frac12 MR^2 \cdot \frac{a}{R} \Rightarrow T = \frac12 Ma$
- Adding: $mg = (m + \frac12 M)a \Rightarrow a = \frac{mg}{m + M/2} = \frac{20}{4} = 5$ m/s²
- $T = \frac12 (4)(5) = 10$ N

Compare: with a massless pulley the block would be in free fall ($a = g$). The pulley's rotational inertia acts like an extra "effective mass" $I/R^2 = M/2$.

## 5. Rotational Kinetic Energy and Work

Each particle has kinetic energy $\frac12 m_i v_i^2 = \frac12 m_i r_i^2\omega^2$. Summing:
$$\boxed{K_{\text{rot}} = \tfrac12 I\omega^2}$$

Work done by a torque: $W = \int \tau\,d\theta$; power: $P = \tau\omega$. The rotational work–energy theorem: $W_{\text{net}} = \Delta(\frac12 I\omega^2)$.

**Engine example:** a car engine delivering 300 N·m of torque at 4000 rpm produces $P = \tau\omega = 300 \times (2\pi \times 4000/60) \approx 125\,700$ W ≈ 126 kW ≈ 169 hp. This is why horsepower and torque curves are linked: $P = \tau\omega$.

**Flywheels** store energy as rotational kinetic energy. A 100 kg steel disk of radius 0.5 m spinning at 10 000 rpm stores $\frac12(\frac12 \cdot 100 \cdot 0.25)(1047)^2 \approx 6.9$ MJ (about 1.9 kWh).

## 6. Rolling Motion

For an object rolling **without slipping**, the contact point is instantaneously at rest relative to the ground, giving the **rolling constraint**:
$$v_{\text{cm}} = R\omega, \qquad a_{\text{cm}} = R\alpha$$

The motion is a combination of translation of the center of mass and rotation about it. Total kinetic energy:
$$K = \tfrac12 M v_{\text{cm}}^2 + \tfrac12 I_{\text{cm}}\omega^2 = \tfrac12 M v^2\left(1 + \frac{I_{\text{cm}}}{MR^2}\right)$$

Write $I_{\text{cm}} = cMR^2$ ($c = 1$ ring, $\frac12$ disk, $\frac25$ solid sphere, $\frac23$ hollow sphere).

### Race down an incline
Objects released from rest at height $h$ and rolling without slipping:
$$Mgh = \tfrac12 Mv^2(1 + c) \Rightarrow v = \sqrt{\frac{2gh}{1 + c}}$$
and the acceleration along an incline of angle $\theta$ is
$$a = \frac{g\sin\theta}{1 + c}$$

**Result independent of mass and radius!** Order of arrival: solid sphere ($c = 0.4$) first, then solid cylinder ($0.5$), hollow sphere ($0.667$), and the thin ring ($1$) last. A frictionless sliding block ($c = 0$ effectively) beats them all. The more of an object's mass is far from its axis, the more energy goes into rotation and the slower it translates.

**Friction in rolling:** static friction at the contact point is what produces the torque to spin up the object, but it does **no work** in rolling without slipping because the contact point doesn't move. Hence mechanical energy is conserved. (Real rolling resistance from deformation of tire and road is a separate, small effect.)

## 7. Angular Momentum

### Single particle
$$\vec L = \vec r \times \vec p = m\,\vec r \times \vec v$$
For a particle moving in a circle of radius $r$: $L = mvr = mr^2\omega$.

A particle moving in a straight line also has angular momentum about any point not on that line: $L = mvr_\perp$.

### Rigid body about a fixed (symmetry) axis
$$\vec L = I\vec\omega$$

### Second law in angular form
$$\boxed{\vec\tau_{\text{net}} = \frac{d\vec L}{dt}}$$

### Conservation of angular momentum
If the net external torque on a system is zero, its total angular momentum is constant:
$$\vec\tau_{\text{ext}} = 0 \Rightarrow \vec L = \text{constant}, \qquad I_1\omega_1 = I_2\omega_2$$

This follows from the isotropy of space (rotational symmetry) via Noether's theorem.

**Examples:**
- **Figure skater:** pulling in the arms reduces $I$, so $\omega$ increases. Rotational kinetic energy $K = L^2/(2I)$ *increases* — the skater does work pulling the arms inward against the centrifugal tendency.
- **Diver/gymnast:** tucking increases spin rate for somersaults; extending slows it for entry.
- **Collapsing stars:** since $I \propto R^2$, shrinking an object's radius by a factor $k$ multiplies its spin rate by $k^2$. When a stellar core about the size of Earth (~$10^4$ km across) collapses to a ~20 km neutron star, $k \sim 500$ and the spin rate rises by a factor of ~$2.5 \times 10^5$: a core rotating once every hour or so ends up spinning tens to hundreds of times per second. This explains why newborn neutron stars are seen as rapidly rotating pulsars.
- **Kepler's second law** (equal areas in equal times) is conservation of angular momentum for a planet under a central force.
- **Cats righting themselves** while falling exploit changes in body shape while keeping total $L = 0$.
- **Helicopters** need a tail rotor to counter the torque on the body from spinning the main rotor.

### Worked example 7.1 – Merry-go-round
**Problem:** A child of mass $30$ kg runs at $4$ m/s tangentially and jumps onto the rim of a stationary merry-go-round (solid disk, $M = 120$ kg, $R = 2$ m). Find the final angular velocity and the fraction of kinetic energy lost.

**Solution:** Angular momentum about the axle is conserved (the axle exerts forces but no torque about itself).
$L_i = mvR = 30 \times 4 \times 2 = 240$ kg·m²/s.
$I_f = \frac12 MR^2 + mR^2 = 240 + 120 = 360$ kg·m².
$\omega_f = 240/360 = 0.667$ rad/s.
$K_i = \frac12 (30)(16) = 240$ J; $K_f = \frac12(360)(0.667)^2 = 80$ J. Two-thirds of the kinetic energy is lost — this is a rotational perfectly inelastic collision.

## 8. Static Equilibrium

A rigid body is in static equilibrium when it has no linear or angular acceleration. Two conditions:
$$\sum \vec F = 0 \qquad \text{and} \qquad \sum \vec\tau = 0 \;\text{(about ANY point)}$$

**Tip:** choose the pivot point for torques at the location of an unknown force to eliminate it from the torque equation.

### Worked example 8.1 – Ladder against a wall
**Problem:** A uniform $5$ m ladder of mass $20$ kg leans against a frictionless wall, making $60°$ with the floor. What minimum coefficient of static friction with the floor prevents slipping? ($g = 10$ m/s²)

**Solution:** Forces: weight $W = 200$ N at the midpoint; wall normal force $N_w$ (horizontal); floor normal force $N_f$ (vertical); floor friction $f$ (horizontal, toward the wall).
- Vertical: $N_f = 200$ N
- Horizontal: $f = N_w$
- Torques about the foot of the ladder: the weight's lever arm is $(L/2)\cos 60°$; the wall force's lever arm is $L\sin 60°$.
  $N_w L\sin 60° = W (L/2)\cos 60° \Rightarrow N_w = \frac{W}{2\tan 60°} = \frac{200}{2 \times 1.732} \approx 57.7$ N
- $\mu_s \ge f/N_f = 57.7/200 \approx 0.29$

The steeper the ladder (larger angle), the less friction it needs — which is why ladder safety guidelines recommend about 75°.

### Worked example 8.2 – Seesaw
A $30$ kg child sits $2$ m from the pivot of a seesaw. Where must a $40$ kg child sit on the other side to balance? $30 \times 2 = 40 \times d \Rightarrow d = 1.5$ m.

### Center of gravity and stability
An object resting on a base is stable if a vertical line through its center of gravity falls within its base of support. A lower center of gravity and wider base increase stability — the principle behind racing car design, the wide stance of wrestlers, and why SUVs are more prone to rollover than sedans.

## 9. Gyroscopes and Precession

When a torque acts perpendicular to a spinning object's angular momentum, it changes the *direction* of $\vec L$ rather than its magnitude. A spinning top or gyroscope supported at one end does not fall; instead its axis sweeps around a vertical cone — **precession**.

For a gyroscope with spin angular momentum $L = I\omega$, supported at a distance $r$ from its center of mass, gravity exerts torque $\tau = Mgr$, and the precession angular velocity is
$$\Omega = \frac{\tau}{L} = \frac{Mgr}{I\omega}$$
The faster it spins, the slower it precesses.

Applications and examples:
- **Gyrocompasses and inertial navigation** in ships, aircraft and spacecraft.
- **Bicycle stability** (partly gyroscopic, mostly from steering geometry).
- **Precession of Earth's axis:** the Sun's and Moon's gravitational torques on Earth's equatorial bulge make Earth's axis precess with a period of about 25 800 years ("precession of the equinoxes"). Polaris will not always be the North Star; in about 12 000 years Vega will be near the pole.
- **Nuclear magnetic resonance (NMR/MRI):** nuclear magnetic moments precess in a magnetic field at the Larmor frequency.

## 10. The Linear–Rotational Dictionary

| Linear | Rotational | Relation |
|---|---|---|
| Position $x$ | Angle $\theta$ | $s = r\theta$ |
| Velocity $v$ | Angular velocity $\omega$ | $v = r\omega$ |
| Acceleration $a$ | Angular acceleration $\alpha$ | $a_t = r\alpha$ |
| Mass $m$ | Moment of inertia $I$ | $I = \sum mr^2$ |
| Force $F$ | Torque $\tau$ | $\vec\tau = \vec r\times\vec F$ |
| $F = ma$ | $\tau = I\alpha$ | |
| Momentum $p = mv$ | Angular momentum $L = I\omega$ | $\vec L = \vec r\times\vec p$ |
| $F = dp/dt$ | $\tau = dL/dt$ | |
| $K = \frac12mv^2$ | $K = \frac12I\omega^2$ | |
| Work $\int F\,dx$ | Work $\int\tau\,d\theta$ | |
| Power $Fv$ | Power $\tau\omega$ | |
