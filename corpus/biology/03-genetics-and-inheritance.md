---
title: Genetics and Inheritance - Mendel, Meiosis, Chromosomes and Population Genetics
field: Biology
subfield: Genetics
level: high-school to undergraduate
keywords: [Mendel, genes, alleles, dominant, recessive, genotype, phenotype, homozygous, heterozygous, Punnett square, law of segregation, law of independent assortment, monohybrid cross, dihybrid cross, test cross, incomplete dominance, codominance, multiple alleles, ABO blood groups, epistasis, polygenic inheritance, pleiotropy, meiosis, crossing over, sex-linked inheritance, linkage, recombination frequency, pedigree analysis, nondisjunction, Down syndrome, Hardy-Weinberg equilibrium, heritability, chi-square test, binomial probability, conditional probability, three-point cross, interference, Haldane mapping function, LOD score, X inactivation, genomic imprinting, natural selection, heterozygote advantage, genetic drift, inbreeding coefficient, linkage disequilibrium, breeder's equation, twin studies, forensic DNA profiling]
---

# Genetics and Inheritance: Mendel, Meiosis, Chromosomes and Population Genetics

**Genetics** is the study of heredity and variation. Why do children resemble their parents, yet differ from them and from each other? How can traits skip generations? Why are some diseases more common in boys? Why does a rare recessive disease persist for centuries even though affected people may have few children? The answers began with Gregor Mendel's pea plants and now extend to whole-genome sequencing. Much of classical genetics is applied probability: once we know how chromosomes behave in meiosis, the ratios seen in crosses, pedigrees and populations follow from a handful of rules that can be derived step by step. This chapter develops those rules, shows where they come from, and shows how they are used in medicine, agriculture and forensic science.

## 1. Mendel's Experiments

### Background: the problem of blending

Before Mendel, most naturalists assumed **blending inheritance**: offspring were thought to be a mixture of their parents, like mixing two paints. Blending has a fatal flaw that was already recognized in the nineteenth century: if traits blend, variation should halve in every generation, so populations would quickly become uniform and there would be nothing left for natural selection to act on. It also cannot explain why a trait absent in one generation can reappear, unchanged, in the next.

Gregor Mendel (1822–1884), an Augustinian friar in Brno (then Brünn, now in the Czech Republic), had studied physics and mathematics at the University of Vienna (1851–1853), where Christian Doppler was among his teachers. That training shaped his approach. He performed careful breeding experiments with garden peas (*Pisum sativum*) between 1856 and 1863, analyzing roughly 28 000 plants. He presented his results to the Natural History Society of Brünn in 1865 and published them in 1866 as "Experiments on Plant Hybridization". The work was largely ignored for 34 years, partly because few biologists of the time thought in terms of probabilities, and partly because later experiments Mendel did on hawkweed (*Hieracium*), at the suggestion of the botanist Carl Nägeli, gave confusing results — hawkweed often sets seed without fertilization (apomixis), so it does not show Mendelian segregation. Mendel became abbot of his monastery in 1868 and did little further experimental work. His paper was rediscovered in 1900 by Hugo de Vries, Carl Correns and Erich von Tschermak, each of whom had obtained similar ratios independently; William Bateson then became Mendel's leading advocate in the English-speaking world.

**Why peas worked well:** many varieties with distinct, discrete traits; self-pollination produces true-breeding lines, while controlled cross-pollination is easy (remove the anthers of one flower and dust its stigma with pollen from another); short generation time; many offspring. Mendel studied seven traits, each with two clear forms: seed shape (round/wrinkled), seed color (yellow/green), flower color (purple/white), pod shape (inflated/constricted), pod color (green/yellow), flower position (axial/terminal) and stem length (tall/dwarf).

Mendel's key innovations were **quantitative counting**, using **large samples**, starting from **true-breeding lines**, following **one trait at a time** before combining them, and interpreting results with **probability**.

### The monohybrid cross
- **P generation:** true-breeding purple × true-breeding white.
- **F₁ generation:** all purple. The white form has not been destroyed — it is merely hidden.
- **F₂ generation** (F₁ self-pollinated): 705 purple : 224 white ≈ **3 : 1**.

The same pattern appeared for all seven traits. Mendel's published F₂ counts are:

| Trait | Dominant form (count) | Recessive form (count) | Total | Ratio |
|---|---|---|---|---|
| Seed shape | Round 5474 | Wrinkled 1850 | 7324 | 2.96 : 1 |
| Seed (cotyledon) color | Yellow 6022 | Green 2001 | 8023 | 3.01 : 1 |
| Flower color | Purple 705 | White 224 | 929 | 3.15 : 1 |
| Pod shape | Inflated 882 | Constricted 299 | 1181 | 2.95 : 1 |
| Pod color | Green 428 | Yellow 152 | 580 | 2.82 : 1 |
| Flower position | Axial 651 | Terminal 207 | 858 | 3.14 : 1 |
| Stem length | Tall 787 | Dwarf 277 | 1064 | 2.84 : 1 |
| **All seven pooled** | **14 949** | **5010** | **19 959** | **2.98 : 1** |

No single trait gives exactly 3 : 1, but every one is close, and the pooled ratio is very close. This is exactly what chance sampling around a true 3 : 1 probability predicts (the chi-square test in Section 3 makes "close" precise).

Mendel concluded:
1. Traits are determined by discrete "factors" (now **genes**) that come in alternative forms (**alleles**).
2. Each individual has **two** alleles for each gene (one from each parent).
3. One allele can be **dominant**, masking the **recessive** allele in heterozygotes.
4. **Law of segregation:** the two alleles separate during gamete formation, so each gamete carries only one allele, with equal probability.

### Mendel's own test of the 1 : 2 : 1 hypothesis

The segregation hypothesis makes a sharper prediction than 3 : 1. If the F₂ purple plants are a mixture of *PP* and *Pp*, then only one-third of them should breed true. The derivation is a conditional probability. In the F₂, $P(PP) = \tfrac14$, $P(Pp) = \tfrac12$ and $P(\text{purple}) = \tfrac34$, so
$$P(PP \mid \text{purple}) = \frac{P(PP)}{P(\text{purple})} = \frac{1/4}{3/4} = \frac13, \qquad P(Pp \mid \text{purple}) = \frac{1/2}{3/4} = \frac23 .$$
Mendel self-pollinated F₂ plants with dominant phenotypes and grew their progeny. Of 565 plants raised from round F₂ seeds, 193 gave only round seeds while 372 gave round and wrinkled seeds in about 3 : 1 — a ratio of 1.93 : 1. For seed color, 166 of 519 bred true and 353 segregated (2.13 : 1). Both are close to the predicted 1 : 2, confirming that the dominant class is genetically heterogeneous exactly as the hypothesis requires.

## 2. Basic Vocabulary

| Term | Definition |
|---|---|
| Gene | A unit of heredity; a DNA sequence coding for a product (protein or functional RNA) |
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
| Carrier | A heterozygote for a recessive allele, usually unaffected |
| True-breeding (pure) line | A line that, when self-fertilized, produces only offspring like itself (homozygous) |
| P, F₁, F₂ | Parental, first filial and second filial generations |
| Gamete | A haploid reproductive cell (egg, sperm, pollen nucleus) carrying one allele per gene |

### Punnett squares
Reginald Punnett's diagram for the F₁ × F₁ cross *Pp* × *Pp*:

| | **P** | **p** |
|---|---|---|
| **P** | PP | Pp |
| **p** | Pp | pp |

Genotypic ratio **1 PP : 2 Pp : 1 pp**; phenotypic ratio **3 purple : 1 white**.

The Punnett square is just a picture of the product rule for independent events. Each parent independently contributes *P* or *p* with probability ½, so
$$P(PP) = \tfrac12 \cdot \tfrac12 = \tfrac14, \qquad P(Pp) = \tfrac12 \cdot \tfrac12 + \tfrac12 \cdot \tfrac12 = \tfrac12, \qquad P(pp) = \tfrac14 .$$
The heterozygote appears twice because it can arise in two mutually exclusive ways (*P* from the egg and *p* from the pollen, or the reverse), so the addition rule applies. Notice that the ratios are probabilities for each offspring; a family or a small sample will rarely show exactly 3 : 1.

### Test cross
To determine whether a dominant-phenotype individual is *PP* or *Pp*, cross it with a homozygous recessive (*pp*):
- All offspring dominant → parent was *PP*.
- 1 : 1 dominant : recessive → parent was *Pp*.

The test cross works because the recessive parent contributes only *p*, so the phenotype of each offspring directly reveals the allele contributed by the parent being tested — the offspring phenotypes are a readout of that parent's gametes. With a finite number of offspring the test is probabilistic: if a *Pp* parent is test-crossed and produces $n$ offspring, the chance that all of them are dominant (wrongly suggesting *PP*) is $(1/2)^n$, which is about 0.1% for $n = 10$. A cross back to either parent is called a **backcross**; the test cross is the special case of backcrossing to the recessive.

### Why are some alleles dominant? The molecular view

Dominance is not a property of an allele alone; it describes how the phenotype of a heterozygote compares with the two homozygotes, and it depends on what is being measured.
- Most recessive alleles are **loss-of-function** alleles. If one functional copy produces enough product for a normal phenotype (the gene is **haplosufficient**), the heterozygote looks normal and the loss-of-function allele is recessive. Carriers of phenylketonuria (PKU) have roughly half the normal phenylalanine hydroxylase activity, which is enough to keep blood phenylalanine in the normal range.
- If one copy is not enough (**haploinsufficiency**), a loss-of-function allele is dominant.
- **Dominant-negative** alleles make an abnormal protein that poisons the function of the normal one (for example, abnormal collagen chains in some forms of osteogenesis imperfecta disrupt the whole triple helix).
- **Gain-of-function** alleles give a protein a new or excessive activity and are usually dominant (the expanded polyglutamine tract in the huntingtin protein of Huntington's disease is toxic regardless of the normal copy).

Four of Mendel's seven genes have now been identified at the molecular level:

| Mendel's trait | Gene | Product of the dominant allele | Nature of the recessive allele |
|---|---|---|---|
| Round vs. wrinkled seed | *R* | Starch-branching enzyme I (SBEI) | Inactivated by an inserted transposon-like DNA element of about 0.8 kb (identified 1990) |
| Tall vs. dwarf stem | *Le* | Gibberellin 3β-hydroxylase, which makes the active growth hormone GA₁ | A single amino-acid substitution that greatly reduces enzyme activity (identified 1997) |
| Yellow vs. green seed | *I* | SGR ("stay-green") protein needed for chlorophyll breakdown as the seed matures | Loss-of-function alleles; chlorophyll persists, so cotyledons stay green (identified 2007) |
| Purple vs. white flower | *A* | A bHLH transcription factor that switches on anthocyanin pigment genes | Loss-of-function allele; no anthocyanin is made (identified 2010) |

The wrinkled-seed story shows how one gene produces a visible phenotype. Without SBEI, developing *rr* seeds make less branched starch (amylopectin) and accumulate more sucrose; the high sugar content draws in water osmotically, so the immature seeds swell and then shrink and wrinkle as they dry. At the level of seed shape *R* is completely dominant, but at the level of starch-grain structure and enzyme activity *Rr* seeds are intermediate — dominance depends on the level of observation.

## 3. Independent Assortment

### The dihybrid cross
Crossing true-breeding round–yellow (*RRYY*) with wrinkled–green (*rryy*): F₁ all *RrYy* (round–yellow). F₂ (*RrYy* × *RrYy*): Mendel observed 315 round–yellow : 108 round–green : 101 wrinkled–yellow : 32 wrinkled–green ≈ **9 : 3 : 3 : 1**.

**Law of independent assortment:** alleles of different genes assort independently during gamete formation — the F₁ produces four gamete types (RY, Ry, rY, ry) in equal proportions. (True for genes on different chromosomes or far apart on the same chromosome.)

**Derivation of 9 : 3 : 3 : 1.** For each gene separately, the F₂ is ¾ dominant phenotype and ¼ recessive. If the genes assort independently, the phenotype for seed shape tells us nothing about seed color, so the joint probabilities are products. Expanding
$$\left(\tfrac34\,\text{round} + \tfrac14\,\text{wrinkled}\right)\left(\tfrac34\,\text{yellow} + \tfrac14\,\text{green}\right) = \tfrac{9}{16}\,\text{RY} + \tfrac{3}{16}\,\text{Rg} + \tfrac{3}{16}\,\text{wY} + \tfrac{1}{16}\,\text{wg}$$
gives the 9 : 3 : 3 : 1 ratio directly. The 9 : 3 : 3 : 1 is therefore nothing more than two 3 : 1 ratios multiplied together. The same reasoning applied to genotypes gives $(1:2:1)^2$, i.e. nine genotype classes in the ratio 1 : 2 : 1 : 2 : 4 : 2 : 1 : 2 : 1.

**Generalization to $n$ genes.** For an F₁ heterozygous at $n$ independently assorting genes with complete dominance:

| Number of genes $n$ | Gamete types $2^n$ | F₂ genotypes $3^n$ | F₂ phenotypes $2^n$ | Cells in Punnett square $4^n$ | Fraction homozygous recessive at all loci |
|---|---|---|---|---|---|
| 1 | 2 | 3 | 2 | 4 | 1/4 |
| 2 | 4 | 9 | 4 | 16 | 1/16 |
| 3 | 8 | 27 | 8 | 64 | 1/64 |
| 4 | 16 | 81 | 16 | 256 | 1/256 |
| 10 | 1024 | 59 049 | 1024 | 1 048 576 | about 1 in a million |

The table explains why Punnett squares become impractical beyond two genes and why the product rule (or a branch diagram) is the tool of choice.

### Probability rules
- **Multiplication (product) rule:** the probability of independent events both occurring is the product of their probabilities. P(*rryy*) from *RrYy* × *RrYy* = ¼ × ¼ = 1/16.
- **Addition (sum) rule:** the probability of either of mutually exclusive events is the sum. P(heterozygote from *Pp* × *Pp*) = P(*Pp*) + P(*pP*) = ¼ + ¼ = ½.
- **Complement rule:** P(at least one) = 1 − P(none). This is usually the easiest route to "at least one" questions.
- **Conditional probability:** $P(A \mid B) = P(A \text{ and } B)/P(B)$. Used whenever we already know something about an individual, such as "this sibling is unaffected".
- **Binomial distribution:** if each child independently has probability $p$ of a phenotype, the probability that exactly $k$ of $n$ children have it is
$$P(k) = \binom{n}{k} p^k (1-p)^{n-k}, \qquad \binom{n}{k} = \frac{n!}{k!\,(n-k)!}.$$
The binomial coefficient counts the birth orders in which $k$ affected and $n-k$ unaffected children can occur; each order has probability $p^k(1-p)^{n-k}$ by the product rule, and the orders are mutually exclusive, so they are added.

**Worked example 3.1:** in a cross *AaBbCc* × *AaBbCc*, what fraction of offspring will be *aabbcc*? (¼)³ = 1/64. What fraction will show all three dominant phenotypes? (¾)³ = 27/64.

**Worked example 3.2:** *AaBb* × *aabb* (dihybrid test cross) → 1 *AaBb* : 1 *Aabb* : 1 *aaBb* : 1 *aabb* if genes assort independently. Deviation from 1:1:1:1 (excess of parental types) indicates **linkage**.

**Worked example 3.3 (branch method with unequal parents).** Parents *AaBbCc* × *AabbCc*; all three genes assort independently and show complete dominance. Find (a) the probability of an *AaBbCc* offspring, (b) the probability of the phenotype "dominant A, recessive B, dominant C", and (c) the probability that an offspring shows at least one recessive phenotype.
1. Treat each gene as a separate monohybrid cross. *Aa* × *Aa*: ¼ *AA*, ½ *Aa*, ¼ *aa*; dominant phenotype ¾. *Bb* × *bb*: ½ *Bb*, ½ *bb*; dominant phenotype ½. *Cc* × *Cc*: same as gene A.
2. (a) P(*Aa*) × P(*Bb*) × P(*Cc*) = ½ × ½ × ½ = 1/8.
3. (b) P(A dominant) × P(*bb*) × P(C dominant) = ¾ × ½ × ¾ = 9/32.
4. (c) First find P(all three dominant) = ¾ × ½ × ¾ = 9/32. By the complement rule, P(at least one recessive) = 1 − 9/32 = 23/32.

**Answer:** (a) 1/8; (b) 9/32 ≈ 0.28; (c) 23/32 ≈ 0.72. (These were checked by enumerating all 64 gamete combinations.)

**Worked example 3.4 (the binomial in a family).** Two parents are both carriers (*Aa*) of an autosomal recessive condition. They plan four children. What is the probability that (a) exactly one child is affected, (b) at least one child is affected, and (c) the first two children are affected and the last two are not?
1. For each child, P(affected) = P(*aa*) = $p = 1/4$, P(unaffected) = 3/4, independently of the other children.
2. (a) Exactly one of four: $\binom{4}{1}(1/4)^1(3/4)^3 = 4 \times \tfrac14 \times \tfrac{27}{64} = \tfrac{27}{64} \approx 0.42$.
3. (b) None affected: $(3/4)^4 = 81/256$. At least one affected: $1 - 81/256 = 175/256 \approx 0.68$.
4. (c) A specific birth order: $(1/4)^2 (3/4)^2 = 9/256 \approx 0.035$. No binomial coefficient is used because the order is specified.

**Answer:** (a) 27/64 ≈ 0.42; (b) 175/256 ≈ 0.68; (c) 9/256 ≈ 0.035. Note that even though "one in four" children is expected to be affected, a family of four has only a 42% chance of having exactly one affected child.

### Chi-square test
Observed counts never match expected ratios exactly, so we need a way to decide whether a deviation is small enough to be due to chance. Karl Pearson introduced the **chi-square goodness-of-fit test** in 1900 — the same year Mendel's work was rediscovered.
$$\chi^2 = \sum_{i} \frac{(O_i - E_i)^2}{E_i}$$
where $O_i$ and $E_i$ are the observed and expected counts in category $i$. Each term measures the squared deviation relative to the size of the category, so a deviation of 10 matters more when only 30 are expected than when 3000 are expected. The procedure:
1. State the **null hypothesis** (e.g. "the true ratio is 3 : 1").
2. Compute the expected counts from the total and the hypothesized ratio (use counts, never percentages).
3. Compute $\chi^2$.
4. Find the **degrees of freedom**: number of categories − 1 (minus one more for each parameter estimated from the same data, as in the Hardy–Weinberg test of Section 9).
5. Compare with the critical value. If $\chi^2$ exceeds it, reject the null hypothesis at that significance level; otherwise the data are consistent with it. A non-significant result does not *prove* the hypothesis; it means the data provide no evidence against it.

Critical values of $\chi^2$:

| Degrees of freedom | p = 0.05 | p = 0.01 |
|---|---|---|
| 1 | 3.841 | 6.635 |
| 2 | 5.991 | 9.210 |
| 3 | 7.815 | 11.345 |
| 4 | 9.488 | 13.277 |
| 5 | 11.070 | 15.086 |

For Mendel's dihybrid data (total 556; expected 312.75, 104.25, 104.25, 34.75): χ² ≈ 0.47, well below 7.81 (3 df) — an excellent fit (p ≈ 0.93). (Ronald Fisher noted in 1936 that Mendel's data overall fit "too well", sparking a long debate; most historians now consider it unlikely that Mendel deliberately falsified results.)

**Worked example 3.5 (chi-square for a monohybrid cross).** Test whether Mendel's flower-color F₂ (705 purple, 224 white) fits 3 : 1.
1. Total $N = 705 + 224 = 929$.
2. Expected: purple $\tfrac34 \times 929 = 696.75$; white $\tfrac14 \times 929 = 232.25$.
3. Deviations: $705 - 696.75 = 8.25$ and $224 - 232.25 = -8.25$ (in a two-category test they are always equal and opposite).
4. $\chi^2 = \dfrac{8.25^2}{696.75} + \dfrac{8.25^2}{232.25} = 0.0977 + 0.2931 = 0.391$.
5. Degrees of freedom $= 2 - 1 = 1$; critical value 3.841.

**Answer:** $\chi^2 \approx 0.39 < 3.84$ (p ≈ 0.53), so the data are fully consistent with 3 : 1. Pooling all seven traits (14 949 : 5010) gives $\chi^2 \approx 0.11$ with 1 df (p ≈ 0.74).

## 4. Extensions of Mendelian Inheritance

Mendel chose traits that behave simply. Most genes behave in more complicated ways, but all the extensions below still rest on segregation of alleles at meiosis; what changes is how genotypes map onto phenotypes.

### Incomplete dominance
Heterozygotes show an intermediate phenotype. Snapdragons: red (*RR*) × white (*rr*) → pink (*Rr*); F₂ 1 red : 2 pink : 1 white (genotypic and phenotypic ratios coincide). The reappearance of pure red and pure white in the F₂ is decisive evidence *against* blending: the alleles were not mixed in the pink F₁, only expressed together. In humans, familial hypercholesterolemia is partly intermediate (heterozygotes have moderately elevated LDL; homozygotes severely elevated).

### Codominance
Both alleles are fully expressed in heterozygotes. **MN blood group:** *L^ML^N* individuals have both M and N antigens. Sickle-cell trait at the molecular level: heterozygotes make both normal and sickle hemoglobin. The difference from incomplete dominance is in what we see: with codominance both parental products are detectable side by side, rather than a single intermediate amount.

### Multiple alleles: ABO blood groups
The *I* gene has three alleles: *I^A* and *I^B* (codominant) and *i* (recessive). The alleles encode versions of a glycosyltransferase enzyme: *I^A* adds N-acetylgalactosamine and *I^B* adds galactose to a precursor sugar chain (the H antigen) on the red-cell surface, while *i* encodes an inactive enzyme, leaving the H antigen unmodified.

| Blood type | Genotypes | Antigens on red cells | Antibodies in plasma | Can receive from |
|---|---|---|---|---|
| A | *I^AI^A*, *I^Ai* | A | Anti-B | A, O |
| B | *I^BI^B*, *I^Bi* | B | Anti-A | B, O |
| AB | *I^AI^B* | A and B | None | All (universal recipient) |
| O | *ii* | None | Anti-A and anti-B | O only (universal donor of red cells) |

With $k$ alleles at a locus, a diploid can have $k$ homozygous and $k(k-1)/2$ heterozygous genotypes, for $k(k+1)/2$ in total. For ABO, $k = 3$ gives 6 genotypes but only 4 phenotypes, because *I^AI^A* and *I^Ai* look alike, as do *I^BI^B* and *I^Bi*. Many genes have dozens of alleles in a population; the human HLA genes, which matter for transplant matching, have thousands.

The **Rh factor** (D antigen) is inherited separately (Rh⁺ dominant). **Hemolytic disease of the newborn** can occur when an Rh⁻ mother carries an Rh⁺ fetus: fetal red cells entering her circulation, usually at delivery, can sensitize her to make anti-D antibodies, which cross the placenta in a *later* pregnancy and destroy the red cells of an Rh⁺ fetus. Anti-D immunoglobulin (RhoGAM), given during pregnancy and after delivery, prevents maternal sensitization. Karl Landsteiner discovered ABO groups in 1901 (Nobel 1930).

### Epistasis
One gene affects the expression of another. **Labrador retrievers:** gene *B* (black *B* > brown *b*) determines pigment color; gene *E* determines whether pigment is deposited in fur — *ee* dogs are yellow regardless of *B*. *BbEe* × *BbEe* → 9 black : 3 brown (chocolate) : 4 yellow (a modified 9:3:3:1). The **Bombay phenotype** in humans (*hh*) masks ABO antigens: without the H precursor, neither the A nor the B enzyme has anything to modify, so an *hh* person with *I^A* or *I^B* alleles types as O.

**Derivation of 9 : 3 : 4.** Start from the dihybrid classes: 9/16 *B_E_*, 3/16 *bbE_*, 3/16 *B_ee*, 1/16 *bbee*. The *B_E_* dogs are black and the *bbE_* dogs are chocolate. Both *B_ee* and *bbee* are yellow, so those classes merge: 3/16 + 1/16 = 4/16. The underlying genotypes still segregate 9 : 3 : 3 : 1; epistasis only groups them differently. Other common groupings:

| F₂ ratio | Name | Biological basis | Classic example |
|---|---|---|---|
| 9 : 3 : 3 : 1 | No interaction | Two independent traits | Pea seed shape and color |
| 9 : 3 : 4 | Recessive epistasis | *ee* masks the *B* gene | Labrador coat color |
| 12 : 3 : 1 | Dominant epistasis | A dominant allele of one gene masks the other | Summer squash fruit color (white : yellow : green) |
| 9 : 7 | Duplicate recessive (complementary genes) | Two enzymes in one pathway; loss of either blocks the product | Sweet pea flower color (purple : white) |
| 15 : 1 | Duplicate dominant genes | Either gene alone suffices | Shepherd's purse capsule shape (triangular : ovoid) |
| 13 : 3 | Dominant suppression | A dominant allele of one gene suppresses the other | White Leghorn × White Wyandotte chicken plumage |
| 9 : 6 : 1 | Additive (duplicate interaction) | Each gene adds to the same phenotype | Summer squash fruit shape (disc : sphere : long) |

A modified ratio whose classes add up to sixteenths is the signature of two independently assorting genes affecting one trait.

### Polygenic inheritance
Many genes, each with small additive effects (plus environment), produce **continuous variation** — a bell-shaped distribution: height, skin color, intelligence-test scores, blood pressure, risk of type 2 diabetes.

**Derivation of the 1 : 6 : 15 : 20 : 15 : 6 : 1 distribution.** Suppose three unlinked genes each have a "contributing" allele (*A*, *B*, *C*) that adds one unit to the trait and a "non-contributing" allele (*a*, *b*, *c*) that adds nothing. In the F₂ of *AaBbCc* × *AaBbCc* each offspring receives six alleles (two per gene), and each has probability ½ of being a contributing one, independently. The number $k$ of contributing alleles is therefore binomial:
$$P(k) = \binom{6}{k}\left(\tfrac12\right)^6 = \frac{\binom{6}{k}}{64}, \qquad k = 0, 1, \ldots, 6 .$$
The binomial coefficients 1, 6, 15, 20, 15, 6, 1 give 7 phenotypic classes. With $n$ genes there are $2n + 1$ classes and the distribution is $\binom{2n}{k}/4^n$. As $n$ grows the binomial approaches a normal (Gaussian) curve, and environmental variation smooths the remaining steps — this is how Ronald Fisher reconciled Mendelian genes with continuous variation in 1918. Genome-wide association studies (GWAS) have identified thousands of variants affecting human height, each with tiny effects; a 2022 study of about 5.4 million people reported more than 12 000 independent associated variants.

### Pleiotropy
One gene affects multiple traits. **Sickle-cell allele:** a single base change in the β-globin gene replaces glutamate with valine at position 6 of the protein, and that one change causes anemia, pain crises, organ damage, and malaria resistance. **Marfan syndrome** (fibrillin-1 mutations): tall stature, long limbs, lens dislocation, aortic aneurysms. **Phenylketonuria:** intellectual disability and light pigmentation if untreated.

### Lethal alleles
Some genotypes are lethal, altering ratios. Yellow coat in mice (*A^Y*) is dominant for color but recessive lethal: *A^YA* × *A^YA* gives 2 yellow : 1 agouti (the *A^YA^Y* embryos die). The derivation is again conditional: at conception the ratio is ¼ *A^YA^Y* : ½ *A^YA* : ¼ *AA*; among survivors, P(yellow) = (½)/(¾) = 2/3. The tailless Manx cat shows the same pattern, and litters from Manx × Manx crosses are correspondingly smaller. The yellow-mouse 2 : 1 ratio, reported by Lucien Cuénot in 1905, was one of the first apparent "exceptions" to Mendel that turned out to confirm segregation.

### Penetrance and expressivity
- **Incomplete penetrance:** not all individuals with the genotype show the phenotype (e.g. *BRCA1* mutations confer ~55–72% lifetime breast cancer risk, not 100%). Penetrance is the fraction of individuals with the genotype who show the phenotype; for an autosomal dominant condition with penetrance 80%, the risk to a child of an affected heterozygote is ½ × 0.8 = 0.4.
- **Variable expressivity:** severity varies among individuals with the same genotype (e.g. neurofibromatosis).

### Gene–environment interaction
Phenotype = genotype + environment (+ interaction). **Hydrangea** flower color depends on soil pH; **Himalayan rabbits and Siamese cats** have a temperature-sensitive pigment enzyme, producing dark fur on cooler extremities; **PKU** is prevented by a low-phenylalanine diet. The range of phenotypes one genotype produces across environments is its **norm of reaction**.

### Inheritance that breaks Mendel's rules
- **Genomic imprinting:** for a small set of genes in mammals (on the order of 100–200), only the copy inherited from one parent is expressed, because the other is silenced by DNA methylation laid down in the egg or sperm. A deletion in chromosome region 15q11–q13 causes **Prader–Willi syndrome** when inherited from the father but **Angelman syndrome** when inherited from the mother — the same deletion, different diseases, depending on parental origin.
- **Maternal effect:** the phenotype of the offspring is determined by the *mother's genotype*, because the egg is pre-loaded with her gene products. The direction of shell coiling in the snail *Lymnaea* is the classic example.
- **Organelle (cytoplasmic) inheritance:** mitochondria and chloroplasts carry their own DNA and are usually transmitted through the egg (see the mitochondrial row of the pedigree table in Section 8).
- **Anticipation:** in disorders caused by expanding repeats, the repeat can lengthen from one generation to the next, giving earlier onset or greater severity. In Huntington's disease, 40 or more CAG repeats in the *HTT* gene are fully penetrant and 36–39 show reduced penetrance; in fragile X syndrome, more than 200 CGG repeats in *FMR1* silence the gene, while 55–200 repeats form an unstable "premutation" that can expand when passed on by a mother.

## 5. Chromosomes and Meiosis

### The chromosome theory of inheritance
Walter Sutton and Theodor Boveri (1902–1903) noted that chromosome behavior during meiosis parallels Mendel's factors: chromosomes come in pairs, as alleles do; homologs separate at meiosis, as alleles segregate; and different pairs orient independently, as different genes assort independently. Thomas Hunt Morgan's work with fruit flies (*Drosophila melanogaster*) from 1910 confirmed that genes reside on chromosomes (Nobel 1933). Two later results made the case conclusive: in 1916 Calvin Bridges showed that rare flies with exceptional sex-linked phenotypes had exactly the abnormal chromosome sets predicted by nondisjunction of the X, and in 1931 Harriet Creighton and Barbara McClintock (in maize) and Curt Stern (in *Drosophila*) showed that genetic recombination between markers is accompanied by a visible physical exchange between chromosomes.

### Chromosome basics
- Humans have **46 chromosomes** in 23 pairs: 22 pairs of **autosomes** and one pair of **sex chromosomes** (XX female, XY male). The number was established only in 1956, by Joe Hin Tjio and Albert Levan; for three decades before that, 48 had been the accepted figure.
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

**Mapping Mendel's laws onto meiosis.** The law of segregation is the separation of homologs in anaphase I (or, for a region beyond a crossover, of sister chromatids in anaphase II): a heterozygote *Aa* has *A* on one homolog and *a* on the other, so half the products receive each. The law of independent assortment is the random orientation of different bivalents at metaphase I: whether the maternal or paternal copy of chromosome 1 faces a given pole has no influence on chromosome 2. Linkage (Section 7) is the exception built into this picture — genes on the *same* chromosome travel together unless a crossover separates them.

**Sources of genetic variation:**
1. **Independent assortment** of homologs: each of the 23 pairs can orient in 2 ways, so there are $2^{23} = 8\,388\,608$ ≈ 8.4 million possible chromosome combinations per human gamete.
2. **Crossing over** (recombination) — on average ~1–3 crossovers per chromosome pair per meiosis — creates new allele combinations within chromosomes.
3. **Random fertilization:** $2^{23} \times 2^{23} = 2^{46} \approx 7.0 \times 10^{13}$ — about 70 trillion combinations per couple, before considering crossing over.
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
Failure of chromosomes to separate properly produces gametes with extra or missing chromosomes (**aneuploidy**). Where the error happens matters:
- **Nondisjunction in meiosis I** (homologs fail to separate): all four products are abnormal — two carry both homologs (n + 1) and two carry neither (n − 1).
- **Nondisjunction in meiosis II** (sister chromatids fail to separate in one of the two cells): two products are normal, one is n + 1 (carrying two copies of the *same* homolog) and one is n − 1.

Fertilization of an n + 1 gamete by a normal gamete gives a **trisomy** (2n + 1); of an n − 1 gamete, a **monosomy** (2n − 1).

- **Trisomy 21 (Down syndrome):** ~1 in 700 births; risk rises steeply with maternal age (about 1 in 1500 at age 20; 1 in 350 at 35; 1 in 30 at 45), mostly due to errors in maternal meiosis I. A leading explanation is that the cohesion holding bivalents together weakens during the decades-long arrest of oocytes in prophase I. Jérôme Lejeune, Marthe Gautier and Raymond Turpin identified the extra chromosome in 1959.
- **Trisomy 18** (Edwards) and **trisomy 13** (Patau): severe; usually fatal in infancy.
- **Sex chromosome aneuploidies:** Turner syndrome (45,X — the only viable monosomy), Klinefelter syndrome (47,XXY), XYY, triple X.
- Most autosomal aneuploidies are lethal early in development; ~50% of first-trimester miscarriages involve chromosomal abnormalities.
- **Polyploidy** (extra full sets) is lethal in humans but common in plants: wheat is hexaploid, strawberries octoploid; seedless bananas and watermelons are triploid.

Approximate birth frequencies of the commonest aneuploidies:

| Condition | Karyotype | Approximate frequency | Typical features |
|---|---|---|---|
| Down syndrome | 47,+21 | 1 in 700 births | Intellectual disability, heart defects, characteristic facial features |
| Edwards syndrome | 47,+18 | about 1 in 5000 births | Severe malformations; most die within the first year |
| Patau syndrome | 47,+13 | about 1 in 10 000–16 000 births | Severe malformations; most die within the first year |
| Klinefelter syndrome | 47,XXY | 1 in 500–1000 males | Tall stature, small testes, infertility |
| XYY | 47,XYY | about 1 in 1000 males | Usually tall; often undiagnosed |
| Triple X | 47,XXX | about 1 in 1000 females | Often mild or undiagnosed |
| Turner syndrome | 45,X | about 1 in 2000–2500 females | Short stature, ovarian failure; most 45,X conceptions miscarry |

**Structural abnormalities:** deletions (cri-du-chat syndrome, 5p−), duplications, inversions and translocations (a balanced Robertsonian translocation can cause familial Down syndrome).

## 6. Sex Determination and Sex-Linked Inheritance

- In mammals, the **SRY** gene on the Y chromosome triggers testis development; without it, ovaries develop. SRY was identified in 1990 (Andrew Sinclair, Peter Goodfellow, Robin Lovell-Badge and colleagues), partly by studying rare XX males who carry a fragment of the Y including SRY. (Birds use ZW systems — females are ZW; many reptiles use incubation temperature; honeybee males are haploid.)
- In *Drosophila*, by contrast, sex is set by the ratio of X chromosomes to autosome sets, and the Y is not sex-determining: XXY flies are female and XO flies are (sterile) males, the opposite of humans, where XXY is male (Klinefelter) and XO is female (Turner). Comparing the two showed that "having a Y" and "having one X" are different rules.
- **X-linked genes:** the X chromosome carries ~800–900 protein-coding genes; the Y only a few dozen. Males are **hemizygous** for X-linked genes, so a single recessive allele produces the phenotype.

**X-linked recessive inheritance:**
- More common in males.
- Affected males inherit the allele from their mothers (fathers pass Y, not X, to sons).
- Carrier mothers (heterozygous) pass the allele to half of their sons (affected) and half of their daughters (carriers).
- Affected fathers pass the allele to all daughters (carriers) and no sons.
- Examples: **red–green color blindness** (~8% of men of Northern European ancestry, ~0.5% of women), **hemophilia A** (factor VIII deficiency; roughly 1 in 5000 male births) and the rarer **hemophilia B** (factor IX deficiency), **Duchenne muscular dystrophy** (dystrophin — the largest human gene, ~2.2 Mb), G6PD deficiency.
- The "royal disease" spread from Queen Victoria, a carrier, through her son Leopold (affected) and her carrier daughters Alice and Beatrice into the royal families of Russia and Spain. DNA analysis of the remains of the Russian imperial family, published in 2009, showed that it was **hemophilia B**, caused by a mutation in the factor IX gene.

**Worked example 6.1:** a carrier woman (*X^HX^h*) and a normal man (*X^HY*) have children. Daughters: ½ *X^HX^H*, ½ *X^HX^h* (carriers), none affected. Sons: ½ *X^HY* (normal), ½ *X^hY* (hemophilia). Overall probability that a child has hemophilia: ¼.

**Worked example 6.2 (affected father, carrier mother).** A red–green color-blind man (*X^cY*) and a woman with normal vision whose father was color-blind have children. Find the probability that (a) a daughter is color-blind, (b) a son is color-blind, (c) a child of unknown sex is color-blind, and (d) two sons are both color-blind.
1. The woman received her father's only X, which carries *c*, and has normal vision, so she is *X^CX^c* (a carrier with certainty).
2. Daughters receive *X^c* from the father (always) and *X^C* or *X^c* from the mother (½ each). So ½ are *X^cX^c* (color-blind) and ½ are *X^CX^c* (carriers).
3. Sons receive Y from the father and *X^C* or *X^c* from the mother: ½ are *X^cY* (color-blind).
4. Unknown sex: P(daughter) × ½ + P(son) × ½ = ½ × ½ + ½ × ½ = ½.
5. Two sons are independent events: ½ × ½ = ¼.

**Answer:** (a) ½; (b) ½; (c) ½; (d) ¼. This cross is how color-blind women arise: they need a color-blind father *and* a mother who carries the allele.

**X-linked dominant:** affected fathers pass the trait to all daughters (e.g. hypophosphatemic rickets, Rett syndrome).
**Y-linked:** father to all sons (few genes; e.g. some male infertility genes).

**Morgan's white-eyed fruit flies (1910):** a white-eyed male crossed with red-eyed females gave all red-eyed F₁; the F₂ had a 3:1 ratio but **all white-eyed flies were male** — the first gene assigned to a specific chromosome (X). The **reciprocal cross** confirmed it: white-eyed females × red-eyed males gave red-eyed daughters (*X^wX^+*) and white-eyed sons (*X^wY*), because sons receive their only X from their mother. Different results from reciprocal crosses are a hallmark of sex linkage (or of cytoplasmic inheritance); for autosomal genes reciprocal crosses give identical results.

**Dosage compensation:** in female mammals, one X is inactivated (Lyonization, Mary Lyon, 1961). The inactive X condenses into a dark-staining **Barr body**, first seen in cat neurons by Murray Barr and Ewart Bertram in 1949. Inactivation happens early in embryonic development, independently in each cell, and the choice is then inherited by all descendants of that cell, so every female mammal is a mosaic of two cell populations. Calico and tortoiseshell cats are almost always female because orange/black fur alleles are X-linked and random X inactivation creates patches. (The rare male calico is usually XXY.) In people, the same mosaicism means carrier women of some X-linked disorders show patchy effects, such as patches of skin lacking sweat glands in carriers of X-linked hypohidrotic ectodermal dysplasia.

## 7. Linkage and Genetic Mapping

Genes close together on the same chromosome tend to be inherited together (**linked**) and do not assort independently. **Crossing over** between them produces recombinant gametes; the farther apart two genes are, the more often a crossover occurs between them. Linkage was first seen by William Bateson, Edith Saunders and Reginald Punnett in sweet peas in 1905, as an excess of parental combinations they called "coupling", but they did not connect it to chromosomes; Morgan did so in 1911.

The arrangement of alleles in a double heterozygote matters. In **coupling** (cis) the dominant alleles are on the same homolog, *AB*/*ab*; in **repulsion** (trans) they are on different homologs, *Ab*/*aB*. "Recombinant" always means a combination not present in the parent's two chromosomes, so the same offspring class can be parental in one case and recombinant in the other.

**Recombination frequency** = (number of recombinant offspring / total offspring) × 100%.
- 1% recombination = **1 map unit** = **1 centimorgan (cM)** (named after Morgan).
- Unlinked genes show 50% recombination (the maximum).
- In humans, 1 cM ≈ roughly 1 million base pairs on average.

**Why the maximum is 50%.** Crossing over happens at the four-chromatid stage. A single crossover between two loci involves only two of the four chromatids, so it yields two recombinant and two parental chromatids — 50% recombinants. Double crossovers can involve two, three or four of the chromatids; averaged over all possibilities (assuming the chromatids are chosen at random), they too give 50%. So however many crossovers occur, the recombinant fraction cannot exceed ½, and two loci far apart on one chromosome behave as though they were on different chromosomes.

Alfred Sturtevant, an undergraduate in Morgan's lab, worked out the first genetic map in 1911 and published it in 1913: six sex-linked factors in *Drosophila* (two of which behaved as a single locus, giving five map positions), arranged in a line using the insight that recombination frequencies are approximately additive.

**Worked example 7.1:** a test cross of *AaBb* (from a parent with *AB*/*ab* chromosomes) × *aabb* gives 420 *AaBb*, 410 *aabb*, 85 *Aabb*, 85 *aaBb*. Recombinants: 170/1000 = 17% → the genes are 17 cM apart.

**Three-point crosses** determine gene order (the double-crossover class is the rarest) and reveal **interference** (one crossover reduces the chance of another nearby). Interference is quantified by the **coefficient of coincidence**
$$\text{c.o.c.} = \frac{\text{observed double crossovers}}{\text{expected double crossovers}}, \qquad I = 1 - \text{c.o.c.},$$
where the expected number is (frequency in region 1) × (frequency in region 2) × (total), the product rule applied as if crossovers in the two regions were independent.

**Worked example 7.2 (a three-point test cross).** A plant heterozygous for three linked genes is test-crossed to *aabbcc*, and the 1000 offspring are classified by the alleles they received from the heterozygous parent: *ABC* 398, *abc* 407, *Abc* 45, *aBC* 40, *ABc* 55, *abC* 50, *AbC* 3, *aBc* 2. Find the gene order, the map distances and the interference.
1. **Parental classes** are the two most frequent: *ABC* and *abc* (805 in total). So the heterozygote was *ABC*/*abc*.
2. **Double-crossover classes** are the two rarest: *AbC* and *aBc* (5 in total).
3. **Gene order:** compare a double-crossover class with the parental class it most resembles. *AbC* differs from *ABC* only at B. A double crossover swaps the middle gene relative to the outer two, so **B is in the middle**: the order is A–B–C.
4. **A–B distance:** count every offspring recombinant between A and B (the A and B alleles in a non-parental combination): *Abc* 45 + *aBC* 40 + *AbC* 3 + *aBc* 2 = 90, i.e. 9.0 cM. The double crossovers must be included because each contains a crossover in this region.
5. **B–C distance:** *ABc* 55 + *abC* 50 + *AbC* 3 + *aBc* 2 = 110, i.e. 11.0 cM.
6. **A–C distance:** 9.0 + 11.0 = 20.0 cM. A direct two-point count of A–C recombinants would give only 45 + 40 + 55 + 50 = 190 (19.0%), because double crossovers restore the parental A–C combination and are invisible without the middle marker — this is why maps are built from short intervals.
7. **Interference:** expected double crossovers = 0.090 × 0.110 × 1000 = 9.9; observed 5. c.o.c. = 5/9.9 = 0.505, so $I = 1 - 0.505 \approx 0.49$.

**Answer:** order A–B–C; A–B 9.0 cM, B–C 11.0 cM; coefficient of coincidence ≈ 0.51 and interference ≈ 0.49 — a first crossover roughly halves the chance of a second nearby.

### From recombination frequency to map distance: the Haldane mapping function

Recombination frequencies add only for short intervals. Over longer distances they underestimate the true distance, because an even number of crossovers between two loci leaves them in the parental combination. In 1919 J. B. S. Haldane derived a correction assuming no interference.

**Derivation.** Define the map distance $d$ (in morgans; 1 M = 100 cM) between two loci as the *expected number* of crossovers between them on a single chromatid. If crossovers occur at random and independently along the chromosome, the number $k$ in the interval follows a Poisson distribution, $P(k) = e^{-d} d^k / k!$. A gamete is recombinant for the two flanking loci if and only if $k$ is odd. Hence
$$r = \sum_{k\ \text{odd}} \frac{e^{-d}d^k}{k!} = e^{-d}\left(d + \frac{d^3}{3!} + \frac{d^5}{5!} + \cdots\right) = e^{-d}\sinh d = \frac{1 - e^{-2d}}{2}.$$
Solving for $d$:
$$d = -\tfrac12 \ln(1 - 2r).$$
For small $d$, $e^{-2d} \approx 1 - 2d$, so $r \approx d$: short distances add. As $d \to \infty$, $r \to \tfrac12$, recovering the 50% ceiling. Real chromosomes show positive interference, so other functions (such as Kosambi's) are often used, but Haldane's shows clearly why the relation is curved.

| Map distance $d$ (cM) | 5 | 10 | 20 | 50 | 100 |
|---|---|---|---|---|---|
| Recombination frequency $r$ (Haldane) | 0.048 | 0.091 | 0.165 | 0.316 | 0.432 |

**Worked example 7.3.** Two loci show 30% recombination. Estimate their map distance with the Haldane function.
1. $r = 0.30$, so $1 - 2r = 0.40$.
2. $\ln 0.40 = -0.916$.
3. $d = -\tfrac12 \times (-0.916) = 0.458$ M.

**Answer:** about 46 cM, noticeably more than the naive 30 cM, because roughly a third of the crossover events in this interval are hidden by double crossovers.

### Genetic maps in humans

Experimental crosses are impossible in humans, so linkage is detected in family data with the **LOD score** (logarithm of the odds), introduced by Newton Morton in 1955:
$$\text{LOD}(\theta) = \log_{10} \frac{\theta^{k}(1 - \theta)^{n - k}}{(1/2)^{n}},$$
for $n$ informative meioses with $k$ recombinants and a trial recombination fraction $\theta$. It compares the likelihood of the data under linkage with that under free assortment. A LOD of 3 (odds of 1000 : 1) is the conventional threshold for declaring linkage. For example, 10 informative meioses with no recombinants give, at $\theta = 0$, $\text{LOD} = \log_{10} 2^{10} = 3.01$. Linkage mapping in families placed the Huntington's disease gene on chromosome 4 in 1983 and the cystic fibrosis gene on chromosome 7 in 1985, years before the genes themselves were isolated (cystic fibrosis in 1989, Huntington's disease in 1993).

Recombination is not uniform along chromosomes: most crossovers fall in narrow **hotspots** a few kilobases wide, and the human female genetic map is about 1.6 times longer than the male map, because oocytes undergo more crossovers per meiosis than spermatocytes. Genetic (cM) and physical (base-pair) maps therefore have the same gene order but different spacings.

## 8. Human Pedigree Analysis

Pedigree symbols: squares = males, circles = females, filled = affected, half-filled or dotted = carriers, horizontal line = mating, vertical line = offspring; generations numbered with Roman numerals. A double horizontal line marks a consanguineous mating, and an arrow marks the **proband** (the person through whom the family came to attention).

| Pattern | Key features | Examples |
|---|---|---|
| **Autosomal recessive** | Skips generations; affected children often have unaffected (carrier) parents; both sexes equally; more common with consanguinity | Cystic fibrosis (~1/2500–3500 among people of Northern European descent; carrier frequency ~1/25), sickle-cell disease, Tay–Sachs, PKU, albinism, spinal muscular atrophy |
| **Autosomal dominant** | Appears every generation; affected individual usually has an affected parent; ~50% of children of an affected heterozygote affected; both sexes | Huntington's disease (late onset — often after having children), Marfan syndrome, achondroplasia (mostly new mutations), familial hypercholesterolemia, neurofibromatosis type 1, polydactyly |
| **X-linked recessive** | Mostly males; transmitted through carrier females; no male-to-male transmission | Hemophilia, Duchenne MD, color blindness |
| **X-linked dominant** | Affected father → all daughters affected, no sons; more females affected | Hypophosphatemic rickets, fragile X (complex) |
| **Mitochondrial** | Transmitted only from mother to all children; variable severity (heteroplasmy) | Leber hereditary optic neuropathy, MELAS |

**A systematic approach to reading a pedigree:**
1. Are there affected children of two unaffected parents? If yes, the trait is recessive (or shows incomplete penetrance).
2. Is there male-to-male transmission? If yes, the trait cannot be X-linked.
3. Are affected individuals mostly male, with the trait passed through unaffected females? This suggests X-linked recessive.
4. Does an affected father have only affected daughters and unaffected sons? This suggests X-linked dominant.
5. Does every affected person have an affected parent, with roughly half of the children of affected people affected? This suggests autosomal dominant.
6. Test each candidate mode against *every* mating in the pedigree; one contradiction is enough to exclude it.

**Worked example 8.1 (genetic counseling with conditional probability).** A woman's brother has cystic fibrosis; she and both her parents are unaffected. She plans children with an unrelated partner from a population in which the carrier frequency is 1/25. What is the probability that their first child will have cystic fibrosis?
1. The brother is *aa*, so both unaffected parents must be carriers (*Aa* × *Aa*).
2. Before using any information about the woman, her genotype probabilities are ¼ *AA*, ½ *Aa*, ¼ *aa*.
3. She is unaffected, which rules out *aa*. Conditioning on this: P(*Aa* | unaffected) = (½)/(¾) = **2/3**, not ½ — a common mistake.
4. P(partner is a carrier) = 1/25.
5. If both are carriers, P(child *aa*) = ¼.
6. All three events are independent, so the risk is $\tfrac23 \times \tfrac1{25} \times \tfrac14 = \tfrac{2}{300} = \tfrac{1}{150}$.

**Answer:** 1/150 ≈ 0.67%, compared with a background risk of $\tfrac1{25} \times \tfrac1{25} \times \tfrac14 = 1/2500$ for two random members of the population. Carrier testing of both partners would replace these probabilities by near-certainties.

**Genetic counseling and testing:** carrier screening, prenatal diagnosis (amniocentesis, chorionic villus sampling, non-invasive prenatal testing from cell-free fetal DNA in maternal blood), preimplantation genetic testing, newborn screening. Counselors combine Mendelian probabilities, test results and family history, often with Bayes' theorem, and help families understand the uncertainty that remains.

## 9. Population Genetics

**Population genetics** studies allele frequencies in populations and how they change — the genetic basis of evolution.

### The Hardy–Weinberg principle
G. H. Hardy and Wilhelm Weinberg (1908, independently): in a large, randomly mating population with no mutation, migration or selection, allele and genotype frequencies remain constant from generation to generation.

The question arose from a misunderstanding. At a 1908 meeting where Reginald Punnett spoke on Mendelism and disease, the statistician Udny Yule argued that if brachydactyly (short fingers) were a Mendelian dominant, it should spread until three-quarters of people had it, which plainly had not happened. Punnett took the problem to his Cambridge colleague, the pure mathematician G. H. Hardy, who showed in a short letter to *Science* in 1908 that there is no tendency for a dominant allele to increase: allele frequencies stay where they are. Weinberg, a physician in Stuttgart, had reached the same result in a lecture earlier that year.

For a gene with two alleles with frequencies $p$ (dominant) and $q$ (recessive):
$$\boxed{p + q = 1}, \qquad \boxed{p^2 + 2pq + q^2 = 1}$$
where $p^2$ = frequency of homozygous dominant, $2pq$ = heterozygous, $q^2$ = homozygous recessive.

**Derivation.** Imagine all the gametes of the population in one pool, a fraction $p$ carrying *A* and $q$ carrying *a*. Random mating is equivalent to drawing two gametes independently from this pool. By the product and addition rules,
$$P(AA) = p \cdot p = p^2, \qquad P(Aa) = p \cdot q + q \cdot p = 2pq, \qquad P(aa) = q^2 ,$$
which is just the expansion $(p + q)^2 = 1$. Now compute the allele frequency in the next generation. All alleles of *AA* individuals and half of those of *Aa* individuals are *A*:
$$p' = p^2 + \tfrac12(2pq) = p(p + q) = p .$$
The allele frequency is unchanged, so the genotype frequencies of the following generation are again $p^2 : 2pq : q^2$. Two conclusions follow: Mendelian inheritance by itself preserves variation (unlike blending), and a single generation of random mating is enough to bring an autosomal locus to equilibrium, whatever the starting genotype frequencies.

**Extensions.** With three alleles of frequencies $p$, $q$, $r$ the genotype frequencies are the terms of $(p + q + r)^2$. For ABO with $p = f(I^A)$, $q = f(I^B)$, $r = f(i)$: type O $= r^2$, type A $= p^2 + 2pr$, type B $= q^2 + 2qr$, type AB $= 2pq$. For illustrative frequencies $p = 0.28$, $q = 0.06$, $r = 0.66$ these give O 43.6%, A 44.8%, B 8.3%, AB 3.4% — values typical of parts of Western Europe, and a reminder that the recessive allele *i* can be the commonest. For an X-linked gene, the frequency of affected males equals the allele frequency $q$, while affected females have frequency $q^2$; if the sexes start with different allele frequencies, the difference halves and changes sign each generation, so equilibrium is approached in damped oscillations rather than in one step.

**Conditions (assumptions) for equilibrium:**
1. No mutation.
2. Random mating.
3. No natural selection.
4. Very large population (no genetic drift).
5. No gene flow (migration).

Violation of any condition can cause evolution (change in allele frequencies). Hardy–Weinberg serves as a **null model** against which real populations are compared.

**Worked example 9.1:** cystic fibrosis affects about 1 in 2500 newborns of Northern European ancestry. $q^2 = 1/2500 \Rightarrow q = 0.02$, $p = 0.98$. Carrier frequency $2pq = 2(0.98)(0.02) \approx 0.039$ — about 1 in 25. Most copies of a rare recessive allele are hidden in heterozygous carriers, which is why selection against rare recessive alleles is slow.

**Worked example 9.2:** in a population, 36% of individuals show the recessive phenotype. $q = 0.6$, $p = 0.4$; homozygous dominant 16%, heterozygous 48%.

**Worked example 9.3 (testing for Hardy–Weinberg proportions).** The MN blood group is codominant, so every genotype can be counted directly. In a sample of 1000 people there are 298 *MM*, 489 *MN* and 213 *NN*. Are these consistent with Hardy–Weinberg equilibrium?
1. Count alleles: $2 \times 1000 = 2000$ alleles, of which *M* $= 2(298) + 489 = 1085$. So $p = 1085/2000 = 0.5425$ and $q = 0.4575$.
2. Expected counts: *MM* $= p^2 N = 294.31$; *MN* $= 2pqN = 496.39$; *NN* $= q^2 N = 209.31$.
3. $\chi^2 = \dfrac{(298 - 294.31)^2}{294.31} + \dfrac{(489 - 496.39)^2}{496.39} + \dfrac{(213 - 209.31)^2}{209.31} = 0.046 + 0.110 + 0.065 = 0.22$.
4. Degrees of freedom: 3 categories − 1 − 1 (because $p$ was estimated from the same data) = 1. Critical value 3.841.

**Answer:** $\chi^2 \approx 0.22 < 3.84$; the sample is consistent with Hardy–Weinberg proportions. A significant excess of homozygotes, by contrast, would suggest inbreeding, population substructure or genotyping errors.

**Worked example 9.4 (an X-linked locus).** About 8% of men of Northern European ancestry have red–green color blindness. Predict the frequency of color-blind women and of carrier women.
1. Males are hemizygous, so the frequency of affected males equals the allele frequency: $q = 0.08$, $p = 0.92$.
2. Affected women need two copies: $q^2 = 0.08^2 = 0.0064$, i.e. 0.64%.
3. Carrier women: $2pq = 2(0.92)(0.08) = 0.147$, i.e. about 15%.
4. Ratio of affected men to affected women: $q/q^2 = 1/q = 12.5$.

**Answer:** about 0.64% of women affected and about 15% carriers. The observed figure (~0.5%) is somewhat lower because "red–green color blindness" combines defects in two neighboring genes (red-pigment and green-pigment opsins); a woman carrying one defective red allele and one defective green allele on different X chromosomes usually has normal color vision.

### Mechanisms of evolutionary change
- **Natural selection:** differential survival and reproduction (directional, stabilizing, disruptive, balancing; heterozygote advantage, e.g. sickle-cell in malarial regions).
- **Genetic drift:** random changes in allele frequencies, strongest in small populations. **Founder effect** (e.g. high frequency of Ellis–van Creveld syndrome in the Old Order Amish; Tay–Sachs and other alleles in Ashkenazi Jewish populations) and **bottleneck effect** (northern elephant seals were hunted down to perhaps 20–100 individuals by the 1890s and, despite recovering to well over 100 000, retain very little genetic variation; cheetahs).
- **Gene flow:** migration transferring alleles between populations, reducing differences.
- **Mutation:** the ultimate source of new alleles (slow on its own).
- **Non-random mating:** inbreeding increases homozygosity (revealing recessive disorders); assortative mating.

### Selection: deriving the change in allele frequency

Let the genotypes have relative fitnesses (relative survival × reproduction) $w_{AA} = 1 - s$, $w_{Aa} = 1$, $w_{aa} = 1 - t$, where $s$ and $t$ are selection coefficients. After selection, the genotype frequencies are proportional to $p^2(1 - s)$, $2pq$ and $q^2(1 - t)$, and the **mean fitness** is
$$\bar{w} = p^2(1 - s) + 2pq + q^2(1 - t) = 1 - sp^2 - tq^2 .$$
The frequency of *a* among the survivors is
$$q' = \frac{pq + q^2(1 - t)}{\bar{w}} .$$
Subtracting $q$ and simplifying the numerator, $pq + q^2 - tq^2 - q(1 - sp^2 - tq^2) = -tq^2(1 - q) + sp^2q = pq(sp - tq)$, so
$$\Delta q = q' - q = \frac{pq\,(sp - tq)}{\bar{w}} .$$
Three useful special cases follow.

- **Selection against a recessive** ($s = 0$): $\Delta q = -tpq^2/(1 - tq^2)$. When $q$ is small, $\Delta q \approx -tq^2$, which is tiny — rare recessive alleles are almost invisible to selection because nearly all copies sit in heterozygotes.
- **A recessive lethal** ($s = 0$, $t = 1$): $\Delta q = -pq^2/(1 - q^2) = -q^2/(1 + q)$, so $q' = q/(1 + q)$. Taking reciprocals, $1/q' = 1/q + 1$: the reciprocal of the allele frequency rises by exactly 1 per generation, giving
$$\frac{1}{q_t} = \frac{1}{q_0} + t \quad\Longrightarrow\quad t = \frac{1}{q_t} - \frac{1}{q_0} \text{ generations.}$$
- **Heterozygote advantage** ($s > 0$, $t > 0$): $\Delta q = 0$ when $sp = tq$, i.e. at the stable equilibrium
$$\hat{q} = \frac{s}{s + t} .$$
If $q$ is below $\hat q$, $sp > tq$ and $q$ rises; if above, it falls. Both alleles are maintained indefinitely (**balancing selection**).

A fourth balance arises between new mutation (rate $\mu$ per generation) and selection against a recessive: the equilibrium is $\hat{q} \approx \sqrt{\mu/t}$, which explains why harmful recessive alleles persist at low but steady frequencies.

**Worked example 9.5 (how slowly selection removes a recessive lethal).** A recessive allele is lethal before reproduction in homozygotes and has frequency $q_0 = 0.02$. Assuming no new mutation, how many generations are needed to halve its frequency, and to halve it again?
1. Use $t = 1/q_t - 1/q_0$.
2. From 0.02 to 0.01: $t = 100 - 50 = 50$ generations.
3. From 0.01 to 0.005: $t = 200 - 100 = 100$ generations.

**Answer:** 50 generations (over 1000 years in humans at 25 years per generation), then a further 100. Each halving takes twice as long as the previous one. This is why eugenic proposals to eliminate recessive disorders by preventing affected people from reproducing were not only unethical but also biologically futile.

**Worked example 9.6 (sickle-cell balancing selection).** In a region with intense malaria, suppose the relative fitnesses are 0.88 for *AA* (susceptible to malaria), 1 for *AS* (protected) and 0.20 for *SS* (sickle-cell disease without modern treatment). These are illustrative values. Find the equilibrium frequency of the *S* allele and of affected births.
1. Here $s = 1 - 0.88 = 0.12$ (against *AA*) and $t = 1 - 0.20 = 0.80$ (against *SS*).
2. $\hat{q} = s/(s + t) = 0.12/0.92 = 0.130$.
3. Births with sickle-cell disease: $\hat{q}^2 = 0.130^2 = 0.017$.

**Answer:** about 13% of alleles are *S*, and about 1.7% of births are *SS*. Allele frequencies of this order are found in parts of sub-Saharan Africa. Where malaria is absent, *s* is effectively zero and the *S* allele slowly declines — one reason the allele is rarer among people of African descent in the Americas than in malarial regions of Africa.

### Genetic drift and inbreeding

In a finite population of $N$ diploid individuals, each generation's $2N$ gene copies are a random sample of the previous generation's. Sampling error changes allele frequencies at random, and eventually one allele is **fixed** and the other lost. The probability that two gene copies drawn from the new generation are copies of the *same* parental gene is $1/(2N)$; such pairs are necessarily identical. This leads to the decay of expected heterozygosity:
$$H_t = H_0\left(1 - \frac{1}{2N}\right)^{t} \approx H_0\, e^{-t/(2N)} .$$
The probability that a new neutral mutation is eventually fixed equals its initial frequency, $1/(2N)$. In real populations $N$ is replaced by the **effective population size** $N_e$, which is usually much smaller than the census size because of unequal sex ratios, variation in family size and fluctuations over time.

**Inbreeding** (mating between relatives) increases homozygosity without changing allele frequencies. The **inbreeding coefficient** $F$ is the probability that the two alleles at a locus in an individual are identical by descent (copies of a single ancestral allele). Genotype frequencies become
$$f(AA) = p^2 + Fpq, \qquad f(Aa) = 2pq(1 - F), \qquad f(aa) = q^2 + Fpq .$$
For the child of first cousins, $F = 1/16$; for the child of full siblings, $F = 1/4$.

**Worked example 9.7 (drift in a small population).** A captive population is kept at $N = 50$ breeding individuals (assume this is also the effective size). What fraction of its initial heterozygosity remains after 100 generations? Compare with $N = 500$.
1. Per generation, heterozygosity is multiplied by $1 - 1/(2N) = 1 - 1/100 = 0.99$.
2. After 100 generations: $0.99^{100} = 0.366$.
3. For $N = 500$: $(1 - 1/1000)^{100} = 0.905$.

**Answer:** about 37% remains with 50 individuals (close to $e^{-1}$), but about 90% with 500. Conservation breeding programs therefore manage pedigrees to maximize $N_e$.

**Worked example 9.8 (consanguinity and recessive disease).** A recessive disorder has allele frequency $q = 0.01$. How much more likely is an affected child from a first-cousin marriage than from a random marriage?
1. Random mating: $f(aa) = q^2 = 0.0001$ (1 in 10 000).
2. First cousins, $F = 1/16$: $f(aa) = q^2 + Fpq = 0.0001 + \tfrac{1}{16}(0.99)(0.01) = 0.0001 + 0.000619 = 0.00072$.
3. Ratio: $0.00072/0.0001 \approx 7.2$.

**Answer:** about 1 in 1400 versus 1 in 10 000, roughly a sevenfold increase. The rarer the allele, the larger the relative increase, which is why rare recessive disorders are disproportionately found in children of consanguineous unions, even though the absolute risk remains small.

### Linkage disequilibrium

Alleles at two loci are in **linkage equilibrium** when the frequency of each two-locus haplotype equals the product of the allele frequencies, e.g. $f(AB) = p_A p_B$. The deviation $D = f(AB) - p_A p_B$ is the **linkage disequilibrium**. Under random mating, recombination breaks up associations at a rate set by the recombination fraction $r$:
$$D_t = (1 - r)^t D_0 .$$
For unlinked loci ($r = 0.5$) $D$ halves each generation, but for loci 1 cM apart ($r = 0.01$) about 37% of the initial association survives after 100 generations. This persistence is what allows GWAS to detect a causal variant through nearby marker SNPs, and it is a fundamental bridge between Mendel's law of independent assortment and population genetics.

### Heritability
**Broad-sense heritability** $H^2 = V_G/V_P$ is the fraction of phenotypic variance in a population attributable to genetic variance; **narrow-sense** $h^2 = V_A/V_P$ uses additive genetic variance (predicts response to selection: $R = h^2S$, the breeder's equation). Here $V_P = V_G + V_E$ (ignoring interaction and covariance), and $V_G = V_A + V_D + V_I$ splits into additive, dominance and epistatic (interaction) parts. Estimated from twin and adoption studies and from genomic data. Human height has $h^2 \approx 0.8$. Heritability describes a population in a given environment; it says nothing about how much of an individual's trait is "due to genes" and does not imply that a trait is unchangeable.

**Why only $V_A$ predicts selection response.** A parent passes on one allele per gene, not its genotype, so dominance and epistatic interactions are broken up every generation; only the average (additive) effects of alleles are reliably transmitted. The breeder's equation follows from regression: the slope of offspring mean on mid-parent value is $h^2$, so if selected parents exceed the population mean by $S$ (the **selection differential**), their offspring exceed it by $R = h^2 S$ (the **response**).

**Twin studies.** Identical (monozygotic, MZ) twins share all their genes; fraternal (dizygotic, DZ) twins share half their segregating genes on average. In the simplest model (additive genes plus a shared family environment $c^2$), the twin correlations are $r_{MZ} = h^2 + c^2$ and $r_{DZ} = \tfrac12 h^2 + c^2$. Subtracting gives **Falconer's formula**:
$$h^2 = 2(r_{MZ} - r_{DZ}), \qquad c^2 = 2r_{DZ} - r_{MZ} .$$

**Worked example 9.9 (selection response and twin estimates).** (a) In a population of a crop plant, mean height is 100 cm. Plants with a mean height of 110 cm are chosen as parents, and $h^2 = 0.40$. Predict the mean of the next generation. (b) For a human trait, twin correlations are $r_{MZ} = 0.86$ and $r_{DZ} = 0.47$. Estimate $h^2$ and $c^2$.
1. (a) Selection differential $S = 110 - 100 = 10$ cm.
2. Response $R = h^2 S = 0.40 \times 10 = 4$ cm.
3. Predicted offspring mean $= 100 + 4 = 104$ cm. Only 40% of the parents' advantage is transmitted because the rest of their superiority was environmental or non-additive.
4. (b) $h^2 = 2(0.86 - 0.47) = 0.78$.
5. $c^2 = 2(0.47) - 0.86 = 0.08$; the remaining $1 - 0.78 - 0.08 = 0.14$ is attributed to unique environment and measurement error.

**Answer:** (a) 104 cm; (b) $h^2 \approx 0.78$, $c^2 \approx 0.08$. These estimates assume, among other things, that MZ and DZ twins share their environments to the same degree.

## 10. Historical Development

| Year | People | Contribution |
|---|---|---|
| 1865–1866 | Gregor Mendel | Presents (1865) and publishes (1866) the laws of segregation and independent assortment |
| 1879–1882 | Walther Flemming | Describes the behavior of chromosomes in cell division and names mitosis |
| 1883 | Edouard van Beneden | Shows that egg and sperm of the roundworm *Ascaris* each contribute half the chromosome number |
| 1888 | Wilhelm Waldeyer | Coins the word "chromosome" |
| 1900 | Hugo de Vries, Carl Correns, Erich von Tschermak | Rediscover Mendel's work; Karl Pearson publishes the chi-square test |
| 1901 | Karl Landsteiner | Discovers the ABO blood groups |
| 1902 | Archibald Garrod | Explains alkaptonuria as a recessive trait; later calls such disorders "inborn errors of metabolism" (1908) |
| 1902–1903 | Walter Sutton, Theodor Boveri | Chromosome theory of inheritance |
| 1905 | William Bateson, Edith Saunders, Reginald Punnett | First observation of linkage ("coupling") in sweet peas |
| 1905–1906 | William Bateson | Coins the word "genetics" |
| 1908 | G. H. Hardy, Wilhelm Weinberg | Hardy–Weinberg principle |
| 1909 | Wilhelm Johannsen | Coins "gene", "genotype" and "phenotype" |
| 1910 | Thomas Hunt Morgan | White-eyed *Drosophila*; first gene assigned to a chromosome |
| 1913 | Alfred Sturtevant | First genetic map |
| 1916 | Calvin Bridges | Nondisjunction of the X as proof of the chromosome theory |
| 1918 | Ronald Fisher | Shows that many Mendelian genes produce continuous variation; introduces the term "variance" |
| 1919 | J. B. S. Haldane | Mapping function relating recombination to map distance |
| 1927 | Hermann Muller | X-rays induce mutations (Nobel 1946) |
| 1931 | Harriet Creighton and Barbara McClintock; Curt Stern | Physical demonstration of crossing over |
| 1949 | Murray Barr, Ewart Bertram | Discover the Barr body |
| 1956 | Joe Hin Tjio, Albert Levan | Human chromosome number is 46 |
| 1959 | Lejeune, Gautier and Turpin; Ford and colleagues; Jacobs and Strong | Trisomy 21 in Down syndrome; 45,X in Turner syndrome; 47,XXY in Klinefelter syndrome |
| 1961 | Mary Lyon | X-chromosome inactivation hypothesis |
| 1990 | Sinclair, Goodfellow, Lovell-Badge and colleagues | Identification of SRY |
| 2003 | Human Genome Project | Essentially complete human genome sequence |
| 2022 | Telomere-to-Telomere Consortium | First gapless sequence of a human genome (the Y chromosome followed in 2023) |

The early twentieth century also saw a bitter dispute between **Mendelians** (led by Bateson), who studied discrete traits, and **biometricians** (Karl Pearson and W. F. R. Weldon), who measured continuous variation and doubted that Mendel's particles could explain it. Fisher's 1918 paper ended the dispute by showing that both were describing the same process, and the work of Fisher, Haldane and Sewall Wright in the 1920s and 1930s fused Mendelian genetics with Darwinian selection into the **modern synthesis** of evolutionary biology.

## 11. Applications in Medicine, Agriculture and Everyday Life

- **Genetic counseling and screening.** Carrier screening for cystic fibrosis, Tay–Sachs disease, spinal muscular atrophy and the hemoglobin disorders uses exactly the probabilities derived in Sections 3, 8 and 9. Newborn screening began with Robert Guthrie's blood-spot test for PKU in the early 1960s; a PKU infant put on a low-phenylalanine diet develops normally — the clearest demonstration that "genetic" does not mean "untreatable".
- **Gene therapy and gene editing.** Onasemnogene abeparvovec, which delivers a working *SMN1* gene to infants with spinal muscular atrophy, was approved in the United States in 2019. In late 2023 the United Kingdom and then the United States approved the first CRISPR-based therapy (exagamglogene autotemcel) for sickle-cell disease, with approval for transfusion-dependent β-thalassemia following in both countries; it edits patients' own blood stem cells to switch fetal hemoglobin back on.
- **Pharmacogenetics.** Inherited variants change drug responses: people with two low-activity alleles of *TPMT* can suffer severe toxicity from standard doses of thiopurine drugs, and variants of the liver enzyme gene *CYP2C19* alter activation of the anti-clotting drug clopidogrel. Testing before treatment allows the dose or drug to be adjusted.
- **Transfusion and transplantation.** ABO and Rh typing make blood transfusion safe; HLA matching, governed by highly polymorphic linked genes inherited as blocks (haplotypes), explains why a sibling has a one-in-four chance of being an identical HLA match.
- **Plant and animal breeding.** The breeder's equation guides selection programs. Hybrid maize exploits **heterosis** (hybrid vigor), the superior performance of crosses between inbred lines. The semi-dwarf wheat varieties of the Green Revolution carry *Rht* alleles that make plants less responsive to gibberellin — the same hormone pathway affected by Mendel's tall/dwarf gene. Seedless watermelons are triploids produced by crossing tetraploid and diploid parents; the odd number of chromosome sets prevents normal meiosis, so seeds do not develop. Since about 2009, dairy cattle breeding has used **genomic selection**, predicting breeding values from thousands of DNA markers.
- **Forensic DNA profiling.** A DNA profile records the alleles at short tandem repeat (STR) loci; the US national database (CODIS) has used 20 core loci since 2017. The **random match probability** is computed with Hardy–Weinberg genotype frequencies ($p^2$ for homozygotes, $2pq$ for heterozygotes) multiplied across loci, assuming the loci are in linkage equilibrium.

**Worked example 11.1 (random match probability).** A crime-scene profile at three unlinked STR loci is: locus 1 heterozygous for alleles with frequencies 0.10 and 0.20; locus 2 homozygous for an allele with frequency 0.15; locus 3 heterozygous for alleles with frequencies 0.05 and 0.30. Estimate the probability that a random unrelated person has the same profile.
1. Locus 1: $2pq = 2(0.10)(0.20) = 0.040$.
2. Locus 2: $p^2 = 0.15^2 = 0.0225$.
3. Locus 3: $2pq = 2(0.05)(0.30) = 0.030$.
4. Product rule across independent loci: $0.040 \times 0.0225 \times 0.030 = 2.7 \times 10^{-5}$.

**Answer:** about 1 in 37 000 for just three loci; with 20 loci the probability becomes astronomically small. In practice laboratories apply corrections for population substructure and relatedness, because close relatives share alleles far more often than the product rule assumes.

- **Conservation.** Small, isolated populations suffer inbreeding depression and loss of variation (Worked examples 9.7 and 9.8). When the Florida panther population had dwindled to a few dozen animals with heart defects and poor sperm quality, eight female pumas from Texas were released in 1995; the resulting gene flow (**genetic rescue**) was followed by a marked increase in numbers and health.
- **Ancestry and relatedness.** Consumer genomics estimates relationships from the total length (in centimorgans) of DNA segments shared identical by descent: first cousins share about one-eighth of their genome on average, but the actual amount varies because of the randomness of assortment and crossing over.

## 12. Connections to Other Subjects

- **Mathematics.** Genetics was one of the first sciences built on probability: the product and addition rules, conditional probability and Bayes' theorem (counseling), the binomial theorem (polygenic traits, family outcomes), the Poisson process (Haldane's mapping function) and exponential decay (heterozygosity, linkage disequilibrium). The Wright–Fisher model of drift is a Markov chain; the recurrence $1/q_{t+1} = 1/q_t + 1$ is a simple difference equation.
- **Statistics.** Pearson's chi-square test, Fisher's analysis of variance, maximum likelihood and LOD scores were all developed in close connection with genetics, and the concept of variance itself was introduced in a genetics paper.
- **Chemistry.** Alleles differ in DNA sequence; a change of one base can swap one amino acid (glutamate → valine in sickle hemoglobin) and alter a protein's charge, solubility and folding. Enzyme deficiencies (phenylalanine hydroxylase in PKU, starch-branching enzyme in wrinkled peas) link genotype to metabolism. Blood-group antigens are carbohydrates attached by glycosyltransferases. See the molecular biology chapter for DNA replication, transcription and translation.
- **Physics.** Hermann Muller showed in 1927 that X-rays raise the mutation rate, founding radiation genetics and informing radiation-protection standards; ultraviolet light causes mutations by forming pyrimidine dimers in DNA. X-ray diffraction revealed the structure of DNA, explaining how genetic information is copied.
- **Cell biology.** Mendel's laws are the visible consequence of chromosome behavior in meiosis, and nondisjunction is a failure of the spindle and cohesion machinery described in the cell biology chapter.
- **Evolution and ecology.** Hardy–Weinberg is the null model of evolution; selection, drift, mutation and gene flow are the forces of change discussed in the evolution chapter. Conservation biology uses effective population size and inbreeding to plan the management of endangered species.
- **Computer science.** Genetic algorithms borrow mutation, recombination and selection to solve optimization problems, and genome analysis is a major application of algorithms for sequence alignment and large-scale statistics.

## 13. Common Misconceptions

- **"Dominant alleles are more common."** Dominance describes the heterozygote's phenotype, not frequency. Polydactyly and Huntington's disease are dominant but rare; the recessive *i* allele is the commonest ABO allele in many populations. Allele frequencies are set by history, selection and drift.
- **"Dominant alleles will spread until three-quarters of the population shows the trait."** This was Yule's error. The 3 : 1 ratio applies only to the offspring of two heterozygotes; Hardy–Weinberg shows that, without selection, allele frequencies do not change at all.
- **"A dominant allele suppresses or destroys the recessive one."** The recessive allele is untouched and is passed on intact — that is why it reappears in the F₂. Dominance usually just means one functional copy is enough.
- **"Recessive alleles are harmful and dominant ones beneficial."** Many recessive alleles are harmless variants (blue eyes, blood type O), and many dominant alleles cause disease (Huntington's disease, achondroplasia, familial hypercholesterolemia).
- **"Each trait is controlled by one gene."** Most traits, including height, skin color and the risk of common diseases, are polygenic and environmentally influenced. Phrases like "the gene for intelligence" are misleading.
- **"If two carriers already have an affected child, their next three children will be unaffected."** Each child is an independent event with probability ¼; the process has no memory. A 1 in 4 risk is a probability per child, not a schedule.
- **"High heritability means a trait cannot be changed."** Heritability is a ratio of variances in one population and one environment. Human height is highly heritable, yet average height rose substantially in many countries during the twentieth century as nutrition improved; PKU is entirely genetic but fully treatable by diet.
- **"Heritability tells what fraction of my trait comes from my genes."** It is a population statistic and has no meaning for an individual; a heritability of 0.8 does not mean that 80% of one person's height is genetic.
- **"Sons can inherit X-linked traits from their fathers."** A father gives his son a Y chromosome, never his X. An X-linked recessive condition in a son always comes through the mother (or a new mutation).
- **"Crossing over happens in meiosis II" or "meiosis II halves the chromosome number."** Crossing over happens in prophase I, and the reduction from diploid to haploid happens in meiosis I, when homologs separate; meiosis II separates sister chromatids, like mitosis.
- **"Siblings share exactly 50% of their DNA."** They share 50% *on average* (identical by descent), but the actual amount varies between sibling pairs because of independent assortment and crossing over.
- **"More chromosomes means a more complex organism."** The fern *Ophioglossum* has far more chromosomes than any mammal, and dogs have more than humans.
- **"Mendel's laws apply to every gene."** Linked genes, imprinted genes, mitochondrial genes, maternal-effect genes and repeat-expansion disorders all deviate from simple Mendelian expectations, though all are explained by the same underlying chromosome mechanics.
- **"Acquired characteristics are inherited."** Muscles built by exercise or skills learned in life are not encoded in germ-line DNA and are not transmitted genetically; some epigenetic marks can be passed on in limited cases, but this is not a general mechanism of heredity.

## 14. Practice Problems

1. (Conceptual) Red snapdragons crossed with white snapdragons give all pink F₁ plants. A student says this proves that inheritance is blending. What F₂ result shows that the student is wrong, and why?
2. For the cross *AaBbCcDd* × *AaBbCcDd* (four unlinked genes, complete dominance), find the fraction of offspring that are (a) heterozygous at all four loci, (b) dominant in phenotype for all four traits, and (c) recessive in phenotype for at least one trait. (d) For the different cross *AaBbCcDd* × *AabbCcDd*, what fraction of offspring are *aabbccdd*?
3. A mother has blood type A and her child has type O. Two men are named as possible fathers: one has type AB and the other has type B. Which man can be excluded, and what is the probability that a type B man who is *I^Bi* and a mother who is *I^Ai* produce a type O child?
4. Manx cats are tailless because of a dominant allele *M* that is lethal in homozygotes. Two Manx cats are crossed. What fraction of the surviving kittens are expected to be Manx, and how does the expected litter size compare with that of a cross between two tailed cats?
5. In an F₂ of 800 sweet-pea plants, 459 have purple flowers and 341 white. Use chi-square to test the fit to (a) a 9 : 7 ratio and (b) a 3 : 1 ratio. What does the result suggest about the number of genes involved?
6. A plant of genotype *Ab*/*aB* is test-crossed with *aabb*, giving 46 *AaBb*, 44 *aabb*, 205 *Aabb* and 205 *aaBb*. (a) What is the map distance between the genes? (b) Predict the numbers of each class among 1000 offspring of a test cross of an *AB*/*ab* plant.
7. Three genes on one chromosome have pairwise recombination frequencies A–B 12%, B–C 7% and A–C 5%. Determine the gene order.
8. A woman with normal blood clotting has a brother with hemophilia; their parents are unaffected. (a) What is the probability that she is a carrier? (b) What is the probability that her first son will have hemophilia? (c) (Harder) She later has three sons, none of whom has hemophilia. Use Bayes' theorem to update the probability that she is a carrier.
9. In a population, phenylketonuria (autosomal recessive) affects 1 in 10 000 newborns. Assuming Hardy–Weinberg equilibrium, find the allele frequency, the carrier frequency, and the ratio of carriers to affected individuals.
10. (Conceptual) A boy with red–green color blindness has a 47,XXY karyotype. His father has normal color vision and his mother is a carrier. In which parent, and at which meiotic division, did nondisjunction most likely occur? Ignore crossing over.
11. In a sheep flock, mean fleece weight is 4.0 kg. Rams and ewes averaging 5.0 kg are selected as parents, and the narrow-sense heritability is 0.35. Predict the mean fleece weight of their offspring, and the mean after five generations of the same selection differential (assume $h^2$ stays constant).
12. (a) How many genotypes are possible at a locus with 10 alleles, and how many of them are heterozygous? (b) A population of effective size 25 starts with heterozygosity 0.60. What heterozygosity is expected after 20 generations of drift?

### Solutions

**1.** Self the pink F₁. The F₂ contains 1 red : 2 pink : 1 white. Pure red and pure white plants reappear unchanged, which would be impossible if the red and white hereditary factors had been mixed into a single pink substance. The F₁ is pink because both alleles are expressed in the heterozygote (incomplete dominance), but they remain separate and segregate at meiosis.

**2.** Treat each gene separately and multiply.
(a) P(heterozygous) = ½ per gene, so $(1/2)^4 = 1/16$.
(b) P(dominant phenotype) = ¾ per gene, so $(3/4)^4 = 81/256 \approx 0.316$.
(c) Complement of (b): $1 - 81/256 = 175/256 \approx 0.684$.
(d) P(*aa*) = ¼ from *Aa* × *Aa*; P(*bb*) = ½ from *Bb* × *bb*; P(*cc*) = ¼; P(*dd*) = ¼. Product: $\tfrac14 \times \tfrac12 \times \tfrac14 \times \tfrac14 = 1/128$.

**3.** The type O child is *ii*, so it received an *i* allele from each parent. The type AB man is *I^AI^B* and has no *i* allele to give, so he is excluded. A type B man could be *I^Bi* and cannot be excluded (blood groups can exclude paternity but cannot prove it). For *I^Ai* × *I^Bi*: P(*i* from mother) × P(*i* from father) = ½ × ½ = ¼.

**4.** *Mm* × *Mm* gives ¼ *MM* (dies before birth), ½ *Mm* (Manx), ¼ *mm* (tailed). Among survivors, P(Manx) = (½)/(¾) = 2/3, so the expected ratio is 2 Manx : 1 tailed. Because a quarter of the embryos die, the expected litter size is about three-quarters of that from a tailed × tailed cross (other things equal).

**5.** (a) Expected for 9 : 7 out of 800: 450 and 350. $\chi^2 = 9^2/450 + 9^2/350 = 0.180 + 0.231 = 0.411$ with 1 df; this is below 3.841 (p ≈ 0.52), so 9 : 7 fits. (b) Expected for 3 : 1: 600 and 200. $\chi^2 = 141^2/600 + 141^2/200 = 33.1 + 99.4 = 132.5$, far above 6.635, so 3 : 1 is decisively rejected. A ratio in sixteenths points to two independently assorting genes, both needed for purple pigment (complementary genes): only *C_P_* plants (9/16) are purple.

**6.** (a) The parent's chromosomes are *Ab* and *aB*, so the parental offspring are *Aabb* and *aaBb* (410), and the recombinants are *AaBb* and *aabb* (46 + 44 = 90). Recombination frequency = 90/500 = 18%, so the genes are 18 cM apart. (b) For *AB*/*ab*, the parental classes are now *AaBb* and *aabb*, each (1 − 0.18)/2 = 41%, and the recombinant classes *Aabb* and *aaBb* each 9%. Among 1000 offspring: about 410 *AaBb*, 410 *aabb*, 90 *Aabb*, 90 *aaBb*.

**7.** The largest distance (A–B, 12) should span the other two: A–C + C–B = 5 + 7 = 12. So C lies between A and B, and the order is **A–C–B** (equivalently B–C–A).

**8.** (a) Her brother received his X from their mother, and the mother is unaffected, so the mother is a carrier (ignoring a new mutation). The woman received one of her mother's two X chromosomes: P(carrier) = ½.
(b) P(carrier) × P(she passes *X^h*) = ½ × ½ = ¼.
(c) Prior: P(carrier) = ½, P(non-carrier) = ½. Likelihood of three unaffected sons: if she is a carrier, $(1/2)^3 = 1/8$; if not, 1. Posterior:
$$P(\text{carrier} \mid 3 \text{ unaffected sons}) = \frac{\tfrac12 \times \tfrac18}{\tfrac12 \times \tfrac18 + \tfrac12 \times 1} = \frac{1/16}{9/16} = \frac19 .$$
The evidence of three unaffected sons lowers her carrier probability from 1/2 to 1/9 (and the risk to her next son to 1/18).

**9.** $q^2 = 1/10\,000$, so $q = 0.01$ and $p = 0.99$. Carrier frequency $2pq = 2(0.99)(0.01) = 0.0198$, about 1 in 50.5. Ratio of carriers to affected: $0.0198/0.0001 = 198$. For every person with PKU there are roughly 200 unaffected carriers.

**10.** The boy is color-blind, so both his X chromosomes carry *c* (*X^cX^cY*). The father's X carries *C*, so neither X came from the father; the father contributed the Y. Both X chromosomes came from the mother (*X^CX^c*), and they carry the *same* allele *c*. In meiosis I, nondisjunction would have sent both homologs (*X^C* and *X^c*) into one egg, giving *X^CX^c* — normal vision. Two copies of *X^c* require the sister chromatids of the *X^c* homolog to fail to separate, so the error occurred in **maternal meiosis II**.

**11.** $S = 5.0 - 4.0 = 1.0$ kg; $R = h^2 S = 0.35 \times 1.0 = 0.35$ kg. Next generation mean = 4.35 kg. After five generations with the same $S$ and $h^2$: $4.0 + 5 \times 0.35 = 5.75$ kg. (In practice $h^2$ tends to fall as additive variance is used up, so long-term responses are usually smaller.)

**12.** (a) $k(k+1)/2 = 10 \times 11/2 = 55$ genotypes, of which $k(k-1)/2 = 45$ are heterozygous (and 10 homozygous). (b) $H_{20} = 0.60\,(1 - 1/50)^{20} = 0.60 \times 0.668 = 0.40$.

## 15. Summary and Key Equations

| Principle / Concept | Key point |
|---|---|
| Law of segregation | Alleles separate into gametes (monohybrid F₂ 3:1; genotypes 1:2:1) |
| Law of independent assortment | Unlinked genes assort independently (dihybrid F₂ 9:3:3:1 = (3:1)²) |
| Test cross | × homozygous recessive reveals genotype |
| Incomplete dominance | Heterozygote intermediate (1:2:1) |
| Codominance | Both alleles expressed (AB blood) |
| Epistasis | One gene masks another (9:3:4, 9:7, 12:3:1, 15:1 …) |
| Polygenic traits | Binomial distribution of contributing alleles → near-normal variation |
| Chi-square test | Compare observed and expected counts; df = categories − 1 − estimated parameters |
| Meiosis | 2n → 4 × n; crossing over + independent assortment |
| Nondisjunction | Meiosis I error: all gametes abnormal; meiosis II error: half abnormal |
| X-linked recessive | More common in males; carrier mothers; no father-to-son transmission |
| Recombination frequency | 1% = 1 cM; max 50%; corrected for multiple crossovers by mapping functions |
| Hardy–Weinberg | $p + q = 1$; $p^2 + 2pq + q^2 = 1$; reached in one generation of random mating |
| Selection | Rare recessives are removed very slowly; heterozygote advantage keeps both alleles |
| Drift and inbreeding | Small populations lose heterozygosity; inbreeding raises homozygosity |
| Heritability | $h^2 = V_A/V_P$; $R = h^2 S$; a population statistic, not destiny |

**Key equations:**
$$P(k \text{ of } n) = \binom{n}{k}p^k(1-p)^{n-k}, \qquad \chi^2 = \sum_i \frac{(O_i - E_i)^2}{E_i}$$
$$r = \tfrac12\left(1 - e^{-2d}\right), \qquad d = -\tfrac12\ln(1 - 2r), \qquad \text{c.o.c.} = \frac{\text{observed DCO}}{\text{expected DCO}}, \qquad I = 1 - \text{c.o.c.}$$
$$p + q = 1, \qquad p^2 + 2pq + q^2 = 1, \qquad f(aa) = q^2 + Fpq$$
$$\Delta q = \frac{pq\,(sp - tq)}{\bar w}, \qquad \hat q = \frac{s}{s+t}, \qquad \frac{1}{q_t} = \frac{1}{q_0} + t \ \ (\text{recessive lethal})$$
$$H_t = H_0\left(1 - \frac{1}{2N}\right)^t, \qquad D_t = (1 - r)^t D_0$$
$$H^2 = \frac{V_G}{V_P}, \qquad h^2 = \frac{V_A}{V_P}, \qquad R = h^2 S, \qquad h^2 = 2(r_{MZ} - r_{DZ})$$
