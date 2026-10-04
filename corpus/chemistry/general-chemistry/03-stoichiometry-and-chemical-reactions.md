---
title: Stoichiometry, the Mole and Chemical Reactions
field: Chemistry
subfield: General Chemistry
level: high-school to undergraduate
keywords: [mole, Avogadro's number, molar mass, empirical formula, molecular formula, percent composition, chemical equation, balancing equations, limiting reactant, theoretical yield, percent yield, molarity, dilution, titration, precipitation reactions, solubility rules, net ionic equation, acid-base neutralization, oxidation-reduction, oxidation numbers, balancing redox, combustion analysis]
---

# Stoichiometry, the Mole and Chemical Reactions

**Stoichiometry** (from Greek *stoicheion*, "element", and *metron*, "measure") is the quantitative relationship between amounts of reactants and products in chemical reactions. It is the arithmetic of chemistry, used in every laboratory, pharmacy, factory and kitchen recipe scaled up to industrial production.

## 1. The Mole

Atoms are far too small to count individually, so chemists count them in batches. The **mole** (mol) is the SI unit for amount of substance:
$$\boxed{1\text{ mol} = 6.02214076\times10^{23}\text{ particles (exact)}}$$
This is **Avogadro's number** $N_A$ (or the Avogadro constant, $6.02214076\times10^{23}$ mol⁻¹). Since 2019 it is defined exactly; previously the mole was defined as the number of atoms in exactly 12 g of carbon-12.

A sense of scale: a mole of sand grains (each about 0.5 mm across) would bury the entire United States roughly 4 meters deep; a mole of seconds is about 19 million billion years — over a million times the age of the universe. Yet 18 g of water (about a tablespoon) contains one mole of molecules.

### Molar mass
The **molar mass** $M$ (g/mol) of a substance is numerically equal to its formula mass in atomic mass units:
- H₂O: $2(1.008) + 16.00 = 18.02$ g/mol
- CO₂: $12.01 + 2(16.00) = 44.01$ g/mol
- C₆H₁₂O₆ (glucose): $6(12.01) + 12(1.008) + 6(16.00) = 180.16$ g/mol
- NaCl: $22.99 + 35.45 = 58.44$ g/mol

### Key conversions
$$n = \frac{m}{M}, \qquad N = nN_A, \qquad n_{\text{gas}} = \frac{PV}{RT}\;(\text{or } V/22.4\text{ L at STP})$$

**Worked example 1.1:** How many molecules are in 5.00 g of water?
$n = 5.00/18.02 = 0.2775$ mol; $N = 0.2775\times6.022\times10^{23} = 1.671\times10^{23}$ molecules; H atoms: $3.34\times10^{23}$.

## 2. Chemical Formulas

### Percent composition
$$\%\text{ element} = \frac{(\text{number of atoms})\times(\text{atomic mass})}{\text{molar mass}}\times100\%$$
Glucose: %C $= 72.06/180.16 = 40.00\%$; %H $= 12.10/180.16 = 6.71\%$; %O $= 96.00/180.16 = 53.29\%$.

### Empirical and molecular formulas
- **Empirical formula:** simplest whole-number ratio of atoms (glucose: CH₂O).
- **Molecular formula:** actual numbers of atoms (C₆H₁₂O₆), a whole-number multiple of the empirical formula.

**Procedure** (from mass percentages):
1. Assume 100 g, so percentages become grams.
2. Convert grams to moles of each element.
3. Divide by the smallest number of moles.
4. Multiply by a small integer if needed to get whole numbers (e.g. 1.5 → ×2; 1.33 → ×3).
5. Molecular formula multiplier = (molar mass) / (empirical formula mass).

**Worked example 2.1:** A compound is 85.6% C and 14.4% H, with molar mass 56 g/mol.
C: $85.6/12.01 = 7.13$ mol; H: $14.4/1.008 = 14.3$ mol. Ratio 1 : 2.00 → empirical formula CH₂ (14.03 g/mol). Multiplier $56/14.03 = 4$ → molecular formula **C₄H₈** (a butene or cyclobutane).

### Combustion analysis
An organic compound is burned in excess O₂; CO₂ and H₂O are trapped and weighed. All C ends in CO₂ and all H in H₂O; oxygen is found by difference.

**Worked example 2.2:** Burning 0.255 g of a compound containing C, H and O gives 0.561 g CO₂ and 0.306 g H₂O.
C: $0.561\times\frac{12.01}{44.01} = 0.1531$ g → 0.01275 mol.
H: $0.306\times\frac{2.016}{18.02} = 0.03423$ g → 0.03396 mol.
O: $0.255 - 0.1531 - 0.0342 = 0.0677$ g → 0.00423 mol.
Ratio C : H : O = 3.01 : 8.03 : 1 → **C₃H₈O** (propanol or methoxyethane).

## 3. Chemical Equations

A balanced chemical equation obeys **conservation of mass**: the same number of each type of atom on both sides (and the same total charge).

$$\text{CH}_4(g) + 2\text{O}_2(g) \to \text{CO}_2(g) + 2\text{H}_2\text{O}(l)$$

State symbols: (s) solid, (l) liquid, (g) gas, (aq) aqueous solution.

### Balancing by inspection
1. Write correct formulas (never change subscripts to balance!).
2. Balance elements appearing in only one reactant and one product first; leave H and O (or free elements) for last.
3. Use the smallest whole-number coefficients.

**Example:** combustion of propane:
$\text{C}_3\text{H}_8 + \text{O}_2 \to \text{CO}_2 + \text{H}_2\text{O}$
C: 3 CO₂. H: 4 H₂O. O on the right: $6 + 4 = 10$ → 5 O₂.
$$\text{C}_3\text{H}_8 + 5\text{O}_2 \to 3\text{CO}_2 + 4\text{H}_2\text{O}$$

**Example:** combustion of octane (fractional coefficients then doubled):
$$2\text{C}_8\text{H}_{18} + 25\text{O}_2 \to 16\text{CO}_2 + 18\text{H}_2\text{O}$$

For complicated equations, the algebraic method (assign variables to coefficients and solve linear equations for each element) always works.

## 4. Reaction Stoichiometry

Coefficients give **mole ratios**. The standard path:
$$\text{mass of A} \xrightarrow{\div M_A}\text{mol A}\xrightarrow{\times\frac{\text{coef. B}}{\text{coef. A}}}\text{mol B}\xrightarrow{\times M_B}\text{mass of B}$$

**Worked example 4.1:** How much CO₂ forms when 100 g of propane burns completely?
$n(\text{C}_3\text{H}_8) = 100/44.10 = 2.268$ mol. $n(\text{CO}_2) = 3\times2.268 = 6.803$ mol. $m = 6.803\times44.01 = 299$ g.
Each gram of propane produces about 3 g of CO₂ — the added mass comes from atmospheric oxygen.

### Limiting reactant
When reactants are not in the exact stoichiometric ratio, the one consumed first — the **limiting reactant** — determines the maximum amount of product. The other is in **excess**.

**Method:** compute how much product each reactant could make; the smaller amount identifies the limiting reactant.

**Worked example 4.2:** 10.0 g of H₂ reacts with 64.0 g of O₂: $2\text{H}_2 + \text{O}_2 \to 2\text{H}_2\text{O}$.
H₂: $10.0/2.016 = 4.96$ mol → could make 4.96 mol H₂O.
O₂: $64.0/32.00 = 2.00$ mol → could make 4.00 mol H₂O.
**O₂ is limiting**; theoretical yield = $4.00\times18.02 = 72.1$ g H₂O. H₂ used: 4.00 mol; excess H₂ left: 0.96 mol (1.94 g).

### Yields
- **Theoretical yield:** maximum product from the limiting reactant.
- **Actual yield:** amount actually obtained.
- **Percent yield** $= \frac{\text{actual}}{\text{theoretical}}\times100\%$.

Yields fall below 100% due to incomplete reactions, side reactions, equilibrium limits, and losses during purification. In a multi-step synthesis, overall yield is the product of step yields: ten steps at 90% each give only 35% overall.

**Atom economy** (green chemistry): $\frac{\text{molar mass of desired product}}{\text{sum of molar masses of all reactants}}\times100\%$ — measures how much of the reactant atoms end up in the product rather than waste.

## 5. Solutions and Concentration

### Molarity
$$\boxed{M = \frac{\text{moles of solute}}{\text{liters of solution}}}\quad(\text{mol/L})$$
**Example:** dissolving 5.844 g NaCl (0.1000 mol) in water to make 250.0 mL of solution gives $0.1000/0.2500 = 0.4000$ M.

Other concentration units:
- **Molality** $m$ = mol solute / kg solvent (temperature-independent; used for colligative properties).
- **Mass percent** = mass solute / mass solution × 100%.
- **Mole fraction** $\chi_A = n_A/n_{\text{total}}$.
- **ppm / ppb** = parts per million/billion (for dilute aqueous solutions, 1 ppm ≈ 1 mg/L).

### Dilution
Moles of solute are unchanged:
$$\boxed{M_1V_1 = M_2V_2}$$
**Example:** to make 500 mL of 0.10 M HCl from 12 M stock: $V_1 = 0.10\times500/12 = 4.2$ mL, diluted to 500 mL. (Safety: always add acid to water, never water to acid, because the heat of dilution can boil water explosively.)

### Titration
A solution of known concentration (titrant) is added to an analyte until the reaction is exactly complete (**equivalence point**), detected with an indicator (color change at the **end point**) or a pH meter.

**Worked example 5.1:** 25.00 mL of HCl is titrated with 0.1000 M NaOH; the end point is reached after 31.25 mL.
$n(\text{NaOH}) = 0.1000\times0.03125 = 3.125\times10^{-3}$ mol $= n(\text{HCl})$ (1:1). $[\text{HCl}] = 3.125\times10^{-3}/0.02500 = 0.1250$ M.

## 6. Types of Chemical Reactions

### By pattern
| Type | General form | Example |
|---|---|---|
| Synthesis (combination) | A + B → AB | 2Na + Cl₂ → 2NaCl |
| Decomposition | AB → A + B | 2H₂O₂ → 2H₂O + O₂; CaCO₃ → CaO + CO₂ |
| Single displacement | A + BC → AC + B | Zn + CuSO₄ → ZnSO₄ + Cu |
| Double displacement (metathesis) | AB + CD → AD + CB | AgNO₃ + NaCl → AgCl↓ + NaNO₃ |
| Combustion | Fuel + O₂ → CO₂ + H₂O (+ energy) | CH₄ + 2O₂ → CO₂ + 2H₂O |

### Reactions in aqueous solution

#### Electrolytes
- **Strong electrolytes** dissociate completely: soluble ionic compounds (NaCl), strong acids (HCl), strong bases (NaOH).
- **Weak electrolytes** partially ionize: weak acids (acetic acid), weak bases (NH₃).
- **Nonelectrolytes** do not ionize: sugar, ethanol.

#### Precipitation reactions and solubility rules
An insoluble product (precipitate) forms when certain ions combine.

| Generally soluble | Exceptions |
|---|---|
| Group 1 (Li⁺, Na⁺, K⁺...) and NH₄⁺ salts | — |
| Nitrates (NO₃⁻), acetates (CH₃COO⁻), perchlorates | — |
| Chlorides, bromides, iodides | Ag⁺, Pb²⁺, Hg₂²⁺ |
| Sulfates (SO₄²⁻) | Ba²⁺, Sr²⁺, Pb²⁺, Ca²⁺ (slightly), Ag⁺ (slightly) |

| Generally insoluble | Exceptions |
|---|---|
| Carbonates, phosphates, sulfides | Group 1 and NH₄⁺ |
| Hydroxides | Group 1, NH₄⁺, Ba²⁺ (Ca²⁺, Sr²⁺ slightly) |

#### Molecular, complete ionic and net ionic equations
For mixing silver nitrate and sodium chloride solutions:
- Molecular: $\text{AgNO}_3(aq) + \text{NaCl}(aq) \to \text{AgCl}(s) + \text{NaNO}_3(aq)$
- Complete ionic: $\text{Ag}^+ + \text{NO}_3^- + \text{Na}^+ + \text{Cl}^- \to \text{AgCl}(s) + \text{Na}^+ + \text{NO}_3^-$
- **Net ionic:** $\text{Ag}^+(aq) + \text{Cl}^-(aq) \to \text{AgCl}(s)$

Na⁺ and NO₃⁻ are **spectator ions** — present but unchanged.

#### Acid–base (neutralization) reactions
Acid + base → salt + water. Net ionic equation for any strong acid with any strong base:
$$\text{H}^+(aq) + \text{OH}^-(aq) \to \text{H}_2\text{O}(l), \qquad \Delta H = -55.8\text{ kJ/mol}$$
Gas-forming variants: carbonates + acids → CO₂ (baking soda and vinegar: $\text{NaHCO}_3 + \text{CH}_3\text{COOH} \to \text{CH}_3\text{COONa} + \text{H}_2\text{O} + \text{CO}_2$).

## 7. Oxidation–Reduction (Redox) Reactions

**Oxidation** is the loss of electrons (increase in oxidation number); **reduction** is the gain of electrons (decrease in oxidation number). Mnemonic: **OIL RIG** — Oxidation Is Loss, Reduction Is Gain. They always occur together.
- **Reducing agent:** is oxidized (donates electrons).
- **Oxidizing agent:** is reduced (accepts electrons).

### Oxidation number rules
1. Free elements: 0 (Na, O₂, P₄).
2. Monatomic ions: equal to the charge (Na⁺ +1, Cl⁻ −1).
3. Fluorine: always −1 in compounds.
4. Oxygen: usually −2 (peroxides −1, e.g. H₂O₂; OF₂ +2).
5. Hydrogen: +1 with nonmetals, −1 with metals (hydrides, NaH).
6. Group 1 metals +1; group 2 metals +2 in compounds.
7. The sum equals the charge of the species.

**Examples:** S in H₂SO₄: $2(+1) + S + 4(-2) = 0 \Rightarrow S = +6$. Mn in MnO₄⁻: $Mn + 4(-2) = -1 \Rightarrow +7$. Cr in Cr₂O₇²⁻: $2Cr - 14 = -2 \Rightarrow +6$. C in CH₄: −4; in CO₂: +4 (combustion oxidizes carbon).

### Balancing redox equations: half-reaction method (acidic solution)
1. Split into oxidation and reduction half-reactions.
2. Balance atoms other than O and H.
3. Balance O by adding H₂O.
4. Balance H by adding H⁺.
5. Balance charge by adding electrons.
6. Multiply half-reactions so electrons cancel; add.
7. (In basic solution: add OH⁻ to both sides to neutralize H⁺, forming water; cancel.)

**Worked example 7.1:** permanganate oxidizes Fe²⁺ in acid.
Reduction: $\text{MnO}_4^- \to \text{Mn}^{2+}$
→ $\text{MnO}_4^- + 8\text{H}^+ + 5e^- \to \text{Mn}^{2+} + 4\text{H}_2\text{O}$
Oxidation: $\text{Fe}^{2+} \to \text{Fe}^{3+} + e^-$ (×5)
Sum:
$$\text{MnO}_4^- + 5\text{Fe}^{2+} + 8\text{H}^+ \to \text{Mn}^{2+} + 5\text{Fe}^{3+} + 4\text{H}_2\text{O}$$
Check: charge left $-1 + 10 + 8 = +17$; right $+2 + 15 = +17$ ✓. Permanganate titrations are self-indicating: purple MnO₄⁻ turns colorless Mn²⁺ until excess remains.

**Worked example 7.2:** dichromate oxidizes ethanol to acetic acid (the basis of old breathalyzers; orange Cr₂O₇²⁻ turns green Cr³⁺):
$$2\text{Cr}_2\text{O}_7^{2-} + 3\text{C}_2\text{H}_5\text{OH} + 16\text{H}^+ \to 4\text{Cr}^{3+} + 3\text{CH}_3\text{COOH} + 11\text{H}_2\text{O}$$

### Common redox processes
- **Combustion:** fuels are oxidized by O₂.
- **Corrosion:** rusting of iron, $4\text{Fe} + 3\text{O}_2 + 2x\text{H}_2\text{O} \to 2\text{Fe}_2\text{O}_3\cdot x\text{H}_2\text{O}$.
- **Metal displacement and the activity series:** a more active metal displaces a less active one from solution. Activity series (most to least active): Li > K > Ba > Ca > Na > Mg > Al > Zn > Fe > Ni > Sn > Pb > (H) > Cu > Ag > Hg > Pt > Au. Metals above hydrogen displace H₂ from acids.
- **Batteries, electrolysis, photosynthesis and cellular respiration** are redox processes.
- **Disproportionation:** one species is simultaneously oxidized and reduced, e.g. $2\text{H}_2\text{O}_2 \to 2\text{H}_2\text{O} + \text{O}_2$ (O goes from −1 to −2 and 0).

## 8. Summary

| Concept | Formula |
|---|---|
| Moles from mass | $n = m/M$ |
| Particles | $N = nN_A$, $N_A = 6.022\times10^{23}$ mol⁻¹ |
| Molarity | $M = n/V$ |
| Dilution | $M_1V_1 = M_2V_2$ |
| Percent yield | actual/theoretical × 100% |
| Empirical → molecular | multiplier = $M$/(empirical formula mass) |
| Neutralization (net) | H⁺ + OH⁻ → H₂O |
| Redox | Oxidation = loss of e⁻; reduction = gain of e⁻ |

**Common mistakes:**
1. Changing subscripts instead of coefficients when balancing.
2. Using mass ratios instead of mole ratios.
3. Forgetting to identify the limiting reactant.
4. Confusing molarity (per liter of solution) with molality (per kg of solvent).
5. Forgetting diatomic elements (H₂, N₂, O₂, F₂, Cl₂, Br₂, I₂).
