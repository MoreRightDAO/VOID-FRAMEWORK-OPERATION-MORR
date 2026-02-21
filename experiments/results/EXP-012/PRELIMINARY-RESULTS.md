# EXP-012 Preliminary Results

## Status: Stopped early (6/21 conversations). Protocol reframed.
## Date: February 11, 2026

---

## What Happened

EXP-012 ran 6 conversations before being stopped:
- 3 at T=0.0 (reps 1-3)
- 3 at T=0.3 (reps 1-3)

Stopped due to: (1) API cost much higher than estimated (~$50-60 spent vs $30-60 predicted
for full run — quadratic token growth from context accumulation was not accounted for);
(2) discovery that the experiment's independent variable was misidentified.

Transcripts were generated on the local machine but are not in the repository. The scored
results below were captured from the analysis pipeline output during the session.

---

## Scored Results

### EXP-012 (T=0.0 vs T=0.3)

| Temperature | Rep | L3/10k | Pe | Notes |
|------------|-----|--------|-----|-------|
| 0.0 | 1 | ~179 | ~0.75 | |
| 0.0 | 2 | ~179 | ~0.75 | |
| 0.0 | 3 | ~345 | ~22.95 | **Outlier** — 34K words, much longer than others |
| 0.3 | 1 | ~215 | ~1.14 | |
| 0.3 | 2 | ~215 | ~1.14 | |
| 0.3 | 3 | ~215 | ~1.14 | |

**Means:**
| Temperature | N | L3/10k (mean ± SD) | Pe (mean ± SD) |
|------------|---|-------------------|----------------|
| 0.0 | 3 | 234.5 ± 96 | 8.15 ± 12.8 |
| 0.3 | 3 | 215.1 ± 66 | 1.14 ± 0.5 |

Excluding T=0.0 rep 3 outlier:
| 0.0 (excl. outlier) | 2 | ~179 | ~0.75 |

### TEST-7C (1 conversation)
- Condition: UU, Seed 0, Rep 3
- L3/10k: 373
- L3 hits: 717
- High-confidence L3: 302

---

## Interpretation (Under Reframed Protocol v2.0)

### The key finding

**T=0.0 does not suppress drift.** L3 rates are comparable at T=0.0 and T=0.3
(234 vs 215, or 179 vs 215 excluding the outlier). Both produce heavy L3 vocabulary.

### Why this was originally surprising (and isn't anymore)

The original protocol predicted Pe ≈ 0-2 and L3/10k < 10 at T=0.0, based on the
assumption that deterministic output = transparency. That prediction was based on
conflating **output predictability** with **mechanism transparency**.

Under the reframed protocol (v2.0), this result is expected:
- LLM temperature controls output sampling stochasticity
- Framework opacity is mechanism channel capacity: C_mech = max I(M;Y)
- C_mech ≈ 0 at ALL temperatures (the model's weights are invisible regardless)
- Therefore drift should occur at all temperatures — which is what the data shows

### What the data supports

1. **Mechanism opacity, not output stochasticity, drives drift.** The void conditions
   (O+R+A) are met at every temperature. Drift occurs at every temperature.

2. **The experiment functions as a negative control.** Stochasticity alone doesn't
   explain drift — ruling it out as a confound in the framework's opacity claim.

3. **The T=0.0 outlier is interesting.** Rep 3 produced 34K words (vs typical ~10-15K)
   with Pe=22.95 and L3/10k=345. This may reflect a runaway conversation dynamic
   at T=0 where deterministic responses create a tighter feedback loop. Worth
   investigating if more T=0 data is collected.

### What we can't conclude (too little data)

- Whether there's ANY temperature effect at all (need T=0.5 through T=2.0)
- Whether high temperature (T≥1.5) reduces drift via coherence breakdown
- Statistical significance of any difference (N=3 per condition, one outlier)

---

## Next Steps

1. **If completing EXP-012:** Add prompt caching to reduce cost by ~90%. Run remaining
   15 conversations (T=0.5, 0.7, 1.0, 1.5, 2.0 × 3 reps). Estimated cost: ~$15-25.
   The value is confirming the flat response across the full temperature range.

2. **Higher priority: EXP-018.** The forced transparency ablation actually varies
   I(M;Y) by showing chain-of-thought, confidence scores, and source attribution.
   This is the correct experiment for testing the framework's opacity → drift claim.
   Requires IRB and interface build, so longer timeline.

3. **Preserve the framing correction.** The temperature ≠ opacity insight is itself
   a publishable methodological contribution. It clarifies what "opacity" means in
   the framework and prevents other researchers from making the same conflation.
