---
title: Work, Energy and Power
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [work, kinetic energy, potential energy, work-energy theorem, conservation of energy, conservative force, power, efficiency, spring potential energy, mechanical energy, equilibrium, potential energy curve]
---

# Work, Energy and Power

Energy is one of the most fundamental and unifying concepts in physics. Many problems that are hard to solve with Newton's laws (for example, finding the speed of an object sliding along a curved track) take just a few lines with energy methods. The reason is that energy is a scalar and, above all, it is **conserved**.

## 1. Work

### Work done by a constant force
When a constant force $\vec F$ acts on an object that undergoes a displacement $\Delta\vec r$, the work done is
$$W = \vec F \cdot \Delta\vec r = F\,d\cos\theta$$
where $\theta$ is the angle between the force and the displacement. Work is a scalar. Its SI unit is the **joule**:
$$1 \text{ J} = 1 \text{ N}\cdot\text{m} = 1 \text{ kg}\cdot\text{m}^2/\text{s}^2$$

**Sign of work:**
- $0 \le \theta < 90°$: $W > 0$ (the force helps the motion and adds energy)
- $\theta = 90°$: $W = 0$ (the force is perpendicular to the motion; e.g. the centripetal force in circular motion, or weight and normal force during horizontal motion)
- $90° < \theta \le 180°$: $W < 0$ (the force opposes the motion; e.g. kinetic friction)

> **Physical work ≠ everyday work:** someone carrying a heavy bag at constant height while walking horizontally gets tired, but the upward force on the bag is perpendicular to its displacement, so in the physics sense they do **no work on the bag**. The fatigue comes from biochemical energy spent as muscle fibers repeatedly contract and relax.

### Work done by a variable force
If the force varies with position, work is an integral:
$$W = \int_{\vec r_1}^{\vec r_2} \vec F \cdot d\vec r$$
In one dimension: $W = \int_{x_1}^{x_2} F(x)\,dx$ — the area under the force–position graph.

**Example – stretching a spring:** the external force needed to hold a spring stretched by $x$ is $F = kx$. The work to stretch it from $0$ to $x$ is
$$W = \int_0^x kx'\,dx' = \tfrac12 k x^2$$
which is the area of the triangle on the $F$–$x$ graph.

## 2. Kinetic Energy and the Work–Energy Theorem

The **kinetic energy** of a mass $m$ moving at speed $v$ is
$$K = \tfrac12 m v^2$$

**Work–energy theorem:** the total work done by the **net force** on an object equals the change in its kinetic energy:
$$\boxed{W_{\text{net}} = \Delta K = \tfrac12 m v_2^2 - \tfrac12 m v_1^2}$$

**Proof (1D):** $W_{\text{net}} = \int F_{\text{net}}\,dx = \int m\frac{dv}{dt}dx = \int m \frac{dx}{dt} dv = \int_{v_1}^{v_2} m v\,dv = \frac12 m v_2^2 - \frac12 m v_1^2$.

The theorem is derived from Newton's second law, so it is not a new law of nature — it is the second law integrated over space. But it is enormously useful in practice.

### Worked example 2.1
**Problem:** A $1200$ kg car moving at $20$ m/s brakes and stops in $40$ m. What is the average braking (friction) force?

**Solution:** $W_{\text{net}} = \Delta K \Rightarrow -F \cdot 40 = 0 - \frac12 (1200)(20)^2 = -240\,000$ J $\Rightarrow F = 6000$ N.

## 3. Conservative and Non-Conservative Forces

A force is **conservative** if the work it does moving an object from A to B is **independent of the path**. Equivalent definitions:
- The work around any closed path is zero: $\oint \vec F \cdot d\vec r = 0$
- The force can be written as the negative gradient of a potential energy: $\vec F = -\nabla U$
- The curl of the force vanishes: $\nabla \times \vec F = 0$ (in simply connected regions)

| Conservative forces | Non-conservative forces |
|---|---|
| Gravity | Kinetic friction |
| Electrostatic (Coulomb) force | Air resistance |
| Ideal spring force | Forces from muscles/engines (generally) |
| | Forces in plastic deformation |

Friction is non-conservative: pushing a box from A to B along a winding route instead of a straight line requires more work against friction. Non-conservative forces usually convert mechanical energy into thermal (internal) energy.

## 4. Potential Energy

For a conservative force, the **potential energy** $U$ is defined so that its change is the negative of the work done by the force:
$$\Delta U = U_B - U_A = -W_{\text{cons}} = -\int_A^B \vec F \cdot d\vec r$$
Conversely, in one dimension: $F(x) = -\frac{dU}{dx}$.

The **absolute value of potential energy has no meaning**; only differences are physical. The zero point (reference) can be chosen freely.

### 4.1 Gravitational potential energy near the surface
$$U = mgh$$
$h$: height above the chosen reference level.

### 4.2 Universal gravitational potential energy
$$U(r) = -\frac{G M m}{r}$$
Reference: $U = 0$ as $r \to \infty$. Bound systems have negative $U$. Near the surface, $U = mgh$ is an approximation of this formula: with $r = R + h$ and $h \ll R$, $\Delta U \approx \frac{GMm}{R^2} h = mgh$.

### 4.3 Elastic (spring) potential energy
$$U = \tfrac12 k x^2$$
$x$: stretch or compression from equilibrium.

### 4.4 Potential energy curves and equilibrium
A graph of $U(x)$ reveals a lot about the motion:
- **Force** is minus the slope: $F = -dU/dx$. An object is always pushed toward lower potential energy.
- **Equilibrium points** are where $dU/dx = 0$.
  - **Stable equilibrium:** $U$ has a minimum ($d^2U/dx^2 > 0$). After a small displacement the object returns (a marble at the bottom of a bowl).
  - **Unstable equilibrium:** $U$ has a maximum ($d^2U/dx^2 < 0$). A small displacement grows (a marble on top of a hill).
  - **Neutral equilibrium:** $U$ is constant (a marble on a flat floor).
- **Turning points:** if the total energy $E$ is fixed, the object can only be where $U(x) \le E$ (since $K \ge 0$). At points where $U(x) = E$ the speed is zero and the object turns around.

Near a stable equilibrium, a Taylor expansion gives $U(x) \approx U(x_0) + \frac12 U''(x_0)(x - x_0)^2$ — the potential of a spring. Therefore **small oscillations about any stable equilibrium are simple harmonic**, with angular frequency $\omega = \sqrt{U''(x_0)/m}$. This result is used everywhere from molecular vibrations to bridge oscillations.

## 5. Conservation of Mechanical Energy

If only conservative forces do work on an object, its **mechanical energy** (kinetic + potential) is conserved:
$$\boxed{E_{\text{mech}} = K + U = \text{constant}} \qquad \tfrac12 m v_1^2 + U_1 = \tfrac12 m v_2^2 + U_2$$

**Proof:** $W_{\text{net}} = W_{\text{cons}} = -\Delta U$ and $W_{\text{net}} = \Delta K$, so $\Delta K + \Delta U = 0$.

If non-conservative forces also act:
$$\boxed{W_{\text{nc}} = \Delta E_{\text{mech}} = \Delta K + \Delta U}$$
For friction $W_{\text{friction}} < 0$, so mechanical energy decreases; the lost mechanical energy becomes heat. **Total energy** (mechanical + internal + all other forms) is **always** conserved — this is the first law of thermodynamics.

### Worked example 5.1 – Pendulum
**Problem:** A pendulum bob on a string of length $L = 2$ m is released from rest with the string horizontal. Find the speed at the lowest point and the string tension there. ($m = 0.5$ kg, $g = 10$ m/s²)

**Solution:** Take the lowest point as reference. Initially $h = L = 2$ m and $v = 0$.
Energy conservation: $mgL = \frac12 m v^2 \Rightarrow v = \sqrt{2gL} = \sqrt{40} \approx 6.32$ m/s.
At the bottom, circular motion: $T - mg = m v^2/L \Rightarrow T = mg + m \cdot 2gL/L = 3mg = 15$ N.

The result is striking: a pendulum released from horizontal has a string tension at the bottom of **three times its weight**, independent of the string length.

The tension does no work (it is always perpendicular to the motion), so energy conservation applies directly. Solving this with Newton's laws alone would require a differential equation because the angle keeps changing.

### Worked example 5.2 – Spring launcher
**Problem:** A spring with $k = 800$ N/m is compressed $0.1$ m and a $0.2$ kg ball is placed against it. When released, how high does the ball rise vertically? (No friction, $g = 10$ m/s²)

**Solution:** $\frac12 k x^2 = mgh \Rightarrow \frac12 (800)(0.01) = 0.2 \times 10 \times h \Rightarrow 4 = 2h \Rightarrow h = 2$ m.
(Strictly, $h$ is measured from the compressed position; the height above the point where the ball leaves the spring is $2 - 0.1 = 1.9$ m.)

### Worked example 5.3 – Ramp with friction
**Problem:** A $2$ kg block is released from the top of a $5$ m high ramp and reaches the bottom at $8$ m/s. How much work did friction do? ($g = 10$ m/s²)

**Solution:** $W_f = \Delta K + \Delta U = \frac12 (2)(64) - 0 + (0 - 2 \times 10 \times 5) = 64 - 100 = -36$ J.
So $36$ J of mechanical energy was converted into heat.

## 6. Power

Power is the rate at which work is done or energy is transferred:
$$P_{\text{avg}} = \frac{W}{\Delta t}, \qquad P = \frac{dW}{dt}$$
SI unit: the **watt**, $1 \text{ W} = 1 \text{ J/s}$.

The instantaneous power delivered by a force to a moving object is
$$P = \vec F \cdot \vec v = F v \cos\theta$$

**Other units:**
- 1 horsepower: mechanical (imperial) hp ≈ 745.7 W; metric hp ≈ 735.5 W
- The kilowatt-hour (kWh) is a unit of **energy**: $1 \text{ kWh} = 1000 \text{ W} \times 3600 \text{ s} = 3.6 \times 10^6$ J. Electricity bills charge for energy in kWh.

### Efficiency
No real machine converts all of its input energy into useful work:
$$\eta = \frac{P_{\text{out}}}{P_{\text{in}}} = \frac{W_{\text{useful}}}{E_{\text{supplied}}} \times 100\%$$

| System | Typical efficiency |
|---|---|
| Large electric motor | 90–97% |
| Transformer | 95–99% |
| Gasoline car engine | 20–35% |
| Diesel engine | 30–45% |
| Combined-cycle gas power plant | 55–62% |
| Commercial silicon solar panel | 18–23% |
| Human muscle (mechanical work) | ~20–25% |
| Incandescent bulb (as light) | ~2–5% |
| LED lighting (as light) | ~30–50% |

### Worked example 6.1 – Elevator motor
**Problem:** An $800$ kg elevator car carrying passengers totaling $300$ kg rises at a constant $2$ m/s. If the motor is 80% efficient, how much electrical power does it draw? ($g = 10$ m/s², no friction)

**Solution:** At constant speed the cable tension equals the weight: $T = (800 + 300) \times 10 = 11\,000$ N.
Mechanical power: $P_{\text{mech}} = T v = 22\,000$ W $= 22$ kW.
Electrical power: $P_{\text{el}} = P_{\text{mech}}/\eta = 22/0.8 = 27.5$ kW.

### Worked example 6.2 – Car and air drag
**Problem:** Air drag on a car is $F_d = \frac12 C_d \rho A v^2$. If the speed doubles, by what factor does the power needed to overcome drag increase?

**Solution:** $P = F_d \cdot v \propto v^3$. Doubling the speed multiplies the power by $2^3 = 8$. This is the main reason fuel consumption climbs steeply at high speed.

## 7. Forms of Energy and Energy Conversion

Beyond mechanical energy, energy appears in many forms:
- **Thermal (internal) energy:** kinetic and potential energy of the random motion of molecules.
- **Chemical energy:** energy stored in chemical bonds (fuels, food, batteries).
- **Electrical energy:** energy associated with the positions and motion of charges.
- **Radiant (electromagnetic) energy:** light, radio waves, X-rays.
- **Nuclear energy:** binding energy in atomic nuclei.
- **Mass energy:** according to Einstein's $E = mc^2$, mass itself is a form of energy.

**Example conversion chain (hydroelectric plant):** sunlight → evaporation of water (thermal) → rain lifted to high ground (gravitational potential) → falling water at the dam (kinetic) → turbine (rotational kinetic) → generator (electrical) → light bulb at home (light + heat).

### A sense of scale

| Event | Approximate energy |
|---|---|
| Kinetic energy of a flying mosquito | $10^{-7}$ J |
| An apple falling 1 m | 1 J |
| Food energy in a slice of bread | ~$3 \times 10^5$ J (≈ 80 kcal) |
| A person's daily food energy | ~$10^7$ J (≈ 2400 kcal) |
| Burning 1 liter of gasoline | ~$3.4 \times 10^7$ J |
| Explosion of 1 ton of TNT | $4.184 \times 10^9$ J |
| Complete conversion of 1 gram of mass | $9 \times 10^{13}$ J |
| Energy radiated by the Sun in 1 second | ~$3.8 \times 10^{26}$ J |

(1 calorie = 4.184 J; the "Calorie" on food labels is actually a kilocalorie.)

## 8. Summary

| Concept | Formula |
|---|---|
| Work of a constant force | $W = Fd\cos\theta$ |
| Work of a variable force | $W = \int \vec F \cdot d\vec r$ |
| Kinetic energy | $K = \frac12 mv^2$ |
| Work–energy theorem | $W_{\text{net}} = \Delta K$ |
| Gravitational PE (near surface) | $U = mgh$ |
| Universal gravitational PE | $U = -GMm/r$ |
| Spring PE | $U = \frac12 kx^2$ |
| Force from potential | $F = -dU/dx$ |
| Conservation of mechanical energy | $K + U = $ const (conservative forces only) |
| General case | $W_{\text{nc}} = \Delta E_{\text{mech}}$ |
| Power | $P = dW/dt = \vec F \cdot \vec v$ |
| Efficiency | $\eta = P_{\text{out}}/P_{\text{in}}$ |
