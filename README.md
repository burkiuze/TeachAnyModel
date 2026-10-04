# TeachAnyModel — open science training data

Original, English-language science material for training, fine-tuning and evaluating language models: long-form reference
documents, hand-written conceptual Q&A, and thousands of generated problems with step-by-step solutions whose answers are
re-checked by tests. It covers physics (Newtonian mechanics through quantum mechanics), chemistry (general, physical,
organic, biochemistry), biology, astronomy and the mathematics that science uses.

Everything here was written for this repository rather than copied from textbooks or websites, so it can be used
under the [Apache-2.0 license](LICENSE).

| Layer | Location | Size | Typical use |
| --- | --- | --- | --- |
| Reference corpus | [`corpus/`](corpus) | 65 Markdown documents, ~175,000 words | continued pretraining, RAG knowledge base |
| Conceptual Q&A | [`qa/`](qa) | 150 hand-written question–answer pairs | instruction tuning, evaluation |
| Worked problems | [`generated/problems.jsonl`](generated) | 7,885 problems from 164 templates (expandable to any size) | instruction tuning for quantitative reasoning, evaluation with checkable answers |

## What's inside

### Reference corpus (`corpus/`)

Each document is a self-contained chapter: definitions, derivations, worked examples with numbers, tables of data,
common misconceptions and a summary. Mathematics is written in LaTeX (`$...$`, `$$...$$`).

| Area | Documents | Words | Topics |
| --- | ---: | ---: | --- |
| Classical mechanics | 9 | 22,200 | kinematics, Newton's laws, work and energy, momentum, rotation, gravitation and orbits, oscillations, Lagrangian and Hamiltonian mechanics, fluids |
| Thermodynamics | 3 | 8,000 | temperature and heat, the laws of thermodynamics, kinetic theory and statistical mechanics |
| Electromagnetism | 5 | 11,600 | electrostatics, circuits, magnetism, induction and AC, Maxwell's equations and EM waves |
| Waves and optics | 3 | 6,800 | waves and sound, geometric optics, wave optics |
| Relativity | 2 | 5,000 | special and general relativity |
| Quantum mechanics | 7 | 18,000 | origins of quantum theory, the Schrödinger equation, postulates and operators, 1D systems, angular momentum and hydrogen, identical particles and approximation methods, entanglement and quantum information |
| Nuclear, particle, condensed matter | 3 | 10,500 | nuclear physics, the Standard Model, solid-state physics |
| General chemistry | 4 | 10,200 | atomic structure and periodicity, bonding, stoichiometry, states of matter and solutions |
| Physical chemistry | 5 | 11,600 | thermochemistry, kinetics, equilibrium, acids and bases, electrochemistry |
| Organic chemistry | 9 | 24,800 | structure and nomenclature, stereochemistry, hydrocarbons, substitution and elimination, aromatic compounds, carbonyl chemistry, acids/derivatives/enolates/amines, spectroscopy, polymers and synthesis |
| Biochemistry | 3 | 9,800 | proteins and enzymes, carbohydrates/lipids/nucleic acids, metabolism and bioenergetics |
| Biology | 6 | 20,900 | cell biology, molecular biology, genetics, evolution, human physiology, ecology |
| Astronomy | 3 | 11,000 | the solar system, stars and stellar evolution, galaxies and cosmology |
| Mathematics | 3 | 8,700 | calculus, linear algebra and differential equations, probability and statistics |

Every file starts with YAML front matter:

```yaml
---
title: The Origins of Quantum Theory
field: Physics
subfield: Quantum Mechanics
level: high-school to undergraduate
keywords: [blackbody radiation, photoelectric effect, Bohr model, de Broglie wavelength]
---
```

### Conceptual Q&A (`qa/*.jsonl`)

Explanations of the "why" questions students and models often get wrong — from "why does ice float?" to Noether's
theorem, SN1 vs SN2, entanglement, dark energy and p-values — plus a set of common misconceptions with corrections.

```json
{"id": "qa-chem-008", "field": "Chemistry", "subfield": "Physical Chemistry", "difficulty": "medium",
 "question": "What is the difference between a catalyst's effect on rate and on equilibrium?",
 "answer": "A catalyst provides an alternative reaction pathway with a lower activation energy. ..."}
```

### Worked problems (`generated/problems.jsonl`)

Produced by the generator in [`scripts/problem_generators/`](scripts/problem_generators). Each of the 164 templates
draws fresh, realistic input values, solves the problem, and writes the solution as numbered steps with the final
answer stated separately. The raw inputs and outputs are kept in `values`, so answers can be checked programmatically.

| Field | Templates | Problems | Examples |
| --- | ---: | ---: | --- |
| Physics | 65 | 3,135 | projectile motion, Atwood machines, rolling, orbits, Bernoulli, Carnot engines, RC circuits, induction, Doppler, thin lenses, photoelectric effect, tunneling, time dilation, binding energy |
| Chemistry | 36 | 1,667 | moles and formulas, limiting reactants, gas laws, colligative properties, enthalpies of formation and bond enthalpies, Gibbs energy, ICE tables, $K_{sp}$, pH of weak acids and buffers, titration curves, rate laws, Arrhenius, Nernst, electrolysis, electron configurations |
| Biology | 25 | 1,212 | Hardy–Weinberg and chi-square tests, Mendelian and X-linked crosses, linkage maps, transcription/translation with mutations, PCR primers, Michaelis–Menten, Nernst/Goldman potentials, water potential, population growth, diversity indices |
| Astronomy | 19 | 950 | parallax, magnitudes, Wien and Stefan–Boltzmann, stellar lifetimes, Kepler's third law, binary-star masses, exoplanet transits and temperatures, Schwarzschild radius, Hubble's law, dark matter from rotation curves |
| Mathematics | 19 | 921 | derivatives and integrals, Taylor series, ODEs, eigenvalues, Cramer's rule, Bayes, binomial/Poisson/normal, regression, uncertainty propagation, Newton's method, numerical integration |

```json
{"id": "weak_acid_ph-00003", "field": "Chemistry", "subfield": "Physical Chemistry", "topic": "Weak acids",
 "template": "weak_acid_ph", "difficulty": "medium",
 "question": "Calculate the pH and the percent ionization of a $0.23$ M solution of hypochlorous acid (HOCl), $K_a = 3.0 \\times 10^{-8}$.",
 "solution": "**Solution:**\n1. HOCl + H₂O ⇌ H₃O⁺ + A⁻. ICE: [HA] $= 0.23 - x$, [H₃O⁺] = [A⁻] $= x$.\n2. ...\n5. Shortcut check: ... the 5% rule holds, so the approximation is fine.\n\n**Answer:** pH = 4.08; 0.036% ionized",
 "answer": "pH = 4.08; 0.036% ionized",
 "values": {"Ka": 3e-08, "c": 0.23, "H3O": 8.305123998e-05, "pH": 4.080653879, "percent_ionization": 0.03610923478}}
```

## Quick start

Requires only Python 3.9+ (standard library; no packages to install).

```bash
# 1. Regenerate or enlarge the problem set (deterministic for a given seed)
python scripts/generate_problems.py                                   # 50 per template -> generated/problems.jsonl
python scripts/generate_problems.py --per-template 1000 --seed 7 --out generated/big.jsonl
python scripts/generate_problems.py --fields Chemistry Biology       # filter by field
python scripts/generate_problems.py --list                           # list all templates

# 2. Export everything into ready-to-train files (written to dist/, which is git-ignored)
python scripts/build_datasets.py
python scripts/build_datasets.py --system-prompt "You are a chemistry tutor." --val-fraction 0.02

# 3. Check the data and the generators
python scripts/validate.py
python -m unittest discover -s tests -v
```

`build_datasets.py` writes:

| File | Format | Contents |
| --- | --- | --- |
| `pretrain.jsonl` | `{"text", "source"}` | corpus documents, Q&A and worked problems as plain text |
| `rag_chunks.jsonl` | `{"id", "title", "section", "field", "text"}` | corpus split at section headings (≤ 4,000 characters) for retrieval |
| `sft_alpaca.jsonl` | `{"instruction", "input", "output"}` | Q&A + problems |
| `sft_sharegpt.jsonl` | `{"conversations": [{"from", "value"}]}` | Q&A + problems |
| `sft_chat.jsonl` | `{"messages": [{"role", "content"}]}` | Q&A + problems with an optional system prompt (OpenAI / Hugging Face chat format) |
| `*.validation.jsonl` | same | a deterministic ~5% hold-out of the SFT pairs (split by hashed id) |

Loading with Hugging Face `datasets`:

```python
from datasets import load_dataset

sft = load_dataset("json", data_files={"train": "dist/sft_chat.jsonl",
                                       "validation": "dist/sft_chat.validation.jsonl"})
corpus = load_dataset("json", data_files="dist/pretrain.jsonl", split="train")
```

The chat-format files plug directly into most fine-tuning frameworks that accept a `messages` column.

## Accuracy and conventions

- **Checked answers.** `tests/test_generators.py` regenerates problems from every template and re-derives the answers
  from the stored inputs with independently written formulas (relative tolerance $10^{-6}$), and also checks the
  schema, determinism, balanced LaTeX delimiters, and that the committed `generated/problems.jsonl` matches a fresh
  run. `scripts/validate.py` checks front matter, unique ids and math delimiters across all data.
- **Constants and assumptions** are stated in the problems. Physics problems use $g = 9.81$ m/s² and CODATA constants
  rounded to four significant figures; chemistry uses standard textbook data (atomic masses, $K_a$, $K_{sp}$,
  $\Delta H_f^\circ$, $E^\circ$). Models are idealized where stated (ideal gases, ideal van 't Hoff factors, no air
  resistance) and the solutions say so.
- **Significant figures.** Intermediate and final results are shown to about three significant figures; the full
  values are in `values`.
- **Notation.** Math uses LaTeX inside `$...$`; chemical formulas use Unicode subscripts (H₂SO₄) outside math and
  `\text{}` inside it.
- This is educational material written to be correct and clear, but it has not been peer-reviewed. If you find an
  error, please open an issue or a pull request.

## Extending the dataset

**Add a problem template.** Templates are plain functions registered with a decorator. They receive a seeded
`random.Random` and return the question, the solution steps, the answer and the values used:

```python
from .common import fmt, nice, q, template

@template("ohms_law", "Physics", "Electromagnetism", "Circuits", "easy")
def ohms_law(rng):
    V, R = nice(rng, 1, 24, 1), nice(rng, 10, 1000, 10)
    I = V / R
    return {
        "question": f"A {q(R, 'Ω')} resistor is connected to a {q(V, 'V')} battery. What current flows?",
        "steps": [f"Ohm's law: $I = V/R = {V}/{R} = {fmt(I)}$ A."],
        "answer": f"$I = {fmt(I)}$ A",
        "values": {"V": V, "R": R, "I": I},
    }
```

Then add an independent check for it in `tests/test_generators.py` (the test suite fails if a template has none),
regenerate with `python scripts/generate_problems.py`, and run the tests.

**Add Q&A or corpus documents.** Q&A files are JSON Lines with the keys `id`, `field`, `subfield`, `difficulty`
(`easy`/`medium`/`hard`), `question` and `answer`. Corpus documents need the front matter shown above and a
level-1 title. Run `python scripts/validate.py` before committing.

## Repository layout

```
corpus/                     long-form reference documents (Markdown + LaTeX)
  physics/ chemistry/ biology/ astronomy/ mathematics/
qa/                         hand-written conceptual Q&A (JSONL)
generated/problems.jsonl    generated worked problems (JSONL)
scripts/
  problem_generators/       template library: common.py, physics.py, chemistry.py, biology.py, astronomy.py, mathematics.py
  generate_problems.py      problem-generation CLI
  build_datasets.py         export to pretraining / RAG / SFT formats
  validate.py               data checks
tests/                      unit tests for the generators
```

## License

Apache License 2.0 — see [LICENSE](LICENSE).
