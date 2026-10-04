---
title: Fluid Mechanics - Statics and Dynamics of Fluids
field: Physics
subfield: Classical Mechanics
level: high-school to undergraduate
keywords: [pressure, density, Pascal's principle, hydrostatic pressure, Archimedes' principle, buoyancy, continuity equation, Bernoulli's equation, viscosity, Poiseuille's law, Reynolds number, turbulence, surface tension, Navier-Stokes]
---

# Fluid Mechanics: Statics and Dynamics of Fluids

A **fluid** is a substance that flows — it cannot resist a shear stress at rest and deforms continuously under one. Liquids and gases are both fluids. Liquids are nearly incompressible; gases are easily compressed. Fluid mechanics explains why ships float, how airplanes fly (in part), how blood circulates, why the sky has weather, and how hydraulic machines multiply force.

## 1. Density and Pressure

### Density
$$\rho = \frac{m}{V} \qquad [\text{kg/m}^3]$$

| Substance | Density (kg/m³) |
|---|---|
| Air (sea level, 20 °C) | 1.20 |
| Helium (STP) | 0.179 |
| Gasoline | ~740 |
| Ice | 917 |
| Water (4 °C) | 1000 |
| Seawater | ~1025 |
| Human blood | ~1060 |
| Aluminum | 2700 |
| Iron | 7870 |
| Mercury | 13 600 |
| Gold | 19 300 |
| Osmium (densest element) | 22 590 |

**Specific gravity** (relative density) is density relative to water at 4 °C; dimensionless.

Water is unusual: its maximum density is at about 4 °C, and ice is less dense than liquid water. Therefore lakes freeze from the top down, and the ice layer insulates the water below, allowing aquatic life to survive winter.

### Pressure
Pressure is normal force per unit area:
$$P = \frac{F_\perp}{A} \qquad [\text{Pa} = \text{N/m}^2]$$
Pressure is a scalar: at a point in a fluid at rest it acts equally in all directions.

Units: 1 atm = 101 325 Pa = 1.01325 bar = 760 mmHg (torr) ≈ 14.7 psi.

**Gauge pressure** is pressure relative to atmospheric: $P_{\text{gauge}} = P_{\text{abs}} - P_{\text{atm}}$. Tire gauges and blood pressure readings are gauge pressures (a blood pressure of 120/80 mmHg means 120 mmHg above atmospheric at peak).

## 2. Hydrostatics

### Pressure varies with depth
Consider a thin horizontal slab of fluid at rest. Balancing forces on it gives $\frac{dP}{dy} = -\rho g$ (with $y$ upward). For an incompressible fluid:
$$\boxed{P = P_0 + \rho g h}$$
where $h$ is depth below a point at pressure $P_0$.

- Pressure depends **only on depth**, not on the shape of the container (**hydrostatic paradox**): water in a narrow tube and in a wide tank exerts the same pressure at the same depth.
- In water, pressure increases by about 1 atm for every 10.3 m of depth. At the bottom of the Mariana Trench (~10 900 m), the pressure exceeds 1000 atm.
- Divers must equalize pressure in their ears and must ascend slowly to avoid decompression sickness (dissolved nitrogen forming bubbles as pressure drops — Henry's law).

### Atmospheric pressure and the barometer
Evangelista Torricelli (1643) inverted a mercury-filled tube into a dish of mercury; the column fell to about 760 mm, leaving a near-vacuum above it. Atmospheric pressure supports the column: $P_{\text{atm}} = \rho_{\text{Hg}}gh$. A water barometer would need a column about 10.3 m tall — which is also why a suction pump cannot lift water more than about 10 m.

In an isothermal atmosphere (ideal gas), $dP/dy = -\rho g$ with $\rho = PM/(RT)$ gives the **barometric formula**:
$$P(h) = P_0 e^{-h/H}, \qquad H = \frac{RT}{Mg} \approx 8.4 \text{ km}$$
At the summit of Everest (8849 m) pressure is about one third of sea-level pressure.

### Pascal's principle
A pressure change applied to an enclosed incompressible fluid is transmitted undiminished to every point of the fluid and to the walls.

**Hydraulic press/lift:** a small force $F_1$ on a small piston $A_1$ creates pressure $P = F_1/A_1$, which acts on a large piston $A_2$:
$$F_2 = F_1\frac{A_2}{A_1}$$
Force is multiplied, but energy is conserved: the small piston must move farther ($d_1A_1 = d_2A_2$, so $F_1d_1 = F_2d_2$). Used in car lifts, hydraulic brakes, excavators and aircraft controls.

## 3. Buoyancy and Archimedes' Principle

> **Archimedes' principle:** a body wholly or partly immersed in a fluid experiences an upward buoyant force equal to the weight of the fluid it displaces.
$$\boxed{F_B = \rho_{\text{fluid}}\,V_{\text{displaced}}\,g}$$

**Origin:** pressure increases with depth, so the upward force on the bottom of an object exceeds the downward force on its top. For a box of height $h$ and area $A$: $F_B = (P_{\text{bottom}} - P_{\text{top}})A = \rho g h A = \rho g V$.

**Floating and sinking** (for a fully submerged uniform object of density $\rho_{\text{obj}}$):
- $\rho_{\text{obj}} < \rho_{\text{fluid}}$: rises; floats partly submerged
- $\rho_{\text{obj}} = \rho_{\text{fluid}}$: neutrally buoyant (fish with swim bladders, submarines adjusting ballast)
- $\rho_{\text{obj}} > \rho_{\text{fluid}}$: sinks

For a floating object, weight = buoyant force, so the **fraction submerged** equals the density ratio:
$$\frac{V_{\text{sub}}}{V_{\text{total}}} = \frac{\rho_{\text{obj}}}{\rho_{\text{fluid}}}$$
Ice in seawater: $917/1025 \approx 0.89$ — about 89% of an iceberg is below the surface ("tip of the iceberg").

Steel ships float because their hollow shape displaces a volume of water whose weight equals the ship's weight. Hot-air balloons and helium balloons float in the "fluid" of air.

**Legend:** Archimedes is said to have used this principle to determine whether King Hiero's crown was pure gold, by comparing the volume of water it displaced with that displaced by an equal mass of gold.

### Worked example 3.1
**Problem:** A rock weighs 30 N in air and 20 N when fully submerged in water. Find its volume and density. ($g = 10$ m/s²)

**Solution:** Buoyant force $F_B = 30 - 20 = 10$ N $= \rho_w V g \Rightarrow V = 10/(1000 \times 10) = 10^{-3}$ m³ (1 liter).
Mass $= 30/10 = 3$ kg. Density $= 3/10^{-3} = 3000$ kg/m³.

## 4. Fluid Dynamics: Ideal Flow

An **ideal fluid** is incompressible and non-viscous, and we consider **steady** (time-independent), **irrotational** flow. **Streamlines** are curves tangent to the velocity at each point; in steady flow they coincide with particle paths and never cross.

### Continuity equation (conservation of mass)
For steady flow through a tube, the mass flow rate is constant:
$$\rho_1 A_1 v_1 = \rho_2 A_2 v_2$$
For an incompressible fluid this becomes conservation of **volume flow rate**:
$$\boxed{Q = A_1v_1 = A_2v_2}$$
Fluid speeds up where the pipe narrows. Putting your thumb over a garden hose makes the water jet faster.

In differential form, $\frac{\partial\rho}{\partial t} + \nabla\cdot(\rho\vec v) = 0$; for incompressible flow, $\nabla\cdot\vec v = 0$.

### Bernoulli's equation (conservation of energy)
Along a streamline in steady, incompressible, non-viscous flow:
$$\boxed{P + \tfrac12\rho v^2 + \rho g y = \text{constant}}$$

**Derivation (work–energy):** consider a parcel of fluid moving from region 1 to region 2. The net work done by pressure is $(P_1 - P_2)\Delta V$. The change in kinetic energy is $\frac12\rho\Delta V(v_2^2 - v_1^2)$ and in potential energy $\rho\Delta Vg(y_2 - y_1)$. Setting work = energy change and dividing by $\Delta V$ gives Bernoulli's equation. Each term has units of pressure, i.e. energy per unit volume.

**Key consequence:** where a fluid moves faster (at the same height), its pressure is lower.

### Applications
1. **Torricelli's law:** water flows from a hole at depth $h$ below the surface of an open tank with speed $v = \sqrt{2gh}$ — the same speed as an object falling from height $h$.
2. **Venturi meter:** measures flow speed from the pressure drop in a constriction: $P_1 - P_2 = \frac12\rho(v_2^2 - v_1^2)$.
3. **Pitot tube:** measures aircraft airspeed by comparing stagnation pressure with static pressure: $v = \sqrt{2(P_{\text{stag}} - P_{\text{static}})/\rho}$.
4. **Atomizers, carburetors, aspirators:** fast-moving air creates low pressure that draws liquid up a tube.
5. **Roofs blown off in storms:** fast wind over the roof lowers pressure above it, while still air inside pushes up.
6. **Airplane wings (lift):** air flows faster over the upper surface, producing lower pressure there. *Caution:* the popular "equal transit time" explanation (air over the top must rejoin air under the bottom at the trailing edge) is **false** — air over the top actually arrives earlier. A complete explanation of lift involves the wing deflecting air downward (Newton's third law) and the circulation around the wing (Kutta–Joukowski theorem); Bernoulli's principle and Newton's laws are two consistent descriptions of the same flow.
7. **Curveballs (Magnus effect):** a spinning ball drags air around with it, creating a pressure difference that curves its path.

### Worked example 4.1
**Problem:** Water flows through a horizontal pipe that narrows from a diameter of 4 cm to 2 cm. In the wide section the speed is 1.5 m/s and the pressure is 200 kPa. Find the speed and pressure in the narrow section.

**Solution:** Area ratio $(4/2)^2 = 4$, so $v_2 = 4 \times 1.5 = 6$ m/s.
$P_2 = P_1 + \frac12\rho(v_1^2 - v_2^2) = 200\,000 + 500(2.25 - 36) = 200\,000 - 16\,875 = 183\,125$ Pa ≈ 183 kPa.

## 5. Real Fluids: Viscosity

**Viscosity** is a fluid's internal friction — resistance to shear. For a **Newtonian fluid** between plates, the shear stress is proportional to the velocity gradient:
$$\tau = \eta\frac{dv}{dy}$$
$\eta$ is the dynamic viscosity (Pa·s).

| Fluid | Viscosity at 20 °C (Pa·s) |
|---|---|
| Air | $1.8 \times 10^{-5}$ |
| Water | $1.0 \times 10^{-3}$ |
| Blood (37 °C) | ~$3$–$4 \times 10^{-3}$ |
| Olive oil | ~$0.08$ |
| Glycerin | ~$1.4$ |
| Honey | ~$2$–$10$ |

Liquid viscosity decreases with temperature (warm honey flows more easily); gas viscosity *increases* with temperature (because faster molecules transfer more momentum between layers).

**Non-Newtonian fluids** have viscosity that depends on shear rate: ketchup and paint thin under stress (shear-thinning); cornstarch–water mixture ("oobleck") stiffens under sudden stress (shear-thickening); toothpaste behaves as a solid until a threshold stress (Bingham plastic). Blood is mildly shear-thinning.

### Poiseuille's law
For steady laminar flow of a viscous fluid through a cylindrical pipe of radius $R$ and length $L$:
$$\boxed{Q = \frac{\pi R^4\,\Delta P}{8\eta L}}$$
The velocity profile is parabolic, maximal at the center and zero at the walls (no-slip condition).

**The $R^4$ dependence is dramatic:** halving a pipe's radius reduces flow 16-fold at the same pressure difference. In the body, arterioles regulate blood flow by small changes in radius; plaque narrowing an artery by 20% in radius requires the heart to supply about 2.4 times the pressure difference to maintain flow ($1/0.8^4 \approx 2.44$).

### Stokes' law
A small sphere of radius $r$ moving slowly through a viscous fluid experiences drag $F = 6\pi\eta rv$. Terminal velocity of a sphere of density $\rho_s$ in fluid $\rho_f$:
$$v_t = \frac{2r^2(\rho_s - \rho_f)g}{9\eta}$$
Used in Millikan's oil-drop experiment (to find droplet size) and to understand sedimentation and the slow settling of fine dust and fog droplets.

## 6. Laminar vs. Turbulent Flow: The Reynolds Number

At low speeds flow is **laminar** (smooth layers); at high speeds it becomes **turbulent** (chaotic eddies). The transition is governed by the dimensionless **Reynolds number**:
$$\boxed{Re = \frac{\rho vL}{\eta} = \frac{vL}{\nu}}$$
where $L$ is a characteristic length (pipe diameter) and $\nu = \eta/\rho$ is the kinematic viscosity. $Re$ compares inertial forces to viscous forces.

- Pipe flow: laminar for $Re \lesssim 2300$; turbulent for $Re \gtrsim 4000$.
- Swimming bacteria: $Re \sim 10^{-5}$ — inertia is irrelevant; if a bacterium stops swimming it halts within less than an atom's width. (E. M. Purcell's famous essay "Life at Low Reynolds Number".)
- Human swimmer: $Re \sim 10^6$. Commercial airliner: $Re \sim 10^7$–$10^8$.

Turbulence is one of the great unsolved problems of classical physics. The governing equations are the **Navier–Stokes equations**:
$$\rho\left(\frac{\partial\vec v}{\partial t} + (\vec v\cdot\nabla)\vec v\right) = -\nabla P + \eta\nabla^2\vec v + \rho\vec g$$
Proving whether smooth solutions always exist in 3D is one of the seven Clay Mathematics Institute Millennium Prize Problems ($1 million prize).

### Drag at high Reynolds number
$F_d = \frac12 C_d\rho Av^2$, where $C_d$ depends on shape ($\approx 0.47$ for a sphere, $\approx 0.04$ for a streamlined airfoil, $\approx 1.0$–$1.3$ for a person or a flat plate facing the flow). Golf ball dimples trigger a turbulent boundary layer that stays attached longer, shrinking the wake and roughly halving drag at typical driving speeds.

## 7. Surface Tension and Capillarity

Molecules at a liquid surface have fewer neighbors and higher energy than those in the bulk, so liquids minimize surface area. **Surface tension** $\gamma$ is the energy per unit area (or force per unit length): water at 20 °C has $\gamma \approx 0.073$ N/m.

Consequences:
- Small droplets and bubbles are spherical.
- Water striders and paperclips can rest on water.
- **Laplace pressure:** the pressure inside a spherical droplet exceeds the outside by $\Delta P = 2\gamma/r$ (a soap bubble with two surfaces: $4\gamma/r$). Smaller bubbles have higher internal pressure. In the lungs, **surfactant** lowers surface tension in alveoli to prevent small alveoli from collapsing; premature infants lacking surfactant suffer respiratory distress syndrome.
- **Capillary rise:** in a narrow tube of radius $r$, a wetting liquid rises to height $h = \frac{2\gamma\cos\theta}{\rho gr}$ (Jurin's law), where $\theta$ is the contact angle. Water rises in glass; mercury (non-wetting) is depressed. Capillarity helps (along with transpiration and cohesion) move water in plants and soil.
- Detergents (surfactants) lower surface tension, helping water wet and penetrate fabrics.

## 8. Summary

| Principle | Equation |
|---|---|
| Density | $\rho = m/V$ |
| Pressure | $P = F/A$ |
| Hydrostatic pressure | $P = P_0 + \rho gh$ |
| Pascal (hydraulics) | $F_2/F_1 = A_2/A_1$ |
| Archimedes | $F_B = \rho_{\text{fluid}}V_{\text{disp}}g$ |
| Continuity | $A_1v_1 = A_2v_2$ |
| Bernoulli | $P + \frac12\rho v^2 + \rho gy = $ const |
| Torricelli | $v = \sqrt{2gh}$ |
| Viscous stress | $\tau = \eta\,dv/dy$ |
| Poiseuille | $Q = \pi R^4\Delta P/(8\eta L)$ |
| Stokes drag | $F = 6\pi\eta rv$ |
| Reynolds number | $Re = \rho vL/\eta$ |
| Laplace pressure | $\Delta P = 2\gamma/r$ |
| Capillary rise | $h = 2\gamma\cos\theta/(\rho gr)$ |
