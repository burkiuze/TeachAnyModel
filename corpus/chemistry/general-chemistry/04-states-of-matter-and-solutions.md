---
title: States of Matter, Gas Laws and Solutions
field: Chemistry
subfield: General Chemistry
level: high-school to undergraduate
keywords: [gas laws, Boyle's law, Charles's law, Avogadro's law, ideal gas law, Dalton's law of partial pressures, molar volume, gas density, effusion, Graham's law, real gases, liquids, vapor pressure, boiling point, solids, crystalline, amorphous, solutions, solubility, Henry's law, colligative properties, Raoult's law, boiling point elevation, freezing point depression, osmotic pressure, colloids]
---

# States of Matter, Gas Laws and Solutions

Matter commonly exists as solid, liquid or gas (plus plasma, and exotic states like Bose–Einstein condensates). The state depends on the balance between the kinetic energy of particles (which tends to disperse them) and intermolecular attractions (which hold them together). This document covers the quantitative behavior of gases, the properties of liquids and solids, and the physical chemistry of solutions.

## 1. Comparing the States

| Property | Solid | Liquid | Gas |
|---|---|---|---|
| Shape | Fixed | Takes container shape | Fills container |
| Volume | Fixed | Fixed | Fills container |
| Compressibility | Very low | Very low | High |
| Particle arrangement | Ordered (crystalline) or disordered (amorphous); close | Disordered, close | Disordered, far apart |
| Particle motion | Vibration about fixed positions | Translation, rotation; slide past each other | Rapid random motion |
| Intermolecular forces vs. KE | Forces dominate | Comparable | KE dominates |
| Density | High | High | Low (~1/1000 of liquid) |

**Plasma** — ionized gas of free electrons and ions — is the most common state of visible matter in the universe (stars, lightning, neon signs, auroras).

## 2. Gas Laws

### Pressure
Gas pressure results from molecular collisions with container walls. Units: 1 atm = 101.325 kPa = 760 mmHg = 760 torr = 1.01325 bar. Measured with barometers (atmospheric) and manometers (enclosed gases).

### Empirical gas laws

| Law | Relationship | Held constant | Equation | Discovered |
|---|---|---|---|---|
| Boyle's law | $V \propto 1/P$ | $n$, $T$ | $P_1V_1 = P_2V_2$ | Robert Boyle, 1662 |
| Charles's law | $V \propto T$ | $n$, $P$ | $V_1/T_1 = V_2/T_2$ | Jacques Charles, ~1787 |
| Gay-Lussac's law | $P \propto T$ | $n$, $V$ | $P_1/T_1 = P_2/T_2$ | Joseph Gay-Lussac, 1802 |
| Avogadro's law | $V \propto n$ | $P$, $T$ | $V_1/n_1 = V_2/n_2$ | Amedeo Avogadro, 1811 |
| Combined gas law | — | $n$ | $\frac{P_1V_1}{T_1} = \frac{P_2V_2}{T_2}$ | — |

**Temperature must be in kelvin.** Extrapolating Charles's law, gas volume would reach zero at −273.15 °C — historically, one route to the concept of absolute zero.

**Avogadro's hypothesis:** equal volumes of gases at the same temperature and pressure contain equal numbers of molecules — regardless of identity.

### The ideal gas law
$$\boxed{PV = nRT}$$
$$R = 8.314\text{ J/(mol·K)} = 0.08206\text{ L·atm/(mol·K)} = 62.36\text{ L·torr/(mol·K)}$$

**Molar volume:** at STP (0 °C, 1 atm), 1 mol of ideal gas occupies 22.41 L; at standard ambient conditions (25 °C, 1 bar) it occupies 24.79 L. (IUPAC redefined STP in 1982 as 0 °C and 1 bar, giving 22.71 L; many textbooks still use 1 atm.)

**Worked example 2.1:** what volume does 10.0 g of CO₂ occupy at 25 °C and 1.00 atm?
$n = 10.0/44.01 = 0.2272$ mol; $V = nRT/P = 0.2272\times0.08206\times298.15/1.00 = 5.56$ L.

### Gas density and molar mass
Rearranging $PV = nRT$ with $n = m/M$:
$$\rho = \frac{PM}{RT}, \qquad M = \frac{\rho RT}{P}$$
Gases with $M$ less than air's average (~29 g/mol) — He (4), H₂ (2), CH₄ (16), NH₃ (17) — rise; heavier gases — CO₂ (44), propane (44), chlorine (71) — sink and can accumulate in low places (a hazard in cellars and pits). Hot-air balloons rise because warmer air is less dense.

### Dalton's law of partial pressures
In a mixture of non-reacting gases, the total pressure is the sum of partial pressures, each being the pressure the gas would exert alone:
$$P_{\text{total}} = P_A + P_B + \cdots, \qquad P_A = \chi_AP_{\text{total}}$$
Dry air at sea level: N₂ 78.08% (0.781 atm), O₂ 20.95% (0.209 atm), Ar 0.93%, CO₂ ~0.042%.

**Applications:**
- **Collecting gas over water:** subtract water's vapor pressure (e.g. 23.8 torr at 25 °C) from the measured pressure.
- **Altitude:** at Everest's summit ($P \approx 0.33$ atm), the O₂ partial pressure is only ~0.07 atm, causing hypoxia.
- **Scuba diving:** at 30 m depth (4 atm total), the O₂ partial pressure in air is ~0.84 atm; above ~1.4–1.6 atm, oxygen becomes toxic, limiting depths for enriched air; N₂ at high partial pressure causes nitrogen narcosis.

### Graham's law of effusion
Effusion (escape through a tiny hole) and diffusion rates are inversely proportional to the square root of molar mass:
$$\frac{r_1}{r_2} = \sqrt{\frac{M_2}{M_1}}$$
Helium balloons deflate faster than air-filled balloons. HCl and NH₃ released at opposite ends of a tube meet closer to the HCl end (NH₃ is lighter), forming a white NH₄Cl ring.

### Kinetic-molecular theory
Explains the gas laws: gas particles are in constant random motion, occupy negligible volume, have elastic collisions and no intermolecular forces; average kinetic energy is proportional to absolute temperature ($\frac32k_BT$ per molecule); $v_{\text{rms}} = \sqrt{3RT/M}$. (Details in the physics document on kinetic theory.)

### Real gases
Real gases deviate from ideality at **high pressures** (molecular volume matters) and **low temperatures** (attractions matter). The **van der Waals equation** corrects for both:
$$\left(P + \frac{an^2}{V^2}\right)(V - nb) = nRT$$
Gases behave most ideally at high temperature and low pressure. Gases with strong intermolecular forces (H₂O, NH₃) deviate most; He and H₂ least. Gases can be liquefied only below their **critical temperature** (CO₂: 31 °C; N₂: −147 °C; He: −268 °C).

## 3. Liquids

### Properties
- **Viscosity:** resistance to flow; increases with intermolecular forces and molecular size/entanglement (honey, glycerol, motor oil), decreases with temperature.
- **Surface tension:** energy needed to increase surface area; high for water (72.8 mN/m at 20 °C) and mercury (485 mN/m) due to strong cohesive forces.
- **Capillary action:** liquid rising in narrow tubes when adhesion to the tube exceeds cohesion (water in glass forms a concave meniscus; mercury, with stronger cohesion, forms a convex one).

### Vapor pressure and boiling
Molecules at the surface with enough kinetic energy escape into the vapor. In a closed container, evaporation and condensation reach dynamic equilibrium; the pressure of the vapor is the **vapor pressure**. It increases steeply with temperature and is higher for liquids with weaker intermolecular forces (**volatile** liquids).

| Liquid | Vapor pressure at 20 °C (kPa) | Normal boiling point (°C) |
|---|---|---|
| Diethyl ether | 58.7 | 34.6 |
| Acetone | 24.6 | 56 |
| Ethanol | 5.9 | 78.4 |
| Water | 2.34 | 100 |
| Ethylene glycol | 0.007 | 197 |
| Mercury | 0.00017 | 357 |

A liquid **boils** when its vapor pressure equals the external pressure. The **normal boiling point** is the temperature where vapor pressure = 1 atm.

**Clausius–Clapeyron equation:**
$$\ln\frac{P_2}{P_1} = -\frac{\Delta H_{\text{vap}}}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$$
**Worked example 3.1:** water's $\Delta H_{\text{vap}} = 40.7$ kJ/mol. At what temperature does water boil where pressure is 0.70 atm?
$\ln(0.70) = -\frac{40\,700}{8.314}\left(\frac{1}{T_2} - \frac{1}{373.15}\right)$ → $\frac{1}{T_2} = \frac{1}{373.15} + \frac{0.3567\times8.314}{40\,700} = 0.0026799 + 0.0000729 = 0.0027528$ → $T_2 \approx 363.3$ K ≈ 90 °C.

## 4. Solids

### Crystalline vs. amorphous
- **Crystalline solids** have long-range periodic order and sharp melting points (salt, quartz, ice, metals).
- **Amorphous solids** lack long-range order and soften over a temperature range (glass, many plastics, rubber). Glass has a **glass transition** rather than a true melting point.

### Types of crystalline solids

| Type | Particles | Forces | Properties | Examples |
|---|---|---|---|---|
| Ionic | Cations and anions | Ionic bonds | Hard, brittle, high mp, conduct when molten | NaCl, CaF₂, MgO |
| Molecular | Molecules | Intermolecular forces | Soft, low mp, nonconducting | Ice, sugar, I₂, CO₂ (dry ice) |
| Covalent network | Atoms | Covalent bonds | Very hard, very high mp, usually nonconducting | Diamond, quartz (SiO₂), SiC, graphite (conducts in-plane) |
| Metallic | Metal cations in electron sea | Metallic bonds | Malleable, ductile, conductive, variable mp | Cu, Fe, Na, W |

**Allotropes:** different structural forms of the same element. Carbon: diamond (sp³ network; hardest natural material, insulator), graphite (sp² layers; soft, conductive, lubricant), graphene (single layer), fullerenes (C₆₀, "buckyballs", Nobel 1996), carbon nanotubes. Oxygen: O₂ and O₃. Phosphorus: white (P₄, pyrophoric), red, black. Tin: white (metallic) and gray (brittle, below 13 °C — "tin pest").

### Phase diagrams
Show the stable phase at each temperature and pressure, with coexistence lines meeting at the **triple point**; the liquid–gas line ends at the **critical point**. Water's solid–liquid line slopes slightly backward (ice is less dense than liquid). CO₂'s triple point is at 5.11 atm, so at 1 atm solid CO₂ sublimes (−78.5 °C) instead of melting.

## 5. Solutions

A **solution** is a homogeneous mixture: a **solute** dissolved in a **solvent**. Solutions can be gaseous (air), liquid (salt water, vodka, carbonated drinks) or solid (alloys such as brass and sterling silver).

### The dissolution process
Dissolving involves three steps:
1. Separating solute particles (endothermic).
2. Separating solvent particles to make room (endothermic).
3. Solute–solvent attraction, **solvation** (hydration in water) (exothermic).

$\Delta H_{\text{soln}}$ can be negative (NaOH, H₂SO₄ — solutions heat up) or positive (NH₄NO₃ — used in instant cold packs). Dissolution also usually increases entropy, which can drive endothermic dissolution.

**"Like dissolves like":** polar and ionic solutes dissolve in polar solvents (water); nonpolar solutes dissolve in nonpolar solvents (hexane, oil). Soaps and detergents are **amphiphilic** (polar head, nonpolar tail) and form **micelles** that trap grease.

### Solubility
The maximum amount of solute that dissolves in a given amount of solvent at a given temperature (a **saturated** solution). **Unsaturated** solutions hold less; **supersaturated** solutions hold more temporarily (unstable — e.g. sodium acetate "hot ice" crystallizes instantly when seeded).

**Temperature effects:**
- Most solids become **more** soluble at higher temperature (sugar, KNO₃); some barely change (NaCl) or decrease (Ce₂(SO₄)₃).
- Gases become **less** soluble at higher temperature — warm soda goes flat faster; thermal pollution lowers dissolved oxygen in rivers, harming fish.

**Pressure effects (gases) — Henry's law:**
$$\boxed{C = k_HP_{\text{gas}}}$$
The solubility of a gas is proportional to its partial pressure above the solution. Carbonated beverages are bottled under high CO₂ pressure; opening the bottle lowers pressure and CO₂ comes out of solution. **Decompression sickness** ("the bends") occurs when divers ascend too quickly and dissolved N₂ forms bubbles in tissues.

## 6. Colligative Properties

Properties of solutions that depend on the **number** of dissolved solute particles, not their identity. The **van 't Hoff factor** $i$ is the number of particles per formula unit: $i = 1$ for nonelectrolytes (glucose), $i \approx 2$ for NaCl, $i \approx 3$ for CaCl₂ (actual values are slightly lower due to ion pairing).

### Vapor-pressure lowering (Raoult's law)
$$\boxed{P_{\text{solution}} = \chi_{\text{solvent}}P^\circ_{\text{solvent}}}$$
A nonvolatile solute lowers the vapor pressure because fewer solvent molecules are at the surface (and entropy favors the solution). For a mixture of two volatile liquids (ideal solution): $P_{\text{total}} = \chi_AP_A^\circ + \chi_BP_B^\circ$ — the basis of **fractional distillation**. Non-ideal mixtures show deviations; some form **azeotropes** (e.g. 95.6% ethanol–water boils at 78.2 °C, below either component, so ordinary distillation cannot exceed this purity).

### Boiling-point elevation
$$\boxed{\Delta T_b = iK_bm}$$
Water: $K_b = 0.512$ °C·kg/mol.

### Freezing-point depression
$$\boxed{\Delta T_f = iK_fm}$$
Water: $K_f = 1.86$ °C·kg/mol. Benzene: 5.12; camphor: 37.7 (useful for determining molar masses).

**Applications:** road salt melts ice (NaCl effective to about −10 °C; CaCl₂ to about −30 °C, being $i = 3$ and more soluble); antifreeze (ethylene glycol) in car radiators both lowers the freezing point and raises the boiling point; ice cream making uses salt–ice mixtures; fish in polar seas produce antifreeze proteins.

**Worked example 6.1:** how many grams of ethylene glycol (C₂H₆O₂, $M = 62.07$ g/mol) must be added to 5.00 kg of water to lower its freezing point to −10.0 °C?
$m = \Delta T_f/K_f = 10.0/1.86 = 5.38$ mol/kg. Moles $= 5.38\times5.00 = 26.9$ mol. Mass $= 26.9\times62.07 \approx 1670$ g. The solution boils at $100 + 0.512\times5.38 = 102.8$ °C.

### Osmotic pressure
**Osmosis** is the net flow of solvent through a **semipermeable membrane** from a dilute to a concentrated solution. The pressure needed to stop it is the **osmotic pressure**:
$$\boxed{\Pi = iMRT}$$
(van 't Hoff, Nobel Chemistry 1901 — the first chemistry Nobel.)

Osmotic pressures are large: 0.1 M glucose at 25 °C has $\Pi = 0.1\times0.08206\times298 = 2.45$ atm. This makes osmometry ideal for measuring molar masses of polymers and proteins.

**Biological significance:**
- Cells in **isotonic** solutions (0.9% NaCl, ~0.15 M, "normal saline"; ~290 mOsm/L) keep their shape.
- In **hypotonic** solutions (pure water), water enters and red blood cells swell and burst (**hemolysis**).
- In **hypertonic** solutions (concentrated salt), water leaves and cells shrivel (**crenation**). This is why salting and sugaring preserve food (microbes dehydrate) and why drinking seawater dehydrates you.
- Plants use turgor pressure from osmosis to stay rigid; wilting is loss of turgor.
- **Reverse osmosis:** applying pressure greater than $\Pi$ forces water from a concentrated to a dilute side — the main technology for desalinating seawater (seawater's osmotic pressure is ~27 atm; plants operate at ~55–80 atm).
- **Dialysis** removes waste from blood through semipermeable membranes.

## 7. Colloids

Mixtures with particles 1–1000 nm across — larger than in solutions, smaller than in suspensions. They do not settle and scatter light (**Tyndall effect** — visible beams of light through fog or a dusty room; also why the sky is blue, via Rayleigh scattering by molecules).

| Colloid type | Dispersed phase | Medium | Examples |
|---|---|---|---|
| Aerosol | Liquid or solid | Gas | Fog, smoke, sprays |
| Foam | Gas | Liquid | Whipped cream, shaving foam |
| Solid foam | Gas | Solid | Styrofoam, pumice, aerogel |
| Emulsion | Liquid | Liquid | Milk, mayonnaise (stabilized by emulsifiers like lecithin in egg yolk) |
| Sol | Solid | Liquid | Paint, ink, blood |
| Gel | Liquid | Solid | Gelatin, jelly, hair gel |

Colloids are stabilized by charge on particle surfaces or by adsorbed molecules; adding electrolytes can neutralize charges and cause **coagulation** (e.g. river deltas form where colloidal clay meets salty seawater; alum clarifies drinking water).

## 8. Summary

| Concept | Equation |
|---|---|
| Ideal gas law | $PV = nRT$ |
| Combined gas law | $P_1V_1/T_1 = P_2V_2/T_2$ |
| Gas density | $\rho = PM/(RT)$ |
| Dalton's law | $P_{\text{tot}} = \sum P_i$; $P_i = \chi_iP_{\text{tot}}$ |
| Graham's law | $r_1/r_2 = \sqrt{M_2/M_1}$ |
| Clausius–Clapeyron | $\ln(P_2/P_1) = -\frac{\Delta H_{\text{vap}}}{R}(1/T_2 - 1/T_1)$ |
| Henry's law | $C = k_HP$ |
| Raoult's law | $P = \chi_{\text{solvent}}P^\circ$ |
| Boiling-point elevation | $\Delta T_b = iK_bm$ |
| Freezing-point depression | $\Delta T_f = iK_fm$ |
| Osmotic pressure | $\Pi = iMRT$ |
