---
title: Newton's Laws of Motion and Dynamics
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [Newton, inertia, force, mass, F=ma, action-reaction, friction, normal force, tension, inclined plane, pulley, Atwood machine, free-body diagram, inertial reference frame, rocket equation]
---

# Newton's Laws of Motion and Dynamics

Isaac Newton (1643–1727) set out his three laws of motion and the law of universal gravitation in the *Philosophiæ Naturalis Principia Mathematica* (Mathematical Principles of Natural Philosophy), published in 1687. These laws unified Galileo's work on inertia, Kepler's laws of planetary motion and ideas from Descartes into a single coherent framework. **Newtonian (classical) mechanics** remains extraordinarily accurate for objects moving slowly compared with light and much larger than atoms; it underlies everything from bridge design to satellite orbits.

Kinematics describes motion; **dynamics** studies its *causes* — forces.

## 1. Basic Concepts

### Force
A force is an interaction that can change an object's state of motion (its velocity) or deform it. Force is a vector. Its SI unit is the **newton** (N):
$$1 \text{ N} = 1 \text{ kg}\cdot\text{m/s}^2$$
One newton gives a 1 kg mass an acceleration of 1 m/s². A typical apple weighs about 1 N.

### Mass
Mass measures an object's **inertia** — its resistance to changes in velocity. It is a scalar with SI unit the kilogram (kg). Mass does not depend on location; it is the same on the Moon as on Earth.

### Weight
Weight is the gravitational force on an object: $\vec W = m\vec g$. Weight is a force and depends on location. A person of mass 60 kg weighs about $60 \times 9.81 \approx 589$ N on Earth and about $97$ N on the Moon ($g_{\text{Moon}} \approx 1.62$ m/s²).

> **Misconception:** in everyday speech people say "I weigh 60 kg", but scientifically 60 kg is a mass, not a weight. Bathroom scales actually measure a force (the normal force) and divide by $g$ to display mass.

### Net force
If several forces act on an object, their vector sum is the **net (resultant) force**:
$$\vec F_{\text{net}} = \sum_i \vec F_i$$

## 2. Newton's First Law: The Law of Inertia

> *An object with zero net force acting on it remains at rest if it is at rest, or continues moving in a straight line at constant speed if it is moving.*

$$\vec F_{\text{net}} = 0 \iff \vec v = \text{constant}$$

### Explanation and history
Aristotle believed a continuous force was needed to keep an object moving, because in everyday life objects stop when we stop pushing them. Galileo realized that objects stop because of **friction**: the smaller the friction, the longer the object keeps moving. With no friction at all it would move forever at constant velocity. Newton turned this idea into a general law.

### Inertial reference frames
The first law effectively **defines inertial reference frames**: frames in which the first law holds are inertial. Any frame moving at constant velocity relative to an inertial frame is also inertial. Accelerating frames (a braking bus, a spinning merry-go-round) are non-inertial; in them objects appear to accelerate "on their own". When a bus brakes suddenly, passengers lurch forward. In reality the passengers keep moving at constant velocity (inertia); it is the bus that slows down.

Earth's surface is not exactly inertial because Earth rotates, but for most everyday problems it is approximately inertial. The effects of rotation appear in phenomena such as the Foucault pendulum and the Coriolis effect.

### Everyday examples
- Yanking a tablecloth quickly leaves the dishes nearly in place.
- Seat belts save lives in sudden stops.
- A wet dog shaking itself: the fur reverses direction, but the water droplets continue straight and fly off.
- A space probe coasting with engines off continues at constant velocity (the Voyager probes are examples).

## 3. Newton's Second Law: The Fundamental Law of Dynamics

> *The acceleration of an object is directly proportional to the net force acting on it, inversely proportional to its mass, and in the direction of the net force.*

$$\boxed{\vec F_{\text{net}} = m\,\vec a}$$

In its more general form (closer to Newton's original), the net force equals the rate of change of momentum:
$$\vec F_{\text{net}} = \frac{d\vec p}{dt}, \qquad \vec p = m\vec v$$

If the mass is constant, $\frac{d(m\vec v)}{dt} = m\frac{d\vec v}{dt} = m\vec a$. For systems with changing mass (rockets, a leaking bucket) the momentum form, applied carefully to the whole system, must be used.

### Component form
The second law is a vector equation; it is written separately for each axis:
$$\sum F_x = m a_x, \qquad \sum F_y = m a_y, \qquad \sum F_z = m a_z$$

### Important interpretations
1. **Force produces acceleration, not velocity.** An object need not move in the direction of the force; in projectile motion the force (weight) points down while the object may be moving up and forward.
2. **Inertial mass:** the $m$ in the second law is inertial mass. Experiments show it equals the "gravitational mass" in the law of gravitation to better than one part in $10^{15}$. This equality (the equivalence principle) is a foundation of Einstein's general relativity.
3. Although the first law looks like a special case of the second, it has independent importance because it defines the inertial frames in which the second law holds.

## 4. Newton's Third Law: Action and Reaction

> *If object A exerts a force on object B, then B exerts a force on A that is equal in magnitude and opposite in direction.*

$$\vec F_{A \to B} = -\vec F_{B \to A}$$

### Critical points
- Action and reaction forces act on **different objects**. Therefore they **never cancel each other**. (Forces that balance act on the same object.)
- An action–reaction pair is always the **same type** of force (both gravitational, both contact forces, etc.).
- They arise and vanish simultaneously.

### Classic example: a book on a table
Two forces act on a book resting on a table: Earth's gravitational pull on the book ($\vec W$) and the table's normal force on the book ($\vec N$). Since the book is in equilibrium, $N = W$. **But these are not an action–reaction pair!** Both act on the same object (the book) and they are different types of force.
- Reaction to the weight: the book pulling **Earth** upward.
- Reaction to the normal force: the book pushing **down on the table**.

### The horse-and-cart paradox
"If the cart pulls back on the horse as hard as the horse pulls on the cart, how can they move?" Answer: the horse's motion is determined by the forces acting *on the horse*. The horse pushes backward on the ground with its hooves; by the third law the ground pushes the horse forward. If this friction force exceeds the cart's backward pull on the horse, the horse (and cart) accelerate forward. To analyze motion, consider the forces on each object separately.

### More examples
- Rockets push exhaust gases backward; the gases push the rocket forward. A rocket does not need air to push against and works in the vacuum of space.
- A swimmer pushes water backward; the water pushes the swimmer forward.
- The recoil of a fired rifle.

## 5. Common Forces in Mechanics

### 5.1 Weight (gravitational force)
$\vec W = m\vec g$, directed toward Earth's center (locally "down").

### 5.2 Normal force ($\vec N$)
The contact force a surface exerts on an object, **perpendicular** to the surface. The normal force is NOT always equal to the weight! Its value follows from the second law applied perpendicular to the surface.
- Object resting on a horizontal surface: $N = mg$
- On a frictionless incline of angle $\theta$: $N = mg\cos\theta$
- In an elevator accelerating upward at $a$: $N = m(g + a)$
- In an elevator accelerating downward at $a$: $N = m(g - a)$
- In a freely falling elevator ($a = g$): $N = 0$ → **apparent weightlessness**

### 5.3 Tension ($\vec T$)
The pulling force exerted by a string, rope or cable; it always acts along the rope, pulling away from the object. In an ideal (massless, inextensible) rope passing over a massless, frictionless pulley, the tension is the same everywhere along the rope.

### 5.4 Friction ($\vec f$)
The force between surfaces in contact that opposes relative motion or the tendency toward relative motion. Microscopically it arises from surface roughness and electromagnetic interactions between atoms.

**Static friction** acts when the object is not sliding. It takes whatever value is needed to prevent motion, up to a maximum:
$$f_s \le \mu_s N$$

**Kinetic friction** acts while sliding and is approximately constant:
$$f_k = \mu_k N$$

$\mu_s$ and $\mu_k$ are the static and kinetic coefficients of friction. Usually $\mu_k < \mu_s$, which is why getting an object moving is harder than keeping it moving.

| Surfaces | $\mu_s$ (approx.) | $\mu_k$ (approx.) |
|---|---|---|
| Rubber on dry asphalt | 1.0 | 0.8 |
| Rubber on wet asphalt | 0.7 | 0.5 |
| Steel on steel (dry) | 0.7 | 0.6 |
| Wood on wood | 0.25–0.5 | 0.2 |
| Ice on ice | 0.1 | 0.03 |
| Teflon on Teflon | 0.04 | 0.04 |
| Synovial joint | 0.01 | 0.003 |

**Friction is (approximately) independent of the apparent contact area** (Amontons' laws). This is surprising at first: the true microscopic contact area is proportional to the normal force, not to the apparent area.

**Why anti-lock brakes (ABS) work:** while a wheel rolls without slipping, tire–road friction is static ($\mu_s > \mu_k$). If the wheels lock and skid, friction becomes kinetic and drops, and steering control is lost. ABS prevents locking and keeps friction static.

### 5.5 Spring force (Hooke's law)
An ideal spring stretched or compressed by $x$ from equilibrium exerts a restoring force opposite to the deformation:
$$F = -kx$$
$k$ is the spring constant (N/m). Hooke's law holds only within the elastic limit.

### 5.6 Fluid resistance (drag)
A velocity-dependent force. At low speeds $F \propto v$ (Stokes drag, small particles); at high speeds $F \propto v^2$.

## 6. Problem-Solving Method: The Free-Body Diagram

The most reliable way to solve dynamics problems is systematic:

1. **Choose the system:** decide which object's motion you are analyzing.
2. **Draw a free-body diagram (FBD):** represent the object as a point and draw arrows for **all external forces acting on it** (and only those). Do not draw forces the object exerts on other things.
3. **Choose axes:** aligning one axis with the acceleration simplifies the algebra (e.g. on an incline, take axes parallel and perpendicular to the surface).
4. **Resolve forces into components.**
5. **Write the second law for each axis:** $\sum F_x = m a_x$, $\sum F_y = m a_y$.
6. **Add constraints:** objects connected by an inextensible rope share the same acceleration magnitude; an object staying on a surface has zero perpendicular acceleration, etc.
7. **Solve and check:** are the units consistent? Do limiting cases make sense (e.g. $\theta \to 0$ or $m \to \infty$)?

## 7. Worked Examples

### Example 7.1 – Horizontal surface with friction
**Problem:** A $10$ kg crate on a horizontal floor ($\mu_k = 0.3$) is pulled by a $60$ N force directed $37°$ above the horizontal. Find its acceleration. ($g = 10$ m/s², $\sin 37° = 0.6$, $\cos 37° = 0.8$)

**Solution:**
Forces: applied force $F$ (components $F_x = 48$ N, $F_y = 36$ N), weight $W = 100$ N (down), normal force $N$ (up), kinetic friction $f_k$ (backward).

Vertical equilibrium ($a_y = 0$): $N + F_y - W = 0 \Rightarrow N = 100 - 36 = 64$ N.
Note: because the force pulls partly upward, the normal force is less than the weight.

Friction: $f_k = \mu_k N = 0.3 \times 64 = 19.2$ N.

Horizontal: $F_x - f_k = m a \Rightarrow 48 - 19.2 = 10a \Rightarrow a = 2.88$ m/s².

### Example 7.2 – Frictionless incline
**Problem:** What is the acceleration of a block released on a frictionless incline of angle $\theta$?

**Solution:** Take $x$ along the incline (down-slope positive) and $y$ perpendicular to it. The components of the weight are $mg\sin\theta$ along the incline and $mg\cos\theta$ perpendicular to it.
- $y$: $N - mg\cos\theta = 0 \Rightarrow N = mg\cos\theta$
- $x$: $mg\sin\theta = ma \Rightarrow \boxed{a = g\sin\theta}$

The result is independent of mass. Limit checks: $\theta = 0$ (flat) → $a = 0$ ✓; $\theta = 90°$ (vertical) → $a = g$ (free fall) ✓.

### Example 7.3 – Incline with friction and the angle of repose
**Problem:** The angle of an incline with static friction coefficient $\mu_s$ is slowly increased. At what angle does a block begin to slide?

**Solution:** At the threshold, static friction is at its maximum:
$mg\sin\theta_c = \mu_s\, mg\cos\theta_c \Rightarrow \boxed{\tan\theta_c = \mu_s}$

This gives a simple experimental way to measure $\mu_s$: if the block starts to slide at $\theta_c = 30°$, then $\mu_s = \tan 30° \approx 0.577$.

Once sliding, the acceleration is $a = g(\sin\theta - \mu_k\cos\theta)$.

### Example 7.4 – The Atwood machine
**Problem:** Masses $m_1$ and $m_2$ ($m_2 > m_1$) hang from the ends of a massless, inextensible string over a massless, frictionless pulley. Find the acceleration and the tension.

**Solution:** $m_2$ moves down and $m_1$ moves up with acceleration $a$. Writing the second law for each (direction of motion positive):
- $m_1$: $T - m_1 g = m_1 a$
- $m_2$: $m_2 g - T = m_2 a$

Adding: $(m_2 - m_1) g = (m_1 + m_2) a$
$$\boxed{a = \frac{m_2 - m_1}{m_1 + m_2}\, g}, \qquad \boxed{T = \frac{2 m_1 m_2}{m_1 + m_2}\, g}$$

Numerical example: $m_1 = 3$ kg, $m_2 = 5$ kg, $g = 10$ m/s² → $a = (2/8) \times 10 = 2.5$ m/s², $T = (2 \times 15 / 8) \times 10 = 37.5$ N.

Check: $T$ must be greater than $m_1 g = 30$ N ($m_1$ accelerates up) and less than $m_2 g = 50$ N ($m_2$ accelerates down). ✓

**Historical note:** George Atwood designed this device in 1784 to "slow down" gravity, making it possible to verify the laws of uniformly accelerated motion at a time when measuring $g$ directly was difficult.

### Example 7.5 – Block on a table and a hanging mass
**Problem:** A $m_1 = 4$ kg block on a horizontal table ($\mu_k = 0.2$) is connected by a string over a pulley at the table's edge to a hanging mass $m_2 = 2$ kg. Find the acceleration and tension. ($g = 10$ m/s²)

**Solution:**
- $m_1$ (horizontal): $T - \mu_k m_1 g = m_1 a \Rightarrow T - 8 = 4a$
- $m_2$ (vertical): $m_2 g - T = m_2 a \Rightarrow 20 - T = 2a$

Adding: $12 = 6a \Rightarrow a = 2$ m/s², $T = 8 + 8 = 16$ N.

### Example 7.6 – A scale in an elevator
**Problem:** A $70$ kg person stands on a bathroom scale in an elevator. What does the scale read (in N) when (a) the elevator moves up at constant speed, (b) it accelerates upward at $2$ m/s², (c) it moves upward while slowing at $2$ m/s², (d) the cable snaps? ($g = 10$ m/s²)

**Solution:** The scale reads the normal force. With up positive: $N - mg = ma \Rightarrow N = m(g + a)$.
(a) $a = 0$: $N = 700$ N
(b) $a = +2$: $N = 840$ N (the person feels heavier)
(c) $a = -2$: $N = 560$ N (the person feels lighter)
(d) $a = -10$: $N = 0$ (weightlessness)

**Important:** the "weight" you feel is really the normal force. Astronauts on the International Space Station feel weightless not because gravity is absent (at the station's altitude $g$ is still about $8.7$ m/s²) but because they and the station are in continuous free fall together.

### Example 7.7 – A car on a curve (circular dynamics)
**Problem:** What is the maximum speed at which a car can round a flat (unbanked) curve of radius $r = 50$ m if the tire–road static friction coefficient is $\mu_s = 0.8$?

**Solution:** Circular motion requires a net force toward the center, $F_c = m v^2/r$. Static friction supplies it:
$\mu_s m g \ge m v^2 / r \Rightarrow v_{\max} = \sqrt{\mu_s g r} = \sqrt{0.8 \times 10 \times 50} = 20$ m/s $= 72$ km/h.

**The result is independent of mass.** On a wet road $\mu_s$ drops and the safe speed decreases. This is why highway curves are **banked**: on a frictionless curve banked at angle $\theta$, the horizontal component of the normal force supplies the centripetal force and the ideal speed is $v = \sqrt{r g \tan\theta}$.

> **About "centrifugal force":** in an inertial frame, centrifugal force is not a real force. The outward push you feel on a curve is your body's inertia — its tendency to keep going straight. In a rotating (non-inertial) frame, a **fictitious force** of magnitude $m\omega^2 r$ pointing outward is introduced for convenience.

### Example 7.8 – Vertical loop (roller coaster)
**Problem:** What minimum speed must a cart have at the top of a vertical loop of radius $R$ to stay on the track?

**Solution:** At the top both gravity and the normal force point down (toward the center):
$N + mg = m v^2/R$. The condition for staying on the track is $N \ge 0$:
$v^2 / R \ge g \Rightarrow \boxed{v_{\min} = \sqrt{gR}}$

## 8. Variable-Mass Systems: The Rocket Equation

A rocket moves forward by expelling exhaust backward at speed $u$ relative to itself. With no external forces, momentum conservation leads to the **Tsiolkovsky rocket equation**:
$$\Delta v = u \ln\frac{m_0}{m_f}$$
$m_0$: initial mass (including fuel), $m_f$: mass after the fuel is burned. The logarithmic dependence means large velocity changes require enormous fuel ratios — the reason for multi-stage rockets.

**Derivation:** at time $t$ the rocket has mass $m$ and velocity $v$. In time $dt$ it ejects exhaust of mass $dm_{\text{gas}}$ at relative speed $u$. Momentum conservation:
$m v = (m - dm_{\text{gas}})(v + dv) + dm_{\text{gas}}(v - u)$
Dropping second-order terms gives $m\,dv = u\, dm_{\text{gas}} = -u\,dm$ (the rocket's mass changes by $dm = -dm_{\text{gas}}$). Integrating: $\int dv = -u\int_{m_0}^{m_f} \frac{dm}{m} \Rightarrow \Delta v = u\ln(m_0/m_f)$.

## 9. Limits of Newtonian Mechanics

Newton's laws are valid over an enormous range but fail in three regimes:
1. **Speeds approaching light ($v \gtrsim 0.1c$):** special relativity is needed; momentum becomes $\vec p = \gamma m \vec v$.
2. **Very strong gravitational fields:** general relativity is needed (Mercury's perihelion precession, black holes, GPS satellite clocks).
3. **Atomic and subatomic scales:** quantum mechanics is needed; particles do not have definite trajectories.

Newton's laws also hold directly only in inertial frames. Newtonian mechanics is the low-speed, weak-field, large-scale limit of these more general theories.

## 10. Summary

| Law | Statement | Key idea |
|---|---|---|
| First law (inertia) | $\vec F_{\text{net}} = 0 \Rightarrow \vec v$ constant | Defines inertial frames |
| Second law | $\vec F_{\text{net}} = m\vec a = d\vec p/dt$ | Force produces acceleration |
| Third law (action–reaction) | $\vec F_{AB} = -\vec F_{BA}$ | Forces come in pairs acting on different objects |

| Force | Formula | Direction |
|---|---|---|
| Weight | $mg$ | Down (toward Earth's center) |
| Normal | Found from dynamics | Perpendicular to surface |
| Kinetic friction | $\mu_k N$ | Opposite relative motion |
| Static friction | $\le \mu_s N$ | Opposite tendency of motion |
| Spring | $-kx$ | Toward equilibrium |
| Centripetal (net) | $mv^2/r$ | Toward center |
