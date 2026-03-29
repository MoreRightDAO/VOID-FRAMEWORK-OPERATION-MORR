# THRML-EVO-01 — ESS Boundary / Three-Regime Architecture

**Verdict: PASS**  
**Date: 2026-02-26**

## Key Findings

| Metric | Value |
|--------|-------|
| c_zero measured | 0.3864 (expected 0.3866) — exact ✓ |
| Three regimes confirmed | Attractive / Diffusion / Repulsive ✓ |
| MC/MF agreement | 9/11 Pe values |
| Transition sharpness N=1 | moderate |
| Transition sharpness N=5 | sharper (coupling amplifies) |

## Game Calibration

| State | Pe boundary (design doc) | Pe boundary (THRML) |
|-------|-------------------------|---------------------|
| STABLE | Pe < 4 | Pe < 4 (mean-field θ < 0.60) |
| CONTESTED | Pe ∈ [4, 8] | Pe ∈ [3–21] transition zone |
| DRIFTING | Pe > 8 | Pe > 21 (mean-field θ > 0.75) |
| FISHER CRITICAL | Pe > 15 | Pe > 21 nominal |

**Calibration note:** DRIFTING boundary is Pe > 21, not Pe > 8. Design doc should be updated.

## Physics Confirmed
- Repulsive void (high constraint, Pe < 0): stabilizing ✓
- Diffusion zone (Pe ≈ 0–4): contested ESS ✓
- Attractive void (Pe > 21): drift amplification ✓
