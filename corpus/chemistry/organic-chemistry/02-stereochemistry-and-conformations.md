---
title: Stereochemistry and Conformational Analysis
field: Chemistry
subfield: Organic Chemistry
level: undergraduate
keywords: [stereochemistry, stereoisomers, chirality, stereocenter, enantiomers, diastereomers, meso compounds, racemic mixture, optical activity, specific rotation, enantiomeric excess, Cahn-Ingold-Prelog rules, R and S configuration, E and Z, cis-trans isomerism, Fischer projection, conformations, Newman projection, staggered, eclipsed, gauche, anti, cyclohexane chair, axial, equatorial, A-values, ring strain, thalidomide, resolution, asymmetric synthesis]
---

# Stereochemistry and Conformational Analysis

**Stereochemistry** is the study of the three-dimensional arrangement of atoms in molecules and its consequences. Two molecules can have identical connectivity yet behave completely differently in biological systems because one is the mirror image of the other — like left and right hands. Stereochemistry is central to drug design, enzyme catalysis, the senses of taste and smell, and the synthesis of complex natural products.

## 1. Classification of Isomers

```
Isomers (same molecular formula)
├── Constitutional isomers (different connectivity)
└── Stereoisomers (same connectivity, different 3D arrangement)
    ├── Enantiomers (non-superimposable mirror images)
    └── Diastereomers (stereoisomers that are not mirror images)
        ├── cis/trans (E/Z) isomers
        └── Compounds with ≥2 stereocenters differing at some (not all) centers
```

**Conformers** (conformational isomers) interconvert by rotation about single bonds and are usually not separable at room temperature; **configurational** stereoisomers require breaking bonds to interconvert.

## 2. Chirality

An object is **chiral** (from Greek *cheir*, "hand") if it is **not superimposable on its mirror image**. Hands, feet, screws, spiral staircases and most biological molecules are chiral. An **achiral** object is superimposable on its mirror image (a sphere, a cup, a methane molecule).

**Symmetry test:** a molecule with a **plane of symmetry** (mirror plane) or a center of inversion is achiral. (Strictly, a molecule is chiral if and only if it lacks any improper rotation axis $S_n$.)

### Stereocenters (chiral centers)
The most common source of chirality is a carbon atom bonded to **four different groups** — a **stereocenter** (asymmetric carbon, stereogenic center), often marked with an asterisk (C*).

Examples:
- **2-Butanol**, CH₃CH(OH)CH₂CH₃: C2 bears H, OH, CH₃ and C₂H₅ → chiral.
- **Lactic acid**, CH₃CH(OH)COOH: chiral; (*S*)-lactic acid forms in muscles; (*R*) and (*S*) are both produced by bacteria.
- **Alanine** and all amino acids except glycine (which has two H atoms on its α-carbon).
- 2-Propanol, CH₃CH(OH)CH₃: C2 has two identical CH₃ groups → achiral.

A molecule with $n$ stereocenters has **at most $2^n$ stereoisomers** (fewer if meso forms exist). Cholesterol has 8 stereocenters (256 possible stereoisomers), yet nature makes only one.

Other sources of chirality: chiral nitrogen or phosphorus (when inversion is slow, e.g. phosphines, quaternary ammonium salts), **axial chirality** (allenes, atropisomeric biaryls like BINAP), **planar chirality** and **helicity** (helicenes, the DNA double helix).

## 3. Enantiomers

**Enantiomers** are pairs of non-superimposable mirror-image molecules.

### Properties
- **Identical physical properties** in an achiral environment: same melting point, boiling point, density, solubility, NMR and IR spectra.
- **Opposite optical rotation:** they rotate plane-polarized light by equal amounts in opposite directions.
- **Different behavior in chiral environments:** they react at different rates with other chiral molecules, interact differently with enzymes and receptors, and can taste, smell or act differently as drugs.

| Compound | Enantiomer A | Enantiomer B |
|---|---|---|
| Carvone | (*R*)-(−): spearmint | (*S*)-(+): caraway, dill |
| Limonene | (*R*)-(+): orange | (*S*)-(−): piney/lemony (turpentine-like) |
| Ibuprofen | (*S*): active anti-inflammatory | (*R*): inactive (converted to *S* in the body) |
| Thalidomide | (*R*): sedative | (*S*): teratogenic (but racemizes in vivo) |
| Ethambutol | (*S,S*): treats tuberculosis | (*R,R*): can cause blindness |
| Naproxen | (*S*): anti-inflammatory | (*R*): liver toxin |
| Methamphetamine | (*S*): potent CNS stimulant | (*R*): weak; used in nasal decongestant |
| Asparagine | (*S*): bitter | (*R*): sweet |
| Penicillamine | (*S*): treats Wilson's disease, arthritis | (*R*): toxic |

**The thalidomide tragedy (1957–1962):** marketed as a racemic sedative for morning sickness, it caused severe birth defects in over 10 000 children. Because the enantiomers interconvert in the body, even pure (*R*)-thalidomide would not have been safe. The tragedy transformed drug regulation (including requirements to study individual enantiomers). Today thalidomide is used, under strict controls, to treat multiple myeloma and leprosy complications.

Today, over half of new small-molecule drugs are single enantiomers ("chiral switches", e.g. esomeprazole from omeprazole; escitalopram from citalopram).

### Optical activity
Plane-polarized light passed through a solution of one enantiomer is rotated. Measured with a **polarimeter**.
- **Dextrorotatory** (+, *d*): clockwise rotation (as viewed facing the light source).
- **Levorotatory** (−, *l*): counterclockwise.

**Specific rotation:**
$$[\alpha]_\lambda^T = \frac{\alpha_{\text{observed}}}{l\cdot c}$$
with $l$ in decimeters and $c$ in g/mL (usually measured at the sodium D line, 589 nm, and 20 or 25 °C).
Examples: sucrose +66.5°; (*S*)-alanine about +14.5° (in 6 M HCl; only about +2° in water — rotation depends strongly on solvent and pH); (*R*)-carvone −61°; cholesterol −31.5°.

**Important:** the sign of rotation (+/−) has **no simple relationship** to the *R*/*S* configuration — it must be measured. (*S*)-lactic acid is (+) but its sodium salt is (−).

### Racemic mixtures and enantiomeric excess
A **racemic mixture** (racemate) contains equal amounts of both enantiomers, labeled (±) or *rac*; it is optically inactive because rotations cancel. Reactions that create a stereocenter from achiral starting materials without chiral influence give racemates.

**Enantiomeric excess:**
$$ee = \frac{|[R] - [S]|}{[R] + [S]}\times100\% = \frac{[\alpha]_{\text{observed}}}{[\alpha]_{\text{pure}}}\times100\%\;(\text{optical purity, approximately})$$
A mixture of 90% *R* and 10% *S* has 80% *ee*.

**Louis Pasteur (1848)** discovered molecular chirality by hand-separating mirror-image crystals of sodium ammonium tartrate with tweezers under a microscope — the first **resolution** of a racemate. Modern resolution methods: forming **diastereomeric salts** with a pure chiral acid or base (separable by crystallization), chiral chromatography, and enzymatic (kinetic) resolution.

## 4. Assigning Configuration: The Cahn–Ingold–Prelog (CIP) Rules

To name stereocenters unambiguously as **R** (Latin *rectus*, right) or **S** (*sinister*, left):

### Step 1: Assign priorities to the four groups
1. **Higher atomic number** of the directly attached atom gets higher priority: I > Br > Cl > S > F > O > N > C > H (and heavier isotopes above lighter: D > H).
2. **Ties:** move outward to the next set of atoms and compare them, highest first, at the first point of difference. Example: –CH₂OH (O,H,H) > –CH(CH₃)₂ (C,C,H) > –CH₂CH₃ (C,H,H) > –CH₃ (H,H,H).
3. **Multiple bonds** are treated as duplicated (or triplicated) single bonds: –CH=O counts as C(O,O,H); –C≡N as C(N,N,N); –CH=CH₂ as C(C,C,H).

### Step 2: Orient the molecule
Point the **lowest-priority group (4) away** from the viewer.

### Step 3: Trace 1 → 2 → 3
- **Clockwise → R**
- **Counterclockwise → S**

**Shortcut:** if the lowest-priority group points **toward** you (on a wedge), determine the direction and **reverse** the answer. Swapping any two groups inverts the configuration.

**Worked example 4.1 — (*R*)-2-butanol:** priorities: –OH (1), –CH₂CH₃ (2), –CH₃ (3), –H (4). With H in back, if OH → C₂H₅ → CH₃ runs clockwise, the configuration is *R*.

**Worked example 4.2 — Glyceraldehyde,** HOCH₂–CH(OH)–CHO: priorities –OH > –CHO [C(O,O,H)] > –CH₂OH [C(O,H,H)] > –H. Natural D-glyceraldehyde is (*R*)-(+).

### Fischer projections
A stereocenter drawn as a cross: **horizontal** lines point **toward** the viewer; **vertical** lines point **away**. Used extensively for sugars and amino acids.
- With the lowest-priority group on a vertical line: read 1→2→3 directly.
- With it on a horizontal line: reverse the result.
- Rotating a Fischer projection by 180° in the plane is allowed; rotating by 90° or swapping two groups inverts the configuration.

### D/L nomenclature (older, still used in biochemistry)
Based on comparison with glyceraldehyde in Fischer projection: **D** if the stereocenter farthest from the carbonyl has its –OH (or –NH₂) on the **right**; **L** if on the left. Natural sugars are mostly **D** (D-glucose, D-fructose, D-ribose); natural amino acids are **L** (all L-amino acids are *S* except L-cysteine, which is *R* because of sulfur's high priority). D/L does not correlate with (+)/(−) either: D-fructose is levorotatory.

## 5. Diastereomers and Meso Compounds

### Molecules with two stereocenters
Up to four stereoisomers: (*R,R*), (*S,S*), (*R,S*), (*S,R*).
- (*R,R*) and (*S,S*) are enantiomers; (*R,S*) and (*S,R*) are enantiomers.
- (*R,R*) and (*R,S*) are **diastereomers**.

**Diastereomers have different physical properties** (melting points, boiling points, solubilities, spectra, reactivities) and can be separated by ordinary methods (crystallization, distillation, chromatography).

**Example — 2,3-dihydroxybutanoic acid** or **threonine** (2 stereocenters, 4 stereoisomers: L-threonine is (2*S*,3*R*); L-allothreonine is (2*S*,3*S*)).

**Epimers:** diastereomers differing at only one stereocenter (D-glucose and D-galactose are C4 epimers; D-glucose and D-mannose are C2 epimers). **Anomers** are epimers at the anomeric carbon of cyclic sugars (α and β).

### Meso compounds
A **meso compound** has stereocenters but is **achiral** because it has an internal plane of symmetry. It is superimposable on its mirror image and optically inactive.

**Tartaric acid** (HOOC–CH(OH)–CH(OH)–COOH) has only **three** stereoisomers, not four:
- (*R,R*)-(+)-tartaric acid (natural, from grapes; mp 170 °C; [α] = +12°)
- (*S,S*)-(−)-tartaric acid (mp 170 °C; [α] = −12°)
- *meso*-tartaric acid (*R,S* ≡ *S,R*; mp 146 °C; [α] = 0°) — a diastereomer of the other two.

*cis*-1,2-Dimethylcyclohexane is also meso; the *trans* isomer is chiral (a pair of enantiomers).

## 6. Cis–Trans and E/Z Isomerism

Rotation about a C=C double bond is restricted (breaking the π bond requires ~260 kJ/mol), so substituents are fixed on one side or the other.

**Cis/trans:** used when each carbon has one H (or two identical groups compared): *cis* = same side; *trans* = opposite sides.
- *cis*-But-2-ene (bp 3.7 °C) and *trans*-but-2-ene (bp 0.9 °C) are diastereomers with different properties.
- **Maleic acid** (*cis*, mp 135 °C, forms an anhydride on heating) vs. **fumaric acid** (*trans*, mp 287 °C, a metabolic intermediate in the citric acid cycle).
- **Trans fats:** partial hydrogenation of vegetable oils isomerizes some natural *cis* double bonds to *trans*; trans fats raise LDL cholesterol and increase heart disease risk, and have been banned or restricted in many countries.
- **Vision:** absorption of a photon converts 11-*cis*-retinal to all-*trans*-retinal in rhodopsin, triggering the nerve signal — the primary event of vision, occurring in ~200 femtoseconds.

**E/Z system** (general, using CIP priorities): on each alkene carbon, determine the higher-priority group.
- **Z** (German *zusammen*, "together"): higher-priority groups on the **same** side.
- **E** (*entgegen*, "opposite"): on **opposite** sides.
Example: (*E*)-1-bromo-1-chloropropene? On C1: Br > Cl; on C2: CH₃ > H. If Br and CH₃ are on opposite sides → *E*.

Note that *cis* does not always equal *Z*. **Cis/trans isomerism also occurs in rings**: *cis*-1,2-dimethylcyclopropane (both methyls on the same face) vs. *trans*.

## 7. Conformational Analysis of Acyclic Molecules

Rotation about C–C single bonds is fast at room temperature, but not all orientations (conformations) have equal energy.

### Ethane
Viewed in a **Newman projection** (looking down the C–C bond: the front carbon is a point, the back carbon a circle):
- **Staggered:** H atoms on the front carbon bisect those on the back — lowest energy.
- **Eclipsed:** H atoms aligned — highest energy, **12 kJ/mol** higher (each H/H eclipsing costs ~4 kJ/mol). This **torsional strain** arises mostly from destabilizing interactions between bonding orbitals and from loss of stabilizing hyperconjugation (σ C–H → σ* C–H) present in the staggered form.
- The barrier is small: rotation occurs ~$10^{11}$ times per second at room temperature.

### Butane (rotation about C2–C3)

| Conformation | Dihedral angle (CH₃–C–C–CH₃) | Relative energy (kJ/mol) |
|---|---|---|
| Anti (staggered) | 180° | 0 (most stable) |
| Gauche (staggered) | ±60° | 3.8 (steric strain between CH₃ groups) |
| Eclipsed (CH₃/H) | ±120° | 16 |
| Fully eclipsed (CH₃/CH₃, syn-periplanar) | 0° | ~19 (highest) |

At room temperature butane is ~70% anti, ~30% gauche. Long alkane chains prefer zigzag all-anti conformations in crystals (as in polyethylene and lipid tails in cell membranes).

**Types of strain:** torsional (eclipsing), steric (van der Waals repulsion between nearby atoms), and angle strain (deviation from ideal bond angles).

## 8. Cycloalkanes and Ring Strain

Adolf von Baeyer (1885) proposed that rings deviate from the tetrahedral angle, creating **angle strain**. Measured strain energies (from heats of combustion per CH₂ compared with an unstrained chain):

| Ring | Total strain (kJ/mol) | Notes |
|---|---|---|
| Cyclopropane | 115 | Planar; 60° C–C–C angles; bent "banana" bonds; all H eclipsed; reactive |
| Cyclobutane | 110 | Slightly puckered ("butterfly") to relieve eclipsing |
| Cyclopentane | 26 | "Envelope" conformation; mostly torsional strain |
| Cyclohexane | ~0 | Chair conformation: perfect angles, all staggered |
| Cycloheptane | 26 | |
| Cyclooctane | ~40 | Transannular strain |

Cyclopropane's strain explains its reactivity (rings open readily); nevertheless, cyclopropane rings occur in natural products (pyrethrin insecticides) and drugs.

## 9. Cyclohexane Conformations

### The chair conformation
Cyclohexane adopts a puckered **chair** conformation with C–C–C angles of ~111° and all C–H bonds staggered — essentially strain-free. It is the most important conformation in organic chemistry; six-membered rings are everywhere (sugars, steroids, many drugs).

Each carbon has one **axial** bond (parallel to the ring's axis, alternating up and down) and one **equatorial** bond (roughly in the ring's "plane", pointing outward). The six axial hydrogens alternate up/down; so do the equatorial ones.

Other conformations: **boat** (~29 kJ/mol higher; eclipsing and "flagpole" steric clash), **twist-boat** (~23 kJ/mol), and **half-chair** (~45 kJ/mol, the transition state for ring flipping).

### Ring flipping
Cyclohexane interconverts between two chair forms ~$10^5$ times per second at room temperature (barrier ~45 kJ/mol). In a **ring flip**, **all axial positions become equatorial and vice versa** (but "up" stays "up").

### Monosubstituted cyclohexanes
Substituents prefer the **equatorial** position. An axial substituent suffers **1,3-diaxial interactions** — steric clashes with the two axial hydrogens on the same side of the ring (each equivalent to a gauche butane interaction).

**A-values** (free energy preference for equatorial, kJ/mol):

| Substituent | A-value | % equatorial at 25 °C |
|---|---|---|
| –F | 1.0 | ~60% |
| –Cl | 2.0 | ~70% |
| –Br | 2.0 | ~70% |
| –OH | 2.2–3.8 (solvent-dependent) | ~75–80% |
| –CH₃ | 7.3 | 95% |
| –CH₂CH₃ | 7.5 | 95% |
| –CH(CH₃)₂ | 9.0 | 97% |
| –C₆H₅ | 12.6 | 99% |
| –C(CH₃)₃ | ~20 | >99.9% |

The **tert-butyl** group is so large that it effectively "locks" the ring in the conformation where it is equatorial — a useful tool for studying conformational effects on reactivity. (Halogens have small A-values despite their size because the C–X bond is long.)

### Disubstituted cyclohexanes
Analyze each chair form and choose the one with more (or larger) equatorial substituents.

| Isomer | Chair 1 | Chair 2 | Preferred |
|---|---|---|---|
| *trans*-1,2-dimethyl | e,e | a,a | e,e (strongly) |
| *cis*-1,2-dimethyl | a,e | e,a | Equal energies |
| *cis*-1,3-dimethyl | e,e | a,a | e,e (strongly) |
| *trans*-1,3-dimethyl | a,e | e,a | Equal energies |
| *trans*-1,4-dimethyl | e,e | a,a | e,e (strongly) |
| *cis*-1,4-dimethyl | a,e | e,a | Equal energies |

So *trans*-1,2-, *cis*-1,3- and *trans*-1,4-dimethylcyclohexane are more stable than their diastereomers.

**β-D-Glucose** is the most abundant sugar in nature, and in its chair form **every** bulky substituent (four –OH and the –CH₂OH) is equatorial — a likely reason for its prevalence.

### Fused rings
**Decalin** exists as *cis* and *trans* isomers; *trans*-decalin is rigid (cannot ring-flip) and more stable. **Steroids** (cholesterol, testosterone, estradiol, cortisol) consist of three fused six-membered rings and one five-membered ring with predominantly *trans* ring fusions, giving rigid, flat shapes important for receptor binding.

## 10. Stereochemistry of Reactions

- **Stereospecific reactions:** different stereoisomers of the starting material give different stereoisomers of the product. SN2 proceeds with **inversion of configuration** (Walden inversion); E2 requires an **anti-periplanar** arrangement; bromine adds **anti** to alkenes; syn-dihydroxylation with OsO₄ adds both OH groups to the same face.
- **Stereoselective reactions:** one stereoisomer forms preferentially among several possible products (e.g. E2 often favors the *E*-alkene).
- **Racemization:** SN1 reactions via planar carbocations, or reactions via planar enols/enolates, typically scramble stereocenters.
- **Asymmetric synthesis:** making one enantiomer selectively using chiral catalysts, auxiliaries or reagents. Landmarks: Knowles' rhodium-catalyzed asymmetric hydrogenation (used to make L-DOPA for Parkinson's disease), Noyori hydrogenation, Sharpless asymmetric epoxidation and dihydroxylation (Nobel 2001); organocatalysis (List and MacMillan, Nobel 2021). Enzymes are nature's perfectly enantioselective catalysts.
- **Prochirality:** a molecule that becomes chiral by a single change; faces of planar trigonal groups are labeled *Re* and *Si*. Enzymes distinguish prochiral groups — e.g. aconitase in the citric acid cycle acts on citrate (an achiral molecule) in a completely stereospecific way, as Alexander Ogston pointed out in 1948 ("three-point attachment").

### Homochirality of life
Living organisms use almost exclusively L-amino acids and D-sugars. The origin of this **homochirality** is an open question; proposals include circularly polarized light in space, chiral mineral surfaces, autocatalytic amplification (the Soai reaction), and parity violation in the weak force (a tiny energy difference between enantiomers). Meteorites such as Murchison contain small L-excesses of some amino acids.

## 11. Summary

| Term | Definition |
|---|---|
| Chiral | Non-superimposable on mirror image |
| Stereocenter | Carbon with four different groups |
| Enantiomers | Non-superimposable mirror images; identical properties except toward chiral things and polarized light |
| Diastereomers | Stereoisomers that are not mirror images; different properties |
| Meso | Has stereocenters but achiral (internal mirror plane) |
| Racemate | 50:50 enantiomers; optically inactive |
| R/S | CIP priorities; lowest priority back; clockwise = R |
| E/Z | Higher priorities same side = Z, opposite = E |
| Max stereoisomers | $2^n$ for $n$ stereocenters |
| Specific rotation | $[\alpha] = \alpha/(l\cdot c)$ |
| Butane | Anti < gauche (3.8) < eclipsed (16) < fully eclipsed (19 kJ/mol) |
| Cyclohexane | Chair; substituents prefer equatorial |
