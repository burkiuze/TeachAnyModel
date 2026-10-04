---
title: Genetics and Inheritance - Mendel, Meiosis, Chromosomes and Population Genetics
field: Biology
subfield: Genetics
level: high-school to undergraduate
keywords: [Mendel, genes, alleles, dominant, recessive, genotype, phenotype, homozygous, heterozygous, Punnett square, law of segregation, law of independent assortment, monohybrid cross, dihybrid cross, test cross, incomplete dominance, codominance, multiple alleles, ABO blood groups, epistasis, polygenic inheritance, pleiotropy, meiosis, crossing over, sex-linked inheritance, linkage, recombination frequency, pedigree analysis, nondisjunction, Down syndrome, Hardy-Weinberg equilibrium, heritability]
---

# Genetics and Inheritance: Mendel, Meiosis, Chromosomes and Population Genetics

**Genetics** is the study of heredity and variation. Why do children resemble their parents, yet differ from them and from each other? How can traits skip generations? Why are some diseases more common in boys? The answers began with Gregor Mendel's pea plants and now extend to whole-genome sequencing.

## 1. Mendel's Experiments

Gregor Mendel (1822–1884), an Augustinian friar in Brno (now Czech Republic), performed careful breeding experiments with garden peas (*Pisum sativum*) between 1856 and 1863, analyzing ~28 000 plants. He published in 1866, but his work was ignored until rediscovered in 1900 by Hugo de Vries, Carl Correns and Erich von Tschermak.

**Why peas worked well:** many varieties with distinct, discrete traits; self-pollination produces true-breeding lines, while controlled cross-pollination is easy; short generation time; many offspring. Mendel studied seven traits, each with two clear forms: seed shape (round/wrinkled), seed color (yellow/green), flower color (purple/white), pod shape (inflated/constricted), pod color (green/yellow), flower position (axial/terminal) and stem length (tall/dwarf).

Mendel's key innovations were **quantitative counting**, using **large samples**, and interpreting results with **probability**.

### The monohybrid cross
- **P generation:** true-breeding purple × true-breeding white.
- **F₁ generation:** all purple.
- **F₂ generation** (F₁ self-pollinated): 705 purple : 224 white ≈ **3 : 1**.

Mendel concluded:
1. Traits are determined by discrete "factors" (now **genes**) that come in alternative forms (**alleles**).
2. Each individual has **two** alleles for each gene (one from each parent).
3. One allele can be **dominant**, masking the **recessive** allele in heterozygotes.
4. **Law of segregation:** the two alleles separate during gamete formation, so each gamete carries only one allele, with equal probability.

## 2. Basic Vocabulary

| Term | Definition |
|---|---|
| Gene | A unit of heredity; a DNA sequence coding for a product |
| Locus | The position of a gene on a chromosome |
| Allele | Alternative version of a gene |
| Genotype | Allele combination (e.g. *Pp*) |
| Phenotype | Observable trait (e.g. purple flowers) |
| Homozygous | Two identical alleles (*PP* or *pp*) |
| Heterozygous | Two different alleles (*Pp*) |
| Dominant | Allele expressed in heterozygotes (uppercase) |
| Recessive | Allele masked in heterozygotes (lowercase) |
| Wild type | The most common allele/phenotype in natural populations |
| Hemizygous | Only one copy (X-linked genes in males) |

### Punnett squares
Reginald Punnett's diagram for the F₁ × F₁ cross *Pp* × *Pp*:

| | **P** | **p** |
|---|---|---|
| **P** | PP | Pp |
| **p** | Pp | pp |

Genotypic ratio **1 PP : 2 Pp : 1 pp**; phenotypic ratio **3 purple : 1 white**.

### Test cross
To determine whether a dominant-phenotype individual is *PP* or *Pp*, cross it with a homozygous recessive (*pp*):
- All offspring dominant → parent was *PP*.
- 1 : 1 dominant : recessive → parent was *Pp*.

## 3. Independent Assortment

### The dihybrid cross
Crossing true-breeding round–yellow (*RRYY*) with wrinkled–green (*rryy*): F₁ all *RrYy* (round–yellow). F₂ (*RrYy* × *RrYy*): Mendel observed 315 round–yellow : 108 round–green : 101 wrinkled–yellow : 32 wrinkled–green ≈ **9 : 3 : 3 : 1**.

**Law of independent assortment:** alleles of different genes assort independently during gamete formation — the F₁ produces four gamete types (RY, Ry, rY, ry) in equal proportions. (True for genes on different chromosomes or far apart on the same chromosome.)

### Probability rules
- **Multiplication (product) rule:** the probability of independent events both occurring is the product of their probabilities. P(*rryy*) from *RrYy* × *RrYy* = ¼ × ¼ = 1/16.
- **Addition (sum) rule:** the probability of either of mutually exclusive events is the sum. P(heterozygote from *Pp* × *Pp*) = P(*Pp*) + P(*pP*) = ¼ + ¼ = ½.

**Worked example 3.1:** in a cross *AaBbCc* × *AaBbCc*, what fraction of offspring will be *aabbcc*? (¼)³ = 1/64. What fraction will show all three dominant phenotypes? (¾)³ = 27/64.

**Worked example 3.2:** *AaBb* × *aabb* (dihybrid test cross) → 1 *AaBb* : 1 *Aabb* : 1 *aaBb* : 1 *aabb* if genes assort independently. Deviation from 1:1:1:1 (excess of parental types) indicates **linkage**.

### Chi-square test
To test whether observed counts fit expected ratios: $\chi^2 = \sum\frac{(O - E)^2}{E}$, compared with critical values for (number of categories − 1) degrees of freedom (3.84 for 1 df, 5.99 for 2, 7.81 for 3 at p = 0.05). For Mendel's dihybrid data (total 556; expected 312.75, 104.25, 104.25, 34.75): χ² ≈ 0.47, well below 7.81 — an excellent fit. (Ronald Fisher noted in 1936 that Mendel's data overall fit "too well", sparking a long debate; most historians now consider it unlikely that Mendel deliberately falsified results.)

## 4. Extensions of Mendelian Inheritance

### Incomplete dominance
Heterozygotes show an intermediate phenotype. Snapdragons: red (*RR*) × white (*rr*) → pink (*Rr*); F₂ 1 red : 2 pink : 1 white (genotypic and phenotypic ratios coincide). In humans, familial hypercholesterolemia is partly intermediate (heterozygotes have moderately elevated LDL; homozygotes severely elevated).

### Codominance
Both alleles are fully expressed in heterozygotes. **MN blood group:** *L^ML^N* individuals have both M and N antigens. Sickle-cell trait at the molecular level: heterozygotes make both normal and sickle hemoglobin.

### Multiple alleles: ABO blood groups
The *I* gene has three alleles: *I^A* and *I^B* (codominant) and *i* (recessive).

| Blood type | Genotypes | Antigens on red cells | Antibodies in plasma | Can receive from |
|---|---|---|---|---|
| A | *I^AI^A*, *I^Ai* | A | Anti-B | A, O |
| B | *I^BI^B*, *I^Bi* | B | Anti-A | B, O |
| AB | *I^AI^B* | A and B | None | All (universal recipient) |
| O | *ii* | None | Anti-A and anti-B | O only (universal donor of red cells) |

The **Rh factor** (D antigen) is inherited separately (Rh⁺ dominant). **Hemolytic disease of the newborn** can occur when an Rh⁻ mother carries an Rh⁺ fetus; anti-D immunoglobulin (RhoGAM) prevents maternal sensitization. Karl Landsteiner discovered ABO groups in 1901 (Nobel 1930).

### Epistasis
One gene affects the expression of another. **Labrador retrievers:** gene *B* (black *B* > brown *b*) determines pigment color; gene *E* determines whether pigment is deposited in fur — *ee* dogs are yellow regardless of *B*. *BbEe* × *BbEe* → 9 black : 3 brown (chocolate) : 4 yellow (a modified 9:3:3:1). The **Bombay phenotype** in humans (*hh*) masks ABO antigens.

### Polygenic inheritance
Many genes, each with small additive effects (plus environment), produce **continuous variation** — a bell-shaped distribution: height, skin color, intelligence-test scores, blood pressure, risk of type 2 diabetes. With three genes each with two alleles contributing additively, an F₂ shows 7 phenotypic classes in a 1:6:15:20:15:6:1 distribution. Genome-wide association studies (GWAS) have identified thousands of variants affecting human height, each with tiny effects.

### Pleiotropy
One gene affects multiple traits. **Sickle-cell allele:** anemia, pain crises, organ damage, and malaria resistance. **Marfan syndrome** (fibrillin-1 mutations): tall stature, long limbs, lens dislocation, aortic aneurysms. **Phenylketonuria:** intellectual disability and light pigmentation if untreated.

### Lethal alleles
Some genotypes are lethal, altering ratios. Yellow coat in mice (*A^Y*) is dominant for color but recessive lethal: *A^YA* × *A^YA* gives 2 yellow : 1 agouti (the *A^YA^Y* embryos die).

### Penetrance and expressivity
- **Incomplete penetrance:** not all individuals with the genotype show the phenotype (e.g. *BRCA1* mutations confer ~55–72% lifetime breast cancer risk, not 100%).
- **Variable expressivity:** severity varies among individuals with the same genotype (e.g. neurofibromatosis).

### Gene–environment interaction
Phenotype = genotype + environment (+ interaction). **Hydrangea** flower color depends on soil pH; **Himalayan rabbits and Siamese cats** have a temperature-sensitive pigment enzyme, producing dark fur on cooler extremities; **PKU** is prevented by a low-phenylalanine diet.

## 5. Chromosomes and Meiosis

### The chromosome theory of inheritance
Walter Sutton and Theodor Boveri (1902–1903) noted that chromosome behavior during meiosis parallels Mendel's factors; Thomas Hunt Morgan's work with fruit flies (*Drosophila melanogaster*) from 1910 confirmed that genes reside on chromosomes (Nobel 1933).

### Chromosome basics
- Humans have **46 chromosomes** in 23 pairs: 22 pairs of **autosomes** and one pair of **sex chromosomes** (XX female, XY male).
- **Homologous chromosomes** carry the same genes (possibly different alleles); one from each parent.
- **Diploid (2n)** somatic cells vs. **haploid (n)** gametes (n = 23 in humans).
- A **karyotype** displays an individual's chromosomes arranged by size and banding pattern.
- Chromosome numbers vary widely and do not reflect complexity: fruit fly 8, human 46, chimpanzee 48, dog 78, the fern *Ophioglossum reticulatum* ~1260.
- Human chromosome 2 resulted from the fusion of two ancestral ape chromosomes — visible as internal telomere-like sequences and a vestigial second centromere.

### Meiosis
**Meiosis** produces four genetically distinct **haploid** cells from one diploid cell through two successive divisions after one round of DNA replication.

**Meiosis I (reductional division — homologs separate):**
- **Prophase I:** homologous chromosomes pair (**synapsis**) via the synaptonemal complex, forming **bivalents (tetrads)**. **Crossing over** exchanges segments between non-sister chromatids at **chiasmata** — producing recombinant chromosomes. (The longest phase; in human oocytes it is arrested from fetal life until ovulation, up to ~50 years.)
- **Metaphase I:** homologous pairs line up at the metaphase plate; orientation of each pair is random (**independent assortment**).
- **Anaphase I:** homologs separate to opposite poles (sister chromatids stay together).
- **Telophase I and cytokinesis:** two haploid cells, each chromosome still with two chromatids.

**Meiosis II (equational division — like mitosis):** sister chromatids separate, producing four haploid cells.

**Sources of genetic variation:**
1. **Independent assortment** of homologs: 2²³ ≈ 8.4 million possible chromosome combinations per human gamete.
2. **Crossing over** (recombination) — on average ~1–3 crossovers per chromosome pair per meiosis — creates new allele combinations within chromosomes.
3. **Random fertilization:** 8.4 million × 8.4 million ≈ 70 trillion combinations per couple, before considering crossing over.
4. Mutations.

### Mitosis vs. meiosis

| Feature | Mitosis | Meiosis |
|---|---|---|
| Purpose | Growth, repair, asexual reproduction | Gamete production (sexual reproduction) |
| Divisions | One | Two |
| Daughter cells | 2, diploid, genetically identical | 4, haploid, genetically different |
| Synapsis and crossing over | No (rare) | Yes (prophase I) |
| Homologs | Behave independently | Pair and separate in meiosis I |
| Location | Somatic cells | Germ cells (testes, ovaries) |

**Gametogenesis:** in males, spermatogenesis produces four sperm per meiosis continuously from puberty (~100 million+ per day). In females, oogenesis produces one egg and polar bodies per meiosis (unequal cytokinesis concentrates cytoplasm in the egg); meiosis II is completed only at fertilization.

### Errors: nondisjunction
Failure of chromosomes to separate properly produces gametes with extra or missing chromosomes (**aneuploidy**):
- **Trisomy 21 (Down syndrome):** ~1 in 700 births; risk rises steeply with maternal age (about 1 in 1500 at age 20; 1 in 350 at 35; 1 in 30 at 45), mostly due to errors in maternal meiosis I.
- **Trisomy 18** (Edwards) and **trisomy 13** (Patau): severe; usually fatal in infancy.
- **Sex chromosome aneuploidies:** Turner syndrome (45,X — the only viable monosomy), Klinefelter syndrome (47,XXY), XYY, triple X.
- Most autosomal aneuploidies are lethal early in development; ~50% of first-trimester miscarriages involve chromosomal abnormalities.
- **Polyploidy** (extra full sets) is lethal in humans but common in plants: wheat is hexaploid, strawberries octoploid; seedless bananas and watermelons are triploid.

**Structural abnormalities:** deletions (cri-du-chat syndrome, 5p−), duplications, inversions and translocations (a balanced Robertsonian translocation can cause familial Down syndrome).

## 6. Sex Determination and Sex-Linked Inheritance

- In mammals, the **SRY** gene on the Y chromosome triggers testis development; without it, ovaries develop. (Birds use ZW systems — females are ZW; many reptiles use incubation temperature; honeybee males are haploid.)
- **X-linked genes:** the X chromosome carries ~800–900 protein-coding genes; the Y only ~70. Males are **hemizygous** for X-linked genes, so a single recessive allele produces the phenotype.

**X-linked recessive inheritance:**
- More common in males.
- Affected males inherit the allele from their mothers (fathers pass Y, not X, to sons).
- Carrier mothers (heterozygous) pass the allele to half of their sons (affected) and half of their daughters (carriers).
- Affected fathers pass the allele to all daughters (carriers) and no sons.
- Examples: **red–green color blindness** (~8% of men of Northern European ancestry, ~0.5% of women), **hemophilia A** (factor VIII; famously spread through Queen Victoria's descendants into the royal families of Spain and Russia), **Duchenne muscular dystrophy** (dystrophin — the largest human gene, ~2.2 Mb), G6PD deficiency.

**Worked example 6.1:** a carrier woman (*X^HX^h*) and a normal man (*X^HY*) have children. Daughters: ½ *X^HX^H*, ½ *X^HX^h* (carriers), none affected. Sons: ½ *X^HY* (normal), ½ *X^hY* (hemophilia). Overall probability that a child has hemophilia: ¼.

**X-linked dominant:** affected fathers pass the trait to all daughters (e.g. hypophosphatemic rickets, Rett syndrome).
**Y-linked:** father to all sons (few genes; e.g. some male infertility genes).

**Morgan's white-eyed fruit flies (1910):** a white-eyed male crossed with red-eyed females gave all red-eyed F₁; the F₂ had a 3:1 ratio but **all white-eyed flies were male** — the first gene assigned to a specific chromosome (X).

**Dosage compensation:** in female mammals, one X is inactivated (Lyonization, Mary Lyon, 1961). Calico and tortoiseshell cats are almost always female because orange/black fur alleles are X-linked and random X inactivation creates patches.

## 7. Linkage and Genetic Mapping

Genes close together on the same chromosome tend to be inherited together (**linked**) and do not assort independently. **Crossing over** between them produces recombinant gametes; the farther apart two genes are, the more often a crossover occurs between them.

**Recombination frequency** = (number of recombinant offspring / total offspring) × 100%.
- 1% recombination = **1 map unit** = **1 centimorgan (cM)** (named after Morgan).
- Unlinked genes show 50% recombination (the maximum).
- In humans, 1 cM ≈ roughly 1 million base pairs on average.

Alfred Sturtevant, an undergraduate in Morgan's lab, constructed the first genetic map in 1913 (five X-linked genes in *Drosophila*), realizing that recombination frequencies are approximately additive.

**Worked example 7.1:** a test cross of *AaBb* (from a parent with *AB*/*ab* chromosomes) × *aabb* gives 420 *AaBb*, 410 *aabb*, 85 *Aabb*, 85 *aaBb*. Recombinants: 170/1000 = 17% → the genes are 17 cM apart.

**Three-point crosses** determine gene order (the double-crossover class is the rarest) and reveal **interference** (one crossover reduces the chance of another nearby).

## 8. Human Pedigree Analysis

Pedigree symbols: squares = males, circles = females, filled = affected, half-filled or dotted = carriers, horizontal line = mating, vertical line = offspring; generations numbered with Roman numerals.

| Pattern | Key features | Examples |
|---|---|---|
| **Autosomal recessive** | Skips generations; affected children often have unaffected (carrier) parents; both sexes equally; more common with consanguinity | Cystic fibrosis (~1/2500–3500 among people of Northern European descent; carrier frequency ~1/25), sickle-cell disease, Tay–Sachs, PKU, albinism, spinal muscular atrophy |
| **Autosomal dominant** | Appears every generation; affected individual usually has an affected parent; ~50% of children of an affected heterozygote affected; both sexes | Huntington's disease (late onset — often after having children), Marfan syndrome, achondroplasia (mostly new mutations), familial hypercholesterolemia, neurofibromatosis type 1, polydactyly |
| **X-linked recessive** | Mostly males; transmitted through carrier females; no male-to-male transmission | Hemophilia, Duchenne MD, color blindness |
| **X-linked dominant** | Affected father → all daughters affected, no sons; more females affected | Hypophosphatemic rickets, fragile X (complex) |
| **Mitochondrial** | Transmitted only from mother to all children; variable severity (heteroplasmy) | Leber hereditary optic neuropathy, MELAS |

**Genetic counseling and testing:** carrier screening, prenatal diagnosis (amniocentesis, chorionic villus sampling, non-invasive prenatal testing from cell-free fetal DNA in maternal blood), preimplantation genetic testing, newborn screening.

## 9. Population Genetics

**Population genetics** studies allele frequencies in populations and how they change — the genetic basis of evolution.

### The Hardy–Weinberg principle
G. H. Hardy and Wilhelm Weinberg (1908, independently): in a large, randomly mating population with no mutation, migration or selection, allele and genotype frequencies remain constant from generation to generation.

For a gene with two alleles with frequencies $p$ (dominant) and $q$ (recessive):
$$\boxed{p + q = 1}, \qquad \boxed{p^2 + 2pq + q^2 = 1}$$
where $p^2$ = frequency of homozygous dominant, $2pq$ = heterozygous, $q^2$ = homozygous recessive.

**Conditions (assumptions) for equilibrium:**
1. No mutation.
2. Random mating.
3. No natural selection.
4. Very large population (no genetic drift).
5. No gene flow (migration).

Violation of any condition can cause evolution (change in allele frequencies). Hardy–Weinberg serves as a **null model** against which real populations are compared.

**Worked example 9.1:** cystic fibrosis affects about 1 in 2500 newborns of Northern European ancestry. $q^2 = 1/2500 \Rightarrow q = 0.02$, $p = 0.98$. Carrier frequency $2pq = 2(0.98)(0.02) \approx 0.039$ — about 1 in 25. Most copies of a rare recessive allele are hidden in heterozygous carriers, which is why selection against rare recessive alleles is slow.

**Worked example 9.2:** in a population, 36% of individuals show the recessive phenotype. $q = 0.6$, $p = 0.4$; homozygous dominant 16%, heterozygous 48%.

### Mechanisms of evolutionary change
- **Natural selection:** differential survival and reproduction (directional, stabilizing, disruptive, balancing; heterozygote advantage, e.g. sickle-cell in malarial regions).
- **Genetic drift:** random changes in allele frequencies, strongest in small populations. **Founder effect** (e.g. high frequency of Ellis–van Creveld syndrome in the Old Order Amish; Tay–Sachs and other alleles in Ashkenazi Jewish populations) and **bottleneck effect** (northern elephant seals reduced to ~20–30 individuals in the 1890s; cheetahs).
- **Gene flow:** migration transferring alleles between populations, reducing differences.
- **Mutation:** the ultimate source of new alleles (slow on its own).
- **Non-random mating:** inbreeding increases homozygosity (revealing recessive disorders); assortative mating.

### Heritability
**Broad-sense heritability** $H^2 = V_G/V_P$ is the fraction of phenotypic variance in a population attributable to genetic variance; **narrow-sense** $h^2 = V_A/V_P$ uses additive genetic variance (predicts response to selection: $R = h^2S$, the breeder's equation). Estimated from twin and adoption studies and from genomic data. Human height has $h^2 \approx 0.8$. Heritability describes a population in a given environment; it says nothing about how much of an individual's trait is "due to genes" and does not imply that a trait is unchangeable.

## 10. Summary

| Principle / Concept | Key point |
|---|---|
| Law of segregation | Alleles separate into gametes (monohybrid F₂ 3:1) |
| Law of independent assortment | Unlinked genes assort independently (dihybrid F₂ 9:3:3:1) |
| Test cross | × homozygous recessive reveals genotype |
| Incomplete dominance | Heterozygote intermediate (1:2:1) |
| Codominance | Both alleles expressed (AB blood) |
| Epistasis | One gene masks another (9:3:4) |
| Meiosis | 2n → 4 × n; crossing over + independent assortment |
| X-linked recessive | More common in males; carrier mothers |
| Recombination frequency | 1% = 1 cM; max 50% |
| Hardy–Weinberg | $p + q = 1$; $p^2 + 2pq + q^2 = 1$ |
