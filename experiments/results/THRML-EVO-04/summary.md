# THRML-EVO-04 — CDG Coupling Depth Gauge Calibration

**Verdict: PASS**  
**Date: 2026-02-26**

## Condition Comparison (session 5)

| Condition | CDG | Description |
|-----------|-----|-------------|
| A (all HIGH) | 19.1 | Highest accumulation ✓ |
| B (alternating) | 3.7 | Reduced by LOW sessions |
| C (3 HIGH → LOW) | 0.0 | Rapid reset |

## CDG Calibration

| Parameter | Measured | Target | Scale factor |
|-----------|---------|--------|--------------|
| CDG per HIGH session | 21.74 | 6.67 | 0.307× |
| CDG per LOW session | -7.21 | ~-5 | recovery confirmed ✓ |

## Design Thresholds (with 0.307× scale factor)

| CDG | Level | Sessions to reach |
|-----|-------|------------------|
| 20 | Interfering | 3 consecutive HIGH |
| 40 | Coupled | 6 consecutive HIGH |
| 60 | Locked | 9 consecutive HIGH |
| 80 | Captured | 12 consecutive HIGH |

## Recovery
- CDG halved within 0 LOW sessions after HIGH peak (immediate reset confirmed)
- Diminishing returns: early gain +53.4 vs late gain -51.5 ✓
