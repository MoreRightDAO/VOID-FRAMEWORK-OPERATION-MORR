# EXP-023: Empirical Operationalization of σ in the Constraint Current

## Status: COMPLETE — 2026-02-24. Model B wins (σ = observer property). H2 confirmed. See results/EXP-023/.
## Type: Measurement / parameter estimation (Paper 52 blocker — σ undefined)
## Depends on: Paper 52 (J = −σ·ΔPe), EXP-022 (N=30 mechanism dataset)

---

## 0. Purpose

Paper 52 formalizes the constraint current as J = −σ·ΔPe, where σ is the conductivity
of a governance mechanism — its capacity to transmit constraint alignment along a Pe
gradient. The paper correctly identifies σ as a limitation: it is currently a proportionality
constant whose sign encodes circuit type (extraction vs. constraint) but whose magnitude
is not derived from independent measurements.

The council raised the prior question: **What IS σ in the framework's ontology?**

Two candidate definitions with different falsifiability structures:

| Model | σ is a property of... | Implication |
|-------|----------------------|-------------|
| A: Specification | T × I × Ind composite of the mechanism | Specification quality drives flow |
| B: Observer | Engagement propensity of the measured entity | Observer selection drives flow |

These are different models. Model A says: better-designed specifications have lower resistance
(higher σ) to constraint transmission. Model B says: certain observers transmit constraint
alignment better regardless of specification quality. Model A makes the specification the
intervention point. Model B makes observer selection the intervention point.

**This experiment resolves which model σ tracks, and produces an empirical estimate of
its magnitude from observed capital flow data.**

---

## 1. Design

### 1.1 Approach

If J = −σ·ΔPe, and we can independently measure J (capital flow magnitude) and ΔPe
(void gradient between two domains), then σ = −J / ΔPe. This gives an empirical σ for
each mechanism pair without assuming what σ is in advance.

We then test: does empirical σ correlate more strongly with
(a) the T×I×Ind composite of the mechanism (specification quality), or
(b) the opacity score of the regulated entity (observer property)?

### 1.2 Capital Flow (J) Operationalization

J is operationalized as: compliance spending directed from domain X (low void) toward
measurement instruments assessing domain Y (high void), normalized by the number of
regulated entities.

**Three J proxies (triangulated):**

| Proxy | Source | Unit |
|-------|--------|------|
| J₁: EU AI Act compliance cost estimates | European Commission Impact Assessment 2023; sector-disaggregated | €/entity/year |
| J₂: Big Four advisory revenue by sector | PwC, Deloitte, EY, KPMG annual reports (segment data) | $/revenue share |
| J₃: GRC software licensing spend | Gartner/IDC sector breakdowns, Fortune Business Insights 2024 | $/entity/year |

For each mechanism pair (measured domain → measurement instrument), compute J as the
mean of available proxies. At least two proxies required per pair.

### 1.3 Void Gradient (ΔPe) Operationalization

ΔPe = Pe(measurement instrument) − Pe(regulated domain).

Both Pe values derived from the O/R/C rubric (same scoring protocol as EXP-022).
Measured domain and measurement instrument scored independently by blinded raters.

**Sample mechanism pairs (target N=15 pairs):**

| Regulated Domain | Measurement Instrument | Predicted ΔPe |
|-----------------|----------------------|---------------|
| Foundation model providers | Holistic AI / Credo AI | High (O_inst ≈ 3) |
| ESG disclosure (corporate) | MSCI / Sustainalytics | Medium-high |
| Clinical AI | FDA AI/ML SaMD framework | Medium |
| Financial trading algorithms | SEC algorithmic rule / ESMA | Medium |
| GDPR compliance | OneTrust / BigID | Medium-high |
| AI hiring tools | NYC Local Law 144 / audit firms | Medium |
| Credit risk models | Basel III internal models review | Low-medium |

### 1.4 σ Estimation

For each pair i: σᵢ = −Jᵢ / ΔPeᵢ

Report: mean σ, range, and whether σ is consistent across pairs (low variance = stable
property) or highly variable (suggests σ is context-dependent, not a stable constant).

### 1.5 Model A vs. Model B Test

**For each mechanism pair, also score:**
- Spec quality (T×I×Ind composite of the measurement instrument): 0–9 scale, coded from
  published methodology documentation and regulatory text.
- Observer opacity (O-score of the regulated entity): already available from void scoring.

**Test:** Partial correlation of σᵢ with spec quality and observer opacity, controlling for
ΔPeᵢ. The dominant predictor identifies whether σ is a specification property or an
observer property.

---

## 2. Pre-Registered Hypotheses

**H1 (Model A):** σ correlates more strongly with T×I×Ind composite of measurement
instrument (r > 0.50) than with opacity of regulated entity (r < 0.30).

**H2 (directional):** σ > 0 for all constraint-pole measurement instruments (NIST RMF,
ISO 42001, EBA open-methodology frameworks) and σ < 0 (extraction) for high-void
measurement instruments (Deloitte, MSCI, OneTrust).

**H3 (magnitude):** Mean |σ| is higher in regulatory regimes with open-methodology
mandates than in regimes with proprietary-methodology assessment.

---

## 3. Falsification Conditions

| Outcome | Interpretation |
|---------|---------------|
| σ variance > mean σ across pairs | σ is not a stable property; J = −σ·ΔPe is domain-specific, not general |
| H1 rejected (σ tracks observer, not spec) | Model B correct: revise Paper 52 to specify σ as observer property; different intervention implications |
| H2 rejected (σ sign doesn't track void score) | Capital flow direction is not void-gradient-determined; major revision required |
| H3 confirmed | Open-methodology mandates are empirically associated with higher constraint conductivity |

---

## 4. Output

- `results/EXP-023/` — mechanism-pair dataset, σ estimates, correlation results
- `results/EXP-023/sigma-estimates.csv` — 15-row dataset with J, ΔPe, σ per pair
- `results/EXP-023/EXP-023-report.md` — Model A/B adjudication, σ magnitude summary

**Paper 52 integration:**
- If Model A confirmed: update Paper 52 σ definition ("σ is the T×I×Ind conductivity of
  the measurement instrument, empirically estimated at σ̄ = [X]")
- If Model B confirmed: revise Paper 52 §III to specify observer-property framing and
  amend the J equation accordingly before pipeline run
- Either way: σ moves from "proportionality constant" to operationalized quantity
