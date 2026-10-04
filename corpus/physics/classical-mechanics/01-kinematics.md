---
title: Kinematics - The Mathematical Description of Motion
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [position, displacement, velocity, speed, acceleration, constant acceleration, free fall, projectile motion, uniform circular motion, relative motion]
---

# Kinematics: The Mathematical Description of Motion

Kinematics is the branch of mechanics that describes how objects move **without asking why** they move. The question "why does this object speed up?" belongs to dynamics (Newton's laws). Kinematics only asks: where is the object, how fast is it going, and how is its velocity changing? The language of kinematics is position, displacement, velocity and acceleration, and the relationships among them are expressed with the derivative and the integral of calculus.

## 1. Reference Frames and Coordinates

To describe motion we first choose a **reference frame**: an origin, a set of mutually perpendicular axes (usually $x$, $y$, $z$) and a clock. Motion is always described *relative to something*. A passenger sitting in a moving train is at rest relative to the train but moving relative to the ground.

- **One-dimensional motion:** position is a single number, $x(t)$.
- **Two- or three-dimensional motion:** position is a vector, $\vec r(t) = x(t)\,\hat i + y(t)\,\hat j + z(t)\,\hat k$.

Here $\hat i, \hat j, \hat k$ are unit vectors along the $x$, $y$ and $z$ axes.

### Scalars and vectors

| Type | Definition | Examples |
|---|---|---|
| Scalar | Has magnitude only (number + unit) | Mass, time, speed, distance traveled, energy, temperature |
| Vector | Has magnitude and direction | Position, displacement, velocity, acceleration, force, momentum |

Vectors add with direction taken into account, using the tip-to-tail (triangle) rule or the parallelogram rule. In components, addition is done component by component:
$$\vec A + \vec B = (A_x + B_x)\,\hat i + (A_y + B_y)\,\hat j + (A_z + B_z)\,\hat k$$

The magnitude of a vector is $|\vec A| = \sqrt{A_x^2 + A_y^2 + A_z^2}$.

## 2. Position, Displacement and Distance

**Displacement** is the change in position:
$$\Delta \vec r = \vec r_{\text{final}} - \vec r_{\text{initial}}$$

Displacement is a vector and depends only on the start and end points, not on the path taken.

**Distance traveled** is the length of the actual path and is a scalar. A runner who completes one lap of a 400 m track has traveled 400 m, but their displacement is zero.

> **Misconception:** "The magnitude of displacement equals the distance traveled" is true only for motion along a straight line without reversing direction. In general $|\Delta \vec r| \le$ distance traveled.

## 3. Velocity and Speed

### Average velocity and average speed

$$\vec v_{\text{avg}} = \frac{\Delta \vec r}{\Delta t} \qquad\qquad \text{average speed} = \frac{\text{distance traveled}}{\Delta t}$$

Average velocity is a vector pointing along the displacement; average speed is a scalar. If the runner above finishes the lap in 50 s, their average speed is $400/50 = 8$ m/s while their average velocity is $0$.

### Instantaneous velocity

Letting the time interval shrink to zero turns the average velocity into the **instantaneous velocity**:
$$\vec v(t) = \lim_{\Delta t \to 0} \frac{\Delta \vec r}{\Delta t} = \frac{d\vec r}{dt}$$

The instantaneous velocity is always **tangent to the path**. Its magnitude is the **instantaneous speed**, $v = |\vec v|$.

Graphical meaning: on a position–time ($x$–$t$) graph, the slope of the tangent line at a point is the velocity at that instant. The slope of a chord (secant) between two points is the average velocity over that interval.

**SI unit:** m/s. Also common: km/h, with $1 \text{ m/s} = 3.6 \text{ km/h}$; for example $72$ km/h $= 20$ m/s. In the US, $1 \text{ mph} \approx 0.447$ m/s.

## 4. Acceleration

Acceleration is the rate of change of velocity:
$$\vec a_{\text{avg}} = \frac{\Delta \vec v}{\Delta t}, \qquad \vec a(t) = \frac{d\vec v}{dt} = \frac{d^2 \vec r}{dt^2}$$

**SI unit:** m/s².

Key points:
1. An object accelerates whenever the **magnitude** *or* the **direction** of its velocity changes. A car rounding a curve at constant speed is accelerating.
2. If acceleration and velocity point the same way the object speeds up; if they point opposite ways it slows down. "Negative acceleration means slowing down" is **wrong** in general: the sign depends on the chosen axis. An object moving in the negative direction with negative acceleration is actually speeding up.
3. On a velocity–time ($v$–$t$) graph, the slope is the acceleration and the signed area under the curve is the displacement.
4. On an acceleration–time ($a$–$t$) graph, the area under the curve is the change in velocity $\Delta v$.

### Derivative and integral relationships

$$x(t) \xrightarrow{\;d/dt\;} v(t) \xrightarrow{\;d/dt\;} a(t)$$
$$v(t) = v_0 + \int_0^t a(t')\,dt', \qquad x(t) = x_0 + \int_0^t v(t')\,dt'$$

**Example:** An object's position is $x(t) = 2t^3 - 6t^2 + 4$ (meters, $t$ in seconds). Then:
- $v(t) = 6t^2 - 12t$ m/s
- $a(t) = 12t - 12$ m/s²
- The object is momentarily at rest when $v = 0$: $6t(t - 2) = 0 \Rightarrow t = 0$ and $t = 2$ s.
- At $t = 1$ s, $a = 0$; this is when the velocity reaches its most negative value, $v(1) = -6$ m/s.
- Position at $t = 2$ s: $x(2) = 16 - 24 + 4 = -4$ m.

## 5. Motion with Constant Acceleration

When the acceleration is constant the integrals above are easy and give the **kinematic equations**. Let the position and velocity at $t = 0$ be $x_0$ and $v_0$:

$$\boxed{v = v_0 + a t}$$
$$\boxed{x = x_0 + v_0 t + \tfrac{1}{2} a t^2}$$
$$\boxed{v^2 = v_0^2 + 2a(x - x_0)}$$
$$\boxed{x - x_0 = \frac{v_0 + v}{2}\, t}$$

### Derivation

1. Since $a = dv/dt$ is constant, $\int_{v_0}^{v} dv = \int_0^t a\,dt \Rightarrow v = v_0 + at$.
2. Integrating $v = dx/dt = v_0 + at$ gives $x - x_0 = v_0 t + \frac12 a t^2$.
3. From (1), $t = (v - v_0)/a$. Substituting into (2):
   $x - x_0 = v_0 \frac{v - v_0}{a} + \frac12 a \frac{(v - v_0)^2}{a^2} = \frac{v^2 - v_0^2}{2a}$, i.e. $v^2 = v_0^2 + 2a\,\Delta x$.
4. With constant acceleration the velocity changes linearly in time, so the average velocity is the arithmetic mean of the initial and final velocities: $v_{\text{avg}} = (v_0 + v)/2$.

> **Warning:** these equations hold **only for constant acceleration**. If the acceleration varies (air resistance, spring forces, ...) you must integrate directly.

### Worked Example 5.1 – Stopping distance

**Problem:** A car travels at 90 km/h. The driver brakes and the car decelerates uniformly at $6$ m/s². The driver's reaction time is $0.8$ s. How far does the car travel from the moment the driver sees the hazard?

**Solution:**
1. Convert units: $v_0 = 90 \text{ km/h} = 90 / 3.6 = 25$ m/s.
2. During the reaction time the car moves at constant speed: $d_1 = v_0 t_r = 25 \times 0.8 = 20$ m.
3. Braking distance from $v^2 = v_0^2 + 2a\,d_2$ with $v = 0$, $a = -6$ m/s²:
   $0 = 625 - 12\,d_2 \Rightarrow d_2 = 625/12 \approx 52.1$ m.
4. Total: $d = d_1 + d_2 \approx 72.1$ m.

**Interpretation:** braking distance scales with the **square** of speed. Doubling the speed (180 km/h) quadruples the braking distance (≈208 m). This is a key reason speed limits matter for safety.

### Worked Example 5.2 – Catch-up problem

**Problem:** A car moving at a constant $30$ m/s passes a stationary police car. At that instant the police car starts accelerating uniformly at $3$ m/s². When and where does it catch the speeder?

**Solution:** Measure both positions from the same origin:
- Speeder: $x_1 = 30t$
- Police: $x_2 = \frac12 (3) t^2 = 1.5 t^2$

At catch-up $x_1 = x_2$: $30t = 1.5t^2 \Rightarrow t(1.5t - 30) = 0 \Rightarrow t = 20$ s (the root $t = 0$ is the start).
Position: $x = 30 \times 20 = 600$ m. The police car's speed then is $3 \times 20 = 60$ m/s — exactly twice the speeder's. This is general: an object starting from rest with constant acceleration that catches a constant-velocity object always has twice its speed at that moment, because both cover the same distance in the same time, so their average velocities are equal, and $v_{\text{avg}} = (0 + v)/2$.

## 6. Free Fall

Neglecting air resistance, all objects near Earth's surface fall with the same acceleration regardless of their mass. This is the **acceleration due to gravity** $g$:
$$g \approx 9.81 \text{ m/s}^2 \;(\text{often rounded to } 10 \text{ m/s}^2 \text{ in problems})$$

Galileo Galilei, through inclined-plane experiments in the early 17th century, showed that Aristotle's claim that "heavier objects fall faster" is false. In 1971, Apollo 15 astronaut David Scott dropped a hammer and a feather together on the airless Moon and they hit the ground at the same time.

Taking upward as positive, $a = -g$ and:
$$v = v_0 - g t, \qquad y = y_0 + v_0 t - \tfrac12 g t^2, \qquad v^2 = v_0^2 - 2g(y - y_0)$$

**Key results for a vertical upward throw ($v_0 > 0$):**
- Time to reach the top: $t_{\text{top}} = v_0 / g$
- Maximum height: $h_{\max} = v_0^2 / (2g)$
- The object returns to launch height after $2v_0/g$ with the same speed it was thrown with (opposite direction).
- At the top the velocity is zero but **the acceleration is not**; it is still $g$, downward. This is one of the most common misconceptions.

### Worked Example 6.1

**Problem:** A stone is released from the top of a $45$ m building ($g = 10$ m/s²). (a) How long does it take to hit the ground? (b) What is its impact speed?

**Solution:**
(a) $h = \frac12 g t^2 \Rightarrow 45 = 5t^2 \Rightarrow t = 3$ s.
(b) $v = g t = 30$ m/s (or $v = \sqrt{2gh} = \sqrt{900} = 30$ m/s).

### Air resistance and terminal velocity

In reality air exerts a drag force opposite to the motion. At high speeds drag is approximately $F_d = \frac12 C_d \rho A v^2$ ($C_d$: drag coefficient, $\rho$: air density, $A$: cross-sectional area). As speed increases, drag grows until it equals the weight; then the acceleration vanishes and the object keeps falling at **terminal velocity**:
$$v_t = \sqrt{\frac{2mg}{C_d \rho A}}$$

A skydiver in the belly-down position reaches about 55 m/s (≈200 km/h); opening the parachute greatly increases $A$ and $C_d$ and lowers the terminal speed to about 5 m/s.

## 7. Two-Dimensional Motion and Projectiles

The most powerful idea in 2D motion: **motions along perpendicular directions are independent.** We analyze horizontal and vertical motion separately and connect them through time.

### Horizontal launch

An object launched horizontally with speed $v_0$ from height $h$:
- Horizontal: no acceleration, $x = v_0 t$
- Vertical: free fall, $y = h - \frac12 g t^2$
- Flight time: $t_f = \sqrt{2h/g}$ (independent of the horizontal speed!)
- Range: $R = v_0 \sqrt{2h/g}$

A ball fired horizontally and a ball dropped from the same height at the same time hit the ground **simultaneously**.

### Oblique launch (ground to ground)

Launched from the ground with speed $v_0$ at angle $\theta$ above the horizontal, the initial velocity components are:
$$v_{0x} = v_0 \cos\theta, \qquad v_{0y} = v_0 \sin\theta$$

Equations of motion:
$$x(t) = v_0 \cos\theta \; t$$
$$y(t) = v_0 \sin\theta \; t - \tfrac12 g t^2$$
$$v_x = v_0\cos\theta \;(\text{constant}), \qquad v_y = v_0 \sin\theta - g t$$

Eliminating $t$, the trajectory is a **parabola**:
$$y = x\tan\theta - \frac{g}{2 v_0^2 \cos^2\theta}\, x^2$$

Derived results:

| Quantity | Formula |
|---|---|
| Time to peak | $t_{\text{peak}} = \dfrac{v_0 \sin\theta}{g}$ |
| Total flight time | $T = \dfrac{2 v_0 \sin\theta}{g}$ |
| Maximum height | $H = \dfrac{v_0^2 \sin^2\theta}{2g}$ |
| Range | $R = \dfrac{v_0^2 \sin 2\theta}{g}$ |

The range follows from $R = v_0 \cos\theta \cdot T = \frac{2 v_0^2 \sin\theta\cos\theta}{g}$ and the identity $\sin 2\theta = 2\sin\theta\cos\theta$.

**Consequences:**
- The range is maximal when $\sin 2\theta = 1$, i.e. $\theta = 45°$: $R_{\max} = v_0^2/g$.
- Complementary angles (e.g. $30°$ and $60°$) give the same range, because $\sin(2\theta) = \sin(180° - 2\theta)$.
- At the peak the vertical velocity is zero but the horizontal velocity is still $v_0\cos\theta$, so the speed is not zero.
- With air resistance the optimal angle is less than $45°$ and the trajectory is not symmetric.

### Worked Example 7.1

**Problem:** A soccer player kicks a ball from the ground at $20$ m/s, $37°$ above the horizontal ($\sin 37° = 0.6$, $\cos 37° = 0.8$, $g = 10$ m/s²). Find (a) the flight time, (b) the maximum height, (c) the range.

**Solution:** $v_{0x} = 20 \times 0.8 = 16$ m/s, $v_{0y} = 20 \times 0.6 = 12$ m/s.
(a) $T = 2 v_{0y}/g = 24/10 = 2.4$ s.
(b) $H = v_{0y}^2/(2g) = 144/20 = 7.2$ m.
(c) $R = v_{0x} T = 16 \times 2.4 = 38.4$ m.

Check: $R = v_0^2 \sin 2\theta / g = 400 \times (2 \times 0.6 \times 0.8)/10 = 400 \times 0.96/10 = 38.4$ m. ✓

## 8. Uniform Circular Motion

An object moving around a circle of radius $r$ at constant speed is in **uniform circular motion**.

- **Period ($T$):** time for one revolution (s).
- **Frequency ($f$):** revolutions per unit time, $f = 1/T$ (Hz = s⁻¹).
- **Angular velocity ($\omega$):** angle swept per unit time, $\omega = \frac{d\theta}{dt} = \frac{2\pi}{T} = 2\pi f$ (rad/s).
- **Linear (tangential) speed:** $v = \frac{2\pi r}{T} = \omega r$.

Although the speed is constant, the direction changes continuously, so the object accelerates. This acceleration always points toward the center and is called **centripetal acceleration**:
$$a_c = \frac{v^2}{r} = \omega^2 r$$

### Derivation of centripetal acceleration

Let $\vec r(t) = r\cos(\omega t)\,\hat i + r\sin(\omega t)\,\hat j$. Then
$$\vec v = \frac{d\vec r}{dt} = -r\omega\sin(\omega t)\,\hat i + r\omega\cos(\omega t)\,\hat j$$
$$\vec a = \frac{d\vec v}{dt} = -r\omega^2\cos(\omega t)\,\hat i - r\omega^2\sin(\omega t)\,\hat j = -\omega^2\,\vec r$$

The minus sign shows that the acceleration points opposite to the position vector, i.e. toward the center. Its magnitude is $\omega^2 r = v^2/r$.

### Non-uniform circular motion

If the speed also changes, the acceleration has two components:
- **Tangential acceleration:** $a_t = \frac{dv}{dt}$ (change in speed)
- **Centripetal (normal) acceleration:** $a_c = v^2/r$ (change in direction)
- Total: $a = \sqrt{a_t^2 + a_c^2}$

Angular acceleration is $\alpha = d\omega/dt$, and $a_t = \alpha r$. For constant angular acceleration, equations exactly analogous to linear motion hold:
$$\omega = \omega_0 + \alpha t, \quad \theta = \theta_0 + \omega_0 t + \tfrac12 \alpha t^2, \quad \omega^2 = \omega_0^2 + 2\alpha(\theta - \theta_0)$$

### Worked Example 8.1

**Problem:** Approximate the Moon's orbit as a circle of radius $r = 3.84 \times 10^8$ m with period $T = 27.3$ days. Find the Moon's centripetal acceleration.

**Solution:** $T = 27.3 \times 86400 \approx 2.36 \times 10^6$ s.
$\omega = 2\pi / T \approx 2.66 \times 10^{-6}$ rad/s.
$a_c = \omega^2 r \approx (2.66\times10^{-6})^2 \times 3.84\times10^8 \approx 2.72 \times 10^{-3}$ m/s².

**Historical note:** Newton did essentially this calculation and noticed $g / a_c \approx 9.8 / 0.00272 \approx 3600 = 60^2$. The Moon is about 60 Earth radii from Earth's center. This showed that gravity weakens with the inverse square of distance and that the force that makes an apple fall is **the same** force that keeps the Moon in orbit (the "Moon test").

## 9. Relative Motion

The velocity of object A relative to observer B is
$$\vec v_{A/B} = \vec v_{A} - \vec v_{B}$$
where both velocities are measured in a common frame (e.g. the ground). More generally velocities chain together:
$$\vec v_{A/C} = \vec v_{A/B} + \vec v_{B/C}$$

This is a consequence of the **Galilean transformation** and holds for speeds much less than the speed of light. Near light speed, Einstein's relativistic velocity-addition formula must be used.

### Worked Example 9.1 – River crossing

**Problem:** A river is $120$ m wide and flows at $3$ m/s relative to the ground. A boat moves at $5$ m/s relative to the water.
(a) If the boat points straight across, how long does the crossing take and how far downstream does it drift?
(b) At what heading must it point to land directly opposite, and how long does that take?

**Solution:**
(a) The cross-stream component is $5$ m/s, so $t = 120/5 = 24$ s. Meanwhile the current carries it $3 \times 24 = 72$ m downstream. Its ground speed is $\sqrt{5^2 + 3^2} = \sqrt{34} \approx 5.83$ m/s.
(b) The upstream component of the boat's water-relative velocity must cancel the current: $5\sin\phi = 3 \Rightarrow \sin\phi = 0.6 \Rightarrow \phi \approx 36.9°$ upstream from the perpendicular. The cross-stream component is $5\cos\phi = 4$ m/s, so $t = 120/4 = 30$ s.

**Interpretation:** crossing in the shortest *time* (a) and crossing along the shortest *path* (b) are different strategies. If the boat's speed relative to the water is less than the current speed, landing directly opposite is impossible.

## 10. Summary Table

| Concept | Definition / Formula | Unit |
|---|---|---|
| Displacement | $\Delta\vec r = \vec r_2 - \vec r_1$ | m |
| Instantaneous velocity | $\vec v = d\vec r/dt$ | m/s |
| Instantaneous acceleration | $\vec a = d\vec v/dt$ | m/s² |
| Constant acceleration | $v = v_0 + at$; $x = x_0 + v_0t + \frac12at^2$; $v^2 = v_0^2 + 2a\Delta x$ | — |
| Free fall | $a = g \approx 9.81$ m/s² (down) | m/s² |
| Projectile range | $R = v_0^2\sin 2\theta/g$ | m |
| Maximum height | $H = v_0^2\sin^2\theta/(2g)$ | m |
| Centripetal acceleration | $a_c = v^2/r = \omega^2 r$ | m/s² |
| Angular velocity | $\omega = 2\pi/T = 2\pi f$ | rad/s |
| Relative velocity | $\vec v_{A/B} = \vec v_A - \vec v_B$ | m/s |

## 11. Common Mistakes

1. **Assuming zero velocity means zero acceleration.** A ball thrown upward is momentarily at rest at the top, but its acceleration is $g$.
2. **Using constant-acceleration equations when acceleration varies.**
3. **Forgetting unit conversions** (km/h ↔ m/s, minutes ↔ seconds).
4. **Mixing sign conventions:** pick one positive direction and sign every vector (position, velocity, acceleration) consistently.
5. **Thinking the horizontal velocity of a projectile changes.** Without air resistance it is constant.
6. **Confusing speed and velocity.** An object circling at constant speed does not have constant velocity.
7. **Believing heavier objects fall faster.** In vacuum all objects fall with the same acceleration; in air, the difference comes from the ratio of drag to weight.
