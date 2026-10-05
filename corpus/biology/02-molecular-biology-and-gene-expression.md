---
title: Molecular Biology - DNA Replication, Transcription, Translation and Gene Regulation
field: Biology
subfield: Molecular Biology
level: high-school to undergraduate
keywords: [central dogma, DNA replication, semiconservative, DNA polymerase, leading strand, lagging strand, Okazaki fragments, primase, ligase, helicase, proofreading, DNA repair, transcription, RNA polymerase, promoter, mRNA processing, splicing, introns, exons, genetic code, codons, tRNA, ribosome, translation, mutations, lac operon, gene regulation, epigenetics, PCR, DNA sequencing, CRISPR, recombinant DNA, Meselson-Stahl experiment, double helix, Chargaff's rules, multifork replication, kinetic proofreading, wobble pairing, open reading frame, reading frame, mRNA half-life, gene expression kinetics, lac repressor, qPCR, restriction mapping, reverse transcriptase, antibiotics, mRNA vaccines, RNA world]
---

# Molecular Biology: DNA Replication, Transcription, Translation and Gene Regulation

Molecular biology explains how genetic information is stored, copied and expressed. Francis Crick summarized the flow of information in 1958 as the **central dogma**:
$$\text{DNA}\xrightarrow{\text{replication}}\text{DNA}\xrightarrow{\text{transcription}}\text{RNA}\xrightarrow{\text{translation}}\text{Protein}$$
Exceptions and extensions: **reverse transcription** (RNA → DNA, in retroviruses, retrotransposons and telomerase), **RNA replication** (RNA viruses), and regulatory RNAs that are never translated. Information never flows from protein back to nucleic acid.

Crick's own formulation was more precise than the popular slogan "DNA makes RNA makes protein". In his 1958 lecture "On Protein Synthesis" and again in a 1970 paper in *Nature*, he stated that once sequence information has passed into protein it cannot get out again: there is no mechanism for copying an amino-acid sequence back into nucleic acid or into another protein. The 1970 discovery of reverse transcriptase by Howard Temin and David Baltimore therefore did not break the dogma; it added a transfer (RNA → DNA) that Crick had already listed as possible. Prions — misfolded proteins that convert normal copies of the same protein into the misfolded shape — transmit a *conformation*, not a sequence, so they do not contradict it either.

This chapter follows the information through each step: how DNA is copied (replication) and kept intact (repair), how a gene is read out (transcription and RNA processing), how the four-letter nucleic-acid alphabet is translated into the twenty-letter protein alphabet (the genetic code and the ribosome), how sequences change (mutation), how cells decide which genes to express (regulation), and how these mechanisms became the tools of biotechnology.

## 1. Discovery of DNA as the Genetic Material

- **1869:** Friedrich Miescher isolated "nuclein" (DNA) from pus cells.
- **1928:** Frederick Griffith's **transformation** experiment: a heat-killed virulent (smooth, S) strain of *Streptococcus pneumoniae* converted live harmless (rough, R) bacteria into virulent ones — some "transforming principle" was transferred.
- **1944:** Oswald Avery, Colin MacLeod and Maclyn McCarty showed the transforming principle is **DNA** (destroyed by DNase, not by protease or RNase).
- **1950:** Erwin Chargaff reported that in double-stranded DNA the amount of adenine equals that of thymine and guanine equals cytosine (**Chargaff's rules**), while the overall base composition varies between species.
- **1952:** Alfred Hershey and Martha Chase labeled bacteriophage T2 with ³⁵S (protein) or ³²P (DNA); only ³²P entered bacteria, confirming DNA as the genetic material of phages. The same year, Rosalind Franklin and her student Raymond Gosling recorded "Photograph 51", an X-ray diffraction pattern of the B form of DNA whose X-shaped cross of spots is the signature of a helix.
- **1953:** Watson and Crick's double helix, based on Rosalind Franklin's X-ray data and Chargaff's rules.
- **1958:** Meselson and Stahl demonstrated **semiconservative replication**.

Before the 1940s most biologists expected genes to be proteins: proteins are built from twenty different units and seemed complex enough to carry information, whereas DNA was thought (wrongly) to be a monotonous repeat of four nucleotides — the "tetranucleotide hypothesis". Chargaff's finding that base composition differs between species undermined that idea, and the double helix explained at once how a four-letter polymer could store information (in the order of its bases) and be copied (each strand specifies its partner).

### The double helix in numbers

DNA is a polymer of nucleotides, each consisting of a deoxyribose sugar, a phosphate and one of four bases — the purines adenine (A) and guanine (G), and the pyrimidines cytosine (C) and thymine (T). Phosphodiester bonds link the 3' carbon of one sugar to the 5' carbon of the next, giving each strand a direction (5' → 3'). The two strands run **antiparallel** and are held together by hydrogen-bonded base pairs (A–T with two hydrogen bonds, G–C with three) and, even more importantly for stability, by **base stacking** between neighboring pairs.

| Property of B-DNA (the usual form in cells) | Value |
|---|---|
| Diameter | about 2.0 nm |
| Rise per base pair | 0.34 nm |
| Base pairs per turn (in solution) | about 10.5 |
| Helical pitch | about 3.6 nm |
| Handedness | right-handed |
| Grooves | major and minor (proteins read sequence mostly in the major groove) |
| Average molar mass per base pair (sodium salt) | about 650 g/mol |
| Hydrogen bonds per pair | A–T: 2; G–C: 3 |

Because every G pairs with a C and every A with a T, in double-stranded DNA $[\text{A}] = [\text{T}]$ and $[\text{G}] = [\text{C}]$, so knowing the fraction of one base fixes all four. The human genome, for example, is about 41% G + C, so G = C ≈ 20.5% and A = T ≈ 29.5%. The rules do *not* hold for single-stranded genomes (some viruses), which is one way such genomes were recognized.

**Worked Example 1.1 — How much DNA is in a human cell?** A diploid human cell contains about $6.2\times10^{9}$ base pairs (twice the haploid $3.1\times10^{9}$). Estimate (a) the total length of its DNA if stretched out as B-DNA, (b) its mass, and (c) the compaction of chromosome 1 (248 million base pairs) into a mitotic chromosome about 10 μm long.
1. Length: $L = (6.2\times10^{9})(0.34\times10^{-9}\ \text{m}) = 2.1\ \text{m}$.
2. Mass: $m = \dfrac{(6.2\times10^{9})(650\ \text{g/mol})}{6.022\times10^{23}\ \text{mol}^{-1}} = 6.7\times10^{-12}\ \text{g} = 6.7\ \text{pg}$.
3. Chromosome 1 as a single molecule: $(2.48\times10^{8})(0.34\ \text{nm}) = 8.4\times10^{7}\ \text{nm} = 8.4\ \text{cm}$.
4. Compaction: $8.4\ \text{cm} / 10\ \mu\text{m} = 0.084\ \text{m} / 1.0\times10^{-5}\ \text{m} \approx 8.4\times10^{3}$.

**Answer:** about 2 m of DNA weighing about 7 pg per cell, and a mitotic chromosome is packed roughly ten-thousand-fold along its length — achieved by wrapping around nucleosomes, folding into loops and condensing with condensin. Copying, reading and repairing such a long, tightly packed molecule is the central logistic problem of the eukaryotic nucleus.

## 2. DNA Replication

### Semiconservative replication
Each new DNA molecule consists of one **parental (template)** strand and one **newly synthesized** strand. **Meselson–Stahl experiment:** *E. coli* grown in heavy ¹⁵N medium were shifted to ¹⁴N; DNA was separated by density in CsCl gradients. After one generation, all DNA had intermediate density (ruling out conservative replication); after two generations, half intermediate and half light (ruling out dispersive replication). Described as "the most beautiful experiment in biology".

The method itself was an advance. Spinning a cesium chloride solution at high speed for many hours sets up a smooth density gradient; each DNA molecule sinks or floats until it reaches the point where the solution density equals its own buoyant density, forming a sharp band. ¹⁵N-DNA is only about 1% denser than ¹⁴N-DNA, yet the bands were cleanly separated, and the UV absorbance of DNA let Meselson and Stahl photograph them without radioactive labels.

*Derivation: the band pattern after n generations.* Start with one fully heavy (¹⁵N/¹⁵N) molecule and let every molecule replicate once per generation in ¹⁴N medium.
1. Under semiconservative replication the two original heavy strands are never broken up or duplicated: each one simply ends up in a different daughter molecule.
2. After $n$ generations there are $2^n$ molecules, and exactly 2 of them contain an original heavy strand (each such molecule is hybrid ¹⁵N/¹⁴N); all the others are light.
3. Therefore, for $n \ge 1$,
$$f_{\text{hybrid}} = \frac{2}{2^{n}} = 2^{\,1-n},\qquad f_{\text{light}} = 1 - 2^{\,1-n}$$
4. The **conservative** model would keep the parental double helix intact: after $n$ generations, a fraction $2^{-n}$ would be fully heavy, the rest fully light, and no hybrid band would ever appear.
5. The **dispersive** model would scatter old material evenly: every molecule would be identical, with a heavy fraction of $2^{-n}$, so there would always be a single band drifting steadily toward the light position.

**Worked Example 2.1 — Predicting the gradient.** What band pattern does each model predict after 4 generations in ¹⁴N medium?
1. Semiconservative: $f_{\text{hybrid}} = 2^{1-4} = 1/8 = 12.5\%$; $f_{\text{light}} = 87.5\%$.
2. Conservative: heavy $2^{-4} = 1/16 = 6.25\%$; light $93.75\%$; hybrid $0$.
3. Dispersive: one band containing $1/16$ of the heavy isotope in every molecule — very close to, but not exactly at, the light position.

**Answer:** semiconservative — two bands, hybrid 12.5% and light 87.5%; conservative — heavy 6.25% and light 93.75%; dispersive — a single band just above the light position. Meselson and Stahl also heated the hybrid DNA to separate its strands and found one heavy and one light single strand, which rules out dispersive replication directly.

### The replication machinery

| Protein | Function |
|---|---|
| **Helicase** | Unwinds the double helix at the replication fork (breaks hydrogen bonds) |
| **Single-strand binding proteins (SSB)** | Keep separated strands apart |
| **Topoisomerase** (gyrase in bacteria) | Relieves supercoiling ahead of the fork (target of fluoroquinolone antibiotics and some anticancer drugs) |
| **Primase** | Synthesizes short RNA primers (~10 nt) — DNA polymerase cannot start a new strand from scratch |
| **DNA polymerase α–primase** (eukaryotes) | Makes the RNA primer and extends it with a short stretch of DNA before handing over to δ or ε |
| **DNA polymerase III** (bacteria) / **δ and ε** (eukaryotes) | Main replicative polymerases; add nucleotides 5'→3' |
| **Sliding clamp** (β clamp / PCNA) | Holds polymerase on DNA for high processivity |
| **Clamp loader** (γ complex / RFC) | Opens the ring-shaped clamp and places it on the primer–template junction using ATP |
| **DNA polymerase I** (bacteria) | Removes RNA primers (5'→3' exonuclease) and fills gaps |
| **DNA ligase** | Seals nicks by forming phosphodiester bonds |
| **Telomerase** (eukaryotes) | Extends chromosome ends |

### Key principles
1. **DNA polymerases synthesize only in the 5' → 3' direction**, adding deoxynucleoside triphosphates (dNTPs) to the 3'-OH of the growing strand. Pyrophosphate (PPᵢ) release and its hydrolysis drive the reaction.
2. They **require a primer** with a free 3'-OH.
3. Because the two strands are antiparallel:
   - The **leading strand** is synthesized continuously toward the replication fork.
   - The **lagging strand** is synthesized discontinuously, away from the fork, in short **Okazaki fragments** (1000–2000 nucleotides in bacteria, 100–200 in eukaryotes; discovered by Reiji and Tsuneko Okazaki, 1968), each requiring a new primer, later joined by ligase.
4. Replication begins at **origins of replication**: one in the circular *E. coli* chromosome (oriC; replication proceeds bidirectionally at ~1000 nucleotides/s per fork, copying 4.6 Mb in ~40 minutes); thousands in eukaryotic chromosomes (forks move only tens of nucleotides per second, roughly 1–3 kb per minute in human cells; the human genome is replicated in ~8 hours of S phase).

In the cell the two polymerases at a fork travel together as one **replisome**. The lagging-strand template is looped out ("trombone model") so that the lagging-strand polymerase can move in the same overall direction as the fork while still synthesizing 5'→3'; each time an Okazaki fragment is finished, the polymerase releases, the loop collapses, and a new primer is laid down near the fork.

### The chemistry of nucleotide addition, and why synthesis runs 5' → 3'

The 3'-OH at the end of the primer attacks the innermost (α) phosphate of the incoming dNTP, forming a new phosphodiester bond and releasing pyrophosphate:
$$(\text{dNMP})_n + \text{dNTP} \longrightarrow (\text{dNMP})_{n+1} + \text{PP}_i$$
This step alone is only slightly favorable, but pyrophosphatase immediately hydrolyzes PPᵢ to two phosphates (standard free energy about −19 kJ/mol), pulling the overall reaction strongly forward. Two metal ions (Mg²⁺) in the active site position the reactants and stabilize the negative charges.

Why has no organism evolved a polymerase that works 3'→5', which would make the lagging strand unnecessary? Consider proofreading. In 5'→3' synthesis, the energy for each addition is carried by the *incoming* nucleotide, so if the last nucleotide added is wrong, the exonuclease can clip it off and leave an ordinary 3'-OH ready for the next correct dNTP. In a hypothetical 3'→5' polymerase, the activating triphosphate would sit on the 5' end of the *growing chain*. Removing a mismatched terminal nucleotide would leave a chain end without a triphosphate — a dead end that could not be extended without a separate re-activation step. The 5'→3' rule is therefore the price of being able to correct errors cheaply, and the discontinuous lagging strand is the price of the 5'→3' rule.

### How long does it take? Origins and forks

**Worked Example 2.2 — Replication timetables.** (a) The *E. coli* chromosome is 4.64 Mb with one origin; forks move at 1000 nt/s. How long does replication take? (b) A diploid human cell copies $6.2\times10^{9}$ bp in an 8-hour S phase with forks moving at about 30 nt/s. How many forks must be active on average? (c) If Okazaki fragments average 200 nt, how many must be made and joined in one human S phase?
1. (a) Two forks leave oriC in opposite directions, so each copies half the chromosome: $t = \dfrac{4.64\times10^{6}/2}{1000\ \text{s}^{-1}} = 2320\ \text{s} \approx 39\ \text{min}$.
2. (b) Total synthesis rate needed: $6.2\times10^{9}\ \text{bp}/(8\times3600\ \text{s}) = 2.15\times10^{5}$ bp/s.
3. Divide by the rate of one fork: $2.15\times10^{5}/30 \approx 7.2\times10^{3}$ forks working at any moment, i.e. about 3600 active origins (each origin launches two forks).
4. (c) At every base pair, one of the two new strands is made by leading-strand synthesis and the other by lagging-strand synthesis, so the lagging strand totals $6.2\times10^{9}$ nucleotides: $6.2\times10^{9}/200 = 3.1\times10^{7}$ fragments.

**Answer:** (a) about 39 minutes; (b) roughly 7000 simultaneous forks (thousands of origins fire during S phase, not all at once — early- and late-replicating regions take turns); (c) about 30 million Okazaki fragments, each needing a primer, primer removal and a ligation. A single human origin would need many weeks to copy one chromosome (Practice Problem 6), which is why eukaryotes evolved many origins.

### Replicating faster than replication: multifork replication

In rich medium *E. coli* divides every 20 minutes, yet copying the chromosome takes about 40 minutes (the **C period**) and a further ~20 minutes (the **D period**) pass between the end of replication and division. Stephen Cooper and Charles Helmstetter (1968) resolved the paradox: a new round of replication starts at oriC before the previous round has finished, so a fast-growing cell contains chromosomes with several generations of nested forks, and each newborn cell inherits a chromosome that is already partly replicated.

*Derivation: the origin-to-terminus copy ratio.* In steady exponential growth with doubling time $\tau$, the number of copies of any locus in the population grows as $2^{t/\tau}$. A locus a fraction $x$ of the way from the origin ($x = 0$) to the terminus ($x = 1$) is copied a time $xC$ after its origin fired. So today's copy number of that locus equals the copy number the origin had a time $xC$ ago:
$$N(x) = N_{\text{ori}}\,2^{-xC/\tau}\qquad\Longrightarrow\qquad \frac{N_{\text{ori}}}{N_{\text{ter}}} = 2^{\,C/\tau}$$
With $C = 40$ min and $\tau = 20$ min, origin-proximal genes are present in $2^{2} = 4$ times as many copies as terminus-proximal genes; in slow growth ($\tau = 60$ min) the ratio falls to $2^{2/3} \approx 1.6$. Measuring this ratio by sequencing ("marker frequency analysis") is a standard way to estimate how fast bacteria in a sample are replicating. It may also explain why highly expressed genes such as most of *E. coli*'s seven ribosomal-RNA operons lie closer to oriC than to the terminus: in fast growth they gain extra gene dosage.

### Fidelity
- Base-pairing selectivity: ~1 error per 10⁴–10⁵ nucleotides.
- **Proofreading** by the polymerase's 3'→5' exonuclease removes mismatches: improves to ~1 per 10⁷.
- **Mismatch repair** after replication: overall ~1 error per 10⁹–10¹⁰ nucleotides. Inherited mismatch repair defects (for example in *MLH1* or *MSH2*) cause Lynch syndrome (hereditary colorectal cancer). In *E. coli*, the mismatch repair system tells the new strand from the old one because the new strand's GATC sites are not yet methylated by Dam methylase; eukaryotes use strand nicks and the orientation of PCNA instead.

Because the stages act in series, the error rates multiply:
$$\varepsilon_{\text{overall}} = \varepsilon_{\text{selection}}\times\varepsilon_{\text{proofreading}}\times\varepsilon_{\text{MMR}} \approx 10^{-5}\times10^{-2}\times(10^{-2}\text{ to }10^{-3}) = 10^{-9}\text{ to }10^{-10}$$
where each $\varepsilon$ after the first is the fraction of errors that *escape* that stage.

*Why can't base pairing alone be accurate enough? Kinetic proofreading.* If a correct and an incorrect nucleotide bind the polymerase with free energies differing by $\Delta\Delta G$, then at equilibrium the ratio of wrong to right bound substrates (at equal concentrations) is a Boltzmann factor:
$$f_0 = e^{-\Delta\Delta G/RT}$$
The free-energy difference between a correct and a mismatched pair is modest, so a single equilibrium check cannot reach the observed accuracy. John Hopfield (1974) and Jacques Ninio (1975) showed how to beat this limit: if the enzyme makes an irreversible, energy-consuming step after the first binding (such as hydrolysis of a nucleoside triphosphate) and then gives the substrate a second independent chance to dissociate, the same discrimination is applied twice, so $f \approx f_0^{2}$; with $k$ independent checks, $f \approx f_0^{k}$. The extra free energy spent is the thermodynamic cost of accuracy. Translation uses this principle (EF-Tu hydrolyzes GTP between initial codon recognition and the final acceptance of the tRNA), as do aminoacyl-tRNA synthetases, whose separate editing sites hydrolyze wrongly charged tRNAs.

**Worked Example 2.3 — From error rates to mutations per cell division.** (a) If the overall replication error rate is $10^{-10}$ to $10^{-9}$ per nucleotide, how many new errors arise each time a diploid human cell ($6.2\times10^{9}$ bp) divides? (b) Using an illustrative $\Delta\Delta G = 12$ kJ/mol, compare one equilibrium check with two independent checks at 37 °C.
1. (a) Expected errors $= (6.2\times10^{9})(10^{-10}) = 0.62$ to $(6.2\times10^{9})(10^{-9}) = 6.2$.
2. (b) $RT = (8.314\ \text{J mol}^{-1}\text{K}^{-1})(310.15\ \text{K}) = 2.58\ \text{kJ/mol}$.
3. One check: $f_0 = e^{-12/2.58} = e^{-4.65} = 9.5\times10^{-3}$, about 1 error in 105.
4. Two checks: $f_0^{2} = 9.1\times10^{-5}$, about 1 error in 11 000.

**Answer:** (a) roughly 0.6 to 6 new point mutations per diploid genome per division; (b) a second, independent check improves accuracy about a hundredfold, from $\sim10^{-2}$ to $\sim10^{-4}$. Over the roughly $10^{16}$ cell divisions of a human lifetime, even this extraordinary fidelity guarantees that every adult is a mosaic of genetically slightly different cells — the raw material of cancer.

### The end-replication problem and telomeres
On linear chromosomes, the lagging strand cannot be fully completed at the very end (no room for a final primer), so chromosomes shorten with each division. **Telomeres** (TTAGGG repeats in vertebrates, several kilobases long) buffer genes from loss; **telomerase** carries its own RNA template to extend them. Telomerase was discovered in the ciliate *Tetrahymena* by Carol Greider and Elizabeth Blackburn in 1984; with Jack Szostak they received the 2009 Nobel Prize in Physiology or Medicine. Telomerase is a specialized reverse transcriptase: its RNA subunit contains a short sequence complementary to the telomere repeat, which the enzyme copies into DNA again and again. Most human somatic cells express little telomerase, so their telomeres shorten until the cells stop dividing (the Hayflick limit); germ cells, stem cells and about 85–90% of cancers keep telomerase active. Bacteria avoid the problem entirely by having circular chromosomes.

## 3. DNA Damage and Repair

DNA in each human cell suffers tens of thousands of lesions per day (depurination, deamination, oxidation, UV damage, strand breaks). Repair systems:
- **Direct reversal:** photolyase reverses UV-induced pyrimidine dimers (not in placental mammals); O⁶-methylguanine methyltransferase.
- **Base excision repair (BER):** glycosylases remove damaged bases (e.g. uracil from deaminated cytosine).
- **Nucleotide excision repair (NER):** removes bulky lesions such as thymine dimers. Defects cause **xeroderma pigmentosum** (extreme sensitivity to sunlight and skin cancer).
- **Mismatch repair (MMR).**
- **Double-strand break repair:** **homologous recombination** (accurate, uses the sister chromatid; requires BRCA1/BRCA2 — mutations greatly raise breast and ovarian cancer risk; PARP inhibitors exploit this weakness) and **non-homologous end joining** (error-prone).
(Lindahl, Modrich and Sancar, Nobel Chemistry 2015.)

| Pathway | Typical lesion | Key idea | Disease when defective |
|---|---|---|---|
| Direct reversal | O⁶-methylguanine; UV dimers (photolyase, absent in placental mammals) | Chemically undo the damage, no excision | Tumors silencing *MGMT* respond better to alkylating chemotherapy |
| Base excision repair | Uracil, oxidized bases (8-oxoguanine), abasic sites | Glycosylase removes one base; AP endonuclease, polymerase and ligase finish | Some cancer predispositions (e.g. *MUTYH*-associated polyposis) |
| Nucleotide excision repair | Bulky adducts, thymine dimers | Cut out a ~25–30-nt stretch containing the lesion and resynthesize | Xeroderma pigmentosum, Cockayne syndrome |
| Mismatch repair | Replication mismatches, small loops | Recognize mismatch, remove the new strand's segment | Lynch syndrome |
| Homologous recombination | Double-strand breaks (S/G₂) | Copy the intact sister chromatid | Hereditary breast/ovarian cancer (*BRCA1/2*) |
| Non-homologous end joining | Double-strand breaks (any phase) | Ligate the ends directly, often with small indels | Severe combined immunodeficiency (NHEJ also joins antibody gene segments) |

Why is uracil in DNA treated as damage when RNA uses it routinely? Cytosine spontaneously deaminates to uracil. If DNA normally contained U instead of T, the cell could not tell a correct U from a damaged C; using T (methylated U) in DNA makes every U a recognizable error. This is a likely reason DNA evolved to use thymine.

The **PARP-inhibitor strategy** is a textbook example of **synthetic lethality**: losing either of two pathways is survivable, but losing both kills the cell. Tumors lacking BRCA1 or BRCA2 cannot repair double-strand breaks by homologous recombination; blocking PARP (which helps repair single-strand breaks) causes breaks that become double-strand breaks at replication forks, killing the tumor cells while sparing normal cells that still have functional BRCA.

## 4. Transcription

**Transcription** copies a gene's DNA sequence into RNA.

### Basic features
- **RNA polymerase** synthesizes RNA 5'→3', using ribonucleoside triphosphates (ATP, GTP, CTP, UTP) and one DNA strand as template.
- The **template (antisense)** strand is read 3'→5'; the RNA has the same sequence as the **coding (sense)** strand, with U in place of T.
- **No primer** is needed.
- Error rate is higher than replication (~1 in 10⁴–10⁵) but errors are not inherited.

Which strand is the template differs from gene to gene: genes on the same chromosome can point in opposite directions, so "the template strand" is defined only for a particular gene. By convention, gene sequences in databases are written as the coding strand, 5' to 3', so that they read like the mRNA.

### Kinds of RNA

| RNA | Typical size | Role |
|---|---|---|
| mRNA (messenger) | hundreds to many thousands of nt | Carries the coding sequence to ribosomes |
| rRNA (ribosomal) | 5S ~120 nt; 16S ~1540 nt (bacteria); 18S, 28S in eukaryotes | Structural and catalytic core of the ribosome |
| tRNA (transfer) | ~76 nt | Adaptor between codon and amino acid |
| snRNA (small nuclear) | ~100–200 nt | Core of the spliceosome |
| snoRNA (small nucleolar) | ~60–300 nt | Guides chemical modification of rRNA |
| miRNA / siRNA | ~21–23 nt | Guide silencing of target mRNAs |
| lncRNA (long non-coding) | > 200 nt | Diverse regulatory roles (e.g. *XIST*) |
| Ribozymes (e.g. RNase P RNA, self-splicing introns) | varies | RNA enzymes |

In a growing bacterium about 80% of the RNA by mass is rRNA, about 15% tRNA and only about 5% mRNA — mRNA is a small, rapidly turned-over fraction.

### Stages
1. **Initiation:** RNA polymerase binds the **promoter** upstream of the gene.
   - Bacteria: a single RNA polymerase (core enzyme α₂ββ′ω plus a **sigma (σ) factor**, together the holoenzyme); σ recognizes promoter elements at −35 (TTGACA) and −10 (TATAAT, Pribnow box). Alternative σ factors switch on whole sets of genes, for example heat-shock genes.
   - Eukaryotes: three nuclear RNA polymerases — **Pol I** (most rRNA), **Pol II** (mRNA, most snRNAs, miRNAs), **Pol III** (tRNA, 5S rRNA). Pol II requires **general transcription factors**; **TFIID** binds the **TATA box** (~−25 to −30). Enhancers, often far away, bind activators that loop DNA to contact the promoter via **Mediator**. (Roger Kornberg, Nobel Chemistry 2006 for the structural basis of eukaryotic transcription.) α-Amanitin from death-cap mushrooms potently inhibits Pol II.
2. **Elongation:** the polymerase unwinds ~10–20 bp of DNA (transcription bubble) and adds nucleotides (~20–50 nt/s).
3. **Termination:**
   - Bacteria: **intrinsic (Rho-independent)** — a GC-rich hairpin followed by a run of U's; or **Rho-dependent** — the Rho helicase dislodges the polymerase.
   - Eukaryotes (Pol II): transcription continues past the polyadenylation signal (AAUAAA); the RNA is cleaved and the polymerase is released.

The intrinsic terminator works through simple chemistry: the G–C-rich hairpin forms in the RNA just behind the polymerase and pulls on the RNA–DNA hybrid, while the run of U's leaves the RNA held to the template only by weak rU–dA base pairs, the weakest of all Watson–Crick pairs, so the transcript lets go.

Promoter numbering counts the first transcribed nucleotide as +1, with negative numbers upstream; there is no position 0. The closer a promoter's −35 and −10 boxes are to the consensus sequences (and the closer their spacing is to the optimal 17 bp), the more often σ initiates there, so promoter sequence sets a gene's basal expression level.

### Eukaryotic mRNA processing
Eukaryotic primary transcripts (pre-mRNA) are processed in the nucleus:
1. **5' cap:** 7-methylguanosine attached by an unusual 5'–5' triphosphate linkage — protects from degradation and helps ribosome binding.
2. **3' poly(A) tail:** ~200 adenine nucleotides added by poly(A) polymerase — stability, export, translation.
3. **Splicing:** non-coding **introns** are removed and **exons** joined by the **spliceosome** (snRNPs; splice sites GU at the 5' end of introns and AG at the 3' end; branch point A forms a lariat). Introns were discovered in 1977 (Roberts and Sharp, Nobel 1993).
   - **Alternative splicing** lets one gene produce multiple protein variants; ~95% of human multi-exon genes are alternatively spliced. The *Drosophila Dscam* gene can potentially produce over 38 000 isoforms.
   - Splicing errors cause disease (some β-thalassemias, spinal muscular atrophy — treated with antisense oligonucleotide nusinersen, which corrects splicing).

Splicing chemistry consists of two **transesterification** reactions, so no net energy is needed to break and remake the bonds (ATP is used by the spliceosome's helicases to rearrange its RNAs). First, the 2'-OH of the branch-point A attacks the phosphate at the 5' splice site, freeing exon 1 and forming the lariat; second, the newly freed 3'-OH of exon 1 attacks the phosphate at the 3' splice site, joining the exons and releasing the intron lariat. Some introns (group I and group II introns) catalyze these reactions on their own — Thomas Cech's discovery of self-splicing RNA in *Tetrahymena* (1982) was the first demonstration that RNA can be an enzyme.

In bacteria, transcription and translation are **coupled** — ribosomes begin translating mRNA while it is still being transcribed.

**Worked Example 4.1 — The longest-running transcript.** The human dystrophin gene (mutated in Duchenne muscular dystrophy) spans about 2.2 Mb and contains 79 exons; its mature mRNA is about 14 kb and encodes a protein of 3685 amino acids. (a) How long does Pol II take to transcribe the gene at 40 nt/s? (b) What fraction of the primary transcript survives splicing? (c) Check that the coding sequence fits within the mRNA.
1. (a) $t = 2.2\times10^{6}\ \text{nt}/40\ \text{nt s}^{-1} = 5.5\times10^{4}\ \text{s} = 15.3\ \text{h}$.
2. (b) $14\times10^{3}/2.2\times10^{6} = 0.0064$, i.e. 0.64%.
3. (c) Coding sequence: $3685\times3 + 3\ (\text{stop}) = 11\,058$ nt, which fits inside the 14-kb mRNA with about 3 kb left for the 5' and 3' untranslated regions.

**Answer:** about 15 hours per transcript (direct measurements in the 1990s gave about 16 hours), and more than 99% of the primary transcript is intron sequence discarded by splicing. One practical consequence: a gene this long cannot be delivered whole by the small AAV vectors used in gene therapy, so trials have used shortened "micro-dystrophin" genes.

**Worked Example 4.2 — From gene to protein, with an intron.** The coding strand of a toy gene (the intron is far shorter than real ones, for clarity) is
5'-ATGAAAGCT **GTGAGTAACTAACCTTTTCCCAG** TGGGAACGTTAA-3'
where the bold stretch is an intron. (a) Write the template strand. (b) Write the pre-mRNA and the mature mRNA. (c) Translate the mature mRNA. (d) What protein would be made if the intron were not removed?
1. (a) The template is the complement, written 3'→5' under the coding strand: 3'-TACTTTCGA CACTCATTGATTGGAAAAGGGTC ACCCTTGCAATT-5'.
2. (b) The pre-mRNA has the coding-strand sequence with U for T: 5'-AUGAAAGCU GUGAGUAACUAACCUUUUCCCAG UGGGAACGUUAA-3'. The intron begins with GU and ends with AG, contains a candidate branch-point A (in the CUAAC stretch) and a pyrimidine-rich tract (CCUUUUCCC) just before the 3' splice site — the features the spliceosome recognizes.
3. Splicing joins the exons: 5'-AUG AAA GCU UGG GAA CGU UAA-3' (a cap and poly(A) tail would also be added).
4. (c) Reading codons from AUG: Met–Lys–Ala–Trp–Glu–Arg–stop.
5. (d) Retained intron: AUG AAA GCU **GUG AGU AAC UAA** → Met–Lys–Ala–Val–Ser–Asn–stop.

**Answer:** the spliced mRNA encodes the hexapeptide Met-Lys-Ala-Trp-Glu-Arg; failure to splice gives a different, truncated product because the intron contains an in-frame stop codon. Many disease-causing splice-site mutations act exactly this way, and cells destroy many such mRNAs by **nonsense-mediated decay**, which recognizes stop codons lying upstream of exon–exon junctions.

## 5. The Genetic Code

The sequence of mRNA is read in **codons** of three nucleotides; 4³ = 64 codons specify 20 amino acids plus stop signals. Deciphered between 1961 and 1966 (Nirenberg and Matthaei used synthetic poly-U RNA, which produced polyphenylalanine — UUU codes for Phe; Khorana, Holley; Nobel 1968).

*Why three?* With an alphabet of 4 letters, words of length $n$ give $4^{n}$ distinct words. Singlets give 4 and doublets only 16, both fewer than 20 amino acids; triplets give 64, enough with room to spare. The minimum word length is the smallest integer $n$ satisfying
$$4^{n}\ge 20 \quad\Longleftrightarrow\quad n \ge \log_4 20 = \frac{\ln 20}{\ln 4} = 2.16 \quad\Longrightarrow\quad n = 3$$
This is only a counting argument; the experimental proof that the code really is a triplet came from genetics (below).

How the code was cracked: after poly-U, Nirenberg, Matthaei and Severo Ochoa's group used random copolymers of known base composition to deduce codon compositions; Har Gobind Khorana synthesized RNAs with defined repeating sequences (for example UCUCUC... gives alternating Ser-Leu); and in 1964 Nirenberg and Philip Leder's **triplet binding assay** showed which aminoacyl-tRNA sticks to ribosomes in the presence of a single trinucleotide, assigning codons one at a time. Robert Holley determined the first complete tRNA sequence (yeast alanine tRNA) in 1965.

### Properties
- **Triplet:** shown by Crick and Brenner (1961) using frameshift mutations.
- **Non-overlapping** and read without punctuation from a fixed start point (**reading frame**).
- **Degenerate (redundant):** most amino acids have multiple codons (Leu, Ser, Arg have six; Met and Trp only one). Synonymous codons often differ in the third position (**wobble**).
- **Start codon:** **AUG** (methionine; N-formylmethionine in bacteria).
- **Stop codons:** **UAA, UAG, UGA** (no tRNA; recognized by release factors).
- **Nearly universal:** the same code in almost all organisms — strong evidence for common ancestry. Minor variations exist (e.g. in vertebrate mitochondria UGA codes for Trp and AGA/AGG are stops; some ciliates read UAA/UAG as Gln).

The Crick–Brenner logic deserves a closer look. They used mutations in the *rII* gene of phage T4 caused by acridine dyes, which insert or delete single bases. One "+" mutation knocked out the gene; combining it with a nearby "−" mutation restored function (the frame is shifted only between the two sites); and, crucially, combining *three* "+" mutations (or three "−") also restored function, while two "+" did not. Only a code read in groups of three, from a fixed starting point, predicts that three single-base shifts cancel.

**Reading frames.** Any stretch of double-stranded DNA can be read in **six frames** — three starting positions on each strand. An **open reading frame (ORF)** is a stretch that begins with a start codon and runs for many codons before reaching a stop codon in the same frame. Genes are found computationally by searching for long ORFs.

**Worked Example 5.1 — How long would a random ORF be?** Assume a random sequence with all four bases equally likely. (a) What is the average number of codons read before a stop codon appears? (b) What is the probability that 100 consecutive codons contain no stop? 300 codons? (c) About how many stop-free stretches of at least 100 codons would 1 Mb of random DNA contain, counting all six frames?
1. Three of the 64 codons are stops, so each codon is a stop with probability $p = 3/64 = 0.0469$.
2. (a) The number of codons up to and including the first stop follows a geometric distribution with mean $1/p = 64/3 = 21.3$ codons.
3. (b) $P(\text{no stop in } k \text{ codons}) = (61/64)^{k}$: for $k = 100$, $(61/64)^{100} = 8.2\times10^{-3}$; for $k = 300$, $(61/64)^{300} = 5.6\times10^{-7}$.
4. (c) 1 Mb gives about $10^{6}/3 \approx 3.3\times10^{5}$ codon positions per frame, $2.0\times10^{6}$ over six frames. A stop-free stretch of 100 codons begins after each stop codon with probability $8.2\times10^{-3}$, so the expected number is $(2.0\times10^{6})(3/64)(8.2\times10^{-3}) \approx 770$.

**Answer:** (a) about 21 codons; (b) 0.8% for 100 codons and about one in two million for 300 codons; (c) roughly 770 open stretches of 100+ codons arise by chance in 1 Mb. A typical protein of 300–400 amino acids therefore stands out clearly from random sequence, but short ORFs do not, which is why gene-finding programs also use codon-usage statistics, splice signals, conservation between species and RNA evidence. Real genomes are not random: AT-rich genomes contain more stop codons (all three are AT-rich) and so have shorter chance ORFs.

### Codon table (complete standard code)

| Amino acid | Codons |
|---|---|
| Phe (F) | UUU, UUC |
| Leu (L) | UUA, UUG, CUU, CUC, CUA, CUG |
| Ile (I) | AUU, AUC, AUA |
| Met (M) / start | AUG |
| Val (V) | GUU, GUC, GUA, GUG |
| Ser (S) | UCU, UCC, UCA, UCG, AGU, AGC |
| Pro (P) | CCU, CCC, CCA, CCG |
| Thr (T) | ACU, ACC, ACA, ACG |
| Ala (A) | GCU, GCC, GCA, GCG |
| Tyr (Y) | UAU, UAC |
| His (H) | CAU, CAC |
| Gln (Q) | CAA, CAG |
| Asn (N) | AAU, AAC |
| Lys (K) | AAA, AAG |
| Asp (D) | GAU, GAC |
| Glu (E) | GAA, GAG |
| Cys (C) | UGU, UGC |
| Trp (W) | UGG |
| Arg (R) | CGU, CGC, CGA, CGG, AGA, AGG |
| Gly (G) | GGU, GGC, GGA, GGG |
| Stop | UAA, UAG, UGA |

The counts add up: 2 + 6 + 3 + 1 + 4 + 6 + 4 + 4 + 4 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 2 + 1 + 6 + 4 = 61 sense codons, plus 3 stops = 64. The code is not arranged at random. Every codon with U in the second position encodes a hydrophobic amino acid (Phe, Leu, Ile, Met, Val), and chemically similar amino acids tend to share codons that differ by one base, so many point mutations and translation errors substitute a similar amino acid. Two rare amino acids extend the code by recoding a stop codon in special contexts: **selenocysteine** (UGA, in some proteins of all three domains of life, including about 25 human selenoproteins) and **pyrrolysine** (UAG, in some archaea and bacteria).

## 6. Translation

### Key players
- **mRNA:** the template, read 5'→3'.
- **tRNA:** adaptor molecules (~76 nt, cloverleaf secondary structure, L-shaped 3D structure) with an **anticodon** that pairs with the codon (antiparallel) and the amino acid attached to the 3' CCA end. **Aminoacyl-tRNA synthetases** (one per amino acid) attach the correct amino acid using ATP — the true "translators" of the code, with proofreading. **Wobble** pairing (e.g. G–U, and inosine in anticodons) allows one tRNA to read several codons, so cells need fewer than 61 tRNA types.
- **Ribosome:** large and small subunits (bacteria 70S = 50S + 30S; eukaryotes 80S = 60S + 40S). Three tRNA sites: **A** (aminoacyl), **P** (peptidyl), **E** (exit). The **peptidyl transferase** activity is catalyzed by rRNA — the ribosome is a ribozyme.

The tRNA idea was predicted before it was found: in 1955 Crick proposed an "adaptor hypothesis", arguing that amino acids cannot recognize nucleotide triplets directly, so some small nucleic-acid adaptor must carry each amino acid to the template. A crucial 1962 experiment showed that the ribosome trusts the adaptor, not the amino acid: chemically converting the cysteine on Cys-tRNA into alanine produced proteins with alanine wherever cysteine codons occurred. Once a tRNA is charged, the ribosome checks only codon–anticodon pairing, so all specificity for the amino acid rests on the synthetases.

**Wobble rules.** Crick proposed in 1966 that the first (5') base of the anticodon, which pairs with the third (3') base of the codon, has geometric freedom to form non-standard pairs:

| 5' base of anticodon | Can pair with 3' base of codon |
|---|---|
| C | G only |
| A | U only (A is rare at this position; it is usually converted to I) |
| G | C or U |
| U | A or G |
| I (inosine) | U, C or A |

For example, a tRNA with anticodon 5'-IGC-3' reads the alanine codons GCU, GCC and GCA, and a second alanine tRNA with 5'-CGC-3' covers GCG. Human mitochondria manage the whole code with only 22 tRNAs, using extended wobble.

### Stages
1. **Initiation:**
   - Bacteria: the small subunit binds the **Shine–Dalgarno sequence** (AGGAGG) upstream of AUG; initiator fMet-tRNA enters the P site; the large subunit joins (GTP-dependent, with initiation factors).
   - Eukaryotes: the small subunit binds the 5' cap and **scans** to the first AUG in a good context (Kozak sequence).
2. **Elongation** (repeated): an aminoacyl-tRNA enters the A site (EF-Tu/eEF1 with GTP); the peptide bond forms (the growing chain transfers from the P-site tRNA to the A-site amino acid); the ribosome **translocates** one codon (EF-G/eEF2, GTP), moving tRNAs from A→P→E. Rate ~15–20 amino acids/s in bacteria, ~5–6/s in eukaryotes.
3. **Termination:** a stop codon in the A site is recognized by **release factors**; the polypeptide is hydrolyzed from the tRNA and released; the ribosome dissociates.

Each peptide bond costs ~4 high-energy phosphate bonds (2 for aminoacylation, 1 each for EF-Tu and EF-G). Multiple ribosomes can translate one mRNA simultaneously (**polysomes**).

The Shine–Dalgarno sequence works by base pairing: it is complementary to a sequence near the 3' end of 16S rRNA, so the rRNA itself positions the start codon in the P site. Proteins grow from the **N-terminus to the C-terminus**, because each new amino acid is added to the carboxyl end of the chain; the 5'→3' direction of reading the mRNA thus corresponds to the N→C direction of the protein. The peptide-bond-forming center of the large subunit contains no protein within about 1.8 nm of the reaction site — shown by the atomic structures of ribosomes published in 2000 (Venkatraman Ramakrishnan, Thomas Steitz and Ada Yonath; Nobel Chemistry 2009).

### Post-translational events
Folding (with chaperones), proteolytic cleavage (e.g. proinsulin → insulin), chemical modifications (phosphorylation, glycosylation, acetylation, ubiquitination, lipidation), and targeting: a hydrophobic **signal peptide** at the N-terminus directs ribosomes to the ER via the signal recognition particle (Günter Blobel, Nobel 1999).

### Worked example
DNA template strand: 3'-TAC GGA CTT ATC-5'
mRNA: 5'-AUG CCU GAA UAG-3'
Protein: Met–Pro–Glu–(stop)

**Worked Example 6.1 — The cost, speed and accuracy of making a protein.** A bacterium makes a protein of 400 amino acids. Translation errors occur at about $10^{-4}$ per codon (the range commonly quoted is $10^{-3}$ to $10^{-4}$). (a) How many high-energy phosphate bonds are consumed in elongation? (b) How long does synthesis take at 20 amino acids/s, and in a eukaryote at 6/s? (c) What fraction of the finished molecules contain no amino-acid error, at error rates of $10^{-4}$ and $10^{-3}$? (d) An *E. coli* cell contains roughly $3\times10^{6}$ protein molecules averaging about 300 amino acids. Estimate the phosphate bonds spent on protein synthesis per cell division.
1. (a) 400 amino acids are joined by 399 peptide bonds: $399\times4 = 1596 \approx 1.6\times10^{3}$ bonds (initiation and termination add a few more).
2. (b) $400/20 = 20$ s in the bacterium; $400/6 = 67$ s in a eukaryote.
3. (c) If each codon is read correctly with probability $1-\varepsilon$, the probability that all 400 are correct is $(1-\varepsilon)^{400}$: $(1-10^{-4})^{400} = 0.96$; $(1-10^{-3})^{400} = 0.67$.
4. (d) Peptide bonds: $(3\times10^{6})(300) = 9\times10^{8}$; phosphate bonds: $4\times9\times10^{8} = 3.6\times10^{9}$.

**Answer:** (a) about 1600 phosphate bonds; (b) 20 s versus about 67 s; (c) 96% versus 67% error-free; (d) a few billion phosphoanhydride bonds per division — protein synthesis is the largest single item in a growing bacterium's energy budget. Part (c) shows why translation error rates near $10^{-4}$ are needed: at $10^{-3}$, a third of all long proteins would carry a mistake, and the error rate sets a practical upper limit on protein length.

### Drugs and toxins that target the central dogma

Differences between bacterial and eukaryotic machinery make the central dogma a rich source of selective drugs.

| Agent | Target | Effect |
|---|---|---|
| Fluoroquinolones (ciprofloxacin) | Bacterial DNA gyrase and topoisomerase IV | Block replication, trap enzyme–DNA breaks |
| Rifampicin | β subunit of bacterial RNA polymerase | Blocks transcription; a key tuberculosis drug |
| α-Amanitin | Eukaryotic RNA polymerase II | Blocks mRNA synthesis (death-cap poisoning) |
| Streptomycin and other aminoglycosides | Bacterial 30S subunit | Misreading of codons, inhibition of initiation |
| Tetracyclines | Bacterial 30S subunit, A site | Block aminoacyl-tRNA binding |
| Chloramphenicol | Bacterial 50S peptidyl transferase center | Blocks peptide-bond formation |
| Macrolides (erythromycin) | Bacterial 50S exit tunnel | Stall elongation of the nascent chain |
| Puromycin (laboratory tool) | A site of all ribosomes | Mimics aminoacyl-tRNA; premature release of the chain |
| Cycloheximide (laboratory tool) | Eukaryotic 60S subunit | Blocks elongation |
| Diphtheria toxin | Eukaryotic eEF2 | Chemically modifies it (ADP-ribosylation), halting translocation |
| Zidovudine (AZT) and related nucleoside analogs | HIV reverse transcriptase | Chain termination (no 3'-OH) |

Some side effects follow directly from molecular biology: mitochondria descend from bacteria and have bacterial-like 70S-type ribosomes, which helps explain why some antibiotics that target the ribosome (for example linezolid, chloramphenicol and aminoglycosides) can harm human cells at high or prolonged doses.

## 7. Mutations

A **mutation** is a heritable change in DNA sequence.

### Point mutations (single-base substitutions)
- **Silent (synonymous):** codon change without amino acid change (GAA → GAG, both Glu).
- **Missense:** different amino acid (sickle-cell: GAG → GTG, Glu6Val in β-globin).
- **Nonsense:** creates a stop codon → truncated protein (some cystic fibrosis and Duchenne muscular dystrophy alleles).
- **Transitions** (purine↔purine, pyrimidine↔pyrimidine) are more common than **transversions**.

The transition bias is stronger than it first looks. For any base there is one possible transition but two possible transversions, so of the 12 possible directed substitutions 4 are transitions and 8 are transversions; if all were equally likely, transversions would outnumber transitions two to one. In fact, among human single-nucleotide variants, transitions outnumber transversions about two to one, so per possible pathway a transition is roughly four times as frequent. Chemistry explains much of this: deamination of 5-methylcytosine (C→T), tautomeric mispairs (such as G pairing with T) and many polymerase errors all produce transitions.

**Worked Example 7.1 — How forgiving is the genetic code?** Consider every possible single-base substitution in every one of the 61 sense codons, assuming each substitution is equally likely. (a) How many substitutions are there? (b) What fractions are synonymous, missense and nonsense? (c) How does this depend on codon position?
1. (a) Each codon has 3 positions and each can change to 3 other bases: $61\times3\times3 = 549$ substitutions.
2. (b) Going through the codon table (a short computer program does this reliably) gives 134 synonymous, 392 missense and 23 nonsense substitutions: $134/549 = 24.4\%$, $392/549 = 71.4\%$, $23/549 = 4.2\%$.
3. (c) By position: first position — 8 synonymous out of 183 (all from the six-codon Leu and Arg families, e.g. UUA ↔ CUA); second position — none synonymous out of 183; third position — 126 synonymous out of 183, or 69%.

**Answer:** about one-quarter of random point mutations in coding sequence are silent, 71% change an amino acid and 4% create a stop codon. The third codon position is mostly "free", which is why third positions evolve fastest and why comparing synonymous with non-synonymous substitution rates is a standard test for natural selection on a gene.

### Insertions and deletions (indels)
If not a multiple of three, they cause a **frameshift**, changing every downstream codon (often creating a premature stop). Example: THE CAT ATE THE RAT → deletion of one letter → THE ATA TET HER AT. The most common cystic fibrosis mutation (ΔF508) is an in-frame deletion of three nucleotides, removing one phenylalanine.

### Larger-scale changes
Duplications, inversions, translocations (e.g. the Philadelphia chromosome t(9;22) creating the BCR-ABL fusion in chronic myeloid leukemia), copy-number variants, **trinucleotide repeat expansions** (Huntington's disease — CAG repeats; fragile X syndrome — CGG repeats), and whole-chromosome aneuploidies.

### Causes
- **Spontaneous:** replication errors, tautomeric shifts, depurination, deamination of cytosine (to uracil) and 5-methylcytosine (to thymine — making CpG sites mutation hotspots).
- **Induced (mutagens):** UV light (thymine dimers), ionizing radiation (strand breaks), chemicals (alkylating agents, base analogs, intercalators like ethidium bromide, benzo[a]pyrene), some viruses. The **Ames test** screens chemicals for mutagenicity using *Salmonella* strains.

The Ames test (developed by Bruce Ames in the 1970s) uses *Salmonella* strains that carry a mutation preventing them from making histidine. Spread on plates without histidine, only bacteria that acquire a second, **reverting** mutation can grow into colonies; a chemical that raises the number of revertant colonies above the spontaneous background is a mutagen. A liver-enzyme extract is added because many compounds, such as benzo[a]pyrene, become mutagenic only after metabolic activation in the body.

Mutations are the ultimate source of genetic variation for evolution; most are neutral or harmful, a few beneficial. Mutations in **germ-line** cells can be inherited; **somatic** mutations affect only the individual (e.g. cancer). Each human is born with ~50–100 new mutations not present in either parent. This follows from the measured germ-line point-mutation rate of about $1.2\times10^{-8}$ per base pair per generation: $(1.2\times10^{-8})(6.2\times10^{9}) \approx 74$ new single-nucleotide mutations per child. Most come from the father, and their number rises with paternal age (by roughly two per year), because sperm precursors keep dividing throughout adult life whereas a woman's oocytes are formed before birth.

**Mutations are random with respect to need.** In 1943 Salvador Luria and Max Delbrück grew many parallel cultures of *E. coli* and counted bacteria resistant to phage T1. If resistance were *induced* by exposure to the phage, every culture would show a similar, Poisson-distributed number of resistant cells. Instead the counts fluctuated wildly — most cultures had few, a few had "jackpots" of hundreds — exactly as expected if mutations arise spontaneously during growth, before exposure, so that an early mutation leaves many resistant descendants. Joshua and Esther Lederberg's **replica plating** (1952) confirmed it: resistant colonies could be found at the same positions on replicas of a plate that had never seen the selective agent. Luria and Delbrück shared the 1969 Nobel Prize with Hershey.

## 8. Regulation of Gene Expression

Every cell has (almost) the same genome, yet a neuron differs from a liver cell because they express different genes. Regulation can occur at every step.

### Prokaryotes: operons
An **operon** is a cluster of genes transcribed together from one promoter, controlled by an **operator** (François Jacob and Jacques Monod, 1961; Nobel 1965 with André Lwoff).

**The lac operon** (*E. coli*; genes *lacZ* — β-galactosidase, *lacY* — permease, *lacA* — transacetylase): an **inducible** operon for lactose catabolism.
- **No lactose:** the *lacI* repressor binds the operator, blocking transcription.
- **Lactose present:** allolactose (an isomer) binds the repressor, which releases the operator → transcription (negative control).
- **Glucose present:** even with lactose, transcription is low — **catabolite repression**. When glucose is low, cAMP rises; the cAMP–CAP (catabolite activator protein) complex binds near the promoter and strongly activates transcription (positive control). Result: bacteria prefer glucose, using lactose only when glucose runs out (**diauxic growth**).

Jacob and Monod deduced this logic from genetics alone. Mutants lacking a working repressor (*lacI⁻*) or with a damaged operator (*lacO*ᶜ, "operator-constitutive") expressed the enzymes all the time (**constitutively**). In partial diploids carrying a second copy of the lac region on a plasmid (the F′ factor), a normal *lacI⁺* gene restored regulation of *both* copies — the repressor is a diffusible product acting *in trans* — whereas *lacO*ᶜ made constitutive only the genes on its own DNA molecule, acting *in cis*. The repressor itself was isolated in 1966 by Walter Gilbert and Benno Müller-Hill, who found only about ten molecules per cell. Laboratory work uses IPTG, a sulfur-containing lactose analog that binds the repressor but is not broken down by β-galactosidase, as a stable inducer.

*Derivation: how much repression does a repressor give?* Treat repressor binding to the operator as a simple equilibrium, $\text{R} + \text{O} \rightleftharpoons \text{RO}$, with dissociation constant $K_d = [\text{R}][\text{O}]/[\text{RO}]$. The fraction of time the operator is free (and so available for transcription) is
$$p_{\text{free}} = \frac{[\text{O}]}{[\text{O}] + [\text{RO}]} = \frac{1}{1 + [\text{R}]/K_d} = \frac{K_d}{K_d + [\text{R}]}$$
The inducer works by raising the repressor's $K_d$ for the operator. A useful conversion: one molecule in a volume $V$ has concentration $1/(N_A V)$; for an *E. coli* cell of about 1 fL ($10^{-15}$ L) this is $1/(6.022\times10^{23}\times10^{-15}\ \text{L}) = 1.66\times10^{-9}$ M, so in a bacterium "one molecule per cell" is about 1.7 nM.

**Worked Example 8.1 — Modeling the lac switch.** An *E. coli* cell (1.0 fL) contains 10 repressor tetramers. Take $K_d = 0.10$ nM for repressor–operator binding without inducer (an illustrative value; measured affinities depend strongly on salt and conditions), and assume inducer raises $K_d$ a thousandfold. (a) What fraction of time is the operator free without inducer? (b) With inducer? (c) What induction ratio does the model predict?
1. Repressor concentration: $[\text{R}] = 10\times1.66\ \text{nM} = 16.6$ nM.
2. (a) $p_{\text{free}} = 0.10/(0.10 + 16.6) = 6.0\times10^{-3}$ — the operator is free 0.6% of the time, a 167-fold repression relative to a free promoter.
3. (b) With inducer, $K_d = 100$ nM: $p_{\text{free}} = 100/(100 + 16.6) = 0.86$.
4. (c) Induction ratio: $0.86/0.0060 \approx 143$.

**Answer:** about 0.6% free without inducer and 86% with it, a predicted induction of about 140-fold. The real operon is induced about a thousandfold, more than this simple model gives, because the repressor tetramer can bind the main operator and one of two auxiliary operators at once, looping the DNA between them and raising its effective local concentration. The calculation also shows why very few repressor molecules suffice: the operator is a single site, so a nanomolar-scale concentration with a sub-nanomolar $K_d$ keeps it occupied almost all the time.

**The trp operon:** a **repressible** operon for tryptophan synthesis — tryptophan (corepressor) activates the repressor, turning genes off when tryptophan is abundant; **attenuation** provides finer control by coupling translation of a leader peptide to transcription termination. The leader peptide contains two adjacent Trp codons. When tryptophan (and hence charged Trp-tRNA) is plentiful, the ribosome translates the leader quickly, and the mRNA behind it folds into a terminator hairpin that stops transcription. When tryptophan is scarce, the ribosome stalls at the Trp codons, the mRNA folds into an alternative "antiterminator" structure instead, and the polymerase continues into the structural genes. Attenuation, worked out by Charles Yanofsky and colleagues, works only because bacterial transcription and translation are coupled.

### Eukaryotes: multiple levels
1. **Chromatin structure:** histone **acetylation** (by HATs) loosens chromatin and promotes transcription; deacetylation (HDACs) represses. Histone methylation can activate or repress depending on the residue. **DNA methylation** at CpG sites (in promoters) generally silences genes.
2. **Transcriptional control** (the most important level): combinations of **transcription factors** binding promoters and **enhancers/silencers**; **combinatorial control** allows a limited number of factors to specify many expression patterns. Master regulators (e.g. MyoD for muscle; Hox genes for body-plan segments) can switch cell fates.
3. **RNA processing:** alternative splicing, RNA editing (e.g. apolipoprotein B mRNA C→U editing produces a shorter protein in intestine).
4. **mRNA transport and stability:** mRNA half-lives range from minutes to days (AU-rich elements promote decay).
5. **Translational control:** initiation factors (phosphorylation of eIF2 in stress), iron-responsive elements (ferritin), **microRNAs** (~22 nt; bind 3' UTRs to repress translation or trigger decay; discovered in *C. elegans* — lin-4 by Victor Ambros and Gary Ruvkun, Nobel Medicine 2024) and siRNAs.
6. **Post-translational control:** protein modification, localization, and degradation (ubiquitin–proteasome system).

Transcription factors typically have a **DNA-binding domain** that recognizes a short sequence (often 6–12 bp) and a separate **activation domain** that recruits coactivators, Mediator or chromatin-modifying enzymes. Familiar DNA-binding motifs include the helix-turn-helix, the zinc finger, the leucine zipper and the helix-loop-helix. The striking demonstration that cell fate can be reset by transcription factors alone came in 2006, when Shinya Yamanaka and Kazutoshi Takahashi turned mouse skin fibroblasts into **induced pluripotent stem cells** by expressing four factors (Oct4, Sox2, Klf4 and c-Myc); Yamanaka shared the 2012 Nobel Prize with John Gurdon.

**RNA interference** (Andrew Fire and Craig Mello, 1998; Nobel 2006): double-stranded RNA is cut by Dicer into ~21–23-nt fragments that are loaded into the RISC complex with an Argonaute protein; the guide strand then finds complementary mRNAs. Perfect complementarity (typical of siRNAs) leads to cleavage; partial pairing through a 7–8-nt "seed" region (typical of animal miRNAs) leads to translational repression and decay. A single miRNA can therefore regulate hundreds of targets.

*Derivation: how fast can expression change?* Let $m$ be the number of mRNA molecules of a gene per cell, made at a constant rate $k$ (molecules per unit time) and degraded with first-order rate constant $\gamma$:
$$\frac{dm}{dt} = k - \gamma m$$
At steady state $dm/dt = 0$, so $m^{*} = k/\gamma$. Starting from $m = 0$ when the gene is switched on, the solution is
$$m(t) = \frac{k}{\gamma}\left(1 - e^{-\gamma t}\right),\qquad \gamma = \frac{\ln 2}{t_{1/2}}$$
and after the gene is switched off, $m(t) = m^{*}e^{-\gamma t}$. Both approach their final values with the same time constant $1/\gamma$: the time to reach 90% of the change is $t_{90} = \ln 10/\gamma = 3.32\,t_{1/2}$. The striking consequence is that **the speed of a response is set by the degradation rate, not the synthesis rate**: increasing $k$ raises the final level but does not make the cell get there faster. Proteins obey the same equation, $dp/dt = k_p m - \gamma_p p$, where for stable proteins $\gamma_p$ is set mainly by dilution as the cell grows and divides.

**Worked Example 8.2 — Turning a gene on.** A bacterial gene is switched on and transcribed at 2.0 mRNA molecules per minute; the mRNA half-life is 5.0 min. (a) What is the steady-state number of mRNAs per cell? (b) How long until 90% of that level is reached? (c) How would (b) change for a mammalian mRNA with a 10-h half-life?
1. $\gamma = \ln 2/5.0\ \text{min} = 0.139\ \text{min}^{-1}$.
2. (a) $m^{*} = k/\gamma = 2.0/0.139 = 14.4$ molecules.
3. (b) $t_{90} = \ln 10/\gamma = 2.303/0.139 = 16.6$ min.
4. (c) $t_{90} = 3.32\times10\ \text{h} = 33$ h.

**Answer:** about 14 mRNA molecules per cell, reached (to 90%) in about 17 minutes. With a 10-hour half-life, the same change takes about 33 hours. Short-lived mRNAs (bacterial half-lives are typically a few minutes; in one large 2011 study of mouse cells the median mRNA half-life was about 9 hours) let bacteria retool their metabolism within a generation, and short half-lives are characteristic of mammalian genes that must respond quickly, such as those for cytokines and transcription factors. Note also the small copy number: with only ~14 molecules, random births and deaths of individual mRNAs make expression **noisy**, so genetically identical cells in the same environment can differ markedly.

### Epigenetics
Heritable changes in gene expression that do not involve changes in DNA sequence — DNA methylation, histone modifications, chromatin remodeling and non-coding RNAs. Examples:
- **X-chromosome inactivation** in female mammals: one X is randomly silenced in each cell (Barr body), directed by the *XIST* lncRNA; calico cats' patchy coats result from this mosaicism.
- **Genomic imprinting:** certain genes are expressed only from the maternally or paternally inherited copy (*IGF2*; Prader–Willi and Angelman syndromes arise from deletions of the same region inherited from father or mother, respectively).
- Environmental influences (diet, stress, toxins) can alter epigenetic marks; the Dutch Hunger Winter (1944–45) cohort showed lasting effects associated with methylation changes.
- Epigenetic dysregulation contributes to cancer; HDAC and DNA methyltransferase inhibitors are used as drugs.

How is a methylation pattern copied? After replication, each CpG site is **hemimethylated** — the parental strand is methylated, the new strand not. The maintenance methyltransferase DNMT1, guided by the partner protein UHRF1, which recognizes hemimethylated sites, methylates the new strand, so the pattern is inherited through cell division. *De novo* methyltransferases (DNMT3A and DNMT3B) set new patterns during development. Most methylation marks are erased and reset in the early embryo and again in the germ line, which is one reason transgenerational epigenetic inheritance in mammals is limited and remains debated.

## 9. Biotechnology and Genetic Engineering

- **Restriction enzymes** (Arber, Nathans and Smith, Nobel 1978) cut DNA at specific sequences (EcoRI: G^AATTC), often leaving "sticky ends".
- **Recombinant DNA** (Cohen and Boyer, 1973): genes inserted into plasmid vectors and cloned in bacteria. **Human insulin** produced in *E. coli* (approved 1982) was the first recombinant drug; others include growth hormone, clotting factors, erythropoietin, hepatitis B vaccine and monoclonal antibodies.
- **Polymerase chain reaction (PCR)** (Kary Mullis, 1983; Nobel 1993): repeated cycles of denaturation (~95 °C), primer annealing (~50–65 °C) and extension (~72 °C, heat-stable *Taq* polymerase) double the target DNA each cycle — 30 cycles give ~10⁹ copies. **RT-qPCR** detects RNA viruses (COVID-19 tests).
- **Gel electrophoresis** separates DNA fragments by size (DNA is negatively charged and migrates toward the positive electrode).
- **DNA sequencing:** Sanger dideoxy chain-termination method (1977; Sanger's second Nobel, 1980); **next-generation sequencing** (Illumina sequencing-by-synthesis) and long-read technologies (PacBio, Oxford Nanopore). The **Human Genome Project** (1990–2003) cost about 3 billion US dollars; a human genome now costs a few hundred dollars. The telomere-to-telomere (T2T) consortium completed a gapless human genome in 2022. Humans have ~20 000 protein-coding genes — only ~1–2% of the genome codes for proteins.
- **DNA fingerprinting/profiling** (Alec Jeffreys, 1984): Jeffreys's original method detected highly variable **minisatellites** (tandem repeats of tens of base pairs) by Southern blotting; modern forensic profiling instead amplifies **short tandem repeats** (STRs, repeat units of 2–6 bp) by PCR, typing a standard panel of loci for forensics and paternity testing.
- **CRISPR–Cas9 genome editing** (Doudna and Charpentier, 2012; Nobel Chemistry 2020): adapted from a bacterial adaptive immune system; a guide RNA directs Cas9 nuclease to a matching DNA sequence next to a PAM motif, where it makes a double-strand break repaired by NHEJ (gene knockouts) or homology-directed repair (precise edits). Base editors and prime editors enable changes without double-strand breaks. The first CRISPR therapy (exa-cel/Casgevy, for sickle-cell disease and β-thalassemia) was approved in 2023.
- **Gene therapy:** viral vectors (AAV, lentivirus) deliver functional genes (e.g. for spinal muscular atrophy, inherited blindness, hemophilia); CAR-T cell therapy for blood cancers.
- **GMOs:** Bt crops (insect-resistant), herbicide-tolerant crops, Golden Rice (β-carotene), and gene-edited crops.
- **Ethical issues:** germline editing (the 2018 case of gene-edited babies in China was widely condemned), genetic privacy, equitable access, biosafety.

Why could insulin not simply be made by putting the human insulin gene into bacteria? Human genes contain introns, and bacteria have no spliceosome. The solution was to work from mRNA: **reverse transcriptase** copies mature, already-spliced mRNA into **complementary DNA (cDNA)**, which can be expressed in bacteria behind a bacterial promoter and Shine–Dalgarno sequence. (The first recombinant insulin was actually made from chemically synthesized genes for the A and B chains, expressed separately in *E. coli* and joined afterward.)

**Sanger sequencing in one paragraph.** DNA polymerase copies a template in the presence of normal dNTPs plus a small proportion of **dideoxynucleotides** (ddNTPs), which lack the 3'-OH and so terminate the chain wherever one is incorporated. This produces a nested set of fragments ending at every position; separated by size (today in capillaries, with a different fluorescent dye on each ddNTP), they spell out the sequence from the colors read in order of length. Next-generation methods instead read hundreds of millions of short fragments in parallel, and nanopore instruments read single long molecules by the changes in ionic current they cause as they thread through a protein pore.

### Quantitative PCR

*Derivation.* If each cycle copies a fraction $E$ (the **efficiency**, between 0 and 1) of the molecules present, then after $n$ cycles
$$N_n = N_0\,(1+E)^{n}$$
In **real-time quantitative PCR (qPCR)** a fluorescent dye or probe reports the amount of product after each cycle, and the **threshold cycle** $C_t$ is the cycle at which fluorescence crosses a fixed threshold, i.e. at which $N$ reaches a fixed value $N_T$. Setting $N_0(1+E)^{C_t} = N_T$ and taking logarithms:
$$C_t = \frac{\log_{10} N_T - \log_{10} N_0}{\log_{10}(1+E)}$$
so $C_t$ falls linearly with $\log_{10} N_0$, with slope $-1/\log_{10}(1+E)$. At perfect efficiency ($E = 1$) the slope is $-1/\log_{10}2 = -3.32$: every tenfold more starting template crosses the threshold 3.32 cycles earlier, and two samples differing by $\Delta C_t$ differ in starting amount by a factor $2^{\Delta C_t}$. Measured slopes between about −3.1 and −3.6 (efficiencies of roughly 90–110%) are usually considered acceptable.

**Worked Example 9.1 — Counting virus copies with qPCR.** (a) Compare the product of 30 cycles at 100% and at 90% efficiency, starting from one molecule. (b) In a qPCR assay with a standard curve of slope −3.32, a standard containing $1.0\times10^{6}$ copies gives $C_t = 18.0$. A patient sample gives $C_t = 28.0$. How many copies were in the sample reaction?
1. (a) $2^{30} = 1.07\times10^{9}$; $1.9^{30} = 2.3\times10^{8}$, only 21% as much — small losses per cycle compound geometrically.
2. (b) $\Delta C_t = 28.0 - 18.0 = 10.0$ cycles later, so the sample started with fewer copies by a factor $10^{10.0/3.32} = 10^{3.01} = 1.03\times10^{3}$.
3. $N_0 = 1.0\times10^{6}/1.03\times10^{3} = 9.7\times10^{2}$ copies.

**Answer:** (a) about $1.1\times10^{9}$ versus $2.3\times10^{8}$ copies; (b) roughly 970 (about $1\times10^{3}$) copies. In practice, reactions reach a plateau when primers, nucleotides or enzyme run out, which is why quantification uses $C_t$ in the exponential phase rather than the final amount of product. For RNA viruses such as SARS-CoV-2, a reverse transcription step first converts the viral RNA into cDNA (RT-qPCR).

### Restriction maps and the statistics of short sequences

In a random sequence with equal base frequencies, a particular sequence of length $\ell$ occurs on average once every $4^{\ell}$ bp: once every 256 bp for a 4-base recognition site and once every 4096 bp for a 6-base site. (Most type II restriction sites are palindromes — they read the same 5'→3' on both strands — so each site needs to be counted only once.)

**Worked Example 9.2 — EcoRI and phage λ.** The DNA of bacteriophage λ is a linear molecule of 48 502 bp. (a) How many EcoRI sites (GAATTC) would a random sequence of this length contain? (b) EcoRI actually cuts λ DNA into fragments of 21 226, 7421, 5804, 5643, 4878 and 3530 bp. How many sites are there, and do the fragments account for the whole molecule?
1. (a) Probability of the site at any position $= (1/4)^{6} = 1/4096$; expected number $= 48\,502/4096 = 11.8$.
2. (b) A linear molecule cut at $s$ sites gives $s + 1$ fragments; 6 fragments means 5 sites.
3. Sum of fragments: $21\,226 + 7421 + 5804 + 5643 + 4878 + 3530 = 48\,502$ bp ✓.

**Answer:** about 12 sites expected but only 5 present — the fragment sizes add up exactly to the genome length. Real genomes are not random: many phage and bacterial genomes contain fewer short palindromic sequences than chance predicts, a pattern usually attributed to selection by restriction–modification systems (which evolved as defenses against phages), and mammalian DNA is depleted of the dinucleotide CpG, so enzymes whose sites contain CpG (such as NotI, GC^GGCCGC) cut human DNA far more rarely than random expectation predicts. Sets of fragment sizes like these, from single and double digests, were the basis of **restriction mapping** before routine sequencing.

**Worked Example 9.3 — How unique is a CRISPR target?** A Cas9 guide RNA matches 20 nucleotides of target DNA, which must be followed by the PAM sequence NGG. (a) How many different 20-nt sequences exist? (b) How many exact chance matches to a given 20-mer are expected in the human genome, counting both strands ($6.2\times10^{9}$ positions)? (c) Off-target cutting depends mostly on the 12 nucleotides nearest the PAM (the "seed"). How many chance matches to a 12-nt seed are expected?
1. (a) $4^{20} = 1.1\times10^{12}$.
2. (b) $6.2\times10^{9}/1.1\times10^{12} = 5.6\times10^{-3}$; requiring the GG of the PAM as well multiplies by $1/16$, giving $3.5\times10^{-4}$.
3. (c) $6.2\times10^{9}/4^{12} = 6.2\times10^{9}/1.68\times10^{7} \approx 370$.

**Answer:** a 20-nt guide is, in principle, unique in the human genome — the chance of an exact random match is less than 1% — but Cas9 tolerates some mismatches, especially far from the PAM, and hundreds of sites match the seed alone. That is why guide designs are screened computationally for near-matches and why high-fidelity Cas9 variants were engineered.

**Worked Example 9.4 — From nanograms to molecules.** A student has 10 ng of a 3000-bp plasmid. (a) How many plasmid molecules is this? (b) Estimate the melting temperature of a 20-nt PCR primer containing 8 A/T and 12 G/C bases, using the Wallace rule $T_m \approx 2(\text{A}+\text{T}) + 4(\text{G}+\text{C})$ °C.
1. Molar mass of the plasmid: $3000\ \text{bp}\times650\ \text{g mol}^{-1}\,\text{bp}^{-1} = 1.95\times10^{6}$ g/mol.
2. Moles: $10\times10^{-9}\ \text{g}/1.95\times10^{6}\ \text{g/mol} = 5.13\times10^{-15}$ mol.
3. Molecules: $(5.13\times10^{-15})(6.022\times10^{23}) = 3.1\times10^{9}$.
4. (b) $T_m \approx 2(8) + 4(12) = 16 + 48 = 64$ °C.

**Answer:** about $3.1\times10^{9}$ plasmid molecules, and a primer $T_m$ of about 64 °C (annealing is usually set a few degrees below $T_m$). The Wallace rule is only a rough guide for short oligonucleotides; it captures the key chemistry — each G–C pair, with three hydrogen bonds and stronger stacking, stabilizes the duplex more than an A–T pair. For long DNA, the classic Marmur–Doty relation $T_m = 69.3 + 0.41(\%\text{GC})$ °C (in standard saline citrate buffer) gives, for 41% GC, $T_m \approx 86$ °C. DNA concentration itself is usually measured by ultraviolet absorbance: an absorbance of 1.0 at 260 nm (1 cm path) corresponds to about 50 μg/mL of double-stranded DNA.

## 10. Historical Development After the Double Helix

The two decades after 1953 turned the double helix into a mechanistic science; the decades since have turned that science into technology.

| Year | Discovery | People |
|---|---|---|
| 1955 | Adaptor hypothesis (predicts tRNA) | Francis Crick |
| 1956 | DNA polymerase I purified (Nobel 1959, shared with Severo Ochoa) | Arthur Kornberg |
| 1958 | Semiconservative replication; "On Protein Synthesis" (central dogma) | Meselson and Stahl; Crick |
| 1961 | Messenger RNA identified | Sydney Brenner, François Jacob, Matthew Meselson (and, independently, a Harvard group including Walter Gilbert and James Watson) |
| 1961 | Operon model; triplet code; poly-U → polyphenylalanine | Jacob and Monod; Crick, Brenner and colleagues; Nirenberg and Matthaei |
| 1962 | Nobel Prize for the double helix (Franklin had died in 1958) | Watson, Crick, Maurice Wilkins |
| 1965 | First tRNA sequence | Robert Holley |
| 1966 | Genetic code complete; wobble hypothesis; lac repressor isolated | Nirenberg, Khorana and others; Crick; Gilbert and Müller-Hill |
| 1968 | Okazaki fragments; Nobel for the genetic code | Reiji and Tsuneko Okazaki; Holley, Khorana, Nirenberg |
| 1970 | Reverse transcriptase; first sequence-specific (type II) restriction enzyme | Temin and Baltimore; Hamilton Smith |
| 1972–73 | First recombinant DNA molecules; cloning in bacteria | Paul Berg; Stanley Cohen and Herbert Boyer |
| 1975 | Asilomar conference on recombinant-DNA safety | — |
| 1977 | DNA sequencing (dideoxy and chemical methods); introns discovered | Frederick Sanger; Allan Maxam and Walter Gilbert; Richard Roberts and Phillip Sharp |
| 1980 | Nobel Chemistry for nucleic-acid biochemistry and sequencing | Berg; Gilbert and Sanger |
| 1982–83 | Catalytic RNA (ribozymes) (Nobel Chemistry 1989) | Thomas Cech; Sidney Altman |
| 1983–85 | PCR invented and published | Kary Mullis and colleagues |
| 1984 | Telomerase; DNA fingerprinting | Greider and Blackburn; Alec Jeffreys |
| 1987 | CRISPR repeats first noticed in *E. coli* (function unknown) | Yoshizumi Ishino and colleagues |
| 1993 | First microRNA (lin-4) | Ambros; Ruvkun |
| 1995 | First genome of a free-living organism (*Haemophilus influenzae*) | J. Craig Venter's institute (TIGR) and collaborators |
| 1998 | RNA interference (Nobel 2006) | Andrew Fire and Craig Mello |
| 2000 | Atomic structures of ribosomal subunits (Nobel Chemistry 2009) | Ramakrishnan, Steitz, Yonath |
| 2001–03 | Human genome draft and "completion" | Human Genome Project; Celera Genomics |
| 2006 | Induced pluripotent stem cells | Yamanaka and Takahashi |
| 2007 | CRISPR shown to be adaptive immunity in bacteria | Rodolphe Barrangou, Philippe Horvath and colleagues |
| 2012 | Programmable Cas9 cutting with a guide RNA (Nobel Chemistry 2020) | Jennifer Doudna and Emmanuelle Charpentier |
| 2020 | mRNA vaccines authorized against COVID-19 | — |
| 2022 | Gapless telomere-to-telomere human genome | T2T Consortium |
| 2023 | First approved CRISPR therapy; Nobel for nucleoside-modified mRNA | Casgevy; Katalin Karikó and Drew Weissman |
| 2024 | Nobel for microRNA; Nobel Chemistry for protein structure prediction and design | Ambros and Ruvkun; Demis Hassabis, John Jumper, David Baker |

Two themes run through this history. First, many central discoveries came from simple model systems — phages, *E. coli*, yeast, *Tetrahymena*, *C. elegans* — whose rapid growth and genetics made bold experiments possible. Second, each conceptual advance became a tool: restriction enzymes from studies of phage defense, PCR from the biochemistry of DNA polymerase, CRISPR from curiosity about odd repeats in bacterial genomes.

## 11. Applications in Medicine, Technology, Industry and Nature

- **Diagnostics.** PCR and RT-qPCR detect pathogens within hours; sequencing identifies outbreak strains and tracks variants; wastewater sequencing monitors community infection levels. Non-invasive prenatal testing analyzes fragments of fetal DNA circulating in the mother's blood to screen for aneuploidies such as trisomy 21. Tumor sequencing reveals targetable mutations, and "liquid biopsies" detect tumor DNA in blood.
- **Drugs that act on the central dogma.** Antibiotics target bacterial replication, transcription and translation (Section 6); antiretroviral drugs block HIV reverse transcriptase (zidovudine was the first approved HIV drug, in 1987); imatinib (approved 2001) inhibits the BCR-ABL kinase created by the Philadelphia translocation; PARP inhibitors exploit BRCA-deficient tumors.
- **RNA medicines.** Antisense oligonucleotides (nusinersen corrects *SMN2* splicing), small interfering RNA drugs (patisiran, approved in 2018, was the first), and **mRNA vaccines**, in which a lipid nanoparticle delivers an mRNA that the recipient's own ribosomes translate into a viral antigen. Replacing uridine with modified nucleosides (such as N1-methylpseudouridine) lets the mRNA avoid triggering innate immune sensors and increases translation — the work recognized by the 2023 Nobel Prize.
- **Gene and cell therapy.** AAV vectors deliver genes to non-dividing cells (retina, motor neurons, liver); lentiviral vectors integrate genes into blood stem cells or T cells (CAR-T therapy); genome editing reactivates fetal hemoglobin in sickle-cell disease.
- **Recombinant proteins.** Insulin, growth hormone, clotting factors, erythropoietin, monoclonal antibodies and vaccines are made in bacteria, yeast or mammalian cells. Industrial enzymes (in detergents, baking, brewing, textiles and biofuel production) are produced the same way.
- **Forensics and genealogy.** STR profiling identifies individuals with high confidence; genome-wide variant data underlie ancestry testing and have been used, controversially, to identify suspects through relatives.
- **Agriculture.** Insect-resistant Bt crops, gene-edited crops, marker-assisted breeding, and PCR-based detection of plant and animal pathogens; DNA testing also checks food authenticity (for example, species substitution in seafood).
- **Research tools.** Reporter genes such as green fluorescent protein (Osamu Shimomura, Martin Chalfie and Roger Tsien; Nobel Chemistry 2008) make gene expression visible in living cells; RNA sequencing measures the expression of every gene at once, even in single cells.
- **Nature.** Bacteria exchange genes by transformation, transduction (via phages) and conjugation (via plasmids) — **horizontal gene transfer**, which spreads antibiotic resistance between species. CRISPR arrays record past phage infections, a heritable immune memory. Retroviruses have left their mark in our own genome: roughly 8% of human DNA derives from ancient endogenous retroviruses, and about half of the genome derives from transposable elements of all kinds.

## 12. Connections to Other Subjects

- **Chemistry.** Phosphodiester-bond formation is a nucleophilic substitution at phosphorus driven by pyrophosphate hydrolysis; the negative charge of the phosphate backbone (its pKa is about 1) explains why DNA migrates toward the anode in electrophoresis and why it binds positively charged histones. Base pairing and stacking set duplex stability and melting temperature; the Boltzmann factor in kinetic proofreading is pure thermodynamics; repressor–operator binding is the law of mass action; ultraviolet absorbance at 260 nm (Beer–Lambert law) is how DNA is quantified.
- **Physics.** The double helix was deduced from X-ray diffraction: a helix produces the characteristic X-shaped pattern of Photograph 51, and the layer-line spacing gave the 3.4-nm pitch of the fiber form Franklin studied. Density-gradient centrifugation (Meselson–Stahl) and sedimentation coefficients (Svedberg units for ribosomes) are applications of mechanics in a centrifugal field. DNA is a semiflexible polymer with a persistence length of about 50 nm (about 150 bp), which governs how tightly it can be bent around nucleosomes and looped between regulatory sites. Optical tweezers measure the forces generated by single polymerases, and nanopore sequencing reads bases from ionic currents.
- **Mathematics and computer science.** Combinatorics explains the triplet code and the frequency of restriction sites; the geometric distribution gives chance ORF lengths; exponential growth describes PCR and replication; first-order differential equations describe gene expression; stochastic processes explain expression noise and the Luria–Delbrück jackpot distribution. Sequence alignment algorithms (Needleman–Wunsch 1970, Smith–Waterman 1981, BLAST 1990) and genome assembly are core problems of bioinformatics. In information terms, each base carries at most $\log_2 4 = 2$ bits, so the haploid human genome holds at most about $6.2\times10^{9}$ bits, roughly 775 megabytes — and DNA is now being explored as an archival data-storage medium.
- **Other areas of biology.** Genetics (Mendel's factors are DNA sequences; dominance often reflects whether half the normal protein is enough), evolution (the near-universal code supports common descent; synonymous-site differences act as **molecular clocks**), immunology (antibody genes are assembled by cutting and rejoining DNA segments), physiology (hormones such as steroids act as transcription factors) and cell biology (the nucleus, ribosomes and ER are the factory floor of the central dogma).
- **Astronomy and astrobiology.** The **RNA world** hypothesis (named by Walter Gilbert in 1986) proposes that early life used RNA both to store information and to catalyze reactions, before DNA and proteins took over; ribozymes, the RNA catalytic core of the ribosome and RNA-derived coenzymes are seen as molecular fossils of that era. Nucleobases such as uracil have been detected in carbonaceous meteorites and in samples returned from the asteroid Ryugu (reported 2023), showing that some building blocks of nucleic acids form abiotically in space. Searches for life elsewhere ask whether alien biochemistry would use the same molecules or an entirely different information carrier.

## 13. Common Misconceptions

- **"The mRNA has the same sequence as the template strand."** The mRNA is *complementary* to the template strand; it matches the *coding* strand, with U in place of T. Mixing up the strands produces the wrong protein in exercises like Worked Example 4.2.
- **"DNA polymerase can synthesize the lagging strand 3' → 5'."** No known polymerase extends a chain at its 5' end. The lagging strand is made 5'→3' in short pieces, which as a whole grow in the direction opposite to fork movement; the 5'→3' rule follows from the chemistry of proofreading (Section 2).
- **"Most of our DNA codes for proteins."** Only about 1–2% of the human genome is protein-coding sequence. The rest includes introns, regulatory elements, non-coding RNA genes, repeated sequences and transposon-derived DNA (about half of the genome).
- **"Non-coding DNA is all useless junk" — or, the opposite, "all of it is functional."** Both extremes are wrong. Some non-coding DNA is clearly functional (promoters, enhancers, ncRNA genes, telomeres, centromeres), but much of it shows no evolutionary constraint, and organisms with very similar biology can differ several-fold in genome size.
- **"One gene makes one protein."** Beadle and Tatum's "one gene–one enzyme" idea (1941) was a landmark, but alternative splicing, alternative promoters and RNA editing let one gene encode several proteins, and thousands of genes encode functional RNAs that are never translated.
- **"A bigger genome means a more complex organism."** Bread wheat's genome (about 16 Gb) is roughly five times the size of ours, and many amphibians, lungfishes and plants have far larger genomes still; much of the difference is repetitive DNA (the "C-value paradox").
- **"The genetic code is the same thing as a person's genome."** The code is the *dictionary* mapping codons to amino acids and is shared by nearly all life; the genome is the specific *text* of an individual or species. Saying someone has "a unique genetic code" really means a unique genome.
- **"Mutations happen because an organism needs them."** The Luria–Delbrück fluctuation test and replica plating showed that mutations arise randomly, before selection; the environment then selects among them. Stress can raise overall mutation rates in some bacteria, but it does not direct mutations to useful genes.
- **"All mutations are harmful."** Most are neutral (about a quarter of coding substitutions are silent, and most of the genome is not under strong constraint), many are mildly harmful, and a few are beneficial — the basis of adaptation.
- **"Ribosome subunits add up: 50S + 30S = 80S."** Svedberg units measure sedimentation rate, which depends on shape as well as mass, so they are not additive: 50S + 30S = 70S, and 60S + 40S = 80S.
- **"Different cell types contain different genes."** With rare exceptions (such as rearranged antibody genes in lymphocytes), all nucleated cells of an individual carry the same genome; they differ in which genes are *expressed*. Cloning of animals from adult nuclei (Dolly the sheep, 1996) and induced pluripotent stem cells demonstrated this directly.
- **"Every AUG is a start codon."** Only the AUG that the ribosome uses to begin (usually the first in a good context, in eukaryotes) is a start codon; internal AUGs simply encode methionine.
- **"mRNA vaccines alter your DNA."** The vaccine mRNA stays in the cytoplasm, where ribosomes translate it, and is degraded within days; it does not enter the nucleus and human cells do not reverse-transcribe it into the genome.
- **"Epigenetic changes are permanent and always passed to children."** Most epigenetic marks are dynamic and most are erased and reset in the germ line and early embryo; well-documented transgenerational epigenetic inheritance is common in plants and some animals, but limited and debated in mammals.
- **"PCR makes an exact copy forever, doubling indefinitely."** Each cycle at most doubles the target, efficiencies are below 100%, reactions plateau as reagents run out, and *Taq* polymerase, which lacks proofreading, introduces occasional errors — high-fidelity polymerases are used when exact sequence matters.

## 14. Practice Problems

1. (Easy, conceptual) Explain why the lagging strand needs many RNA primers while the leading strand needs only one per origin, and why DNA ligase is needed far more often on the lagging strand.
2. (Easy) In a Meselson–Stahl experiment, *E. coli* grown on ¹⁵N are transferred to ¹⁴N medium. What fractions of DNA molecules are hybrid and light after 3 generations under semiconservative replication? What would the conservative and dispersive models predict?
3. (Easy) A DNA template strand reads 3'-TACCGTAAGGTCTGCACT-5'. Write the coding strand, the mRNA and the encoded peptide.
4. (Medium) Using the mRNA from Problem 3 (numbering its nucleotides 1–18 from the 5' end), classify each mutation and give the resulting peptide: (a) C9 → U; (b) C10 → U; (c) insertion of a G between nucleotides 3 and 4; (d) deletion of nucleotides 4–6.
5. (Medium) *E. coli* has a 4.64-Mb chromosome and, under certain conditions, forks move at 800 nt/s. (a) How long does one round of replication take? (b) How can the cells nevertheless divide every 25 minutes? (c) Predict the ratio of origin-proximal to terminus-proximal gene copies in such a culture.
6. (Medium) Human chromosome 1 contains about 248 Mb. With forks moving at 30 nt/s, how long would replication take from a single central origin? How long if origins spaced every 100 kb all fired at once, and how many origins would that be? Why does real S phase take about 8 hours?
7. (Medium) A eukaryotic protein has a mass of 50 kDa. Taking 110 Da as the average mass of an amino-acid residue, estimate (a) the number of amino acids, (b) the minimum length of coding sequence (including the stop codon), (c) the time to translate it at 6 amino acids/s, and (d) the number of high-energy phosphate bonds used in elongation.
8. (Medium) In an RT-qPCR experiment, a gene's transcript crosses the threshold at $C_t = 24.0$ in treated cells and $C_t = 27.3$ in untreated cells (with equal amounts of reference RNA). By what factor is the transcript more abundant in treated cells if the efficiency is 100%? If it is 95%?
9. (Medium) HindIII recognizes AAGCTT. (a) How many sites would you expect in the 48 502-bp λ genome if the sequence were random? (b) HindIII actually cuts λ at 7 sites. How many fragments are produced? (c) How many fragments would the same 7 cuts produce if the molecule were circular?
10. (Medium) A gene is transcribed at 0.50 mRNA/min and its mRNA has a half-life of 20 min. (a) Find the steady-state mRNA number. (b) Transcription is then shut off; how long until the mRNA falls to 10% of its steady-state value? (c) If a microRNA halves the half-life without changing transcription, what is the new steady state?
11. (Hard) A 1.0-fL bacterium contains 20 repressor tetramers that bind an operator with $K_d = 0.050$ nM. (a) What fraction of time is the operator free? (b) If an inducer raises $K_d$ a thousandfold, what fraction is free? (c) What induction ratio does the simple binding model predict? (d) State two simplifications in this model.
12. (Conceptual) A biotechnology company wants *E. coli* to make a human enzyme. Explain why cloning the gene directly from human genomic DNA would fail, and describe two molecular-biology steps that solve the problem. Name one kind of human protein that *E. coli* still cannot produce correctly, and why.

### Solutions

**1.** DNA polymerase extends only 3' ends, so each strand can grow only 5'→3'. On the leading strand, that direction points into the fork, so once primed, synthesis can continue as the fork opens. On the lagging strand, 5'→3' synthesis points away from the fork; as new template is exposed near the fork, the polymerase must start again with a new primer, producing Okazaki fragments. Each fragment's RNA primer is removed and replaced with DNA, leaving a nick that ligase must seal. **Answer:** one primer per leading strand versus one primer per Okazaki fragment (millions per human S phase); ligation is needed at every fragment junction.

**2.**
1. Semiconservative: $f_{\text{hybrid}} = 2^{1-3} = 1/4$; $f_{\text{light}} = 3/4$.
2. Conservative: $2^{-3} = 1/8$ heavy, $7/8$ light, no hybrid.
3. Dispersive: a single band with $1/8$ of the heavy label in every molecule.

**Answer:** semiconservative — 25% hybrid and 75% light; conservative — 12.5% heavy and 87.5% light; dispersive — one band close to light density.

**3.**
1. Coding strand (complement of the template, written 5'→3'): 5'-ATGGCATTCCAGACGTGA-3'.
2. mRNA (coding sequence with U): 5'-AUG GCA UUC CAG ACG UGA-3'.
3. Translation: AUG Met, GCA Ala, UUC Phe, CAG Gln, ACG Thr, UGA stop.

**Answer:** Met–Ala–Phe–Gln–Thr.

**4.**
1. (a) Codon 3 changes UUC → UUU, still Phe: **silent**; peptide Met-Ala-Phe-Gln-Thr.
2. (b) Codon 4 changes CAG → UAG, a stop codon: **nonsense**; peptide Met-Ala-Phe.
3. (c) The mRNA becomes AUG GGC AUU CCA GAC GUG A...: **frameshift**; Met-Gly-Ile-Pro-Asp-Val..., and the original UGA stop is no longer in frame, so translation continues into the 3' untranslated region until a stop codon happens to occur in the new frame.
4. (d) Removing GCA deletes exactly one codon: **in-frame deletion**; peptide Met-Phe-Gln-Thr (like ΔF508 in cystic fibrosis).

**Answer:** (a) silent; (b) nonsense, Met-Ala-Phe; (c) frameshift, Met-Gly-Ile-Pro-Asp-Val-...; (d) in-frame deletion, Met-Phe-Gln-Thr.

**5.**
1. (a) Each of two forks copies $2.32\times10^{6}$ nt: $t = 2.32\times10^{6}/800 = 2900$ s $= 48$ min.
2. (b) Replication rounds overlap: new rounds start at oriC before previous rounds finish (multifork replication), so a cell completes a chromosome every 25 min even though each round takes 48 min.
3. (c) $N_{\text{ori}}/N_{\text{ter}} = 2^{C/\tau} = 2^{48.3/25} = 2^{1.93} = 3.8$.

**Answer:** (a) about 48 min; (b) overlapping rounds of replication; (c) origin-region genes outnumber terminus-region genes about 3.8 to 1.

**6.**
1. One central origin: each fork copies 124 Mb; $t = 1.24\times10^{8}/30 = 4.1\times10^{6}$ s $= 48$ days.
2. Origins every 100 kb: $2.48\times10^{8}/10^{5} = 2480$ origins; each fork copies 50 kb: $t = 5.0\times10^{4}/30 = 1.7\times10^{3}$ s $\approx 28$ min.
3. S phase lasts about 8 h because origins do not all fire at once: different chromosomal domains replicate in a fixed early-to-late order (gene-rich, active chromatin tends to replicate early), and only a subset of licensed origins is used in any given cell cycle.

**Answer:** about 48 days with one origin versus about half an hour with 2480 simultaneously firing origins; real S phase is longer because origin firing is staggered.

**7.**
1. (a) $50\,000/110 = 455$ amino acids.
2. (b) $455\times3 + 3 = 1368$ nt.
3. (c) $455/6 = 76$ s.
4. (d) 454 peptide bonds $\times4 = 1816$ phosphate bonds.

**Answer:** about 455 amino acids, 1368 nt of coding sequence (the whole mRNA is longer, with UTRs and a poly(A) tail), about 76 s, and about 1800 high-energy phosphate bonds.

**8.**
1. $\Delta C_t = 27.3 - 24.0 = 3.3$ cycles; the treated sample crossed earlier, so it had more template.
2. At $E = 1$: fold change $= 2^{3.3} = 9.8$.
3. At $E = 0.95$: fold change $= 1.95^{3.3} = 9.1$.

**Answer:** about 9.8-fold higher at 100% efficiency, and about 9.1-fold at 95% — a reminder that assuming perfect efficiency can bias estimates.

**9.**
1. (a) $48\,502/4^{6} = 48\,502/4096 = 11.8$ sites expected.
2. (b) A linear molecule with 7 cuts gives $7 + 1 = 8$ fragments.
3. (c) A circular molecule with 7 cuts gives 7 fragments.

**Answer:** about 12 expected, 7 observed; 8 fragments from linear λ DNA and 7 from a circle. (λ's ends carry 12-nt single-stranded "cos" overhangs that can anneal, so in practice the two end fragments may stick together unless the digest is heated before running the gel.)

**10.**
1. $\gamma = \ln 2/20\ \text{min} = 0.0347\ \text{min}^{-1}$.
2. (a) $m^{*} = 0.50/0.0347 = 14.4$ molecules.
3. (b) $t = \ln 10/\gamma = 2.303/0.0347 = 66$ min (3.32 half-lives).
4. (c) Halving $t_{1/2}$ doubles $\gamma$, so $m^{*}$ halves to 7.2.

**Answer:** (a) about 14 mRNAs; (b) about 66 min; (c) about 7 mRNAs — and the gene would now respond twice as fast.

**11.**
1. $[\text{R}] = 20\times1.66\ \text{nM} = 33.2$ nM.
2. (a) $p_{\text{free}} = 0.050/(0.050 + 33.2) = 1.5\times10^{-3}$.
3. (b) $K_d = 50$ nM: $p_{\text{free}} = 50/(50 + 33.2) = 0.60$.
4. (c) Ratio $= 0.60/0.0015 \approx 400$.
5. (d) Possible simplifications: all repressor is treated as free, although much of it binds non-specifically to the rest of the chromosome; the model ignores DNA looping to auxiliary operators; it ignores CAP activation, cell-to-cell variation in the small number of repressor molecules, and the time needed to reach equilibrium; and it treats transcription as proportional to the fraction of time the operator is free.

**Answer:** (a) 0.15% free (about 670-fold repression); (b) 60% free; (c) about 400-fold induction; (d) see step 5.

**12.** Human genes are interrupted by introns, and bacteria lack spliceosomes, so the genomic gene would be transcribed and translated with introns included, giving a nonsense product; in addition, human promoters and translation signals are not recognized by bacterial RNA polymerase and ribosomes. The solutions are (1) to make **cDNA** by reverse-transcribing mature mRNA (or to synthesize the coding sequence chemically, often with codons optimized for *E. coli*), and (2) to place it in an **expression vector** with a bacterial promoter (often an inducible one such as the lac promoter, switched on with IPTG) and a Shine–Dalgarno sequence. **Answer:** proteins needing eukaryotic post-translational modifications — most notably **glycoproteins** such as many therapeutic antibodies and erythropoietin — are made in yeast or mammalian (for example Chinese hamster ovary) cells instead, because *E. coli* lacks the ER and Golgi glycosylation machinery and often cannot form multiple disulfide bonds correctly in its cytoplasm.

## 15. Summary and Key Equations

| Process | Template | Product | Enzyme | Location (eukaryotes) |
|---|---|---|---|---|
| Replication | DNA (both strands) | DNA | DNA polymerase (+ primase, helicase, ligase) | Nucleus (S phase) |
| Transcription | DNA (template strand) | RNA | RNA polymerase | Nucleus |
| RNA processing | Pre-mRNA | mRNA (cap, tail, spliced) | Spliceosome, capping, poly(A) polymerase | Nucleus |
| Translation | mRNA | Protein | Ribosome (rRNA catalysis) | Cytoplasm / rough ER |
| Reverse transcription | RNA | DNA | Reverse transcriptase | (Retroviruses, telomerase) |

| Process | Typical speed | Error rate (after all correction) |
|---|---|---|
| Replication | ~1000 nt/s per fork (bacteria); tens of nt/s (eukaryotes) | ~$10^{-9}$ to $10^{-10}$ per nucleotide |
| Transcription | ~20–50 nt/s | ~$10^{-4}$ to $10^{-5}$ per nucleotide |
| Translation | ~15–20 aa/s (bacteria); ~5–6 aa/s (eukaryotes) | ~$10^{-3}$ to $10^{-4}$ per codon |

| Genome | Size | Protein-coding genes (approx.) |
|---|---|---|
| Phage φX174 | 5386 nt (single-stranded DNA) | 11 |
| Phage λ | 48 502 bp | about 70 |
| *E. coli* K-12 | 4.64 Mb | about 4300 |
| Budding yeast (*S. cerevisiae*) | 12.1 Mb | about 6000 |
| Human mitochondrion | 16 569 bp | 13 (plus 22 tRNAs and 2 rRNAs) |
| Human nuclear genome (haploid) | about 3.1 Gb | about 20 000 |

**Key equations**
- Meselson–Stahl, after $n \ge 1$ generations: $f_{\text{hybrid}} = 2^{\,1-n}$, $f_{\text{light}} = 1 - 2^{\,1-n}$.
- Replication time with one bidirectional origin: $t = L/(2v)$; origin-to-terminus copy ratio in exponential growth: $N_{\text{ori}}/N_{\text{ter}} = 2^{C/\tau}$.
- Serial fidelity: $\varepsilon_{\text{overall}} = \varepsilon_{1}\varepsilon_{2}\varepsilon_{3}$; equilibrium discrimination $f_0 = e^{-\Delta\Delta G/RT}$, kinetic proofreading $f \approx f_0^{k}$.
- Code length: $4^{n} \ge 20 \Rightarrow n = 3$; chance stop-free run of $k$ codons: $(61/64)^{k}$.
- Probability a protein of $N$ residues is error-free: $(1-\varepsilon)^{N}$.
- Operator occupancy: $p_{\text{free}} = K_d/(K_d + [\text{R}])$; one molecule per femtolitre ≈ 1.7 nM.
- Expression kinetics: $dm/dt = k - \gamma m$, $m^{*} = k/\gamma$, $\gamma = \ln 2/t_{1/2}$, $t_{90} = 3.32\,t_{1/2}$.
- PCR: $N_n = N_0(1+E)^{n}$; qPCR fold change $= (1+E)^{\Delta C_t}$; standard-curve slope $= -1/\log_{10}(1+E)$ ($-3.32$ at 100%).
- Expected frequency of a specific $\ell$-base site in random DNA: once per $4^{\ell}$ bp.
- DNA bookkeeping: 0.34 nm and about 650 g/mol per base pair; $A_{260} = 1.0 \approx 50\ \mu$g/mL dsDNA.

**Key numbers:** codons 64 (61 sense + 3 stop); start AUG; DNA synthesis always 5'→3'; replication error rate ~10⁻⁹–10⁻¹⁰ after repair (about 0.6–6 new errors per diploid human cell division); human genome ~3.1 Gb, ~20 000 protein-coding genes; about 74 new germ-line point mutations per human generation; about one-quarter of random coding substitutions are synonymous.
