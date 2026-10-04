---
title: Thermochemistry and Chemical Thermodynamics
field: Chemistry
subfield: Physical Chemistry
level: high-school to undergraduate
keywords: [thermochemistry, system and surroundings, endothermic, exothermic, enthalpy, calorimetry, bomb calorimeter, Hess's law, standard enthalpy of formation, bond enthalpy, entropy, standard molar entropy, second law, Gibbs free energy, spontaneity, temperature dependence of spontaneity, standard free energy of formation, equilibrium constant, coupled reactions, ATP]
---

# Thermochemistry and Chemical Thermodynamics

Why do some reactions release heat while others absorb it? Why does ice melt above 0 °C but not below? Why can some reactions run "uphill" by absorbing heat? Chemical thermodynamics answers these questions with three state functions: **enthalpy** ($H$), **entropy** ($S$) and **Gibbs free energy** ($G$). It tells us whether a reaction *can* happen and how far it goes — but not how fast (that is kinetics).

## 1. Energy, Heat and Work in Chemistry

- **System:** the reaction mixture; **surroundings:** everything else.
- **Exothermic process:** releases heat to the surroundings ($q < 0$ for the system); the surroundings warm up. Examples: combustion, neutralization, freezing, condensation, respiration.
- **Endothermic process:** absorbs heat ($q > 0$); surroundings cool. Examples: melting, evaporation, photosynthesis, dissolving NH₄NO₃, thermal decomposition of CaCO₃.

**First law (chemistry sign convention):** $\Delta U = q + w$, where $w$ is work done **on** the system. For expansion against constant external pressure, $w = -P_{\text{ext}}\Delta V$.

Chemical energy is stored in the arrangement of atoms and electrons: breaking bonds requires energy; forming bonds releases energy. A reaction is exothermic if the bonds formed are stronger overall than those broken.

## 2. Enthalpy

Most chemistry happens at constant pressure (open to the atmosphere). The heat exchanged at constant pressure equals the change in **enthalpy**:
$$H = U + PV, \qquad \boxed{\Delta H = q_P}$$
- $\Delta H < 0$: exothermic. $\Delta H > 0$: endothermic.
- Enthalpy is a **state function**: $\Delta H$ depends only on initial and final states.
- $\Delta H$ is **extensive**: doubling the amounts doubles $\Delta H$. Reversing a reaction reverses the sign of $\Delta H$.
- $\Delta H$ and $\Delta U$ differ by $\Delta(PV)$; for reactions involving gases, $\Delta H = \Delta U + \Delta n_{\text{gas}}RT$. The difference is usually small (a few kJ/mol).

**Thermochemical equation:**
$$\text{CH}_4(g) + 2\text{O}_2(g) \to \text{CO}_2(g) + 2\text{H}_2\text{O}(l), \qquad \Delta H° = -890.3\text{ kJ/mol}$$
States matter: forming H₂O(g) instead of H₂O(l) releases 88 kJ less (2 × 44 kJ/mol, the enthalpy of vaporization).

## 3. Calorimetry

Measuring heat flow with a calorimeter: $q = mc\Delta T$ or $q = C_{\text{cal}}\Delta T$.

**Coffee-cup calorimeter** (constant pressure, measures $\Delta H$): reactions in solution.

**Worked example 3.1:** 50.0 mL of 1.00 M HCl and 50.0 mL of 1.00 M NaOH, both at 22.0 °C, are mixed; the temperature rises to 28.7 °C. Assume density 1.00 g/mL and $c = 4.18$ J/(g·°C).
$q_{\text{soln}} = 100.0\times4.18\times6.7 = 2800$ J. Moles of water formed: 0.0500 mol.
$\Delta H = -2800/0.0500 = -56$ kJ/mol (accepted value −55.8 kJ/mol).

**Bomb calorimeter** (constant volume, measures $\Delta U$): combustion in a sealed steel vessel under O₂. Used to determine the energy content of fuels and foods.

**Food energy:** carbohydrates and proteins ~17 kJ/g (4 kcal/g); fats ~37 kJ/g (9 kcal/g); ethanol ~29 kJ/g (7 kcal/g).

## 4. Hess's Law

> If a reaction can be expressed as the sum of several steps, its enthalpy change is the sum of the enthalpy changes of the steps.

This follows from enthalpy being a state function (Germain Hess, 1840). It lets us find $\Delta H$ for reactions that are hard to measure directly.

**Worked example 4.1:** find $\Delta H$ for $\text{C(s)} + \frac12\text{O}_2(g) \to \text{CO}(g)$ (incomplete combustion can't be done cleanly).
Known:
(1) $\text{C(s)} + \text{O}_2 \to \text{CO}_2$, $\Delta H_1 = -393.5$ kJ
(2) $\text{CO} + \frac12\text{O}_2 \to \text{CO}_2$, $\Delta H_2 = -283.0$ kJ
Target = (1) − (2): $\Delta H = -393.5 - (-283.0) = -110.5$ kJ.

## 5. Standard Enthalpies of Formation

**Standard state:** pure substance at 1 bar (gases), 1 M (solutions), usually 25 °C, in its most stable form. Marked with °.

The **standard enthalpy of formation** $\Delta H_f°$ is the enthalpy change to form 1 mol of a compound from its elements in their standard states. By definition, $\Delta H_f° = 0$ for elements in their standard states (O₂(g), C(graphite), H₂(g), Fe(s), Br₂(l)...).

$$\boxed{\Delta H°_{\text{rxn}} = \sum n\,\Delta H_f°(\text{products}) - \sum n\,\Delta H_f°(\text{reactants})}$$

| Substance | $\Delta H_f°$ (kJ/mol) | | Substance | $\Delta H_f°$ (kJ/mol) |
|---|---|---|---|---|
| H₂O(l) | −285.8 | | CH₄(g) | −74.8 |
| H₂O(g) | −241.8 | | C₂H₆(g) | −84.7 |
| CO₂(g) | −393.5 | | C₂H₄(g) | +52.3 |
| CO(g) | −110.5 | | C₂H₂(g) | +226.7 |
| NH₃(g) | −45.9 | | C₂H₅OH(l) | −277.7 |
| NO(g) | +90.3 | | C₆H₁₂O₆(s) | −1273 |
| NO₂(g) | +33.2 | | C₆H₆(l) | +49.0 |
| SO₂(g) | −296.8 | | CaCO₃(s) | −1206.9 |
| HCl(g) | −92.3 | | CaO(s) | −635.1 |
| NaCl(s) | −411.2 | | Fe₂O₃(s) | −824.2 |
| O₃(g) | +142.7 | | Al₂O₃(s) | −1675.7 |
| C(diamond) | +1.9 | | H₂O₂(l) | −187.8 |

**Worked example 5.1:** enthalpy of combustion of ethanol:
$\text{C}_2\text{H}_5\text{OH}(l) + 3\text{O}_2(g) \to 2\text{CO}_2(g) + 3\text{H}_2\text{O}(l)$
$\Delta H° = [2(-393.5) + 3(-285.8)] - [(-277.7) + 0] = [-787.0 - 857.4] + 277.7 = -1366.7$ kJ/mol.

**Worked example 5.2:** thermite reaction, $2\text{Al} + \text{Fe}_2\text{O}_3 \to \text{Al}_2\text{O}_3 + 2\text{Fe}$:
$\Delta H° = -1675.7 - (-824.2) = -851.5$ kJ — enough to melt the iron produced (used for welding railroad tracks).

### Bond enthalpies (estimates)
$$\Delta H \approx \sum D(\text{bonds broken}) - \sum D(\text{bonds formed})$$
Average bond enthalpies give approximate values (within ~10%), since the strength of a given bond varies with molecular environment. Example: $\text{CH}_4 + 2\text{O}_2 \to \text{CO}_2 + 2\text{H}_2\text{O}(g)$: broken $4(413) + 2(498) = 2648$ kJ; formed $2(799) + 4(463) = 3450$ kJ; $\Delta H \approx -802$ kJ (actual −802.3 kJ for gaseous water — this example happens to agree closely).

## 6. Entropy

Many spontaneous processes are endothermic: ice melting at room temperature, NH₄NO₃ dissolving, water evaporating. Energy alone does not decide spontaneity. The other factor is **entropy** ($S$), a measure of the number of microscopic arrangements (microstates) consistent with a macroscopic state — loosely, the dispersal of energy and matter:
$$S = k_B\ln W$$

### Predicting the sign of ΔS
Entropy increases ($\Delta S > 0$) when:
- Solid → liquid → gas ($S_{\text{gas}} \gg S_{\text{liquid}} > S_{\text{solid}}$).
- The number of moles of gas increases: $\text{CaCO}_3(s) \to \text{CaO}(s) + \text{CO}_2(g)$, $\Delta S > 0$.
- A solid or liquid dissolves (usually).
- Temperature rises.
- Molecules become larger or more complex (more vibrational/rotational modes).
- Gases expand or mix.

### Standard molar entropies
Thanks to the **third law** ($S = 0$ for a perfect crystal at 0 K), absolute entropies can be measured. Unlike $\Delta H_f°$, **elements have nonzero $S°$**.

| Substance | $S°$ (J/(mol·K)) |
|---|---|
| C(diamond) | 2.4 |
| C(graphite) | 5.7 |
| Fe(s) | 27.3 |
| H₂O(l) | 69.9 |
| H₂O(g) | 188.8 |
| H₂(g) | 130.7 |
| N₂(g) | 191.6 |
| O₂(g) | 205.2 |
| CO₂(g) | 213.8 |
| NH₃(g) | 192.8 |
| CH₄(g) | 186.3 |

$$\Delta S°_{\text{rxn}} = \sum nS°(\text{products}) - \sum nS°(\text{reactants})$$

### Second law in chemistry
For a spontaneous process, the total entropy of system plus surroundings increases:
$$\Delta S_{\text{univ}} = \Delta S_{\text{sys}} + \Delta S_{\text{surr}} > 0$$
At constant $T$ and $P$, the heat released to the surroundings is $-\Delta H_{\text{sys}}$, so $\Delta S_{\text{surr}} = -\Delta H_{\text{sys}}/T$. Exothermic reactions increase the entropy of the surroundings — more so at low temperature.

## 7. Gibbs Free Energy

Combining: $\Delta S_{\text{univ}} = \Delta S_{\text{sys}} - \Delta H_{\text{sys}}/T$. Multiplying by $-T$ defines the change in **Gibbs free energy** (J. Willard Gibbs, 1870s):
$$\boxed{\Delta G = \Delta H - T\Delta S} = -T\Delta S_{\text{univ}}$$

**Spontaneity criterion (constant $T$ and $P$):**
- $\Delta G < 0$: spontaneous (thermodynamically favorable) in the forward direction.
- $\Delta G > 0$: non-spontaneous forward; the reverse is spontaneous.
- $\Delta G = 0$: equilibrium.

"Spontaneous" does not mean fast. Diamond converting to graphite has $\Delta G° = -2.9$ kJ/mol — spontaneous — but immeasurably slow at room temperature. "Diamonds are forever" is a kinetic, not thermodynamic, statement.

$\Delta G$ also equals the **maximum non-expansion work** obtainable from a process (e.g. electrical work from a battery or fuel cell, or biochemical work in cells).

### Temperature and spontaneity

| $\Delta H$ | $\Delta S$ | $\Delta G = \Delta H - T\Delta S$ | Spontaneous? | Example |
|---|---|---|---|---|
| − | + | Always − | At all temperatures | Combustion; $2\text{H}_2\text{O}_2\to2\text{H}_2\text{O} + \text{O}_2$ |
| + | − | Always + | Never (reverse always) | $3\text{O}_2\to2\text{O}_3$ |
| − | − | − at low $T$ | Below $T = \Delta H/\Delta S$ | Freezing water; $\text{N}_2 + 3\text{H}_2\to2\text{NH}_3$ |
| + | + | − at high $T$ | Above $T = \Delta H/\Delta S$ | Melting ice; $\text{CaCO}_3\to\text{CaO} + \text{CO}_2$ |

The crossover temperature is $T = \Delta H/\Delta S$ (assuming both are roughly temperature-independent).

**Worked example 7.1 — Melting ice:** $\Delta H_{\text{fus}} = +6.01$ kJ/mol, $\Delta S_{\text{fus}} = +22.0$ J/(mol·K). $T = 6010/22.0 = 273$ K = 0 °C. Above 0 °C, $T\Delta S > \Delta H$ and melting is spontaneous; below, freezing is.

**Worked example 7.2 — Limestone decomposition:** $\text{CaCO}_3(s)\to\text{CaO}(s) + \text{CO}_2(g)$. $\Delta H° = -635.1 - 393.5 + 1206.9 = +178.3$ kJ; $\Delta S° = 38.1 + 213.8 - 92.9 = +159.0$ J/K. At 25 °C, $\Delta G° = 178.3 - 298.15\times0.1590 = +130.9$ kJ (non-spontaneous). Spontaneous above $T = 178\,300/159.0 \approx 1121$ K (~850 °C) — which is why lime kilns operate around 900 °C. (Cement production releases CO₂ from this reaction, ~8% of global CO₂ emissions.)

### Standard free energy of formation
$\Delta G_f° = 0$ for elements in standard states, and
$$\Delta G°_{\text{rxn}} = \sum n\,\Delta G_f°(\text{products}) - \sum n\,\Delta G_f°(\text{reactants})$$
Selected values (kJ/mol): H₂O(l) −237.1; H₂O(g) −228.6; CO₂(g) −394.4; CH₄(g) −50.5; NH₃(g) −16.4; NO(g) +86.6; C₆H₁₂O₆(s) −910.

## 8. Free Energy and Equilibrium

$\Delta G°$ refers to standard conditions; under other conditions:
$$\boxed{\Delta G = \Delta G° + RT\ln Q}$$
where $Q$ is the reaction quotient. At equilibrium $\Delta G = 0$ and $Q = K$, giving the fundamental link between thermodynamics and equilibrium:
$$\boxed{\Delta G° = -RT\ln K}, \qquad K = e^{-\Delta G°/RT}$$

| $\Delta G°$ (kJ/mol, 25 °C) | $K$ | Equilibrium position |
|---|---|---|
| −100 | $3\times10^{17}$ | Essentially complete |
| −10 | 57 | Products favored |
| 0 | 1 | Balanced |
| +10 | 0.018 | Reactants favored |
| +100 | $3\times10^{-18}$ | Essentially no reaction |

Every 5.7 kJ/mol of $\Delta G°$ changes $K$ by a factor of 10 at 25 °C.

**Van 't Hoff equation:** temperature dependence of $K$:
$$\ln\frac{K_2}{K_1} = -\frac{\Delta H°}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$$
For exothermic reactions, $K$ decreases as $T$ increases (consistent with Le Chatelier's principle).

## 9. Coupled Reactions and Biochemical Energetics

A non-spontaneous reaction can be driven by coupling it to a strongly spontaneous one, as long as the total $\Delta G < 0$.

**Smelting copper:** $\text{Cu}_2\text{S}\to2\text{Cu} + \text{S}$ ($\Delta G° = +86.2$ kJ) coupled with $\text{S} + \text{O}_2\to\text{SO}_2$ ($-300.1$ kJ) gives an overall $\Delta G° = -213.9$ kJ.

**ATP, the energy currency of cells:**
$$\text{ATP} + \text{H}_2\text{O}\to\text{ADP} + \text{P}_i, \qquad \Delta G°' \approx -30.5\text{ kJ/mol}$$
(under cellular conditions, $\Delta G \approx -50$ to $-57$ kJ/mol because of the concentrations involved). Cells couple ATP hydrolysis to unfavorable processes such as biosynthesis, active transport and muscle contraction. Glucose oxidation ($\Delta G° \approx -2870$ kJ/mol) regenerates ~30–32 ATP per glucose. An average adult turns over roughly their own body mass in ATP each day.

**Example coupling:** glutamate + NH₃ → glutamine ($\Delta G°' = +14.2$ kJ/mol) is driven by ATP hydrolysis via a phosphorylated intermediate; net $\Delta G°' \approx -16.3$ kJ/mol.

## 10. Summary

| Quantity | Meaning | Key equation |
|---|---|---|
| $\Delta H$ | Heat at constant pressure | $\Delta H° = \sum n\Delta H_f°(\text{prod}) - \sum n\Delta H_f°(\text{react})$ |
| Hess's law | $\Delta H$ is path-independent | Add steps |
| $\Delta S$ | Change in dispersal/microstates | $\Delta S° = \sum nS°(\text{prod}) - \sum nS°(\text{react})$ |
| $\Delta S_{\text{surr}}$ | | $-\Delta H_{\text{sys}}/T$ |
| $\Delta G$ | Spontaneity at constant $T$, $P$ | $\Delta G = \Delta H - T\Delta S$ |
| Non-standard | | $\Delta G = \Delta G° + RT\ln Q$ |
| Equilibrium | | $\Delta G° = -RT\ln K$ |
| Van 't Hoff | $K$ vs $T$ | $\ln(K_2/K_1) = -\frac{\Delta H°}{R}(1/T_2 - 1/T_1)$ |
| Calorimetry | | $q = mc\Delta T$ |
