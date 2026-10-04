---
title: Chemical Equilibrium
field: Chemistry
subfield: Physical Chemistry
level: high-school to undergraduate
keywords: [dynamic equilibrium, equilibrium constant, law of mass action, Kc, Kp, reaction quotient, heterogeneous equilibrium, ICE table, Le Chatelier's principle, effect of concentration, pressure, temperature, catalyst, solubility product, Ksp, common ion effect, precipitation, complex ion equilibria, Haber process]
---

# Chemical Equilibrium

Many reactions do not go to completion. Instead they reach a state where reactants and products coexist in constant concentrations. This **chemical equilibrium** is not static: forward and reverse reactions continue at equal rates. Understanding equilibrium lets chemists predict yields, optimize industrial processes (like ammonia synthesis), and explain phenomena from blood pH to cave formation.

## 1. Dynamic Equilibrium

Consider $\text{N}_2\text{O}_4(g)\rightleftharpoons2\text{NO}_2(g)$ (colorless ⇌ brown). Starting with pure N₂O₄, the forward rate is initially high; as NO₂ accumulates, the reverse rate increases. Eventually:
$$\text{rate}_{\text{forward}} = \text{rate}_{\text{reverse}}$$
and concentrations stop changing — though molecules continue to react in both directions (demonstrated with isotopic labeling). The same equilibrium state is reached whether one starts from reactants or products.

## 2. The Equilibrium Constant

### Law of mass action
For the general reaction $a\text{A} + b\text{B}\rightleftharpoons c\text{C} + d\text{D}$ at equilibrium (Guldberg and Waage, 1864):
$$\boxed{K_c = \frac{[\text{C}]^c[\text{D}]^d}{[\text{A}]^a[\text{B}]^b}}$$
For gases, partial pressures can be used:
$$K_p = \frac{P_\text{C}^cP_\text{D}^d}{P_\text{A}^aP_\text{B}^b}, \qquad K_p = K_c(RT)^{\Delta n}$$
where $\Delta n$ = moles of gaseous products − moles of gaseous reactants (with $R = 0.08206$ L·atm/(mol·K)).

Strictly, $K$ is defined with **activities** (dimensionless effective concentrations relative to standard states), so $K$ is dimensionless; concentrations in M and pressures in bar/atm approximate activities for dilute solutions and ideal gases.

### Rules for writing K
- **Pure solids and pure liquids are omitted** (activity = 1). For $\text{CaCO}_3(s)\rightleftharpoons\text{CaO}(s) + \text{CO}_2(g)$: $K_p = P_{\text{CO}_2}$. The solvent (water in dilute aqueous solution) is also omitted.
- **Reversing a reaction:** $K' = 1/K$.
- **Multiplying coefficients by $n$:** $K' = K^n$.
- **Adding reactions:** multiply their $K$ values.

### Magnitude of K
- $K \gg 1$ (e.g. > $10^3$): products favored; reaction goes nearly to completion. $\text{H}_2 + \text{Cl}_2\rightleftharpoons2\text{HCl}$, $K \approx 10^{33}$ at 25 °C.
- $K \ll 1$ (< $10^{-3}$): reactants favored; little product. $\text{N}_2 + \text{O}_2\rightleftharpoons2\text{NO}$, $K \approx 4.6\times10^{-31}$ at 25 °C (fortunately, or the atmosphere would react away — though $K$ increases at high temperatures in engines and lightning, producing NO pollution).
- $K \approx 1$: significant amounts of both.

$K$ depends only on temperature (not on initial concentrations, pressure, or catalysts). It is related to thermodynamics by $\Delta G° = -RT\ln K$.

## 3. The Reaction Quotient Q

$Q$ has the same form as $K$ but uses current (not necessarily equilibrium) concentrations. Comparing $Q$ with $K$ predicts the direction of reaction:
- $Q < K$: too few products → reaction proceeds **forward**.
- $Q > K$: too many products → reaction proceeds **in reverse**.
- $Q = K$: at equilibrium.

Thermodynamically, $\Delta G = RT\ln(Q/K)$: negative when $Q < K$.

## 4. Calculating Equilibrium Concentrations (ICE Tables)

**ICE** = Initial, Change, Equilibrium.

### Worked example 4.1
$\text{H}_2(g) + \text{I}_2(g)\rightleftharpoons2\text{HI}(g)$, $K_c = 50.5$ at 448 °C. Initially 1.00 mol H₂ and 1.00 mol I₂ in a 1.00 L flask. Find equilibrium concentrations.

| | H₂ | I₂ | HI |
|---|---|---|---|
| Initial | 1.00 | 1.00 | 0 |
| Change | −x | −x | +2x |
| Equilibrium | 1.00 − x | 1.00 − x | 2x |

$50.5 = \frac{(2x)^2}{(1.00 - x)^2}$ → taking square roots: $7.106 = \frac{2x}{1.00 - x}$ → $x = \frac{7.106}{9.106} = 0.780$.
$[\text{H}_2] = [\text{I}_2] = 0.220$ M; $[\text{HI}] = 1.56$ M. Check: $1.56^2/0.220^2 = 50.3$ ✓.

### Worked example 4.2 — Small-K approximation
$\text{N}_2\text{O}_4\rightleftharpoons2\text{NO}_2$, $K_c = 4.64\times10^{-3}$ at 25 °C, starting with 0.100 M N₂O₄.
$4.64\times10^{-3} = \frac{(2x)^2}{0.100 - x}$. If $x \ll 0.100$: $4x^2 = 4.64\times10^{-4}$, $x = 0.0108$. That is 10.8% of 0.100 — above the usual 5% threshold, so solve the quadratic: $4x^2 + 4.64\times10^{-3}x - 4.64\times10^{-4} = 0$ → $x = 0.0102$ M. $[\text{NO}_2] = 0.0204$ M, $[\text{N}_2\text{O}_4] = 0.0898$ M.

**The 5% rule:** if $x$ is less than 5% of the initial concentration, the approximation is acceptable.

## 5. Le Chatelier's Principle

> If a system at equilibrium is disturbed, it shifts in the direction that tends to counteract the disturbance. — Henri Le Chatelier, 1884

### Concentration changes
- Adding a reactant or removing a product → shifts **right** (toward products).
- Adding a product or removing a reactant → shifts **left**.
- $K$ is unchanged; $Q$ temporarily differs from $K$ and the system readjusts.
- Industrial chemists continuously remove products to drive reactions (e.g. condensing ammonia out of the Haber reactor; distilling off water in esterification).

### Pressure and volume changes (gases)
- **Decreasing volume** (increasing pressure) shifts toward the side with **fewer moles of gas**.
- Increasing volume shifts toward more moles of gas.
- No effect if $\Delta n_{\text{gas}} = 0$ (e.g. H₂ + I₂ ⇌ 2HI).
- Adding an inert gas at constant volume has **no effect** (partial pressures unchanged).

### Temperature changes
Temperature changes **$K$ itself**. Treat heat as a reactant (endothermic) or product (exothermic):
- **Exothermic** ($\Delta H < 0$): raising $T$ shifts left, $K$ decreases.
- **Endothermic** ($\Delta H > 0$): raising $T$ shifts right, $K$ increases.

Example: $\text{N}_2\text{O}_4\rightleftharpoons2\text{NO}_2$ is endothermic ($\Delta H° = +57.2$ kJ). A sealed tube turns darker brown in hot water and paler in ice water — a classic demonstration.

Example: $[\text{Co(H}_2\text{O)}_6]^{2+}$ (pink) + 4Cl⁻ ⇌ $[\text{CoCl}_4]^{2-}$ (blue) + 6H₂O is endothermic: heating turns the solution blue; cooling turns it pink. (Used in humidity indicators.)

### Catalysts
A catalyst does **not** shift equilibrium; it only helps the system reach equilibrium faster.

### The Haber–Bosch process: a case study
$$\text{N}_2(g) + 3\text{H}_2(g)\rightleftharpoons2\text{NH}_3(g), \qquad \Delta H° = -92.2\text{ kJ}$$
- **High pressure** (150–300 atm) favors the side with fewer gas moles (2 vs. 4) → more NH₃.
- **Low temperature** would favor NH₃ (exothermic), but the rate would be too slow. A compromise of ~400–500 °C is used with an iron catalyst.
- NH₃ is removed by condensation and unreacted gases recycled, so overall conversion reaches ~97%.
- $K_p \approx 6\times10^5$ at 25 °C but only ~$1.5\times10^{-5}$ at 500 °C.

The process consumes 1–2% of the world's energy supply and is responsible for the nitrogen in roughly half of the protein in human bodies.

## 6. Solubility Equilibria

For a sparingly soluble ionic solid:
$$\text{M}_x\text{A}_y(s)\rightleftharpoons x\text{M}^{y+}(aq) + y\text{A}^{x-}(aq), \qquad K_{sp} = [\text{M}^{y+}]^x[\text{A}^{x-}]^y$$
$K_{sp}$ is the **solubility product constant**.

| Compound | $K_{sp}$ (25 °C) |
|---|---|
| AgCl | $1.8\times10^{-10}$ |
| AgBr | $5.0\times10^{-13}$ |
| AgI | $8.3\times10^{-17}$ |
| BaSO₄ | $1.1\times10^{-10}$ |
| CaCO₃ | $3.4\times10^{-9}$ (calcite) |
| CaF₂ | $3.9\times10^{-11}$ |
| Ca₃(PO₄)₂ | ~$2\times10^{-29}$ |
| Mg(OH)₂ | $5.6\times10^{-12}$ |
| Fe(OH)₃ | ~$3\times10^{-39}$ |
| PbI₂ | $9.8\times10^{-9}$ |
| CuS | ~$6\times10^{-37}$ |

### Molar solubility from Ksp
For AgCl: $K_{sp} = s^2$, $s = \sqrt{1.8\times10^{-10}} = 1.34\times10^{-5}$ M.
For CaF₂: $K_{sp} = s(2s)^2 = 4s^3$, $s = \sqrt[3]{3.9\times10^{-11}/4} = 2.1\times10^{-4}$ M.
For a general salt $\text{M}_x\text{A}_y$: $K_{sp} = x^xy^ys^{x+y}$.

Note: $K_{sp}$ values can only be compared directly to rank solubilities for salts with the same ion ratio.

### Common-ion effect
Adding an ion already present in the equilibrium suppresses solubility (Le Chatelier). Solubility of AgCl in 0.10 M NaCl: $K_{sp} = s(0.10 + s) \approx 0.10s$ → $s = 1.8\times10^{-9}$ M — about 7500 times lower than in pure water.

### Predicting precipitation
Compute the ion product $Q$ with actual concentrations:
- $Q > K_{sp}$: precipitate forms.
- $Q < K_{sp}$: unsaturated; no precipitate.
- $Q = K_{sp}$: saturated.

**Worked example 6.1:** mixing equal volumes of $2.0\times10^{-4}$ M AgNO₃ and $2.0\times10^{-4}$ M NaCl gives $[\text{Ag}^+] = [\text{Cl}^-] = 1.0\times10^{-4}$ M after dilution. $Q = 1.0\times10^{-8} > 1.8\times10^{-10}$ → AgCl precipitates.

**Selective precipitation:** ions can be separated by adding a reagent gradually, exploiting different $K_{sp}$ values (classical qualitative analysis schemes).

### Effects of pH and complexation on solubility
- Salts of basic anions (CO₃²⁻, OH⁻, F⁻, PO₄³⁻, S²⁻) become **more soluble in acid**, because H⁺ removes the anion. Examples: acid rain dissolves limestone and marble; tooth enamel (hydroxyapatite, Ca₅(PO₄)₃OH) dissolves in acids produced by bacteria. **Fluoride** converts it to fluorapatite (Ca₅(PO₄)₃F), which is less soluble and more acid-resistant.
- **Caves and stalactites:** CO₂-rich groundwater dissolves limestone: $\text{CaCO}_3 + \text{CO}_2 + \text{H}_2\text{O}\rightleftharpoons\text{Ca}^{2+} + 2\text{HCO}_3^-$. When the water drips into a cave and loses CO₂, the equilibrium shifts left and CaCO₃ deposits.
- **Kidney stones** (calcium oxalate, calcium phosphate) form when urine becomes supersaturated.
- **Barium sulfate** is used as a contrast agent for X-rays of the digestive tract despite Ba²⁺ being toxic, because its $K_{sp}$ is so low that very little dissolves.

## 7. Complex Ion Equilibria

Metal ions (Lewis acids) bind ligands (Lewis bases) to form **complex ions**, characterized by **formation constants** $K_f$:
$$\text{Ag}^+ + 2\text{NH}_3\rightleftharpoons[\text{Ag(NH}_3)_2]^+, \qquad K_f = \frac{[\text{Ag(NH}_3)_2^+]}{[\text{Ag}^+][\text{NH}_3]^2} = 1.7\times10^7$$
Complexation increases solubility: AgCl dissolves in aqueous ammonia because complex formation removes Ag⁺. The overall equilibrium constant is $K = K_{sp}K_f = (1.8\times10^{-10})(1.7\times10^7) = 3.1\times10^{-3}$.

**Chelating agents** (multidentate ligands) like EDTA form exceptionally stable complexes (the chelate effect, largely entropic). EDTA is used to treat heavy-metal poisoning, as a food preservative, in water softening, and in complexometric titrations. Heme (iron–porphyrin) and chlorophyll (magnesium–porphyrin) are biological chelates. Carbon monoxide is toxic because it binds hemoglobin's iron ~200–250 times more strongly than O₂.

## 8. Summary

| Concept | Formula / rule |
|---|---|
| Equilibrium constant | $K_c = \frac{[\text{C}]^c[\text{D}]^d}{[\text{A}]^a[\text{B}]^b}$ |
| $K_p$ vs $K_c$ | $K_p = K_c(RT)^{\Delta n}$ |
| Direction | $Q < K$ forward; $Q > K$ reverse |
| Thermodynamics link | $\Delta G° = -RT\ln K$ |
| Le Chatelier | System opposes disturbances |
| Temperature | Only temperature changes $K$ |
| Solubility product | $K_{sp} = [\text{M}]^x[\text{A}]^y$ |
| Precipitation | $Q > K_{sp}$ |
| Coupled equilibria | $K_{\text{overall}} = K_1K_2$ |
