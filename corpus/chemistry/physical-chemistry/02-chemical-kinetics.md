---
title: Chemical Kinetics - Reaction Rates and Mechanisms
field: Chemistry
subfield: Physical Chemistry
level: high-school to undergraduate
keywords: [reaction rate, rate law, rate constant, reaction order, initial rates method, integrated rate law, zero order, first order, second order, half-life, Arrhenius equation, activation energy, collision theory, transition state theory, activated complex, reaction mechanism, elementary step, molecularity, rate-determining step, intermediate, steady-state approximation, catalysis, enzyme kinetics, Michaelis-Menten]
---

# Chemical Kinetics: Reaction Rates and Mechanisms

Thermodynamics tells us **whether** a reaction can occur; **kinetics** tells us **how fast** it occurs and **by what pathway**. A mixture of hydrogen and oxygen is thermodynamically primed to explode into water, yet it can sit unchanged for years — until a spark provides the activation energy. Kinetics governs everything from the shelf life of food and medicines to the design of catalytic converters, the depletion of ozone, and the speed of enzymes.

## 1. Reaction Rates

For a reaction $a\text{A} + b\text{B}\to c\text{C} + d\text{D}$, the rate is defined so that it is the same regardless of which species is monitored:
$$\text{rate} = -\frac1a\frac{d[\text{A}]}{dt} = -\frac1b\frac{d[\text{B}]}{dt} = \frac1c\frac{d[\text{C}]}{dt} = \frac1d\frac{d[\text{D}]}{dt}$$
Units: M/s (mol L⁻¹ s⁻¹). Example: in $2\text{N}_2\text{O}_5\to4\text{NO}_2 + \text{O}_2$, NO₂ appears four times as fast as O₂ and twice as fast as N₂O₅ disappears.

- **Average rate:** $\Delta[\text{X}]/\Delta t$ over an interval.
- **Instantaneous rate:** slope of the tangent to the concentration–time curve.
- **Initial rate:** instantaneous rate at $t = 0$.

Rates are measured by tracking concentration over time via color (spectrophotometry, Beer–Lambert law $A = \varepsilon lc$), pressure, conductivity, pH, or sampling and analysis.

### Factors affecting rate
1. **Concentration** (or pressure for gases): more collisions.
2. **Temperature:** faster molecules, more energetic collisions; rates typically increase steeply.
3. **Surface area:** finely divided solids react faster (flour dust and coal dust explosions; powdered medicines dissolve faster).
4. **Catalysts:** provide alternative pathways with lower activation energy.
5. **Nature of reactants:** ionic reactions in solution are often nearly instantaneous; reactions breaking strong covalent bonds are slower.
6. **Light** (photochemical reactions), solvent, ionic strength.

## 2. Rate Laws

The **rate law** expresses how rate depends on concentrations:
$$\text{rate} = k[\text{A}]^m[\text{B}]^n$$
- $k$ is the **rate constant** (depends on temperature, not on concentration).
- $m$ and $n$ are the **orders** with respect to A and B; the overall order is $m + n$.
- **Orders must be determined experimentally.** They are generally *not* equal to the stoichiometric coefficients (they are only for elementary steps).

**Examples:**
- $2\text{NO} + \text{O}_2\to2\text{NO}_2$: rate $= k[\text{NO}]^2[\text{O}_2]$ (third order overall).
- $\text{H}_2 + \text{I}_2\to2\text{HI}$: rate $= k[\text{H}_2][\text{I}_2]$.
- $\text{H}_2 + \text{Br}_2\to2\text{HBr}$: rate $= \frac{k[\text{H}_2][\text{Br}_2]^{1/2}}{1 + k'[\text{HBr}]/[\text{Br}_2]}$ — a complex radical chain mechanism, despite the similar stoichiometry.
- $\text{CHCl}_3 + \text{Cl}_2\to\text{CCl}_4 + \text{HCl}$: rate $= k[\text{CHCl}_3][\text{Cl}_2]^{1/2}$ (fractional order).

Units of $k$ depend on overall order: zero order M/s; first order s⁻¹; second order M⁻¹s⁻¹; third order M⁻²s⁻¹.

### Method of initial rates
Vary one concentration at a time and observe the effect on the initial rate.

**Worked example 2.1:** for $\text{A} + \text{B}\to\text{C}$:

| Experiment | [A]₀ (M) | [B]₀ (M) | Initial rate (M/s) |
|---|---|---|---|
| 1 | 0.10 | 0.10 | $2.0\times10^{-3}$ |
| 2 | 0.20 | 0.10 | $8.0\times10^{-3}$ |
| 3 | 0.10 | 0.20 | $4.0\times10^{-3}$ |

Doubling [A] (1 → 2) quadruples the rate → second order in A. Doubling [B] (1 → 3) doubles the rate → first order in B.
Rate $= k[\text{A}]^2[\text{B}]$; from experiment 1, $k = \frac{2.0\times10^{-3}}{(0.10)^2(0.10)} = 2.0$ M⁻²s⁻¹.

## 3. Integrated Rate Laws

Integrating the rate law gives concentration as a function of time.

| Order | Rate law | Integrated form | Linear plot | Slope | Half-life |
|---|---|---|---|---|---|
| 0 | $k$ | $[\text{A}] = [\text{A}]_0 - kt$ | [A] vs $t$ | $-k$ | $\frac{[\text{A}]_0}{2k}$ |
| 1 | $k[\text{A}]$ | $\ln[\text{A}] = \ln[\text{A}]_0 - kt$ | ln[A] vs $t$ | $-k$ | $\frac{\ln2}{k}$ |
| 2 | $k[\text{A}]^2$ | $\frac{1}{[\text{A}]} = \frac{1}{[\text{A}]_0} + kt$ | 1/[A] vs $t$ | $+k$ | $\frac{1}{k[\text{A}]_0}$ |

(For $\text{rate} = -d[\text{A}]/dt$.) Plotting data in each form and seeing which is linear identifies the order.

### First-order reactions
Examples: radioactive decay; many decompositions (N₂O₅, H₂O₂ uncatalyzed); drug elimination from the body (often); isomerizations (cyclopropane → propene).
- The **half-life is independent of concentration** — a hallmark of first-order kinetics.
- After $n$ half-lives, $(1/2)^n$ remains. After 10 half-lives, less than 0.1%.

**Worked example 3.1:** the decomposition of N₂O₅ at 45 °C has $k = 6.2\times10^{-4}$ s⁻¹. Half-life: $\ln2/k = 1118$ s ≈ 18.6 min. Starting at 0.50 M, after 30 min (1800 s): $[\text{N}_2\text{O}_5] = 0.50e^{-1.116} = 0.164$ M.

**Pharmacokinetics:** a drug with a 6-hour half-life eliminated by first-order kinetics falls to 25% after 12 hours, 12.5% after 18 hours. Dosing schedules are based on half-lives. Ethanol, in contrast, is metabolized by **zero-order** kinetics at typical concentrations (the liver enzyme alcohol dehydrogenase is saturated): roughly 7–10 g per hour regardless of blood level.

### Zero-order reactions
Rate independent of concentration — typically when a catalyst surface or enzyme is saturated. Example: decomposition of NH₃ on a hot tungsten surface; alcohol metabolism.

### Second-order reactions
Examples: $2\text{NO}_2\to2\text{NO} + \text{O}_2$; dimerization of butadiene; many bimolecular reactions in solution. Half-life increases as the reaction proceeds (each half-life is twice as long as the previous one).

**Pseudo-first-order conditions:** if one reactant is in large excess, its concentration is effectively constant, and a second-order reaction behaves as first order in the other reactant: rate $= k[\text{A}][\text{B}]_0 = k'[\text{A}]$. Used to simplify kinetic measurements (e.g. hydrolysis in water).

## 4. Temperature Dependence: The Arrhenius Equation

Svante Arrhenius (1889) found that rate constants depend exponentially on temperature:
$$\boxed{k = Ae^{-E_a/RT}}$$
- $E_a$ = **activation energy** (kJ/mol), the minimum energy barrier for reaction.
- $A$ = **pre-exponential (frequency) factor**, related to collision frequency and orientation.

Taking logarithms: $\ln k = \ln A - \frac{E_a}{R}\cdot\frac1T$. A plot of $\ln k$ vs. $1/T$ (**Arrhenius plot**) is a straight line with slope $-E_a/R$.

Two-temperature form:
$$\ln\frac{k_2}{k_1} = -\frac{E_a}{R}\left(\frac{1}{T_2} - \frac{1}{T_1}\right)$$

**Worked example 4.1:** a reaction's rate constant doubles from 25 °C to 35 °C. Find $E_a$.
$\ln2 = \frac{E_a}{8.314}\left(\frac{1}{298.15} - \frac{1}{308.15}\right) = \frac{E_a}{8.314}(1.0884\times10^{-4})$ → $E_a = \frac{0.6931\times8.314}{1.0884\times10^{-4}} \approx 52.9$ kJ/mol.
This is the origin of the rule of thumb that "rates double for every 10 °C rise" — it holds for activation energies around 50 kJ/mol near room temperature.

**Applications:** refrigeration slows food spoilage; cooking speeds up chemistry (each 10 °C increase in a pressure cooker greatly shortens cooking time); cold-blooded animals become sluggish in the cold; fireflies flash faster on warm nights; crickets chirp faster with temperature (Dolbear's law).

## 5. Theories of Reaction Rates

### Collision theory
For a reaction to occur, molecules must:
1. **Collide.**
2. With **sufficient energy** (at least $E_a$) — the fraction of collisions with enough energy is ~$e^{-E_a/RT}$ (from the Maxwell–Boltzmann distribution).
3. With the **correct orientation** — described by a steric factor $p$ (often $\ll1$ for complex molecules).

$$k = pZe^{-E_a/RT}$$
where $Z$ is related to collision frequency. Only a tiny fraction of collisions are effective: for $E_a = 50$ kJ/mol at 298 K, $e^{-E_a/RT} \approx 1.7\times10^{-9}$.

### Transition state theory
(Eyring, Evans, Polanyi, 1935.) Reactants pass through a high-energy, fleeting **transition state** (activated complex, marked ‡) at the top of the energy barrier, in quasi-equilibrium with reactants:
$$k = \frac{k_BT}{h}e^{-\Delta G^\ddagger/RT} = \frac{k_BT}{h}e^{\Delta S^\ddagger/R}e^{-\Delta H^\ddagger/RT}$$
(Eyring equation; $k_BT/h \approx 6.2\times10^{12}$ s⁻¹ at 25 °C.) The transition state is a saddle point on the potential energy surface — partially formed and partially broken bonds — with a lifetime of femtoseconds. Ahmed Zewail observed transition states directly with femtosecond laser spectroscopy (Nobel 1999).

### Reaction energy diagrams
Plot potential energy along the **reaction coordinate**:
- Reactants → transition state (peak; height above reactants = $E_a$) → products.
- $\Delta H$ = energy of products − energy of reactants.
- For the reverse reaction, $E_{a,\text{rev}} = E_{a,\text{fwd}} - \Delta H$.
- **Intermediates** sit in local minima (valleys) between transition states in multi-step mechanisms.
- **Hammond's postulate:** the transition state resembles the species (reactant or product) closest to it in energy — early, reactant-like transition states for exothermic steps; late, product-like for endothermic steps.

## 6. Reaction Mechanisms

A **mechanism** is the sequence of **elementary steps** by which a reaction occurs at the molecular level. The steps must sum to the overall equation and must be consistent with the observed rate law.

### Elementary steps and molecularity
For an elementary step, the rate law **can** be written from its stoichiometry:

| Molecularity | Elementary step | Rate law |
|---|---|---|
| Unimolecular | A → products | $k[\text{A}]$ |
| Bimolecular | A + B → products | $k[\text{A}][\text{B}]$ |
| Bimolecular | 2A → products | $k[\text{A}]^2$ |
| Termolecular (rare) | A + B + C → products | $k[\text{A}][\text{B}][\text{C}]$ |

Termolecular steps are rare because simultaneous three-body collisions are improbable.

### Rate-determining step
The slowest step limits the overall rate — like the narrowest point of a funnel or the slowest worker on an assembly line.

**Example 6.1:** $\text{NO}_2 + \text{CO}\to\text{NO} + \text{CO}_2$, observed rate $= k[\text{NO}_2]^2$ (below ~225 °C).
Proposed mechanism:
- Step 1 (slow): $\text{NO}_2 + \text{NO}_2\to\text{NO}_3 + \text{NO}$
- Step 2 (fast): $\text{NO}_3 + \text{CO}\to\text{NO}_2 + \text{CO}_2$
Sum: $\text{NO}_2 + \text{CO}\to\text{NO} + \text{CO}_2$ ✓. Rate determined by step 1: $k_1[\text{NO}_2]^2$ ✓. CO does not appear in the rate law because it reacts after the slow step. NO₃ is an **intermediate** (formed then consumed).

**Example 6.2 — Fast pre-equilibrium:** $2\text{NO} + \text{O}_2\to2\text{NO}_2$, rate $= k[\text{NO}]^2[\text{O}_2]$.
- Step 1 (fast, reversible): $2\text{NO}\rightleftharpoons\text{N}_2\text{O}_2$, with $[\text{N}_2\text{O}_2] = K_1[\text{NO}]^2$
- Step 2 (slow): $\text{N}_2\text{O}_2 + \text{O}_2\to2\text{NO}_2$
Rate $= k_2[\text{N}_2\text{O}_2][\text{O}_2] = k_2K_1[\text{NO}]^2[\text{O}_2]$ ✓ — consistent without requiring a termolecular collision. (This reaction also has a **negative apparent activation energy**: it slows down as temperature rises, because the pre-equilibrium shifts left.)

### Steady-state approximation
For a reactive intermediate I present at low concentration, assume $d[\text{I}]/dt \approx 0$ after a brief induction period, and solve for [I] algebraically. More general than the pre-equilibrium approach; essential for chain reactions and enzyme kinetics.

### Chain reactions
Involve reactive intermediates (radicals) that are regenerated:
- **Initiation:** $\text{Cl}_2\xrightarrow{h\nu}2\text{Cl}\cdot$
- **Propagation:** $\text{Cl}\cdot + \text{CH}_4\to\text{HCl} + \cdot\text{CH}_3$; $\cdot\text{CH}_3 + \text{Cl}_2\to\text{CH}_3\text{Cl} + \text{Cl}\cdot$
- **Termination:** radicals combine ($2\text{Cl}\cdot\to\text{Cl}_2$, etc.)

**Branching chains**, where one radical produces two or more (e.g. $\text{H}\cdot + \text{O}_2\to\cdot\text{OH} + \cdot\text{O}\cdot$ in H₂/O₂ mixtures), cause explosions. Polymerization and combustion are chain reactions.

**Ozone depletion:** chlorine atoms from CFCs catalytically destroy ozone in the stratosphere: $\text{Cl}\cdot + \text{O}_3\to\text{ClO}\cdot + \text{O}_2$; $\text{ClO}\cdot + \text{O}\to\text{Cl}\cdot + \text{O}_2$ — net $\text{O}_3 + \text{O}\to2\text{O}_2$. A single chlorine atom can destroy ~100 000 ozone molecules. Molina, Rowland and Crutzen (Nobel 1995) elucidated this; the 1987 Montreal Protocol phased out CFCs, and the ozone layer is slowly recovering.

## 7. Catalysis

A **catalyst** increases the rate of a reaction without being consumed, by providing an alternative mechanism with **lower activation energy**. Key points:
- A catalyst speeds up the forward and reverse reactions **equally**; it does **not** change $\Delta H$, $\Delta G$, or the equilibrium constant — only how quickly equilibrium is reached.
- It appears in the mechanism but cancels from the overall equation.
- Roughly 80–90% of industrial chemical processes use catalysts.

**Example:** lowering $E_a$ from 75 to 50 kJ/mol at 25 °C speeds the reaction by $e^{25\,000/(8.314\times298)} \approx 2.4\times10^4$ times.

### Types
- **Homogeneous catalysis:** catalyst in the same phase as reactants. Examples: acid catalysis of ester hydrolysis; I⁻ catalyzing H₂O₂ decomposition; Cl atoms in ozone destruction; organometallic catalysts (Wilkinson's catalyst for hydrogenation; Grubbs catalysts for olefin metathesis, Nobel 2005).
- **Heterogeneous catalysis:** catalyst in a different phase, usually a solid surface. Reactants **adsorb**, bonds weaken and rearrange, products **desorb**. Examples:
  - **Haber–Bosch process:** $\text{N}_2 + 3\text{H}_2\rightleftharpoons2\text{NH}_3$ on iron (promoted with K₂O, Al₂O₃) at ~400–500 °C, 150–300 atm. Produces fertilizer that feeds roughly half the world's population (Haber, Nobel 1918; Bosch, 1931; Ertl studied the surface mechanism, Nobel 2007).
  - **Catalytic converters:** Pt, Pd and Rh convert CO → CO₂, hydrocarbons → CO₂ + H₂O, NOₓ → N₂.
  - **Contact process:** $2\text{SO}_2 + \text{O}_2\to2\text{SO}_3$ on V₂O₅ (sulfuric acid manufacture — the most produced chemical by mass).
  - **Ostwald process:** NH₃ oxidation on Pt–Rh gauze for nitric acid.
  - **Hydrogenation** of vegetable oils on Ni; **cracking** of petroleum on zeolites.
- **Biocatalysis (enzymes):** protein catalysts of remarkable speed and specificity.
- **Photocatalysis and electrocatalysis:** TiO₂ self-cleaning surfaces, water splitting, fuel-cell electrodes.
- **Organocatalysis:** small organic molecules as catalysts (List and MacMillan, Nobel 2021).

**Catalyst poisoning:** substances that bind strongly to active sites deactivate catalysts (lead deactivated early catalytic converters, which is one reason leaded gasoline was phased out; sulfur poisons many metal catalysts).

## 8. Enzyme Kinetics

Enzymes accelerate reactions by factors of $10^6$ to $10^{17}$. Orotidine 5'-phosphate decarboxylase speeds up a reaction whose uncatalyzed half-life is ~78 million years so that it occurs in milliseconds. Enzymes work by binding the substrate in an **active site**, stabilizing the transition state (which binds more tightly than the substrate), positioning catalytic groups (acid–base catalysis, covalent catalysis, metal ions) and excluding water.

### Michaelis–Menten kinetics
Mechanism: $\text{E} + \text{S}\underset{k_{-1}}{\overset{k_1}{\rightleftharpoons}}\text{ES}\xrightarrow{k_{\text{cat}}}\text{E} + \text{P}$. With the steady-state approximation for [ES]:
$$\boxed{v = \frac{V_{\max}[\text{S}]}{K_M + [\text{S}]}}, \qquad V_{\max} = k_{\text{cat}}[\text{E}]_{\text{total}}, \qquad K_M = \frac{k_{-1} + k_{\text{cat}}}{k_1}$$
- At low [S] ($\ll K_M$): $v \approx \frac{V_{\max}}{K_M}[\text{S}]$ — first order in substrate.
- At high [S] ($\gg K_M$): $v \to V_{\max}$ — zero order (enzyme saturated).
- $K_M$ is the substrate concentration at half-maximal velocity; a lower $K_M$ roughly indicates tighter binding.
- $k_{\text{cat}}$ (**turnover number**): substrate molecules converted per enzyme per second (carbonic anhydrase: ~$10^6$ s⁻¹; catalase: ~$4\times10^7$ s⁻¹).
- $k_{\text{cat}}/K_M$ (**specificity constant**): catalytic efficiency. The upper limit is set by diffusion (~$10^8$–$10^9$ M⁻¹s⁻¹); enzymes near this limit (triose phosphate isomerase, fumarase) are called "catalytically perfect".

**Lineweaver–Burk plot:** $\frac1v = \frac{K_M}{V_{\max}}\cdot\frac{1}{[\text{S}]} + \frac{1}{V_{\max}}$ (linearized, though modern fitting uses nonlinear regression).

### Inhibition
- **Competitive inhibitors** bind the active site, competing with substrate: apparent $K_M$ increases, $V_{\max}$ unchanged (overcome by high [S]). Examples: statins (inhibit HMG-CoA reductase), methotrexate, ethanol as antidote for methanol poisoning (competes for alcohol dehydrogenase).
- **Noncompetitive inhibitors** bind elsewhere: $V_{\max}$ decreases, $K_M$ unchanged.
- **Uncompetitive inhibitors** bind only ES: both decrease.
- **Irreversible inhibitors** covalently modify the enzyme: aspirin (acetylates cyclooxygenase), penicillin (acylates bacterial transpeptidase), nerve agents and organophosphate pesticides (acetylcholinesterase).

Many drugs are enzyme inhibitors; HIV protease inhibitors and kinase inhibitors (e.g. imatinib for chronic myeloid leukemia) are examples of rational design.

## 9. Summary

| Concept | Formula |
|---|---|
| Rate law | rate $= k[\text{A}]^m[\text{B}]^n$ |
| Zero order | $[\text{A}] = [\text{A}]_0 - kt$; $t_{1/2} = [\text{A}]_0/2k$ |
| First order | $\ln[\text{A}] = \ln[\text{A}]_0 - kt$; $t_{1/2} = 0.693/k$ |
| Second order | $1/[\text{A}] = 1/[\text{A}]_0 + kt$; $t_{1/2} = 1/(k[\text{A}]_0)$ |
| Arrhenius | $k = Ae^{-E_a/RT}$ |
| Two-point Arrhenius | $\ln(k_2/k_1) = -\frac{E_a}{R}(1/T_2 - 1/T_1)$ |
| Eyring | $k = \frac{k_BT}{h}e^{-\Delta G^\ddagger/RT}$ |
| Michaelis–Menten | $v = V_{\max}[\text{S}]/(K_M + [\text{S}])$ |
| Catalyst | Lowers $E_a$; does not change $K$ or $\Delta G$ |
