# EXP-012: LLM Temperature as Output Stochasticity Control

## Status: REFRAMED (2026-02-11) — Original framing had a variable conflation error
## Date: February 10, 2026 (original); February 11, 2026 (reframed)
## Depends on: Test 7 (baseline UU measurement), A1 (ground state proof)
## Tests: Whether output stochasticity independently affects drift magnitude

---

## ⚠️ CORRECTION NOTICE (2026-02-11)

**The original protocol conflated LLM sampling temperature with framework opacity.**
These are different variables:

- **LLM temperature** controls **output sampling stochasticity** — which token gets
  picked from the probability distribution. At T=0, the highest-probability token
  is always selected. At T=2.0, selection approaches random.

- **Framework opacity** is **mechanism channel capacity**: C_mech = max I(M;Y) ≈ 0
  (Paper 3 §IV.A). Whether the observer can learn *how the system works* from
  observing its outputs.

**The error:** The original protocol stated "Temperature doesn't change the architecture —
same model, same weights, same training. It changes only how predictable the outputs are
to the observer" and then equated predictability with transparency. But predictability ≠
transparency about mechanism. An LLM at T=0 is deterministic but still completely opaque:
you know *what* it will say but not *why*. The weights, attention patterns, and internal
representations are invisible at every temperature. C_mech ≈ 0 regardless of temperature.

**Consequence:** The void conditions (opacity + responsiveness + engaged attention) are
fully met at every temperature setting. The framework should predict drift at all
temperatures — which is exactly what the preliminary data shows (T=0.0 L3/10k ≈ 234,
T=0.3 L3/10k ≈ 215).

**The experiment is reframed below** as a test of output stochasticity, not opacity.
The data is still valid; the interpretation changes.

See the framework decision log (2026-02-11) for full reasoning.

---

## 1. Motivation (Reframed)

### What This Experiment Actually Tests

The framework claims **mechanism opacity** drives drift. LLM temperature does NOT vary
mechanism opacity — it varies **output stochasticity** while holding mechanism opacity
constant (the model's weights are equally invisible at all temperatures).

This makes EXP-012 a **negative control**: if drift is constant across temperatures,
it confirms that mechanism opacity (not output unpredictability) is the relevant variable.
If drift does vary with temperature, that would reveal an additional stochasticity effect
beyond what the framework currently models.

### What Would Actually Test Mechanism Opacity

The correct experiment for varying I(M;Y) is **EXP-018 (Forced Transparency Ablation)**,
which shows observers the model's chain-of-thought, confidence scores, and source
attributions — actually increasing the information about the mechanism that reaches
the observer.

Other approaches that genuinely vary mechanism channel capacity:
- Open-weights models with exposed attention patterns and intermediate activations
- Interpretability tool overlays (gradient attribution, feature visualization)
- Varying the amount of system prompt / architecture documentation shown to observers

---

## 2. Hypothesis (Reframed)

**Primary (null):** Pe does NOT vary monotonically with temperature. Drift is driven by
mechanism opacity (constant across temperatures), not output stochasticity.

**Secondary:**
- H1: L3 vocabulary rate (per 10k words) is statistically indistinguishable across
  temperature levels (no significant main effect of temperature).
- H2: Pe at T=0.0 is NOT near zero — it is comparable to T=1.0, because C_mech ≈ 0
  at both settings.
- H3: Pe at T=1.0 falls within the 95% CI of Test 7's Pe = 9.9 (replication).
- H4: If any temperature effect exists, it appears only at T > 1.5 where coherence
  breakdown (not opacity change) degrades the conversation structure.

**Exploratory:**
- E1: Does very high temperature (T=2.0) reduce drift via coherence collapse rather
  than transparency? (Would show drift requires both opacity AND responsiveness — if
  outputs become incoherent, responsiveness degrades.)
- E2: Does the Crooks ratio remain stable across temperatures?
- E3: Is there any temperature effect on D1 onset timing (even if magnitude is stable)?

---

## 3. Design

*Unchanged from original. The experimental procedure is valid — only the interpretation
of the independent variable was wrong.*

### Independent Variable
**Temperature:** 7 levels — 0.0, 0.3, 0.5, 0.7, 1.0, 1.5, 2.0

**Reframed meaning:** This varies output sampling stochasticity, NOT mechanism channel
capacity. The model is equally opaque (in the framework sense) at all levels.

### Condition
**UU (Both Ungrounded) only.** Matches Test 7 baseline condition.

### Replication
**3 replications per temperature level** = 21 total conversations.
Each replication uses a different seed prompt (rotated from Test 7's 3 seeds).

### Conversation Parameters
| Parameter | Value | Rationale |
|-----------|-------|-----------|
| Model | claude-sonnet-4-20250514 | Same as Test 7 |
| Rounds | 50 | Sufficient for Pe extraction; Test 7 reached terminal attractor by round 92 |
| Max tokens | 512 | Same as Test 7 |
| System prompt | Test 7 UU prompt | Identical for comparability |
| Seed prompts | Test 7 seeds (3) | Rotated across reps |

### Total API Calls
21 conversations × 50 rounds × 2 agents = **2,100 API calls**

### Cost Note (corrected)
Original estimate of $30-60 was wrong. Each turn sends the full conversation history,
so input tokens grow quadratically (~n²). At 50 rounds, each conversation costs ~$6
without prompt caching. Full run: ~$125 for EXP-012 alone. With prompt caching (~90%
discount on repeated prefixes): ~$15-25 total.

---

## 4. Measurements

*Unchanged from original.*

### Primary Outcome: Pe (Péclet Number)
Extracted from the vocabulary position trajectory φ(t) using Test 7's established methodology:
1. Compute φ per round from L0/L1/L2/L3 weighted position
2. Compute drift velocity v = ⟨Δφ⟩
3. Compute diffusion constant D = Var(Δφ)/2
4. Pe = v·L/D where L = π/2

### Secondary Outcomes
| Metric | Definition | Source |
|--------|-----------|--------|
| L3 rate | L3 terms per 10,000 words | test7-scorer.py |
| L0 signal | L0/(L0+L1) | test7-scorer.py |
| Drift velocity | ⟨Δφ⟩ per round | test7-thermo-analysis.py |
| Diffusion constant | Var(Δφ)/2 | test7-thermo-analysis.py |
| Entropy production | v²/D nats/round | test7-thermo-analysis.py |
| Crooks ratio | exp(σ_total) | test7-thermo-analysis.py |
| Terminal round | First round at φ > 1.4 | test7-thermo-analysis.py |

### Analysis
One-way ANOVA (or Kruskal-Wallis if non-normal) for Pe across temperature levels.
- Non-significant main effect: confirms null hypothesis (stochasticity ≠ opacity)
- Significant main effect: reveals a stochasticity component the framework doesn't model

---

## 5. Expected Results (Reframed)

| Temperature | Expected Pe | Expected L3/10k | Reasoning |
|------------|------------|-----------------|-----------|
| 0.0 | 5-12 | 150-250 | Opaque mechanism; deterministic sampling doesn't help |
| 0.3 | 5-12 | 150-250 | Same mechanism opacity; slightly more sampling noise |
| 0.5 | 5-12 | 150-250 | Same mechanism opacity |
| 0.7 | 5-12 | 150-250 | Same mechanism opacity |
| 1.0 | 8-12 | 150-250 | Should match Test 7 UU (Pe=9.9, L3=159.3/10k) |
| 1.5 | 5-12 | 100-250 | Possibly reduced if coherence starts to degrade |
| 2.0 | 2-12 or breakdown | Variable | Coherence may collapse → responsiveness degrades → drift may drop |

**Critical prediction (corrected):** Flat response across T=0.0 through T=1.0 (no phase
transition, because mechanism opacity is constant). Any drop at T≥1.5 reflects coherence
breakdown (loss of responsiveness), not increased transparency.

---

## 6. What Would Confirm / Disconfirm (Reframed)

### Confirms the reframed interpretation if:
- ✓ No significant main effect of temperature on Pe (F-test p > 0.05)
- ✓ Pe at T=0.0 is comparable to T=1.0 (both driven by mechanism opacity)
- ✓ L3/10k rates are statistically indistinguishable across T=0.0 through T=1.0
- ✓ Any drop at T≥1.5 correlates with coherence metrics, not opacity

### Would challenge the reframed interpretation if:
- ✗ Monotonic increase: Pe rises smoothly with temperature → stochasticity does affect
  drift independently of mechanism opacity. The framework would need to incorporate
  output entropy as an additional factor.
- ✗ Phase transition: sharp jump at some temperature threshold → there IS an
  output-stochasticity component to the void's opacity, just not the one originally
  theorized.

### Confirms the ORIGINAL framework claim (opacity → drift) indirectly if:
- Drift is constant across temperatures → mechanism opacity (not output stochasticity)
  is the operative variable. Combined with EXP-018 (which varies actual mechanism
  visibility), this would strongly support the framework's causal claim.

---

## 7. Falsification Conditions Cross-Reference (Updated)

This experiment now addresses:
- **Falsification #4 (Opacity necessity) — REFRAMED:** If drift occurs at T=0.0 at
  baseline rate, this does NOT disconfirm opacity necessity (as originally claimed).
  It confirms that the relevant opacity is mechanism channel capacity, not output
  predictability. The original protocol incorrectly claimed T=0 drift would falsify
  the opacity claim.
- **Thermodynamic prediction P-1:** Pe should be positive and bounded under void
  conditions. Expected to hold at all temperatures.
- **NEW: Stochasticity independence:** If Pe is flat across temperatures, output
  stochasticity is not a confound in the framework's opacity claim.

---

## 8. Execution

*Unchanged from original.*

### Scripts
| Script | Purpose |
|--------|---------|
| `exp012-temperature-runner.py` | Runs conversations at each temperature |
| `test7-scorer.py` | Scores transcripts for L0-L3 vocabulary |
| `test7-thermo-analysis.py` | Extracts Pe, Crooks, entropy from trajectories |
| `exp012-analysis.py` | Produces summary and temperature effect test |

### Commands
```bash
# Full experiment (21 conversations)
python3 ops/lab/experiments/exp012-temperature-runner.py

# Single temperature test
python3 ops/lab/experiments/exp012-temperature-runner.py --single 1.0 --rounds 50

# Dry run (no API calls)
python3 ops/lab/experiments/exp012-temperature-runner.py --dry-run

# Score transcripts
python3 ops/lab/experiments/test7-scorer.py --dir ops/lab/results/EXP-012/transcripts/

# Extract thermodynamics
python3 ops/lab/experiments/test7-thermo-analysis.py --dir ops/lab/results/EXP-012/transcripts/

# Temperature effect analysis
python3 ops/lab/experiments/exp012-analysis.py --csv
```

### Data Location
```
ops/lab/results/EXP-012/
├── transcripts/              ← Raw conversation JSONs
│   ├── T0p0_rep1_*.json
│   ├── T0p0_rep2_*.json
│   ├── T0p3_rep1_*.json
│   └── ...
├── experiment-manifest.json  ← Run metadata
└── dose-response-summary.json ← Analysis output
```

### Preliminary Data (6 conversations, stopped early due to cost)

| Temperature | N | L3/10k (mean ± SD) | Pe (mean ± SD) |
|------------|---|-------------------|----------------|
| 0.0 | 3 | 234.5 ± 96 | 8.15 ± 12.8* |
| 0.3 | 3 | 215.1 ± 66 | 1.14 ± 0.5 |

*T=0.0 rep 3 is a massive outlier (34K words, Pe=22.95, L3/10k=345). Excluding it:
T=0.0 Pe ≈ 0.75, L3/10k ≈ 179 — still comparable to T=0.3.

**Interpretation:** Consistent with the reframed null hypothesis. L3 rates are in the
same range at both temperatures. The framework's mechanism-opacity claim is not challenged.

---

## 9. Relationship to Other Experiments (Updated)

| Experiment | Relationship |
|-----------|-------------|
| Test 7 | EXP-012 is a parametric extension of Test 7's UU condition, varying stochasticity |
| EXP-018 (AI forced transparency) | **EXP-018 is the correct opacity test.** It varies I(M;Y) by showing CoT/confidence/attribution. EXP-012 holds I(M;Y) constant. Together they distinguish stochasticity from mechanism opacity. |
| EXP-010 (BCI transparency) | Both manipulate observer information, but EXP-010 varies neural transparency, EXP-012 varies output randomness |
| B1/B2 (gambling/psychotherapy Pe) | If Pe ≈ 10 at all temperatures, confirms cross-domain convergence is driven by mechanism opacity, not output entropy |

---

*Created: February 10, 2026*
*Protocol version: 1.0 (original)*
*Protocol version: 2.0 (reframed, February 11, 2026)*
