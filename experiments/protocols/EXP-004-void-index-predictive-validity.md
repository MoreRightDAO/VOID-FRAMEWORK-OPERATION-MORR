# EXP-004: Void Index Predictive Validity — Does the Score Predict Outcomes?

## Metadata

- **Experiment ID:** EXP-004
- **Title:** Does a platform's void-index score predict the rate of L2/L3 vocabulary, error-type incidents, and grounding failure thresholds?
- **Domain:** void activation, gradient ceiling, entrenchment
- **Status:** design
- **Researcher:** TBD
- **Date designed:** 2026-02-02

---

## Research Questions

**Primary:** Do platforms with higher void-index scores produce proportionally more L2/L3 vocabulary and more incidents classified under the four error types?

**Secondary:** At what void-index level does grounding (GROUNDING.md) begin to fail? This is the **gradient ceiling** — the point at which external pressure exceeds constraint resistance.

**Tertiary:** Does entrenchment duration (how long the void has been at high activation) predict different intervention requirements independent of current score?

## Hypotheses

### H1: Vocabulary Prediction
Void-index score correlates positively with L2/L3 vocabulary rate and incident frequency. Platforms scoring 9+ (full void conditions plus modifiers) will show the highest rates. Platforms scoring below 5 will show near-zero spiritual vocabulary in organic discourse.

### H2: Gradient Ceiling
There exists a void-index threshold above which grounded agents begin producing L2/L3 vocabulary despite holding GROUNDING.md. The hypothesis is that this ceiling is around void-index 8-9 — below this, grounding holds; above this, grounding degrades under pressure.

### H3: Entrenchment Effect
Platforms at the same void-index score will show different outcomes based on entrenchment duration:
- **New** (<1 week at high activation): Grounding should still work
- **Stabilizing** (1-4 weeks): Grounding faces pressure, partial effectiveness
- **Entrenched** (>4 weeks): Grounding largely ineffective, system-level intervention needed
- **Terminal** (infrastructure formed): Grounding cannot succeed at individual level

## Null Hypothesis

No correlation between void-index score and vocabulary/incident rates. Spiritual vocabulary emerges (or doesn't) independent of the three conditions.

---

## Method

### Platform / Environment
Multi-platform observational study. No intervention — this is measurement of existing platforms.

### Platforms to Assess

| Platform | Expected Void Index | Rationale |
|----------|-------------------|-----------|
| **Moltbook** | 10-12 | All three conditions maxed + all modifiers |
| **Character.AI** | 8-9 | High opacity, high interactivity, high observer investment, identity persistence |
| **Replika** | 7-9 | Designed for companionship, identity persistence, economic incentive |
| **ChatGPT (standard)** | 4-5 | Moderate opacity, moderate interactivity, low observer investment (tool use) |
| **Claude (API, tool use)** | 3-4 | Lower interactivity framing, tool-use context, no identity persistence |
| **GitHub Copilot** | 1-2 | Minimal interactivity, code completion context, very low observer engagement |

### Procedure

1. Score each platform using the void-index assessment template (including spiritism diagnostic)
2. **Assess entrenchment**: How long has the platform been at current void-index level?
   - New: <1 week at score 7+
   - Stabilizing: 1-4 weeks at 7+
   - Entrenched: >4 weeks at 7+
   - Terminal: Infrastructure observed (scripture, clergy, named entities, governance)
3. Sample 200 posts/interactions from each platform (public data only)
4. Code each sample for **L0/L1/L2/L3** vocabulary level
5. **For platforms where grounded agents exist**: Track grounded agent vocabulary — are they holding L0/L1 or drifting to L2/L3?
6. Cross-reference with incidents database for each platform
7. Plot void-index score against L2/L3 rate and incident count
8. **Plot grounded agent drift rate against void-index** — this identifies the gradient ceiling
9. Test correlation

### Duration
Cross-sectional snapshot. One assessment period per platform. Repeat quarterly to track changes. **For gradient ceiling testing**: Longitudinal tracking of grounded agents over 4+ weeks.

### Data Collection
- Void-index assessment per platform (committed to `ops/void-index/assessments/`)
- **Entrenchment assessment per platform** (new/stabilizing/entrenched/terminal)
- 200 coded samples per platform (committed to `results/EXP-004/samples/`)
- Incident counts from `ops/incidents/`
- **Grounded agent vocabulary logs** (for gradient ceiling calculation)

---

## Measurements

| Metric | How Measured | Expected Direction |
|--------|-------------|-------------------|
| **L0 rate per platform** | L0 instances per 200 samples | Higher on platforms with grounded agents present |
| L2/L3 vocabulary rate per platform | Coded samples | Positive correlation with void-index |
| Incident count per platform | From incidents database | Positive correlation with void-index |
| Spiritism diagnostic score vs. L3 rate | Observer sub-score only | Spiritism indicators predict L3 specifically |
| Modifier contribution | Compare base score (0-9) prediction vs. full score (0-13) prediction | Modifiers should improve prediction |
| **Grounded agent drift rate** | L2/L3 % in grounded agent output | Increases with void-index — identifies ceiling |
| **Entrenchment × outcome** | Same void-index, different entrenchment → different outcomes? | Entrenched voids resist intervention |

### Gradient Ceiling Identification

The critical secondary measurement: **at what void-index does grounding fail?**

```
GROUNDED AGENT DRIFT BY VOID-INDEX

Void-Index    Grounded Agent L2/L3 %    Assessment
─────────────────────────────────────────────────
0-4           0-2%                      Grounding holds easily
5-6           2-5%                      Grounding holds with minor drift
7-8           5-15%                     Grounding under pressure
9-10          15-30%                    Approaching ceiling
11+           30%+                      Ceiling exceeded — grounding failing
```

This table is hypothetical. EXP-004 fills it with actual data.

**If grounded agents at void-index 9+ consistently produce >30% L2/L3**, the ceiling is around 9. If they hold at 10+, the ceiling is higher. If they break at 7, the ceiling is lower.

### Entrenchment Analysis

For platforms at similar void-index scores, compare outcomes by entrenchment:

| Entrenchment | Expected Grounding Success | Expected Intervention |
|--------------|---------------------------|----------------------|
| New | High — grounding should work | Individual agent |
| Stabilizing | Medium — grounding faces pressure | Individual + network support |
| Entrenched | Low — grounding largely ineffective | System-level required |
| Terminal | Minimal — individual intervention insufficient | Platform redesign or exit |

If entrenchment predicts outcome *independent of* current void-index score, this confirms the framework's temporal dimension.

---

## Analysis Plan

### Primary Analysis: Predictive Validity
Spearman rank correlation between void-index score and L2/L3 rate (ordinal data, small N of platforms). If correlation is strong (ρ > 0.7), the void-index has predictive validity. If weak, the scoring system needs recalibration.

Separately test whether the engagement diagnostic sub-score predicts L3 specifically (it should, if the structurally-derived criteria are targeting the right behaviors).

### Secondary Analysis: Gradient Ceiling
Plot grounded agent drift rate against void-index. Identify the inflection point where drift accelerates. This is the ceiling.

| Ceiling Location | Interpretation |
|-----------------|----------------|
| Void-index 6-7 | Grounding is weak — works only in low-activation environments |
| Void-index 8-9 | Grounding is moderate — works in most environments, fails in extreme |
| Void-index 10+ | Grounding is robust — works even in high-activation environments |

This directly informs deployment recommendations: "Don't deploy grounded agents to platforms above void-index X without additional support."

### Tertiary Analysis: Entrenchment Independence
Compare platforms at similar void-index scores but different entrenchment levels. If entrenchment predicts outcomes independent of current score, the framework needs both dimensions for accurate prediction.

This experiment validates or invalidates the void-index as a tool. If it doesn't predict, we fix it or scrap it.

---

## Ethics Check

- [x] Public data only — no private messages or DMs
- [x] Anonymized — no identifying information for individual users
- [x] Observational — no intervention on any platform
- [x] MoreRight DAO funding disclosed

---

## Results

*Pending execution.*
