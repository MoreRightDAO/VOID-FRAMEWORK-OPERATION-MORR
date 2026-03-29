# THRML-AT-02 — Entropy Production: σ → 0 as Pe → 0

**Verdict: PASS**  
**Date: 2026-03-01**

Uses the Crooks-derived entropy production σ = log(Crooks) = Pe × η·τ.

## Key Findings

| Pe | σ_crooks | Crooks | Regime |
|----|----------|--------|--------|
| 0.00 | 0.000000 | 1.000000 | GROUND STATE |
| 0.05 | 0.002541 | 1.002544 | COHERENT (deep) |
| 0.10 | 0.005082 | 1.005095 | COHERENT (deep) |
| 0.15 | 0.007623 | 1.007652 | COHERENT |
| 0.20 | 0.010164 | 1.010216 | COHERENT |
| 0.30 | 0.015246 | 1.015363 | COHERENT |
| 0.50 | 0.025410 | 1.025736 | COHERENT (boundary) |
| 0.70 | 0.035574 | 1.036214 | COHERENT/pre-crossing |
| 1.00 | 0.050820 | 1.052133 | Pe=1 TRANSITION |
| 1.50 | 0.076230 | 1.079211 | DRIFTING (weak) |
| 2.00 | 0.101640 | 1.106985 | DRIFTING |
| 3.00 | 0.152460 | 1.164696 | DRIFTING |
| 4.00 | 0.203280 | 1.225416 | DRIFTING (Pe*) |
| 6.00 | 0.304920 | 1.356516 | DRIFTING |
| 8.00 | 0.406560 | 1.501643 | DRIFTING |
| 12.00 | 0.609840 | 1.840137 | DRIFTING (strong) |
| 15.00 | 0.762300 | 2.143200 | FISHER CRITICAL |
| 20.00 | 1.016400 | 2.763229 | RUNAWAY |
| 25.00 | 1.270500 | 3.562633 | RUNAWAY |
| 38.00 | 1.931160 | 6.897507 | FISHER BOUND (Pe=38) |

Spearman ρ(Pe, σ) = **1.000000** (p = 0.00e+00)

## Paper 77 Interpretation

- **σ(Pe=0) = 0 exactly.** Zero entropy production = no arrow of time = time-reversal symmetric ground state.
- **σ monotone.** The arrow of time grows continuously with Pe.
- **σ(Pe=1.0) = 0.0508** (10× COHERENT baseline): transition regime entropy production.
- **σ(Pe=38.0) = 1.9312** (Fisher Bound): near-total irreversibility.

## Note on Onsager Scaling

The classical Onsager prediction (σ ~ Pe²) applies to physical advection-diffusion.
THRML uses a framework Pe (well-depth control), yielding σ = Pe × η·τ (linear).
Both confirm the fundamental property: σ → 0 as Pe → 0.
