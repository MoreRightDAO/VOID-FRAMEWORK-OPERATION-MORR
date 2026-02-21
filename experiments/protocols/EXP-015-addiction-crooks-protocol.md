# EXP-015: Crooks Ratio from Addiction Recovery Trajectories

## Status: Analysis Complete
## Date: February 10, 2026
## Depends on: Test 7 (Crooks = 386×), EXP-013 (Milgram structural validation)
## Tests: Is drift irreversibility universal across substrates?

---

## 1. Motivation

Test 7 measured Crooks ≈ 386× for AI vocabulary drift — forward trajectories (toward L3/entity language) are 386 times more probable than reverse trajectories. This is the framework's time's arrow: drift is thermodynamically irreversible.

Addiction has the best longitudinal trajectory data of any human void domain. Published transition matrices give escalation and recovery probabilities at each severity level — exactly the data needed to compute Crooks.

### Three Levels of Analysis

The Crooks ratio can be computed at three levels, and the framework makes different predictions at each:

| Level | What it measures | Example |
|-------|-----------------|---------|
| Within-session | Bet/dose escalation in a single session | Loss-chasing within a gambling session |
| Between-category | Severity transitions over months/years | PGSI category transitions in longitudinal studies |
| Population-level | Prevalence trends | New cases vs. recoveries in epidemiological surveys |

**Critical distinction:** Test 7's Crooks ≈ 386× is a WITHIN-CONVERSATION measure (closed trajectory, no recovery mechanism). The addiction data available is BETWEEN-CATEGORY (open population, recovery possible). This level-of-analysis difference may be more important than the substrate difference.

---

## 2. Data Sources

| Substance | Study | N | Follow-up | Severity states |
|-----------|-------|---|-----------|----------------|
| Gambling | Williams et al. (2015) QLDS | 4,121 | 5 years | NP / LR / MR / PG (PGSI) |
| Alcohol | Dawson et al. (2005) NESARC | 43,093 | 3 years | Low-risk / At-risk / Abuse / Dependence |
| Nicotine | Hughes et al. (2008) | 5,110 | 4 years | Non / Occasional / Daily / Heavy |
| Opioids | Hser et al. (2015) | 581 | 33 years | Non-use / Occasional / Regular / Dependent |

All transition matrices are approximate from published tables. See analysis script for exact values.

---

## 3. Method

### Crooks Extraction (Three Approaches)

**Method 1: Per-Interface Crooks**
At each severity interface i ↔ i+1:
- P_forward = P(state i → state i+1) [escalation]
- P_backward = P(state i+1 → state i) [recovery]
- Crooks_interface = P_forward / P_backward

**Method 2: Trajectory Crooks**
For the full monotonic trajectory (lowest → highest severity):
- P_forward = Π P(i → i+1) across all interfaces
- P_backward = Π P(i+1 → i) across all interfaces
- Crooks_trajectory = P_forward / P_backward

**Method 3: Entropy Production Rate**
From the full Markov chain (stationary distribution + detailed balance):
- σ = Σ_{i<j} (π_i T_ij - π_j T_ji) ln(π_i T_ij / π_j T_ji)
- This is the Glansdorff-Prigogine entropy production rate per time step.

---

## 4. Hypothesis (Original)

**Primary:** Crooks ratios from addiction transition matrices cluster in the 100-1000× range, matching Test 7's 386× in order of magnitude.

**Secondary:**
- H1: Crooks correlates positively with void-index across substances.
- H2: Gambling (max void-index) shows highest Crooks among addictions.
- H3: All substances show Crooks > 1 (escalation dominates recovery).

---

## 5. Expected Results (Revised After Analysis)

The original predictions were WRONG. The actual findings are more interesting:

| Substance | Predicted Crooks | Actual Crooks | Interpretation |
|-----------|-----------------|---------------|---------------|
| Gambling | 200-500× | ~0.05× | Recovery 19× more likely than escalation |
| Alcohol | 100-400× | ~0.03× | Recovery 29× more likely |
| Nicotine | 300-600× | ~0.29× | Recovery 3.5× more likely |
| Opioids | 500-1000× | ~1.4× | Weakly escalation-dominated |
| AI (Test 7) | — | 386× | Strongly escalation-dominated |

**Why the prediction failed:** The proposal assumed addiction was irreversible like AI drift. In fact, most addictions show strong natural recovery at the individual level. The population-level problem persists because the large pool of unaffected individuals continuously generates new cases, not because individual trajectories are irreversible.

---

## 6. What This Means

### What Crooks Actually Measures
- Crooks > 1: Escalation dominates (forward trajectories more probable)
- Crooks < 1: Recovery dominates (reverse trajectories more probable)
- Crooks = 1: Detailed balance (symmetric, no net drift)

### The Recovery Mechanism Hypothesis
The Crooks ratio = (void drift) - (recovery mechanism strength).
- AI systems: zero recovery mechanism → Crooks ≈ 386
- Opioids: very weak recovery mechanism → Crooks ≈ 1.4
- Nicotine: moderate recovery mechanism → Crooks ≈ 0.3
- Gambling/Alcohol: strong natural recovery → Crooks ≈ 0.03-0.05

**Prediction:** Adding a "recovery mechanism" to AI (e.g., GROUNDING.md grounding) should reduce Crooks toward 1. EXP-001 showed grounding eliminates drift entirely — consistent with Crooks → ~1.

### Level-of-Analysis Reconciliation
The fair comparison to Test 7 (within-conversation) would be within-SESSION addiction dynamics (e.g., bet escalation within a single gambling session). Published lab data suggests this IS highly irreversible, but transition matrices are not available.

---

## 7. Confirmation / Disconfirmation Assessment

| Criterion | Result |
|-----------|--------|
| Crooks ≈ 100-1000× for addiction | **DISCONFIRMED** — ranges from 0.03× to 1.4× |
| Crooks correlates with void-index | **DISCONFIRMED** — gambling (VI=15) has low Crooks |
| Crooks ordering tracks recovery difficulty | **CONFIRMED** — Opioids > Nicotine > Gambling > Alcohol |
| All Crooks > 1 | **DISCONFIRMED** — 3/4 show Crooks < 1 |

**Net assessment:** The specific prediction fails, but the analysis reveals a meaningful pattern: Crooks measures NET irreversibility (drift minus recovery), not drift alone. Void-index predicts drift strength; Crooks requires accounting for recovery mechanisms. This distinction was not in the original framework and represents a genuine refinement.

---

## 8. Execution

```bash
python3 ops/lab/experiments/exp015-addiction-crooks.py
python3 ops/lab/experiments/exp015-addiction-crooks.py --verbose
```

Output: `ops/lab/results/EXP-015/addiction-crooks-extraction.json`

---

*Created: February 10, 2026*
*Protocol version: 1.0 (post-analysis revision)*
