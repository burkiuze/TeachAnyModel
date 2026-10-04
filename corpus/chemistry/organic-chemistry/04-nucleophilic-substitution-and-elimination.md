---
title: Nucleophilic Substitution and Elimination - SN1, SN2, E1 and E2
field: Chemistry
subfield: Organic Chemistry
level: undergraduate
keywords: [alkyl halides, nucleophilic substitution, SN2, SN1, Walden inversion, backside attack, steric hindrance, carbocation, racemization, leaving group, nucleophilicity, solvent effects, polar protic, polar aprotic, elimination, E2, E1, anti-periplanar, Zaitsev's rule, Hofmann product, bulky base, competition between substitution and elimination, E1cB, alcohols as substrates, tosylates]
---

# Nucleophilic Substitution and Elimination: SN1, SN2, E1 and E2

Alkyl halides (haloalkanes) and related compounds with good leaving groups undergo two fundamental reaction types: **substitution**, in which a nucleophile replaces the leaving group, and **elimination**, in which a proton and the leaving group are removed to form an alkene. The four mechanisms — SN2, SN1, E2, E1 — form the conceptual core of organic reactivity. Predicting which one dominates requires weighing the substrate, the nucleophile/base, the leaving group, the solvent and the temperature.

## 1. Alkyl Halides

The C–X bond is polar (C δ⁺, X δ⁻), making the carbon **electrophilic**. Bond strength decreases down the group: C–F (485 kJ/mol) > C–Cl (339) > C–Br (285) > C–I (218); bond length increases.

Uses and significance: solvents (dichloromethane, chloroform), anesthetics (halothane, sevoflurane), refrigerants (CFCs, now replaced by HFCs and HFOs because of ozone depletion and global warming), Teflon (from tetrafluoroethylene), PVC, pesticides (DDT — effective but persistent and bioaccumulating), flame retardants, and countless synthetic intermediates. Many halogenated natural products come from marine organisms.

### General reactions
**Substitution:** $\text{Nu}^- + \text{R–LG}\to\text{R–Nu} + \text{LG}^-$
**Elimination:** $\text{B}^- + \text{H–C–C–LG}\to\text{B–H} + \text{C=C} + \text{LG}^-$

## 2. The SN2 Mechanism

**S**ubstitution, **N**ucleophilic, **2** = bimolecular (rate depends on two species).

### Mechanism
A single, **concerted** step: the nucleophile attacks the carbon from the side **opposite** the leaving group (**backside attack**), as the C–LG bond breaks.
$$\text{HO}^- + \text{CH}_3\text{–Br}\to[\text{HO}\cdots\text{CH}_3\cdots\text{Br}]^{\ddagger-}\to\text{HO–CH}_3 + \text{Br}^-$$
In the transition state, the carbon is pentacoordinate (trigonal bipyramidal), with partial bonds to both the nucleophile and the leaving group, and the three other substituents planar.

### Kinetics
$$\text{rate} = k[\text{R–LG}][\text{Nu}^-]$$
Second order overall: doubling either concentration doubles the rate.

### Stereochemistry: inversion of configuration
Backside attack flips the three substituents like an umbrella in the wind — **Walden inversion** (Paul Walden, 1896). An (*R*) substrate gives an (*S*) product (if the priorities of Nu and LG are comparable).
Example: (*S*)-2-bromobutane + OH⁻ → (*R*)-2-butanol.
Hughes and Ingold (1935) proved inversion using radioactive iodide exchange with optically active 2-iodooctane: the rate of racemization was exactly twice the rate of isotopic exchange — each substitution inverts one molecule.

### Substrate effects: steric hindrance
SN2 is very sensitive to crowding around the electrophilic carbon:
$$\text{methyl} > \text{primary} > \text{secondary} \gg \text{tertiary (no SN2)}$$
Approximate relative rates: CH₃Br 30 : CH₃CH₂Br 1 : (CH₃)₂CHBr 0.02 : (CH₃)₃CBr ~0. **Neopentyl** halides ((CH₃)₃CCH₂X), though primary, are extremely slow (~10⁻⁵) because of β-branching. Vinyl and aryl halides do not undergo SN2 (backside blocked; stronger sp² C–X bonds).

**Allylic and benzylic** halides react especially fast by SN2 (the π system stabilizes the transition state).

## 3. The SN1 Mechanism

**S**ubstitution, **N**ucleophilic, **1** = unimolecular.

### Mechanism (stepwise)
1. **Ionization (slow, rate-determining):** the leaving group departs, forming a **carbocation**:
   $(\text{CH}_3)_3\text{C–Br}\to(\text{CH}_3)_3\text{C}^+ + \text{Br}^-$
2. **Nucleophilic attack (fast):** the nucleophile attacks the planar carbocation:
   $(\text{CH}_3)_3\text{C}^+ + \text{H}_2\text{O}\to(\text{CH}_3)_3\text{C–OH}_2^+$
3. (If the nucleophile is neutral) **deprotonation**: $(\text{CH}_3)_3\text{C–OH}_2^+ + \text{H}_2\text{O}\to(\text{CH}_3)_3\text{COH} + \text{H}_3\text{O}^+$

When the solvent is the nucleophile, it is called **solvolysis** (hydrolysis in water, alcoholysis in alcohols).

### Kinetics
$$\text{rate} = k[\text{R–LG}]$$
First order — independent of nucleophile concentration and identity.

### Stereochemistry: racemization (mostly)
The sp², planar carbocation can be attacked from either face, giving a mixture of retention and inversion. In practice, there is often slight excess inversion because the departing leaving group partially shields the front face (ion pairs).

### Substrate effects: carbocation stability
$$\text{tertiary} > \text{secondary} \gg \text{primary} \approx \text{methyl (no SN1)}$$
Also favored: allylic, benzylic (resonance), and substrates with adjacent lone-pair donors (α-alkoxy halides). Approximate relative solvolysis rates in aqueous formic acid: CH₃Br 1, CH₃CH₂Br 2, (CH₃)₂CHBr 43, (CH₃)₃CBr ~10⁸.

### Carbocation rearrangements
Because a carbocation intermediate forms, **1,2-hydride and 1,2-alkyl shifts** can occur to give more stable cations, leading to rearranged products. Rearrangement is diagnostic of SN1/E1 pathways. Example: 3-methyl-2-butyl bromide in ethanol gives mainly 2-ethoxy-2-methylbutane via a hydride shift.

## 4. The Leaving Group

Good leaving groups are **weak bases** — stable as anions (conjugate bases of strong acids). Leaving group ability parallels the acidity of the conjugate acid.

| Leaving group | Conjugate acid pKa | Quality |
|---|---|---|
| TfO⁻ (triflate, CF₃SO₃⁻) | ~−14 | Excellent ("super" leaving group) |
| I⁻ | −10 | Excellent |
| Br⁻ | −9 | Very good |
| TsO⁻ (tosylate), MsO⁻ (mesylate) | ~−2 to −3 | Very good |
| H₂O (from protonated alcohols, ROH₂⁺) | −1.7 | Good |
| Cl⁻ | −7 | Good (C–Cl bond stronger than C–Br) |
| F⁻ | 3.2 | Poor (very strong C–F bond) |
| HO⁻, RO⁻ | 15.7–18 | Very poor |
| H₂N⁻, H⁻, R⁻ | 35–50 | Never leave |

**Converting alcohols into good substrates:** –OH is a poor leaving group. Options:
- **Protonation** with strong acid (HBr, HI): ROH + HBr → RBr + H₂O (SN1 for 3°, SN2 for 1°).
- **Sulfonate esters:** ROH + TsCl/pyridine → ROTs (retention at carbon, since the C–O bond is not broken); the tosylate then undergoes SN2 with inversion.
- **SOCl₂** (→ RCl) and **PBr₃** (→ RBr) for primary and secondary alcohols, typically with inversion (SN2).
- **Mitsunobu reaction** (DEAD, PPh₃, acidic nucleophile): substitution with clean inversion.

## 5. The Nucleophile

**Nucleophilicity** (a kinetic property: how fast a species attacks an electrophile) correlates with, but is not identical to, **basicity** (a thermodynamic property: affinity for H⁺).

Trends:
1. **Charge:** an anion is more nucleophilic than its conjugate acid (HO⁻ > H₂O; RS⁻ > RSH; NH₂⁻ > NH₃).
2. **Across a row:** nucleophilicity parallels basicity: NH₂⁻ > HO⁻ > F⁻; R₃N > R₂O.
3. **Down a column:** depends on solvent.
   - In **polar protic** solvents (water, alcohols), small anions are strongly solvated by hydrogen bonding, which hinders them: **I⁻ > Br⁻ > Cl⁻ > F⁻**; also HS⁻ > HO⁻. Larger, more **polarizable** atoms are better nucleophiles here.
   - In **polar aprotic** solvents, the order follows basicity: F⁻ > Cl⁻ > Br⁻ > I⁻.
4. **Sterics:** bulky species are poor nucleophiles but can still be strong bases: tert-butoxide ((CH₃)₃CO⁻) and LDA are strong, hindered bases.

Approximate nucleophilicity in methanol (toward CH₃I): RS⁻ ≈ I⁻ > CN⁻ > N₃⁻ > Br⁻ > HO⁻ ≈ RO⁻ > Cl⁻ > NH₃ > CH₃COO⁻ > F⁻ > H₂O > CH₃OH.

## 6. Solvent Effects

| Solvent type | Examples | Effect |
|---|---|---|
| **Polar protic** (O–H or N–H bonds) | Water, methanol, ethanol, acetic acid, formic acid | Stabilize carbocations and leaving-group anions (hydrogen bonding) → **favor SN1/E1**. Solvate and weaken anionic nucleophiles → slow SN2. |
| **Polar aprotic** (polar, no O–H/N–H) | DMSO, DMF, acetone, acetonitrile, HMPA | Solvate cations well but leave anions "naked" and reactive → **greatly accelerate SN2** (often by 10³–10⁶). |
| **Nonpolar** | Hexane, benzene | Poor solvents for ionic reagents; rarely used for these reactions. |

Example: CH₃I + Cl⁻ is about a million times faster in DMF than in methanol.

## 7. Elimination: The E2 Mechanism

**E**limination, bimolecular. A strong base removes a β-hydrogen at the same time as the leaving group departs and the π bond forms — one concerted step.
$$\text{B}^- + \text{H–C}_\beta\text{–C}_\alpha\text{–X}\to\text{B–H} + \text{C=C} + \text{X}^-$$
$$\text{rate} = k[\text{R–X}][\text{B}^-]$$

### Stereochemistry: anti-periplanar requirement
The C–H and C–LG bonds must be **anti-periplanar** (dihedral angle 180°, in the same plane on opposite sides) for optimal orbital overlap: the C–H σ bond donates into the C–LG σ* orbital.
- In **cyclohexanes**, both H and LG must be **axial** (trans-diaxial). This can dramatically affect rates: in menthyl chloride, the chlorine must go axial (forcing the other groups axial), so E2 is slow and gives only the less substituted alkene; neomenthyl chloride reacts ~200 times faster and gives mostly the more substituted alkene.
- E2 is **stereospecific**: the configuration of the substrate determines the alkene geometry. For example, (1*R*,2*R*)- and (1*R*,2*S*)-1,2-diphenyl-1-bromopropane give different (*E*/*Z*) alkenes.

### Regiochemistry: Zaitsev vs. Hofmann
- **Zaitsev's rule** (Alexander Zaitsev, 1875): with small bases (EtO⁻, HO⁻, MeO⁻), the **more substituted** (more stable) alkene predominates. 2-Bromobutane + NaOEt → but-2-ene (~80%, mostly *trans*) + but-1-ene (~20%).
- **Hofmann product:** with **bulky bases** (potassium tert-butoxide, LDA, DBU in some cases) or poor leaving groups such as –NR₃⁺ (Hofmann elimination of quaternary ammonium hydroxides) and F⁻, the **less substituted** alkene predominates, because the base removes the more accessible β-hydrogen. 2-Bromo-2-methylbutane + KOtBu → mostly 2-methylbut-1-ene.
- When there is a choice of β-hydrogens, E2 typically gives the *E* (trans) alkene preferentially.

## 8. Elimination: The E1 Mechanism

**E**limination, unimolecular. Stepwise:
1. Ionization to a carbocation (slow, rate-determining — the same first step as SN1).
2. A weak base (often the solvent) removes a β-hydrogen, forming the alkene.
$$\text{rate} = k[\text{R–X}]$$
- Favored for **tertiary** (and secondary) substrates with **weak bases** in **polar protic** solvents, especially at **higher temperatures**.
- Follows **Zaitsev's rule** (most stable alkene).
- **Rearrangements possible.**
- Competes with SN1; heat favors E1 (elimination produces more molecules → higher entropy; $-T\Delta S$ becomes more favorable at high $T$).
- **Acid-catalyzed dehydration of alcohols** (H₂SO₄ or H₃PO₄, heat) proceeds by E1 for secondary and tertiary alcohols (and E2-like for primary): cyclohexanol → cyclohexene. The reaction is driven by distilling off the lower-boiling alkene (Le Chatelier).

### E1cB
**E**limination, **u**nimolecular, via the **c**onjugate **B**ase: when the β-hydrogen is acidic (adjacent to a carbonyl) and the leaving group is poor (e.g. –OH), a carbanion (enolate) forms first, then expels the leaving group. Important in the dehydration step of aldol condensations and in some biochemical pathways (e.g. enolase-type reactions).

## 9. Predicting the Mechanism

### Step 1: Classify the substrate

| Substrate | SN2 | SN1 | E2 | E1 |
|---|---|---|---|---|
| Methyl (CH₃X) | ✓✓ | ✗ | ✗ (no β-H) | ✗ |
| Primary (RCH₂X) | ✓✓ (most) | ✗ | ✓ with bulky strong base | ✗ |
| Secondary (R₂CHX) | ✓ (good Nu, aprotic) | ✓ (weak Nu, protic) | ✓✓ (strong base) | ✓ (weak base, heat) |
| Tertiary (R₃CX) | ✗ | ✓✓ (weak Nu/base) | ✓✓ (strong base) | ✓ (weak base, heat) |
| Allylic/benzylic 1° or 2° | ✓✓ | ✓✓ | ✓ | ✓ |
| Vinyl/aryl | ✗ | ✗ | (special conditions) | ✗ |

### Step 2: Classify the reagent
- **Strong nucleophile, weak base:** I⁻, Br⁻, Cl⁻, RS⁻, HS⁻, CN⁻, N₃⁻, RCOO⁻ (moderate), NH₃, R₃N → substitution (SN2).
- **Strong nucleophile, strong base:** HO⁻, CH₃O⁻, CH₃CH₂O⁻ → SN2 with methyl/1°; E2 with 2° and 3°.
- **Strong, bulky base (poor nucleophile):** (CH₃)₃CO⁻, LDA, DBU, DBN → E2 (Hofmann with appropriate substrates).
- **Weak nucleophile, weak base:** H₂O, ROH, RCOOH → SN1/E1 (3° and 2°), very slow or no reaction with 1°.
- **Strong base, poor nucleophile (hydride):** NaH → deprotonation.

### Step 3: Consider solvent and temperature
- Polar aprotic → SN2. Polar protic → SN1/E1.
- Higher temperature → elimination over substitution.

### Worked examples
| Substrate + reagent | Major pathway and product |
|---|---|
| CH₃CH₂CH₂Br + NaCN in DMSO | SN2 → CH₃CH₂CH₂CN (butanenitrile) |
| CH₃CH₂CH₂Br + KOtBu | E2 → CH₃CH=CH₂ (propene) |
| (CH₃)₂CHBr + NaOEt in EtOH | E2 major (propene ~80%), SN2 minor (ethyl isopropyl ether) |
| (CH₃)₂CHBr + NaI in acetone | SN2 → 2-iodopropane (NaBr precipitates — the Finkelstein reaction) |
| (CH₃)₃CBr + H₂O, 25 °C | SN1 → (CH₃)₃COH (major) + some E1 → (CH₃)₂C=CH₂ |
| (CH₃)₃CBr + NaOEt in EtOH | E2 → (CH₃)₂C=CH₂ |
| (CH₃)₃CBr + CH₃OH, heat | SN1/E1 mixture; heat favors E1 |
| (*R*)-2-bromooctane + NaSH in DMF | SN2 with inversion → (*S*)-octane-2-thiol |
| Cyclohexanol + H₂SO₄, heat | E1 dehydration → cyclohexene |
| CH₃CH₂OH + HBr | SN2 → CH₃CH₂Br |

### Comparison table

| Feature | SN2 | SN1 | E2 | E1 |
|---|---|---|---|---|
| Steps | 1 (concerted) | 2+ (carbocation) | 1 (concerted) | 2 (carbocation) |
| Rate law | $k$[RX][Nu] | $k$[RX] | $k$[RX][B] | $k$[RX] |
| Substrate preference | Me > 1° > 2° | 3° > 2° | 3° > 2° > 1° | 3° > 2° |
| Reagent | Good nucleophile | Weak nucleophile | Strong base | Weak base |
| Solvent | Polar aprotic | Polar protic | Varies (often the base's conjugate acid) | Polar protic |
| Stereochemistry | Inversion | Racemization (partial) | Anti-periplanar; stereospecific | Mixture (more stable alkene) |
| Rearrangements | No | Possible | No | Possible |
| Regiochemistry | — | — | Zaitsev (small base) / Hofmann (bulky) | Zaitsev |

## 10. Applications

- **Williamson ether synthesis:** alkoxide + primary alkyl halide (SN2) → ether: CH₃CH₂O⁻Na⁺ + CH₃I → CH₃CH₂OCH₃. Choose the combination with the less hindered alkyl halide (tertiary alkoxide + methyl halide works; methoxide + tertiary halide gives elimination).
- **Biological methylation:** S-adenosylmethionine (SAM) transfers methyl groups by SN2 to DNA, proteins and neurotransmitters (e.g. norepinephrine → epinephrine).
- **Alkylating anticancer drugs** (nitrogen mustards like cyclophosphamide, and cisplatin's related chemistry) attack DNA bases; nitrogen mustards form aziridinium ions by intramolecular SN2, which then alkylate guanine N7. The same chemistry makes sulfur mustard a chemical weapon.
- **Synthesis of amines, nitriles, azides, thiols, ethers** from alkyl halides; **Finkelstein** halide exchange; **Gabriel synthesis** of primary amines.
- **Dehydrohalogenation** with strong base produces alkenes; double dehydrohalogenation of vicinal or geminal dihalides with NaNH₂ produces alkynes.
- **Industrial dehydration:** ethanol → ethylene over alumina (bio-ethylene).

## 11. Summary

**Decision flowchart (simplified):**
1. Is the substrate methyl or primary? → SN2 (unless a bulky strong base is used → E2).
2. Is it tertiary? → Strong base: E2. Weak nucleophile/base: SN1 + E1 (heat → E1).
3. Is it secondary? → Strong base/nucleophile like RO⁻, HO⁻: E2 mostly. Good nucleophile that is a weak base (I⁻, RS⁻, CN⁻, N₃⁻) in aprotic solvent: SN2. Weak nucleophile in protic solvent: SN1/E1.

**Key principles:**
- Good leaving groups are weak bases.
- Steric hindrance kills SN2; carbocation stability drives SN1/E1.
- Polar aprotic solvents accelerate SN2; polar protic solvents favor ionization.
- Heat and strong, bulky bases favor elimination.
- SN2 inverts; SN1 racemizes; E2 requires anti-periplanar geometry.
