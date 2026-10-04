---
title: Linear Momentum, Impulse and Collisions
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [momentum, impulse, conservation of momentum, elastic collision, inelastic collision, center of mass, coefficient of restitution, ballistic pendulum, recoil, two-dimensional collision]
---

# Linear Momentum, Impulse and Collisions

Energy conservation alone cannot solve a collision problem, because during a collision some kinetic energy may be converted into heat, sound and deformation. Yet another quantity is *always* conserved when objects interact only with each other: **linear momentum**. Momentum conservation is one of the deepest principles in physics; it follows from the fact that the laws of physics are the same everywhere in space (translational symmetry, via Noether's theorem).

## 1. Linear Momentum

The **linear momentum** of a particle of mass $m$ and velocity $\vec v$ is
$$\vec p = m\vec v$$
It is a vector pointing along the velocity. SI unit: kg·m/s (equivalently N·s).

Momentum captures the idea of "quantity of motion": a slow truck and a fast bullet can both be hard to stop. A 10 000 kg truck at 1 m/s and a 10 g bullet at 1000 m/s have momenta of 10 000 kg·m/s and 10 kg·m/s respectively.

**Relation to kinetic energy:** $K = \frac{p^2}{2m}$. For the same momentum, the lighter object has more kinetic energy.

**Newton's second law in momentum form:**
$$\vec F_{\text{net}} = \frac{d\vec p}{dt}$$

## 2. Impulse

The **impulse** of a force over a time interval is
$$\vec J = \int_{t_1}^{t_2} \vec F\,dt$$
Integrating the second law gives the **impulse–momentum theorem**:
$$\boxed{\vec J = \Delta\vec p = \vec p_2 - \vec p_1}$$

For a force that varies during a collision we often use the average force: $\vec J = \vec F_{\text{avg}}\,\Delta t$. Graphically, impulse is the area under the force–time curve.

### Applications: stretching the collision time
For a given change in momentum, a **longer collision time means a smaller average force**:
$$F_{\text{avg}} = \frac{\Delta p}{\Delta t}$$
- **Airbags and crumple zones** extend the stopping time of passengers and reduce the forces on them.
- Bending your knees when landing from a jump increases $\Delta t$.
- Catching a ball by moving your hands backward with it.
- Gym mats, bicycle helmets (crushable foam), and packaging foam work the same way.

### Worked example 2.1
**Problem:** A $0.15$ kg baseball approaches a bat at $40$ m/s and leaves in the opposite direction at $50$ m/s. The contact lasts $1.2$ ms. Find the impulse and average force.

**Solution:** Take the outgoing direction as positive. $p_1 = 0.15 \times (-40) = -6$ kg·m/s, $p_2 = 0.15 \times 50 = 7.5$ kg·m/s.
$J = \Delta p = 13.5$ N·s.
$F_{\text{avg}} = J/\Delta t = 13.5 / 0.0012 = 11\,250$ N — about 7600 times the ball's weight.

Note that reversing direction makes the momentum change larger than simply stopping the ball; this is why a bouncing collision involves a larger impulse than a sticking one.

## 3. Conservation of Linear Momentum

Consider a system of particles. Forces on the particles are either **internal** (between particles of the system) or **external** (from outside). By Newton's third law, internal forces come in equal and opposite pairs and cancel when summed over the system. Therefore:
$$\frac{d\vec P_{\text{total}}}{dt} = \vec F_{\text{ext}}$$

**Law of conservation of momentum:** if the net external force on a system is zero, its total momentum is constant:
$$\boxed{\vec F_{\text{ext}} = 0 \Rightarrow \sum_i m_i\vec v_i = \text{constant}}$$

Notes:
- Conservation can hold in one direction even if not in another. For example, a projectile exploding in midair: gravity acts vertically, so horizontal momentum is conserved.
- In collisions and explosions, internal forces are typically so large and brief that external forces (gravity, friction) can be neglected *during* the event (the **impulse approximation**).

### Recoil
**Problem:** A $4$ kg rifle fires a $10$ g bullet at $800$ m/s. What is the rifle's recoil velocity?

**Solution:** Initially everything is at rest: $P = 0$. After firing: $0 = (0.01)(800) + (4)v_r \Rightarrow v_r = -2$ m/s. The rifle moves backward at 2 m/s.
Kinetic energies: bullet $\frac12(0.01)(800^2) = 3200$ J; rifle $\frac12(4)(2^2) = 8$ J. Equal momenta, very unequal energies — the light object carries away most of the energy.

## 4. Center of Mass

The **center of mass** of a system is the mass-weighted average position:
$$\vec R_{\text{cm}} = \frac{\sum_i m_i \vec r_i}{\sum_i m_i} = \frac{1}{M}\sum_i m_i\vec r_i, \qquad \vec R_{\text{cm}} = \frac{1}{M}\int \vec r\,dm \;\text{(continuous body)}$$

Differentiating: $M\vec V_{\text{cm}} = \vec P_{\text{total}}$ and
$$M\vec A_{\text{cm}} = \vec F_{\text{ext}}$$

**The center of mass moves as if all the mass were concentrated there and all external forces acted on it.** This is why we can treat extended objects as point particles in translational problems. When a firework shell explodes in midair, the fragments fly apart but their center of mass continues along the original parabola (until fragments hit the ground).

For symmetric uniform objects the center of mass lies at the geometric center. It need not lie inside the material: the center of mass of a ring or a boomerang is in empty space. A high jumper using the Fosbury flop arches the body so that their center of mass may pass *below* the bar.

### Worked example 4.1
**Problem:** A $60$ kg person stands at one end of a $4$ m, $40$ kg boat floating at rest. The person walks to the other end. How far does the boat move? (Neglect water resistance.)

**Solution:** No horizontal external force, so the center of mass stays put. Let the person move $+4$ m relative to the boat and the boat move $x$ relative to the water. The person's displacement relative to the water is $4 + x$.
$60(4 + x) + 40x = 0 \Rightarrow 240 + 100x = 0 \Rightarrow x = -2.4$ m.
The boat moves 2.4 m backward; the person moves 1.6 m forward relative to the water.

## 5. Collisions

In every isolated collision **momentum is conserved**. What distinguishes types of collisions is what happens to **kinetic energy**:

| Type | Momentum | Kinetic energy | Example |
|---|---|---|---|
| Elastic | Conserved | Conserved | Billiard balls (approximately), gas molecules, atomic scattering |
| Inelastic | Conserved | Decreases | Most real collisions, a bouncing ball |
| Perfectly (completely) inelastic | Conserved | Maximum possible loss; objects stick together | Clay balls, coupling railroad cars, a bullet embedding in a block |
| Superelastic (explosive) | Conserved | Increases | Explosions, release of a compressed spring between carts |

### 5.1 Perfectly inelastic collision
The objects move together after the collision:
$$m_1 v_1 + m_2 v_2 = (m_1 + m_2) v_f \Rightarrow v_f = \frac{m_1 v_1 + m_2 v_2}{m_1 + m_2}$$

The kinetic energy lost is
$$\Delta K = -\frac12 \frac{m_1 m_2}{m_1 + m_2} (v_1 - v_2)^2$$
where $\mu = \frac{m_1 m_2}{m_1+m_2}$ is the **reduced mass**. Only the kinetic energy associated with motion of the center of mass survives; all the energy of relative motion is dissipated.

### 5.2 One-dimensional elastic collision
Both momentum and kinetic energy are conserved:
$$m_1 v_1 + m_2 v_2 = m_1 v_1' + m_2 v_2'$$
$$\tfrac12 m_1 v_1^2 + \tfrac12 m_2 v_2^2 = \tfrac12 m_1 v_1'^2 + \tfrac12 m_2 v_2'^2$$

Rearranging both as $m_1(v_1 - v_1') = m_2(v_2' - v_2)$ and $m_1(v_1^2 - v_1'^2) = m_2(v_2'^2 - v_2^2)$ and dividing gives a very useful linear relation:
$$\boxed{v_1 - v_2 = -(v_1' - v_2')}$$
**In a 1D elastic collision the relative velocity reverses.** Solving:
$$v_1' = \frac{m_1 - m_2}{m_1 + m_2} v_1 + \frac{2m_2}{m_1 + m_2} v_2$$
$$v_2' = \frac{2m_1}{m_1 + m_2} v_1 + \frac{m_2 - m_1}{m_1 + m_2} v_2$$

**Special cases** (target at rest, $v_2 = 0$):
- **Equal masses:** $v_1' = 0$, $v_2' = v_1$ — the objects exchange velocities (Newton's cradle, a head-on billiard shot).
- **Heavy target ($m_2 \gg m_1$):** $v_1' \approx -v_1$, $v_2' \approx 0$ — the light object bounces back (a ball hitting a wall).
- **Light target ($m_1 \gg m_2$):** $v_1' \approx v_1$, $v_2' \approx 2v_1$ — the light object flies off at twice the projectile's speed (a golf club hitting a ball).

**Neutron moderation in reactors:** to slow fast neutrons efficiently, they must collide with nuclei of similar mass. That is why reactors use water (hydrogen nuclei ≈ neutron mass) or graphite (carbon) as moderators rather than heavy elements like lead.

### 5.3 Coefficient of restitution
For a general 1D collision, the **coefficient of restitution** is
$$e = -\frac{v_2' - v_1'}{v_2 - v_1} = \frac{\text{speed of separation}}{\text{speed of approach}}$$
- $e = 1$: elastic
- $0 < e < 1$: inelastic
- $e = 0$: perfectly inelastic

A ball dropped from height $h$ onto a rigid floor rebounds to height $h' = e^2 h$, which gives a simple way to measure $e$. A basketball has $e \approx 0.75$–$0.85$; a superball about $0.9$.

### 5.4 Two-dimensional collisions
Momentum conservation is applied separately in each direction:
$$\sum p_x \text{ before} = \sum p_x \text{ after}, \qquad \sum p_y \text{ before} = \sum p_y \text{ after}$$

**Remarkable result:** in an elastic, glancing collision between **equal masses** with one initially at rest, the two objects move off at **90°** to each other (as long as the collision is not head-on).

**Proof:** momentum: $\vec v_1 = \vec v_1' + \vec v_2'$. Energy: $v_1^2 = v_1'^2 + v_2'^2$. Squaring the first: $v_1^2 = v_1'^2 + v_2'^2 + 2\vec v_1'\cdot\vec v_2'$. Comparing, $\vec v_1' \cdot \vec v_2' = 0$, so the final velocities are perpendicular. Billiard players use this intuitively, and it is seen in bubble-chamber photographs of proton–proton scattering.

## 6. Worked Problems

### Problem 6.1 – Ballistic pendulum
**Problem:** A $10$ g bullet is fired into a $2$ kg wooden block hanging from strings and embeds in it. The block (with bullet) swings up to a height of $5$ cm. Find the bullet's speed. ($g = 9.8$ m/s²)

**Solution:** Two stages:
1. **Collision (momentum conserved, energy NOT):** $m v = (m + M) V$.
2. **Swing (energy conserved, momentum NOT — gravity and tension act):** $\frac12 (m+M) V^2 = (m+M) g h \Rightarrow V = \sqrt{2gh} = \sqrt{2 \times 9.8 \times 0.05} \approx 0.99$ m/s.

$v = \frac{m + M}{m} V = \frac{2.01}{0.01} \times 0.99 \approx 199$ m/s.

Fraction of kinetic energy retained in the collision: $\frac{m}{m+M} = \frac{0.01}{2.01} \approx 0.5\%$. More than 99% of the bullet's kinetic energy becomes heat and deformation. Using energy conservation across the collision would be a serious error.

### Problem 6.2 – Elastic collision
**Problem:** A $2$ kg cart moving right at $6$ m/s collides elastically with a $4$ kg cart moving left at $3$ m/s. Find the final velocities.

**Solution:** $v_1 = 6$, $v_2 = -3$.
$v_1' = \frac{2 - 4}{6}(6) + \frac{8}{6}(-3) = -2 - 4 = -6$ m/s
$v_2' = \frac{4}{6}(6) + \frac{2}{6}(-3) = 4 - 1 = 3$ m/s
Check momentum: before $12 - 12 = 0$; after $-12 + 12 = 0$ ✓. Relative velocity: before $6 - (-3) = 9$; after $-6 - 3 = -9$ ✓. Since total momentum is zero we are in the center-of-mass frame, where an elastic collision simply reverses each velocity.

### Problem 6.3 – Explosion
**Problem:** A $3$ kg shell moving horizontally at $20$ m/s explodes into two pieces. A $1$ kg piece moves straight backward at $10$ m/s. Find the velocity of the other piece and the energy released.

**Solution:** $3 \times 20 = 1 \times (-10) + 2 v \Rightarrow 60 + 10 = 2v \Rightarrow v = 35$ m/s forward.
$K_{\text{before}} = \frac12 (3)(400) = 600$ J. $K_{\text{after}} = \frac12(1)(100) + \frac12(2)(1225) = 50 + 1225 = 1275$ J.
Energy released by the explosion: $675$ J (from chemical energy).

### Problem 6.4 – 2D car crash (accident reconstruction)
**Problem:** A $1500$ kg car traveling east at $20$ m/s collides at an intersection with a $2500$ kg truck traveling north at $15$ m/s. They lock together. Find the velocity of the wreckage just after the crash.

**Solution:**
$p_x = 1500 \times 20 = 30\,000$ kg·m/s; $p_y = 2500 \times 15 = 37\,500$ kg·m/s.
$V_x = 30\,000/4000 = 7.5$ m/s; $V_y = 37\,500/4000 = 9.375$ m/s.
$V = \sqrt{7.5^2 + 9.375^2} \approx 12.0$ m/s, direction $\tan\phi = 9.375/7.5 = 1.25 \Rightarrow \phi \approx 51.3°$ north of east.

Accident investigators run this logic in reverse: from skid marks (which give the post-crash speed via friction and the work–energy theorem) and directions, they infer pre-collision speeds.

## 7. Center-of-Mass Frame

It is often simplest to analyze collisions in the frame moving with the center of mass, where the total momentum is zero. In this frame:
- Before the collision, the two objects approach each other with momenta $\vec p$ and $-\vec p$.
- In an elastic collision, they leave with momenta of the same magnitude, only rotated in direction.
- In a perfectly inelastic collision, both end at rest.

The kinetic energy in the lab frame splits as $K_{\text{lab}} = \frac12 M V_{\text{cm}}^2 + K_{\text{cm}}$. Only $K_{\text{cm}}$ is available to be converted into other forms (heat, new particles). This is why particle physicists build **colliders**, where two beams hit head-on (lab frame = CM frame), rather than firing a beam at a fixed target, where much of the energy is wasted on center-of-mass motion.

## 8. Summary

| Concept | Formula |
|---|---|
| Momentum | $\vec p = m\vec v$ |
| Impulse | $\vec J = \int \vec F dt = \Delta \vec p$ |
| Second law | $\vec F_{\text{net}} = d\vec p/dt$ |
| Conservation | $\vec F_{\text{ext}} = 0 \Rightarrow \vec P$ constant |
| Center of mass | $\vec R_{\text{cm}} = \sum m_i\vec r_i / M$; $M\vec A_{\text{cm}} = \vec F_{\text{ext}}$ |
| Perfectly inelastic | $v_f = (m_1v_1 + m_2v_2)/(m_1+m_2)$ |
| 1D elastic | $v_1 - v_2 = -(v_1' - v_2')$ |
| Coefficient of restitution | $e = (v_2' - v_1')/(v_1 - v_2)$ |
| KE–momentum | $K = p^2/2m$ |

**Common mistakes:**
1. Using kinetic-energy conservation in an inelastic collision.
2. Forgetting that momentum is a vector — signs in 1D, components in 2D.
3. Applying momentum conservation over a stage in which external forces matter (e.g. the swing of a ballistic pendulum).
4. Confusing "momentum is conserved" with "each object's momentum is unchanged" — it is the *total* that is conserved.
