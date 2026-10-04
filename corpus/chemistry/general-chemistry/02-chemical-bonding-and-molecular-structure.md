---
title: Chemical Bonding and Molecular Structure
field: Chemistry
subfield: General Chemistry
level: high-school to undergraduate
keywords: [chemical bond, ionic bond, lattice energy, Born-Haber cycle, covalent bond, Lewis structures, octet rule, formal charge, resonance, bond order, bond energy, bond polarity, dipole moment, VSEPR theory, molecular geometry, hybridization, sigma bond, pi bond, valence bond theory, molecular orbital theory, paramagnetism of oxygen, metallic bonding, intermolecular forces, hydrogen bonding, van der Waals forces]
---

# Chemical Bonding and Molecular Structure

Atoms combine because bonded arrangements have lower energy than separated atoms. Understanding **why** and **how** atoms bond explains the shapes of molecules, the properties of materials, and the course of chemical reactions. All chemical bonding is fundamentally electrostatic, governed by quantum mechanics: electrons are shared or transferred so as to be attracted to more than one nucleus.

## 1. Why Atoms Bond

As two atoms approach, attractions (electrons to the other nucleus) compete with repulsions (electron–electron, nucleus–nucleus). The potential energy curve has a minimum at the **bond length**; the depth of the minimum is the **bond dissociation energy**. Noble gases have filled valence shells and little tendency to bond; other atoms tend to achieve noble-gas configurations by losing, gaining or sharing electrons (the **octet rule** for main-group elements, a useful heuristic).

## 2. Ionic Bonding

When an atom with low ionization energy (a metal) meets an atom with high electron affinity (a nonmetal), electrons transfer, forming cations and anions held together by electrostatic attraction.

$$\text{Na} \to \text{Na}^+ + e^- \;(+496\text{ kJ/mol}), \qquad \text{Cl} + e^- \to \text{Cl}^- \;(-349\text{ kJ/mol})$$
Electron transfer alone is uphill (+147 kJ/mol); the driving force is the large **lattice energy** released when ions pack into a crystal.

### Lattice energy
The energy released when gaseous ions form one mole of an ionic solid (or, as often tabulated, the energy required to separate it). By Coulomb's law, it scales as
$$U \propto \frac{|q_+q_-|}{r_+ + r_-}$$
- Higher charges → much larger lattice energy: MgO (~3800 kJ/mol) vs. NaCl (~787 kJ/mol).
- Smaller ions → larger lattice energy: LiF > NaF > KF.

### Born–Haber cycle (NaCl)
A Hess's law cycle relating lattice energy to measurable quantities:

| Step | ΔH (kJ/mol) |
|---|---|
| Na(s) → Na(g) (sublimation) | +107 |
| ½Cl₂(g) → Cl(g) (half the bond energy) | +122 |
| Na(g) → Na⁺(g) + e⁻ (ionization) | +496 |
| Cl(g) + e⁻ → Cl⁻(g) (electron affinity) | −349 |
| Na⁺(g) + Cl⁻(g) → NaCl(s) (lattice formation) | −787 |
| **Net: Na(s) + ½Cl₂(g) → NaCl(s)** | **−411** |

### Properties of ionic compounds
High melting and boiling points (NaCl melts at 801 °C); hard but brittle (shifting layers brings like charges together, causing cleavage); conduct electricity when molten or dissolved (mobile ions) but not as solids; many dissolve in water.

## 3. Covalent Bonding

Atoms with similar electronegativities **share** electron pairs. The shared electrons are attracted to both nuclei. Gilbert N. Lewis (1916) introduced the electron-pair bond.

### Lewis structures
**Procedure:**
1. Count total valence electrons (add for negative charge, subtract for positive).
2. Choose a skeleton (least electronegative atom usually central; H and F are always terminal).
3. Connect atoms with single bonds (2 electrons each).
4. Complete octets of outer atoms with lone pairs.
5. Place remaining electrons on the central atom.
6. If the central atom lacks an octet, form multiple bonds using lone pairs from outer atoms.
7. Check formal charges.

**Examples:**
- H₂O: 8 valence electrons; O with two O–H bonds and two lone pairs.
- CO₂: 16 electrons; O=C=O with two lone pairs on each O.
- N₂: 10 electrons; :N≡N: (triple bond, one lone pair each).
- NH₄⁺: 8 electrons; four N–H bonds, positive charge.

### Formal charge
$$\text{FC} = (\text{valence electrons}) - (\text{nonbonding electrons}) - \tfrac12(\text{bonding electrons})$$
The best Lewis structure minimizes formal charges and places negative formal charges on more electronegative atoms. The sum equals the overall charge.

### Resonance
When more than one valid Lewis structure exists, the true structure is a **resonance hybrid** — a weighted average, not a rapid flipping between forms.
- **Ozone (O₃):** two equivalent structures; both O–O bonds are identical (128 pm), intermediate between single (148 pm) and double (121 pm).
- **Carbonate (CO₃²⁻):** three equivalent structures; each C–O bond order is 4/3.
- **Benzene (C₆H₆):** two Kekulé structures; all C–C bonds are 139 pm, between single (154 pm) and double (134 pm). Resonance (delocalization) makes benzene unusually stable (aromaticity).

### Exceptions to the octet rule
- **Incomplete octets:** BF₃ (B has 6 electrons), BeCl₂ (gas phase). Such species are Lewis acids.
- **Odd-electron species (radicals):** NO, NO₂, ClO₂, ·OH.
- **Expanded octets** (period 3 and beyond): PCl₅ (10 electrons around P), SF₆ (12), XeF₄. (Modern analyses attribute these to ionic/multicenter bonding rather than d-orbital participation, but the Lewis description remains useful.)

### Bond order, length and energy

| Bond | Bond order | Length (pm) | Energy (kJ/mol) |
|---|---|---|---|
| C–C | 1 | 154 | 348 |
| C=C | 2 | 134 | 614 |
| C≡C | 3 | 120 | 839 |
| C–O | 1 | 143 | 358 |
| C=O | 2 | 123 | 745 (799 in CO₂) |
| C≡O | 3 | 113 | 1072 |
| N–N | 1 | 145 | 163 |
| N≡N | 3 | 110 | 945 |
| O–H | 1 | 96 | 463 |
| C–H | 1 | 109 | 413 |
| H–H | 1 | 74 | 436 |
| H–F | 1 | 92 | 567 |
| F–F | 1 | 142 | 155 |
| Cl–Cl | 1 | 199 | 242 |

Higher bond order → shorter and stronger bonds (though a double bond is less than twice as strong as a single bond, because a π bond is weaker than a σ bond). N₂'s very strong triple bond explains its inertness and why nitrogen fixation (Haber–Bosch process, nitrogenase enzymes) is so energy-intensive.

**Estimating reaction enthalpies:** $\Delta H \approx \sum E(\text{bonds broken}) - \sum E(\text{bonds formed})$.

## 4. Bond Polarity and Molecular Polarity

When atoms differ in electronegativity, shared electrons are pulled toward the more electronegative atom, creating partial charges ($\delta^+$, $\delta^-$) — a **polar covalent bond** with a **bond dipole**.

**Dipole moment:** $\mu = Qr$, measured in debyes (1 D = $3.336\times10^{-30}$ C·m).

**Molecular polarity** depends on both bond polarity and geometry: bond dipoles add as vectors.
- CO₂ (linear): two polar C=O bonds cancel → nonpolar ($\mu = 0$).
- H₂O (bent): bond dipoles don't cancel → polar ($\mu = 1.85$ D).
- CCl₄ (tetrahedral): nonpolar; CHCl₃: polar (1.04 D).
- BF₃ (trigonal planar): nonpolar; NH₃ (trigonal pyramidal): polar (1.47 D).

Polarity governs solubility ("like dissolves like"), boiling points, and interactions with electric fields.

## 5. VSEPR Theory: Predicting Molecular Shapes

**Valence Shell Electron Pair Repulsion** (Gillespie and Nyholm, 1957): electron domains (bonding pairs, lone pairs; a multiple bond counts as one domain) around a central atom arrange themselves to **minimize repulsion**. Repulsion strength: lone pair–lone pair > lone pair–bond pair > bond pair–bond pair.

| Electron domains | Electron geometry | Bonding domains | Lone pairs | Molecular shape | Ideal angle | Example |
|---|---|---|---|---|---|---|
| 2 | Linear | 2 | 0 | Linear | 180° | CO₂, BeCl₂, HCN |
| 3 | Trigonal planar | 3 | 0 | Trigonal planar | 120° | BF₃, SO₃, CO₃²⁻ |
| 3 | Trigonal planar | 2 | 1 | Bent | <120° | SO₂, O₃ |
| 4 | Tetrahedral | 4 | 0 | Tetrahedral | 109.5° | CH₄, NH₄⁺ |
| 4 | Tetrahedral | 3 | 1 | Trigonal pyramidal | 107° | NH₃ |
| 4 | Tetrahedral | 2 | 2 | Bent | 104.5° | H₂O |
| 5 | Trigonal bipyramidal | 5 | 0 | Trigonal bipyramidal | 90°, 120° | PCl₅ |
| 5 | Trigonal bipyramidal | 4 | 1 | Seesaw | — | SF₄ |
| 5 | Trigonal bipyramidal | 3 | 2 | T-shaped | 90° | ClF₃ |
| 5 | Trigonal bipyramidal | 2 | 3 | Linear | 180° | XeF₂, I₃⁻ |
| 6 | Octahedral | 6 | 0 | Octahedral | 90° | SF₆ |
| 6 | Octahedral | 5 | 1 | Square pyramidal | <90° | BrF₅ |
| 6 | Octahedral | 4 | 2 | Square planar | 90° | XeF₄ |

Notes:
- Lone pairs occupy more space, compressing bond angles: CH₄ (109.5°) > NH₃ (107°) > H₂O (104.5°).
- In trigonal bipyramidal geometries, lone pairs go in **equatorial** positions (fewer 90° repulsions).
- In octahedral geometry with two lone pairs, they go **opposite** each other (square planar).

## 6. Valence Bond Theory and Hybridization

**Valence bond (VB) theory** (Heitler, London, Pauling, Slater): a covalent bond forms when atomic orbitals on two atoms overlap, sharing a pair of electrons with opposite spins.

### Sigma and pi bonds
- **σ (sigma) bond:** electron density along the internuclear axis (end-on overlap: s–s, s–p, p–p head-on, hybrid orbitals). Every single bond is a σ bond. Free rotation is possible around σ bonds.
- **π (pi) bond:** side-by-side overlap of parallel p orbitals, with density above and below the axis. Double bond = 1σ + 1π; triple bond = 1σ + 2π. π bonds restrict rotation, giving rise to cis/trans isomerism.

### Hybridization
Carbon's ground state (2s² 2p²) suggests two bonds, yet carbon forms four equivalent bonds in CH₄. Pauling (1931) proposed that atomic orbitals mix to form equivalent **hybrid orbitals**:

| Hybridization | Atomic orbitals mixed | Geometry | Angle | Example |
|---|---|---|---|---|
| sp | 1 s + 1 p | Linear | 180° | C in C₂H₂ (ethyne), CO₂ |
| sp² | 1 s + 2 p | Trigonal planar | 120° | C in C₂H₄ (ethene), BF₃, benzene |
| sp³ | 1 s + 3 p | Tetrahedral | 109.5° | C in CH₄, N in NH₃, O in H₂O |
| sp³d | 1 s + 3 p + 1 d | Trigonal bipyramidal | 90°/120° | PCl₅ (traditional description) |
| sp³d² | 1 s + 3 p + 2 d | Octahedral | 90° | SF₆ (traditional description) |

**Quick rule:** count electron domains (σ bonds + lone pairs) on the atom: 2 → sp, 3 → sp², 4 → sp³.

**Ethene (C₂H₄):** each C is sp² hybridized; sp²–sp² overlap forms the C–C σ bond; sp²–1s overlap forms C–H bonds; unhybridized 2p orbitals overlap sideways to form the π bond. The molecule is planar.

**Ethyne (C₂H₂):** each C is sp; one σ and two perpendicular π bonds form the triple bond; linear.

**s-character:** sp (50% s) > sp² (33%) > sp³ (25%). More s-character holds electrons closer to the nucleus: shorter, stronger bonds and greater electronegativity of the carbon. This explains why terminal alkynes (pKa ~25) are far more acidic than alkenes (~44) and alkanes (~50).

## 7. Molecular Orbital (MO) Theory

VB theory localizes electrons in bonds; **molecular orbital theory** (Hund, Mulliken, Lennard-Jones) treats electrons as delocalized over the whole molecule, occupying **molecular orbitals** formed as linear combinations of atomic orbitals (**LCAO**).

### Bonding and antibonding orbitals
Combining two atomic orbitals gives two MOs:
- **Bonding MO** (in-phase combination): electron density concentrated between nuclei; lower energy than the atomic orbitals.
- **Antibonding MO** (out-of-phase, marked *): a node between nuclei; higher energy.

$$\text{Bond order} = \frac{(\text{bonding electrons}) - (\text{antibonding electrons})}{2}$$

### Homonuclear diatomic molecules (period 2)
MO energy order for O₂ and F₂:
$$\sigma_{2s} < \sigma^*_{2s} < \sigma_{2p} < \pi_{2p} < \pi^*_{2p} < \sigma^*_{2p}$$
For B₂, C₂, N₂, s–p mixing raises $\sigma_{2p}$ above $\pi_{2p}$:
$$\sigma_{2s} < \sigma^*_{2s} < \pi_{2p} < \sigma_{2p} < \pi^*_{2p} < \sigma^*_{2p}$$

| Molecule | Valence electrons | Bond order | Magnetism | Bond energy (kJ/mol) |
|---|---|---|---|---|
| H₂ | 2 | 1 | Diamagnetic | 436 |
| He₂ | 4 | 0 | Does not exist (stably) | — |
| Li₂ | 2 | 1 | Diamagnetic | 105 |
| B₂ | 6 | 1 | **Paramagnetic** | 290 |
| C₂ | 8 | 2 | Diamagnetic | 602 |
| N₂ | 10 | 3 | Diamagnetic | 945 |
| O₂ | 12 | 2 | **Paramagnetic** (two unpaired electrons in π*) | 498 |
| F₂ | 14 | 1 | Diamagnetic | 155 |
| Ne₂ | 16 | 0 | Does not exist | — |

**Triumph of MO theory:** the Lewis structure O=O has all electrons paired, predicting diamagnetism. Yet liquid oxygen is attracted to a magnet — it is **paramagnetic**. MO theory places two electrons in two degenerate π* orbitals with parallel spins (Hund's rule), correctly predicting paramagnetism and bond order 2. Ground-state O₂ is a "triplet" diradical, which explains why its reactions with organic molecules (singlets) are kinetically slow despite being thermodynamically favorable — fortunately for us.

**Ions:** O₂⁺ (bond order 2.5, shorter bond), O₂⁻ superoxide (1.5), O₂²⁻ peroxide (1).

### HOMO and LUMO
The **highest occupied** and **lowest unoccupied molecular orbitals** (frontier orbitals) govern reactivity (Fukui, Hoffmann; Nobel 1981) and electronic spectra. The HOMO–LUMO gap determines the color of dyes and the band gap of organic semiconductors (OLEDs). Extended conjugation narrows the gap.

### Delocalized π systems
MO theory naturally describes resonance: benzene's six π electrons occupy three delocalized bonding MOs spread over the ring. **Hückel's rule:** planar, cyclic, fully conjugated rings with $4n + 2$ π electrons are aromatic and especially stable.

## 8. Metallic Bonding

In metals, valence electrons are delocalized over the whole crystal — a "sea of electrons" around a lattice of cations. In band-theory terms, atomic orbitals merge into continuous bands that are partially filled. This explains:
- **Electrical and thermal conductivity** (mobile electrons).
- **Luster** (electrons absorb and re-emit light of many frequencies).
- **Malleability and ductility** (non-directional bonding lets layers slide without breaking bonds).
- Melting points rise with the number of valence electrons (Na 98 °C; Mg 650 °C; Al 660 °C; transition metals such as W 3422 °C, with strong d-electron bonding).
- **Alloys** (steel, brass, bronze) tune properties by mixing metals or adding nonmetals.

## 9. Intermolecular Forces

Forces **between** molecules are much weaker than covalent bonds (typically 0.1–40 kJ/mol vs. 150–1000 kJ/mol), but they determine boiling points, melting points, solubility, viscosity, surface tension and the structures of biological macromolecules.

| Force | Origin | Typical strength (kJ/mol) | Example |
|---|---|---|---|
| Ion–dipole | Ion and polar molecule | 40–600 | Na⁺ hydrated by water |
| Hydrogen bond | H on N, O, F attracted to lone pair on N, O, F | 10–40 | Water, DNA base pairs, protein secondary structure |
| Dipole–dipole | Permanent dipoles | 5–25 | HCl, acetone |
| Dipole–induced dipole | Permanent dipole polarizes neighbor | 2–10 | O₂ dissolving in water |
| London dispersion | Instantaneous dipoles from electron fluctuations | 0.05–40 (grows with size) | All molecules; dominant in nonpolar ones (I₂, alkanes, noble gases) |

(The term **van der Waals forces** often refers collectively to dipole–dipole, induced-dipole and dispersion forces.)

### London dispersion forces
Present in all molecules. Electron clouds fluctuate, creating momentary dipoles that induce dipoles in neighbors. Strength increases with **polarizability** — larger molecules with more electrons and greater surface area have stronger dispersion forces:
- Halogens at room temperature: F₂ and Cl₂ gases, Br₂ liquid, I₂ solid.
- Alkanes: methane (bp −162 °C), butane (−0.5 °C), octane (126 °C).
- Branching lowers boiling point (less surface contact): n-pentane 36 °C vs. neopentane 9.5 °C.
- Geckos cling to walls using dispersion forces from millions of nanoscale setae on their feet.

### Hydrogen bonding
A special, strong dipole–dipole interaction (with partial covalent character) between an H atom bonded to N, O or F and a lone pair on another N, O or F.

**Water's anomalous properties** due to hydrogen bonding:
- Boiling point 100 °C vs. H₂S −60 °C (if water followed the trend of H₂Te, H₂Se, H₂S, it would boil near −80 °C).
- High specific heat, heat of vaporization and surface tension.
- Ice is less dense than liquid water (open hexagonal hydrogen-bonded lattice), so ice floats.
- Excellent solvent for ionic and polar substances.

**Biological importance:** hydrogen bonds hold together the DNA double helix (A–T: two bonds; G–C: three bonds), stabilize protein α-helices and β-sheets, and mediate enzyme–substrate recognition. Individually weak, collectively strong, and reversible — ideal for biology.

### Effects on physical properties
- **Boiling/melting points:** stronger intermolecular forces → higher boiling points. Ethanol (C₂H₅OH, H-bonding, bp 78 °C) vs. dimethyl ether (CH₃OCH₃, same formula, no O–H, bp −24 °C).
- **Solubility:** "like dissolves like" — polar dissolves polar, nonpolar dissolves nonpolar. Oil and water don't mix because water molecules prefer hydrogen-bonding with each other (the hydrophobic effect is largely entropic).
- **Viscosity and surface tension** increase with intermolecular forces.
- **Vapor pressure** decreases as intermolecular forces increase.

## 10. Summary

| Concept | Key relation / rule |
|---|---|
| Lattice energy | $\propto q_+q_-/(r_+ + r_-)$ |
| Formal charge | V − N − B/2 |
| Bond order (MO) | (bonding − antibonding)/2 |
| Dipole moment | $\mu = Qr$ (debye) |
| VSEPR | Electron domains maximize separation |
| Hybridization | 2 domains sp, 3 sp², 4 sp³ |
| σ vs π | Single = σ; double = σ + π; triple = σ + 2π |
| O₂ | Paramagnetic, bond order 2 (MO theory) |
| Intermolecular strength | Ion–dipole > H-bond > dipole–dipole > dispersion (for similar sizes) |
| Hückel's rule | $4n + 2$ π electrons → aromatic |
