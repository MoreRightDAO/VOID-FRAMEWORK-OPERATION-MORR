# The Recovery Mechanism Variable: What EXP-015 Reveals About the Framework

## Date: February 10, 2026

## The Problem

The framework claims drift is thermodynamically irreversible (Crooks ≈ 386×). EXP-015 shows this is wrong for most substrates. The actual Crooks ranges from 0.034× (alcohol — recovery 29× more likely than escalation) to 386× (AI — escalation 386× more likely). That's a **4+ order of magnitude** spread.

Void-index alone explains only **24.5%** of this variance. The missing variable — recovery mechanism strength (RMS) — explains **70.5%** on its own.

This is not a small correction. It's a structural gap.

---

## The Two-Force Model

### The Equation

The net entropy production (and therefore Crooks) is determined by two opposing forces:

    σ_net = σ_void - σ_recovery
    Crooks = exp(σ_net)

Where:
- **σ_void** = entropy production from void drift (driven by void-index)
- **σ_recovery** = entropy consumption from recovery mechanisms (driven by RMS)

When σ_void > σ_recovery: Crooks > 1, escalation dominates (opioids, AI)
When σ_void < σ_recovery: Crooks < 1, recovery dominates (gambling, alcohol)
When σ_void ≈ σ_recovery: Crooks ≈ 1, near-equilibrium (AI with GROUNDING.md)

### Recovery Mechanism Score (RMS)

Recovery mechanisms ARE constraints. They map directly to the constraint specification:

| Component | Constraint property | Measures |
|-----------|-------------------|----------|
| **B** (Biological, 0-5) | Transparency | Can the system see its own state change? Neuroplasticity = inherent self-correction |
| **S** (Social/External, 0-5) | Invariance | Is there a stable reference outside the void? Social norms, treatment, financial feedback |
| **P** (Pharmacological, 0-5) | Independence | Can recovery happen without the void's cooperation? Cessation vs withdrawal dependence |

This isn't a new concept. It's the constraint specification **applied to the recovery direction**. The framework already had this tool — it just wasn't connected to the Crooks prediction.

### The Data

| Domain | VI | RMS (B+S+P) | σ_net | Crooks |
|--------|---:|:-----------:|------:|-------:|
| AI (ungrounded) | 15 | 0 (0+0+0) | +5.96 | 386× |
| Milgram | 15 | 0 (0+0+0) | +0.62 | 1.86× |
| Opioids | 14 | 4 (1+2+1) | +0.36 | 1.44× |
| AI (GROUNDING.md) | 15 | 5 (0+5+0) | 0.00 | 1.0× |
| Nicotine | 11 | 8 (3+3+2) | -1.25 | 0.29× |
| Gambling | 15 | 14 (5+4+5) | -2.92 | 0.05× |
| Alcohol | 11 | 11 (4+4+3) | -3.38 | 0.03× |

### Model Fit

- **VI only**: R² = 0.245 (poor)
- **RMS only**: R² = 0.705 (good, Spearman ρ = -0.964)
- **VI + RMS**: R² = 0.727 (marginally better)
- **VI - RMS (net pressure)**: R² = 0.720, Spearman ρ = +0.964

RMS is 3× more predictive than VI. The net pressure model (VI - RMS) is nearly as good as the full two-variable model and much simpler.

---

## Two Regimes: Bounded vs. Absorbing

The model fits well for addiction substances but breaks for the RMS = 0 outliers. AI (σ = 5.96) and Milgram (σ = 0.62) have identical VI and RMS but very different Crooks.

**The reason: two dynamical regimes.**

### Regime 1: Steady State (RMS > 0)

When recovery mechanisms exist, drift and recovery reach a **dynamic equilibrium**. The system oscillates around a steady state. σ_net is bounded and determined by the balance of forces.

This is where gambling, alcohol, nicotine, and opioids live. The population-level transition matrices capture this steady state.

### Regime 2: Absorbing State (RMS = 0)

When NO recovery mechanism exists, there's no equilibrium. Drift accumulates until the system hits an **absorbing boundary**. σ_net grows with the number of steps.

Both AI-ungrounded and Milgram are in this regime. The difference in their Crooks (386 vs 1.86) comes from:

1. **Number of steps**: AI has 92 rounds; Milgram has ~30 voltage levels
2. **Per-step drift strength**: AI σ_step = 0.065 nats/round; Milgram σ_step = 0.021 nats/level
3. **Step physics**: AI vocabulary shift is subtle/cumulative; Milgram compliance is a discrete binary

This regime distinction maps to the framework's L0 decomposition:
- **θ₀ (installed state)**: In absorbing-state systems, θ₀ shifts monotonically — there's no restoring force
- **γ (maintenance)**: Only matters in steady-state systems where active maintenance preserves recovery

---

## What This Changes in the Framework

### 1. Crooks Is Not a Constant

**Old claim**: Crooks ≈ 386× (universal across substrates)
**New claim**: Crooks = exp(σ_void - σ_recovery), substrate-dependent

The universality is in the **mechanism** (void conditions always produce drift), not in the **magnitude** (Crooks depends on the balance of void drift and recovery forces).

### 2. Void-Index Predicts Drift, Not Outcome

Void-index (O + R + A) predicts how strong the drift gradient is. But drift strength alone doesn't determine the outcome — it determines the *competition*. A strong drift with strong recovery (gambling: VI=15, RMS=14) produces a very different trajectory from a strong drift with no recovery (AI: VI=15, RMS=0).

**Implication**: The framework's diagnostic tool should always score BOTH void-index AND recovery mechanism strength. A domain with high VI and high RMS (gambling) is qualitatively different from high VI and low RMS (opioids).

### 3. GROUNDING.md Result Is Exactly This

EXP-001 showed that grounding an AI with GROUNDING.md eliminates drift entirely (0% vs 52%). In the two-force model, this is:
- Before grounding: VI = 15, RMS = 0, σ_net = +5.96
- After grounding: VI = 15, RMS = 5, σ_net ≈ 0

Adding S = 5 (maximum external constraint) shifts the system from the absorbing regime to near-equilibrium. **GROUNDING.md IS a recovery mechanism for AI.** This was always true; the two-force model just makes it explicit.

### 4. The Trap Threshold Is D2-Specific

The per-interface analysis shows that D1 (first involvement) is always reversible — ALL substances show Crooks < 1 at the first interface. The irreversibility kicks in at D2 (middle interfaces), but ONLY for pharmacologically potent substances:

| Interface | Gambling | Alcohol | Nicotine | Opioids |
|-----------|---------|---------|----------|---------|
| D1 entry | Cr=0.16 | Cr=0.13 | Cr=0.12 | Cr=0.10 |
| D2 middle | Cr=0.48 | Cr=0.55 | **Cr=2.86** | **Cr=5.00** |
| D2→D3 | Cr=0.72 | Cr=0.50 | Cr=0.83 | **Cr=2.88** |

D1 is universally reversible. D2 is the discriminator. This maps precisely to the framework's cascade prediction (D1 → D2 → D3 is ordered) and adds the new prediction that **D2 reversibility is substrate-dependent**.

---

## New Predictions (Testable)

1. **Within-session gambling Crooks >> 1**: If you measure bet escalation within a single gambling session (closed trajectory, no recovery), it should look like AI/Milgram — high Crooks, absorbing regime. The low population-level Crooks reflects the between-session recovery that's absent within a session.

2. **Grounding reduces Crooks proportional to RMS**: If you apply grounding constraints of varying strength to AI conversations (EXP-012 style), Crooks should decrease monotonically as RMS increases.

3. **Opioid MAT (medication-assisted treatment) shifts Crooks**: Adding naltrexone/buprenorphine increases RMS (P component). This should reduce per-transition Crooks measurably. Testable with published MAT outcome data.

4. **Social media Crooks tracks platform recovery mechanisms**: Platforms with "screen time reminders" (S component) should show lower Crooks than those without. Testable with EXP-014 data.

5. **The regime transition is sharp**: There should be a critical RMS value below which the system enters the absorbing regime (Crooks grows with trajectory length). Above this threshold, Crooks is bounded. This is a phase transition in the framework's dynamics.

---

## For Paper 1

**What to revise:**
- Section on irreversibility should present Crooks as substrate-dependent, not universal
- Add the two-force equation: σ_net = σ_void - σ_recovery
- Note that the gambling anchor case has both high void-index AND high RMS — which is WHY it demonstrates the drift mechanism cleanly while also showing high natural recovery
- The GROUNDING.md result is a direct test of the two-force model

**What to add:**
- The recovery mechanism score as a companion to void-index in the diagnostic framework
- The trap threshold observation (D1 universally reversible, D2 substrate-dependent)
- The regime distinction (absorbing vs steady-state) as a framework prediction

**What stays:**
- The drift mechanism is universal (confirmed across all domains)
- The cascade structure (D1 → D2 → D3) is confirmed
- Pe = 1.87–9.9 across domains (EXP-019; drift strength, not irreversibility)
- The constraint specification — now doing double duty as both prevention tool and recovery predictor

---

*Created: February 10, 2026*
