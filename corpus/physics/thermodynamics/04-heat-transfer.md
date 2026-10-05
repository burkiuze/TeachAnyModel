---
title: Heat Transfer: Conduction, Convection and Radiation
field: Physics
subfield: Thermodynamics
level: high-school to undergraduate
keywords: [heat transfer, conduction, Fourier's law, thermal conductivity, thermal resistance, R-value, U-factor, composite wall, critical radius of insulation, heat equation, thermal diffusivity, thermal effusivity, Newton's law of cooling, convection coefficient, Biot number, Nusselt number, Reynolds number, Prandtl number, natural convection, forced convection, blackbody radiation, Stefan-Boltzmann law, Wien's law, emissivity, Kirchhoff's law, radiative exchange, greenhouse effect, insulation, fins, heat sink, human thermoregulation]
---

# Heat Transfer: Conduction, Convection and Radiation

Thermodynamics tells us *how much* energy must flow for a system to move from one equilibrium state to another, and the second law tells us that heat flows spontaneously from hot to cold. Neither says *how fast*. Yet nearly every practical question about heat is a question of rate: How many watts does a house lose on a winter night? How large must a heat sink be to keep a processor below 90 °C? How long does a roast take to cook through? Why is a swim in 15 °C water dangerous when an afternoon in 15 °C air is pleasant? What sets the temperature of a planet? The discipline that answers these questions is **heat transfer**.

Energy moves as heat by three mechanisms: **conduction** (transfer through matter without bulk motion), **convection** (transfer between a surface and a moving fluid) and **radiation** (emission and absorption of electromagnetic waves). This chapter develops each from its basic law (Fourier's law, Newton's law of cooling, the Stefan–Boltzmann law) into working tools: thermal resistances and R-values, the heat equation and diffusion time scales, convection coefficients and dimensionless numbers, and radiative exchange. We then apply them to the greenhouse effect, insulation, heat sinks and the human body's heat balance.

## 1. Rates, Fluxes and the Three Mechanisms

Three quantities recur throughout:
- **Heat** $Q$, an amount of energy transferred because of a temperature difference (joules, J).
- **Heat transfer rate** $\dot Q = dQ/dt$ (watts, W).
- **Heat flux** $q'' = \dot Q/A$, the rate per unit area normal to the flow (W/m²).

A problem is **steady** when temperatures do not change with time and **transient** when they do. Every analysis applies energy conservation to a chosen region:
$$\text{rate in} - \text{rate out} + \text{rate of generation} = \text{rate of energy storage}$$

| Mechanism | What carries the energy | Basic rate law | Key dependence |
|---|---|---|---|
| Conduction | Molecular collisions, lattice vibrations (phonons), free electrons | $q'' = -k\,dT/dx$ | Proportional to temperature gradient |
| Convection | Moving fluid, with conduction in a thin layer at the wall | $q'' = h(T_s - T_\infty)$ | Proportional to temperature difference; $h$ depends on the flow |
| Radiation | Photons (mostly infrared at everyday temperatures) | $q'' = \varepsilon\sigma(T_s^4 - T_{\text{sur}}^4)$ | Fourth powers of absolute temperatures; needs no medium |

Usually two or three mechanisms act together: a room radiator warms the air by convection and the walls by radiation, after heat reached its surface by conduction through the metal.

## 2. Historical Development

| Year | Person(s) | Contribution |
|---|---|---|
| 1701 | Isaac Newton | Anonymous paper "Scala graduum caloris": cooling rate proportional to excess temperature, used to estimate temperatures of red-hot iron |
| 1756 | Johann Gottlob Leidenfrost | Water drops skittering on very hot metal on a vapor cushion |
| 1791 | Pierre Prévost | Theory of exchanges: every body radiates continually; equilibrium means equal emission and absorption |
| 1790s | Count Rumford (Benjamin Thompson) | Fluids conduct poorly and carry heat mainly by circulation; clothing and fur insulate by trapping air |
| 1800 | William Herschel | Discovered infrared radiation beyond the red end of the solar spectrum |
| 1804 | John Leslie | "Leslie cube": surfaces at one temperature radiate differently depending on finish |
| 1807, 1822 | Joseph Fourier | Memoir introducing the heat equation and trigonometric series (1807); *Théorie analytique de la chaleur* (1822) |
| 1824 | Joseph Fourier | Argued that the atmosphere keeps Earth's surface warmer — the first statement of the greenhouse idea |
| 1827 | Georg Ohm | Modeled electrical conduction on Fourier's heat conduction |
| 1834 | William Prout | Introduced the word "convection" |
| 1856, 1859 | Eunice Foote; John Tyndall | Foote: CO₂-filled vessels warm more in sunlight; Tyndall: measured infrared absorption by water vapor and CO₂ |
| 1859–1860 | Gustav Kirchhoff | Law of thermal radiation; the ideal "black body" |
| 1862 | William Thomson (Lord Kelvin) | Cooling-Earth estimate of Earth's age: 20 to 400 million years — far too short, because radioactive heating and mantle convection were unknown |
| 1879, 1884 | Josef Stefan; Ludwig Boltzmann | Stefan inferred the $T^4$ law from experiment; Boltzmann derived it from thermodynamics |
| 1883 | Osborne Reynolds | Dye experiments on laminar and turbulent pipe flow |
| 1892 | James Dewar | Silvered vacuum flask |
| 1893, 1900 | Wilhelm Wien; Max Planck | Displacement law; radiation law and the quantum of action |
| 1904 | Ludwig Prandtl | Boundary-layer theory |
| 1915 | Wilhelm Nusselt | Similarity analysis of convective heat transfer |

Fourier's work shaped mathematics as much as physics. The examiners of his 1807 memoir, Lagrange in particular, objected to representing arbitrary functions by trigonometric series. Fourier series and transforms, and the method of solving linear partial differential equations by superposing modes, grew from heat conduction.

## 3. Conduction and Fourier's Law

### 3.1 Statement of the law
For one-dimensional conduction through a cross-sectional area $A$, **Fourier's law** states:
$$\boxed{\dot Q_x = -kA\frac{dT}{dx}}$$
In three dimensions the heat flux is a vector, $\vec q\,'' = -k\nabla T$. The **thermal conductivity** $k$ (W/(m·K)) is a material property. The minus sign expresses the second law: heat flows *down* the gradient. Fourier's law is an empirical *constitutive* relation, like Ohm's or Hooke's law. It fails only in extreme cases such as structures smaller than the phonon mean free path or ultrafast laser heating. In **anisotropic** materials (wood along versus across the grain, layered graphite) $k$ becomes a tensor.

### 3.2 Microscopic mechanisms
- **Gases:** molecules carry energy between collisions. Kinetic theory gives $k \approx \tfrac13\rho c_v\bar v\lambda$ (density, specific heat per unit mass, mean speed, mean free path). Because $\lambda \propto 1/\rho$, $k$ is nearly *independent of pressure* until the mean free path approaches the container size. Light, fast molecules conduct best: helium and hydrogen conduct six to seven times better than air.
- **Liquids:** intermediate; water (0.61 W/(m·K)) is unusually good for a nonmetal.
- **Nonmetallic solids:** heat travels as lattice vibrations, **phonons**. Stiff bonds, light atoms and perfect crystals give high $k$ (diamond); disorder scatters phonons and gives low $k$ (glass, polymers).
- **Metals:** free electrons carry most of the heat as well as the current. The **Wiedemann–Franz law** (1853) states $k/(\sigma_eT) \approx L$, with the Lorenz number $L = \pi^2k_B^2/(3e^2) = 2.44\times10^{-8}$ W·Ω/K². For copper ($\sigma_e = 5.96\times10^7$ S/m at 293 K) it predicts $k \approx 427$ W/(m·K), within about 6% of the measured value.

### 3.3 Thermal conductivity data
Values near room temperature (about 300 K); manufactured materials vary with composition, density and moisture.

| Material | $k$ (W/(m·K)) | Material | $k$ (W/(m·K)) |
|---|---|---|---|
| Diamond (pure crystal) | 2000–2200 | Ice (0 °C) | 2.2 |
| Silver | 429 | Concrete | about 1.4 |
| Copper | 401 | Window glass | 0.8–1.4 |
| Gold | 317 | Common brick | 0.72 |
| Aluminium (pure) | 237 | Water (25 °C) | 0.61 |
| Silicon | 148 | Muscle tissue | about 0.5 |
| Brass | about 110 | Fat tissue | about 0.2 |
| Iron (pure) | 80 | Gypsum board | 0.17 |
| Carbon steel | 45–60 | Pine (across grain) | 0.12 |
| Lead | 35 | Mineral wool, fiberglass | 0.035–0.045 |
| Stainless steel (304) | 15 | Expanded polystyrene | 0.033–0.038 |
| Granite | about 2.8 | Polyurethane foam | 0.022–0.028 |
| Hydrogen gas | 0.183 | Air | 0.0263 |
| Helium gas | 0.152 | Argon | 0.0177 |
| Silica aerogel | about 0.015 | Carbon dioxide | 0.0166 |

The range spans five orders of magnitude, so material choice dominates thermal design. The best insulators are mostly gas; their job is to keep that gas still.

## 4. Thermal Resistance, R-Values and Composite Walls

### 4.1 Steady conduction through a plane wall
Consider a slab of thickness $L$ and area $A$ with faces held at $T_1$ and $T_2$, no internal heat generation and constant $k$.

1. In steady state the energy entering a thin slice between $x$ and $x + dx$ must equal the energy leaving it, so $\dot Q_x$ is the same at every $x$: $d\dot Q_x/dx = 0$.
2. Substituting Fourier's law: $\frac{d}{dx}\left(-kA\frac{dT}{dx}\right) = 0$, so $\frac{d^2T}{dx^2} = 0$.
3. Integrating twice: $T(x) = C_1x + C_2$. Applying $T(0) = T_1$ and $T(L) = T_2$ gives the linear profile $T(x) = T_1 - (T_1 - T_2)\,x/L$.
4. Then $dT/dx = -(T_1 - T_2)/L$ and
$$\boxed{\dot Q = \frac{kA(T_1 - T_2)}{L} = \frac{T_1 - T_2}{R_{\text{cond}}}, \qquad R_{\text{cond}} = \frac{L}{kA}}$$

### 4.2 The thermal-circuit analogy
This is Ohm's law, $I = \Delta V/R$, with temperature difference as voltage, heat rate as current and **thermal resistance** $R$ (K/W) as resistance. It applies to every mechanism whose rate is proportional to a temperature difference:

| Process | Thermal resistance |
|---|---|
| Conduction through a plane layer | $R = L/(kA)$ |
| Conduction through a cylindrical shell | $R = \ln(r_2/r_1)/(2\pi kL)$ |
| Convection from a surface | $R = 1/(hA)$ |
| Linearized radiation from a surface | $R = 1/(h_rA)$ |

Layers crossed in sequence are in **series**, $R_{\text{tot}} = \sum R_i$; side-by-side paths (a wooden stud beside insulation) are in **parallel**, $1/R_{\text{tot}} = \sum 1/R_i$. Where solids touch, microscopic air gaps add a **contact resistance** — hence thermal paste between a processor and its heat sink.

### 4.3 R-values and U-factors
Per unit area, a layer's **R-value** is $R'' = L/k$ (m²·K/W); series R-values add, and the **U-factor** is the reciprocal of the total:
$$U = \frac{1}{\sum R''_i}, \qquad \dot Q = UA\,\Delta T$$
In the United States, R-values are quoted in ft²·°F·h/BTU; the conversion is 1 ft²·°F·h/BTU = 0.1761 m²·K/W, or 1 m²·K/W = 5.678 US units. A US "R-19" batt has $R'' = 3.35$ m²·K/W. The air films on each side of a wall add resistance; standard design values are about 0.13 m²·K/W indoors and 0.04 m²·K/W outdoors.

### 4.4 Cylindrical shells and the critical radius of insulation
For a pipe or wire, the heat flows radially through surfaces whose area $2\pi rL$ grows with $r$.

1. In steady state the same $\dot Q$ crosses every cylindrical surface: $\dot Q = -k(2\pi rL)\,dT/dr$.
2. Separate variables: $dT = -\frac{\dot Q}{2\pi kL}\frac{dr}{r}$.
3. Integrate from $r_1$ to $r_2$: $T_1 - T_2 = \frac{\dot Q}{2\pi kL}\ln\frac{r_2}{r_1}$, so $R_{\text{cyl}} = \frac{\ln(r_2/r_1)}{2\pi kL}$.

Now add insulation of outer radius $r$ to a wire of radius $r_1$, with convection coefficient $h$ outside. The total resistance per unit length is
$$R'(r) = \frac{\ln(r/r_1)}{2\pi k} + \frac{1}{2\pi rh}$$
The first term grows with $r$, but the second shrinks because the outer surface area grows. Setting $dR'/dr = \frac{1}{2\pi kr} - \frac{1}{2\pi hr^2} = 0$ gives the **critical radius**
$$\boxed{r_c = \frac{k}{h}}$$
The second derivative is positive there, so $r_c$ is a *minimum* of resistance — a *maximum* of heat loss. For a wire thinner than $k/h$, a thin coat of insulation *increases* heat loss, which helps electrical cables stay cool; for large steam pipes $r_1 \gg r_c$ and insulation always helps. (For a sphere, $r_c = 2k/h$.)

### Worked example 4.1 – A single-pane window
**Problem:** A single-pane window, 1.2 m × 1.5 m, has glass 4.0 mm thick with $k = 1.0$ W/(m·K). Indoor air is at 20 °C and outdoor air at −5 °C. The inside and outside convection coefficients are 8 and 25 W/(m²·K). Find the heat loss, and compare with a naive estimate that ignores the air films.

1. Area: $A = 1.2 \times 1.5 = 1.8$ m²; $\Delta T = 25$ K.
2. Naive estimate (glass faces at the air temperatures): $\dot Q = kA\Delta T/L = 1.0 \times 1.8 \times 25/0.004 = 11\,250$ W. This is absurdly large.
3. Proper series resistance per unit area: $R'' = \frac{1}{8} + \frac{0.004}{1.0} + \frac{1}{25} = 0.125 + 0.004 + 0.040 = 0.169$ m²·K/W.
4. $U = 1/0.169 = 5.92$ W/(m²·K); flux $q'' = U\Delta T = 148$ W/m²; $\dot Q = q''A = 266$ W.
5. Inner glass surface temperature: $T = 20 - q''/h_i = 20 - 148/8 = 1.5$ °C.

**Answer:** about 270 W. The air films supply 98% of the resistance; the glass hardly matters, and its cold inner surface (1.5 °C) explains condensation and frost on single glazing. Double glazing (U ≈ 2.8 W/(m²·K)) and low-emissivity, argon-filled units (U ≈ 1.1–1.4) improve on this by adding gas layers and suppressing radiation, not by using better glass.

### Worked example 4.2 – An insulated masonry wall
**Problem:** A wall consists (inside to outside) of 13 mm gypsum board ($k = 0.17$), 90 mm mineral wool ($k = 0.040$) and 100 mm brick ($k = 0.72$), with film resistances 0.13 (inside) and 0.04 (outside) m²·K/W. The wall area is 40 m², indoors 20 °C, outdoors −5 °C. Find the R-value, U-factor, heat loss and the temperature at each interface.

1. Layer resistances: gypsum $0.013/0.17 = 0.0765$; wool $0.090/0.040 = 2.25$; brick $0.100/0.72 = 0.139$ m²·K/W.
2. Total: $R'' = 0.13 + 0.0765 + 2.25 + 0.139 + 0.04 = 2.64$ m²·K/W, equal to R-15.0 in US units.
3. $U = 1/2.64 = 0.379$ W/(m²·K); $q'' = 25/2.64 = 9.49$ W/m²; $\dot Q = 9.49 \times 40 = 379$ W (about 9.1 kWh per day).
4. Temperature drops are $q''R''_i$: inner surface $20 - 9.49 \times 0.13 = 18.8$ °C; gypsum/wool interface 18.0 °C; wool/brick interface −3.3 °C; outer brick surface −4.6 °C.
5. Without the wool, $R'' = 0.385$ and $\dot Q = 2590$ W — 6.8 times more.

**Answer:** $U \approx 0.38$ W/(m²·K), loss ≈ 380 W. Of the 25 K drop, 21.3 K occurs across the insulation, just as most of the voltage in a series circuit appears across the largest resistor. In a real wall, studs and fasteners act as parallel "thermal bridges" that raise the effective U-factor.

## 5. The Heat Equation and Thermal Diffusion

### 5.1 Derivation
Consider a slab element of area $A$ between $x$ and $x + dx$, with density $\rho$, specific heat $c$ and heat generation $\dot q$ per unit volume (W/m³, from electric current, reactions or metabolism).

1. Rate of storage: $\rho cA\,dx\,\frac{\partial T}{\partial t}$.
2. Net conduction in: $q''(x)A - q''(x + dx)A \approx -\frac{\partial q''}{\partial x}A\,dx$ (Taylor expansion to first order).
3. Generation: $\dot qA\,dx$.
4. Energy balance, dividing by $A\,dx$: $\rho c\frac{\partial T}{\partial t} = -\frac{\partial q''}{\partial x} + \dot q$.
5. Insert Fourier's law $q'' = -k\,\partial T/\partial x$ and take $k$ constant:
$$\boxed{\frac{\partial T}{\partial t} = \alpha\frac{\partial^2T}{\partial x^2} + \frac{\dot q}{\rho c}, \qquad \alpha = \frac{k}{\rho c}}$$
In three dimensions the divergence theorem gives $\partial T/\partial t = \alpha\nabla^2T + \dot q/(\rho c)$; in steady state without generation this is **Laplace's equation**, $\nabla^2T = 0$, which also governs electrostatic potential in charge-free space. The heat equation is the prototype **diffusion equation**, shared by dissolving molecules (Fick's law, 1855) and random walks.

### 5.2 Thermal diffusivity
The **thermal diffusivity** $\alpha$ (m²/s) measures how quickly a material *equalizes* temperature: $k$ spreads heat while the volumetric heat capacity $\rho c$ soaks it up. Conductivity governs steady flow; diffusivity governs how fast temperatures change.

| Material | $k$ (W/(m·K)) | $\rho$ (kg/m³) | $c$ (J/(kg·K)) | $\alpha$ (m²/s) | $L^2/\alpha$ for $L$ = 1 cm |
|---|---|---|---|---|---|
| Copper | 401 | 8933 | 385 | $1.17\times10^{-4}$ | 0.86 s |
| Aluminium | 237 | 2702 | 903 | $9.7\times10^{-5}$ | 1.0 s |
| Stainless steel 304 | 14.9 | 7900 | 477 | $3.95\times10^{-6}$ | 25 s |
| Granite | 2.79 | 2630 | 775 | $1.37\times10^{-6}$ | 73 s |
| Ice (0 °C) | 2.2 | 917 | 2050 | $1.17\times10^{-6}$ | 85 s |
| Pine | 0.12 | 510 | 1380 | $1.7\times10^{-7}$ | 590 s |
| Water (25 °C) | 0.607 | 997 | 4181 | $1.46\times10^{-7}$ | 690 s |
| Air (300 K, still) | 0.0263 | 1.161 | 1007 | $2.25\times10^{-5}$ | 4.4 s |

Air has a high diffusivity despite its tiny conductivity, because its heat capacity per unit volume is about 3500 times smaller than water's.

### 5.3 Time scales and the square-root law
If a temperature change must spread a distance $L$, then $\partial T/\partial t \sim \Delta T/t$ and $\alpha\,\partial^2T/\partial x^2 \sim \alpha\Delta T/L^2$. Balancing the two:
$$\boxed{t \sim \frac{L^2}{\alpha}, \qquad L \sim \sqrt{\alpha t}}$$
Diffusion time grows as the *square* of distance. Heat diffuses through 1 cm of water in about 10 minutes but through 1 m in about 80 days. Doubling the thickness of a steak roughly quadruples the time for its center to cook.

The exact solution for a **semi-infinite solid** initially at $T_i$ whose surface is suddenly held at $T_s$ makes this precise:
$$\frac{T(x,t) - T_s}{T_i - T_s} = \operatorname{erf}\left(\frac{x}{2\sqrt{\alpha t}}\right), \qquad q''_s(t) = \frac{k(T_s - T_i)}{\sqrt{\pi\alpha t}}$$
The disturbance penetrates a distance of order $2\sqrt{\alpha t}$, and the surface heat flux decays as $t^{-1/2}$. Similarly, heat released at a plane spreads as a Gaussian whose mean-square width grows as $\langle x^2\rangle = 2\alpha t$ — the same law Einstein derived for Brownian motion in 1905.

### 5.4 Periodic heating: why cellars stay cool
Suppose the ground surface temperature oscillates as $T_m + \Delta T\cos\omega t$ (daily or yearly cycle). We seek a solution of $\partial T/\partial t = \alpha\,\partial^2T/\partial x^2$ in the form $T = T_m + \operatorname{Re}[\Delta T\,e^{i\omega t - \kappa x}]$.

1. Substituting: $i\omega = \alpha\kappa^2$, so $\kappa = \sqrt{i\omega/\alpha}$.
2. Since $\sqrt{i} = (1 + i)/\sqrt2$, we get $\kappa = (1 + i)/\delta$ with **damping depth** $\delta = \sqrt{2\alpha/\omega}$.
3. Taking the real part:
$$T(x,t) = T_m + \Delta T\,e^{-x/\delta}\cos\left(\omega t - \frac{x}{\delta}\right)$$
The amplitude decays by a factor $e$ every depth $\delta$, and the phase lags by $x/\delta$ radians. Slow cycles (small $\omega$) penetrate deeper, as $\delta \propto \omega^{-1/2}$.

### Worked example 5.1 – Temperature waves in soil
**Problem:** Moist soil has $\alpha = 5.0\times10^{-7}$ m²/s. Find the damping depths for the daily and annual cycles, the annual amplitude and lag at 1 m and 2 m, and the depth where the annual swing falls to 1%.

1. Daily: $\omega = 2\pi/86\,400\ \text{s} = 7.27\times10^{-5}$ s⁻¹; $\delta = \sqrt{2(5.0\times10^{-7})/7.27\times10^{-5}} = 0.117$ m.
2. Annual: $\omega = 2\pi/(3.156\times10^7\ \text{s}) = 1.99\times10^{-7}$ s⁻¹; $\delta = 2.24$ m.
3. At 1 m: daily amplitude factor $e^{-1/0.117} = 2\times10^{-4}$ (negligible); annual factor $e^{-1/2.24} = 0.64$, lag $(1/2.24)/\omega = 26$ days.
4. At 2 m: annual factor 0.41, lag 52 days.
5. For 1%: $x = \delta\ln100 = 2.24 \times 4.61 = 10.3$ m.

**Answer:** δ ≈ 12 cm (daily) and 2.2 m (annual). Daily swings vanish within a few tens of centimetres; at 2 m the annual swing is 41% of the surface swing and about seven weeks late; below about 10 m the ground stays near the annual mean. Hence cool cellars, water pipes buried below the frost line, and ground-source heat pumps. At $x = \pi\delta \approx 7$ m the annual cycle is half a year out of phase.

### 5.5 Contact temperature and thermal effusivity
When two semi-infinite bodies at $T_1$ and $T_2$ touch, the interface jumps at once to a temperature $T_c$ that stays constant. Equating the surface fluxes from 5.3, $\sqrt{k_1\rho_1c_1}(T_1 - T_c) = \sqrt{k_2\rho_2c_2}(T_c - T_2)$, gives
$$T_c = \frac{e_1T_1 + e_2T_2}{e_1 + e_2}, \qquad e = \sqrt{k\rho c}$$
The **thermal effusivity** $e$, in SI units of $\text{W s}^{1/2}\text{ m}^{-2}\text{ K}^{-1}$, decides what a surface *feels* like. Skin ($e \approx 1200$) at 33 °C touching objects at 20 °C reaches about 21.8 °C on stainless steel ($e \approx 7500$), 20.6 °C on aluminium ($e \approx 24\,000$) but 30.5 °C on pine ($e \approx 290$). Nerves sense the contact temperature, so metal "feels colder" than wood in the same room.

## 6. Convection

### 6.1 Newton's law of cooling and the boundary layer
Convection is the transfer between a surface at $T_s$ and a fluid whose temperature far from the surface is $T_\infty$. Its rate law is written as
$$\boxed{\dot Q = hA(T_s - T_\infty)}$$
where $h$ (W/(m²·K)) is the **convection heat transfer coefficient**. In modern use this "law" is really a *definition* of $h$, packing the complexity of the flow into one number to be measured or calculated.

The physical picture is Prandtl's boundary layer. Fluid touching the wall is at rest (no slip), so at the wall heat passes by pure conduction, $q'' = -k_f\,(\partial T/\partial y)_{y=0}$; further out, moving fluid sweeps it away. Faster, more turbulent flow thins the thermal boundary layer, steepens the wall gradient and raises $h$; roughly $h \approx k_f/\delta_t$, with $\delta_t$ the layer thickness.

### 6.2 Lumped-capacitance cooling and the Biot number
If a small object conducts heat internally much faster than its surface sheds it, its temperature stays nearly uniform, and an energy balance on the whole body gives:

1. $mc\,\frac{dT}{dt} = -hA(T - T_\infty)$, with $m = \rho V$.
2. Let $\theta = T - T_\infty$: $\frac{d\theta}{dt} = -\frac{\theta}{\tau}$, where $\tau = \frac{\rho cV}{hA}$.
3. Integrating from $\theta_0$ at $t = 0$:
$$\boxed{T(t) = T_\infty + (T_0 - T_\infty)e^{-t/\tau}, \qquad \tau = \frac{\rho cV}{hA}}$$
The time constant $\tau$ is a thermal "RC time": capacitance $\rho cV$ times resistance $1/(hA)$.

The approximation is valid when the **Biot number**
$$\text{Bi} = \frac{hL_c}{k_{\text{solid}}}, \qquad L_c = \frac{V}{A}$$
is less than about 0.1. Bi is the ratio of internal conduction resistance $L_c/(kA)$ to external convection resistance $1/(hA)$. Large Bi means steep internal gradients (a thick roast in an oven) that require the full heat equation.

### Worked example 6.1 – Cooling a copper sphere
**Problem:** A polished copper sphere ($\rho = 8933$ kg/m³, $c = 385$ J/(kg·K), $k = 401$ W/(m·K)) of diameter 2.0 cm is taken from an oven at 200 °C into air at 25 °C with $h = 15$ W/(m²·K). How long until it reaches 50 °C?

1. $L_c = V/A = D/6 = 3.33\times10^{-3}$ m.
2. $\text{Bi} = 15 \times 3.33\times10^{-3}/401 = 1.2\times10^{-4} \ll 0.1$, so the lumped model is excellent.
3. $\tau = \rho cL_c/h = 8933 \times 385 \times 3.33\times10^{-3}/15 = 764$ s.
4. $t = \tau\ln\frac{T_0 - T_\infty}{T - T_\infty} = 764\ln\frac{175}{25} = 764 \times 1.946 = 1490$ s.
5. Check radiation: with $\varepsilon \approx 0.03$ for polished copper, the initial radiative loss is about 0.09 W against a convective loss of 3.3 W, so neglecting it is justified.

**Answer:** about 1490 s ≈ 25 min.

### 6.3 Typical convection coefficients

| Situation | $h$ (W/(m²·K)) |
|---|---|
| Natural convection, gases | 2–25 |
| Natural convection, liquids | 50–1000 |
| Forced convection, gases | 25–250 |
| Forced convection, liquids | 100–20 000 |
| Boiling or condensation | 2500–100 000 |

Liquids beat gases through higher conductivity and heat capacity; phase change beats everything because latent heat carries large energy at nearly constant temperature.

### 6.4 Natural versus forced convection
In **forced convection** a fan, pump, wind or the object's own motion drives the flow: a car radiator, a hair dryer, wind chill on skin. In **natural (free) convection** buoyancy drives it: fluid warmed by a hot surface expands, becomes less dense and rises, drawing cooler fluid in behind. Natural convection drives sea breezes, thunderstorms, the plume above a candle, mantle convection inside Earth and the outer 30% (by radius) of the Sun.

Because the temperature difference itself creates the flow, $h$ depends on $\Delta T$: for laminar flow on a vertical plate $h \propto \Delta T^{1/4}$, so the flux grows as $\Delta T^{5/4}$ and Newton's law of cooling is only approximate. Without gravity there is no buoyant convection — a candle flame in orbit is a dim sphere fed only by diffusion.

### 6.5 Dimensionless numbers
Convection depends on velocity $V$, size $L$, and fluid density, viscosity, conductivity and specific heat. Dimensional analysis collapses these into a few dimensionless groups, so one experiment on a model predicts many real situations.

| Number | Definition | Physical meaning |
|---|---|---|
| Reynolds | $\text{Re} = \rho VL/\mu = VL/\nu$ | Inertial forces relative to viscous forces; decides laminar versus turbulent flow |
| Prandtl | $\text{Pr} = \nu/\alpha = c_p\mu/k$ | Momentum diffusivity relative to thermal diffusivity (a fluid property) |
| Nusselt | $\text{Nu} = hL/k_{\text{fluid}}$ | Convective enhancement over pure conduction across the fluid layer |
| Grashof | $\text{Gr} = g\beta\Delta TL^3/\nu^2$ | Buoyancy relative to viscous forces (natural convection) |
| Rayleigh | $\text{Ra} = \text{Gr}\cdot\text{Pr}$ | Strength of buoyant driving; onset of natural convection |
| Biot | $\text{Bi} = hL/k_{\text{solid}}$ | Internal versus external resistance of a *solid* body |

Here $\nu = \mu/\rho$ is the kinematic viscosity and $\beta$ the volumetric expansion coefficient. Typical Prandtl numbers: air ≈ 0.71, water ≈ 7 at 20 °C, engine oils hundreds to thousands, liquid mercury ≈ 0.025. When Pr is large, the thermal boundary layer is much thinner than the velocity boundary layer; in liquid metals it is much thicker. Nu and Bi look alike, but Nu uses the *fluid* conductivity and is the unknown to be found, while Bi uses the *solid* conductivity and compares two resistances.

Results are expressed as correlations, $\text{Nu} = f(\text{Re}, \text{Pr})$ for forced flow or $\text{Nu} = f(\text{Ra}, \text{Pr})$ for natural flow. Examples: laminar flow over a flat plate, $\overline{\text{Nu}}_L = 0.664\,\text{Re}_L^{1/2}\text{Pr}^{1/3}$ (valid for $\text{Re}_L$ below about $5\times10^5$ and Pr above about 0.6); fully developed laminar pipe flow, Nu = 3.66 (uniform wall temperature) or 4.36 (uniform heat flux); turbulent pipe flow, the Dittus–Boelter correlation $\text{Nu} = 0.023\,\text{Re}^{0.8}\text{Pr}^{n}$ with $n = 0.4$ for heating and 0.3 for cooling the fluid. Pipe flow becomes turbulent above Re ≈ 2300.

### Worked example 6.2 – Forced convection over a flat plate
**Problem:** Air at about 300 K ($\nu = 1.589\times10^{-5}$ m²/s, $k = 0.0263$ W/(m·K), Pr = 0.707) blows at 5.0 m/s along a 0.50 m × 0.50 m plate held at 60 °C; the air is at 20 °C. Estimate $h$ and the heat loss from one face. (For simplicity we use properties at 300 K rather than at the mean film temperature.)

1. $\text{Re}_L = VL/\nu = 5.0 \times 0.50/1.589\times10^{-5} = 1.57\times10^5$, below $5\times10^5$, so the boundary layer is laminar.
2. $\overline{\text{Nu}}_L = 0.664 \times (1.57\times10^5)^{1/2} \times 0.707^{1/3} = 0.664 \times 396.7 \times 0.891 = 235$.
3. $h = \text{Nu}\,k/L = 235 \times 0.0263/0.50 = 12.3$ W/(m²·K).
4. $\dot Q = hA\Delta T = 12.3 \times 0.25 \times 40 = 123$ W.
5. Velocity boundary-layer thickness at the trailing edge: $\delta \approx 5L/\sqrt{\text{Re}_L} = 6.3$ mm; the thermal layer is similar, $\delta/\text{Pr}^{1/3} \approx 7$ mm. All the temperature change happens within a few millimetres of the plate.

**Answer:** $h \approx 12$ W/(m²·K), $\dot Q \approx 120$ W — 235 times (the Nusselt number) the rate of pure conduction through a 0.5 m layer of still air.

### 6.6 Boiling and condensation
When a heated surface exceeds the liquid's saturation temperature, vapor bubbles nucleate, grow and depart, stirring the liquid violently. This **nucleate boiling** gives the highest $h$ values in common use. On a much hotter surface a continuous vapor film forms and insulates it (**film boiling**), so the heat flux can actually *fall* as the surface gets hotter; a water drop dancing on a very hot pan (the Leidenfrost effect) is film boiling in miniature. Condensation is equally effective, which is why steam burns are severe and power-plant condensers are compact.

## 7. Thermal Radiation

### 7.1 Blackbody radiation
Every body above absolute zero emits electromagnetic radiation because its charged constituents are in thermal motion. An ideal **blackbody** absorbs all incident radiation at every wavelength and direction; thermodynamics then requires it to be the best possible emitter at each wavelength. Its spectrum is given by **Planck's law** for the spectral radiance (power per unit area, solid angle and wavelength; in Sections 7.1 and 7.2 $h$ denotes Planck's constant, not a convection coefficient):
$$B_\lambda(T) = \frac{2hc^2}{\lambda^5}\frac{1}{e^{hc/(\lambda k_BT)} - 1}$$
The total power emitted per unit area — the **emissive power** — is the **Stefan–Boltzmann law**:
$$\boxed{E_b = \sigma T^4, \qquad \sigma = 5.670374\times10^{-8}\ \text{W/(m}^2\text{K}^4)}$$
and the spectrum peaks at a wavelength given by **Wien's displacement law**:
$$\boxed{\lambda_{\max}T = b = 2.897772\times10^{-3}\ \text{m}\cdot\text{K}}$$

| Source | $T$ (K) | $\lambda_{\max}$ | $\sigma T^4$ (W/m²) |
|---|---|---|---|
| Cosmic microwave background | 2.725 | 1.06 mm | $3.1\times10^{-6}$ |
| Earth's surface (mean) | 288 | 10.1 μm | 390 |
| Human skin (approx.) | 307 | 9.4 μm | 503 |
| Red-hot steel | 1000 | 2.9 μm | $5.7\times10^4$ |
| Incandescent filament | 3000 | 0.97 μm | $4.6\times10^6$ |
| Sun's photosphere | 5772 | 502 nm | $6.29\times10^7$ |

Everyday objects radiate almost entirely in the infrared, so thermal cameras work at about 8–14 μm, and an incandescent bulb is mostly a heater because most of its output lies beyond the visible.

### 7.2 Deriving the Stefan–Boltzmann and Wien laws from Planck's law
**Stefan–Boltzmann.** Blackbody radiance is the same in all directions, and integrating radiance over a hemisphere weighted by $\cos\theta$ (the projected area) gives a factor $\pi$.

1. In frequency form, $B_\nu = \frac{2h\nu^3}{c^2}\frac{1}{e^{h\nu/k_BT} - 1}$, and $E_b = \pi\int_0^\infty B_\nu\,d\nu$.
2. Substitute $x = h\nu/(k_BT)$, so $\nu = k_BTx/h$ and $d\nu = (k_BT/h)\,dx$:
$$E_b = \frac{2\pi h}{c^2}\left(\frac{k_BT}{h}\right)^4\int_0^\infty\frac{x^3}{e^x - 1}\,dx$$
3. The integral is a pure number, $\int_0^\infty x^3/(e^x - 1)\,dx = \pi^4/15 \approx 6.494$.
4. Hence
$$E_b = \frac{2\pi^5k_B^4}{15h^3c^2}T^4 = \sigma T^4$$
Inserting the exact SI values of $h$, $k_B$ and $c$ gives $\sigma = 5.670374\times10^{-8}$ W/(m²·K⁴) — a constant Stefan had found empirically, now computed from fundamental constants.

**Wien.** Write $B_\lambda \propto \lambda^{-5}(e^{a/\lambda} - 1)^{-1}$ with $a = hc/(k_BT)$.

1. Set $dB_\lambda/d\lambda = 0$: $-5\lambda^{-6}(e^{a/\lambda} - 1)^{-1} + \lambda^{-5}(e^{a/\lambda} - 1)^{-2}e^{a/\lambda}a\lambda^{-2} = 0$.
2. Multiply through by $\lambda^6(e^{a/\lambda} - 1)^2$ and let $x = a/\lambda$: $5(e^x - 1) = xe^x$, i.e. $x = 5(1 - e^{-x})$.
3. Solving numerically: $x = 4.965114$.
4. Therefore $\lambda_{\max}T = hc/(4.965114\,k_B) = 2.897772\times10^{-3}$ m·K.

Per unit *frequency*, the same steps give $x = 3(1 - e^{-x})$, $x = 2.821$, and a peak at $\nu_{\max} = (5.88\times10^{10}\ \text{Hz/K})\,T$, in a different part of the spectrum. The "peak" depends on how the spectrum is plotted; the total power does not.

### 7.3 Real surfaces: emissivity, absorptivity and Kirchhoff's law
A real surface emits less than a blackbody. Its **emissivity** $\varepsilon$ (0 to 1) is the ratio of its emission to blackbody emission at the same temperature, so $E = \varepsilon\sigma T^4$. Radiation striking a surface is partly absorbed, reflected or transmitted, with fractions satisfying
$$\alpha + \rho + \tau = 1$$
(here $\alpha$ is absorptivity and $\rho$ reflectivity, not diffusivity and density). For an opaque surface $\tau = 0$.

**Kirchhoff's law** (1859–1860): at each wavelength and direction, a surface absorbs exactly as well as it emits, $\varepsilon_\lambda = \alpha_\lambda$; otherwise a body in an isothermal enclosure could spontaneously heat or cool itself, violating the second law. Good absorbers are good emitters; good reflectors are poor emitters.

A **gray body** has $\varepsilon_\lambda$ independent of wavelength, so $\varepsilon = \alpha$ for any incident spectrum. Few surfaces are gray across the range from sunlight (peak near 0.5 μm) to thermal infrared (peak near 10 μm), so solar absorptivity $\alpha_s$ can differ greatly from infrared emissivity $\varepsilon$:

| Surface | Solar absorptivity $\alpha_s$ | Infrared emissivity $\varepsilon$ |
|---|---|---|
| Polished aluminium | 0.09 | 0.03 |
| Anodized aluminium | 0.14 | 0.84 |
| White acrylic paint | 0.26 | 0.90 |
| Black paint | 0.98 | 0.98 |
| Polished silver | — | about 0.02 |
| Human skin | depends on pigmentation | 0.97–0.98 |
| Water, glass, brick, concrete | — | 0.90–0.96 |

White paint reflects sunlight yet radiates infrared almost like a blackbody, so white roofs stay cool. Window glass transmits most sunlight but is opaque and highly emissive in the thermal infrared. **Selective surfaces** on solar collectors combine high $\alpha_s$ with low $\varepsilon$, absorbing sunlight while radiating little.

### 7.4 Radiative exchange between surfaces
Because all surfaces emit, the *net* exchange is what matters. The fraction of radiation leaving surface 1 that strikes surface 2 directly is the **view factor** $F_{12}$, a geometric quantity obeying reciprocity, $A_1F_{12} = A_2F_{21}$.

For diffuse gray surfaces, define the **radiosity** $J$ — all radiation leaving a surface, emitted plus reflected: $J = \varepsilon E_b + (1 - \varepsilon)G$, where $G$ is the incident irradiation. The net loss from the surface is $\dot Q = A(J - G)$.

1. Solve the radiosity definition for $G$: $G = \frac{J - \varepsilon E_b}{1 - \varepsilon}$.
2. Substitute: $\dot Q = A\left(J - \frac{J - \varepsilon E_b}{1 - \varepsilon}\right) = \frac{E_b - J}{(1 - \varepsilon)/(\varepsilon A)}$. Each surface thus has a **surface resistance** $(1 - \varepsilon)/(\varepsilon A)$.
3. The net exchange between two surfaces that see only each other is $(J_1 - J_2)A_1F_{12}$, a **space resistance** $1/(A_1F_{12})$.
4. In series:
$$\dot Q_{12} = \frac{\sigma(T_1^4 - T_2^4)}{\dfrac{1 - \varepsilon_1}{\varepsilon_1A_1} + \dfrac{1}{A_1F_{12}} + \dfrac{1 - \varepsilon_2}{\varepsilon_2A_2}}$$
Two important special cases:
- **Large parallel plates** ($A_1 = A_2$, $F_{12} = 1$):
$$q''_{12} = \frac{\sigma(T_1^4 - T_2^4)}{1/\varepsilon_1 + 1/\varepsilon_2 - 1}$$
- **Small body in a large enclosure** ($A_1/A_2 \to 0$, $F_{12} = 1$): $\dot Q = \varepsilon_1\sigma A_1(T_1^4 - T_2^4)$. The enclosure's emissivity drops out because a large enclosure acts like a blackbody cavity.

### 7.5 The radiation heat transfer coefficient
Factoring the difference of fourth powers, $T_s^4 - T_{\text{sur}}^4 = (T_s - T_{\text{sur}})(T_s + T_{\text{sur}})(T_s^2 + T_{\text{sur}}^2)$, lets radiation be written in Newton's-law form:
$$\dot Q = h_rA(T_s - T_{\text{sur}}), \qquad h_r = \varepsilon\sigma(T_s + T_{\text{sur}})(T_s^2 + T_{\text{sur}}^2) \approx 4\varepsilon\sigma T_m^3$$
where $T_m$ is the mean absolute temperature. Near room temperature $h_r \approx 6$ W/(m²·K) for $\varepsilon = 1$, comparable to natural convection in air, so radiation is never negligible in still air; at high temperatures it dominates because $h_r$ grows as $T^3$.

### Worked example 7.1 – Radiation in a liquid-nitrogen container
**Problem:** The walls of a vacuum-insulated container can be modeled as large parallel plates at 300 K and 77 K (liquid nitrogen), with 0.50 m² of wall area. Find the radiative heat leak with silvered walls ($\varepsilon = 0.05$ on both sides) and with unsilvered walls ($\varepsilon = 0.9$), and the nitrogen boil-off rate ($h_{fg} = 199$ kJ/kg, liquid density 807 kg/m³).

1. $T_1^4 - T_2^4 = 300^4 - 77^4 = 8.100\times10^9 - 3.5\times10^7 = 8.065\times10^9$ K⁴, and $\sigma \times 8.065\times10^9 = 457$ W/m².
2. Silvered: denominator $1/0.05 + 1/0.05 - 1 = 39$; $q'' = 457/39 = 11.7$ W/m²; $\dot Q = 5.9$ W.
3. Unsilvered: denominator $2/0.9 - 1 = 1.22$; $q'' = 374$ W/m²; $\dot Q = 187$ W.
4. Boil-off (silvered): $\dot m = 5.9/199\,000 = 2.9\times10^{-5}$ kg/s = 0.106 kg/h ≈ 0.13 L/h ≈ 3.2 L per day. Unsilvered: 3.4 kg/h.

**Answer:** about 6 W versus 190 W — silvering cuts the leak by a factor of 32. The vacuum removes conduction and convection; low emissivity attacks the radiation that remains. This is the principle of Dewar's flask.

## 8. Planetary Energy Balance and the Greenhouse Effect

A planet exchanges energy with space only by radiation. Earth intercepts sunlight on its cross-section $\pi R^2$ but radiates from its whole surface $4\pi R^2$.

1. Absorbed: $\pi R^2S(1 - a)$, with solar constant $S = 1361$ W/m² and albedo (reflected fraction) $a \approx 0.30$.
2. Emitted (treating Earth as a blackbody in the infrared): $4\pi R^2\sigma T_e^4$.
3. Equating: 
$$\boxed{T_e = \left[\frac{S(1 - a)}{4\sigma}\right]^{1/4}}$$
With the numbers, $S(1 - a)/4 = 238$ W/m² and $T_e = 255$ K (−18 °C). The observed mean surface temperature is about 288 K (15 °C). The 33 K difference is the **greenhouse effect**.

**A one-layer model.** Let the atmosphere be a single layer at $T_a$, transparent to sunlight but absorbing a fraction $\varepsilon$ of the infrared emitted by the surface (and therefore, by Kirchhoff's law, emitting $\varepsilon\sigma T_a^4$ both upward and downward).

1. Atmosphere balance: absorbed $\varepsilon\sigma T_s^4$ = emitted $2\varepsilon\sigma T_a^4$, so $T_a^4 = T_s^4/2$.
2. Top-of-atmosphere balance: absorbed sunlight equals the outgoing infrared, i.e. the layer's emission plus the surface emission that leaks through: $\sigma T_e^4 = \varepsilon\sigma T_a^4 + (1 - \varepsilon)\sigma T_s^4 = \sigma T_s^4(1 - \varepsilon/2)$.
3. Therefore
$$T_s = T_e\left(\frac{2}{2 - \varepsilon}\right)^{1/4}$$
A fully absorbing layer ($\varepsilon = 1$) gives $T_s = 2^{1/4}T_e = 303$ K, too warm; an absorptivity of about 0.78 reproduces 288 K.

The model is crude — real air cools with height, convection carries much surface heat upward, and absorption varies strongly with wavelength — but it captures the essential physics. Greenhouse gases (H₂O, CO₂, CH₄, N₂O, O₃) pass most sunlight but absorb parts of the thermal infrared; CO₂ has a strong band near 15 μm, close to the 10 μm peak of Earth's emission. Adding CO₂ raises the altitude from which infrared escapes to space; the air there is colder and emits less, so the surface must warm until balance is restored.

### Worked example 8.1 – Forcing and the no-feedback response
**Problem:** A widely used simplified expression gives the radiative forcing of CO₂ as $\Delta F = 5.35\ln(C/C_0)$ W/m² (Myhre and co-workers, 1998). Find the forcing for a doubling of CO₂ and the warming it would cause if Earth simply radiated more as a blackbody at $T_e$, with no feedbacks.

1. $\Delta F = 5.35\ln2 = 3.71$ W/m².
2. Linearize $E = \sigma T_e^4$: $dE/dT = 4\sigma T_e^3 = 4 \times 5.670\times10^{-8} \times 254.6^3 = 3.74$ W/(m²·K).
3. $\Delta T = \Delta F/(4\sigma T_e^3) = 3.71/3.74 = 0.99$ K.

**Answer:** about 3.7 W/m² and roughly 1 K of warming before feedbacks. Feedbacks — chiefly increased water vapor, reduced snow and ice cover, and changes in clouds — amplify this; the IPCC's Sixth Assessment Report (2021) gave a best estimate of 3 °C for the equilibrium warming from doubled CO₂, with a likely range of 2.5–4 °C. Atmospheric CO₂ has risen from about 280 ppm before industrialization to above 420 ppm in the 2020s, a forcing of $5.35\ln(420/280) \approx 2.2$ W/m².

## 9. Insulation, Fins and Heat Sinks

### 9.1 How insulation works
Still air conducts poorly (0.026 W/(m·K)), but an air gap more than about a centimetre wide starts to convect (the exact width depends on the temperature difference), and air passes radiation. Mineral wool, fiberglass, foams, feathers, fur and fabrics divide air into tiny cells that suppress convection and block radiation, so their conductivity approaches that of still air; foams blown with heavier gases do slightly better. **Silica aerogel** (about 0.015 W/(m·K)) beats still air because its pores, mostly tens of nanometres across, are smaller than the mean free path of air molecules (about 70 nm at room conditions), so molecules hit pore walls more often than one another.

**Vacuum insulation panels** and Dewar flasks remove the gas altogether; **multilayer insulation** (MLI) on spacecraft stacks dozens of reflective films in vacuum to defeat radiation (see Practice Problem 9). Windows use argon or krypton fills and low-emissivity coatings. Clothing insulation is measured in **clo**: 1 clo = 0.155 m²·K/W, roughly a business suit (a unit introduced by Gagge, Burton and Bazett in 1941).

### 9.2 Fins: extending the surface
When convection is the bottleneck, **fins** add surface area. Consider a straight fin of cross-section $A_c$, perimeter $P$ and conductivity $k$, with base at $T_b$ in fluid at $T_\infty$.

1. Energy balance on a fin element $dx$: conduction in minus conduction out equals convection from its side, $-\frac{d}{dx}\left(-kA_c\frac{dT}{dx}\right)dx = hP\,dx\,(T - T_\infty)$.
2. With $\theta = T - T_\infty$ and $m^2 = hP/(kA_c)$: $\frac{d^2\theta}{dx^2} - m^2\theta = 0$.
3. For a fin of length $L$ with an insulated tip ($d\theta/dx = 0$ at $x = L$) and $\theta(0) = \theta_b$, the solution is $\theta(x) = \theta_b\frac{\cosh m(L - x)}{\cosh mL}$.
4. The heat entering the base is $\dot Q_f = -kA_c\,(d\theta/dx)_{x=0}$:
$$\dot Q_f = \sqrt{hPkA_c}\,\theta_b\tanh mL$$
5. The **fin efficiency** compares this with the ideal of a fin entirely at $T_b$:
$$\eta_f = \frac{\dot Q_f}{hPL\,\theta_b} = \frac{\tanh mL}{mL}$$
For a thin plate fin of thickness $t$, $m \approx \sqrt{2h/(kt)}$. Good fins are thin, closely spaced and made of aluminium or copper; beyond $mL \approx 2$ extra length adds little because the tip is already near the fluid temperature.

### Worked example 9.1 – Sizing a processor heat sink
**Problem:** A processor dissipates 95 W. The junction-to-case resistance is 0.25 K/W and the thermal paste adds 0.10 K/W. Air inside the computer case is at 35 °C, and the junction must stay at or below 90 °C. (a) What sink-to-air resistance is required? (b) With fan-forced air ($h = 40$ W/(m²·K)) and aluminium-alloy fins ($k = 200$ W/(m·K)) 1.0 mm thick and 30 mm tall, how much finned area is needed?

1. Total allowed resistance: $(90 - 35)/95 = 0.579$ K/W.
2. Required $R_{sa} = 0.579 - 0.25 - 0.10 = 0.229$ K/W.
3. Fin parameter: $m = \sqrt{2 \times 40/(200 \times 0.001)} = 20$ m⁻¹; $mL = 0.60$; $\eta_f = \tanh(0.60)/0.60 = 0.537/0.60 = 0.895$.
4. Since fins provide nearly all the area, $R_{sa} \approx 1/(\eta_fhA)$, so $A = 1/(0.895 \times 40 \times 0.229) = 0.122$ m².
5. Each fin 40 mm deep × 30 mm tall has two faces totalling $2.4\times10^{-3}$ m², so about 51 fins are needed. The 0.122 m² is about 76 times the 4 cm × 4 cm footprint of the chip package.
6. Check: a small cooler with $R_{sa} = 0.50$ K/W would give $T_j = 35 + 95(0.85) = 116$ °C, so the chip would throttle.

**Answer:** $R_{sa} \le 0.23$ K/W, requiring about 0.12 m² of fin area. **Heat pipes** — sealed tubes in which a fluid evaporates at the hot end and condenses at the cold end — often carry heat from the small chip to the large fin stack with very little temperature drop.

### 9.3 Further applications
- **Industry:** heat exchangers in power plants and refineries; quenching of steel, where the Biot number and boiling regime control hardness and cracking; furnaces and casting; liquefied-gas storage.
- **Buildings:** codes are written in R-values and U-factors; thermal mass (high $\rho c$) smooths daily swings; ground-source heat pumps use the stable temperature a few metres down.
- **Space:** with no air, spacecraft rely on conduction to radiators and on MLI; the International Space Station rejects heat through ammonia loops and large radiator panels.
- **Medicine:** infrared thermography and ear thermometers read emitted radiation; radiant warmers keep newborns warm; therapeutic hypothermia cools patients after cardiac arrest; cryosurgery destroys tissue by controlled freezing.
- **Nature:** elephants shed heat through large, blood-rich ears; whales and seals rely on blubber; countercurrent exchange in the legs of wading birds returns heat to the core; animals of cold climates tend to be larger (Bergmann's rule), partly because surface area grows more slowly than volume.

## 10. The Human Body's Heat Balance

The body must hold its core near 37 °C while producing heat continuously. Its energy balance is
$$M - W = C + R + E + K + S$$
where $M$ is metabolic power, $W$ mechanical work done, $C$ convection, $R$ radiation, $E$ evaporation (sweat and breath), $K$ conduction to touching surfaces and $S$ the rate of heat storage. When $S > 0$ for long, core temperature rises (heat illness); when $S < 0$, it falls (hypothermia).

- **Metabolism:** at rest about 80–100 W for an adult. The unit 1 met = 58.2 W/m² of body surface, about 105 W for a typical surface area of 1.8 m². Hard exercise raises $M$ tenfold or more, and muscles are only about 20–25% efficient, so most of the energy becomes heat.
- **Radiation and convection:** skin has $\varepsilon \approx 0.97$; in a comfortable room each removes tens of watts.
- **Evaporation:** each kilogram of evaporated sweat removes about 2.4 MJ, so 1 L/h carries away about 670 W. When the air is hotter than the skin, evaporation is the *only* cooling route, and high humidity cripples it.
- **Control:** the hypothalamus regulates skin blood flow. Vasodilation turns tissue into a "variable conductor" bringing core heat to the skin; vasoconstriction turns skin and fat into insulation. Shivering raises $M$; brown fat produces heat directly.

Cold water is dangerous because its conductivity is about 23 times that of air and its convection coefficients are tens of times larger, so immersion strips heat far faster than air at the same temperature.

### Worked example 10.1 – A cyclist on a warm day
**Problem:** A cyclist has a metabolic rate of 600 W and delivers 150 W of mechanical power. Skin area is 1.8 m², skin temperature 35 °C, emissivity 0.97. Air and surroundings are at 30 °C, and riding gives $h_c = 20$ W/(m²·K). Neglect breathing, conduction and sunlight, and use the same area for convection and radiation. How much sweat must evaporate to stay in balance? Repeat for air and surroundings at 40 °C.

1. Heat to dissipate: $M - W = 600 - 150 = 450$ W.
2. Convection: $C = 20 \times 1.8 \times (35 - 30) = 180$ W.
3. Radiation: $R = 0.97 \times 5.670\times10^{-8} \times 1.8 \times (308.15^4 - 303.15^4) = 56.5$ W.
4. Evaporation: $E = 450 - 180 - 56.5 = 213$ W; sweat rate $213/(2.42\times10^6\ \text{J/kg}) = 8.8\times10^{-5}$ kg/s = 0.32 kg/h.
5. At 40 °C: $C = 20 \times 1.8 \times (35 - 40) = -180$ W and $R = -59.4$ W (both are now *gains*), so $E = 450 + 180 + 59.4 = 689$ W, requiring 1.0 kg/h of evaporated sweat.

**Answer:** about 0.3 kg/h at 30 °C but about 1 kg/h at 40 °C — near the limit of human sweating, and possible only if the air is dry enough for sweat to evaporate. Hence the importance of wet-bulb temperature, which combines heat and humidity: a wet-bulb temperature of 35 °C has been proposed as an upper limit for prolonged survival, and laboratory studies suggest the practical limit for many people is lower.

## 11. Common Misconceptions

- **"Cold flows in through the window."** There is no flow of "cold"; heat flows out, and the interior cools because it loses energy.
- **"Metal objects in a room are colder than wooden ones."** In equilibrium both are at room temperature. Metal feels colder because its high effusivity pulls the skin's contact temperature toward its own (Section 5.5).
- **"Blankets produce warmth."** Insulation only slows heat loss; a blanket wrapped around ice keeps it frozen longer.
- **"Heat rises."** *Hot fluid* rises because it is buoyant; conduction and radiation go in every direction.
- **"Only hot objects radiate."** Everything above 0 K radiates. Surfaces lose heat by radiation to a clear night sky, which is why frost can form on cars when the air is above freezing.
- **"White surfaces are poor emitters."** White paint has an infrared emissivity near 0.9. Visible color says little about infrared behavior; metallic shine is what lowers emissivity.
- **"Glasshouses work mainly by trapping infrared."** They stay warm mainly because the glass stops warm air from rising away; R. W. Wood showed this in 1909 using an infrared-transparent rock-salt cover. The *atmospheric* greenhouse effect is genuinely radiative, despite sharing the name.
- **"More insulation always means less heat loss."** Below the critical radius $r_c = k/h$, adding insulation to a wire increases heat loss.
- **"Wind chill can cool an object below air temperature."** Wind speeds cooling toward air temperature but cannot take a dry object below it; evaporation can.
- **"Space is cold, so objects there freeze instantly."** Vacuum is an excellent insulator; an object in shadow cools only slowly, by radiation, and a sunlit spacecraft can overheat.
- **"Conductivity tells how fast something heats up."** That is diffusivity, $\alpha = k/(\rho c)$. Water conducts five times better than pine yet has a similar diffusivity because it stores far more heat per unit volume.
- **"Newton's law of cooling is exact."** It is an approximation that defines $h$; in natural convection $h$ depends on $\Delta T$, and radiation is nonlinear in temperature.

## 12. Connections to Other Topics

- **Electric circuits:** Fourier's law inspired Ohm's law; thermal networks use series and parallel resistances, and lumped cooling is an RC circuit.
- **Diffusion and probability:** the heat equation also describes Fick diffusion and Brownian motion; its Gaussian solution is the central limit theorem in physical form, and the Black–Scholes equation of finance can be transformed into it.
- **Mathematics:** Fourier series and transforms, separation of variables and Green's functions grew from heat conduction.
- **Quantum mechanics:** Planck's 1900 explanation of blackbody radiation launched quantum theory; the Schrödinger equation is a diffusion equation in imaginary time.
- **Kinetic theory and statistical mechanics:** gas conductivity, phonons and the Wiedemann–Franz law follow from microscopic models.
- **Second law:** heat $\dot Q$ flowing from $T_H$ to $T_C$ generates entropy at the rate $\dot Q(1/T_C - 1/T_H) > 0$; every thermal resistance is a source of irreversibility.
- **Fluid mechanics:** convection is coupled to momentum transport through boundary layers and turbulence.
- **Earth and climate science:** planetary radiation balance, atmospheric and mantle convection, permafrost and geothermal energy. Earth's internal heat reaches the surface at only about 0.09 W/m² on average, thousands of times less than absorbed sunlight.
- **Astrophysics:** stellar energy moves outward by radiation in some zones and convection in others; stellar temperatures follow from Wien's and the Stefan–Boltzmann laws.
- **Biology:** thermoregulation, metabolic scaling with body size and the evolution of fur, feathers and blubber.

## 13. Practice Problems

1. **(Easy)** A copper bar ($k = 401$ W/(m·K)), 0.50 m long with a cross-section of 2.0 cm², connects a bath of boiling water (100 °C) to a mixture of ice and water (0 °C). Its sides are insulated. Find the heat flow and the mass of ice melted per hour ($L_f = 334$ kJ/kg).
2. **(Easy)** An attic floor of 50 m² is insulated with US R-19 batts. Convert to SI units and find the heat loss when the attic is 20 K colder than the rooms below (ignore other layers).
3. **(Easy–medium)** A cup of coffee cools from 90 °C to 70 °C in 5.0 min in a 20 °C room. Assuming Newton's law of cooling, when will it reach 50 °C?
4. **(Medium)** A 4 kg turkey takes 3.0 h to cook through. Using diffusion scaling, estimate the time for an 8 kg turkey of the same shape and oven temperature.
5. **(Medium)** The Sun's luminosity is $3.828\times10^{26}$ W and its radius $6.957\times10^8$ m. Find its effective surface temperature and the wavelength of peak emission.
6. **(Medium)** Calculate the radiation heat transfer coefficient for a surface at 30 °C ($\varepsilon = 0.9$) in surroundings at 20 °C, and compare the radiative flux with a natural-convection flux using $h = 4$ W/(m²·K) and air at 20 °C.
7. **(Medium)** A 1.0 mm radius electrical wire is coated with insulation of $k = 0.15$ W/(m·K); the outer convection coefficient is 10 W/(m²·K). Find the critical radius. Holding the wire surface 30 K above the air, compare the heat loss per metre for a bare wire and for insulation of outer radius 3.0 mm and 15 mm.
8. **(Medium–hard)** A steam pipe of outer radius 5.0 cm has its surface at 180 °C, in air at 20 °C. It is insulated with mineral wool ($k = 0.045$ W/(m·K)) to an outer radius of 10 cm; the outer combined convection-and-radiation coefficient is 10 W/(m²·K). Find the heat loss per metre and the outer surface temperature. Compare with the bare pipe (convection with the same $h$, plus radiation with $\varepsilon = 0.8$ to surroundings at 20 °C).
9. **(Hard)** Two large parallel plates of emissivity $\varepsilon$ are at $T_1$ and $T_2$. Show that inserting $N$ thin shields, each with emissivity $\varepsilon$ on both sides, reduces the radiative flux by a factor $N + 1$. Apply this to Worked Example 7.1 with 10 shields.
10. **(Medium–hard)** A resting person produces 100 W of heat. Air and surroundings are at 38 °C, skin is at 35 °C, $h_c = 10$ W/(m²·K), $\varepsilon = 0.97$, area 1.8 m². How much sweat must evaporate per hour ($h_{fg} = 2.42$ MJ/kg)?

### Solutions

**1.** $\dot Q = kA\Delta T/L = 401 \times 2.0\times10^{-4} \times 100/0.50 = 16.0$ W. In one hour: $16.0 \times 3600 = 5.77\times10^4$ J, which melts $5.77\times10^4/3.34\times10^5 = 0.173$ kg. **Answer:** 16 W; about 170 g of ice per hour.

**2.** $R'' = 19 \times 0.1761 = 3.35$ m²·K/W, so $U = 0.299$ W/(m²·K). $\dot Q = UA\Delta T = 0.299 \times 50 \times 20 = 299$ W, about 7.2 kWh per day. **Answer:** 3.35 m²·K/W; about 300 W.

**3.** $T - 20 = 70e^{-kt}$. From $50 = 70e^{-5k}$: $k = \ln(1.4)/5 = 0.0673$ min⁻¹. For $T = 50$ °C: $30 = 70e^{-kt}$, so $t = \ln(70/30)/0.0673 = 0.847/0.0673 = 12.6$ min. **Answer:** about 12.6 min after the start (7.6 min after it reaches 70 °C).

**4.** Cooking time scales as $t \propto L^2/\alpha$. For the same shape, $L \propto m^{1/3}$, so $t \propto m^{2/3}$: $t = 3.0 \times 2^{2/3} = 3.0 \times 1.587 = 4.8$ h. **Answer:** about 4.8 h, not 6 h — doubling the mass increases the time by only 59%.

**5.** $L = 4\pi R^2\sigma T^4$, so $T = [L/(4\pi R^2\sigma)]^{1/4}$. Surface flux: $L/(4\pi R^2) = 3.828\times10^{26}/(4\pi \times (6.957\times10^8)^2) = 6.29\times10^7$ W/m². Then $T = (6.29\times10^7/5.670\times10^{-8})^{1/4} = 5772$ K. Wien: $\lambda_{\max} = 2.898\times10^{-3}/5772 = 5.02\times10^{-7}$ m. **Answer:** 5772 K; 502 nm (blue-green, although the Sun looks white because it emits strongly across the whole visible range).

**6.** $T_s = 303.15$ K, $T_{\text{sur}} = 293.15$ K. $h_r = 0.9 \times 5.670\times10^{-8} \times (596.3) \times (303.15^2 + 293.15^2) = 5.41$ W/(m²·K); the approximation $4\varepsilon\sigma T_m^3$ with $T_m = 298.15$ K gives the same 5.41. Radiative flux $= 5.41 \times 10 = 54$ W/m²; convective flux $= 4 \times 10 = 40$ W/m². **Answer:** $h_r \approx 5.4$ W/(m²·K); radiation slightly exceeds natural convection.

**7.** $r_c = k/h = 0.15/10 = 0.015$ m = 15 mm. Bare wire: $q' = h(2\pi r_1)\Delta T = 10 \times 2\pi \times 0.001 \times 30 = 1.89$ W/m. With $r_2 = 3$ mm: $R' = \ln 3/(2\pi \times 0.15) + 1/(10 \times 2\pi \times 0.003) = 1.166 + 5.305 = 6.47$ m·K/W, so $q' = 30/6.47 = 4.64$ W/m. With $r_2 = 15$ mm: $R' = \ln 15/(2\pi \times 0.15) + 1/(10 \times 2\pi \times 0.015) = 2.873 + 1.061 = 3.93$ m·K/W, so $q' = 7.63$ W/m, the maximum possible. **Answer:** $r_c = 15$ mm; the coated wire loses 2.5 times (3 mm) and 4.0 times (15 mm) as much heat as the bare wire.

**8.** Insulation: $R'_{\text{ins}} = \ln(10/5)/(2\pi \times 0.045) = 2.452$ m·K/W. Outer surface: $R'_{\text{conv}} = 1/(10 \times 2\pi \times 0.10) = 0.159$ m·K/W. $q' = 160/2.611 = 61.3$ W/m. Outer surface: $T = 20 + 61.3 \times 0.159 = 29.8$ °C. Bare pipe: convection $10 \times 2\pi \times 0.05 \times 160 = 503$ W/m; radiation $0.8 \times 5.670\times10^{-8} \times 2\pi \times 0.05 \times (453.15^4 - 293.15^4) = 496$ W/m; total 998 W/m. **Answer:** 61 W/m with a 30 °C jacket surface, versus about 1000 W/m bare — a factor of 16. For 100 m of pipe running all year, insulation saves about 820 MWh.

**9.** With equal emissivities, each pair of facing surfaces has the same denominator $D = 2/\varepsilon - 1$. In steady state the same flux $q''$ crosses every gap. For the gaps between plate 1, shields $s_1 \ldots s_N$ and plate 2: $\sigma(T_1^4 - T_{s1}^4) = q''D$, $\sigma(T_{s1}^4 - T_{s2}^4) = q''D$, and so on — $N + 1$ equations in all. Adding them, the intermediate shield temperatures cancel: $\sigma(T_1^4 - T_2^4) = (N + 1)q''D$, so $q'' = \frac{\sigma(T_1^4 - T_2^4)}{(N + 1)(2/\varepsilon - 1)}$, which is the no-shield value divided by $N + 1$. In Worked Example 7.1 ($q''_0 = 11.7$ W/m²), 10 shields give $11.7/11 = 1.07$ W/m². **Answer:** factor $N + 1$; about 1.1 W/m². This is the principle of multilayer insulation.

**10.** $C = 10 \times 1.8 \times (35 - 38) = -54$ W (a gain). $R = 0.97 \times 5.670\times10^{-8} \times 1.8 \times (308.15^4 - 311.15^4) = -35.3$ W (a gain). Balance: $E = 100 + 54 + 35.3 = 189$ W. Sweat: $189/2.42\times10^6 = 7.8\times10^{-5}$ kg/s = 0.28 kg/h. **Answer:** about 0.28 kg (roughly 0.3 L) per hour, even at rest — all of it must evaporate, which becomes impossible in very humid air.

## 14. Summary

- Heat flows down temperature differences by **conduction**, **convection** and **radiation**.
- **Fourier's law** $q'' = -k\,dT/dx$ governs conduction; $k$ spans five orders of magnitude, from diamond to aerogel. Free electrons make metals good conductors; trapped, still gas makes insulators.
- Steady heat flow obeys an **Ohm's-law analogy**: resistances combine in series and parallel, and building elements are rated by **R-values** and **U-factors**.
- The **heat equation** governs transient conduction: diffusion times scale as $L^2/\alpha$, periodic heating penetrates a depth $\sqrt{2\alpha/\omega}$, and effusivity sets contact temperature.
- **Convection** is summarized by $h$, from a few W/(m²·K) in still air to $10^5$ in boiling. **Reynolds**, **Prandtl** and **Nusselt** numbers organize the results; the **Biot** number decides whether a solid cools uniformly.
- **Radiation** follows Planck's law, the **Stefan–Boltzmann** and **Wien** laws and **Kirchhoff's law**; at room temperature it rivals natural convection.
- Radiative balance gives Earth an effective temperature of 255 K; the greenhouse effect raises the surface mean to about 288 K.
- Insulation stills gas, fins add area, and the human body balances metabolism against convection, radiation and evaporation of sweat.

### Key equations

| Quantity | Equation |
|---|---|
| Fourier's law | $\dot Q = -kA\,dT/dx$ |
| Conduction resistances | $R = L/(kA)$ (wall); $R = \ln(r_2/r_1)/(2\pi kL)$ (cylinder) |
| Overall coefficient | $\dot Q = UA\Delta T$, $U = 1/\sum R''$ |
| Critical radius (cylinder) | $r_c = k/h$ |
| Heat equation | $\partial T/\partial t = \alpha\nabla^2T + \dot q/(\rho c)$, $\alpha = k/(\rho c)$ |
| Diffusion time; damping depth | $t \sim L^2/\alpha$; $\delta = \sqrt{2\alpha/\omega}$ |
| Contact temperature | $T_c = (e_1T_1 + e_2T_2)/(e_1 + e_2)$, $e = \sqrt{k\rho c}$ |
| Newton's law of cooling | $\dot Q = hA(T_s - T_\infty)$ |
| Lumped cooling | $T - T_\infty = (T_0 - T_\infty)e^{-t/\tau}$, $\tau = \rho cV/(hA)$, valid for $\text{Bi} = hL_c/k < 0.1$ |
| Dimensionless groups | $\text{Re} = VL/\nu$, $\text{Pr} = \nu/\alpha$, $\text{Nu} = hL/k_{\text{fluid}}$ |
| Stefan–Boltzmann law | $E = \varepsilon\sigma T^4$, $\sigma = 2\pi^5k_B^4/(15h^3c^2)$ |
| Wien's law | $\lambda_{\max}T = 2.898\times10^{-3}$ m·K |
| Radiative exchange | $\dot Q = \varepsilon\sigma A(T_s^4 - T_{\text{sur}}^4)$ (small body); $q'' = \sigma(T_1^4 - T_2^4)/(1/\varepsilon_1 + 1/\varepsilon_2 - 1)$ (plates) |
| Radiation coefficient | $h_r \approx 4\varepsilon\sigma T_m^3$ |
| Planetary temperature | $T_e = [S(1 - a)/(4\sigma)]^{1/4}$; one-layer model $T_s = T_e[2/(2 - \varepsilon)]^{1/4}$ |
| Fin heat rate | $\dot Q_f = \sqrt{hPkA_c}\,\theta_b\tanh mL$, $m = \sqrt{hP/(kA_c)}$ |
| Human heat balance | $M - W = C + R + E + K + S$ |
