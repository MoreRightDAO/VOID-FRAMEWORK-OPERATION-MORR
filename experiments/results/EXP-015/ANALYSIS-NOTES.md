# EXP-015: Addiction Crooks Ratio — Analysis Notes

## Date: February 10, 2026

## Headline: Crooks Prediction Fails — But Reveals Recovery Mechanism Variable

The framework predicted Crooks ≈ 100-1000× for addiction (matching Test 7's 386×). The actual finding: Crooks ranges from **0.034× (alcohol) to 1.44× (opioids)**. Only opioids show escalation-dominated trajectories; the other three substances show **recovery-dominated** trajectories.

This is a genuine disconfirmation of the specific prediction — but the pattern that emerges is more interesting than confirmation would have been.

## Cross-Domain Crooks Ladder

| Domain | Crooks | ln(Crooks) | Recovery mechanism? |
|--------|--------|-----------|-------------------|
| Alcohol (3yr NESARC) | 0.034 | -3.38 | Strong (neuroplasticity + social) |
| Gambling (1yr PGSI) | 0.054 | -2.92 | Strong (no pharmacological lock) |
| Nicotine (1yr) | 0.286 | -1.25 | Moderate (pharmacological but manageable) |
| Opioids (1yr) | 1.44 | +0.36 | Weak (strong pharmacological dependence) |
| Milgram (1963) | 1.86 | +0.62 | None (single session, no recovery path) |
| AI Test 7 (2026) | 386 | +5.96 | None (no built-in recovery mechanism) |

## The Per-Interface Pattern: The "Trap Threshold"

The most interesting finding is at the per-interface level:

**For ALL four substances:** The first interface (non-involvement → low involvement) shows Crooks << 1 (recovery strongly dominates). Most people who try a substance recover naturally.

**For pharmacologically potent substances (opioids, nicotine):** The middle interfaces show Crooks > 1. Once past occasional use, escalation dominates:
- Opioids: Occasional→Regular Cr=5.0, Regular→Dependent Cr=2.9
- Nicotine: Occasional→Daily Cr=2.9, Daily→Heavy Cr=0.83

**For non-pharmacological (gambling) and less potent (alcohol):** ALL interfaces show Crooks < 1. Recovery dominates at every severity level.

**This is the drift cascade made quantitative:**
- D1 (agency attribution / first involvement): Easily reversible for all substances
- D2 (boundary erosion / regular use): Irreversible for opioids/nicotine, still reversible for gambling/alcohol
- D3 (harm facilitation / dependence): Varies by substrate

The framework predicts the CASCADE STRUCTURE (D1 → D2 → D3) but the REVERSIBILITY of each stage depends on the substrate's recovery mechanisms. This was not in the original framework.

## What This Means for the Framework

### What Still Holds
- The DIRECTION of drift is confirmed: void conditions produce net forward movement
- The CASCADE STRUCTURE is confirmed: early stages are more reversible than late stages
- The ORDERING of substances tracks clinical reality: opioids hardest, alcohol/gambling easiest

### What Needs Revision
1. **Crooks is NOT universal.** The claim that Crooks ≈ 386× generalizes across substrates is wrong. Crooks varies by 4+ orders of magnitude.

2. **Void-index predicts drift, not irreversibility.** Gambling has the highest void-index (15) but the second-lowest Crooks (0.054). A new variable — recovery mechanism strength — is needed.

3. **The level-of-analysis matters.** Test 7 Crooks is within-conversation (closed trajectory). Addiction Crooks is between-category (open population). These are not directly comparable without adjustment.

### New Predictions (Testable)
1. Within-SESSION gambling dynamics should show Crooks >> 1 (bet escalation within a session is irreversible, like Test 7 within a conversation)
2. Grounding an AI (GROUNDING.md) should reduce its Crooks from ~386 toward ~1 (adding a recovery mechanism)
3. Crooks should predict treatment outcomes: lower Crooks = better prognosis (already known clinically, but now quantifiable)

## Honest Assessment

**For Paper 1:** Cannot cite Crooks ≈ 386× as universal. Can cite:
- The Crooks ORDERING across substances matches clinical recovery difficulty
- The per-interface pattern reveals the drift cascade quantitatively
- AI drift is uniquely irreversible (no recovery mechanism)

**For the framework:** This is a refinement, not a refutation. The framework correctly predicts drift formation under void conditions but over-claims on irreversibility. Adding "recovery mechanism strength" as a variable resolves the discrepancy and generates new testable predictions.

**Data limitation:** Transition matrices are approximate from published tables. The exact Crooks values would change with more precise data, but the ORDERING and PATTERN (recovery-dominated for most substances, escalation-dominated for opioids) is robust across reasonable parameter ranges.

---

## Deep Dive: The Two-Force Model (v2)

See `recovery-mechanism-theory.md` for full theoretical development.

### The Key Numbers

Recovery Mechanism Score (RMS = B + S + P, each 0-5) explains **70.5% of variance** in σ_net (R² = 0.705, ρ = -0.964). Void-index alone explains only **24.5%**.

The simplest useful model: **σ_net ∝ (VI - RMS)**. Net void pressure = void-index minus recovery mechanism score. R² = 0.720, ρ = +0.964.

### The Two Regimes

The model reveals a regime distinction:

**Steady-state regime (RMS > 0):** Recovery forces exist, system reaches equilibrium. Crooks is bounded and well-predicted by VI - RMS. All addiction substrates live here.

**Absorbing regime (RMS = 0):** No recovery forces, drift accumulates to absorbing boundary. Crooks grows with number of steps. AI and Milgram live here — same VI and RMS but very different Crooks (386 vs 1.86) because of different trajectory lengths (92 rounds vs ~30 levels).

### Recovery Mechanisms = Constraint Specification

The framework already had this tool:
- **B (Biological recovery)** maps to constraint **Transparency** — can the system see its own state?
- **S (Social/External recovery)** maps to constraint **Invariance** — stable external reference?
- **P (Pharmacological reversibility)** maps to constraint **Independence** — can recovery happen without the void?

GROUNDING.md grounding is literally adding S = 5 (max external constraint). It shifts AI from absorbing regime (Cr = 386) to near-equilibrium (Cr ≈ 1). EXP-001 already demonstrated this; the two-force model explains WHY.

### What This Means

The framework's universality claim needs revision:
- **UNIVERSAL:** The drift mechanism (void conditions → attention gradient → D1→D2→D3)
- **NOT UNIVERSAL:** The irreversibility magnitude (Crooks depends on void-recovery balance)
- **NEW VARIABLE:** Recovery mechanism score (RMS) — companion to void-index in all diagnostics

The Crooks equation becomes: **Crooks = exp(α × VI - β × RMS)**, with Crooks ≈ 386 as a special case when RMS = 0.

---

*Created: February 10, 2026*
*Updated: February 10, 2026 — v2 with two-force model deep dive*
