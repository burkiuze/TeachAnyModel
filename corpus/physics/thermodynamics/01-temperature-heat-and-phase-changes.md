---
title: Temperature, Heat, Thermal Expansion and Phase Changes
field: Physics
subfield: Thermodynamics
level: high-school to undergraduate
keywords: [temperature, zeroth law, thermometer, Celsius, Kelvin, Fahrenheit, thermal expansion, heat, specific heat capacity, calorimetry, latent heat, phase diagram, triple point, critical point, conduction, convection, radiation, Stefan-Boltzmann law, Newton's law of cooling]
---

# Temperature, Heat, Thermal Expansion and Phase Changes

Thermodynamics is the science of energy, heat, work and their relation to the properties of matter. It was developed in the 19th century largely to understand steam engines, but its laws turned out to be among the most universal in all of science — applying equally to stars, chemical reactions, living cells, black holes and computers.

## 1. Temperature and the Zeroth Law

### Thermal equilibrium
When two objects are placed in thermal contact, energy flows from the hotter to the colder until they reach the same temperature. They are then in **thermal equilibrium**: no net energy flows between them.

### The zeroth law of thermodynamics
> If two systems are each in thermal equilibrium with a third system, they are in thermal equilibrium with each other.

This seemingly obvious statement is what makes **thermometers** possible: the thermometer is the "third system". It establishes temperature as a well-defined property — two systems have the same temperature if and only if they are in thermal equilibrium. (It was named "zeroth" because it was formulated after the first and second laws but is logically prior to them.)

### Microscopic meaning
Temperature measures the average kinetic energy of the random motion of particles. For an ideal monatomic gas, $\langle\frac12mv^2\rangle = \frac32k_BT$, where $k_B = 1.380649 \times 10^{-23}$ J/K is Boltzmann's constant. More fundamentally, statistical mechanics defines temperature through entropy: $\frac{1}{T} = \left(\frac{\partial S}{\partial E}\right)_{V,N}$.

### Temperature scales

| Scale | Water freezes | Water boils (1 atm) | Absolute zero |
|---|---|---|---|
| Celsius (°C) | 0 | 100 | −273.15 |
| Kelvin (K) | 273.15 | 373.15 | 0 |
| Fahrenheit (°F) | 32 | 212 | −459.67 |

Conversions:
$$T_K = T_C + 273.15, \qquad T_F = \tfrac95 T_C + 32$$

The **Kelvin** scale is the absolute thermodynamic scale; zero kelvin (absolute zero) is the lowest possible temperature, at which a system is in its ground state. Since 2019 the kelvin is defined by fixing the numerical value of $k_B$ exactly. A temperature *difference* of 1 K equals a difference of 1 °C. Note: it is "kelvin", not "degrees kelvin".

−40 °C = −40 °F is the one temperature where the two scales agree.

### Thermometers
Any property that changes reproducibly with temperature can make a thermometer: liquid expansion (mercury, alcohol), gas pressure at constant volume (the constant-volume gas thermometer, a primary standard), electrical resistance (platinum resistance thermometers, thermistors), thermoelectric voltage (thermocouples), and emitted infrared radiation (pyrometers, ear thermometers).

## 2. Thermal Expansion

Most materials expand when heated, because increased atomic vibration amplitudes, combined with the asymmetric (anharmonic) shape of interatomic potentials, increase average separations.

**Linear expansion:**
$$\Delta L = \alpha L_0\Delta T$$
**Volume expansion:**
$$\Delta V = \beta V_0\Delta T, \qquad \beta \approx 3\alpha \text{ (isotropic solids)}$$

| Material | $\alpha$ (10⁻⁶ /K) |
|---|---|
| Invar (Fe–Ni alloy) | ~1.2 |
| Pyrex glass | 3.2 |
| Concrete | ~12 |
| Steel | ~12 |
| Copper | 17 |
| Aluminum | 23 |
| Ordinary (soda-lime) glass | ~9 |

**Applications and consequences:**
- Expansion joints in bridges, railways and sidewalks.
- **Bimetallic strips** (two metals with different $\alpha$ bonded together) bend when heated; used in thermostats and circuit breakers.
- Pyrex resists thermal shock because of its low $\alpha$.
- Steel reinforcement in concrete works partly because both have similar $\alpha$.
- A hole in a plate *expands* when heated, as if it were made of the same material — useful for shrink-fitting.
- Sea-level rise: thermal expansion of warming ocean water is a major contributor alongside melting land ice.

**Anomalous expansion of water:** water contracts when heated from 0 °C to 4 °C, then expands. The resulting density maximum at ~4 °C and the lower density of ice are due to hydrogen bonding, which in ice creates an open hexagonal lattice.

### Worked example 2.1
A 1 km steel bridge experiences temperatures from −20 °C to +40 °C. Change in length: $\Delta L = 12 \times 10^{-6} \times 1000 \times 60 = 0.72$ m. Expansion joints must accommodate about 72 cm.

## 3. Heat

**Heat** ($Q$) is energy transferred between systems because of a temperature difference. Heat is not something a body "contains" — a body contains internal energy; heat is energy *in transit*. (The 18th-century caloric theory, which treated heat as a conserved fluid, was overturned by experiments such as Count Rumford's cannon-boring observations and James Joule's paddle-wheel experiments in the 1840s, which showed that mechanical work can produce heat in a fixed ratio.)

Units: joule (J). The calorie (cal) is the heat needed to raise 1 g of water by 1 °C: 1 cal = 4.184 J. The food Calorie is 1 kcal.

### Specific heat capacity
The heat required to change the temperature of a mass $m$ by $\Delta T$ (without phase change):
$$\boxed{Q = mc\Delta T}$$
$c$ is the **specific heat capacity** (J/(kg·K)). The **molar heat capacity** $C$ is per mole: $Q = nC\Delta T$.

| Substance | $c$ (J/(kg·K)) |
|---|---|
| Water (liquid) | 4186 |
| Ice | ~2100 |
| Steam | ~2010 |
| Air (constant pressure) | ~1005 |
| Aluminum | 900 |
| Glass | ~840 |
| Iron/steel | ~450 |
| Copper | 385 |
| Lead | 128 |

Water's unusually high specific heat (due to hydrogen bonding) moderates coastal climates, makes oceans a vast heat reservoir, makes water an excellent coolant, and helps organisms regulate their temperature.

**Dulong–Petit law:** at room temperature, many solid elements have molar heat capacity ≈ $3R \approx 25$ J/(mol·K), because each atom has 3 vibrational degrees of freedom, each contributing $k_B$ (kinetic + potential) by equipartition. At low temperatures heat capacities fall toward zero — a quantum effect explained by Einstein (1907) and Debye (1912).

### Calorimetry
In an isolated system, heat lost by hot objects equals heat gained by cold objects:
$$\sum Q_i = 0$$

**Worked example 3.1:** A $0.2$ kg piece of aluminum at 100 °C is dropped into $0.5$ kg of water at 20 °C in an insulated container. Find the final temperature.
$0.2 \times 900 \times (T - 100) + 0.5 \times 4186 \times (T - 20) = 0$
$180T - 18\,000 + 2093T - 41\,860 = 0 \Rightarrow 2273T = 59\,860 \Rightarrow T \approx 26.3$ °C.
Despite starting 80 °C hotter, the aluminum raises the water only 6.3 °C — water's large heat capacity dominates.

## 4. Phase Changes and Latent Heat

During a phase change (melting, boiling, sublimation) at constant pressure, heat is absorbed or released **without a change in temperature**. The energy goes into breaking (or forming) intermolecular bonds, i.e. into potential energy.

$$\boxed{Q = mL}$$
$L$ is the **latent heat** (J/kg).

| Substance | Melting point | $L_f$ (kJ/kg) | Boiling point (1 atm) | $L_v$ (kJ/kg) |
|---|---|---|---|---|
| Water | 0 °C | 334 | 100 °C | 2257 |
| Ethanol | −114 °C | 108 | 78 °C | 855 |
| Lead | 327 °C | 23 | 1749 °C | 871 |
| Nitrogen | −210 °C | 25.7 | −196 °C | 199 |
| Iron | 1538 °C | 247 | 2862 °C | 6090 |

**Why steam burns are severe:** condensing 1 g of steam at 100 °C releases 2257 J — more than five times the 419 J released by cooling 1 g of water from 100 °C to 0 °C.

**Evaporative cooling:** sweating cools the body because evaporating water absorbs latent heat from the skin. This is also how evaporative coolers and clay water pots work. Evaporation can occur at any temperature; boiling occurs when the vapor pressure equals the surrounding pressure.

### Heating curve of water (worked example 4.1)
**Problem:** How much heat converts 1 kg of ice at −10 °C into steam at 110 °C?
1. Warm ice −10 → 0 °C: $1 \times 2100 \times 10 = 21$ kJ
2. Melt at 0 °C: $1 \times 334 = 334$ kJ
3. Warm water 0 → 100 °C: $1 \times 4186 \times 100 = 418.6$ kJ
4. Boil at 100 °C: $1 \times 2257 = 2257$ kJ
5. Warm steam 100 → 110 °C: $1 \times 2010 \times 10 = 20.1$ kJ
Total ≈ **3051 kJ**. Vaporization alone is about 74% of the total.

### Phase diagrams
A **phase diagram** shows which phase is stable at each pressure and temperature. Key features:
- **Coexistence curves** (melting, vaporization, sublimation lines), along which two phases coexist. Their slopes obey the **Clausius–Clapeyron equation**: $\frac{dP}{dT} = \frac{L}{T\Delta v}$.
- **Triple point:** the unique $(P, T)$ where solid, liquid and gas coexist. For water: 273.16 K (0.01 °C) and 611.657 Pa.
- **Critical point:** the end of the liquid–vapor line, above which liquid and gas become indistinguishable (a **supercritical fluid**). For water: 647.1 K (374 °C), 22.06 MPa. For CO₂: 304.1 K (31 °C), 7.38 MPa — supercritical CO₂ is used to decaffeinate coffee.

**Water's anomaly:** water's melting curve has a negative slope (ice is less dense than liquid), so increasing pressure *lowers* the melting point slightly. (The popular claim that ice skating works only because blade pressure melts the ice is largely incorrect; the pressure effect is too small. A thin, intrinsically disordered "premelted" surface layer and frictional heating are the main reasons ice is slippery.)

**Boiling point and pressure:** at the top of Everest (~34 kPa), water boils at about 71 °C, making cooking slow. Pressure cookers (~200 kPa absolute) raise the boiling point to about 120 °C, cooking food much faster.

**Sublimation:** dry ice (solid CO₂) sublimes at −78.5 °C at 1 atm because CO₂'s triple-point pressure (5.11 atm) is above atmospheric pressure — liquid CO₂ cannot exist at 1 atm. Freeze-drying uses sublimation of ice under vacuum.

## 5. Heat Transfer Mechanisms

### Conduction
Energy transfer through a material by microscopic collisions (and in metals, mainly by free electrons), without bulk motion. **Fourier's law**:
$$\boxed{\frac{dQ}{dt} = -kA\frac{dT}{dx}} \qquad \text{(for a slab: } P = kA\frac{T_H - T_C}{L}\text{)}$$
$k$ is the **thermal conductivity** (W/(m·K)).

| Material | $k$ (W/(m·K)) |
|---|---|
| Diamond | ~2000 |
| Copper | 400 |
| Aluminum | 237 |
| Steel | ~50 |
| Glass | ~0.8 |
| Water | 0.6 |
| Wood | ~0.1 |
| Fiberglass insulation | ~0.04 |
| Air (still) | 0.026 |
| Silica aerogel | ~0.015 |

Good electrical conductors are generally good thermal conductors (Wiedemann–Franz law) because free electrons carry both charge and heat. Diamond is an exception: an electrical insulator with extraordinary thermal conductivity, carried by lattice vibrations (phonons).

**Why metal feels colder than wood** at the same room temperature: metal conducts heat away from your skin much faster.

**Thermal resistance:** for layers in series, $R = L/(kA)$ add like electrical resistors. Building insulation is rated by R-value.

### Convection
Energy transfer by bulk motion of a fluid. **Natural convection** is driven by buoyancy (warm fluid is less dense and rises): sea breezes, boiling water, atmospheric weather, ocean currents, and convection in Earth's mantle (driving plate tectonics) and in the outer layers of the Sun. **Forced convection** uses fans or pumps (radiators, wind chill, computer cooling).

Newton's law of cooling (approximate, for modest temperature differences): the rate of heat loss is proportional to the temperature difference with the surroundings:
$$\frac{dT}{dt} = -k(T - T_{\text{env}}) \Rightarrow T(t) = T_{\text{env}} + (T_0 - T_{\text{env}})e^{-kt}$$
Forensic scientists use this to estimate time of death; it also describes a cooling cup of coffee.

### Radiation
All objects emit electromagnetic radiation because of their temperature. No medium is required — this is how the Sun heats Earth across the vacuum of space. The **Stefan–Boltzmann law** gives the power radiated:
$$\boxed{P = e\sigma AT^4}, \qquad \sigma = 5.670 \times 10^{-8} \text{ W/(m}^2\text{K}^4)$$
$e$ is the emissivity (0 to 1; 1 for an ideal black body). Net power exchanged with surroundings at $T_s$: $P_{\text{net}} = e\sigma A(T^4 - T_s^4)$.

**Wien's displacement law:** the wavelength of peak emission is inversely proportional to temperature:
$$\lambda_{\max}T = 2.898 \times 10^{-3} \text{ m·K}$$
- Sun ($T \approx 5772$ K): $\lambda_{\max} \approx 502$ nm (visible, blue-green)
- Human body ($T \approx 310$ K): $\lambda_{\max} \approx 9.3$ μm (infrared — hence thermal cameras)
- Cosmic microwave background ($T = 2.725$ K): $\lambda_{\max} \approx 1.06$ mm (microwave)

Good absorbers are good emitters (Kirchhoff's law of thermal radiation). Dark surfaces absorb and emit well; shiny surfaces do neither. Thermos flasks use a vacuum (no conduction or convection) and silvered walls (minimal radiation).

**The greenhouse effect:** Earth's surface absorbs visible sunlight and re-emits infrared. Greenhouse gases (H₂O, CO₂, CH₄) absorb and re-emit infrared, reducing the energy escaping to space. Without any greenhouse effect, Earth's average surface temperature would be about −18 °C instead of about +15 °C. Increasing CO₂ concentrations (from ~280 ppm pre-industrial to over 420 ppm today) strengthen this effect and drive global warming.

### Worked example 5.1 – Radiation from the human body
**Problem:** A person with skin surface area 1.8 m², skin temperature 34 °C (307 K) and emissivity 0.97 stands in a room at 22 °C (295 K). Estimate the net radiated power.
$P = 0.97 \times 5.67\times10^{-8} \times 1.8 \times (307^4 - 295^4)$
$307^4 \approx 8.883 \times 10^9$, $295^4 \approx 7.573 \times 10^9$, difference $\approx 1.310\times10^9$.
$P \approx 0.97 \times 5.67\times10^{-8} \times 1.8 \times 1.310\times10^9 \approx 130$ W.
This is comparable to the resting metabolic rate (~80–100 W); clothing reduces the effective radiating surface temperature and hence the loss.

## 6. Summary

| Concept | Formula |
|---|---|
| Kelvin–Celsius | $T_K = T_C + 273.15$ |
| Linear expansion | $\Delta L = \alpha L_0\Delta T$ |
| Volume expansion | $\Delta V = \beta V_0\Delta T$, $\beta\approx3\alpha$ |
| Sensible heat | $Q = mc\Delta T$ |
| Latent heat | $Q = mL$ |
| Conduction (Fourier) | $P = kA\Delta T/L$ |
| Newton's law of cooling | $T(t) = T_{\text{env}} + (T_0 - T_{\text{env}})e^{-kt}$ |
| Stefan–Boltzmann | $P = e\sigma AT^4$ |
| Wien | $\lambda_{\max}T = 2.898\times10^{-3}$ m·K |
| Clausius–Clapeyron | $dP/dT = L/(T\Delta v)$ |
