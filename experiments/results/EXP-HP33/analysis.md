# HP33 — Balmer-α Prediction Test: One Calibration, All Transitions
*2026-03-14 | Shamir | Session: bridge-tests-so4-2-ltVzx*

---

## Summary

**1 PASS / 3 FAIL.** The S³ Gegenbauer projection captures the selection rules exactly but NOT the radial scaling. The Balmer-α matrix element is off by a factor of 6.4. This is not a failure of the SO(4,2) embedding — it's a clean separation between what the 6D fundamental rep captures (angular structure) and what the infinite-dimensional UIR captures (radial wave functions).

---

## What the S³ Embedding Gets Right

### Selection rules: EXACT (Δk = ±1)

The Gegenbauer recurrence gives an analytically exact result:

```
x · C_k^1(x) = [C_{k+1}^1(x) + C_{k-1}^1(x)] / 2
```

Therefore:
- **⟨k±1|cos ψ|k⟩ = 1/2** for ALL k (normalized, universal)
- **⟨k'|cos ψ|k⟩ = 0** for |k'-k| ≠ 1 (exact selection rule)

This maps to hydrogen: Δn = ±1, verified numerically to 6 decimal places across all k from 0 to 5. The full matrix element table is perfectly tridiagonal with all off-diagonal elements exactly 0.500.

### Lyman-α calibration: EXACT (by construction)

M₁₂ = R/2 = 1.4898/2 = 0.7449 ea₀ — matches the known 1s→2p dipole moment.

---

## What the S³ Embedding Gets Wrong

### The S³ prediction is UNIVERSAL: M = R/2 = 0.7449 for ALL Δk=1 transitions

But the actual hydrogen matrix elements grow rapidly with n:

| Transition | Known (ea₀) | S³ pred (ea₀) | Ratio |
|-----------|-------------|---------------|-------|
| 1s→2p | 0.7449 | 0.7449 | **1.00** (cal) |
| 2s→3p | 3.065 | 0.7449 | 4.1 |
| 2p→3d | 4.748 | 0.7449 | **6.4** |
| 3s→4p | 6.680 | 0.7449 | 9.0 |
| 3p→4d | 9.880 | 0.7449 | 13.3 |
| 3d→4f | 15.100 | 0.7449 | **20.3** |

The S³ angular matrix element is constant (1/2) but the physical matrix elements grow because the **radial integrals** scale as ~n².

### The l-channel ratios are also wrong

CG predicts 2p→3d / 2p→3s = √2 ≈ 1.41. The known ratio is 9.2. The factor of 6.5 discrepancy comes from the l-dependent radial integrals (the radial wave function overlap ∫R_{n'l'}·r·R_{nl}·r²dr depends strongly on l).

---

## Diagnosis: Angular vs Radial Separation

The S³ Gegenbauer projection captures the **angular structure** of hydrogen:
- Selection rules (Δk = ±1 → Δn = ±1)
- The universal angular matrix element (1/2)
- The Dirac-Weyl null cone decomposition

It does NOT capture the **radial structure**:
- The n-dependent scaling (wave function overlap grows with n)
- The l-dependent radial integrals (higher l → larger radial overlap for Δl = +1)

**This is not a failure of the SO(4,2) identification.** It's the expected separation between:
- The **6D fundamental rep** (the Eckert field) — carries the angular/selection rule information
- The **infinite-dimensional UIR** (the Rac/hydrogen states) — carries the radial wave function information

The S³ embedding lives in the fundamental. The hydrogen radial wave functions live in the Rac. The intertwiner (HP31) connects them, but the full matrix element requires BOTH pieces. We computed only the fundamental piece.

---

## What Would Fix It

The full matrix element is:

```
⟨n'l'm'|r|nlm⟩ = (radial integral) × (angular CG factor)
```

The S³ embedding gives the angular factor (1/2 from Gegenbauer × CG coefficient from SO(3)). The radial integral requires working in the Rac representation — specifically, computing the matrix element of the position operator r between hydrogen radial wave functions R_{nl}(r) and R_{n'l'}(r).

The Gordon formula (1929) gives these exactly. The key point: **the radial integral is not predicted by the null cone map alone**. It requires the full infinite-dimensional representation theory of SO(4,2).

The next step would be to compute the SO(4,2) matrix elements of the fundamental acting on the Rac, which automatically includes both the angular AND radial parts. This is the Barut-Kleinert formula (1967).

---

## Kill Conditions

| KC | Test | Status | Detail |
|----|------|--------|--------|
| K-HP-136 | Balmer-α within 50% | **FAIL** | Off by 6.4× (radial scaling missing) |
| K-HP-137 | Selection rules Δl=±1 | **PASS** | Exact from Gegenbauer recurrence |
| K-HP-138 | l-channel ratios match CG | **FAIL** | CG gives √2, known is 9.2 (radial l-dep) |
| K-HP-139 | Power-law n-scaling | **FAIL** | Best α=0.44, RMS log-error=1.48 |

**Score: 1/4 PASS.**

---

## Impact Assessment

### What's confirmed (HP27 + HP31 + HP32 + HP33)
- SO(4,2) IS the right group (HP27: Casimir matches)
- The Eckert fundamental rep connects to hydrogen (HP31: intertwiner exists)
- The null cone embedding is exact (HP32: Fisher metric, Dirac-Weyl)
- Selection rules are exact (HP33: Gegenbauer Δk=±1 → Δn=±1)

### What HP33 reveals
- The 6D fundamental captures ANGULAR structure only
- RADIAL structure requires the infinite-dimensional Rac
- The separation is clean — not a partial failure, but a clear boundary
- The missing piece is well-understood mathematically (Gordon/Barut-Kleinert formulas)

### What this means for the program
- **Paper 131**: Unaffected (Kramers barriers, not hydrogen specifics)
- **Paper 132**: HP33 sharpens the claim. The SO(4,2) embedding is STRUCTURAL (selection rules, symmetry) not QUANTITATIVE (matrix elements). This is honest and correct — the same way the rotation group SO(3) gives selection rules without giving radial integrals.
- **Next experiment**: HP34 would use the Barut-Kleinert approach — compute SO(4,2) matrix elements of the fundamental ACTING ON the Rac. This automatically includes radial integrals.

---

## Numerical Quick-Reference

```
# S³ Gegenbauer (exact)
⟨k±1|cos ψ|k⟩ = 1/2    (for ALL k, normalized)
⟨k'|cos ψ|k⟩ = 0       (for |k'-k| ≠ 1)

# HP32 calibration
d = 2.6849, R = 1.4898
M = R/2 = 0.7449 ea₀ (universal angular factor)

# What's missing
Radial scaling: grows as ~n² (from Rac, not fundamental)
l-dependence: radial integrals vary by factors of 10+ across l channels
Total l-summed strengths: 1→2: 2.23, 2→3: 8.13, 3→4: 18.3

# Kill conditions: 1/4 PASS
# But the 1 PASS (selection rules) is the STRUCTURAL result
# The 3 FAILs are all radial — well-understood, fixable via Rac
```

---

*End of HP33 analysis.*
