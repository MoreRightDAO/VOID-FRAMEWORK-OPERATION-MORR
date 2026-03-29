# THRML-SC-01 — Crooks Ratio by Domain State

**Verdict: PASS**  
**Date: 2026-02-26**

## Crooks Reference Table (R = exp(Pe × 0.05082))

| State | Pe | Crooks | Interpretation |
|-------|-----|--------|----------------|
| ANCIENT/STABLE | 0.5 | 1.03 | Near-reversible |
| STABLE | 1.5 | 1.08 | Weakly irreversible |
| CONTESTED (Pe*) | 4.0 | 1.23 | ESS balance point |
| DRIFTING | 8.0 | 1.50 | Moderately irreversible |
| FISHER CRITICAL | 15.0 | 2.14 | Strongly irreversible |
| RUNAWAY | 25.0 | 3.56 | Near-irreversible limit |

## Phase Riding Window
Pe ∈ [3.5, 5.0] → Crooks ∈ [1.19, 1.29]
Near-unity = forward/reverse equally probable = phase transition sweet spot

## Game Calibration
- **Reversibility Gate loot tiers**: based on Crooks run score
  - Bronze (<1.5): standard loot
  - Silver (1.5–2.5): rare loot
  - Gold (>2.5): legendary loot (Fisher Critical domain required)
