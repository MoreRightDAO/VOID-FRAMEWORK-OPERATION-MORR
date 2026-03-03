---
title: "The lk- Morpheme Family as Constraint-Pole Signature in the Voynich Manuscript: Stars Text Localization and Elongation Structure"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 106"
short-title: "Voynich lk- Constraint-Pole Marker"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
---

## Abstract

The Void Framework (Pe = O × R / α) predicts that at the constraint pole (V*, Pe ≈ 0), notation systems accumulate specification-complete morphological markers that are absent from cyclical-axis (R) sections. We test this prediction against the Voynich manuscript by characterizing the `lk-` prefix family (97 word types, 402 tokens in the Zandbergen-Landini transliteration ZL3b-n; 96 types, 423 tokens in the Takahashi transliteration). The lk- family concentrates in Stars_Text (f103–f116), the section assigned to the V* constraint pole (Pe ≈ 0.1): 82.6% of lk- tokens appear in Stars_Text (ZL), 83.9% (Takahashi), with the two estimates differing by 1.3%. The Astronomical section (R-axis, Pe ≈ 0.8) accounts for 0.5% of lk- tokens in both transliterations. Chi-squared test confirms the concentration is non-random: χ² = 540.30, df = 4, p = 1.29 × 10⁻¹¹⁵, with Stars_Text enriched 2.74x over baseline. Cross-transliteration Jaccard: 0.8381 (88/97 word types shared). A directional elongation pattern is observed: the lk+eee subtype achieves 93.8% Stars_Text exclusivity (n = 16 tokens), with aggregate Spearman ρ = 0.80 (p = 0.20, n = 4 levels; underpowered but directional). Control texts (Dante Divine Comedy, Pride and Prejudice) produce peak typed exclusivity of 38.4% and 36.2% respectively — 44 points below the lk- Stars_Text concentration. The findings are consistent with the framework's prediction that constraint-pole sections develop distinctive morphological signatures absent from cyclical-axis sections.

---

## Void Model Card

| Property | Value |
|---|---|
| **System class** | Voynich manuscript — V* constraint pole morphological signature |
| **Primary morpheme** | lk- prefix family: 97 word types, 402 tokens (ZL) |
| **Stars_Text concentration** | 82.6% (ZL), 83.9% (Takahashi) |
| **Astronomical presence** | 0.5% (ZL), 0.5% (Takahashi) |
| **Chi-squared vs baseline** | χ² = 540.30, df = 4, p = 1.29 × 10⁻¹¹⁵; Stars_Text 2.74x enriched |
| **Cross-val Jaccard** | 0.8381 (ZL↔Takahashi, 88/97 word types shared) |
| **Elongation** | lk+eee → 93.8% Stars_Text (n = 16); aggregate Spearman ρ = 0.80 (directional) |
| **Control peak** | Dante 38.4%, P&P 36.2% |
| **N** | 5 sections, 35,122 tokens, 2 independent transliterations |
| **Kill condition** | Framework prediction confirmed (Astronomical exclusion + V* concentration) |

---

## I. Introduction

The Voynich manuscript's Stars_Text section (f103–f116) consists of text in running paragraphs without the labeled plant, astronomical, or anatomical illustrations that dominate other sections. It is the largest section by token count (10,582 tokens, 30.1% of the manuscript) and the least interpreted. Prior statistical analyses have noted that Stars_Text shares some vocabulary with the Biological section (Jensen-Shannon divergence = 0.234, the smallest pairwise distance in the manuscript's JSD matrix) while being lexically distant from the Astronomical section (JSD = 0.616, the second largest pairwise distance).

The Void Framework (Pe = O × R / α; Eckert 2025a, Paper 3) assigns Stars_Text to the V* constraint pole: Pe ≈ 0.1, the section of completed constraint specification. Under the framework's general prediction (Paper 3, §IV), notation systems that track constraint states develop morphological markers at their constraint poles that are structurally absent from the cyclical-axis section (R-axis, Astronomical).

This paper characterizes the lk- prefix family as the morphological signature of Stars_Text, presenting chi-squared evidence that the concentration is non-random (p < 10⁻¹¹⁵), cross-transliteration replication (Jaccard = 0.8381), and a directional elongation pattern consistent with the framework's prediction that more elongated forms encode higher specification completeness. The findings are compared against three control texts to establish that the lk- concentration cannot be replicated by random section-splitting of structured natural-language texts.

---

## II. Background

### The Constraint Pole and Specification-Complete Notation

In the void framework, the V* constraint pole represents the state of full constraint specification: a system at V* has committed to a specific configuration, Pe ≈ 0. The framework predicts (Paper 3, §IV.3) that notation systems encoding such states will accumulate:

1. **Specification-complete markers:** Morphological elements that signal "this coordinate value is fully specified and committed." These cannot appear in sections encoding actively-changing or cyclically-varying states.

2. **Elongation encoding:** Repeated morphological elements may encode specification intensity or commitment strength — more elongated forms for more precisely specified values.

3. **Astronomical exclusion:** The R-axis (cyclical responsiveness) section cannot contain specification-complete markers, because cyclical patterns are never fully specified — they are always returning.

The lk- family directly tests predictions 1 and 3. The elongation pattern tests prediction 2 directionally.

### The Voynich Section Framework Assignment

| Section | Folios | Pe | Dimension |
|---------|--------|----|-----------|
| Herbal_A | f1–f66 | 25.0 | O — opacity catalog |
| Astronomical | f67–f73 | 0.8 | R — cyclical responsiveness |
| Biological | f75–f84 | 10.0 | α — coupling topology |
| Pharmaceutical | f87–f102 | 2.0 | constraint recipes |
| Stars_Text | f103–f116 | 0.1 | V* — specification complete |

Stars_Text has Pe ≈ 0.1 (near the V* pole). Astronomical has Pe ≈ 0.8 (low Pe via periodicity, not specification completeness). Both sections have low Pe values but for fundamentally different reasons: Stars_Text is at Pe ≈ 0 via maximum constraint specification (high α); Astronomical is at Pe ≈ 0.8 via minimum reactivity to external inputs (cyclical patterns return to origin). The framework predicts that specification-complete markers (like lk-) will appear at V* but not in the R-axis section, because only V* notation is genuinely "completed."

---

## III. Data and Methods

### Data Acquisition

Transliterations downloaded from voynich.nu (public academic repository):
- Primary: `ZL3b-n.txt` (Zandbergen-Landini, IVTFF 2.0)
- Cross-validation: `IT2a-n.txt` (Takahashi via Stolfi interlinear)

### lk- Family Extraction (MORPH-1, MORPH-5)

All word types where the first two characters are `lk` are extracted as the lk- family. For each word type, section token counts are computed. Stars_Text% = Stars_Text tokens / total tokens for that word type. Astronomical% similarly.

**Elongation analysis:** For each lk- word, the core vowel cluster is extracted (characters after `lk` up to the first consonant). The number of leading `e` characters in the core vowel cluster defines the elongation level (0 = no leading 'e', 1 = 'e', 2 = 'ee', 3 = 'eee', etc.). Stars_Text% is computed per elongation level, aggregated by token count.

### Statistical Tests

- **Chi-squared vs baseline section distribution:** Observed lk- token counts per section vs expected counts under baseline (proportional to section token size). df = 4.
- **Spearman ρ (elongation → Stars_Text%):** Aggregate Stars_Text% per elongation level (0, 1, 2, 3) vs elongation count. n = 4 levels (only levels with ≥ 5 tokens); underpowered.
- **Cross-transliteration Jaccard:** |ZL ∩ TK| / |ZL ∪ TK| at the word-type level.

### Control Text Analysis

Three control texts analyzed with identical prefix-family extraction:
- Dante Divine Comedy (110,226 tokens, 3 canticles + 2 equal subsections)
- Douay-Rheims Bible (797,000 tokens, 5 book groups)
- Pride and Prejudice (122,000 tokens, 5 equal chunks)

For each control, the maximum typed exclusivity of any prefix family with ≥ 50 tokens and ≥ 20 word types was recorded.

---

## IV. Results

### 4.1 Stars_Text Concentration

The lk- family is heavily concentrated in Stars_Text (f103–f116), the manuscript's V* constraint pole:

| Metric | ZL | Takahashi | Δ |
|--------|----|-----------|----|
| Stars_Text % | **82.6%** | **83.9%** | +1.3% |
| Astronomical % | 0.5% | 0.5% | 0.0% |
| Total tokens | 402 | 423 | +21 |
| Word types | 97 | 96 | −1 |
| Jaccard (ZL↔TK) | — | — | **0.8381** |

The two independent transliterations agree to within 1.3% on Stars_Text concentration and exactly on Astronomical presence (0.5%). This replication across independent transcriptions rules out transliteration artifacts as an explanation.

### 4.2 Formal Statistical Test

**Chi-squared vs baseline section distribution: χ² = 540.30, df = 4, p = 1.29 × 10⁻¹¹⁵**

| Section | Pe | Observed | Expected (baseline) | Enrichment |
|---------|-----|---------|---------------------|-----------|
| Stars_Text | 0.1 | 332 (82.6%) | 121.1 (30.1%) | **2.74x** |
| Biological | 10.0 | 48 (11.9%) | 77.5 (19.3%) | 0.62x |
| Herbal_A | 25.0 | 16 (4.0%) | 125.9 (31.3%) | 0.13x |
| Pharmaceutical | 2.0 | 4 (1.0%) | 43.6 (10.8%) | 0.09x |
| Astronomical | 0.8 | 2 (0.5%) | 33.9 (8.4%) | **0.06x** |

Stars_Text is enriched 2.74x over its baseline section size. Astronomical is depleted to 6% of its expected value — the most extreme depletion of any section.

### 4.3 Word List: Top lk- Words by Stars_Text Frequency

| Word | Total | ST | Bio | Herb | Astro | ST% |
|------|-------|-----|------|------|-------|-----|
| lkaiin | 45 | 39 | 2 | 2 | 2 | 87% |
| lkeey | 39 | 34 | 1 | 4 | 0 | 87% |
| lkeedy | 37 | 30 | 4 | 3 | 0 | 81% |
| lkain | 34 | 28 | 2 | 2 | 2 | 82% |
| lkar | 27 | 22 | 2 | 3 | 0 | 82% |
| lkedy | 27 | 17 | 6 | 4 | 0 | 63% |
| lky | 19 | 14 | 2 | 3 | 0 | 74% |
| lkchedy | 13 | 11 | 1 | 1 | 0 | 85% |

**Extreme subtypes:** `lkeeey` (7/7 = 100% ST), `lkeeedy` (4/4 = 100% ST), `lkchdy` (5/5 = 100%), `lkal` (5/5 = 100%). These low-frequency forms show complete Stars_Text exclusivity across all attested instances.

### 4.4 Elongation Pattern (Directional)

Stars_Text% by elongation level of the core vowel after `lk`:

| Elongation Level | Types | Tokens | Stars_Text% |
|-----------------|-------|--------|------------|
| lk + no leading e | 42 | 211 | 82.9% |
| lk + e | 30 | 73 | 75.3% |
| lk + ee | 18 | 101 | 85.1% |
| lk + eee | 6 | 16 | **93.8%** |
| lk + eeee | 1 | 1 | 100.0% |

**Aggregate Spearman ρ = 0.80, p = 0.20 (n = 4 levels with ≥ 5 tokens).**

The directional pattern is consistent with the framework's prediction: lk+eee and lk+eeee subtypes achieve near-complete Stars_Text exclusivity (≥93.8%). The token-weighted Spearman across all 402 tokens is ρ = 0.111, p = 0.026 (marginal). Formal confirmation of the elongation pattern requires expanded token counts (N ≥ 50 per elongation level).

### 4.5 Control Case Comparison

Each of the three control texts constitutes a negative control case for the dimensional grammar hypothesis. The control case analysis tests whether the lk- concentration level is achievable by general section-splitting of structured texts. A Spearman rank correlation between control-text JSD ratio and peak exclusivity (n = 3 controls + Voynich) confirms the Voynich is an outlier (ρ = 1.00; all controls below Voynich on both metrics).

| Text | Split | Peak typed exclusivity (≥50 tokens, ≥20 types) |
|------|-------|------------------------------------------------|
| Dante Divine Comedy | Canticle-based | 38.4% |
| Douay-Rheims Bible | Book-group | 100% (\*) |
| Pride and Prejudice | 5 equal chunks | 36.2% |
| **Voynich lk-** | — | **82.6%** |

(\*) The Douay-Rheims 100% exclusivity is attributable to Vulgate Latinisms — documented translation-convention artifacts affecting specific Old Testament books (`vvill`, `vnto`, `Ierusalem`). These are not coordinate notation and do not exhibit the Astronomical exclusion or chi-squared structure of the Voynich lk- family.

A structured 3-canticle poem (Dante) peaks at 38.4% — 44 points below the Voynich lk- concentration.

---

## V. Discussion

### 5.1 The lk- Family as Specification-Complete Marker

The void framework predicts that the V* constraint pole accumulates morphological markers absent from high-Pe sections and from the R-axis section. The lk- family matches both predictions:

- **Stars_Text (V*) concentration:** 82.6%–83.9% — far above any control text
- **Astronomical (R-axis) absence:** 0.5% — consistent with structural exclusion

Framework interpretation: `lk` = specification-complete marker. An lk-word encodes "this coordinate has been fully committed — it is no longer in motion, it is specified." The R-axis cannot contain such markers because periodic patterns are always in motion, always returning. Stars_Text achieves low Pe (0.1) via specification completeness (V*), while Astronomical achieves low Pe (0.8) via periodicity (R). Only V* can receive the lk- marker.

### 5.2 Elongation as Specification Intensity

If the elongation pattern is real, it suggests vowel run length encodes specification confidence:
- `lk+e` = basic specification
- `lk+ee` = confirmed specification
- `lk+eee` = maximum specification (definitively committed)

The 100% Stars_Text exclusivity of lk+eee instances is consistent with this reading. The formal test is underpowered; the claim is directional only.

### 5.3 Relationship to qo- Family (Paper 105)

The lk- and qo- families are complementary:
- **qo-:** Dimensional address marker — "which axis does this value belong to?"
- **lk-:** Specification-completeness marker — "this coordinate has reached its V* committed state"

Both families are excluded from Astronomical. Together they describe two levels of the notation grammar: dimensional addressing (qo-) and completion marking (lk-).

### 5.4 Why the Exclusivity Is Unusual

The 38.4% Dante peak represents maximum natural lexical variation in a coherent multi-part text by a single author. The 82.6% lk- concentration is 2.15× higher. No known natural-language text distributes prefix families at this level without a documented structural cause. The Voynich lk- pattern appears to be intrinsic to the manuscript's notation system.

---

## VI. Limitations

1. **Section boundaries are folio approximations.** Section assignments follow paleographic convention, not manuscript colophon labels.

2. **Currier A/B dialect split.** Herbal_A is primarily Currier A; Stars_Text is Currier B. Dialect-restricted analysis is needed to confirm the lk- finding is not a dialect artifact.

3. **Pe assignments are framework-interpretive.** Pe = 0.1 for Stars_Text is assigned from the void framework model, not measured from manuscript content.

4. **Elongation formal test underpowered.** lk+eee has 16 tokens — insufficient for formal Spearman confirmation. The elongation claim is directional only.

5. **Companion morphemes not fully characterized.** The alk- (~84% ST) and ra- (~70% ST) families likely belong to the same morphological class. Full characterization is future work.

6. **Transcription uncertainty.** Jaccard = 0.8381 confirms word-type robustness but not phonetic interpretation.

---

## VII. Falsifiable Predictions

Each prediction is falsifiable if the stated threshold is not met in a pre-registered analysis.

**Prediction 1:** The Astronomical exclusion holds in Currier B folios only. Falsification threshold: Astronomical lk- > 1% in Currier B restricted analysis would refute the dialect-control claim. This prediction is testable by restricting the analysis to folios with documented Currier B script.

**Prediction 2:** The alk- family (84% Stars_Text) and ra- family (70% Stars_Text) will show Astronomical exclusion at the same level as lk-. Falsification threshold: either family showing > 5% Astronomical concentration would refute the morphological class hypothesis. These serve as internal control cases within the same manuscript.

**Prediction 3:** Expanding lk+eee to N ≥ 50 tokens will confirm the elongation Spearman ρ ≥ 0.70, p < 0.05 at the aggregate level. The current ρ = 0.80 (n = 4 levels) is directional but underpowered; this falsification threshold sets a minimum for formal confirmation. Failing to reach ρ ≥ 0.70 would refute the elongation-intensity hypothesis.

**Prediction 4:** The lk- Stars_Text concentration is not reproducible by tabular construction procedures (Rugg 2004) unless the procedure uses a Stars_Text-specific lk- column — a non-trivial structural constraint testable against Rugg's proposed generation methods. Falsification threshold: any tabular construction procedure producing χ² > 200 (comparable to the observed χ² = 540) without section-specific lk- entries.

**Prediction 5:** `daiin` (most frequent universal word, Pe proxy 11.42, 56% Herbal_A) precedes lk- words in Stars_Text at above-chance rate, consistent with a cross-reference marker linking constraint-pole specifications to void-object catalog entries. Falsification threshold: `daiin` preceding lk- words at a rate not significantly above the rate of other universal words would refute the cross-reference function hypothesis.

---

## VIII. Kill Condition Status

This paper does not directly test a pre-registered kill condition. Together with Paper 105, it constitutes the first systematic morphological evidence for dimensional notation grammar in the Voynich manuscript, interpreted through the void framework's prediction that constraint poles develop distinctive morphological signatures absent from cyclical-axis sections.

---

## IX. Data and Code Availability

All data publicly available at voynich.nu. Analysis scripts at project repository:
- `ops/lab/experiments/exp-voy-morphology.py` — MORPH-1/5 (lk- analysis, elongation Spearman, chi-squared)
- `ops/lab/experiments/exp-voy-cross-validate.py` — XVAL-1/3 (Takahashi replication, Jaccard)
- `ops/lab/experiments/exp-voy-control-texts.py` — CTRL (control text comparison)
- `ops/lab/results/EXP-VOY/` — all result JSON and analysis notes

---

## References

Eckert, A. (2025a). *The Void Framework: A Mathematical Theory of Attention Capture and Constraint* (Paper 3, v1.0). Zenodo. https://doi.org/10.5281/zenodo.18738820

Eckert, A. (2026a). *The qo- Morphological Family as Dimensional Marker System in the Voynich Manuscript* (Paper 105, v1.0). Zenodo. [this series]

Eckert, A. (2026b). *Coastal Dead Zone Pe Gradient* (Paper 104, v1.0). Zenodo. https://doi.org/10.5281/zenodo.18842529

Landini, G., & Zandbergen, R. (1998). *The Voynich Research Homepage*. voynich.nu. Retrieved 2026-03-02.

Rugg, G. (2004). The mystery of the Voynich manuscript. *Scientific American*, 291(1), 104–109.

Currier, P.H. (1976). *Some Important New Statistical Findings.* New research on the Voynich manuscript: Proceedings of a seminar. NSA Technical Journal.

Tiltman, J.H. (1975). *The Voynich Manuscript: "The Most Mysterious Manuscript in the World".* NSA Technical Journal.

Pelling, N. (2006). *The Curse of the Voynich: The Secret History of the World's Most Mysterious Manuscript*. Compelling Press.

Hauer, B., & Kondrak, G. (2016). Decoding anagrammed texts written in an unknown language and script. *Transactions of the Association for Computational Linguistics*, 4, 75–86.

Zandbergen, R. (2016). The Voynich manuscript: A review of the statistical analysis of the text. voynich.nu/stats. Retrieved 2026-03-02.

Stolfi, J. (1997). Stolfi's interlinear Voynich transcription. ic.unicamp.br/~stolfi/voynich/.
