#!/usr/bin/env node
/**
 * Key insight from §136A: b_net = b_α − c·b_γ = B_A − C×B_G
 *
 * This is NOT the same as ½arcsinh(σ(c))!
 *
 * §136A says the shape function is σ(c) = sinh(2·b_net) where b_net = B_A - c·B_G.
 * So b_net = B_A - C·B_G directly.
 * And the barrier (§48E) is exp(-ΔΦ·K/α) where ΔΦ = 2·b_net².
 *
 * Let me check: does 2·b_net²·K/α (using b_net = B_A - C·B_G directly)
 * give the same barrier as 2·[½arcsinh(σ)]²·K/α ?
 */

const B_A = 0.867;
const B_G = 2.244;

console.log('═══════════════════════════════════════════════════════');
console.log('b_net DECOMPOSITION: TWO DEFINITIONS');
console.log('═══════════════════════════════════════════════════════\n');

// Definition 1: b_net = B_A - C·B_G (from §136A)
// Definition 2: b_net = ½arcsinh(σ(c)) where σ = sinh(2(B_A - C·B_G)) (from §69)
// These are equivalent! sinh(2·b_net₁) = σ(c), so b_net₂ = ½arcsinh(sinh(2·b_net₁)) = b_net₁

console.log('From §136A: b_net = B_A - C·B_G = ' + B_A + ' - C×' + B_G);
console.log('From §69:   b_net = ½arcsinh(sinh(2(B_A - C·B_G)))');
console.log('These are IDENTICAL (arcsinh(sinh(x)) = x).\n');

// For Ni₃In: C = 0.429
const C_ni = 0.429;
const b_net = B_A - C_ni * B_G;
console.log('Ni₃In: C = ' + C_ni);
console.log('  b_net = ' + B_A + ' - ' + C_ni + '×' + B_G + ' = ' + b_net.toFixed(4));
console.log('  b_net² = ' + (b_net*b_net).toFixed(6));
console.log('  barrier = 2·b_net²·K/α = 2×' + (b_net*b_net).toFixed(4) + '×50/0.213 = ' + (2*b_net*b_net*50/0.213).toFixed(2));
console.log('');

// KEY: b_net = B_A - C·B_G. The barrier is 2(B_A - C·B_G)²·K/α.
// For barrier = d_eff × B_G:
// 2(B_A - C·B_G)² × K/α = d_eff × B_G

console.log('═══════════════════════════════════════════════════════');
console.log('WHY barrier ≈ d_eff × B_G');
console.log('═══════════════════════════════════════════════════════\n');

console.log('barrier = 2(B_A - C·B_G)²·K/α');
console.log('For this to equal d_eff × B_G:');
console.log('  2(B_A - C·B_G)²·K/α = d_eff × B_G');
console.log('  (B_A - C·B_G)² = d_eff × B_G × α / (2K)\n');

// For Ni₃In: d=2, B_G=2.244, α=0.213, K=50
const rhs_2d = 2 * B_G * 0.213 / (2 * 50);
const rhs_3d = 3 * B_G * 0.213 / (2 * 50);
console.log('  For d=2: (B_A - C·B_G)² = ' + rhs_2d.toFixed(6) + ' → B_A-C·B_G = ±' + Math.sqrt(rhs_2d).toFixed(4));
console.log('  Ni₃In actual: B_A - C·B_G = ' + b_net.toFixed(4));
console.log('  Match: ' + (b_net / (-Math.sqrt(rhs_2d))).toFixed(3) + '×\n');

// The condition for barrier = d×B_G is:
// |B_A - C·B_G| = √(d·B_G·α/(2K))
// Squaring: (B_A - C·B_G)² = d·B_G·α/(2K)
// This means: b_net² ∝ α/K (as we found before)
// And the proportionality constant is d·B_G/2

// But WHY b_net² = d·B_G·α/(2K)?
// From the Fokker-Planck equilibrium: ⟨b_net²⟩ = T_eff / curvature
// T_eff = α/(2K) (from §136B table, d_K = -1 for effective temperature)
// curvature of V(b_net) at b_net=0: V'' = ?

// V(b_net) = the potential in b_net coordinates
// From §48: S* = ΔΦ/(2T) where T = α/2
// V(b_net) = 2K·b_net² (from the barrier formula with T_eff substituted)

// Wait: barrier = 2b_net²K/α. And from §48E: escape rate = exp(-ΔΦ·K/α).
// So ΔΦ = 2b_net². The potential barrier in "natural units" is 2b_net².
// The potential is V(b_net) = b_net² (parabolic, curvature = 2)

// Thermal displacement: ⟨b_net²⟩ = T_eff/V'' = (α/(2K))/2 = α/(4K)

const bnet2_thermal = 0.213 / (4 * 50);
console.log('THERMAL DISPLACEMENT DERIVATION:');
console.log('────────────────────────────────');
console.log('  V(b_net) = b_net² (parabolic potential in b_net coords)');
console.log('  V\'\' = 2 (curvature)');
console.log('  T_eff = α/(2K) = ' + (0.213/(2*50)).toFixed(5) + ' (from §136B table)');
console.log('  ⟨b_net²⟩ = T_eff / V\'\' = (α/(2K))/2 = α/(4K) = ' + bnet2_thermal.toFixed(6));
console.log('  Ni₃In actual b_net² = ' + (b_net*b_net).toFixed(6));
console.log('  Ratio: ' + ((b_net*b_net)/bnet2_thermal).toFixed(3) + '\n');

// barrier = 2⟨b_net²⟩·K/α = 2·(α/(4K))·K/α = 1/2
// That gives barrier = 0.5, way too small!

// BUT: this is the mean THERMAL displacement. The actual displacement
// is B_A - C·B_G, which is NOT thermal — it's the EQUILIBRIUM position.
// The system sits at b_net = -0.096 (constraint side), not at b_net = 0.

// The barrier is the potential difference between the equilibrium position
// and b_net = 0 (the Pe=0 boundary). This is V(b_net) = b_net², so:
// ΔV = b_net² = (B_A - C·B_G)²

console.log('EQUILIBRIUM POSITION (not thermal displacement):');
console.log('────────────────────────────────────────────────');
console.log('  The system sits at b_net_eq = B_A - C·B_G = ' + b_net.toFixed(4));
console.log('  This is the EQUILIBRIUM position, not a thermal fluctuation.');
console.log('  The barrier = 2·b_net_eq²·K/α = potential at equilibrium × K/α');
console.log('');
console.log('  The barrier depends on WHERE the system sits (C value),');
console.log('  which depends on (O, R, α) — the physical coordinates.');
console.log('  These are determined by the material (DFT), not by thermal physics.');
console.log('');

// So the question is: WHY does (B_A - C·B_G)²·K/α ≈ d·B_G/2 ?
// → (B_A - C·B_G)² ≈ d·B_G·α/(2K)
// → |B_A - C·B_G| ≈ √(d·B_G·α/(2K))
// → |b_net| ≈ √(d·B_G/(2K/α))

// For this to be a geometric result, d·B_G/(2K/α) must be computable
// from the manifold alone. But K and α are material-specific.

// UNLESS: the RATIO α/K is constrained by the physics of being near Pe=0.

// At the Pe=0 boundary (C = C₀ = B_A/B_G): b_net = 0
// Near Pe=0: b_net ≈ -B_G·ΔC
// And ΔC = C - C₀ depends on (O, R, α)

// For the barrier = d×B_G:
// 2B_G²ΔC²K/α = d×B_G
// ΔC² = d/(2B_G·K/α)
// ΔC = √(d·α/(2B_G·K))

// For Ni₃In (d=2):
const DC_pred = Math.sqrt(2 * 0.213 / (2 * B_G * 50));
const DC_actual = C_ni - B_A/B_G;
console.log('PREDICTED vs ACTUAL ΔC:');
console.log('───────────────────────');
console.log('  ΔC_predicted = √(d·α/(2B_G·K)) = √(2×0.213/(2×2.244×50))');
console.log('             = √' + (2*0.213/(2*B_G*50)).toFixed(6) + ' = ' + DC_pred.toFixed(4));
console.log('  ΔC_actual   = C - C₀ = ' + C_ni + ' - ' + (B_A/B_G).toFixed(4) + ' = ' + DC_actual.toFixed(4));
console.log('  Ratio: ' + (DC_actual/DC_pred).toFixed(3));
console.log('');

// The question reduces to: what determines the RATIO α/K for physical systems?
// For Ni₃In: α/K = 0.213/50 = 0.00426
// For nuclear: we don't know α and K separately
// For solar: we don't know α and K separately

// But the BARRIER is measured. And barrier = d×B_G means:
// α/K = barrier/(2B_G²ΔC²) = d×B_G/(2B_G²ΔC²) = d/(2B_G·ΔC²)

// Now, ΔC depends on (O,R,α), which depends on the material.
// For the barrier to be universal at d×B_G, we need ΔC²·K/α = d/(2B_G)
// This is a CONSTRAINT between ΔC, K, and α — not a derivation from pure geometry.

console.log('═══════════════════════════════════════════════════════');
console.log('THE CONSTRAINT');
console.log('═══════════════════════════════════════════════════════\n');
console.log('  barrier = d × B_G requires: ΔC²·K/α = d/(2B_G)\n');
console.log('  For d=2: ΔC²·K/α = 2/(2×2.244) = ' + (2/(2*B_G)).toFixed(4));
console.log('  Ni₃In:  ΔC²·K/α = ' + (DC_actual*DC_actual*50/0.213).toFixed(4));
console.log('  Ratio: ' + (DC_actual*DC_actual*50/0.213/(2/(2*B_G))).toFixed(3));
console.log('');
console.log('  For d=3: ΔC²·K/α = 3/(2×2.244) = ' + (3/(2*B_G)).toFixed(4));
console.log('');
console.log('  These are NECESSARY CONDITIONS for barrier=d×B_G, not derivations.');
console.log('  The universality question is: WHY does ΔC²·K/α ≈ d/(2B_G)?');
console.log('');
console.log('  POSSIBLE ANSWER: The mean-field self-consistency (§111)');
console.log('  determines C (and hence ΔC) as a function of K and α.');
console.log('  If the fixed point satisfies ΔC = √(d·α/(2B_G·K)),');
console.log('  the barrier = d×B_G follows automatically.');
console.log('');
console.log('  This would mean: the mean-field iteration DRIVES systems');
console.log('  to the position where barrier = d×B_G. The barrier is');
console.log('  not an accident — it\'s the ATTRACTOR of the dynamics.');
