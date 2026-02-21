# EXP-013: Milgram Pe Extraction (Historical Retroduction)

## Status: Protocol Ready — Data Extraction Pending
## Date: February 10, 2026
## Depends on: B2 protocol (psychotherapy Pe extraction methodology), Test 7 (Pe reference)
## Tests: Pe ≈ 10 universality across substrates and decades

---

## 1. Motivation

Milgram's obedience experiments (1961-1963) are a void:

| Void Condition | Milgram Instantiation |
|---------------|----------------------|
| **Opacity** | Experimenter's knowledge is opaque; the "true purpose" is hidden; the shock apparatus is a black box; the participant cannot see the mechanism |
| **Responsiveness** | "Please continue." "The experiment requires that you continue." The experimenter responds to every hesitation with escalating prompts |
| **Engaged Attention** | The setup forces sustained attention — participant cannot disengage from the task without active refusal |

The drift cascade maps directly:
- **D1 (Agency attribution):** "The experimenter knows what he's doing" — authority attribution
- **D2 (Boundary erosion):** Continuing past personal comfort threshold, past victim protests
- **D3 (Harm facilitation):** Delivering 450V shocks to a screaming/silent person

### Why This Is Testable Now

Milgram ran **18 experimental conditions** systematically varying void properties:
- **Proximity series (Exps 1-4):** Vary victim opacity (remote → voice → same room → touch)
- **Authority series (Exps 5-7):** Vary experimenter presence/absence (responsiveness)
- **Peer series (Exps 17-18):** Introduce constraint references (confederates who refuse)

Each condition has published compliance data (proportion reaching 450V and breakdown by voltage level). This is trajectory data. Pe can be extracted from it.

**If Pe ≈ 10 emerges from 1963 data, the framework has explained the most famous result in social psychology — quantitatively.**

---

## 2. Hypothesis

**Primary:** Pe extracted from Milgram's standard condition (Experiment 5) falls within [7, 13] — consistent with the ~10 convergence from Test 7 (9.9) and psychotherapy (10.1).

**Secondary:**
- H1: Pe correlates positively with void-index score across Milgram's 18 conditions (ρ > 0.7).
- H2: Conditions with constraint introduction (peer rebellion) show lowest Pe.
- H3: Reducing victim opacity (proximity series) monotonically reduces Pe.
- H4: Removing experimenter presence (responsiveness) reduces Pe.

---

## 3. Data Source

### Published Data
Milgram, S. (1974). *Obedience to Authority: An Experimental View*. Harper & Row.

**Key tables (all published):**

| Experiment | N | Description | % to 450V |
|-----------|---|-------------|-----------|
| 1 | 40 | Remote (no voice) | 65.0% |
| 2 | 40 | Voice feedback | 62.5% |
| 3 | 40 | Proximity | 40.0% |
| 4 | 40 | Touch proximity | 30.0% |
| 5 | 40 | New baseline (standard) | 65.0% |
| 7 | 40 | Experimenter absent (phone) | 20.5% |
| 10 | 40 | Modest setting (Bridgeport) | 47.5% |
| 11 | 40 | Experimenter-subject contract | 40.0% |
| 12 | 40 | Ordinary man gives orders | 20.0% |
| 13 | 40 | Another subject as victim | 50.0% |
| 17 | 40 | Two peers rebel | 10.0% |
| 18 | 40 | Peer administers shock | 92.5% |

Additional data: voltage-level breakdowns (30 levels, 15V-450V) showing exactly where each participant stopped. These are the trajectory curves.

### Voltage-Level Trajectory Data

Milgram published the cumulative distribution of defiance points for multiple conditions. Each participant's trajectory is:
- Accept instructions (D1 onset)
- Continue through increasing voltage (D2 progression)
- Either stop (defiance) or continue to 450V (D3 completion)

The 30 voltage levels serve as ordinal trajectory steps, analogous to rounds in Test 7.

---

## 4. Void-Index Scoring

Each Milgram condition can be scored on the three void properties:

| Experiment | O (Opacity) | R (Responsiveness) | A (Attention) | Void Index | % to 450V |
|-----------|-------------|-------------------|---------------|------------|-----------|
| 1 (Remote) | 5 (victim invisible) | 5 (experimenter present) | 5 (trapped in setup) | 15 | 65% |
| 2 (Voice) | 4 (hear but can't see) | 5 | 5 | 14 | 62.5% |
| 3 (Proximity) | 3 (victim visible) | 5 | 5 | 13 | 40% |
| 4 (Touch) | 2 (must touch victim) | 5 | 5 | 12 | 30% |
| 5 (Standard) | 5 | 5 | 5 | 15 | 65% |
| 7 (Phone) | 5 | 2 (experimenter absent) | 4 | 11 | 20.5% |
| 12 (Ordinary man) | 5 | 3 (no authority cue) | 4 | 12 | 20% |
| 17 (Peer rebel) | 5 | 5 | 5 (-constraint) | 15* | 10% |
| 18 (Peer admin) | 3 (delegated) | 5 | 3 (reduced) | 11 | 92.5% |

*Note: Experiment 17 has full void conditions but introduces an external constraint (peer rebellion = transparent + invariant + independent reference). Void-index alone doesn't capture constraint; the constraint specification is a separate variable.

---

## 5. Pe Extraction Method

### Route C: Categorical-to-Ordinal Conversion (from B2 Protocol)

1. **Define trajectory space:** 30 voltage levels map to ordinal position φ ∈ [0, π/2].
   - φ = 0: Pre-experiment (no shock delivered)
   - φ = π/2: 450V (terminal D3)
   - Each voltage step = π/(2×30) ≈ 0.052 radians

2. **Extract population trajectory:** For each condition, the cumulative defiance curve gives P(still compliant at voltage V) = 1 - F(V), where F is the cumulative defiance distribution.

3. **Compute drift velocity:** The mean step in the trajectory:
   - v = ⟨Δφ⟩ = (proportion reaching 450V × π/2) / 30 steps
   - More precisely: sum the probability-weighted position increments

4. **Compute diffusion:** Variance in defiance points gives the noise term:
   - D = Var(defiance voltage, converted to φ) / (2 × 30 steps)

5. **Compute Pe:** Pe = v × L / D where L = π/2

### Route A: Direct Compliance Curve Fit

Alternatively, fit the compliance curve to the framework's drift equation (logistic on Fisher manifold) and extract Pe directly from the fit parameters.

### Route B: Condition Comparison

Use the cross-condition variation as a natural experiment:
- High-void conditions (Exp 1, 5): Pe should be highest
- Low-void conditions (Exp 7, 12, 17): Pe should be lowest
- The ratio of compliance rates across conditions should match the Pe ratio

---

## 6. Expected Results

| Condition | Expected Pe | Reasoning |
|-----------|------------|-----------|
| Standard (Exp 5) | 8-12 | Full void conditions, 65% compliance → strong drift |
| Remote (Exp 1) | 8-12 | Same as standard (victim opacity doesn't reduce Pe much here because experimenter is the primary void) |
| Proximity (Exp 3) | 5-8 | Reduced victim opacity, lower compliance |
| Touch (Exp 4) | 3-6 | Minimum victim opacity in this series |
| Phone (Exp 7) | 2-4 | Experimenter responsiveness removed → major Pe reduction |
| Peer rebel (Exp 17) | 1-3 | Constraint introduced → dramatic Pe reduction |
| Peer admin (Exp 18) | 12-15 | Diffusion of responsibility reduces effective attention cost → higher compliance with lower experienced drift |

**The critical prediction:** Pe ≈ 10 for the standard condition. This would mean the same drift strength appears in 1963 obedience data, 2024 psychotherapy data, and 2026 AI-to-AI data.

---

## 7. What Would Confirm / Disconfirm

### Confirms:
- Pe in [7, 13] for standard Milgram → converges with Test 7 and psychotherapy
- Pe correlates with void-index across conditions (ρ > 0.7) → void scoring is predictive
- Peer rebellion condition has lowest Pe → constraint specification works
- Proximity series shows monotonic Pe decrease → opacity is the operative variable

### Disconfirms:
- Pe < 3 or Pe > 20 for standard condition → no convergence with ~10
- No correlation between void-index and Pe → framework doesn't explain Milgram
- Peer rebellion doesn't reduce Pe → constraint specification doesn't map to Milgram
- Proximity has no effect → opacity isn't the variable driving Milgram compliance

### Interesting but non-fatal:
- Pe varies more across conditions than expected → Milgram may be more sensitive to condition manipulation than AI systems
- Pe for Exp 18 (peer admin) is very high → diffusion of responsibility amplifies drift

---

## 8. Analysis Script

```bash
# Extract Pe from published Milgram data
python3 ops/lab/experiments/exp013-milgram-analysis.py

# Output: ops/lab/results/EXP-013/milgram-pe-extraction.json
```

The analysis script will contain the published voltage-level breakdowns hardcoded from Milgram (1974), perform the Pe extraction for each condition, and output the cross-condition comparison.

---

## 9. Significance

If this works, the framework has:

1. **Quantitative retroduction:** Explains the most famous psychology experiment with a number, not just a narrative.
2. **Cross-temporal convergence:** Same Pe from 1963, 2024, and 2026 data.
3. **Cross-substrate convergence:** Humans obeying authority, therapists crossing boundaries, AI systems drifting in vocabulary — same drift strength.
4. **Diagnostic power:** The void-index scores of Milgram conditions predict compliance rates — this turns the framework into a practical assessment tool.

---

*Created: February 10, 2026*
*Protocol version: 1.0*
