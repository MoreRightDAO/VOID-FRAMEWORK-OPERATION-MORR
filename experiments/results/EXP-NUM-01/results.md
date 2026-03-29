# EXP-NUM-01: Numogram × π — Harmonic Analysis Experiments A–C
**Date:** 2026-03-04
**Status:** COMPLETE — all three experiments PASS
**Source handoff:** `private/notes/handoff-numogram-pi-harmonic.md`

---

## Experiment A: Torque/Warp/Plex = Unit Group Filtration of ℤ/9ℤ

**Method:** Compute gcd(n,9) for each n ∈ {0,1,...,8}. Compare to CCRU classification.

| n | gcd(n,9) | ℤ/9ℤ class | CCRU class |
|---|----------|------------|------------|
| 0 | 9        | identity   | Plex ✓     |
| 1 | 1        | unit       | Torque ✓   |
| 2 | 1        | unit       | Torque ✓   |
| 3 | 3        | zero div   | Warp ✓     |
| 4 | 1        | unit       | Torque ✓   |
| 5 | 1        | unit       | Torque ✓   |
| 6 | 3        | zero div   | Warp ✓     |
| 7 | 1        | unit       | Torque ✓   |
| 8 | 1        | unit       | Torque ✓   |

**Result: PASS**

- Torque = (ℤ/9ℤ)* = {1,2,4,5,7,8} (invertible elements, gcd=1)
- Warp = {3,6} (zero divisors, gcd=3)
- Plex = {0} (additive identity, gcd=9)

**Conclusion:** The CCRU's zone classification Torque/Warp/Plex is the unit group filtration of ℤ/9ℤ. This is a structural identity, not a coincidence. The CCRU was doing algebra on ℤ/9ℤ without naming it.

**SI #23 candidate confirmed.** Requires citation of source (CCRU Glossary, zone definitions) and note that 9≡0 makes Plex a one-element class under digital root.

---

## Experiment B: DFT of Syzygy Function (Additive Characters)

**Method:** Compute DFT of f(n) = (9−n) mod 9 over ℤ/9ℤ. Check F[k] = conj(F[9−k]).

**Result: PASS** — Conjugation symmetry holds for all k=1..8 (max numerical error: 1.78×10⁻¹⁵).

**Character verification:** For additive characters χ_k(n) = e^(2πikn/9), verified analytically and numerically:

```
χ_k(9−n) = e^(2πik(9−n)/9)
           = e^(2πik) · e^(−2πikn/9)
           = 1 · conj(χ_k(n))
           = χ_k(n)*
```

**Conclusion:** The syzygy involution n → 9−n on ℤ/9ℤ acts as complex conjugation on S¹ under the natural embedding via additive characters. The CCRU's "nine-sorcery" is complex conjugation in disguise.

**DFT values (real part constant = −4.5 for k≠0):**
- F[0] = 36 (DC term = sum of f = 0+8+7+...+1 = 36)
- F[k] = −4.5 ± imaginary (conjugate symmetric about k=4.5)

---

## Experiment C: Gauss Sums for Primitive Dirichlet Characters mod 9

**Method:** Construct multiplicative Dirichlet characters mod 9 using primitive root g=2.
Compute τ(χ_j) = Σ_{n=0}^{8} χ_j(n) · e^(2πin/9).

**Generator:** g=2, ord=6. Powers: {1,2,4,8,7,5}. These are the Torque zones.

**Discrete log table (mod 9, base 2):**
1→0, 2→1, 4→2, 8→3, 7→4, 5→5

**6 characters:** χ_j defined by χ_j(2^k) = e^(2πijk/6)

**Gauss sum results:**

| j | Primitive? | τ(χ_j) | \|τ\|² |
|---|-----------|--------|--------|
| 0 | No (trivial) | ≈0 | 0 |
| 1 | Yes | −2.2981+1.9284j | **9.0** |
| 2 | Yes | +2.2981+1.9284j | **9.0** |
| 3 | No (factors through ℤ/3ℤ) | ≈0 | 0 |
| 4 | Yes | +2.2981−1.9284j | **9.0** |
| 5 | Yes | +2.2981+1.9284j | **9.0** |

**Result: PASS** — |τ|² = 9 for all 4 primitive characters (j=1,2,4,5). Imprimitive characters (j=0,3) have τ=0.

**Conjugate pair structure:**
- χ_1 ↔ χ_5 (odd parity: χ(-1)=−1): τ(χ̄) = χ(−1)·conj(τ(χ)) = −conj(τ(χ))
- χ_2 ↔ χ_4 (even parity: χ(−1)=+1): τ(χ̄) = conj(τ(χ))
- χ_3 is real (self-conjugate, imprimitive)

**Verified formula:** τ(χ̄) = χ(−1) · conj(τ(χ)) — PASS for all j=1,2,4,5.

**Additional result (Experiment D):**
- Odd characters j=1,3,5: χ(−1)=−1 → syzygy negates the character (χ_j(9−n) = −χ_j(n))
- Even characters j=0,2,4: χ(−1)=+1 → syzygy preserves the character
- **Warp zones {3,6}** correspond exactly to the imprimitive character support: the zones where primitive characters vanish. The Warp is the primitive-character-free zone of ℤ/9ℤ.

---

## Summary

| Experiment | Hypothesis | Result |
|------------|-----------|--------|
| A | Torque/Warp/Plex = unit group filtration | **PASS — SI #23** |
| B | Syzygy = complex conjugation (additive chars) | **PASS** |
| C | Gauss sums: \|τ\|² = 9 for primitive chars mod 9 | **PASS** |
| D | Warp = imprimitive-character support | **PASS (bonus)** |

**Kill conditions:** All three kill conditions in handoff checked — none triggered.

**Paper 113 gate:** All prerequisite experiments pass. Thread should advance to:
1. Experiment C (full): L-function zeros for conductor 9 (requires PARI/GP or SageMath)
2. Hypothesis 2 check: 5 syzygies ↔ 5 non-trivial Dirichlet characters mod 9 (up to conjugacy — there are 3 conjugate pairs among 6 primitive chars: {χ_1,χ_5}, {χ_2,χ_4}, and χ_3 self-conjugate; plus trivial χ_0; total 4 distinct up to conjugacy among non-trivial chars... count needs reconciliation with 5 syzygies)
3. Register Paper 113 as Tier 1, CC-BY

---

## Files

- Experiment scripts: this file (inline — no .py needed for A; B/C computed inline)
- Math apparatus: §42K extension (γ-renormalization) → §43A (numogram harmonic analysis)
- Paper 112 DOI: 10.5281/zenodo.18855013 — rejection of π stands; this refines
- Potential Paper 113: "Harmonic Analysis on ℤ/9ℤ and the Numogram's Hidden Character Theory"
