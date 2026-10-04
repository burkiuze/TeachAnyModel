---
title: Acids and Bases - pH, Equilibria, Buffers and Titrations
field: Chemistry
subfield: Physical Chemistry
level: high-school to undergraduate
keywords: [Arrhenius acid, Brønsted-Lowry acid, Lewis acid, conjugate acid-base pair, autoionization of water, Kw, pH, pOH, strong acid, weak acid, Ka, pKa, Kb, percent ionization, polyprotic acids, salt hydrolysis, buffers, Henderson-Hasselbalch equation, buffer capacity, titration curves, equivalence point, indicators, acid strength and molecular structure, blood pH, ocean acidification]
---

# Acids and Bases: pH, Equilibria, Buffers and Titrations

Acids and bases are everywhere: stomach acid (HCl), vinegar (acetic acid), citrus fruits (citric acid), soap and drain cleaner (bases), baking soda, antacids, batteries, fertilizers, and the precisely regulated pH of blood. Acid–base chemistry is central to biochemistry, environmental science, medicine and industry.

## 1. Definitions of Acids and Bases

### Arrhenius (1884)
- **Acid:** produces H⁺ (more precisely H₃O⁺) in water. HCl → H⁺ + Cl⁻.
- **Base:** produces OH⁻ in water. NaOH → Na⁺ + OH⁻.
Limited to aqueous solutions; cannot explain why NH₃ is a base.

### Brønsted–Lowry (1923)
- **Acid:** proton (H⁺) donor.
- **Base:** proton acceptor.
Acid–base reactions are proton transfers:
$$\underset{\text{acid}}{\text{HA}} + \underset{\text{base}}{\text{H}_2\text{O}}\rightleftharpoons\underset{\text{conj. acid}}{\text{H}_3\text{O}^+} + \underset{\text{conj. base}}{\text{A}^-}$$
$$\underset{\text{base}}{\text{NH}_3} + \underset{\text{acid}}{\text{H}_2\text{O}}\rightleftharpoons\underset{\text{conj. acid}}{\text{NH}_4^+} + \underset{\text{conj. base}}{\text{OH}^-}$$

**Conjugate acid–base pairs** differ by one H⁺: HCl/Cl⁻, H₂O/OH⁻, H₃O⁺/H₂O, NH₄⁺/NH₃, CH₃COOH/CH₃COO⁻.
- The stronger an acid, the weaker its conjugate base (and vice versa).
- Equilibrium favors formation of the weaker acid and weaker base.
- **Amphoteric (amphiprotic)** species act as either acid or base: H₂O, HCO₃⁻, HSO₄⁻, H₂PO₄⁻, amino acids.

The bare proton H⁺ does not exist free in water; it is bonded to water molecules as H₃O⁺ (hydronium), and more realistically as larger clusters (H₅O₂⁺, H₉O₄⁺). Protons move through water exceptionally fast by "hopping" along hydrogen-bonded chains (the Grotthuss mechanism).

### Lewis (1923)
- **Lewis acid:** electron-pair acceptor.
- **Lewis base:** electron-pair donor.
The most general definition; includes reactions without protons:
- $\text{BF}_3 + :\text{NH}_3\to\text{F}_3\text{B}{-}\text{NH}_3$
- $\text{Ag}^+ + 2:\text{NH}_3\to[\text{Ag(NH}_3)_2]^+$ (metal ions are Lewis acids)
- $\text{CO}_2 + \text{OH}^-\to\text{HCO}_3^-$
- AlCl₃ and FeBr₃ as Lewis acid catalysts in organic chemistry.

In organic chemistry, Lewis bases are **nucleophiles** and Lewis acids are **electrophiles** (in a kinetic sense).

## 2. Autoionization of Water and the pH Scale

Water ionizes slightly:
$$2\text{H}_2\text{O}\rightleftharpoons\text{H}_3\text{O}^+ + \text{OH}^-, \qquad \boxed{K_w = [\text{H}_3\text{O}^+][\text{OH}^-] = 1.0\times10^{-14}\text{ at 25 °C}}$$
In pure water, $[\text{H}_3\text{O}^+] = [\text{OH}^-] = 1.0\times10^{-7}$ M. (Only about 2 in a billion water molecules are ionized.)

$K_w$ increases with temperature (autoionization is endothermic): $K_w = 5.5\times10^{-14}$ at 50 °C, so neutral pH at 50 °C is 6.63 — neutral does not always mean pH 7.

### pH and pOH
Søren Sørensen (1909) introduced the logarithmic scale:
$$\boxed{\text{pH} = -\log_{10}[\text{H}_3\text{O}^+]}, \qquad \text{pOH} = -\log[\text{OH}^-], \qquad \text{pH} + \text{pOH} = 14.00\;(25\text{ °C})$$
- Acidic: pH < 7; neutral: pH = 7; basic (alkaline): pH > 7 (at 25 °C).
- Each pH unit is a **tenfold** change in [H₃O⁺]. pH 3 is 10 000 times more acidic than pH 7.
- pH can be negative (concentrated strong acids) or above 14.
- Significant figures: the number of decimal places in pH equals the number of significant figures in [H⁺].

| Substance | Approximate pH |
|---|---|
| Battery acid (H₂SO₄) | ~0–1 |
| Gastric juice | 1.5–3.5 |
| Lemon juice | ~2.0–2.6 |
| Vinegar | ~2.4–3.4 |
| Cola | ~2.5 |
| Coffee | ~5 |
| Normal rain (CO₂ dissolved) | ~5.6 |
| Acid rain | < 5.6 (as low as ~4) |
| Milk | ~6.5–6.8 |
| Pure water (25 °C) | 7.0 |
| Human blood | 7.35–7.45 |
| Seawater | ~8.1 |
| Baking soda solution | ~8.3 |
| Milk of magnesia | ~10.5 |
| Household ammonia | ~11.5 |
| Bleach | ~12.5 |
| Drain cleaner (NaOH) | ~14 |

## 3. Strong Acids and Bases

**Strong acids** ionize essentially completely in water: HCl, HBr, HI, HNO₃, HClO₄, H₂SO₄ (first proton only). Their conjugate bases (Cl⁻, NO₃⁻...) are negligibly basic.

**Strong bases:** group 1 hydroxides (LiOH, NaOH, KOH...) and heavier group 2 hydroxides (Ca(OH)₂, Sr(OH)₂, Ba(OH)₂), plus oxide ion O²⁻ and amide NH₂⁻ (which react completely with water).

**Leveling effect:** in water, all acids stronger than H₃O⁺ are "leveled" to H₃O⁺; their relative strengths can be distinguished only in less basic solvents (e.g. acetic acid).

**Worked example 3.1:** pH of 0.025 M HNO₃: $[\text{H}_3\text{O}^+] = 0.025$ M; pH $= -\log(0.025) = 1.60$.
pH of 0.010 M Ba(OH)₂: $[\text{OH}^-] = 0.020$ M; pOH = 1.70; pH = 12.30.

**Very dilute strong acids:** for $10^{-8}$ M HCl, water's own ionization cannot be ignored; pH ≈ 6.98, not 8.

## 4. Weak Acids and Bases

### Acid dissociation constant
$$\text{HA} + \text{H}_2\text{O}\rightleftharpoons\text{H}_3\text{O}^+ + \text{A}^-, \qquad \boxed{K_a = \frac{[\text{H}_3\text{O}^+][\text{A}^-]}{[\text{HA}]}}, \qquad \text{p}K_a = -\log K_a$$
Smaller $K_a$ (larger p$K_a$) → weaker acid.

| Acid | Formula | $K_a$ | p$K_a$ |
|---|---|---|---|
| Hydrogen sulfate ion | HSO₄⁻ | $1.0\times10^{-2}$ | 1.99 |
| Phosphoric acid | H₃PO₄ | $7.5\times10^{-3}$ | 2.12 |
| Hydrofluoric acid | HF | $6.8\times10^{-4}$ | 3.17 |
| Nitrous acid | HNO₂ | $4.5\times10^{-4}$ | 3.35 |
| Formic acid | HCOOH | $1.8\times10^{-4}$ | 3.75 |
| Benzoic acid | C₆H₅COOH | $6.3\times10^{-5}$ | 4.20 |
| Acetic acid | CH₃COOH | $1.8\times10^{-5}$ | 4.76 |
| Carbonic acid | H₂CO₃ (as CO₂(aq)) | $4.3\times10^{-7}$ | 6.37 |
| Hydrogen sulfide | H₂S | $1\times10^{-7}$ | ~7.0 |
| Dihydrogen phosphate | H₂PO₄⁻ | $6.2\times10^{-8}$ | 7.21 |
| Hypochlorous acid | HOCl | $3.0\times10^{-8}$ | 7.53 |
| Ammonium ion | NH₄⁺ | $5.6\times10^{-10}$ | 9.25 |
| Hydrocyanic acid | HCN | $4.9\times10^{-10}$ | 9.31 |
| Phenol | C₆H₅OH | $1.0\times10^{-10}$ | 10.0 |
| Bicarbonate | HCO₃⁻ | $4.7\times10^{-11}$ | 10.33 |
| Hydrogen phosphate | HPO₄²⁻ | $4.2\times10^{-13}$ | 12.38 |
| Water | H₂O | — | 15.7 (or 14.0, depending on convention) |

HF is a weak acid but extremely dangerous: it penetrates skin and binds calcium, causing deep tissue and bone damage and potentially fatal hypocalcemia. It also etches glass.

### Calculating the pH of a weak acid
**Worked example 4.1:** pH of 0.10 M acetic acid ($K_a = 1.8\times10^{-5}$).
ICE: $[\text{H}_3\text{O}^+] = [\text{A}^-] = x$, $[\text{HA}] = 0.10 - x \approx 0.10$.
$1.8\times10^{-5} = x^2/0.10$ → $x = 1.34\times10^{-3}$ M (1.3% of 0.10, approximation valid).
pH $= 2.87$. Percent ionization $= 1.3\%$.

Shortcut: $[\text{H}^+] \approx \sqrt{K_aC}$ when $C/K_a > 400$ (roughly).

**Percent ionization increases on dilution** (Le Chatelier: dilution favors the side with more particles): 0.010 M acetic acid is 4.2% ionized; 0.0010 M is about 12.6%.

### Bases and Kb
$$\text{B} + \text{H}_2\text{O}\rightleftharpoons\text{BH}^+ + \text{OH}^-, \qquad K_b = \frac{[\text{BH}^+][\text{OH}^-]}{[\text{B}]}$$
Examples: ammonia ($K_b = 1.8\times10^{-5}$), methylamine ($4.4\times10^{-4}$), pyridine ($1.7\times10^{-9}$), aniline ($4.3\times10^{-10}$).

**Relationship for conjugate pairs:**
$$\boxed{K_aK_b = K_w}, \qquad \text{p}K_a + \text{p}K_b = 14.00$$

**Worked example 4.2:** pH of 0.20 M NH₃: $x = \sqrt{1.8\times10^{-5}\times0.20} = 1.9\times10^{-3}$ M = [OH⁻]; pOH = 2.72; pH = 11.28.

### Polyprotic acids
Acids with more than one ionizable proton ionize stepwise, with $K_{a1} \gg K_{a2} \gg K_{a3}$ (removing H⁺ from an increasingly negative ion is harder).
- **H₂SO₄:** strong first, $K_{a2} = 1.0\times10^{-2}$.
- **H₃PO₄:** p$K_a$ = 2.12, 7.21, 12.38.
- **H₂CO₃:** p$K_a$ = 6.37, 10.33.
- **Citric acid** (triprotic): p$K_a$ = 3.13, 4.76, 6.40.
For most purposes, the pH is determined by the first ionization.

### Salt solutions (hydrolysis)
Ions from salts can act as acids or bases:
- **Neutral:** cation of a strong base + anion of a strong acid (NaCl, KNO₃).
- **Basic:** anion is the conjugate base of a weak acid (CH₃COONa, Na₂CO₃, NaF, Na₃PO₄). Sodium carbonate (washing soda) solutions are quite alkaline.
- **Acidic:** cation is the conjugate acid of a weak base (NH₄Cl), or a small, highly charged metal ion that polarizes coordinated water: $[\text{Al(H}_2\text{O)}_6]^{3+}\rightleftharpoons[\text{Al(H}_2\text{O)}_5\text{OH}]^{2+} + \text{H}^+$ (p$K_a$ ≈ 5.0). Fe³⁺ solutions are acidic for the same reason.
- **Both weak:** compare $K_a$ of the cation and $K_b$ of the anion (NH₄CN is basic since $K_b(\text{CN}^-) > K_a(\text{NH}_4^+)$).

**Worked example 4.3:** pH of 0.10 M sodium acetate. $K_b(\text{CH}_3\text{COO}^-) = 10^{-14}/1.8\times10^{-5} = 5.6\times10^{-10}$. $[\text{OH}^-] = \sqrt{5.6\times10^{-11}} = 7.5\times10^{-6}$ M; pOH = 5.13; pH = 8.87.

## 5. Molecular Structure and Acid Strength

For binary acids H–X:
- **Down a group, acidity increases** because the H–X bond weakens (larger atom, poorer overlap): HF ≪ HCl < HBr < HI. Bond strength dominates over electronegativity here.
- **Across a period, acidity increases** with electronegativity of X: CH₄ < NH₃ < H₂O < HF.

For oxyacids H–O–Y:
- More electronegative Y → stronger acid: HOCl (p$K_a$ 7.5) > HOBr (8.6) > HOI (10.6).
- More oxygen atoms on Y → stronger acid (inductive withdrawal and resonance delocalization of the conjugate base's charge): HOCl (7.5) < HClO₂ (2.0) < HClO₃ (~−1) < HClO₄ (~−10, very strong).

For carboxylic acids:
- **Resonance stabilization** of the carboxylate anion makes carboxylic acids (p$K_a$ ~4–5) far more acidic than alcohols (~16).
- **Inductive effects:** electron-withdrawing groups near the COOH increase acidity: CH₃COOH (4.76) < ClCH₂COOH (2.87) < Cl₂CHCOOH (1.35) < Cl₃CCOOH (0.66); CF₃COOH (0.23). The effect weakens with distance from the carboxyl group.
- Phenols (p$K_a$ ~10) are more acidic than alcohols because the phenoxide's charge is delocalized into the ring; nitro groups at ortho/para positions increase acidity further (2,4,6-trinitrophenol, picric acid, p$K_a$ 0.4).

**General principle:** anything that stabilizes the conjugate base (spreading out negative charge, placing it on electronegative atoms, resonance, induction, more s-character, solvation) strengthens the acid. (The "ARIO" mnemonic: Atom, Resonance, Induction, Orbital.)

## 6. Buffers

A **buffer** resists changes in pH when small amounts of acid or base are added. It contains comparable amounts of a weak acid and its conjugate base (e.g. CH₃COOH/CH₃COO⁻) or a weak base and its conjugate acid (NH₃/NH₄⁺).
- Added H⁺ is consumed by the base: $\text{A}^- + \text{H}^+\to\text{HA}$.
- Added OH⁻ is consumed by the acid: $\text{HA} + \text{OH}^-\to\text{A}^- + \text{H}_2\text{O}$.

### Henderson–Hasselbalch equation
$$\boxed{\text{pH} = \text{p}K_a + \log\frac{[\text{A}^-]}{[\text{HA}]}}$$
- When $[\text{A}^-] = [\text{HA}]$, pH = p$K_a$.
- A buffer is effective within about **p$K_a$ ± 1**. Choose an acid with p$K_a$ near the target pH.
- **Buffer capacity** — the amount of acid/base the buffer can absorb — increases with total concentration and is greatest when pH = p$K_a$.

**Worked example 6.1:** a buffer contains 0.50 M CH₃COOH and 0.50 M CH₃COONa (pH = 4.76). Add 0.010 mol HCl to 1.00 L.
New: [CH₃COOH] = 0.51 M, [CH₃COO⁻] = 0.49 M. pH $= 4.76 + \log(0.49/0.51) = 4.76 - 0.017 = 4.74$.
The same amount of HCl added to 1.00 L of pure water would change the pH from 7.00 to 2.00.

**Worked example 6.2 — Preparing a buffer:** to make a pH 7.40 phosphate buffer (p$K_{a2}$ = 7.21): $\log\frac{[\text{HPO}_4^{2-}]}{[\text{H}_2\text{PO}_4^-]} = 0.19$ → ratio = 1.55.

### Biological buffers
- **Blood** pH is maintained at 7.35–7.45, primarily by the **carbonic acid–bicarbonate** system:
$$\text{CO}_2 + \text{H}_2\text{O}\rightleftharpoons\text{H}_2\text{CO}_3\rightleftharpoons\text{H}^+ + \text{HCO}_3^-$$
With effective p$K_a$ = 6.1 and normal [HCO₃⁻]/[CO₂] ≈ 20:1, pH = 6.1 + log 20 = 7.40. Though 6.1 is far from 7.4, the system is effective because it is **open**: the lungs adjust CO₂ (breathing) and the kidneys adjust HCO₃⁻.
- **Acidosis** (pH < 7.35) and **alkalosis** (> 7.45) can be respiratory (hypoventilation raises CO₂; hyperventilation lowers it) or metabolic (diabetic ketoacidosis; vomiting). pH outside ~6.8–7.8 is life-threatening.
- **Intracellular buffers:** phosphate (H₂PO₄⁻/HPO₄²⁻, p$K_a$ 7.21) and proteins (histidine side chains, p$K_a$ ~6.0).
- **Laboratory buffers:** Tris (p$K_a$ 8.1), HEPES (7.5), phosphate-buffered saline (PBS).

## 7. Acid–Base Titrations

A titration adds a base (or acid) of known concentration to determine the amount of acid (or base). The **equivalence point** is reached when moles of added titrant exactly react with the analyte.

### Strong acid + strong base
E.g. 50.0 mL of 0.100 M HCl with 0.100 M NaOH:
- Initial pH = 1.00.
- Gradual rise; at 49.9 mL, pH ≈ 4.0.
- **Equivalence point (50.0 mL): pH = 7.00** (NaCl solution is neutral).
- Very steep jump around equivalence (pH ~4 → ~10 within ±0.1 mL).
- Beyond: pH approaches that of the titrant (~13).

### Weak acid + strong base
E.g. 50.0 mL of 0.100 M CH₃COOH with 0.100 M NaOH:
- Initial pH = 2.87 (weak acid).
- **Buffer region:** a mixture of CH₃COOH and CH₃COO⁻.
- **Half-equivalence point (25.0 mL): pH = p$K_a$ = 4.76** — a convenient way to measure p$K_a$.
- **Equivalence point (50.0 mL): pH ≈ 8.72** (> 7, because acetate is basic: [CH₃COO⁻] = 0.0500 M, $[\text{OH}^-] = \sqrt{5.6\times10^{-10}\times0.0500} = 5.3\times10^{-6}$, pOH 5.28).
- Smaller pH jump than for a strong acid.

### Weak base + strong acid
Equivalence point pH < 7 (conjugate acid is acidic). Example: NH₃ titrated with HCl gives pH ≈ 5.3 at equivalence for 0.1 M solutions.

### Polyprotic acids
Show multiple equivalence points (e.g. H₃PO₄ shows two clearly; the third is too weak to see in water).

### Indicators
Acid–base indicators are weak acids whose acid (HIn) and base (In⁻) forms have different colors. The color changes over roughly p$K_{\text{In}}$ ± 1. Choose an indicator whose range includes the equivalence-point pH.

| Indicator | pH range | Color change (acid → base) |
|---|---|---|
| Methyl violet | 0.0–1.6 | Yellow → violet |
| Thymol blue (1st) | 1.2–2.8 | Red → yellow |
| Methyl orange | 3.1–4.4 | Red → yellow |
| Bromocresol green | 3.8–5.4 | Yellow → blue |
| Methyl red | 4.4–6.2 | Red → yellow |
| Bromothymol blue | 6.0–7.6 | Yellow → blue |
| Phenol red | 6.8–8.4 | Yellow → red |
| Phenolphthalein | 8.2–10.0 | Colorless → pink |
| Alizarin yellow R | 10.1–12.0 | Yellow → red |

Phenolphthalein suits weak acid–strong base titrations; methyl orange or methyl red suit weak base–strong acid titrations; almost any of the middle indicators works for strong–strong titrations because the jump is so steep. **Red cabbage juice** (anthocyanins) is a natural universal indicator: red in acid, purple near neutral, green to yellow in base. Hydrangea flowers are blue in acidic soils (aluminum is available) and pink in alkaline soils.

## 8. Acids and Bases in the Environment and Industry

- **Acid rain:** SO₂ and NOₓ from burning fossil fuels form H₂SO₄ and HNO₃, lowering rain pH, damaging forests, acidifying lakes, and corroding limestone buildings. Emission controls (scrubbers, catalytic converters) have greatly reduced it in many regions.
- **Ocean acidification:** the oceans absorb ~25–30% of anthropogenic CO₂; surface ocean pH has dropped from about 8.2 to 8.1 since pre-industrial times (a ~30% increase in [H⁺]), reducing carbonate ion availability and threatening shell-forming organisms and coral reefs.
- **Antacids:** Mg(OH)₂, Al(OH)₃, CaCO₃, NaHCO₃ neutralize excess stomach acid. Proton-pump inhibitors (omeprazole) reduce acid secretion.
- **Industrial chemicals:** sulfuric acid is the most produced chemical worldwide (~250+ million tonnes/year), used mainly for phosphate fertilizers. Sodium hydroxide (chlor-alkali process) is used in soap, paper and aluminum processing.
- **Soap making (saponification):** fats + NaOH → glycerol + sodium carboxylate salts (soap).
- **Cooking:** baking soda (NaHCO₃) + acidic ingredients release CO₂ to leaven baked goods; baking powder contains both a base and a solid acid.

## 9. Summary

| Concept | Formula |
|---|---|
| Water autoionization | $K_w = [\text{H}^+][\text{OH}^-] = 1.0\times10^{-14}$ (25 °C) |
| pH | $-\log[\text{H}_3\text{O}^+]$; pH + pOH = 14 |
| Acid constant | $K_a = [\text{H}^+][\text{A}^-]/[\text{HA}]$ |
| Weak acid shortcut | $[\text{H}^+] \approx\sqrt{K_aC}$ |
| Conjugate pair | $K_aK_b = K_w$ |
| Henderson–Hasselbalch | pH = p$K_a$ + log([A⁻]/[HA]) |
| Half-equivalence | pH = p$K_a$ |
| Indicator range | p$K_{\text{In}}$ ± 1 |
