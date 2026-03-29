# THRML-EVO-03 — Kin Selection / Cooper Pair

**Verdict: PASS**  
**Date: 2026-02-26**  
**Version: v2 (asymmetric domains)**

## Setup
- Agent A: drift domain (c_A = 0.08, Pe ≈ 30, θ*_A ≈ 0.69)
- Agent B: constraint domain (c_B = 0.30, Pe ≈ 6)
- Cross-coupling pulls A's θ DOWN

## Key Findings

| J_cross mult | θ_A single | θ_A coupled | Δθ_A | VP reduction |
|-------------|-----------|-------------|------|--------------|
| 0.5× | 0.5978 | 0.5512 | +0.047 | +0.025 |
| 1.0× | 0.5978 | 0.5509 | +0.047 | +0.025 |
| 30.0× | 0.5978 | 0.5334 | +0.064 | +0.060 |
| 50.0× | 0.5978 | 0.5219 | +0.076 | +0.077 |

Hamilton's rule satisfied at **all tested J_cross values** (including minimum 0.5× baseline).

## Game Calibration
- **Cooper Pair eligibility**: any complementary archetype pairing (asymmetric domain exposure)
- **VP exposure reduction**: 2.5% at baseline coupling → 7.7% at maximum coupling
- **Design note**: threshold at J_cross_base × 0.5 — all pairs with complementary archetypes qualify
