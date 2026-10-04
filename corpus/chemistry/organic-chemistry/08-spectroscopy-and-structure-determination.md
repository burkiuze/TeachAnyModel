---
title: Spectroscopy and Structure Determination - IR, NMR, Mass Spectrometry and UV-Vis
field: Chemistry
subfield: Organic Chemistry
level: undergraduate
keywords: [spectroscopy, electromagnetic spectrum, infrared spectroscopy, wavenumber, functional group region, fingerprint region, NMR spectroscopy, chemical shift, shielding, integration, spin-spin splitting, n+1 rule, coupling constant, 13C NMR, DEPT, 2D NMR, COSY, HSQC, mass spectrometry, molecular ion, fragmentation, isotope patterns, nitrogen rule, McLafferty rearrangement, high-resolution mass spectrometry, UV-Vis spectroscopy, Beer-Lambert law, chromophores, X-ray crystallography, chromatography]
---

# Spectroscopy and Structure Determination

Before the mid-20th century, determining an organic structure could take years of chemical degradation and synthesis. Today, a combination of spectroscopic methods — **infrared (IR)**, **nuclear magnetic resonance (NMR)**, **mass spectrometry (MS)** and **ultraviolet–visible (UV–Vis)** spectroscopy — can solve most structures of small molecules in hours using milligrams or less of material.

| Technique | Radiation / principle | Information |
|---|---|---|
| Mass spectrometry | Ionization and mass-to-charge separation | Molecular mass, formula (high resolution), fragments, isotopes |
| Infrared | IR (2.5–25 μm; 4000–400 cm⁻¹) — molecular vibrations | Functional groups |
| NMR | Radio waves in a strong magnetic field — nuclear spin transitions | Carbon–hydrogen framework, connectivity, stereochemistry |
| UV–Vis | 200–800 nm — electronic transitions | Conjugated π systems, concentration |
| X-ray crystallography | X-ray diffraction from crystals | Complete 3D structure, absolute configuration |

## 1. Infrared (IR) Spectroscopy

### Principle
Covalent bonds vibrate (stretch and bend) at characteristic frequencies. A molecule absorbs IR radiation when the frequency matches a vibrational frequency **and** the vibration changes the molecule's dipole moment. Symmetric vibrations of nonpolar bonds (e.g. the C≡C stretch in a symmetric alkyne, or N₂, O₂) are IR-inactive (but Raman-active).

Positions are given in **wavenumbers** ($\tilde\nu = 1/\lambda$, cm⁻¹), proportional to frequency and energy. Treating a bond as a harmonic spring (Hooke's law):
$$\tilde\nu = \frac{1}{2\pi c}\sqrt{\frac{k}{\mu}}, \qquad \mu = \frac{m_1m_2}{m_1 + m_2}$$
- **Stronger bonds** (larger $k$) absorb at higher wavenumbers: C≡C (~2200) > C=C (~1650) > C–C (~1200).
- **Lighter atoms** (smaller $\mu$) absorb at higher wavenumbers: C–H (~3000) > C–D (~2200) > C–C.

The number of vibrational modes is $3N - 6$ ($3N - 5$ for linear molecules), so even small molecules have complex spectra.

### Regions of the IR spectrum
- **4000–1500 cm⁻¹: functional group region** — characteristic stretches.
- **1500–400 cm⁻¹: fingerprint region** — complex bending and skeletal vibrations, unique to each compound; used to confirm identity by comparison with reference spectra.

### Characteristic absorptions

| Bond / group | Wavenumber (cm⁻¹) | Intensity and appearance |
|---|---|---|
| O–H (alcohol, phenol) | 3200–3550 | Strong, **broad** (hydrogen bonding); sharp ~3620 if free |
| O–H (carboxylic acid) | 2500–3300 | Very broad, often overlapping C–H |
| N–H (amine, amide) | 3300–3500 | Medium; primary amines **two** spikes, secondary **one**, tertiary none |
| ≡C–H (terminal alkyne) | ~3300 | Strong, sharp |
| =C–H (alkene, aromatic) | 3000–3100 | Medium |
| C–H (alkane, sp³) | 2850–2960 | Strong (just **below** 3000) |
| C–H (aldehyde) | ~2720 and ~2820 | Two weak bands (Fermi doublet) |
| C≡N (nitrile) | 2210–2260 | Medium, sharp |
| C≡C (alkyne) | 2100–2260 | Weak to medium (absent if symmetric) |
| C=O (acid chloride) | ~1800 | Very strong |
| C=O (anhydride) | ~1820 and ~1760 | Two strong bands |
| C=O (ester) | 1735–1750 | Very strong |
| C=O (aldehyde) | 1720–1740 | Very strong |
| C=O (ketone) | ~1715 (cyclohexanone 1715; cyclopentanone 1745) | Very strong |
| C=O (carboxylic acid) | 1700–1725 | Very strong |
| C=O (amide) | 1630–1690 | Strong ("amide I") |
| C=O conjugated (with C=C or aryl) | ~20–30 cm⁻¹ lower | |
| C=C (alkene) | 1620–1680 | Variable (weak if symmetric) |
| C=C (aromatic ring) | ~1600 and ~1450–1500 | Medium, often several bands |
| N–O (nitro) | ~1550 and ~1350 | Two strong bands |
| C–O (alcohol, ether, ester) | 1000–1300 | Strong |
| C–Cl, C–Br | 550–800 | Fingerprint region |

**The C=O stretch** near 1700 cm⁻¹ is usually the most intense and diagnostic peak. Ring strain raises C=O frequency; conjugation lowers it.

### Strategy for reading an IR spectrum
1. Check for C=O (~1650–1820). If present, identify the type from position and other bands (broad O–H → acid; N–H → amide; C–O near 1200 → ester; 2720/2820 → aldehyde; none → ketone).
2. Check for O–H/N–H (3200–3550).
3. Note C–H stretches above vs. below 3000 (unsaturated vs. saturated).
4. Check the triple-bond region (2100–2260).
5. Look for aromatic C=C (~1600, 1500).

## 2. Nuclear Magnetic Resonance (NMR) Spectroscopy

### Principle
Nuclei with an odd number of protons or neutrons have **spin** (¹H, ¹³C, ¹⁹F, ³¹P, ¹⁵N have spin ½). In a magnetic field $B_0$, a spin-½ nucleus has two energy states (aligned and opposed). The energy gap is
$$\Delta E = h\nu = \gamma\hbar B_0$$
and nuclei absorb radio-frequency radiation at the **resonance (Larmor) frequency** $\nu = \gamma B_0/2\pi$. For ¹H: 42.58 MHz per tesla — a "400 MHz" spectrometer has a 9.4 T superconducting magnet. ¹³C resonates at about one quarter of the ¹H frequency (100 MHz on a 400 MHz instrument).

The population difference between the two states is tiny (~1 in 10⁵ at 9.4 T), making NMR inherently insensitive — hence strong magnets. Modern NMR uses short RF pulses and **Fourier transformation** of the resulting signal (Richard Ernst, Nobel Chemistry 1991). Kurt Wüthrich (Nobel 2002) used NMR to determine protein structures in solution. **MRI** is NMR of water protons in the body (Lauterbur and Mansfield, Nobel Medicine 2003).

### ¹H NMR: four types of information
1. **Number of signals** → number of chemically non-equivalent sets of protons.
2. **Chemical shift (δ)** → electronic environment of each set.
3. **Integration** → relative number of protons in each set.
4. **Splitting (multiplicity)** → number of neighboring protons.

### Chemical equivalence
Protons interchangeable by molecular symmetry (rotation, reflection) or rapid processes (rotation about single bonds) are **equivalent** and give one signal. Test: replace each proton in turn by a "Z" group — if the resulting compounds are identical (or enantiomers), the protons are equivalent (homotopic or enantiotopic); if they are diastereomers, the protons are **diastereotopic** and can give separate signals (e.g. the CH₂ protons next to a stereocenter).
Examples: CH₃CH₂Cl has 2 signals; (CH₃)₃CCl has 1; CH₃CH₂CH₂Br has 3; *p*-xylene has 2; ethyl acetate has 3.

### Chemical shift
Electrons circulating around a nucleus generate a small magnetic field opposing $B_0$ — **shielding**. Shielded nuclei resonate at lower frequency (**upfield**, lower δ); deshielded nuclei at higher frequency (**downfield**, higher δ).
$$\delta\,(\text{ppm}) = \frac{\nu_{\text{sample}} - \nu_{\text{TMS}}}{\nu_{\text{spectrometer}}}\times10^6$$
The reference **tetramethylsilane** (TMS, Si(CH₃)₄) is defined as δ 0. Using ppm makes shifts independent of field strength.

**Deshielding factors:**
- **Electronegative atoms** nearby withdraw electron density: CH₃–F (4.26) > CH₃–OH (3.40) > CH₃–Cl (3.05) > CH₃–Br (2.68) > CH₃–I (2.16) > CH₄ (0.23). The effect is additive (CH₂Cl₂ 5.30, CHCl₃ 7.27) and falls off with distance.
- **Magnetic anisotropy of π systems:** circulation of π electrons creates local fields. **Aromatic** protons (δ 6.5–8.5) and alkene protons (δ 4.5–6.5) lie in deshielding zones; **aldehyde** protons (δ 9–10) are strongly deshielded. Alkyne protons (δ ~2–3) lie in a shielding zone along the triple-bond axis. ([18]Annulene's inner protons appear at δ −3, above TMS, while the outer ones are at δ +9 — a striking proof of the aromatic ring current.)
- **Hydrogen bonding:** O–H and N–H shifts vary with concentration, solvent and temperature (broad signals; disappear on shaking with D₂O).

### Typical ¹H chemical shifts

| Proton type | δ (ppm) |
|---|---|
| Alkyl (R–CH₃, R–CH₂–R) | 0.9–1.5 |
| Allylic (C=C–C–H), α to C=O, benzylic (Ar–C–H) | 1.6–2.6 |
| Terminal alkyne (≡C–H) | 2.0–3.0 |
| H–C–N (amines) | 2.2–2.9 |
| H–C–X (halides) | 2.5–4.0 |
| H–C–O (alcohols, ethers, esters O–CH) | 3.3–4.5 |
| Alkene (=C–H) | 4.5–6.5 |
| Aromatic (Ar–H) | 6.5–8.5 |
| Aldehyde (–CHO) | 9.0–10.0 |
| Carboxylic acid (–COOH) | 10–13 (broad) |
| Alcohol O–H | 1–5 (variable, broad) |
| Phenol O–H | 4–8 |
| Amine N–H | 0.5–5 |
| Amide N–H | 5–9 |

### Integration
The area under each signal is proportional to the number of protons producing it, shown as integral curves or numbers. Integrals give **ratios**; e.g. ethyl acetate gives 3:2:3.

### Spin–spin splitting (coupling)
Protons on adjacent carbons (typically three bonds apart, H–C–C–H) influence each other's magnetic environment, splitting signals into multiplets.
**The n + 1 rule:** a signal from protons with $n$ equivalent neighboring protons is split into $n + 1$ peaks, with relative intensities from **Pascal's triangle**:

| Neighbors $n$ | Multiplicity | Intensities |
|---|---|---|
| 0 | Singlet (s) | 1 |
| 1 | Doublet (d) | 1:1 |
| 2 | Triplet (t) | 1:2:1 |
| 3 | Quartet (q) | 1:3:3:1 |
| 4 | Quintet | 1:4:6:4:1 |
| 5 | Sextet | 1:5:10:10:5:1 |
| 6 | Septet | 1:6:15:20:15:6:1 |

**Coupling rules:**
- Equivalent protons do not split each other (CH₃–CH₃ gives a singlet).
- Protons on O–H and N–H usually don't couple (rapid exchange) unless the sample is very pure and dry.
- Coupling is mutual: if A splits B with coupling constant $J$, B splits A with the same $J$.
- If a proton has non-equivalent neighbors with different coupling constants, the pattern is more complex: e.g. a doublet of doublets (dd), doublet of triplets.

**Coupling constants ($J$, in Hz)** are independent of field strength:

| Relationship | $J$ (Hz) |
|---|---|
| Vicinal, free rotation (H–C–C–H) | 6–8 |
| Alkene *trans* (H–C=C–H) | 12–18 |
| Alkene *cis* | 6–12 |
| Geminal on alkene (=CH₂) | 0–3 |
| Aromatic ortho | 6–9 |
| Aromatic meta | 1–3 |
| Aldehyde CHO to α-H | 1–3 |
| Cyclohexane axial–axial | 8–13 |
| Cyclohexane axial–equatorial, eq–eq | 2–5 |

The dependence of vicinal $J$ on dihedral angle is described by the **Karplus equation** — largest at 0° and 180°, smallest near 90° — so $J$ values reveal stereochemistry (distinguishing *cis*/*trans* alkenes and axial/equatorial protons).

**Characteristic patterns:**
- **Ethyl group** (–CH₂CH₃): quartet (2H) + triplet (3H).
- **Isopropyl group** (–CH(CH₃)₂): septet (1H) + doublet (6H).
- ***tert*-Butyl group:** singlet (9H) near δ 1.0–1.3.
- **Methyl ester** (–COOCH₃): singlet (3H) at δ ~3.7.
- **Methyl ketone** (–COCH₃): singlet (3H) at δ ~2.1.
- **Para-disubstituted benzene:** two doublets (2H each) — an "AA'BB'" pattern.
- **Monosubstituted benzene:** 5H multiplet near δ 7.2–7.5.

### Worked example 2.1 — Ethyl acetate (CH₃COOCH₂CH₃)
- δ 1.26 (triplet, 3H): CH₃ of ethyl (2 neighbors).
- δ 2.04 (singlet, 3H): acetyl CH₃ (no neighbors; α to C=O).
- δ 4.12 (quartet, 2H): O–CH₂ (3 neighbors; deshielded by O).

### Worked example 2.2 — Identify C₃H₇Br with signals at δ 1.71 (doublet, 6H) and δ 4.21 (septet, 1H)
Doublet 6H + septet 1H = isopropyl group; CH deshielded by Br → **2-bromopropane**. (1-Bromopropane would show three signals: triplet 3H ~1.0, sextet 2H ~1.9, triplet 2H ~3.4.)

### ¹³C NMR spectroscopy
- ¹³C is only 1.1% abundant and has a smaller γ → ~6000 times less sensitive than ¹H; spectra require more scans.
- Normally recorded **proton-decoupled**: each unique carbon appears as a **singlet**. (¹³C–¹³C coupling is negligible because adjacent ¹³C atoms are rare.)
- Chemical shift range is wide (0–220 ppm), so signals rarely overlap; the **number of signals** directly gives the number of non-equivalent carbons.
- Integrals are **not** reliably proportional to the number of carbons (relaxation and NOE effects; quaternary carbons are often weak).

| Carbon type | δ (ppm) |
|---|---|
| Alkyl (CH₃, CH₂, CH) | 0–50 |
| C–N | 30–65 |
| C–O (alcohols, ethers) | 50–90 |
| C–Cl, C–Br | 25–70 |
| Alkyne (C≡C) | 65–90 |
| Alkene (C=C) | 100–150 |
| Aromatic | 110–160 |
| Nitrile (C≡N) | 115–125 |
| Carboxylic acid / ester / amide C=O | 160–185 |
| Aldehyde C=O | 190–205 |
| Ketone C=O | 200–220 |

**DEPT** (Distortionless Enhancement by Polarization Transfer) experiments distinguish CH₃, CH₂, CH and quaternary carbons: DEPT-90 shows only CH; DEPT-135 shows CH and CH₃ up, CH₂ down; quaternary carbons don't appear.

### Two-dimensional NMR
- **COSY** (¹H–¹H correlation): cross-peaks connect protons that are coupled (usually on adjacent carbons) — traces spin systems.
- **HSQC/HMQC:** correlates each proton with the carbon it is directly attached to.
- **HMBC:** correlates protons with carbons two or three bonds away — connects fragments across heteroatoms and quaternary carbons.
- **NOESY/ROESY:** shows protons close in space (< ~5 Å), revealing stereochemistry and conformation (nuclear Overhauser effect).

## 3. Mass Spectrometry (MS)

### Principle
Molecules are ionized, the ions are separated by **mass-to-charge ratio (m/z)**, and their abundances are recorded.

**Electron ionization (EI):** a 70 eV electron beam knocks an electron from the molecule, forming the **molecular ion** M⁺· (a radical cation) with m/z = molecular mass. Excess energy causes **fragmentation** into smaller ions and neutral radicals/molecules.
- The **base peak** is the most intense peak (set to 100%).
- The **molecular ion peak** gives the molecular mass (it may be weak or absent for alcohols and branched compounds).

**Soft ionization** methods produce intact ions of large molecules: **electrospray ionization** (ESI; John Fenn, Nobel 2002) and **MALDI** (Koichi Tanaka, Nobel 2002) enable MS of proteins, DNA and polymers; chemical ionization gives [M+H]⁺.

**Analyzers:** magnetic sector, quadrupole, time-of-flight (TOF), ion trap, Orbitrap, FT-ICR. Coupled with chromatography: **GC–MS** (forensics, drug testing, environmental analysis) and **LC–MS** (pharmaceuticals, metabolomics, proteomics).

### Interpreting mass spectra
**Nitrogen rule:** a molecule with an **odd** molecular mass contains an **odd** number of nitrogen atoms; even mass → zero or even number of N.

**Isotope patterns:**
- **M+1 peak:** mostly from ¹³C (1.1% per carbon). The number of carbons ≈ (intensity of M+1 / intensity of M) / 1.1%.
- **Chlorine:** ³⁵Cl : ³⁷Cl ≈ 3 : 1 → M and M+2 peaks in a **3:1** ratio.
- **Bromine:** ⁷⁹Br : ⁸¹Br ≈ 1 : 1 → M and M+2 peaks of **nearly equal** height.
- **Sulfur:** ³⁴S gives an M+2 peak of ~4.4%.
- Two bromines: M : M+2 : M+4 ≈ 1 : 2 : 1.

**High-resolution MS (HRMS)** measures m/z to 4–5 decimal places, distinguishing formulas with the same nominal mass because exact atomic masses are not integers (¹H 1.00783, ¹²C 12.00000, ¹⁴N 14.00307, ¹⁶O 15.99491). Example: CO (27.9949), N₂ (28.0061) and C₂H₄ (28.0313) all have nominal mass 28.

### Common fragmentations
- **Alkanes:** clusters of peaks 14 mass units apart (CH₂); cleavage at branch points gives more stable carbocations (tertiary > secondary).
- **Loss of common fragments:** M − 15 (CH₃), M − 18 (H₂O, from alcohols), M − 29 (C₂H₅ or CHO), M − 31 (OCH₃), M − 43 (C₃H₇ or CH₃CO), M − 45 (COOH).
- **α-Cleavage** next to heteroatoms (alcohols, amines, ethers, carbonyls) forms resonance-stabilized cations: e.g. acylium ions R–C≡O⁺ (m/z 43 for CH₃CO⁺); iminium ions from amines (m/z 30 for CH₂=NH₂⁺).
- **Benzylic cleavage:** alkylbenzenes give the **tropylium ion** C₇H₇⁺ at **m/z 91** (often the base peak).
- **McLafferty rearrangement:** carbonyl compounds with a γ-hydrogen undergo a six-membered transition state transfer of the γ-H to oxygen and cleavage of the α–β bond, losing an alkene (e.g. 2-hexanone gives m/z 58).
- **Retro-Diels–Alder** fragmentation of cyclohexenes.

### Worked example 3.1
A compound shows M⁺ at m/z 122 and M+2 at m/z 124 of equal intensity; the base peak is at m/z 43. Equal M/M+2 → one bromine. 122 − 79 = 43 → C₃H₇ (m/z 43 = C₃H₇⁺). The compound is C₃H₇Br (1- or 2-bromopropane; ¹H NMR would distinguish them).

## 4. Ultraviolet–Visible (UV–Vis) Spectroscopy

### Principle
Molecules absorb UV (200–400 nm) or visible (400–800 nm) light, promoting electrons from occupied to unoccupied orbitals — typically **π → π*** (strong) and **n → π*** (weak) transitions in conjugated systems and carbonyls. Isolated C=C bonds absorb below 200 nm (vacuum UV, not routinely measured).

### Beer–Lambert law
$$\boxed{A = \log_{10}\frac{I_0}{I} = \varepsilon lc}$$
$A$ is absorbance, $\varepsilon$ the molar absorptivity (L mol⁻¹ cm⁻¹), $l$ path length (cm), $c$ concentration (M). UV–Vis is widely used for **quantitative analysis** (DNA concentration at 260 nm; protein at 280 nm from Trp and Tyr; enzyme kinetics via NADH at 340 nm; clinical assays).

### Conjugation and color
Extending conjugation lowers the HOMO–LUMO gap and shifts λmax to longer wavelengths (**bathochromic** or red shift):

| Compound | Conjugated C=C | λmax (nm) |
|---|---|---|
| Ethene | 1 | 171 |
| Buta-1,3-diene | 2 | 217 |
| Hexa-1,3,5-triene | 3 | 258 |
| β-Carotene | 11 | ~450 (also 425, 480) → orange |
| Lycopene | 11 (+2 unconjugated) | ~470 → red (tomatoes) |

A compound absorbing in the visible appears as the **complementary color**: absorbing blue (~450 nm) looks orange; absorbing green (~530 nm) looks red-purple (chlorophyll absorbs red and blue, reflecting green). Substances that absorb light are **chromophores**; groups that modify absorption (–OH, –NH₂, –OR) are **auxochromes**. pH indicators change color because protonation alters conjugation (phenolphthalein becomes a conjugated, colored dianion in base).

## 5. Other Structural Methods
- **X-ray crystallography:** diffraction from a single crystal gives the full 3D arrangement of atoms, bond lengths and angles, and (with anomalous scattering) absolute configuration. Dorothy Hodgkin solved penicillin (1945), vitamin B₁₂ (1955) and insulin (1969).
- **Cryo-electron microscopy** for large biomolecules.
- **Chromatography** separates mixtures before analysis: thin-layer chromatography (TLC, R_f values), column chromatography, gas chromatography (GC), high-performance liquid chromatography (HPLC).
- **Elemental analysis** (combustion) gives empirical formulas.
- **Optical rotation and circular dichroism** probe chirality.
- **Raman spectroscopy** (complementary to IR; symmetric vibrations).

## 6. Solving a Structure: Integrated Strategy

1. **Molecular formula** (HRMS, or elemental analysis + MS) → calculate **degree of unsaturation**.
2. **IR** → identify functional groups (C=O type, O–H, N–H, C≡N, etc.).
3. **¹³C NMR** (+ DEPT) → number and types of carbons (carbonyls, aromatic, sp³, symmetry).
4. **¹H NMR** → fragments from shifts, integration and splitting (ethyl, isopropyl, para-substitution...).
5. **Assemble fragments** consistent with all data; use 2D NMR for connectivity if needed.
6. **Verify:** predicted spectra should match all observed data; check MS fragmentation.

### Worked example 6.1
**Data:** C₄H₈O₂. IR: 1740 cm⁻¹ (strong), 1240 cm⁻¹; no O–H. ¹H NMR: δ 1.26 (t, 3H), 2.04 (s, 3H), 4.12 (q, 2H). ¹³C NMR: δ 14.2, 21.0, 60.4, 171.1.
**Analysis:** DoU = (8 + 2 − 8)/2 = 1 → one C=O. IR 1740 + 1240 and no O–H → ester. ¹³C 171 → ester carbonyl; 60.4 → O–CH₂. ¹H: ethyl group on O (quartet at 4.12) and an isolated CH₃ next to C=O (singlet at 2.04).
**Structure:** ethyl acetate, CH₃COOCH₂CH₃. (Its isomer methyl propanoate, CH₃CH₂COOCH₃, would show a singlet at δ ~3.7 for OCH₃ and a quartet at ~2.3 for CH₂ next to C=O.)

### Worked example 6.2
**Data:** C₈H₈O. IR: 1685 cm⁻¹. ¹H NMR: δ 2.60 (s, 3H), 7.4–7.6 (m, 3H), 7.95 (d, 2H). MS: m/z 120 (M⁺), 105 (base peak), 77.
**Analysis:** DoU = (16 + 2 − 8)/2 = 5 → benzene ring (4) + C=O (1). 1685 cm⁻¹ → conjugated ketone. Singlet 3H at 2.60 → CH₃ next to C=O. 5 aromatic H → monosubstituted benzene. MS: 120 − 15 = 105 (C₆H₅CO⁺, benzoyl cation, loss of CH₃); 77 (C₆H₅⁺).
**Structure:** acetophenone, C₆H₅COCH₃.

## 7. Summary

| Method | Key data | Typical use |
|---|---|---|
| MS | M⁺ (mass), M+1/M+2 isotopes, fragments | Formula, halogens, substructures |
| IR | ~1700 C=O; 3200–3550 O–H/N–H; ~2200 C≡N/C≡C; 3000 C–H | Functional groups |
| ¹H NMR | δ, integration, splitting (n+1), J | Proton environments and connectivity |
| ¹³C NMR | Number of signals, δ (0–220) | Carbon skeleton, symmetry |
| UV–Vis | λmax, ε; Beer–Lambert $A = \varepsilon lc$ | Conjugation, quantitation |
