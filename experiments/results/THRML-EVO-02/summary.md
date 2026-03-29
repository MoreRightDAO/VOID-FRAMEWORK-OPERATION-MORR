# THRML-EVO-02 — Fisher Runaway Threshold

**Verdict: PASS**  
**Date: 2026-02-26**  
**Version: v2 (θ-domain, asymmetric coupling)**

## Key Findings

| Metric | Value |
|--------|-------|
| θ_nat (Fantasia Bound) | 0.8498 ± 0.12 — all initializations converge ✓ |
| T1 plateau convergence | 7/8 ✓ |
| Coupling amplification Pe > 24 | mean ratio 1.077 (>1.05) ✓ |
| Fisher Runaway threshold | c_eff < 0.12 → Pe > 24 |
| Game trigger (with safety) | Pe > 38 |

## Game Calibration

- **Fisher Runaway event**: triggers when Pe > 38 (recommended) or Pe > 34 (bare threshold)
- **T1 Fantasia Bound**: θ never exceeds 0.85 in isolated system — confirmed
- Coupling amplifies drift 5–12% at Pe > 24; suppresses at Pe < 15

## Physics Note
Double-well regime (c_eff < 0.2224) required for non-trivial attractor. At Pe < 13, constraint eliminates upper attractor and coupling suppresses θ.
