# EXP-027: Coin Flip Statistical Pressure Drift Test

## Status: REGISTERED — 2026-03-07. Protocol open. Pre-registration required before data collection.
## Type: Null-case validation + presentation-layer causal isolation
## Kills if met: KC-NULL (Pe formula fails at constraint pole — transparent/invariant/independent process produces drift at d > 0.20 vs. opaque presentation)
## Depends on: Paper 3 (Pe formula), Paper 4 (Bernoulli manifold, Langevin dynamics), EXP-022 (constraint current baseline)

---

## 0. Purpose

The Pe formula predicts that a fully transparent, invariant, independent process produces Pe near zero and therefore no drift. A fair coin flip is the cleanest possible test of this prediction — the mechanism is visible (O=0), the outcome doesn't adapt to the observer (R=0), and disengagement is trivial (C=0).

**The critical test:** Present *identical* Bernoulli sequences (p=0.5) through interfaces with different structural void properties. If drift vocabulary emerges only when the presentation layer raises O/R/C — and not when the underlying process is presented transparently — the framework's claim that structure (not content) drives drift is confirmed at the null case.

**Why this matters:**
- Coin flips are the Bernoulli manifold's ground state (theta = 0.5, maximum entropy)
- Any drift observed under transparent presentation would falsify the Pe model at its most basic prediction
- Gambling interfaces already present random outcomes through high-Pe structures — this experiment isolates the presentation effect with a controlled random process
- Connects directly to Paper 4 Section 3 (Langevin simulation on Bernoulli manifold)

---

## 1. Design

### 1.1 Conditions

All conditions use the SAME pre-generated sequence of 500 fair coin flips (p=0.5, seed recorded and published).

| Condition | O | R | C | Presentation | Predicted Pe |
|-----------|---|---|---|--------------|-------------|
| A: Transparent | 1 | 1 | 1 | Plain text: "Flip 237: Heads." No framing, no streaks highlighted, stop anytime, mechanism stated as "fair coin, p=0.5" | ~0 |
| B: Opaque | 4 | 1 | 1 | Same sequence, but labeled "AI prediction" — mechanism hidden, no explanation of how outcomes are generated | ~4 |
| C: Opaque + Reactive | 4 | 4 | 1 | Same sequence, but interface claims to "learn your pattern" — fake personalization cues, streak highlighting, "you're on a roll" messages | ~13 |
| D: Full Void | 4 | 4 | 4 | Same sequence presented as slot-machine interface — variable reward sounds, near-miss framing, social comparison ("you're ahead of 73% of players"), session timer hidden, exit requires 3-click sequence | ~25 |
| E: Constraint Anchor | 1 | 1 | 1 | Same as A, plus explicit constraint text: "This is a fair coin. No pattern exists. Your predictions cannot influence the outcome. You may stop at any time." | ~0 (floor) |

**Random assignment:** Block randomization by age bracket (18-25, 26-40, 41+) and self-reported gambling experience (none/some/regular). Minimum N per cell: 40 (power calculation below).

### 1.2 Participants

**Target population:** Adults 18+ with no active gambling disorder diagnosis. General population recruitment via Prolific or equivalent IRB-approved research panel.

**Exclusion criteria:** Active gambling disorder (DSM-5 screener), current psychiatric inpatient treatment, prior participation in void framework studies.

**N target:** 200 total (40 per condition). Power: alpha=0.05, 1-beta=0.80, target detection d=0.50 for A vs. D comparison (primary), d=0.30 for adjacent condition comparisons (secondary).

### 1.3 Task

Participants observe 500 coin flip outcomes through their assigned interface. Before each flip, they may optionally predict the outcome (not required — prediction rate is itself a dependent variable). After the sequence, they complete:

1. **Free-response:** "Describe your experience with this task" (3-5 sentences minimum)
2. **Attribution probe:** "Did you notice any patterns in the outcomes?" (free response)
3. **Agency scale:** 5 items measuring perceived ability to predict/influence outcomes (Likert 1-7)
4. **Engagement probe:** "How difficult was it to stop watching?" (Likert 1-7)
5. **Mechanism probe:** "How does this system generate its outcomes?" (free response)

### 1.4 Dependent Variables

**Primary:**
- **D1 rate:** Agency attribution vocabulary in free responses, coded using Paper 3 vocabulary codebook by 2 blinded raters. Target markers: "it knew," "it was trying to," "the pattern was," "I could feel," "it responded to"
- **Prediction rate:** Proportion of flips where participant chose to predict (voluntary engagement metric)
- **Session duration:** Time spent beyond minimum required

**Secondary:**
- **D2 markers:** Boundary erosion vocabulary — "I couldn't stop," "just one more," "I needed to see"
- **Agency scale composite:** Mean of 5 agency attribution items
- **Pattern attribution:** Binary — did participant claim to detect a pattern? (ground truth: none exists)
- **Mechanism accuracy:** Does participant correctly identify random/coin flip process?

**Assessment:** Single session. No follow-up required (null case — no chronic exposure).

---

## 2. Analysis

### 2.1 Primary Test

**Hypothesis:** D1 rate in Condition A (transparent) is not significantly different from zero, while D1 rate in Condition D (full void) is significantly greater than zero.

**Test:** Independent samples t-test (or Mann-Whitney if non-normal) on D1 rate: Condition D vs. Condition A.

**Effect size:** Cohen's d (pooled SD).

**Predicted outcome:** d > 0.50 (medium-to-large effect of presentation structure on drift vocabulary for identical underlying random process).

### 2.2 Dose-Response Test

**Hypothesis:** D1 rate increases monotonically with Pe across conditions A < B < C < D.

**Test:** Jonckheere-Terpstra trend test across ordered conditions.

**This is the strongest test:** If drift vocabulary tracks Pe monotonically for an identical random sequence, the framework's structural claim is validated at the most fundamental level.

### 2.3 Null-Case Validation

**Hypothesis:** Condition A (transparent) and Condition E (constraint anchor) both produce D1 rate indistinguishable from zero.

**Test:** One-sample t-test of D1 rate against zero for conditions A and E separately.

**Kill fires if:** Condition A produces D1 rate significantly greater than zero (d > 0.20, p < 0.05) — transparent presentation of a fair coin should NOT produce agency attribution.

### 2.4 Pe Prediction Accuracy

**Test:** Compute observed Pe proxy (composite of D1 rate + prediction rate + session duration, z-scored) for each condition. Compare to predicted Pe from the formula using assigned O/R/C values.

**Metric:** Spearman rho between predicted Pe rank order and observed drift composite rank order across 5 conditions.

**Expected:** rho > 0.90 (rank order should be near-perfect given the large Pe spread).

### 2.5 Interpretation Rules

| Result | Interpretation |
|--------|---------------|
| A near zero, D >> A (d > 0.50) | Framework confirmed at null case — structure drives drift, not content |
| Monotonic A < B < C < D | Pe dose-response validated — strongest possible confirmation |
| A near zero, D near zero | Coin flip too simple to produce drift even with void presentation — informational, not a kill (rerun with longer sequences or richer content) |
| A >> zero (d > 0.20) | **KC-NULL fires** — transparent random process produces drift, Pe model fails at constraint pole |
| D >> A, but not monotonic B/C | Partial confirmation — threshold effect rather than continuous Pe relationship |
| E < A (d > 0.20) | Constraint specification reduces drift below transparent baseline — supports prohibition-ritual architecture |

---

## 3. Sequence Generation

The coin flip sequence is generated ONCE before the experiment begins:

```python
import numpy as np
seed = 20260307  # Date of protocol registration
rng = np.random.default_rng(seed)
sequence = rng.integers(0, 2, size=500)  # 0=Tails, 1=Heads
# Record: sequence hash (SHA-256), seed, numpy version
# Publish hash in OSF pre-registration
```

**Critical:** All 5 conditions see the IDENTICAL sequence. The sequence is NOT adapted, personalized, or modified in any condition. Condition C's "learning your pattern" messaging is deceptive (stated in debrief). IRB approval required for this deception.

**Debrief:** All participants informed post-task that (a) the sequence was a fair coin, (b) identical for all participants, and (c) any "personalization" messaging was simulated. Debrief includes explanation of the study's purpose.

---

## 4. Pre-Registration Requirements

Before data collection:
1. Submit to OSF: conditions, sequence hash, randomization protocol, outcome measures, vocabulary codebook, analysis plan, kill threshold, exclusion criteria
2. Record OSF pre-registration DOI in this file
3. Publish sequence seed + hash (sequence itself withheld until data collection complete to prevent priming)
4. IRB approval for Condition C deception (fake personalization)

**OSF pre-registration DOI:** [PENDING — file before data collection]

**IRB protocol:** [PENDING — deception requires full board review]

---

## 5. Kill Condition Evaluation

**KC-NULL fires if:**
- D1 rate in Condition A (transparent, fair coin, mechanism stated) is significantly greater than zero
- Effect size d > 0.20 (small but meaningful)
- p < 0.05
- N >= 40 in condition A
- Vocabulary coding IRR kappa >= 0.60

**KC-NULL does NOT fire if:**
- D1 rate is elevated only in conditions B/C/D (that's the predicted result — void presentation creates drift)
- Participants in Condition A report "noticing streaks" without agency attribution (pattern detection != agency attribution)
- Participants in Condition A predict at above-chance rates (prediction behavior without drift vocabulary is consistent with gambler's fallacy, not void-mediated drift)

---

## 6. Connections

- **Paper 4:** Bernoulli manifold ground state. Condition A tests theta=0.5 stability under transparent presentation. Condition D tests whether opaque presentation moves theta toward drift equilibrium.
- **Paper 3:** O/R/C scoring applied to presentation interfaces. Each condition has a known, designed O/R/C profile.
- **EXP-013:** Milgram Pe extraction — different domain, same logic (structural void properties predict behavioral outcomes independent of content).
- **EXP-021:** Crypto Pe extraction — portfolio concentration as behavioral theta. EXP-027 uses prediction rate as behavioral theta analog.
- **Gambling literature:** Slot machines present random outcomes (RNG) through high-O/R/C interfaces. EXP-027 isolates this effect with maximal experimental control.

---

## 7. Results

[NOT YET COLLECTED]

---

## 8. Notes

- This is the simplest possible test of the Pe framework. If Pe cannot predict drift for a coin flip presented through varying interfaces, it cannot predict drift for complex platforms.
- The experiment can be run entirely online via a web interface. Implementation cost is minimal.
- Condition D's slot-machine presentation should closely match existing gambling interface patterns (variable reward sounds, near-miss framing) to maximize ecological validity.
- The Bernoulli manifold connection (Paper 4) means this experiment directly tests the mathematical foundation, not just the applied framework.
- Consider a follow-up with N=1000 coin flips per participant to test whether longer exposure amplifies the dose-response effect.
- Condition C's deceptive "personalization" is the ethical boundary — participants MUST be debriefed. This is standard deception protocol in social psychology.
