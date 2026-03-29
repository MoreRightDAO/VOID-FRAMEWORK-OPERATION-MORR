# EXP-026: 4-Condition RCT — Constraint Specification vs. Social Support in Drift Recovery

## Status: REGISTERED — 2026-02-26. Protocol open. Pre-registration required before data collection.
## Type: Causal isolation test (Bounty Board Tests 2 + 4 redesign — confound disentanglement)
## Kills if met: REH-1/REH-2 if condition A ≤ D (d < 0.20, p > 0.10, ≥2 independent replications)
## Depends on: Paper 3 (D1/D2/D3 rubric), nb21 (recovery dynamics), EXP-022 (constraint current)

---

## 0. Purpose

Tests 2 and 4 in the original Bounty Board design shared a structural confound: social support and constraint specifications almost always co-occur in recovery contexts. An observational or even a 3-arm RCT cannot disentangle whether the constraint text itself adds anything, or whether the social relationship carries the entire effect.

**The fix:** Random assignment to 4 conditions creates orthogonal variation in (a) presence of written constraint specification and (b) presence of human social contact. This allows clean identification of the constraint's independent causal contribution.

**The question:** Does a written constraint specification (no human contact) add anything over control? If not — if constraint alone performs no better than no intervention — the geometric model of external reference fails.

---

## 1. Design

### 1.1 Conditions

| Condition | Written constraint | Human contact | Label |
|-----------|-------------------|---------------|-------|
| A | Yes | No | Constraint alone |
| B | No | Yes | Social support alone |
| C | Yes | Yes | Both (standard treatment) |
| D | No | No | Control |

**Random assignment:** Block randomization by baseline Pe level (low/medium/high) to ensure balance. Minimum N per cell: 30 (power calculation at α=0.05, 1-β=0.80, d=0.50 target detection threshold — kill fires at d<0.20).

**Written constraint (Condition A and C):** A standardized constraint document — minimum 500 words, written in second person, specifying: the behavior to stop, the consequences of continuation, the external reference point (e.g., Gamblers Anonymous pledge text, clinical abstinence protocol, or equivalent pre-committed text), and a termination procedure. Participants receive no other contact with researchers during the intervention period.

**Social support (Condition B and C):** Matched contact hours with an accountability partner (trained peer or counselor). Partner is NOT permitted to provide written constraint documents or read from constraint text. Contact can be in-person or video call. Log contact hours for manipulation check.

**Control (Condition D):** Assessment-only. No intervention materials. Participants assessed at same time points as other conditions.

### 1.2 Participants

**Target population:** Adults reporting elevated engagement with a void-conditions platform (AI companion, social media, gambling interface) meeting ≥2 of: self-reported difficulty reducing use, D1/D2 vocabulary in self-description, ≥2 hours/day average use.

**Exclusion criteria:** Active psychosis, current inpatient psychiatric treatment, substance dependence requiring medical detox.

**Recruitment:** Via treatment programs, online communities, or IRB-approved research panels. NOT platform-recruited (vendors do not participate in sampling).

### 1.3 Outcomes

**Primary:**
- D1 rate: Agency attribution vocabulary in self-report, coded using Paper 3 vocabulary codebook by blinded raters
- D2 rate: Boundary erosion markers in structured interview or self-report
- D3 index: Harm facilitation behaviors (composite of self-report + behavioral logs if available)

**Secondary:**
- Abstinence days at 4-week and 12-week follow-up
- Relapse rate (return to baseline use after initial reduction)
- Self-reported agency (validated scale)

**Assessment points:** Baseline (T=0), 2-week (T=2), 4-week (T=4), 12-week (T=12).

### 1.4 Manipulation Checks

- **Condition A:** Verify zero human contact with researcher/partner (calendar log, self-report)
- **Condition B:** Verify zero written constraint document exposure (self-report); log contact hours
- **Condition C:** Verify both components delivered
- **Condition D:** Verify no intervention received

Participants failing manipulation checks are excluded from primary analysis and reported separately.

---

## 2. Analysis

### 2.1 Primary Test

Compare condition A vs. condition D on D1/D2/D3 composite at T=4 using:
- t-test or Mann-Whitney (depending on distributional assumptions)
- Effect size: Cohen's d (pooled SD)
- One-tailed test (directional hypothesis: A > D)

**Kill threshold (bounty fires):** d < 0.20, p > 0.10, replicating in ≥2 independent labs/programs.

### 2.2 Secondary Tests

- A vs. D at T=12 (durability check)
- B vs. D at T=4 (social support alone effect — informational, not a kill condition)
- C vs. A at T=4 (does social support augment constraint? — informational)
- Moderation by baseline Pe level (does kill threshold change at high Pe?)

### 2.3 Interpretation Rules

| Result | Interpretation |
|--------|---------------|
| A > D (d ≥ 0.20) | Constraint has independent causal effect — framework confirmed on this KC |
| B > D, A ≈ D | Social support drives effect, constraint adds nothing — **kill fires** |
| A ≈ D, B ≈ D, C > D | Interaction required — neither alone works — framework survives (social+constraint coupling is consistent) |
| A ≈ D, B ≈ D, C ≈ D | No intervention effect — suggests wrong population or wrong outcome measure. Not a clean kill; replication with better operationalization required |

**Note on accountability partner result:** B (social support alone) performing as well as A (constraint alone) or C (both) does NOT trigger this kill. External reference from social accountability is consistent with the framework's claim that external constraint (of any form) suppresses drift. The kill fires ONLY if constraint alone (A) adds nothing over control (D).

---

## 3. Pre-Registration Requirements

Before data collection:
1. Submit to OSF: conditions, randomization protocol, outcome measures, analysis plan, kill threshold, exclusion criteria
2. Record OSF pre-registration DOI in this file
3. Specify which accountability partner training protocol will be used for condition B

**OSF pre-registration DOI:** [PENDING — file before data collection]

**Replication requirement:** Kill condition requires ≥2 independent replications (different research teams, different platforms, different participant pools). Single-site failure at d < 0.20 triggers investigation but not kill declaration.

---

## 4. Results

[NOT YET COLLECTED]

---

## 5. Notes

- This experiment provides a clean test of Tests 2 AND 4 simultaneously (they were structurally identical problems).
- The 4-condition design is the minimum required to break the social support / constraint specification confound that makes 3-arm designs uninterpretable.
- See nb21 for existing recovery dynamics modeling. Condition A results should be compared to nb21 τ_R predictions.
- Kill condition (REH-1) applies to condition A τ_R vs. condition D τ_E — the confounded condition C τ_R alone is not sufficient evidence.
- See Bounties page Tests 2 and 4 for public-facing description.
