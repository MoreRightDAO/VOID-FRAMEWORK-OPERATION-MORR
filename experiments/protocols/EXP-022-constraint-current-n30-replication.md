# EXP-022: Constraint Current — N=30 Replication of Pe-Effectiveness Correlation

## Status: COMPLETE — 2026-02-24. All hypotheses confirmed. See results/EXP-022/.
## Type: Empirical replication (Paper 52 blocker — N=10 → N≥30)
## Depends on: Paper 52 (J = −σ·ΔPe formalism), EXP-019 (cross-domain Pe methodology)

---

## 0. Purpose

Paper 52 reports Spearman ρ = −0.865 between Pe and effectiveness across N=10 international
governance mechanisms (p=0.0012). The council identified this as the primary credibility
blocker: N=10 is exploratory, not confirmatory. The p-value is achievable under undisclosed
selection conditions. The limitation section of Paper 52 already flags this.

**The question:** Does ρ(Pe, effectiveness) hold at N≥30 using the same O/R/C rubric,
applied by blinded raters, to an independently sampled set of governance mechanisms?

**Kill condition for this experiment:** If ρ falls below −0.60 at N=30, the Paper 52
result was a small-sample artifact and the constraint current thesis requires revision.

---

## 1. Design

### 1.1 Sampling Frame

Governance mechanisms are defined as: binding international agreements, multilateral
financial instruments, or statutory regulatory regimes that (a) have measurable effectiveness
outcomes in the academic literature, (b) have been in operation for ≥5 years, and (c) operate
on a domain scoreable on the O/R/C rubric.

**Target sample:** N=30 mechanisms, sampled from four categories:

| Category | Target N | Examples |
|----------|---------|---------|
| International financial regulation | 8 | Basel III, FATF, Dodd-Frank, MiFID II |
| Environmental/climate governance | 8 | Kyoto Protocol, Paris Agreement, EU ETS, REACH |
| AI/technology governance | 7 | EU AI Act, GDPR, FTC algorithmic guidance, CA CPRA |
| Development/institutional | 7 | IMF SAPs, World Bank conditionality, MDGs, SDGs |

The N=10 mechanisms from Paper 52 are included in the replication set (overlap allows
continuity check). The remaining 20+ are newly sampled.

### 1.2 Scoring Protocol

**Void Index scoring (O/R/C):** Each mechanism scored by two independent raters using the
standardized Void Model Card rubric from Paper 3. Raters are blinded to effectiveness scores
during void scoring. Inter-rater reliability computed (Cohen's κ) before moving to analysis.
Discrepancies >1 point on any subscale resolved by adjudication round.

**Effectiveness scoring:** Coded from academic consensus. For each mechanism, identify:
- Primary outcome domain (financial stability, emissions reduction, AI compliance, etc.)
- Best available effectiveness metric from peer-reviewed literature (meta-analyses preferred)
- Consensus rating: 0 (ineffective/harmful), 1 (mixed), 2 (modest positive), 3 (effective)
- Source citation required for each rating.

**Pe derivation:** Calculated from O/R/C composite using the standard formula from Paper 9.
Pe is derived AFTER effectiveness is coded, by a separate analyst who is blinded to
effectiveness scores.

**Longevity:** Years since adoption to present (2026).

### 1.3 Analysis

Primary: Spearman ρ(Pe, effectiveness) with bootstrap confidence intervals (N=10,000
resamples). Report as point estimate with 95% CI.

Secondary:
- Spearman ρ(Pe, longevity) — expect non-significant per Paper 52
- Spearman ρ(Void Index raw, effectiveness) — does O/R/C composite match Pe?
- Partial correlations controlling for mechanism age and domain
- Subgroup analysis by category (financial vs. environmental vs. AI vs. development)

**Pre-registration:** Primary hypothesis (ρ < −0.60) and analysis plan registered in
`ops/lab/protocols/` before data collection begins. No analyst sees combined Pe + effectiveness
data until pre-registration is complete.

### 1.4 Sample Size Justification

At N=10, ρ=−0.865 has power >0.99 (the result is large). The concern is not power but
selection: were the N=10 chosen in a way that inflated ρ? At N=30 with random sampling
within the frame above, a true effect of ρ=−0.70 has 85% power at α=0.05. A true effect
of ρ=−0.50 has 60% power — just sufficient to detect a weakened but meaningful relationship.
If N=30 produces ρ < −0.50, the paper requires revision of its effect size claims.

---

## 2. Data Sources

| Variable | Source |
|----------|--------|
| Mechanism effectiveness | Systematic reviews in Journal of International Economics, Global Environmental Politics, OECD working papers, World Bank evaluation reports |
| Mechanism parameters (O/R/C scoring inputs) | Statutory texts, OECD regulatory database, governance mechanism registry |
| Longevity | Adoption date from UN Treaty Collection, official regulatory registers |

All sources cited to primary documents. No analyst opinion substituted for documented consensus.

---

## 3. Pre-Registered Hypotheses

**H1 (primary):** Spearman ρ(Pe, effectiveness) < −0.60 at N=30, p < 0.05 (one-tailed).
- Confirms Paper 52 directional claim at expanded sample.

**H2:** Spearman ρ(Pe, longevity) is non-significant (|ρ| < 0.30, p > 0.10).
- Replicates selection-pathology pattern: mechanisms persist regardless of effectiveness.

**H3:** Inter-rater reliability (Cohen's κ) on O/R/C subscores ≥ 0.70.
- Confirms void scoring is intersubjectively reliable, not rater-dependent.

---

## 4. Falsification Conditions

| Outcome | Interpretation |
|---------|---------------|
| ρ ≥ −0.40 at N=30 | Paper 52 result was small-sample artifact. Revise constraint current thesis. |
| ρ ∈ (−0.60, −0.40) | Weakened replication. Paper 52 claims require downgrade to "preliminary." |
| ρ ≤ −0.60, p < 0.05 | Replication confirmed. Paper 52 quantitative claims stand. |
| Cohen's κ < 0.60 | Scoring rubric requires revision before further quantitative claims. |

---

## 5. Output

- `results/EXP-022/` — raw scores, IRR calculations, Spearman results, bootstrap CIs
- `results/EXP-022/mechanisms-dataset.csv` — 30-row dataset, publishable as data supplement
- `results/EXP-022/EXP-022-report.md` — findings summary, falsification assessment
- If H1 confirmed: update Paper 52 §X (Limitations) to note replication result and add
  dataset to §Data and Code Availability section.
