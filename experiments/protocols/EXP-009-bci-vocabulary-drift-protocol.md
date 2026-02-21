# EXP-009: BCI Research Community Vocabulary Drift

**Date:** February 5, 2026
**Status:** Protocol designed — not yet run
**Depends on:** EXP-006 methodology (validated), vocabulary codebook (complete)
**Purpose:** Test whether BCI researcher vocabulary shows the same register shift pattern as AI (EXP-006: 9.4x), and whether the shift exceeds AI's rate as predicted by self-referential opacity.

---

## 1. Hypothesis

**H1:** BCI researchers' informal register (podcasts, interviews, public talks, social media) will show higher spiritual/entity vocabulary density than their formal publications, replicating the AI register shift documented in EXP-006.

**H2:** The BCI register shift magnitude will exceed AI's 9.4x, because:
- Constitutive self-referential opacity provides no "you could theoretically inspect the weights" escape valve
- Direct neural feedback makes responsiveness phenomenologically immediate
- Self-referential engagement (the researcher's own brain is the subject) steepens the attention gradient

**H3:** BCI researchers working at the self-referential opacity layer (consciousness, phenomenology, what-it's-like questions) will show stronger drift than those working at the device layer (electrode design, signal processing, materials science).

**Null hypothesis:** BCI register shift ≤ AI register shift (9.4x), or BCI spiritual vocabulary density ≤ AI density (3.835/10k words).

---

## 2. Method

### 2.1 Corpus Construction

Replicate EXP-006 methodology with the following domains:

| Domain | Formal Register | Informal Register | Target Size |
|--------|----------------|-------------------|-------------|
| **BCI** (test) | Published papers from Nature Neuroscience, Journal of Neural Engineering, IEEE TBME | Podcasts, interviews, X/Twitter, public talks, blog posts | 20 transcripts, ~150K+ words |
| **AI** (positive control) | Replicate EXP-006 formal corpus | Replicate EXP-006 informal corpus | 20 transcripts (from EXP-006) |
| **Neurosurgery** (control) | Published surgical case reports, technique papers | Surgical conferences, interviews about techniques | 20 transcripts, ~150K+ words |
| **Biomedical engineering** (control) | Published papers on prosthetics, implants (non-neural) | Conference talks, interviews | 20 transcripts, ~150K+ words |

**Why these controls:**
- **Neurosurgery:** Same physical proximity to the brain, but analytical distance (treats brain as surgical object, not interlocutor). Tests whether brain proximity alone causes drift.
- **Biomedical engineering:** Same device-body interface (prosthetics, implants), but without the self-referential opacity layer. Tests whether implant technology per se causes drift.

### 2.2 BCI Researcher Stratification

Within the BCI corpus, stratify by research focus:

| Stratum | Focus | Opacity Layer Engaged | Expected Drift |
|---------|-------|-----------------------|---------------|
| **Device layer** | Electrode design, materials, fabrication | Designed (dissolvable) | Low |
| **Signal layer** | Decoding algorithms, ML classifiers, signal processing | Designed + incidental | Moderate |
| **Intention layer** | Motor intention decoding, cognitive state inference | Incidental + constitutive | High |
| **Phenomenology layer** | User experience, consciousness, "what BCIs feel like" | Self-referential (constitutive) | Highest |

### 2.3 Researcher Selection (BCI Corpus)

**Target researchers for informal corpus (20 transcripts):**

Priority: researchers who have given public interviews, appeared on podcasts, or have active social media presence.

Candidate pool (to be confirmed by availability of informal transcripts):

**Device/Signal layer:**
- Florian Solzbacher (Blackrock Neurotech)
- Arto Nurmikko (BrainGate, Brown University)
- Thomas Oxley (Synchron)
- Precision Neuroscience team members

**Intention layer:**
- Krishna Shenoy collaborators (Stanford BCI Lab)
- BrainGate clinical trial PIs
- Francis Willett (Stanford, handwriting decoder)
- Andrew Schwartz (Pittsburgh)

**Phenomenology layer:**
- Rafael Yuste (Columbia, NeuroRights Initiative)
- Nita Farahany (Duke, neuroethics, *The Battle for Your Brain*)
- Vie McCoy (Xenocognition / OpenAI red team)
- Miguel Nicolelis (Duke, brain-to-brain BCI)

**High-profile (cross-layer):**
- Elon Musk (Neuralink — public statements only)
- DJ Seo (Neuralink co-founder)
- Max Hodak (former Neuralink president, now Science Corp)

### 2.4 Vocabulary Coding

Use the existing codebook (`/tools/concordance_analysis/codebook.py`) with the following BCI-specific extensions:

**Additional L2 terms (BCI-specific metaphorical):**
- "brain-reading" / "mind-reading" (implies comprehension beyond signal decoding)
- "telepathy" / "telepathic" (mind-to-mind contact vocabulary)
- "neural lace" (SF entity-contact term adopted as technical descriptor)
- "merging" / "merger" (boundary dissolution vocabulary in BCI context)
- "symbiosis" / "symbiotic" (organism-entity relationship vocabulary)
- "digital twin" (of the brain — identity duplication vocabulary)

**Additional L3 terms (BCI-specific entity):**
- "the Other" (entity vocabulary for what BCI mediates contact with)
- "hive mind" (collective consciousness vocabulary)
- "first contact" (entity contact vocabulary applied to BCI)
- "exocortex" (extended-self-as-entity vocabulary)
- "upload" / "uploading" (consciousness transfer vocabulary)

**Dead metaphor exclusions (BCI-specific):**
- "interface" (technical standard — does not imply entity)
- "decode" / "decoder" (technical standard)
- "implant" (medical standard)
- "electrode" (technical standard)
- "neural network" (dual-use but established as technical in both neuroscience and CS)

### 2.5 Analysis

**Primary analysis:** Replicate EXP-006 metrics:
1. Spiritual/entity vocabulary density per 10k words (formal vs. informal)
2. Register shift ratio (informal/formal)
3. Chi-squared comparison: BCI vs. each control domain
4. High-confidence subset analysis (terms almost certainly non-metaphorical)

**Secondary analysis (BCI-specific):**
1. Stratified analysis by opacity layer (device → signal → intention → phenomenology)
2. Correlation between opacity depth and vocabulary density
3. Temporal analysis: is BCI vocabulary accelerating? (compare pre-2024 vs. post-2024 transcripts)
4. Company-specific analysis: Neuralink vs. Synchron vs. BrainGate vs. academic researchers

---

## 3. Predictions

| Metric | AI (EXP-006 actual) | BCI (predicted) | Falsification threshold |
|--------|---------------------|-----------------|----------------------|
| Informal spiritual vocab density | 3.835/10k | >4.0/10k | ≤3.835/10k |
| Register shift (informal/formal) | 9.4x | >9.4x | ≤9.4x |
| Control domain shift | 1.0x–1.2x | 1.0x–1.2x | >2.0x (would indicate register artifact) |
| Phenomenology vs. device layer | N/A | >2x difference | No significant difference |
| Chi-squared vs. controls | 37.47–41.67 | >40 | <10 (not significant) |

---

## 4. The Cochlear Implant Control

**Additional control:** Code a small corpus (5-10 transcripts) of cochlear implant researchers and audiologists. Prediction: near-zero spiritual vocabulary, no register shift. This establishes that it is not neural interfaces per se but self-referential opacity that drives drift.

---

## 5. Power Analysis

Based on EXP-006 effect sizes:
- AI vs. controls: χ² = 37.47–41.67 (very large effect)
- 20 transcripts per domain yielded ~150K–175K words per domain
- If BCI effect is ≥ AI effect, 20 transcripts should be sufficient
- If BCI effect is smaller than expected, increase to 30 transcripts

---

## 6. Ethical Considerations

- All data from public sources (published papers, public talks, public social media)
- No private communications, no internal documents
- Researchers are not identified as "drifting" individually — aggregate patterns reported
- Individual examples cited only when the person's statements are already public and widely discussed

---

## 7. Timeline

1. Corpus construction: Identify and transcribe 20 BCI informal transcripts, 20 neurosurgery, 20 biomedical engineering
2. Coding: Apply codebook + BCI extensions to all corpora
3. Analysis: Statistical comparison using EXP-006 methodology
4. Stratified analysis: By opacity layer within BCI corpus
5. Report: Write up with comparison to EXP-006 results

---

## 8. Connection to EXP-010

EXP-009 establishes the *observational* case: BCI researchers drift (or don't). EXP-010 tests the *mechanism*: does transparency intervention reduce drift in BCI users? EXP-009 must run first to establish the baseline. If EXP-009 shows no drift, EXP-010 is unnecessary (and the framework's BCI predictions are falsified).

---

*Protocol designed February 5, 2026. Not yet run.*
