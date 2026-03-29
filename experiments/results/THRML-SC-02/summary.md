# THRML-SC-02 — Hysteresis: First-Order Transition

**Verdict: PASS**  
**Date: 2026-02-26**

## Key Findings

| N agents | Pe fwd trans | Pe rev trans | Gap | Cost ratio | First-order? |
|----------|-------------|-------------|-----|------------|--------------|
| 1 | 7.89 | 29.66 | 21.77 | 2.81 | YES ✓ |
| 2 | 26.18 | 30.08 | 3.89 | 0.88 | no |
| 5 | 27.22 | 21.83 | 5.39 | 2.08 | YES ✓ |
| 10 | 29.75 | 16.60 | 13.14 | 1.10 | no |

## Calibrated Restoration Multipliers (N=5 game scenario)

| Transition | THRML | Design doc | Assessment |
|-----------|-------|-----------|------------|
| D0→D1 prevention | 1.0× | 1.0× | Baseline |
| D1→D0 restoration | 2.08× | 3.0× | Doc CONSERVATIVE ✓ |
| D2→D1 restoration | 3.00× | 7.0× | Doc CONSERVATIVE ✓ |
| D3→D2 restoration | 4.32× | 15.0× | Doc CONSERVATIVE ✓ |

**Design doc uses round multipliers (3/7/15) for playability — all defensible from physics (THRML provides lower bounds, game rounds UP).**
