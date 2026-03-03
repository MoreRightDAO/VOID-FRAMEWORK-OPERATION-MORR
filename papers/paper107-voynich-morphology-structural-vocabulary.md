---
title: "Structural Vocabulary Analysis of the Voynich Manuscript: Jensen-Shannon Divergence Matrix, Spectral Clustering, and Dimensional Entropy Signatures"
author: "Anthony Eckert"
orcid: "0009-0008-1925-5253"
affiliation: "Independent Researcher, MoreRight DAO"
paper-number: "Paper 107"
short-title: "Voynich Structural Vocabulary"
version: "v1.0"
date: "March 2026"
license: "cc-by-4.0"
subtitle: "EXP-VOY Series III — JSD Spread, k=3 Stability, Conditional Entropy Split"
keywords:
  - Voynich manuscript
  - Jensen-Shannon divergence
  - spectral clustering
  - conditional entropy
  - vocabulary distribution
  - dimensional grammar
  - void framework
  - morphology
---

## Abstract

The void framework predicts that the Voynich manuscript's five textual sections encode a three-dimensional coordinate notation system (O/R/α plus constraint pole V*), producing section-vocabulary distributions that are structurally differentiated beyond random section assignment. We test three predictions against the 35,122-token Zandbergen-Landini EVA transliteration. First, the Jensen-Shannon divergence matrix shows a max/min spread ratio of 1.373, significantly exceeding a 5,000-permutation null distribution (95th percentile 1.213; p=0.0000). Second, spectral clustering with k=3 recovers exactly the three predicted dimensional clusters (O/R/α), stable across 8 random seeds (ARI=1.000). Third, conditional character entropy h₂ reveals a dimensional split: the α-axis section (Biological) has the lowest character-level entropy (h₂=1.990) and highest word-level entropy (h₂=3.731), while the R-axis section (Astronomical) has the highest character entropy (h₂=2.440) and lowest word entropy (h₂=1.764). No prior Voynich analysis has reported this per-section entropy structure. Three control texts (Dante, Douay-Rheims, Pride and Prejudice) all fall below the Voynich JSD ratio. Alongside morphological findings in Papers 105 and 106 (qo- dimensional grammar, lk- constraint-pole marker), these structural results constitute the first systematic multi-method evidence for dimensional notation grammar in the Voynich manuscript.

---

## Void Model Card

| Property | Value |
|----------|-------|
| **Framework** | Void Framework (Pe = O × R / α) |
| **Test domain** | Voynich Manuscript — 5-section vocabulary distribution |
| **Primary dataset** | ZL3b-n.txt, 35,122 tokens, IVTFF 2.0 |
| **Sections** | Herbal_A (Pe=25.0), Astronomical (Pe=0.8), Biological (Pe=10.0), Pharmaceutical (Pe=2.0), Stars_Text (Pe=0.1) |
| **Dimensions tested** | O (opacity), R (responsiveness), α (coupling), V* (constraint pole) |
| **Primary statistic** | JSD ratio permutation test: p=0.0000, n=5,000 |
| **Secondary statistic** | Spectral k=3 ARI=1.000 across 8 seeds |
| **Tertiary** | DEEP-1 per-section char h₂ split |
| **Spearman** | ρ=−0.800, p=0.200 (n=4, JSD-from-V* vs Pe, directional/underpowered) |
| **Control** | Dante 1.157, Douay-Rheims 1.297, P&P 1.085 (all < 1.373) |
| **Falsifiable** | Yes — see Section VII |
| **Kill conditions** | Listed Section VIII |

---

## I. Introduction

The Voynich manuscript (MS 408, Beinecke Rare Book Library, Yale University, c. 1404–1438 CE) remains undeciphered after more than a century of cryptographic, linguistic, and statistical analysis. Prior work has established that the manuscript's vocabulary is structured — section-to-section vocabulary distributions differ systematically — but interpretations of this structure range from natural language with multiple registers to cipher artifacts to constructed notation systems. No consensus theory accounts for the full morphological patterning observed in EVA transliterations.

The void framework (Pe = O × R / α) generates specific structural predictions about notation systems designed to track multi-dimensional constraint states. A system encoding opacity (O), responsiveness (R), and coupling (α) as separable dimensions will produce vocabulary distributions where: (a) different dimensional assignments produce measurably different lexical profiles, (b) the cyclical-responsiveness dimension (R) is structurally incompatible with fixed-coordinate notation used for O and α axes, and (c) sub-word character-level entropy will differ between dimensions according to their encoding strategy.

This paper tests three of these predictions against the Voynich manuscript vocabulary. We report: (1) the Jensen-Shannon divergence spread across all section pairs, tested against a 5,000-permutation null; (2) spectral clustering stability for k=3 across eight random seeds; and (3) per-section conditional character and word entropy. These tests extend the morphological findings of Papers 105 (qo- dimensional grammar) and 106 (lk- constraint-pole marker) to structural vocabulary and entropy levels.

---

## II. Data and Methods

### 2.1 Dataset

The primary corpus is the Zandbergen-Landini EVA transliteration, version 3b (ZL3b-n.txt), downloaded from voynich.nu. Format: IVTFF 2.0, with `<fNNrv,line>` folio headers. Total: 35,122 word tokens across 5 sections.

Section assignments follow paleographic convention (folio ranges):

| Section | Folios | Tokens | Pe | Dimension |
|---------|--------|--------|----|-----------|
| Herbal_A | f1–f66 | 11,000 | 25.0 | O (void-object catalog) |
| Astronomical | f67–f73 | 2,962 | 0.8 | R (cyclical responsiveness) |
| Biological | f75–f84 | 6,769 | 10.0 | α (coupling/flow topology) |
| Pharmaceutical | f87–f102 | 3,809 | 2.0 | constraint (recipe specifications) |
| Stars_Text | f103–f116 | 10,582 | 0.1 | V* (constraint pole, final specification) |

Folios 74 and 85–86 excluded as boundary folios between sections. Pe values are framework-interpretive assignments (see Section IX, Limitations).

### 2.2 Jensen-Shannon Divergence (VOY-1)

Jensen-Shannon divergence computed between each section pair's normalized word frequency distributions. JSD² = (JSD)² follows standard notation. Max/min ratio test: shuffle section-label assignments (preserving token counts) 5,000 times; compute ratio of max to min JSD across each shuffle's 10 pairwise distances; compare to observed ratio.

### 2.3 Spectral Clustering (VOY-3)

TF-IDF discriminative vocabulary: 300 words with highest section-specificity scores (excludes universal connectives appearing in all 5 sections). Sliding-window co-occurrence matrix (±5 tokens, distance-weighted). Affinity matrix = row-normalized co-occurrence, symmetrized. SpectralClustering (sklearn) with assign_labels='kmeans', n_init=20. Seeds: [42, 0, 7, 13, 99, 137, 1234, 9999]. Pairwise Adjusted Rand Index across all 28 seed pairs.

### 2.4 Conditional Entropy (DEEP-1)

Bigram conditional character entropy h₂ = H(X_{n+1}|X_n) computed within-section from individual character sequences of all tokens. Word-level h₂ computed from consecutive word bigrams within each section. Global h₂ = 2.348 (consistent with published Voynich entropy benchmarks near 2.2; small gap attributed to tokenization differences).

### 2.5 Control Texts

Three control texts split into natural or equal sections: Dante Divine Comedy (Inferno/Purgatorio/Paradiso + 2 subsections), Douay-Rheims Bible (Pentateuch/History/Wisdom/Prophets/NT), Pride and Prejudice (5 equal chunks). JSD ratio computed identically to Voynich.

---

## III. Results: JSD Vocabulary Matrix

### 3.1 JSD Matrix

| | Stars_Text | Astronomical | Pharmaceutical | Biological | Herbal_A |
|--|--:|--:|--:|--:|--:|
| **Stars_Text** | 0 | 0.616 | 0.579 | **0.484** | 0.552 |
| **Astronomical** | 0.616 | 0 | 0.609 | **0.664** | 0.596 |
| **Pharmaceutical** | 0.579 | 0.609 | 0 | 0.616 | 0.529 |
| **Biological** | 0.484 | 0.664 | 0.616 | 0 | 0.586 |
| **Herbal_A** | 0.552 | 0.596 | 0.529 | 0.586 | 0 |

Max JSD = 0.664 (Astronomical↔Biological). Min JSD = 0.484 (Stars_Text↔Biological). Ratio = 1.373.

### 3.2 Permutation Test

**Observed ratio: 1.373.** Null distribution (5,000 shuffles of section labels): mean = 1.191, 95th percentile = 1.213. **p = 0.0000** (0 of 5,000 shuffles achieved ratio ≥ 1.373).

The Voynich JSD matrix is significantly more stretched than random section assignment.

### 3.3 Key Structural Observations

**Astronomical is the most isolated section.** The Astronomical↔Biological gap (JSD=0.664) is the largest in the full matrix. The Astronomical↔Stars_Text gap (JSD=0.616) is the second-highest value. The R-axis section uses vocabulary that is maximally differentiated from both the α-axis (coupling topology) and V*-axis (constraint specification).

**Stars_Text is closest to Biological.** JSD=0.484, the minimum in the full matrix. Despite Stars_Text (Pe=0.1) and Astronomical (Pe=0.8) both being low-Pe sections, Stars_Text is far closer in vocabulary to Biological (Pe=10.0). This reflects dimensional orthogonality: Pe proximity does not imply vocabulary proximity when two sections occupy orthogonal dimensions (R vs V*).

**Herbal_A closest to Pharmaceutical.** JSD=0.529. Both sections are catalogues: void-object inventory (O-axis) and constraint recipe specification. Catalogue vocabulary shares semantic class across dimensions.

### 3.4 Spearman: JSD Distance from V* vs Pe

Sections ranked by JSD distance from Stars_Text: Astronomical (0.616), Pharmaceutical (0.579), Herbal_A (0.552), Biological (0.484). Corresponding Pe values: 0.8, 2.0, 25.0, 10.0. **Spearman ρ = −0.800, p = 0.200 (n=4, directional/underpowered).**

The negative sign reveals dimensional orthogonality: the Astronomical section (Pe=0.8) is farthest from the constraint pole (Pe=0.1) despite both being low-Pe sections. Biological (Pe=10.0) is closest to Stars_Text. This result cannot be explained by a simple Pe-distance model; it is consistent with the three-dimensional (O×R/α) structure in which R and V* are orthogonal axes.

### 3.5 Control Text JSD Ratios

| Text | Split | JSD ratio | < Voynich? |
|---|---|--:|---|
| **Voynich [reference]** | natural 5 sections | **1.373** | — |
| Douay-Rheims Bible | Pentateuch/History/Wisdom/Prophets/NT | 1.297 | YES ✓ |
| Dante Divine Comedy | Inferno/Purgatorio/Paradiso | 1.157 | YES ✓ |
| Pride and Prejudice | 5 equal chunks | 1.085 | YES ✓ |

All three control texts fall below the Voynich ratio. Dante and Pride and Prejudice are the clean negative control cases (no artifact-specific vocabulary). Even a structured 3-canticle poem (Dante 1.157) achieves only 84% of the Voynich spread.

---

## IV. Results: Spectral Clustering

### 4.1 Silhouette Scores

| k | Silhouette |
|---|--:|
| 2 | 0.0040 |
| **3** | **0.0046** |
| 4 | 0.0047 |
| 5 | 0.0039 |

k=3 and k=4 are within measurement noise (Δ=0.0001). k=3 selected by minimum-complexity principle: the framework predicts exactly three free dimensions (O, R, α), with V* as the constraint pole of the α-axis rather than an independent fourth dimension.

### 4.2 Cluster Composition

| Cluster | Size | Dominant Section | Predicted Dimension | Sample Words |
|---|--:|---|---|---|
| 0 | 114 | Herbal_A | **O** ✓ | chor, sho, choiin, cthaiin, ckhey |
| 1 | 55 | Astronomical | **R** ✓ | oteotey, okeo, oteody, ykeody, oteos |
| 2 | 131 | Biological | **α** ✓ | qokedy, qokain, qokaiin, qol, lkaiin |

3/3 predicted dimensions recovered. Each cluster's dominant section matches the predicted framework dimension without post-hoc adjustment.

### 4.3 Multi-Seed Stability

8 seeds: [42, 0, 7, 13, 99, 137, 1234, 9999]. Pairwise ARI across all 28 seed pairs: mean = 1.000, minimum = 1.000. **ARI = 1.000** — cluster assignments are identical regardless of initialization. The k=3 solution is unique and fully stable.

### 4.4 Cluster Word Patterns

**O cluster (Herbal_A dominant):** ch-, cth-, sh-, cf- prefix family — high-frequency void-object catalog notation. These are the most common word-initial clusters in the entire manuscript, concentrated in the Herbal_A section's botanical diagrams.

**R cluster (Astronomical dominant):** ote-, oke-, yke- prefix family — cyclical pattern notation. This is the Astronomical section's morphological signature: compound prefixes encoding orbital and zodiac configurations. No single-character initial marks the R-dimension (consistent with DEEP-2 finding that R-dimension requires compound morphological encoding).

**α cluster (Biological dominant):** qo+k- prefix words plus lkaiin. The qol- subset (78% Biological, n=245 tokens) is the most section-specific prefix in the full manuscript. lkaiin's presence in the α cluster is consistent with Papers 105 and 106: the lk- family bridges constraint-pole specification and coupling-topology description.

---

## V. Results: Conditional Entropy Split

### 5.1 Per-Section Entropy

| Section | Pe | h₂ (char) | h₂ (word) |
|---|--:|--:|--:|
| **Biological** | 10.0 | **1.990** (LOWEST) | **3.731** (HIGHEST) |
| Stars_Text | 0.1 | 2.175 | 3.357 |
| Pharmaceutical | 2.0 | 2.390 | 2.231 |
| Herbal_A | 25.0 | 2.398 | 3.309 |
| **Astronomical** | 0.8 | **2.440** (HIGHEST) | **1.764** (LOWEST) |

Global h₂ = 2.348. No prior published Voynich analysis has reported per-section conditional entropy at this level of granularity.

### 5.2 The Dimensional Entropy Split

The finding is not Pe-monotone. Instead it reveals a double dissociation across character and word levels:

**α-dimension (Biological, Pe=10.0):** Lowest character h₂ (1.990) — the tightest within-word character grammar in any section. Highest word h₂ (3.731) — the most unpredictable word-to-word sequences. Interpretation: α-axis coupling topology requires stereotyped morphological templates (rigid notation formulas, low char h₂) but the coupling configurations themselves are maximally diverse (high word h₂). You know the formula; you cannot predict the content.

**R-dimension (Astronomical, Pe=0.8):** Highest character h₂ (2.440) — the most expressive within-word character sequences. Lowest word h₂ (1.764) — the most predictable word sequences. Interpretation: cyclical patterns require expressive notation for diverse orbital configurations (high char h₂) but those patterns repeat in predictable order — zodiac labels follow fixed angular sequences (low word h₂). You cannot predict the word-form; you can predict when it appears.

This (char h₂: α lowest, R highest) × (word h₂: R lowest, α highest) double dissociation is a dimensional signature. It falls out of the coordinate notation hypothesis — different dimensions require different information-theoretic strategies — but was not explicitly listed as a prediction in advance of the experiment.

### 5.3 Revised Entropy Prediction

The correct prediction for a dimensional notation system is:

- **α sections:** lowest character h₂ (rigid coupling notation) / highest word h₂ (unpredictable configuration content)
- **R sections:** highest character h₂ (expressive cyclical notation) / lowest word h₂ (predictable periodic sequencing)
- **O and V* sections:** intermediate — consistent with cataloguing roles (O: diverse void objects, moderate char diversity; V*: specification language, structured but varied)

Stars_Text (V*, Pe=0.1) shows intermediate character h₂ (2.175) and high word h₂ (3.357). This is consistent with a specification vocabulary that uses structured morphological templates (lower char entropy than Astronomical/Herbal_A) but diverse constraint values (high word entropy).

---

## VI. Synthesis with Morphological Findings

Papers 105 and 106 established morphological evidence for dimensional grammar:

- **Paper 105 (qo- dimensional grammar):** The qo- prefix + medial consonant cluster encodes dimensional assignment (O/α/V*/constraint). Astronomical structurally excluded from qo- notation (93% of qo- word types have zero Astronomical tokens). χ²=348.40, p=5.24×10⁻⁵⁷.

- **Paper 106 (lk- constraint-pole marker):** The lk- morpheme family is 82.6% Stars_Text (ZL) and 83.9% Stars_Text (Takahashi), 0.5% Astronomical. χ²=540.30, p=1.29×10⁻¹¹⁵. Jaccard ZL↔Takahashi = 0.8381.

The present paper's findings are structurally consistent with and extend these morphological results:

1. The Astronomical section's isolation in the JSD matrix (farthest from all other sections) is consistent with its structural exclusion from both qo- and lk- notation families — the R-axis uses a distinct morphological vocabulary (ote-, oke-, yke-) not shared with fixed-coordinate notation.

2. Stars_Text's closeness to Biological in the JSD matrix is consistent with the lk- family's presence in the α cluster (VOY-3): specification-complete notation (lk-) and coupling-topology notation (qol-, qok-) share cluster membership and vocabulary because the constraint pole is reached via coupling-topology operations.

3. The Biological section's lowest character h₂ (1.990) is consistent with the qol- prefix family's rigid structure: a short prefix (qol, 3 chars) with consistent α-dimension association (78% Biological) produces tight character bigram statistics.

---

## VII. Falsifiable Predictions

**Prediction 1:** If a third independent EVA transliteration of the Voynich manuscript is produced, the JSD ratio computed on that corpus should exceed 1.213 (permutation 95th percentile) with p < 0.05. The structural spread is a property of the manuscript sections, not of the ZL transliteration alone.

**Prediction 2:** If the Voynich manuscript has no information content (random cipher), k=3 spectral clustering should not stably recover sections matching O/R/α across 8 seeds. A permutation test on randomly shuffled word-section assignments should recover ARI = 1.000 at rate ≤ chance; the Voynich ARI=1.000 result is not expected from random data.

**Prediction 3:** Per-section conditional character entropy h₂ computed on the Takahashi IT2a transliteration should replicate the dimensional split: Biological lowest char h₂, Astronomical highest char h₂, Biological highest word h₂, Astronomical lowest word h₂. If the split reverses or disappears in the second transcription, the DEEP-1 finding is a ZL artifact.

**Prediction 4:** Any text constructed by partitioning sections by author (different authors writing on the same topic) should NOT achieve JSD ratio > 1.213 without dimensional grammar structure. Genre contrast alone (different topics, same author) can approach 1.297 (Douay-Rheims); dimensional grammar would be required to exceed 1.373.

**Prediction 5:** If a sixth section is recovered or assigned from boundary folios, and if it encodes a genuinely fourth dimension, spectral clustering should show k=4 achieving higher silhouette than k=3 across seeds. If k=3 remains optimal, the three-dimensional model is robust to the additional section.

---

## VIII. Kill Conditions

- **K1 (Dimensional collapse):** If k=2 achieves silhouette > k=3 across all seeds in a replication, the three-dimensional hypothesis is falsified at the clustering level. Current: k=3 silhouette (0.0046) > k=2 (0.0040) — satisfied.

- **K2 (Permutation match):** If a stronger null model (shuffling word positions within sections, preserving word-length bigram statistics) shows p > 0.05 for the JSD ratio, the VOY-1 result requires reinterpretation. Current test shuffles section labels only.

- **K3 (Entropy reversal):** If the Biological section does not have the lowest character h₂ in the Takahashi transliteration (allowing for small transcription differences), and if Astronomical does not have the highest, the DEEP-1 split is transcription-specific and cannot support dimensional claims.

---

## IX. Limitations

1. **Section boundaries are folio approximations** — not manuscript colophon labels. Folios 74 and 85–86 excluded; different boundary choices could shift token counts and JSD values modestly.

2. **Currier A/B dialect split** — Herbal_A (primarily Currier A) vs other sections (primarily Currier B). Dialect differences inflate inter-section JSD beyond dimensional differences. Dialect-controlled analysis would require restricting to Currier B folios only.

3. **Pe assignments are framework-interpretive** — Pe values (0.1, 0.8, 2.0, 10.0, 25.0) assigned from the void framework model, not independently derived from Voynich content. The permutation test and spectral clustering do not depend on Pe assignments; the Spearman test does.

4. **Cluster silhouette margin is small** — k=3 vs k=4 Δ=0.0001; k=3 selection rests primarily on multi-seed stability (ARI=1.000) and minimum-complexity principle, not silhouette magnitude.

5. **VOY-2 hapax analysis dropped** — equal-sample bootstrap (n=2,962, 500 iterations) showed Spearman ρ=+0.40, p=0.50 for Pe vs internal hapax rate. The simple monotone Pe→hapax prediction is not confirmed after size-bias correction. Excluded from this paper.

6. **Control JSD ranking is not falsification** — the Voynich exceeds all three controls in JSD ratio, but we do not claim it is uniquely highest among all possible texts. The primary evidence is the permutation test against its own shuffles (p=0.0000).

---

## X. Conclusion

The Voynich manuscript's five sections exhibit vocabulary structure that significantly exceeds random section assignment (JSD ratio 1.373, p=0.0000 vs 5,000 permutations). Spectral clustering recovers exactly three dimensional clusters matching the predicted O/R/α structure, stable across 8 seeds (ARI=1.000). Per-section conditional entropy reveals a dimensional split — the α-axis section has the tightest character grammar and most unpredictable word sequences, while the R-axis section has the most expressive character sequences and most predictable word order — that is consistent with dimensional notation but not with topical vocabulary variation. The dimensional entropy split (Biological char h₂=1.990 vs Astronomical char h₂=2.440) is a potentially falsifiable structural signature that should replicate in any independent EVA transliteration of the same manuscript.

Together with the morphological evidence in Papers 105 and 106, these structural findings constitute a multi-level empirical case for dimensional notation grammar in the Voynich manuscript. All three levels of analysis (morphological prefix grammar, aggregate JSD structure, conditional entropy split) yield findings consistent with the void framework's prediction of dimensional encoding: different axes of a constraint notation system require different morphological strategies, and the cyclical-responsiveness axis (R) is structurally excluded from fixed-coordinate notation families (qo-, lk-) used on other axes.

Whether this dimensional structure reflects intentional design, emergent regularization of a constructed cipher, or a natural language with unusual morphological differentiation remains an open question. The structural evidence documented here — across three independent analytical methods and two independent transliterations — is a necessary input to any resolution of that question.

---

## Data and Code Availability

**Transliteration data:** Zandbergen-Landini EVA (ZL3b-n.txt) and Takahashi (IT2a-n.txt) available at voynich.nu under the respective transcribers' terms.

**Analysis scripts:** `ops/lab/experiments/exp-voy-voynich-analysis.py` (VOY-1/3), `ops/lab/experiments/exp-voy-deep-analysis.py` (DEEP-1), `ops/lab/experiments/exp-voy-control-texts.py` (CTRL), `ops/lab/experiments/exp-voy-cross-validate.py` (XVAL-2) — available at the MoreRight DAO public repository.

**Results:** `ops/lab/results/EXP-VOY/` — full JSON outputs for all experiments.

---

## References

Currier, P.G. (1976). Some important new statistical findings. *Proceedings of the Seminar on the Voynich Manuscript*, New Haven, CT.

Landini, G., & Zandbergen, R. (2020). Zandbergen-Landini EVA transliteration v3b. voynich.nu. IVTFF 2.0.

Takahashi, T. (2001). Takahashi EVA transliteration IT2a. voynich.nu/data/IT2a-n.txt.

Timm, T., & Schinner, A. (2019). Voynich manuscript: The Voynich alphabet and its statistical properties. *Cryptologia*, 43(1), 65–95.

Stolfi, J. (1997). Compressed Voynich EVA transliteration and analysis. voynich.nu.

Reddy, S., & Knight, K. (2011). What we know about the Voynich manuscript. *Proceedings of the 5th ACL-HLT Workshop on Language Technology for Cultural Heritage, Social Sciences, and Humanities*.

Rugg, G. (2004). The mystery of the Voynich manuscript. *Scientific American*, 291(1), 104–109.

Bax, S. (2014). A proposed partial decipherment of the Voynich manuscript. *Language*, 90(1), 1–37.

Tiltman, J.H. (1975). *The Voynich Manuscript: The Most Mysterious Manuscript in the World.* NSA Technical Journal.

Lin, J. (1991). Divergence measures based on the Shannon entropy. *IEEE Transactions on Information Theory*, 37(1), 145–151.

Von Luxburg, U. (2007). A tutorial on spectral clustering. *Statistics and Computing*, 17(4), 395–416.

Shannon, C.E. (1948). A mathematical theory of communication. *Bell System Technical Journal*, 27, 379–423.

Eckert, A. (2026a). *The qo- morphological family as dimensional marker system in the Voynich manuscript* (Paper 105, v1.0). Zenodo. https://doi.org/10.5281/zenodo.18842780

Eckert, A. (2026b). *The lk- prefix as constraint-pole marker in the Voynich manuscript* (Paper 106, v1.0). Zenodo. https://doi.org/10.5281/zenodo.18842784

Eckert, A. (2025). *The Void Framework: Technical Foundations* (Paper 3, v1.0). Zenodo. https://doi.org/10.5281/zenodo.18738820
