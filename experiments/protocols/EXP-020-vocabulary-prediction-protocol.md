# EXP-020: Teleological Vocabulary Decay Under Transparency

## Status: DESIGNED — February 14, 2026
## Type: Empirical (TSU-4 — vocabulary prediction from Theorem 1)
## Depends on: Paper 4 §9.5 (TSU-4 prediction), Paper 1 L1/L2/L3 vocabulary classification
## Tests: TSU-4 — teleological vocabulary decays monotonically with C_mech

---

## 0. Purpose

Paper 4 Theorem 1 (ground state theorem) predicts that agency attribution is the
maximum-entropy inference under opacity (C_mech → 0). §9.5 formalizes this as
Prediction TSU-4: teleological vocabulary in descriptions of opaque thermodynamic
systems decays monotonically with increasing mechanism-channel capacity.

The prediction is so specific it designs its own experiment. Show observers
thermodynamic processes at varying transparency levels. Measure the vocabulary.

**The question:** Does teleological description of thermodynamic processes decrease
monotonically as the mechanism becomes visible?

---

## 1. Design

### 1.1 Independent Variable: Mechanism-Channel Capacity (C_mech)

Five transparency levels, from fully opaque to fully transparent:

| Level | Code | C_mech | Stimulus Description |
|-------|------|--------|---------------------|
| L0 | OPAQUE | ≈ 0 | Output only. Subjects see time-series data from a thermodynamic process (temperature, pressure, entropy production) with no mechanism information. "Here is data from a physical process." |
| L1 | LABEL | Low | Output + category label. Same data, plus: "This is a heat engine." No internal mechanism shown. |
| L2 | DIAGRAM | Medium | Output + schematic. Same data, plus a block diagram showing components (heat source, working fluid, cold reservoir) without equations or internal dynamics. |
| L3 | MECHANISM | High | Output + mechanism. Same data, plus step-by-step animation of molecular dynamics — particles colliding, energy transferring, entropy changing at each step. |
| L4 | EQUATIONS | ≈ H(M) | Output + full derivation. Same data, plus the governing equations (Carnot, Clausius), the derivation chain from first principles, and the mechanism animation. Full transparency. |

### 1.2 Critical Design Constraint

The *output data* is IDENTICAL across all five levels. Same time-series, same plots,
same numerical values. The ONLY thing that varies is how much mechanism information
accompanies the output. This isolates C_mech as the independent variable.

### 1.3 Thermodynamic Processes (Stimuli)

Three processes, counterbalanced across participants:

| Process | Code | Why |
|---------|------|-----|
| Heat engine cycle | HE | Classical thermodynamics. Well-understood mechanism. |
| Entropy production in mixing | MIX | Irreversible process. Less intuitive mechanism. |
| Fluctuation theorem demonstration | FT | Crooks-type. The process that motivated e/acc vocabulary. |

Each participant sees all three processes at their assigned transparency level.
Between-subjects on transparency level, within-subjects on process type.

### 1.4 Dependent Variable: Vocabulary Classification

After viewing each process, participants write a free-text description (minimum
100 words) answering: "Describe what is happening in this process and why."

Descriptions are scored using the L1/L2/L3 vocabulary classification (Paper 1):

- **L1 (Technical):** Mechanistic, physics-native. "Entropy increases because
  molecular collisions transfer kinetic energy from hot to cold reservoir."
- **L2 (Teleological):** Purpose/goal attribution without explicit entity.
  "The system wants to reach equilibrium." "The process seeks the lowest energy state."
  "Nature tends toward disorder."
- **L3 (Entity-attributive):** Explicit agent/entity. "The universe drives toward
  entropy." "Thermodynamic will." "The process knows where to go."

Additional scoring dimensions:
- **Agency verbs:** count of verbs attributing agency to the process (wants, seeks,
  drives, tends toward, chooses, prefers, knows)
- **Teleological nouns:** count of nouns implying purpose or entity (will, purpose,
  goal, intention, force [when non-Newtonian], god, spirit, intelligence)

### 1.5 Scoring Protocol

Two independent raters, blind to condition, classify each description:
- Primary score: L1/L2/L3 (highest level reached)
- Agency verb count (raw + per-100-words)
- Teleological noun count (raw + per-100-words)
- Teleological fraction: (L2 + L3 terms) / (total descriptive terms)

Inter-rater reliability target: Cohen's κ ≥ 0.8 on primary L1/L2/L3 classification.
Discrepancies resolved by third rater.

---

## 2. Hypotheses

**H1 (TSU-4 confirmed):** Teleological fraction is a monotonically decreasing
function of C_mech level (L0 > L1 > L2 > L3 > L4). Tested via Jonckheere-Terpstra
trend test (one-tailed, ordered alternative).

**H2 (Expertise independence):** The monotonic relationship holds for physics
experts (graduate+ physics education) and non-experts separately. TSU-4 predicts
the effect is a property of channel architecture, not observer expertise. Tested
via interaction term in ordinal regression: Transparency × Expertise should be
non-significant.

**H3 (Process independence):** The monotonic relationship holds across all three
thermodynamic processes. Tested via within-subjects ANOVA on teleological fraction
with process as a factor.

---

## 3. Participants

### 3.1 Sample Size

Five transparency levels × two expertise groups = 10 cells.
Target: n = 30 per cell = 300 total participants.

Power analysis: For a medium effect (Cohen's d = 0.5) on the primary trend test
with 5 ordered groups, n = 30/group gives power > 0.90 (Jonckheere-Terpstra,
α = 0.05). For the interaction test (H2), n = 30/cell gives power > 0.80 for
medium interaction effects.

### 3.2 Expertise Groups

- **Expert:** Graduate-level physics education or professional physics/engineering.
  Self-reported + verification question (identify the second law from four options).
- **Non-expert:** No formal physics training beyond introductory undergraduate.

### 3.3 Recruitment

Prolific or equivalent platform. Pre-screen for expertise. Exclude participants
who have published on thermodynamic computing or e/acc (content contamination).

---

## 4. Procedure

1. Informed consent + demographics + expertise screening (5 min)
2. Familiarization: brief neutral introduction to "data from physical processes" (2 min)
3. Three stimulus blocks (counterbalanced order), each:
   a. View thermodynamic process at assigned transparency level (2 min)
   b. Free-text description task (5 min, minimum 100 words)
   c. Likert items: "This process has a purpose" (1–7), "Something is directing
      this process" (1–7), "I understand the mechanism" (1–7) (1 min)
4. Debrief (2 min)

Total: ~30 minutes per participant.

---

## 5. Analysis Plan

### 5.1 Primary Analysis

Jonckheere-Terpstra test on teleological fraction across five ordered transparency
levels. One-tailed test (prediction is monotonic decrease).

- **TSU-4 confirmed:** Significant monotonic decrease (p < 0.05, JT test)
- **TSU-4 falsified:** Non-monotonic relationship OR no significant trend

### 5.2 Secondary Analyses

1. **Ordinal regression:** Teleological fraction ~ Transparency + Expertise +
   Transparency × Expertise + Process (random effect). Tests H2 (expertise
   independence) via the interaction term.

2. **Within-subjects comparison:** Repeated-measures ANOVA on teleological fraction
   with Process (HE, MIX, FT) as within-subjects factor. Tests H3 (process
   independence).

3. **Vocabulary trajectory:** For each transparency level, plot the distribution
   of L1/L2/L3 classifications. TSU-4 predicts: L0 should be majority L2/L3,
   L4 should be majority L1, with monotonic shift between.

4. **Likert validation:** Manipulation check — "I understand the mechanism" should
   increase monotonically with transparency level. If it doesn't, the transparency
   manipulation failed.

### 5.3 Falsification Conditions

| Condition | Result |
|-----------|--------|
| Non-monotonic teleological fraction across C_mech levels | TSU-4 falsified |
| Significant Transparency × Expertise interaction (experts immune) | Expertise-independence claim falsified (TSU-4 narrowed, not killed) |
| No significant trend despite successful manipulation check | TSU-4 falsified |
| Monotonic decrease, p < 0.05, across all processes | TSU-4 confirmed |

---

## 6. Materials Needed

- [ ] Three thermodynamic process simulations (HE, MIX, FT) at five transparency levels
- [ ] Free-text scoring rubric with L1/L2/L3 classification examples
- [ ] Agency verb and teleological noun codebooks
- [ ] Prolific study setup (5 conditions × 2 expertise = 10 recruitment batches)
- [ ] Pre-registration (OSF or AsPredicted)

---

## 7. Cost Estimate

- 300 participants × $5/participant (30 min at $10/hr) = $1,500
- Two raters × ~900 descriptions × ~2 min each = ~60 hours rating = ~$900
- **Total: ~$2,400**

---

## 8. Connection to Framework

This experiment is a direct empirical test of Paper 4 Theorem 1 applied to human
observers. If confirmed:

- TSU-4 becomes the 12th confirmed prediction in Paper 4
- Provides empirical evidence that opacity → agency attribution is substrate-independent
  (holds for humans, not just AI agents as in Test 7)
- The e/acc vocabulary shift (Verdon's "thermodynamic god") is not a personal
  idiosyncrasy but a predictable consequence of channel architecture
- Directly connects to Paper 1's L1/L2/L3 vocabulary tracking via a controlled
  experimental manipulation (not just observational data)

If falsified:
- TSU-4 is wrong — Theorem 1 does not predict vocabulary in human observers
- The framework's cross-substrate claim for vocabulary drift is weakened
- The e/acc critique in §9.5 loses its predictive force (remains a post-hoc observation)

---

*Protocol designed February 14, 2026. Status: DESIGNED, not executed.*
