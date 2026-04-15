# Event-Study v3 Pre-Registration Protocol

Date: 2026-04-03
Owner: MoreRight social-media litigation pipeline
Status: Draft prereg protocol
Purpose: Pre-lock design choices before running v3 event-study upgrades to reduce post-hoc flexibility risk.

## 1) Research Question

Can externally auditable platform-policy event windows show youth-concentrated adverse movement patterns that remain after placebo and negative-control testing?

## 2) Hypothesis Families

H1 (primary):
- Under-25 severe-outcome windows show stronger adverse movement than 26+ controls during pre-locked platform-policy events.

H2 (secondary):
- 18-25 bands show stronger concentration than broad adult controls in the same windows.

H3 (boundary):
- Regulatory/payout windows are expected to be less age-specific; if 26+ controls move similarly, those windows are non-diagnostic for youth-specific inference.

## 3) Data Inputs (Pre-Locked)

1. NSDUH age-band annual series (frozen snapshot).
2. Event metadata table with source references and timestamp fields.
3. Feature timeline references used only for event qualification, not outcome tuning.

## 4) Event Inclusion Rules (Pre-Locked)

Include an event only if all are true:

1. Publicly verifiable date from independent sources.
2. Event corresponds to a material platform-policy/product shift likely to affect exposure geometry.
3. Event is not selected based on observed outcome spikes in target series.

Exclude events when:

1. Date uncertainty exceeds predefined tolerance.
2. Overlap/collision with major non-platform macro shock windows cannot be resolved.
3. Event is primarily legal/PR noise without product-level exposure relevance.

## 5) Window Definitions (Pre-Locked)

1. Primary window: fixed symmetric annual window around event year.
2. Sensitivity windows: one narrower and one wider fixed alternative.
3. Placebo windows: calendar-shifted windows preserving window length and structure.

## 6) Outcome Families (Pre-Locked)

Primary:
- Youth severe outcome deltas (under-25 and/or 18-25 depending on available series definitions).

Negative controls:
- 26+ severe outcomes
- additional adult comparator outcomes where available

## 7) Estimation and Inference (Pre-Locked)

1. Exact/randomization inference for window concentration statistics.
2. Permutation tests aligned to pre-specified null structure.
3. Bootstrap intervals for robustness summary.

## 8) Multiplicity and Decision Rules

1. Report family-wise results by hypothesis family.
2. Distinguish exploratory from confirmatory outputs explicitly.
3. A finding is "supportive" only if:
   - primary youth family passes threshold, and
   - adult negative controls do not show equivalent signal direction/magnitude.

## 9) Robustness Battery (Mandatory)

1. Placebo window battery.
2. Alternative window width battery.
3. Leave-one-event-out stress test.
4. Event-family partition checks.
5. Sensitivity to pre-specified covariate adjustments (if included).

## 10) Non-Claims (Pre-Locked)

1. v3 is not framed as standalone legal causation proof.
2. v3 strengthens or weakens age-specific timing plausibility within an observational framework.
3. Null or mixed findings are treated as informative boundary evidence, not failures to be hidden.

## 11) Output Artifacts

1. `nsduh_event_window_quasi_v3_results.json`
2. `nsduh_event_window_quasi_v3_table.csv`
3. `EVENT-WINDOW-QUASI-EXPERIMENT-V3-NOTE.md`
4. Updated hostile-witness rows for any new supported/non-supported claims
5. Paper addendum section with explicit caveat language

## 12) Governance and Freeze Controls

1. Freeze this protocol before running v3 scripts.
2. Record commit hash at freeze and at run.
3. Log any deviation in a dedicated deviations table with rationale and impact.

## 13) Sign-Off

- Method lead:
- Date frozen:
- Commit hash (freeze):
- Commit hash (run):

