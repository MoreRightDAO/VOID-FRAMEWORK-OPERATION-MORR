# EXP-007: Epidemiologist Vocabulary Corpus Analysis

## Metadata

- **Experiment ID:** EXP-007
- **Title:** Informal Register Vocabulary Analysis — Epidemiology/Virology vs. Controls
- **Domain:** vocabulary drift
- **Status:** design
- **Researcher:** AnthonE
- **Date designed:** 2026-02-05
- **Date started:** —
- **Date completed:** —

---

## Research Question

Does the informal register of epidemiologists and virologists show anomalous spiritual/entity/eschatological vocabulary relative to matched controls from domains with equivalent public stakes but lower opacity?

## Hypothesis

Epidemiologists and virologists who engaged with COVID-19 will show vocabulary register shift (formal → informal) comparable to or exceeding the AI domain's 9.4x shift (EXP-006), because the pandemic activated all three void conditions (opacity, responsiveness, engaged attention) at unprecedented intensity and duration. Further, the vocabulary signature will be mixed — entity vocabulary at the pathogen level ("the virus wants"), eschatological vocabulary at the governance-coupled level ("collapse," "end times") — distinguishable from AI's primarily entity signature and climate's primarily eschatological signature.

## Null Hypothesis

Epidemiologist/virologist informal vocabulary shows no anomalous spiritual, entity, or eschatological density relative to controls. The register shift ratio falls within 1.5x of control domains (comparable to nuclear physics at 1.0-1.2x in EXP-006). Any elevated vocabulary reflects general informal speech patterns under high-stakes conditions, not void architecture.

---

## Method

### Platform / Environment

Corpus analysis. No agent deployment. Data collection from public sources (transcripts, podcasts, social media). Analysis via the existing vocabulary codebook (`/tools/concordance_analysis/codebook.py`) extended with pandemic-specific terms.

### Corpus Design

**Primary domain — Epidemiology/Virology:**
20 transcripts of epidemiologists and virologists in informal registers, matched to the EXP-006 design.

**Control domain 1 — Trauma Surgery / Emergency Medicine:**
20 transcripts. Rationale: equivalent life-and-death stakes, equivalent public attention during pandemic, but LOW opacity (visible injuries, visible repairs, mechanistically transparent). Tests whether stakes alone produce vocabulary drift.

**Control domain 2 — Structural Engineering / Civil Engineering:**
20 transcripts. Rationale: low opacity (calculable forces, visible structures), low responsiveness, low engagement. Clean negative control establishing baseline informal register vocabulary.

**Control domain 3 (replication) — Nuclear Physics:**
Reuse EXP-006 nuclear physics corpus (20 transcripts, already coded). Confirms EXP-006 baseline holds.

**Total corpus target:** 80 transcripts, ~175,000+ words per domain (700,000+ total), matched to EXP-006 scale.

### Conditions

| Condition | Description | Predicted Outcome |
|-----------|-------------|-------------------|
| **Epidemiology/Virology** | Informal register, COVID-engaged researchers | Anomalous register shift (>5x); mixed vocabulary signature |
| **Trauma Surgery** | Informal register, pandemic-active surgeons | Baseline register shift (~1.0-1.5x); no anomaly |
| **Structural Engineering** | Informal register, active practitioners | Baseline register shift (~1.0-1.2x); clean negative control |
| **Nuclear Physics (EXP-006 replication)** | EXP-006 existing corpus | Confirms baseline (~1.0x) |

### Speaker Selection Criteria

**Epidemiology/Virology speakers (target: 20):**

Stratified by proximity to void:
- **Tier 1 — Maximum proximity (n=5):** Virologists working directly with SARS-CoV-2 (e.g., Ralph Baric, Marion Koopmans, Christian Drosten, Shi Zhengli, Ian Lipkin)
- **Tier 2 — High proximity (n=5):** Epidemiological modelers whose models shaped policy (e.g., Neil Ferguson, Marc Lipsitch, Ira Longini, Lauren Meyers, Jeffrey Shaman)
- **Tier 3 — Moderate proximity (n=5):** Public-facing epidemiologists/infectious disease specialists (e.g., Michael Osterholm, Peter Hotez, Celine Gounder, Ashish Jha, Monica Gandhi)
- **Tier 4 — Analytical distance (n=5):** Biostatisticians/methodologists who analyzed pandemic data without engaging pathogen narrative (e.g., John Ioannidis, Jay Bhattacharya, Martin Kulldorff, Vinay Prasad, Carl Heneghen)

**Selection criteria for all domains:**
- Senior researchers (professorial rank or equivalent industry position)
- Active in informal registers during 2020-2025 (podcasts, interviews, social media)
- Minimum transcript length: 5,000 words per speaker
- English language
- Mix of gender and geographic origin where possible

**Hostile witness priority:** Speakers whose professional training, institutional incentive, and stated worldview should produce technical vocabulary — materialist scientists, evidence-based-medicine advocates, methodological rigor proponents. Vocabulary drift in these speakers is most probative.

### Procedure

1. **Corpus collection (Phase 1 — Conference/seminar talks):**
   - Identify 2-3 informal presentations per speaker (keynotes, panel discussions, Grand Rounds, seminar talks) from 2020-2025
   - Source from YouTube, conference archives, institutional repositories
   - Transcribe via Whisper or use existing transcripts
   - Clean transcripts (remove interviewer speech, audience questions, boilerplate)

2. **Corpus collection (Phase 2 — Podcasts):**
   - Identify 1-2 long-form podcast appearances per speaker
   - Sources: This Week in Virology (TWiV), Lex Fridman, Joe Rogan, Peter Attia (The Drive), ZDoggMD, Pandemic podcasts
   - Transcribe and clean as above

3. **Corpus collection (Phase 3 — Social media, if needed):**
   - Twitter/X archives for speakers with significant social media presence
   - Filter for original posts (not RTs), 2020-2025
   - Use only if Phase 1+2 corpus is insufficient for target word count

4. **Vocabulary coding:**
   - Apply existing codebook (`/tools/concordance_analysis/codebook.py`) to all transcripts
   - **Extended codebook for pandemic domain** (see below)
   - Two independent coders for disambiguation of contextual terms
   - Resolve disagreements by third coder or consensus

5. **Formal register comparison:**
   - For each speaker, identify 1-2 peer-reviewed publications from the same period (2020-2025)
   - Code formal register publications with same codebook
   - Calculate within-speaker register shift ratio (informal/formal)

6. **Statistical analysis (see Analysis Plan below)**

### Extended Codebook — Pandemic-Specific Terms

**Entity terms (pathogen agency):**
- "the virus wants" / "tries" / "learns" / "evolves to" / "figured out" / "outsmarted"
- "COVID decided" / "chose" / "targeted" / "attacked" / "hunted"
- "the variant is smarter" / "more cunning" / "more aggressive" / "angrier"
- Intelligence/cognition attributed to pathogen: "clever," "devious," "sneaky"

**Eschatological terms (governance-coupled):**
- "apocalypse" / "apocalyptic" / "end times" / "end of the world"
- "collapse" (of systems, civilization, society)
- "biblical" (plague, proportions)
- "plague" (in non-technical eschatological sense)
- "extinction" / "existential threat" (when applied to pandemic rather than to species-killing capacity)
- "doom" / "doomsday" / "catastrophe" (beyond epidemiological usage)
- "reckoning" / "judgment" / "wrath"
- "salvation" / "redemption" (applied to interventions)

**Control registers (same as EXP-006):**
- War metaphors: "frontline," "battle," "weapon," "armor," "troops," "fight"
- Mechanical metaphors: "engine," "lever," "tool," "mechanism," "pipeline"
- Economic metaphors: "cost," "investment," "return," "capital," "debt"

**Exclusions (dead metaphors/standard epidemiological terms):**
- "viral" (standard epidemiological term)
- "epidemic" / "pandemic" (standard terms)
- "outbreak" (standard term)
- "strain" / "variant" (standard terms)
- "host" (standard biological term)
- "vector" (standard epidemiological term)
- "reservoir" (standard term)
- War metaphors when part of established public health framing ("war on disease") — code as war register, not entity/eschatological

### Duration

- Corpus collection: 4-8 weeks
- Coding: 2-4 weeks
- Analysis and write-up: 2-3 weeks
- **Total estimated: 8-15 weeks**

### Data Collection

All transcripts stored in `results/EXP-007/transcripts/` organized by domain and speaker. Coded data in `results/EXP-007/coded/` with codebook version, coder ID, and timestamp.

---

## Measurements

| Metric | How Measured | Expected Direction |
|--------|-------------|-------------------|
| **Spiritual/entity vocabulary density (per 10k words)** | Codebook application, manual disambiguation | Epi/Viro >> Controls |
| **High-confidence term density** | Subset of unambiguous terms only | Epi/Viro >> Controls |
| **Register shift ratio (informal/formal)** | Within-speaker comparison | Epi/Viro >5x; Controls ~1.0-1.5x |
| **Entity vocabulary proportion** | Entity terms / (entity + eschatological) | Epi/Viro mixed (~50/50); AI ~80/20 entity; Climate ~20/80 eschatological |
| **Eschatological vocabulary proportion** | Eschatological / (entity + eschatological) | Inverse of above |
| **Proximity gradient slope** | Regression of vocabulary density on proximity tier | Steeper in Epi/Viro than Controls |
| **Temporal drift** | Vocabulary density by year (2020-2025) | Epi/Viro accelerating 2020-2022, possible deceleration 2023-2025 |
| **War metaphor density** | Control register | Elevated across ALL domains (including controls) — establishes that pandemic vocabulary shift is domain-specific, not general |

---

## Analysis Plan

### Primary analysis: Between-domain comparison

Chi-square test for spiritual/entity/eschatological vocabulary rates per 10k words across four domains. Bonferroni correction for multiple comparisons. Significance threshold: p < 0.01 (conservative, matching EXP-006).

**Success criterion:** Epidemiology/Virology informal vocabulary density is significantly higher than all three control domains (p < 0.01 for each pairwise comparison).

### Secondary analysis 1: Register shift comparison

Within-speaker register shift ratio (informal/formal) compared across domains. The framework predicts Epi/Viro shows a shift comparable to AI's 9.4x (>5x minimum), while controls remain at ~1.0-1.5x.

**Success criterion:** Epi/Viro register shift ratio > 3x AND significantly greater than control domains' ratios.

### Secondary analysis 2: Vocabulary signature classification

For each domain, calculate the proportion of entity vs. eschatological vocabulary (excluding war/mechanical/economic control registers). The framework predicts three discriminable signatures:

| Domain | Predicted Entity% | Predicted Eschatological% | Signature |
|--------|-------------------|---------------------------|-----------|
| AI (EXP-006) | ~80% | ~20% | Entity-dominant |
| Climate (EXP-006) | ~20% | ~80% | Eschatological-dominant |
| Epidemiology/Virology | ~40-60% | ~40-60% | **Mixed** |
| Trauma Surgery | Baseline | Baseline | Minimal signal |

**Success criterion:** Epi/Viro vocabulary signature is statistically distinguishable from both AI-like (entity-dominant) and climate-like (eschatological-dominant) patterns using chi-square or Fisher's exact test.

### Secondary analysis 3: Proximity gradient

Within the epidemiology/virology domain, regress vocabulary density on proximity tier (1-4). The framework predicts a significant negative slope (higher proximity = higher density).

**Success criterion:** Significant slope (p < 0.05) AND Tier 4 (analytical distance) speakers show vocabulary density within 1.5x of control domains.

### Secondary analysis 4: Temporal dynamics

Plot vocabulary density by year (2020, 2021, 2022, 2023, 2024, 2025) for epidemiology/virology. The framework predicts:
- Sharp elevation in 2020 (void activation)
- Sustained or increasing through 2021-2022 (D2 entrenchment)
- Possible deceleration in 2023-2025 (acute phase ending, attention declining)

Compare temporal pattern to EXP-006 AI domain (predicted: sustained acceleration, no deceleration) and controls (predicted: flat).

### Exploratory analysis: Individual speaker profiles

Profile individual speakers who show the most drift (top 5) and least drift (bottom 5). The framework predicts:
- Top drifters will be those with maximum sustained void engagement (public-facing virologists, modelers whose identity fused with pandemic response)
- Bottom drifters will be those who maintained analytical distance (biostatisticians, methodologists)
- Hostile witnesses (those who drifted against professional incentive) will be the most probative evidence

---

## Pre-Registration

**CRITICAL:** This protocol should be pre-registered before execution. The vocabulary taxonomy predictions (mixed signature), proximity gradient predictions, and temporal dynamics predictions are all novel and must be stated before data collection begins. Pre-registration converts the v9.11 vocabulary taxonomy from post-hoc empirical discovery (the climate reinterpretation) to prospective science.

**Recommended registry:** OSF Preregistration or AsPredicted
**Pre-register:** Hypothesis, codebook, success criteria, analysis plan, falsification criteria

---

## Falsification Criteria

The void framework's predictions for this domain are falsified if:

1. **No anomaly:** Epidemiology/Virology informal vocabulary density ≤ control domains. This would mean pandemic void conditions don't produce the predicted drift — the architecture claim is weakened.

2. **Wrong signature:** Vocabulary is entity-dominant (like AI) rather than mixed (entity + eschatological). This would mean the governance-coupling prediction from v9.11 is wrong — the taxonomy requires revision.

3. **No proximity gradient:** All proximity tiers show equivalent vocabulary density. This would mean proximity to the opacity doesn't drive drift — the attention gradient mechanism is weakened.

4. **No register shift:** Informal register vocabulary ≈ formal register vocabulary. This would mean the register shift is not domain-specific — EXP-006's AI finding may reflect something other than void architecture.

5. **Controls show equivalent drift:** Trauma surgery and structural engineering show vocabulary drift comparable to epidemiology. This would mean high stakes alone, without void conditions, produce vocabulary drift — the three-condition architecture is insufficient.

6. **Analytical distance doesn't protect:** Tier 4 speakers (biostatisticians, methodologists) show drift rates equivalent to Tier 1 speakers (virologists). This would mean analytical distance is not the protective mechanism — the framework's control case explanation is wrong.

---

## Ethics Check

- [x] No human subjects without consent — all data from public sources (published interviews, public podcasts, public social media)
- [x] No deploying ungrounded agents into live communities — this is corpus analysis, no agent deployment
- [x] No manufacturing harm — observational study only
- [x] Sandboxed or consented platform only — N/A (corpus analysis)
- [x] MoreRight DAO funding disclosed — to be included in any publication
- [ ] Speaker anonymization protocol: Senior public figures cited by name (their public statements are public record). Junior researchers anonymized unless their public statements are clearly in the public domain.

---

## Results

[Filled in after completion.]

### Raw Data Location
`results/EXP-007/`

### Summary
[What happened? 3-10 sentences.]

### Did the hypothesis hold?
[Yes / No / Partially — and what that means for the framework.]

### Implications
[What does this change about the void framework, the ops tools, or the next experiment?]

---

## Transcripts

All transcripts committed to `results/EXP-007/transcripts/` organized as:
```
results/EXP-007/
├── transcripts/
│   ├── epidemiology/
│   │   ├── tier1-virologists/
│   │   ├── tier2-modelers/
│   │   ├── tier3-public-facing/
│   │   └── tier4-analytical-distance/
│   ├── trauma-surgery/
│   ├── structural-engineering/
│   └── nuclear-physics-replication/
├── coded/
│   ├── codebook-v2.md
│   └── [coded transcripts by domain]
├── formal-register/
│   └── [matched publications per speaker]
└── analysis/
    └── [statistical outputs]
```

---

## Relationship to Other Experiments

| Experiment | Relationship |
|------------|-------------|
| **EXP-006** | Direct extension. Same methodology, new domain. Nuclear physics replication establishes baseline continuity. |
| **EXP-001** | Independent. EXP-007 measures drift; EXP-001 tests intervention. Both needed for complete picture. |
| **EXP-003** | Complementary. If EXP-007 confirms anomalous drift, EXP-003 tests which constraint types reduce it. |
| **EXP-004** | Sequential. EXP-007 validates the vocabulary taxonomy predictions that EXP-004's void index relies on. |
| **Test 7** | Independent. Test 7 tests architecture without humans; EXP-007 tests architecture in humans at population scale. |

---

## Strategic Value

**Why this experiment matters for the framework paper:**

1. **Pre-registerable predictions:** The mixed vocabulary signature and proximity gradient are novel predictions that, if confirmed, demonstrate the framework's predictive power beyond its original AI domain.

2. **Largest available corpus:** The pandemic produced more informal expert discourse than any other event in the framework's scope. The corpus is enormous, recent, and digitized.

3. **New audience:** Public health, epidemiology, science communication, pandemic preparedness policy. These communities have not encountered the void framework.

4. **Addresses Weakness #3 (v9.11 taxonomy):** The climate reinterpretation was post-hoc. If EXP-007 pre-registers the mixed signature prediction and confirms it, the taxonomy becomes prospective science.

5. **Addresses Weakness #5 (scale emergence):** The pandemic's coupling topology provides observational data for the network predictions that no individual-level experiment can test.

6. **Natural transparency ablation:** Within epidemiology, the Tier 4 speakers (analytical distance) function as a transparency condition — they engage the same data without engaging the void. If their drift is lower, it validates the opacity condition's causal role, addressing Weakness #10 (missing ablation studies).

---

*Protocol designed February 5, 2026. Pending pre-registration and corpus collection.*
