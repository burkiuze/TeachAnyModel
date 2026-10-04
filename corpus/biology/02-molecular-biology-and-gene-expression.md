---
title: Molecular Biology - DNA Replication, Transcription, Translation and Gene Regulation
field: Biology
subfield: Molecular Biology
level: high-school to undergraduate
keywords: [central dogma, DNA replication, semiconservative, DNA polymerase, leading strand, lagging strand, Okazaki fragments, primase, ligase, helicase, proofreading, DNA repair, transcription, RNA polymerase, promoter, mRNA processing, splicing, introns, exons, genetic code, codons, tRNA, ribosome, translation, mutations, lac operon, gene regulation, epigenetics, PCR, DNA sequencing, CRISPR, recombinant DNA]
---

# Molecular Biology: DNA Replication, Transcription, Translation and Gene Regulation

Molecular biology explains how genetic information is stored, copied and expressed. Francis Crick summarized the flow of information in 1958 as the **central dogma**:
$$\text{DNA}\xrightarrow{\text{replication}}\text{DNA}\xrightarrow{\text{transcription}}\text{RNA}\xrightarrow{\text{translation}}\text{Protein}$$
Exceptions and extensions: **reverse transcription** (RNA → DNA, in retroviruses and telomerase), **RNA replication** (RNA viruses), and regulatory RNAs that are never translated. Information never flows from protein back to nucleic acid.

## 1. Discovery of DNA as the Genetic Material

- **1869:** Friedrich Miescher isolated "nuclein" (DNA) from pus cells.
- **1928:** Frederick Griffith's **transformation** experiment: a heat-killed virulent (smooth, S) strain of *Streptococcus pneumoniae* converted live harmless (rough, R) bacteria into virulent ones — some "transforming principle" was transferred.
- **1944:** Oswald Avery, Colin MacLeod and Maclyn McCarty showed the transforming principle is **DNA** (destroyed by DNase, not by protease or RNase).
- **1952:** Alfred Hershey and Martha Chase labeled bacteriophage T2 with ³⁵S (protein) or ³²P (DNA); only ³²P entered bacteria, confirming DNA as the genetic material of phages.
- **1953:** Watson and Crick's double helix, based on Rosalind Franklin's X-ray data and Chargaff's rules.
- **1958:** Meselson and Stahl demonstrated **semiconservative replication**.

## 2. DNA Replication

### Semiconservative replication
Each new DNA molecule consists of one **parental (template)** strand and one **newly synthesized** strand. **Meselson–Stahl experiment:** *E. coli* grown in heavy ¹⁵N medium were shifted to ¹⁴N; DNA was separated by density in CsCl gradients. After one generation, all DNA had intermediate density (ruling out conservative replication); after two generations, half intermediate and half light (ruling out dispersive replication). Described as "the most beautiful experiment in biology".

### The replication machinery

| Protein | Function |
|---|---|
| **Helicase** | Unwinds the double helix at the replication fork (breaks hydrogen bonds) |
| **Single-strand binding proteins (SSB)** | Keep separated strands apart |
| **Topoisomerase** (gyrase in bacteria) | Relieves supercoiling ahead of the fork (target of fluoroquinolone antibiotics and some anticancer drugs) |
| **Primase** | Synthesizes short RNA primers (~10 nt) — DNA polymerase cannot start a new strand from scratch |
| **DNA polymerase III** (bacteria) / **δ and ε** (eukaryotes) | Main replicative polymerases; add nucleotides 5'→3' |
| **Sliding clamp** (β clamp / PCNA) | Holds polymerase on DNA for high processivity |
| **DNA polymerase I** (bacteria) | Removes RNA primers (5'→3' exonuclease) and fills gaps |
| **DNA ligase** | Seals nicks by forming phosphodiester bonds |
| **Telomerase** (eukaryotes) | Extends chromosome ends |

### Key principles
1. **DNA polymerases synthesize only in the 5' → 3' direction**, adding deoxynucleoside triphosphates (dNTPs) to the 3'-OH of the growing strand. Pyrophosphate (PPᵢ) release and its hydrolysis drive the reaction.
2. They **require a primer** with a free 3'-OH.
3. Because the two strands are antiparallel:
   - The **leading strand** is synthesized continuously toward the replication fork.
   - The **lagging strand** is synthesized discontinuously, away from the fork, in short **Okazaki fragments** (1000–2000 nucleotides in bacteria, 100–200 in eukaryotes; discovered by Reiji and Tsuneko Okazaki, 1968), each requiring a new primer, later joined by ligase.
4. Replication begins at **origins of replication**: one in the circular *E. coli* chromosome (oriC; replication proceeds bidirectionally at ~1000 nucleotides/s per fork, copying 4.6 Mb in ~40 minutes); thousands in eukaryotic chromosomes (forks move ~50 nt/s; the human genome is replicated in ~8 hours of S phase).

### Fidelity
- Base-pairing selectivity: ~1 error per 10⁴–10⁵ nucleotides.
- **Proofreading** by the polymerase's 3'→5' exonuclease removes mismatches: improves to ~1 per 10⁷.
- **Mismatch repair** after replication: overall ~1 error per 10⁹–10¹⁰ nucleotides. In humans, that is roughly 0.1–1 new mutation per cell division in the genome. Inherited mismatch repair defects cause Lynch syndrome (hereditary colorectal cancer).

### The end-replication problem and telomeres
On linear chromosomes, the lagging strand cannot be fully completed at the very end (no room for a final primer), so chromosomes shorten with each division. **Telomeres** (TTAGGG repeats in vertebrates, several kilobases long) buffer genes from loss; **telomerase** carries its own RNA template to extend them.

## 3. DNA Damage and Repair

DNA in each human cell suffers tens of thousands of lesions per day (depurination, deamination, oxidation, UV damage, strand breaks). Repair systems:
- **Direct reversal:** photolyase reverses UV-induced pyrimidine dimers (not in placental mammals); O⁶-methylguanine methyltransferase.
- **Base excision repair (BER):** glycosylases remove damaged bases (e.g. uracil from deaminated cytosine).
- **Nucleotide excision repair (NER):** removes bulky lesions such as thymine dimers. Defects cause **xeroderma pigmentosum** (extreme sensitivity to sunlight and skin cancer).
- **Mismatch repair (MMR).**
- **Double-strand break repair:** **homologous recombination** (accurate, uses the sister chromatid; requires BRCA1/BRCA2 — mutations greatly raise breast and ovarian cancer risk; PARP inhibitors exploit this weakness) and **non-homologous end joining** (error-prone).
(Lindahl, Modrich and Sancar, Nobel Chemistry 2015.)

## 4. Transcription

**Transcription** copies a gene's DNA sequence into RNA.

### Basic features
- **RNA polymerase** synthesizes RNA 5'→3', using ribonucleoside triphosphates (ATP, GTP, CTP, UTP) and one DNA strand as template.
- The **template (antisense)** strand is read 3'→5'; the RNA has the same sequence as the **coding (sense)** strand, with U in place of T.
- **No primer** is needed.
- Error rate is higher than replication (~1 in 10⁴–10⁵) but errors are not inherited.

### Stages
1. **Initiation:** RNA polymerase binds the **promoter** upstream of the gene.
   - Bacteria: a single RNA polymerase; the **sigma (σ) factor** recognizes promoter elements at −35 (TTGACA) and −10 (TATAAT, Pribnow box).
   - Eukaryotes: three nuclear RNA polymerases — **Pol I** (most rRNA), **Pol II** (mRNA, most snRNAs, miRNAs), **Pol III** (tRNA, 5S rRNA). Pol II requires **general transcription factors**; **TFIID** binds the **TATA box** (~−25 to −30). Enhancers, often far away, bind activators that loop DNA to contact the promoter via **Mediator**. (Roger Kornberg, Nobel Chemistry 2006 for the structural basis of eukaryotic transcription.) α-Amanitin from death-cap mushrooms potently inhibits Pol II.
2. **Elongation:** the polymerase unwinds ~10–20 bp of DNA (transcription bubble) and adds nucleotides (~20–50 nt/s).
3. **Termination:**
   - Bacteria: **intrinsic (Rho-independent)** — a GC-rich hairpin followed by a run of U's; or **Rho-dependent** — the Rho helicase dislodges the polymerase.
   - Eukaryotes (Pol II): transcription continues past the polyadenylation signal (AAUAAA); the RNA is cleaved and the polymerase is released.

### Eukaryotic mRNA processing
Eukaryotic primary transcripts (pre-mRNA) are processed in the nucleus:
1. **5' cap:** 7-methylguanosine attached by an unusual 5'–5' triphosphate linkage — protects from degradation and helps ribosome binding.
2. **3' poly(A) tail:** ~200 adenine nucleotides added by poly(A) polymerase — stability, export, translation.
3. **Splicing:** non-coding **introns** are removed and **exons** joined by the **spliceosome** (snRNPs; splice sites GU at the 5' end of introns and AG at the 3' end; branch point A forms a lariat). Introns were discovered in 1977 (Roberts and Sharp, Nobel 1993).
   - **Alternative splicing** lets one gene produce multiple protein variants; ~95% of human multi-exon genes are alternatively spliced. The *Drosophila Dscam* gene can potentially produce over 38 000 isoforms.
   - Splicing errors cause disease (some β-thalassemias, spinal muscular atrophy — treated with antisense oligonucleotide nusinersen, which corrects splicing).

In bacteria, transcription and translation are **coupled** — ribosomes begin translating mRNA while it is still being transcribed.

## 5. The Genetic Code

The sequence of mRNA is read in **codons** of three nucleotides; 4³ = 64 codons specify 20 amino acids plus stop signals. Deciphered between 1961 and 1966 (Nirenberg and Matthaei used synthetic poly-U RNA, which produced polyphenylalanine — UUU codes for Phe; Khorana, Holley; Nobel 1968).

### Properties
- **Triplet:** shown by Crick and Brenner (1961) using frameshift mutations.
- **Non-overlapping** and read without punctuation from a fixed start point (**reading frame**).
- **Degenerate (redundant):** most amino acids have multiple codons (Leu, Ser, Arg have six; Met and Trp only one). Synonymous codons often differ in the third position (**wobble**).
- **Start codon:** **AUG** (methionine; N-formylmethionine in bacteria).
- **Stop codons:** **UAA, UAG, UGA** (no tRNA; recognized by release factors).
- **Nearly universal:** the same code in almost all organisms — strong evidence for common ancestry. Minor variations exist (e.g. in vertebrate mitochondria UGA codes for Trp and AGA/AGG are stops; some ciliates read UAA/UAG as Gln).

### Codon table (selected)

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

## 6. Translation

### Key players
- **mRNA:** the template, read 5'→3'.
- **tRNA:** adaptor molecules (~76 nt, cloverleaf secondary structure, L-shaped 3D structure) with an **anticodon** that pairs with the codon (antiparallel) and the amino acid attached to the 3' CCA end. **Aminoacyl-tRNA synthetases** (one per amino acid) attach the correct amino acid using ATP — the true "translators" of the code, with proofreading. **Wobble** pairing (e.g. G–U, and inosine in anticodons) allows one tRNA to read several codons, so cells need fewer than 61 tRNA types.
- **Ribosome:** large and small subunits (bacteria 70S = 50S + 30S; eukaryotes 80S = 60S + 40S). Three tRNA sites: **A** (aminoacyl), **P** (peptidyl), **E** (exit). The **peptidyl transferase** activity is catalyzed by rRNA — the ribosome is a ribozyme.

### Stages
1. **Initiation:**
   - Bacteria: the small subunit binds the **Shine–Dalgarno sequence** (AGGAGG) upstream of AUG; initiator fMet-tRNA enters the P site; the large subunit joins (GTP-dependent, with initiation factors).
   - Eukaryotes: the small subunit binds the 5' cap and **scans** to the first AUG in a good context (Kozak sequence).
2. **Elongation** (repeated): an aminoacyl-tRNA enters the A site (EF-Tu/eEF1 with GTP); the peptide bond forms (the growing chain transfers from the P-site tRNA to the A-site amino acid); the ribosome **translocates** one codon (EF-G/eEF2, GTP), moving tRNAs from A→P→E. Rate ~15–20 amino acids/s in bacteria, ~5–6/s in eukaryotes.
3. **Termination:** a stop codon in the A site is recognized by **release factors**; the polypeptide is hydrolyzed from the tRNA and released; the ribosome dissociates.

Each peptide bond costs ~4 high-energy phosphate bonds (2 for aminoacylation, 1 each for EF-Tu and EF-G). Multiple ribosomes can translate one mRNA simultaneously (**polysomes**).

### Post-translational events
Folding (with chaperones), proteolytic cleavage (e.g. proinsulin → insulin), chemical modifications (phosphorylation, glycosylation, acetylation, ubiquitination, lipidation), and targeting: a hydrophobic **signal peptide** at the N-terminus directs ribosomes to the ER via the signal recognition particle (Günter Blobel, Nobel 1999).

### Worked example
DNA template strand: 3'-TAC GGA CTT ATC-5'
mRNA: 5'-AUG CCU GAA UAG-3'
Protein: Met–Pro–Glu–(stop)

## 7. Mutations

A **mutation** is a heritable change in DNA sequence.

### Point mutations (single-base substitutions)
- **Silent (synonymous):** codon change without amino acid change (GAA → GAG, both Glu).
- **Missense:** different amino acid (sickle-cell: GAG → GTG, Glu6Val in β-globin).
- **Nonsense:** creates a stop codon → truncated protein (some cystic fibrosis and Duchenne muscular dystrophy alleles).
- **Transitions** (purine↔purine, pyrimidine↔pyrimidine) are more common than **transversions**.

### Insertions and deletions (indels)
If not a multiple of three, they cause a **frameshift**, changing every downstream codon (often creating a premature stop). Example: THE CAT ATE THE RAT → deletion of one letter → THE ATA TET HER AT. The most common cystic fibrosis mutation (ΔF508) is an in-frame deletion of three nucleotides, removing one phenylalanine.

### Larger-scale changes
Duplications, inversions, translocations (e.g. the Philadelphia chromosome t(9;22) creating the BCR-ABL fusion in chronic myeloid leukemia), copy-number variants, **trinucleotide repeat expansions** (Huntington's disease — CAG repeats; fragile X syndrome — CGG repeats), and whole-chromosome aneuploidies.

### Causes
- **Spontaneous:** replication errors, tautomeric shifts, depurination, deamination of cytosine (to uracil) and 5-methylcytosine (to thymine — making CpG sites mutation hotspots).
- **Induced (mutagens):** UV light (thymine dimers), ionizing radiation (strand breaks), chemicals (alkylating agents, base analogs, intercalators like ethidium bromide, benzo[a]pyrene), some viruses. The **Ames test** screens chemicals for mutagenicity using *Salmonella* strains.

Mutations are the ultimate source of genetic variation for evolution; most are neutral or harmful, a few beneficial. Mutations in **germ-line** cells can be inherited; **somatic** mutations affect only the individual (e.g. cancer). Each human is born with ~50–100 new mutations not present in either parent.

## 8. Regulation of Gene Expression

Every cell has (almost) the same genome, yet a neuron differs from a liver cell because they express different genes. Regulation can occur at every step.

### Prokaryotes: operons
An **operon** is a cluster of genes transcribed together from one promoter, controlled by an **operator** (François Jacob and Jacques Monod, 1961; Nobel 1965 with André Lwoff).

**The lac operon** (*E. coli*; genes *lacZ* — β-galactosidase, *lacY* — permease, *lacA* — transacetylase): an **inducible** operon for lactose catabolism.
- **No lactose:** the *lacI* repressor binds the operator, blocking transcription.
- **Lactose present:** allolactose (an isomer) binds the repressor, which releases the operator → transcription (negative control).
- **Glucose present:** even with lactose, transcription is low — **catabolite repression**. When glucose is low, cAMP rises; the cAMP–CAP (catabolite activator protein) complex binds near the promoter and strongly activates transcription (positive control). Result: bacteria prefer glucose, using lactose only when glucose runs out (**diauxic growth**).

**The trp operon:** a **repressible** operon for tryptophan synthesis — tryptophan (corepressor) activates the repressor, turning genes off when tryptophan is abundant; **attenuation** provides finer control by coupling translation of a leader peptide to transcription termination.

### Eukaryotes: multiple levels
1. **Chromatin structure:** histone **acetylation** (by HATs) loosens chromatin and promotes transcription; deacetylation (HDACs) represses. Histone methylation can activate or repress depending on the residue. **DNA methylation** at CpG sites (in promoters) generally silences genes.
2. **Transcriptional control** (the most important level): combinations of **transcription factors** binding promoters and **enhancers/silencers**; **combinatorial control** allows a limited number of factors to specify many expression patterns. Master regulators (e.g. MyoD for muscle; Hox genes for body-plan segments) can switch cell fates.
3. **RNA processing:** alternative splicing, RNA editing (e.g. apolipoprotein B mRNA C→U editing produces a shorter protein in intestine).
4. **mRNA transport and stability:** mRNA half-lives range from minutes to days (AU-rich elements promote decay).
5. **Translational control:** initiation factors (phosphorylation of eIF2 in stress), iron-responsive elements (ferritin), **microRNAs** (~22 nt; bind 3' UTRs to repress translation or trigger decay; discovered in *C. elegans* — lin-4 by Victor Ambros and Gary Ruvkun, Nobel Medicine 2024) and siRNAs.
6. **Post-translational control:** protein modification, localization, and degradation (ubiquitin–proteasome system).

### Epigenetics
Heritable changes in gene expression that do not involve changes in DNA sequence — DNA methylation, histone modifications, chromatin remodeling and non-coding RNAs. Examples:
- **X-chromosome inactivation** in female mammals: one X is randomly silenced in each cell (Barr body), directed by the *XIST* lncRNA; calico cats' patchy coats result from this mosaicism.
- **Genomic imprinting:** certain genes are expressed only from the maternally or paternally inherited copy (*IGF2*; Prader–Willi and Angelman syndromes arise from deletions of the same region inherited from father or mother, respectively).
- Environmental influences (diet, stress, toxins) can alter epigenetic marks; the Dutch Hunger Winter (1944–45) cohort showed lasting effects associated with methylation changes.
- Epigenetic dysregulation contributes to cancer; HDAC and DNA methyltransferase inhibitors are used as drugs.

## 9. Biotechnology and Genetic Engineering

- **Restriction enzymes** (Arber, Nathans and Smith, Nobel 1978) cut DNA at specific sequences (EcoRI: G^AATTC), often leaving "sticky ends".
- **Recombinant DNA** (Cohen and Boyer, 1973): genes inserted into plasmid vectors and cloned in bacteria. **Human insulin** produced in *E. coli* (approved 1982) was the first recombinant drug; others include growth hormone, clotting factors, erythropoietin, hepatitis B vaccine and monoclonal antibodies.
- **Polymerase chain reaction (PCR)** (Kary Mullis, 1983; Nobel 1993): repeated cycles of denaturation (~95 °C), primer annealing (~50–65 °C) and extension (~72 °C, heat-stable *Taq* polymerase) double the target DNA each cycle — 30 cycles give ~10⁹ copies. **RT-qPCR** detects RNA viruses (COVID-19 tests).
- **Gel electrophoresis** separates DNA fragments by size (DNA is negatively charged and migrates toward the positive electrode).
- **DNA sequencing:** Sanger dideoxy chain-termination method (1977; Sanger's second Nobel, 1980); **next-generation sequencing** (Illumina sequencing-by-synthesis) and long-read technologies (PacBio, Oxford Nanopore). The **Human Genome Project** (1990–2003) cost about 3 billion US dollars; a human genome now costs a few hundred dollars. The telomere-to-telomere (T2T) consortium completed a gapless human genome in 2022. Humans have ~20 000 protein-coding genes — only ~1–2% of the genome codes for proteins.
- **DNA fingerprinting/profiling** (Alec Jeffreys, 1984) using short tandem repeats (STRs) for forensics and paternity testing.
- **CRISPR–Cas9 genome editing** (Doudna and Charpentier, 2012; Nobel Chemistry 2020): adapted from a bacterial adaptive immune system; a guide RNA directs Cas9 nuclease to a matching DNA sequence next to a PAM motif, where it makes a double-strand break repaired by NHEJ (gene knockouts) or homology-directed repair (precise edits). Base editors and prime editors enable changes without double-strand breaks. The first CRISPR therapy (exa-cel/Casgevy, for sickle-cell disease and β-thalassemia) was approved in 2023.
- **Gene therapy:** viral vectors (AAV, lentivirus) deliver functional genes (e.g. for spinal muscular atrophy, inherited blindness, hemophilia); CAR-T cell therapy for blood cancers.
- **GMOs:** Bt crops (insect-resistant), herbicide-tolerant crops, Golden Rice (β-carotene), and gene-edited crops.
- **Ethical issues:** germline editing (the 2018 case of gene-edited babies in China was widely condemned), genetic privacy, equitable access, biosafety.

## 10. Summary

| Process | Template | Product | Enzyme | Location (eukaryotes) |
|---|---|---|---|---|
| Replication | DNA (both strands) | DNA | DNA polymerase (+ primase, helicase, ligase) | Nucleus (S phase) |
| Transcription | DNA (template strand) | RNA | RNA polymerase | Nucleus |
| RNA processing | Pre-mRNA | mRNA (cap, tail, spliced) | Spliceosome, capping, poly(A) polymerase | Nucleus |
| Translation | mRNA | Protein | Ribosome (rRNA catalysis) | Cytoplasm / rough ER |
| Reverse transcription | RNA | DNA | Reverse transcriptase | (Retroviruses, telomerase) |

**Key numbers:** codons 64 (61 sense + 3 stop); start AUG; DNA synthesis always 5'→3'; replication error rate ~10⁻⁹–10⁻¹⁰ after repair; human genome ~3.1 Gb, ~20 000 protein-coding genes.
