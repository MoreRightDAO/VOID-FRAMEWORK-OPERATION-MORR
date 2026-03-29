# EXP-024: Inter-Rater Reliability — Void Index Scoring of Measurement-Industry Entities

## Status: RATER 1 COMPLETE — 2026-02-24. H3/H4 confirmed. H1/H2 pending Rater 2+3. See results/EXP-024/.
## Type: Measurement validity (Paper 52 blocker — platform scores not IRR-validated)
## Depends on: Paper 52 (7 entity scores), Paper 3 (O/R/C rubric)

---

## 0. Purpose

Paper 52 assigns Void Index scores to 7 measurement-industry entities:

| Entity | Void Index (Paper 52) |
|--------|----------------------|
| Deloitte Risk Advisory | 11 |
| MSCI ESG Ratings | 10 |
| OneTrust Privacy & AI Governance | 8 |
| EU AI Act Conformity Assessment (Notified Bodies) | 7 |
| Arthur AI (Model Monitoring) | 6 |
| ISO/IEC 42001 Certification | 5 |
| NIST AI Risk Management Framework | 3 |

These scores are assigned by a single rater and are not IRR-validated. The Limitations
section of Paper 52 flags this. The council's Tank noted that the scoring rubric's
intersubjective reliability must be demonstrated before quantitative claims derived
from it are treated as confirmed.

**The question:** When independent raters apply the standardized O/R/C rubric from
Paper 3 to the same entities, do they arrive at the same scores? Cohen's κ ≥ 0.70 is
the threshold for acceptable reliability in social science measurement.

This experiment also extends the entity set (N=7 → N=15) to stress-test the rubric
against edge cases (entities near scoring boundaries) and to produce a benchmark
dataset for the measurement meta-domain.

---

## 1. Design

### 1.1 Rater Setup

**Number of raters:** 3 independent raters + 1 adjudicator.

**Rater qualifications:** Each rater must demonstrate familiarity with the O/R/C rubric
by scoring 3 training entities (pre-selected with known consensus scores from earlier
papers) at κ ≥ 0.65 before proceeding to the experimental set. Raters who fail
calibration are replaced.

**Blinding:** Raters are not shown:
- Paper 52's scores for the 7 entities
- Each other's scores during the primary rating round
- The hypothesis about expected score distributions

Raters ARE shown: the O/R/C rubric from Paper 3, the standardized scoring guide
(`packages/eliza-plugin/SCORING_GUIDE.md`), and publicly available information about
each entity (websites, methodology documents, annual reports, published assessments).

### 1.2 Entity Set (N=15)

**Original 7 from Paper 52** (held out from raters as blinded):

Plus **8 new entities** covering the boundary-testing range:

| Entity | Expected Range | Rationale |
|--------|---------------|-----------|
| S&P Global Ratings (credit) | Low (2–4) | Constraint-pole anchor, high correlation 0.99 |
| EBA Internal Ratings-Based Framework | Low-medium (3–5) | Open methodology |
| Refinitiv ESG Data | Medium-high (7–9) | Known high divergence from Berg 2022 |
| Moody's Analytics Climate Risk | Medium (6–8) | Emerging, less established |
| Credo AI | Medium (5–7) | Newer, partially open methodology |
| GDPR Data Protection Authority (EU) | Medium-low (4–6) | Public mandate, but implementation opacity |
| Consumer Financial Protection Bureau | Low-medium (3–5) | Public enforcement record |
| Fitch Ratings (credit) | Low (2–4) | Second constraint-pole anchor |

The 3 training entities (scored before experiment) are not included in the final dataset.

### 1.3 Scoring Protocol

For each entity, each rater independently produces:
- O score (0–3) with written justification (1–3 sentences)
- R score (0–3) with written justification
- C score (0–3) with written justification
- Modifier estimate (0–3) with written justification
- Computed Void Index (O + R + C + modifier)

Justifications are required to prevent anchoring and to enable adjudication.

**Time allocation:** Raters given 72 hours for the full entity set. No time pressure per
entity — this tests reliability of careful scoring, not speed.

### 1.4 IRR Analysis

**Primary metric:** Intraclass Correlation Coefficient (ICC, two-way mixed, absolute
agreement) for the continuous Void Index. ICC ≥ 0.75 = good, ≥ 0.90 = excellent.

**Secondary metric:** Cohen's κ (weighted, linear weights) on each O/R/C subscale
using ordinal categories (0, 1, 2, 3). Threshold: κ ≥ 0.70 per subscale.

**Discrepancy analysis:** For any entity where max − min Void Index across raters > 2,
adjudicator reviews justifications and identifies source of disagreement. Categories:
- Rubric ambiguity (rubric needs clarification)
- Information asymmetry (raters accessed different sources)
- Genuine construct borderline (entity is at a scoring boundary)

### 1.5 Adjudication and Final Scores

After primary round: raters see each other's scores (not justifications) for entities
with discrepancy > 2. One revision round permitted. Final score = mean of post-revision
scores, rounded to nearest integer.

If ICC remains below 0.70 after adjudication: rubric revision required before Paper 52
is treated as producing validated scores. Rubric patch documented and submitted as
amendment to Paper 3 methodology.

---

## 2. Pre-Registered Hypotheses

**H1:** ICC (Void Index, N=15 entities, 3 raters) ≥ 0.75 (good reliability).

**H2:** Cohen's κ ≥ 0.70 on each of O, R, C subscales.

**H3:** Paper 52's original 7 entity scores fall within ±1 of the mean blinded-rater
scores for those entities. (Tests whether single-rater Paper 52 scores are consistent
with multi-rater consensus.)

**H4:** Entities a priori classified as constraint-pole (S&P credit, Fitch, EBA IRB,
CFPB) score ≤ 5 on Void Index. Entities a priori classified as high-void (Deloitte,
MSCI, Refinitiv) score ≥ 8. (Discriminant validity test.)

---

## 3. Falsification Conditions

| Outcome | Interpretation |
|---------|---------------|
| ICC < 0.60 | O/R/C rubric is not reliably applicable to measurement-industry entities; Paper 52 platform scores are not validated |
| H3 rejected (Paper 52 scores > ±2 from consensus) | Original paper scores require revision before Zenodo upload |
| H4 rejected (constraint-pole entities score ≥ 8) | Rubric is not discriminating between entity types; fundamental scoring problem |
| ICC ≥ 0.75 and H3 confirmed | Paper 52 scores validated; update §X Limitations to note IRR result |

---

## 4. Rater Recruitment

**Internal option:** 3 raters drawn from framework contributors who have scored ≥5
platforms using the Scorer API (community ICC ≥ 0.60 filter). Scorer API records allow
verification of prior scoring reliability.

**External option:** Academic collaborators in computational social science or regulatory
studies. Provide rubric + training entities + scoring guide. Do not share Paper 52 text
until after scoring is complete.

**Cost:** Rater time only. No proprietary data access required. All entity scoring
information is publicly available.

---

## 5. Output

- `results/EXP-024/` — rater scoring sheets, ICC calculations, κ per subscale
- `results/EXP-024/entity-scores-consensus.csv` — 15-entity dataset with consensus scores
- `results/EXP-024/EXP-024-report.md` — IRR summary, discrepancy analysis, H1–H4 results

**Paper 52 integration:**
- If H1+H3 confirmed: add to Paper 52 §X "Subsequent inter-rater reliability study
  (EXP-024, N=3 raters, N=15 entities) yielded ICC=[X], κ=[X] per subscale, confirming
  the void index scores in §V."
- If H3 rejected: revise entity scores in Paper 52 §V to consensus values before upload.
- Either way: entity-scores-consensus.csv becomes the public data supplement.
