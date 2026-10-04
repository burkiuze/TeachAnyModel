---
title: Universal Gravitation, Kepler's Laws and Orbital Mechanics
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [Newton's law of gravitation, gravitational constant, gravitational field, Kepler's laws, orbital velocity, escape velocity, geostationary orbit, tides, shell theorem, orbital energy, Hohmann transfer, Lagrange points]
---

# Universal Gravitation, Kepler's Laws and Orbital Mechanics

Gravity is the weakest of the four fundamental forces, yet it dominates the universe on large scales because it is always attractive and acts over unlimited distances, and because large bodies are electrically neutral. Newton's insight that the same force pulls an apple to the ground and holds the Moon in orbit was the first great unification in physics.

## 1. Newton's Law of Universal Gravitation

Every pair of point masses attracts each other with a force proportional to the product of their masses and inversely proportional to the square of the distance between them:
$$\boxed{F = G\frac{m_1 m_2}{r^2}}$$
In vector form, the force on mass 2 due to mass 1 is $\vec F_{12} = -G\frac{m_1 m_2}{r^2}\hat r_{12}$, where $\hat r_{12}$ points from 1 to 2.

The **gravitational constant** is
$$G = 6.674 \times 10^{-11} \text{ N·m}^2/\text{kg}^2$$
$G$ is the least precisely known fundamental constant (relative uncertainty ~$2 \times 10^{-5}$), because gravity between laboratory masses is extremely weak. Henry Cavendish first measured it in 1798 with a torsion balance; his experiment was famously described as "weighing the Earth", because knowing $G$ and $g$ gives Earth's mass.

**How weak is gravity?** The gravitational attraction between two 1 kg masses 1 m apart is $6.7 \times 10^{-11}$ N. The electric repulsion between two protons is about $10^{36}$ times stronger than their gravitational attraction.

### Shell theorem
Newton proved (and needed calculus to do so) two results for spherically symmetric bodies:
1. A uniform spherical shell attracts an external mass as if all its mass were concentrated at its center.
2. A uniform spherical shell exerts **zero net gravitational force** on a mass anywhere inside it.

Consequence: Earth (approximately spherically symmetric) attracts external objects as a point mass at its center. Inside a uniform-density Earth, only the mass interior to radius $r$ matters, so $g(r) = g_0 \frac{r}{R}$ — gravity would decrease linearly to zero at the center. (Real Earth has a dense core, so $g$ actually increases slightly with depth for the first ~2900 km before dropping.)

## 2. Gravitational Field and Acceleration Due to Gravity

The **gravitational field** of a mass $M$ is the force per unit mass:
$$\vec g = \frac{\vec F}{m} = -\frac{GM}{r^2}\hat r$$

At Earth's surface:
$$g = \frac{GM_E}{R_E^2} = \frac{(6.674\times10^{-11})(5.972\times10^{24})}{(6.371\times10^6)^2} \approx 9.82 \text{ m/s}^2$$

**Variations of $g$:**
- With altitude: $g(h) = g_0\left(\frac{R}{R+h}\right)^2$. At the ISS altitude (~400 km), $g \approx 8.7$ m/s² (about 89% of surface value).
- With latitude: $g \approx 9.780$ m/s² at the equator and $9.832$ m/s² at the poles, because of (a) Earth's rotation (centrifugal effect is largest at the equator) and (b) Earth's equatorial bulge (equatorial radius is ~21 km larger than polar).
- Local geology: dense ore bodies slightly increase $g$; gravimetry is used in mineral and oil prospecting.

| Body | Surface $g$ (m/s²) | Relative to Earth |
|---|---|---|
| Moon | 1.62 | 0.17 |
| Mercury | 3.7 | 0.38 |
| Mars | 3.71 | 0.38 |
| Venus | 8.87 | 0.90 |
| Earth | 9.81 | 1.00 |
| Jupiter (cloud tops) | 24.8 | 2.53 |
| Sun (photosphere) | 274 | 28 |
| White dwarf (typical) | ~$10^6$ | ~$10^5$ |
| Neutron star (typical) | ~$10^{12}$ | ~$10^{11}$ |

## 3. Gravitational Potential Energy and Potential

$$U(r) = -\frac{GMm}{r}, \qquad V(r) = \frac{U}{m} = -\frac{GM}{r}$$
with the reference $U(\infty) = 0$.

Derivation: $U(r) = -\int_\infty^r \vec F\cdot d\vec r = -\int_\infty^r \left(-\frac{GMm}{r'^2}\right)dr' = -\frac{GMm}{r}$.

Potential energy is negative for bound systems: you must add energy to separate the masses to infinity.

## 4. Kepler's Laws of Planetary Motion

Johannes Kepler (1571–1630), analyzing Tycho Brahe's extremely precise naked-eye observations of Mars, discovered three empirical laws. Newton later derived all three from his laws of motion and gravitation.

### First law: law of ellipses
Each planet moves in an **ellipse** with the Sun at one **focus**.

Ellipse terminology:
- Semi-major axis $a$; semi-minor axis $b$
- Eccentricity $e = \sqrt{1 - b^2/a^2}$ ($e = 0$ is a circle; $0 < e < 1$ an ellipse)
- Distance from center to focus: $c = ae$
- Closest point to the Sun: **perihelion**, $r_p = a(1 - e)$; farthest: **aphelion**, $r_a = a(1 + e)$
- (For Earth orbits: perigee and apogee.)

Earth's orbital eccentricity is only 0.0167; its distance from the Sun varies between about 147.1 and 152.1 million km. Earth is at perihelion in early January — **seasons are caused by axial tilt (23.4°), not by distance**.

More generally, motion under an inverse-square force follows a **conic section**: ellipse (bound, $E < 0$), parabola ($E = 0$) or hyperbola (unbound, $E > 0$).

### Second law: law of equal areas
The line joining a planet to the Sun sweeps out **equal areas in equal times**. Planets move fastest at perihelion and slowest at aphelion.

**Physical origin:** gravity is a central force (directed along the line to the Sun), so it exerts no torque about the Sun and angular momentum is conserved. The areal velocity is
$$\frac{dA}{dt} = \frac{L}{2m} = \text{constant}$$
At perihelion and aphelion the velocity is perpendicular to the radius, so $r_p v_p = r_a v_a$.

### Third law: law of periods
The square of the orbital period is proportional to the cube of the semi-major axis:
$$\boxed{T^2 = \frac{4\pi^2}{G(M + m)}\,a^3 \approx \frac{4\pi^2}{GM}a^3}$$

**Derivation for a circular orbit:** gravity provides the centripetal force:
$$\frac{GMm}{r^2} = m\frac{v^2}{r} = m\frac{4\pi^2 r}{T^2} \Rightarrow T^2 = \frac{4\pi^2}{GM}r^3$$

In convenient units for the Solar System (period in years, $a$ in astronomical units, 1 AU ≈ $1.496 \times 10^{11}$ m): $T^2 = a^3$.

| Planet | $a$ (AU) | $T$ (years) | $T^2 / a^3$ |
|---|---|---|---|
| Mercury | 0.387 | 0.241 | 1.00 |
| Venus | 0.723 | 0.615 | 1.00 |
| Earth | 1.000 | 1.000 | 1.00 |
| Mars | 1.524 | 1.881 | 1.00 |
| Jupiter | 5.203 | 11.86 | 1.00 |
| Saturn | 9.537 | 29.46 | 1.00 |
| Uranus | 19.19 | 84.01 | 1.00 |
| Neptune | 30.07 | 164.8 | 1.00 |

**Weighing celestial bodies:** the third law lets us find the mass of any body that has a satellite. From the Moon's orbit we get Earth's mass; from Earth's orbit, the Sun's mass ($1.989 \times 10^{30}$ kg); from stars orbiting the center of the Milky Way, the mass of the supermassive black hole Sagittarius A* (~4 million solar masses — Nobel Prize in Physics 2020). From the orbital speeds of stars in galaxies, astronomers inferred the existence of **dark matter**.

## 5. Circular Orbits and Satellites

### Orbital speed
$$\frac{GMm}{r^2} = \frac{mv^2}{r} \Rightarrow \boxed{v_{\text{orb}} = \sqrt{\frac{GM}{r}}}$$
Orbital speed is independent of the satellite's mass and decreases with distance. For low Earth orbit ($r \approx R_E$): $v \approx \sqrt{gR_E} \approx 7.9$ km/s, with a period of about 84 minutes at the surface radius (about 92 minutes for the ISS at 400 km).

### Orbital energy
$$K = \frac12 mv^2 = \frac{GMm}{2r}, \qquad U = -\frac{GMm}{r}, \qquad E = K + U = -\frac{GMm}{2r}$$
For any circular orbit: $K = -E$ and $U = 2E$ (an instance of the **virial theorem**: $2\langle K\rangle = -\langle U\rangle$ for inverse-square forces).
For an elliptical orbit: $E = -\frac{GMm}{2a}$; the energy depends only on the semi-major axis.

**Orbital paradox:** to move to a higher orbit, a satellite must fire its engines (add energy), yet in the higher orbit it moves *slower*. Conversely, atmospheric drag makes a satellite lose energy, drop to a lower orbit and **speed up**.

The **vis-viva equation** gives the speed at any point of an elliptical orbit:
$$v^2 = GM\left(\frac{2}{r} - \frac{1}{a}\right)$$

### Geostationary orbit
A satellite that orbits above the equator with period equal to Earth's sidereal rotation period (23 h 56 min 4 s = 86 164 s) remains fixed over one point:
$$r = \left(\frac{GM_E T^2}{4\pi^2}\right)^{1/3} = \left(\frac{3.986\times10^{14} \times 86164^2}{4\pi^2}\right)^{1/3} \approx 4.216 \times 10^7 \text{ m}$$
That is about 42 164 km from Earth's center, or **35 786 km above the surface**, with orbital speed about 3.07 km/s. Used for communications and weather satellites. Arthur C. Clarke popularized the idea in 1945.

## 6. Escape Velocity

The minimum launch speed for an object to escape a body's gravity entirely (reaching infinity with zero speed, ignoring air resistance) follows from $E = 0$:
$$\frac12 mv_{\text{esc}}^2 - \frac{GMm}{R} = 0 \Rightarrow \boxed{v_{\text{esc}} = \sqrt{\frac{2GM}{R}} = \sqrt{2}\,v_{\text{orb}}}$$

| Body | Escape velocity |
|---|---|
| Moon | 2.38 km/s |
| Mars | 5.03 km/s |
| Earth | 11.19 km/s |
| Jupiter | 59.5 km/s |
| Sun (from surface) | 617.7 km/s |
| Escape the Solar System from Earth's orbit | 42.1 km/s (relative to the Sun) |

**Atmospheres:** a planet retains a gas if typical molecular speeds are well below escape velocity (a rule of thumb: rms speed < 1/6 of $v_{\text{esc}}$). The Moon lost any atmosphere; Earth lost most of its hydrogen and helium but retains N₂ and O₂.

**Black holes:** if a body is compressed so that $v_{\text{esc}} = c$, not even light escapes. Setting $v_{\text{esc}} = c$ gives the **Schwarzschild radius** $r_s = 2GM/c^2$ (Newtonian reasoning happens to give the correct general-relativistic result). For the Sun $r_s \approx 2.95$ km; for Earth, about 8.9 mm.

## 7. Tides

Tides arise because gravity varies with distance: the Moon pulls harder on the near side of Earth than on Earth's center, and harder on Earth's center than on the far side. Relative to Earth's center, the oceans are stretched into two bulges — one facing the Moon and one opposite. As Earth rotates, a given location passes through both bulges, giving **two high tides per lunar day** (24 h 50 min).

The tidal acceleration across a body of size $\Delta r$ at distance $r$ from mass $M$ scales as
$$a_{\text{tidal}} \approx \frac{2GM}{r^3}\Delta r$$
— an inverse **cube** law. Although the Sun's gravitational pull on Earth is about 180 times the Moon's, its tidal effect is only about 46% of the Moon's because it is so much farther away.

- **Spring tides** (largest range): Sun, Earth and Moon aligned (new and full moon).
- **Neap tides** (smallest range): Sun and Moon at right angles (first and third quarter).
- **Tidal locking:** tidal friction has slowed the Moon's rotation until it always shows the same face to Earth. Earth's day is lengthening by about 2 milliseconds per century, and the Moon recedes from Earth by about 3.8 cm per year (measured with laser reflectors left by Apollo astronauts) — angular momentum is transferred from Earth's spin to the Moon's orbit.
- **Roche limit:** a fluid moon closer than about 2.44 planetary radii (for equal densities) is torn apart by tides; Saturn's rings lie mostly within its Roche limit.

## 8. Orbital Maneuvers

### Hohmann transfer orbit
The most fuel-efficient two-impulse transfer between two coplanar circular orbits uses an ellipse tangent to both: perihelion at the inner orbit, aphelion at the outer. Semi-major axis $a_t = (r_1 + r_2)/2$; transfer time is half the ellipse's period:
$$t = \pi\sqrt{\frac{a_t^3}{GM}}$$
An Earth-to-Mars Hohmann transfer takes about 259 days (≈8.5 months), and launch windows recur every **synodic period** of about 26 months.

### Gravity assist (slingshot)
A spacecraft passing close to a moving planet can gain (or lose) speed relative to the Sun. In the planet's frame, the encounter is elastic — the speed is unchanged, only the direction turns. Transforming back to the Sun's frame, the spacecraft can gain up to twice the planet's orbital speed. Voyager 2 used Jupiter, Saturn, Uranus and Neptune in succession.

### Lagrange points
In the three-body problem of a small object near two large orbiting bodies (e.g. Sun and Earth), there are five points where the small object can remain stationary relative to the two bodies. L1, L2 and L3 lie on the line through the bodies and are unstable; L4 and L5 form equilateral triangles with them and are stable if the mass ratio exceeds about 25 (true for Sun–Jupiter, where "Trojan" asteroids gather). The James Webb Space Telescope orbits near the Sun–Earth L2 point, about 1.5 million km from Earth.

## 9. Beyond Newton

Newtonian gravity fails in some precise tests:
- **Mercury's perihelion** precesses by 43 arcseconds per century more than Newtonian theory predicts (after accounting for perturbations by other planets). Einstein's general relativity (1915) explained it exactly.
- **Light bending** by the Sun is twice the "Newtonian" value; confirmed in the 1919 eclipse expedition led by Eddington.
- **Gravitational time dilation and gravitational waves** have no Newtonian analogue.

In general relativity gravity is not a force but the curvature of spacetime produced by mass-energy. Newton's law is its weak-field, slow-motion limit.

## 10. Summary

| Quantity | Formula |
|---|---|
| Gravitational force | $F = Gm_1m_2/r^2$ |
| Gravitational field | $g = GM/r^2$ |
| Potential energy | $U = -GMm/r$ |
| Kepler III | $T^2 = 4\pi^2a^3/(GM)$ |
| Circular orbital speed | $v = \sqrt{GM/r}$ |
| Orbital energy | $E = -GMm/(2a)$ |
| Vis-viva | $v^2 = GM(2/r - 1/a)$ |
| Escape velocity | $v_{\text{esc}} = \sqrt{2GM/R}$ |
| Schwarzschild radius | $r_s = 2GM/c^2$ |
| Tidal acceleration | $\approx 2GM\Delta r/r^3$ |

**Key constants:** $G = 6.674\times10^{-11}$ N·m²/kg²; $M_E = 5.972\times10^{24}$ kg; $R_E = 6371$ km; $M_\odot = 1.989\times10^{30}$ kg; $M_{\text{Moon}} = 7.35\times10^{22}$ kg; Earth–Moon distance ≈ 384 400 km; 1 AU ≈ $1.496\times10^{11}$ m.
