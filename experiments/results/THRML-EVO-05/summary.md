# THRML-EVO-05 — Rarity Selection / Founder Effect Calibration

**Verdict: PASS**  
**Date: 2026-02-26**

## Key Finding: Per-Scorer Impact Scales Inversely with N

| N scorers | Per-scorer impact | Relative to N=20 |
|-----------|-----------------|-----------------|
| 2 (RARE) | 9.36 | 9.94× |
| 5 | 3.76 | 4.00× |
| 10 | 1.88 | 2.00× |
| 20 (COMMON) | 0.94 | 1.00× (baseline) |
| 50 | 0.38 | 0.40× |

**Impact scales as 1/N (exact inverse proportionality confirmed).**

## Founder Effect Multiplier Validation

- THRML measured impact ratio RARE/COMMON: **9.94×**
- Design doc uses **5× MORR** for Founder Effect epoch (N < 3)
- **5× is CONSERVATIVE** relative to physics (actual 9.94×)
- Multiplier is DEFENSIBLE — intentionally set below physics to prevent gaming

## Variance Finding
RARE (N=2) Pe variance = 37.4 vs COMMON (N=20) = 39.9. RARE has LOWER variance
because high per-scorer impact drives domain to equilibrium faster (shorter transient).
This is correct physics — rare scorers are more impactful, not noisier.
