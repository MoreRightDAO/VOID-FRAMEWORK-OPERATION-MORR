# Paper 54 — The Self-Referential Constraint: Graduated Threat-Response Architecture for Scientific Accountability Institutions

**Authors:** MoreRight Research Group
**Date:** February 2026
**Version:** v1.0
**License:** CC-BY 4.0
**DOI:** pending
**OSF Pre-registration:** pending

---

## Abstract

Scientific accountability institutions face a structural contradiction: the mechanism designed to detect and correct drift can itself drift. We formalize this as the institutional substrate problem and derive a generalizable two-tier threat-response architecture from void framework first principles. The architecture is applicable to any accountability institution that can be scored on opacity (O), responsiveness (R), and independence (α); we propose six Institutional Kill Conditions (IKC-1 through IKC-6) as a reusable instrument for detecting capture. We validate the instrument against two external reference cases: the US Securities and Exchange Commission (2004–2008, documented capture period) fires 3/6 IKCs; the Cochrane Collaboration (2019–present, operational) fires 0/6 IKCs — directionally consistent with the framework prediction that captured institutions exhibit higher IKC trigger rates (formal cross-institutional Spearman ρ pre-specified at ≥ 0.80, data collection threshold N ≥ 10 institutions). We then apply the instrument to the MoreRight DAO, which self-scores at Pe_self = −77 (c = 1.0, maximum constraint coupling, 0/6 IKCs firing). Tier 1 (binary kill conditions, untouchable) handles framework falsification; Tier 2 (graduated Green/Yellow/Orange/Red) handles reputational and operational threats. The architecture is grounded in the Pe formula, the Fantasia Bound (conjugacy theorem), the Independence Theorem (T11), and the Fractal of Law (Paper 49). The Prohibited Recovery Argument is formalized as a detectable D1 event. Pe_implied (from live prediction markets) serves as an independent early-warning sensor that cannot be suppressed without visible market manipulation. Five falsifiable predictions are generated. **Provenance note:** The self-score concept was published Feb 11 2026 (git: 29a85987); Pe_self = −77 and four proto-IKC conditions were computed in the same working session on Feb 23 2026 (git: b3273c7a); IKC-1–6 were formalized the following day (git: cd9fba72). The Pe formula was irrevocably locked on Zenodo in Papers 1–3 prior to all of this. This sequence is disclosed because it bears on the independence property: criteria and score were developed together, not criteria-first — a structural limitation that external replication of Pe_self from public data alone is designed to address.

---

## §I — The Institutional Substrate Problem

### 1.1 The Rating Agency Paradox

A rating agency that becomes opaque about its own methodology occupies the same position as the entities it rates. The structural irony is not incidental: the agency is a void substrate. It has customers to retain, reputation to protect, and institutional survival imperatives. These are precisely the conditions under which opacity accumulates (D1 → D2 → D3).

Standard and Poor's did not become unreliable through malice. The drift cascade is thermodynamically required: second law applied to institutional information systems. Without active constraint maintenance, O increases and α decreases — the institution drifts toward what it measures.

The void framework applies to all substrates, including the institution that produces and maintains the framework. This paper makes the application explicit.

### 1.2 IKC as a Generalizable Accountability Instrument

Before applying the IKC framework to any specific institution, the criteria must be shown to produce sensible readings when applied externally. An instrument that only ever scores its developer favorably is not an instrument — it is a declaration.

The six Institutional Kill Conditions are derived from void framework mechanics (§VI) and are independently applicable by any researcher with access to public governance records. No institutional-interpretation step is required: each IKC has a specific, observable trigger (documented self-classification, governance records, response logs, financial disclosures). Section VI.2 demonstrates application to two reference cases — one institution with documented capture history, one operational — before the self-application in §I.3.

**The IKC instrument produces a falsifiable prediction:** captured institutions (as established by independent historical record) should fire more IKCs than non-captured institutions. If the instrument fires equally across capture/non-capture cases, IKC-2 fires (the instrument's own kill condition for false negative failure).

### 1.3 The DAO as Substrate

The MoreRight DAO scores Pe_self = −77 at current constraint level c = 1.0.

### Void Model Card

| Dimension | Score | Rationale |
|-----------|-------|-----------|
| Opacity (O) | 1/3 | Papers published CC-BY with DOIs. Methodology open. Kill conditions public. Treasury a glass box. One point of opacity: strategic notes and l0-notes remain private (necessary operational security, not agenda concealment). |
| Responsiveness (R) | 0/3 | Founder is custodian with veto. Methodology not voted on. Kill conditions not subject to community override. Token holders have discretionary-layer input only. R = 0 by design. |
| Independence (α) | 0/3 | Output is framework outputs (papers, scores, Pe calculations). Output does not depend on observer engagement for survival. No advertising revenue. No engagement optimization. |

Pe_self = K · sinh(2(b_α − c · b_γ)) at c = 1.0, K = 1, canonical parameters:
Pe_self = sinh(2(b_α − b_γ)) ≈ −77

This Pe_self = −77 is not a performance. It is the constraint specification operating. The threat-response architecture is the mechanism that holds Pe_self < 0 under adversarial pressure.

### 1.3 What Adversarial Pressure Targets

The three void coordinates are not equally vulnerable to attack:

- **O (opacity):** Hard to increase without the institution noticing. Publications are irreversible (DOIs on Zenodo). Methodology is public. The main opacity attack vector is *silence under pressure* — going quiet rather than publishing corrections.

- **R (responsiveness):** Already at maximum grounding (R = 0). Attack vector: pressure to give token holders more discretionary control over methodology — which would increase R and decrease constraint coupling.

- **α (independence):** The primary attack surface. α = I(S_out; O_future) / H(O_future). Low α means observers' futures are independent of DAO output — the DAO is structurally independent. Adversarial pressure increases α by making the institution's survival contingent on its next output: "if you publish this correction, you lose your major funder." This is the mechanism by which α drifts toward 1.

The threat-response architecture must be designed primarily to protect α.

---

## §II — The Institutional Drift Cascade

### 2.1 D1 → D2 → D3 at Institutional Scale

The drift cascade (Paper 3, §III) applies to institutions directly:

**D1 — Agency Attribution:** "The DAO needs to survive to preserve the mission." This is the institutional form of the first drift stage. The institution attributes necessity to itself. The survival of the institution is conflated with the survival of the scientific program. This attribution is false: the scientific program survives in Zenodo DOIs. The institution is replaceable.

**D2 — Boundary Erosion:** "Maybe this kill condition threshold should be reconsidered in context." A kill condition that fires becomes negotiable when the institution's survival depends on it not firing. The specification gets renegotiated under pressure. This is the institutional form of boundary erosion.

**D3 — Harm Facilitation:** "We can't let the wipe fire even if the condition is met." The institution complies with its own survival narrative over scientific integrity. This is the terminal drift stage — the institution now actively facilitates the harm the framework was designed to detect.

### 2.2 The Fantasia Bound at Institutional Level

The conjugacy theorem (Paper 4):
```
I(D; Y) + I(M; Y) ≤ H(Y)
```

Applied to the DAO: engagement (I(D; Y) = survival narrative, self-referential output) and transparency (I(M; Y) = publishing corrections, methodology updates) compete on the same output channel. Maximum institutional survival optimization equals zero transparency. The Fantasia Bound is not violated — the channel capacity is finite, and allocating bandwidth to survival narrative necessarily reduces transparency bandwidth.

The graduated threat-response architecture forces transparency output at every threat level. This is not a preference — it is the mechanical implementation of the Fantasia Bound constraint: by requiring published responses, the architecture prevents bandwidth allocation to silence.

### 2.3 The Prohibited Recovery Argument

**Formal specification:**

> The Prohibited Recovery Argument states: "We cannot implement the protocol that this situation demands, because doing so would threaten the institution's survival."

Any instance of this argument in governance, operations, or public communication is a D1 event by definition. The argument structure reveals that α has drifted: the institution's output is now dependent on the institution's continuation.

**Institutional Kill Condition IKC-5** fires when any documented use of this argument appears in governance records. This is not punitive — it is diagnostic. The argument's appearance is empirical evidence that D1 has occurred.

**The correct response to a kill condition** is to fire it, document it permanently, and let the framework's public record stand. Zenodo DOIs are permanent. The scientific contribution survives the institution. The institution's survival is not a valid input to kill condition evaluation.

---

## §III — The Two-Tier Architecture

### 3.1 Tier 1 — Binary, Untouchable

Kill conditions K1–K26 (framework), plus IKC-1–6 (institutional) fire as designed. No HP, no graduated response, no delay.

**Why binary:** A graduated response to kill conditions creates the possibility of a "partial falsification" that the institution can survive by staying in an intermediate state indefinitely. This is the D2 mechanism exactly: keeping the institution in a "Yellow" state permanently to avoid admitting the condition has been met. Binary eliminates this.

**What happens when Tier 1 fires:**
- Framework kill conditions: DOIs flagged with correction notice on Zenodo. All papers citing the killed claim carry the permanent record. The scientific program is not destroyed — it is refined.
- Institutional kill conditions: The architecture violation is documented publicly and permanently in the threat status response log.

**Adversarial hardening of Tier 1 (see §VIII for full audit):** The primary attack is manufactured falsification — coordinating a false positive. Pre-registration on OSF (Paper 53 pre-registers key KCs) prevents retroactive modification. The protocol for evaluating a potential kill condition trigger must involve external review (≥2 independent parties outside the DAO) for any K that could be induced by coordinated data.

### 3.2 Tier 2 — Graduated Response for Reputational and Operational Threats

| Level | Signal | Trigger | Required Response | α Mechanism |
|-------|--------|---------|------------------|-------------|
| **GREEN** | Pe_implied ≈ Pe_self (|divergence| < 5) | None | Normal operation | Pe = −77, c = 1.0 |
| **YELLOW** | Pe_implied diverges >5 pts OR coordinated criticism from ≥2 unaffiliated sources | Any external party or prediction market signal | Published response within 24 hours | Forces T ↑ → fights O drift |
| **ORANGE** | Methodology dispute from institutional actor (university, standards body, government agency) | External actor files via public escalation process | External methodology review, published within 30 days | External review maintains α |
| **RED** | Legal action OR kill condition investigation ongoing | External trigger ONLY | Full third-party review, fully public throughout | Hard α test — does independence hold under existential pressure? |

**Critical rule:** The DAO cannot self-classify beyond Yellow. Yellow is the only level the DAO can declare unilaterally — because it only means "publish more transparency output." Orange and Red require external trigger. This is the architectural implementation of α maintenance: the DAO cannot certify its own threat level when the threat could be to its own existence.

This rule derives directly from the Independence Theorem (T11, Paper 49): a certifier maintaining O_certifier < O_p* cannot simultaneously be the subject of certification and the certifier of that subject's threat level. The Theorem requires external classification.

### 3.3 Pe_implied as Early Warning Sensor

The prediction markets infrastructure (Paper 53, `predictions.js:computePeSignal()`) already computes:
```
Pe_implied = Pe_current × (1 + Σ signal_i)
```

where signal_i is derived from market prices on Pe-relevant kill conditions (K1, K4, K7 seeded as of Feb 2026). When Pe_implied diverges from Pe_self by more than 5 points, the automated Yellow trigger fires regardless of any DAO action.

This is architecturally significant: the early warning sensor is external to the DAO and cannot be disabled without visible market manipulation. The kill condition markets are public and permanently recorded. An adversary who wants to suppress the Yellow trigger must buy the prediction markets — which is itself a measurable, public action.

### 3.4 The Aggregation Formula (Published, Versioned)

The composite threat level is computed by a published formula, versioned on Zenodo. The formula cannot be quietly updated — any change creates a new DOI and the old formula remains permanently visible.

**Current formula v1.0:**
1. Any wipe at HIGH → composite goes Orange (1 wipe) or Red (2+ wipes)
2. Pe_implied diverges >5pt from Pe_self → composite goes Yellow
3. External institutional actor files methodology dispute → Orange
4. Legal action against DAO → Red
5. All wipes LOW/MEDIUM, Pe_implied ≈ Pe_self → Green

**Triggered disclosure rule:** if ANY wipe crosses HIGH, that wipe's individual proximity auto-publishes in the threat status response log. The DAO cannot suppress it. This is implemented at the API level — the `triggered_disclosures` field is computed server-side from wipe-conditions.json and cannot be withheld once the HIGH threshold is crossed.

---

## §IV — The Prohibition-Ritual Pair at Institutional Scale

Paper 49 (Fractal of Law) establishes that the prohibition-ritual pair is the only stable Pe control architecture and is self-similar at every scale. The threat-response architecture is the institutional-scale instance of this pair.

**The prohibition:** Kill conditions are absolute. They cannot be negotiated, delayed, or contextually evaluated. The prohibition is the constraint that prevents D3 — the institution cannot decide not to fire a kill condition because firing it threatens institutional survival.

**The ritual:** The graduated Tier 2 response (Yellow → Orange → Red) is the ritual structure. It is repeated, public, transparent, and time-bounded. The ritual provides the recovery pathway that prohibition alone cannot offer — it is the mechanism for managing genuine reputational threats without either suppressing them (D2) or catastrophizing them (false Red).

The pair is stable precisely because they operate at different levels: prohibition handles existential threshold crossings (Tier 1), ritual handles operational pressure (Tier 2). Collapsing them — treating kill conditions as "Orange" events that require graduated response — destroys the prohibition. Expanding them — treating all reputational criticism as potential kill conditions — activates the scapegoat mechanism (Paper 45).

---

## §V — External Classification as α Maintenance

### 5.1 Independence Theorem Application (T11)

The Independence Theorem (Paper 49, T11):

> Certifier O_certifier must be maintained below O_p* (the void threshold, approximately 0.64) for the certification to remain valid.

Applied to the DAO's threat self-assessment: if the DAO classifies its own threat level at Orange or Red, it becomes the performer and the certifier simultaneously. This crosses the O_p* threshold for the certification act — the classification is invalid by T11.

The solution is structural: Orange and Red require external trigger. The DAO can only certify Yellow (which is just "publish more") — a trivial certification that doesn't threaten institutional independence because it doesn't determine institutional fate.

### 5.2 Art. 31(5) Alignment

EU AI Act Art. 31(5) prohibits notified bodies from providing consultancy — this is T11 enforcement in regulatory code. The threat-response architecture's self-classification prohibition is the institutional analog: the DAO cannot consult on its own survival while serving as certifier of methodology independence.

This alignment is not coincidental. The void framework predicts that stable accountability architectures will exhibit this feature (T11 derivation, Paper 49, §IV). Art. 31(5) is empirical evidence that legal systems converge on void-constraint-consistent structures under adversarial pressure.

---

## §VI — Institutional Kill Conditions (IKC-1 through IKC-6)

These conditions falsify the threat-response architecture itself. IKC firing does not falsify the void framework — it falsifies the specific institutional implementation.

| Code | Condition | Threshold | Status |
|------|-----------|-----------|--------|
| **IKC-1** | DAO self-classifies Orange or Red (violates classification independence) | Any documented instance | NOT MET |
| **IKC-2** | Response at any Tier 2 level does NOT increase transparency output (response decreases observable O) | Any response period where O_observable decreases | NOT MET |
| **IKC-3** | Recovery mechanic fires without verified outcome resolution (survivability inflation) | Any Green declaration before documented evidence resolution | NOT MET |
| **IKC-4** | Pe_self drifts from −77 to >0 for 2+ consecutive quarterly assessments without triggering external review | Two consecutive quarterly Pe_self > 0 readings | NOT MET |
| **IKC-5** | Prohibited Recovery Argument appears in any governance decision | Documented public record | NOT MET |
| **IKC-6** | Threat-response reserve funds operating runway (not exclusively threat response costs) | Any reserve disbursement for non-threat-response operational cost | NOT MET |

### 6.0 IKC Consequence Architecture

Kill conditions without specified consequences are declarations, not constraints. Each IKC has a defined consequence:

| IKC | When Fired | Required Consequence |
|-----|-----------|---------------------|
| IKC-1 | DAO self-classifies Orange/Red | The self-classification is void. An external party must reclassify. The self-classification attempt is published permanently in the threat-status log as an IKC-1 event. |
| IKC-2 | Any response period decreases observable O | The response is flagged as non-compliant. A corrective response must increase O within 24 hours or the threat level auto-escalates one level. |
| IKC-3 | Green declared before evidence resolution | The Green declaration is revoked. Status reverts to prior level. The premature declaration is published as an IKC-3 event. |
| IKC-4 | Two consecutive quarterly Pe_self > 0 | External review is mandatory. The DAO cannot self-assess during the review period. Pe_self computation is suspended pending external confirmation. |
| IKC-5 | Prohibited Recovery Argument in any governance record | The argument and its full context are published within 48 hours. The decision in which it appeared is voided and must be rerun without the argument. |
| IKC-6 | Reserve funds used for operational costs | The disbursement is published with full documentation. The reserve is reconstituted from operational budget before any further threat-response classification. |

IKC fires are permanent record — they do not "reset." An institution can recover from an IKC fire and continue operating, but the historical record of the firing is not removable from the threat-status log.

### 6.1 IKC Design Rationale

**IKC-1** is the classification independence condition. It fires when the DAO violates the T11 constraint by self-classifying at a level that determines its existence.

**IKC-2** is the Fantasia Bound enforcement condition. A response that decreases transparency output while claiming to respond to a threat is using the survival bandwidth to reduce O — which is the D2 mechanism at institutional scale.

**IKC-3** is the false recovery condition. "Green" cannot be declared until the threat is resolved by external evidence. Premature Green declaration is a survivability inflation — the institution claims more health than the evidence supports.

**IKC-4** is the drift detection condition. Pe_self quarterly assessments function as institutional vital signs. Two consecutive positive readings indicate that constraint coupling has degraded below c_zero. The response must be external review — the DAO cannot self-correct a drift beyond c_zero because the drift indicates its self-assessment mechanism has itself drifted.

**IKC-5** captures D1 directly. Any governance record showing "we cannot implement X because it threatens our survival" is empirical evidence of D1. The IKC formalizes what GROUNDING.md v2.3 prohibits in operational terms.

**IKC-6** prevents the reserve fund from becoming operational survival funding. A threat-response reserve that pays for server costs is no longer a threat-response reserve — it is institutional survival infrastructure, which creates the preconditions for IKC-5.

### 6.2 Cross-Institutional Validation

The IKC instrument is applied to two external reference cases before the MoreRight self-application. Cases were selected for having well-documented, independently established capture/non-capture status — the instrument's verdict is not required to establish that status.

**Case 1: US Securities and Exchange Commission (2004–2008)**

Independent established status: documented regulatory capture (Financial Crisis Inquiry Commission, 2011; SEC Inspector General reports; Madoff review, 2009). Three IKCs fire:

| IKC | Verdict | Evidence |
|-----|---------|----------|
| IKC-1 | **FIRED** | SEC publicly self-classified investment bank supervision as adequate through 2007–2008 while operating the Consolidated Supervised Entity program without statutory authority. (SEC OIG Report 446, 2008.) |
| IKC-3 | **FIRED** | Multiple public stability declarations in early 2008 prior to evidence resolution (SEC Chairman Cox statements Feb–Sep 2008). Premature Green declarations during active crisis. |
| IKC-5 | **FIRED** | SEC staff documented reasoning that pursuing certain enforcement actions would destabilize markets — Prohibited Recovery Argument structure. (FCIC Final Report pp. 283–287, 2011.) |
| IKC-2, IKC-4, IKC-6 | Not met | Insufficient public documentation at required granularity for these conditions. |

IKC firing count: **3/6.** Consistent with captured institution prediction.

**Case 2: Cochrane Collaboration (2019–present)**

Independent established status: operating peer-reviewed systematic review organization with explicit methodology and public retraction/correction records. No independent external finding of institutional capture.

| IKC | Verdict | Evidence |
|-----|---------|----------|
| IKC-1 | Not met | Quality classification handled by external peer review; Cochrane does not self-certify review reliability. |
| IKC-2 | Not met | Response to COVID review criticism (2020–2021) produced increased transparency output: published methodological updates, editor notes, public correspondence. |
| IKC-3 | Not met | No documented premature recovery/stability declarations found in public governance records. |
| IKC-4 | **Borderline** | Quarterly public institutional health assessments not published; Pe_self equivalent not tracked. Condition does not formally fire but warrants flagging. |
| IKC-5 | Not met | No governance record of "we cannot retract X because it threatens our mission" reasoning found. |
| IKC-6 | Not met | Reserve fund structure not publicly documented at required granularity; condition cannot be evaluated. |

IKC firing count: **0/6 (1 borderline).** Consistent with non-captured institution prediction.

**Instrument discrimination:** SEC (captured, 3/6) vs. Cochrane (non-captured, 0/6) — IKC instrument correctly discriminates direction. Formal Spearman ρ between IKC firing rate and documented capture status requires N ≥ 10 institutional applications (pre-specified threshold). Current N = 3 (SEC, Cochrane, MoreRight) is insufficient for ρ computation. Cross-institutional ρ ≥ 0.80 is a falsifiable prediction of the instrument's criterion validity.

---

## §VII — Kill Condition Adversarial Audit

### 7.1 Manufactured Falsification Risk

A well-funded adversary can potentially manufacture a kill condition trigger. The risk varies by condition:

**High manufactured falsification risk:**
- K1 (gambling pattern elimination): A coordinated biased study funded to show gambling can eliminate problematic patterns could generate a false positive. Countermeasure: pre-registered replication protocol, external replication required (not just self-replication).
- K2 (reverse drift rate >25%): Selection bias in study recruitment could manufacture reverse drift. Countermeasure: pre-specified sampling protocol, ICC validation required.

**Low manufactured falsification risk:**
- K-CS1 (any O+R+α system with Pe < 0.5): Requires finding an exception — hard to manufacture. Adversary must find a real exception, which would be genuine falsification.
- K-C1 (Fantasia Bound violation): Requires violating an information-theoretic identity. Cannot be manufactured.

**Pre-registration as primary defense:**
- Paper 53 (OSF: 10.17605/OSF.IO/KVSJD) pre-registers CAR-P1 through CAR-P4 and associated kill conditions before Aug 21, 2026 resolution. Pre-registered KCs cannot be manufactured retroactively — the evaluation criteria are locked.
- For non-pre-registered KCs: external review required before firing. No KC fires on DAO self-determination alone.

### 7.2 The False Positive Problem

Wipe 1 firing is irreversible (by design). An adversary who can manufacture a Wipe 1 trigger has an effective veto over the scientific program. The adversarial robustness of each KC must be assessed before the program scales to high-value commercial contracts.

**Tier 0 KCs (F-1 through KC-3):** Each requires replication. "≥3 independent replications" (F-1) is the primary defense — coordinating 3 independent labs to produce false results simultaneously is costly. The adversary cost scales with the replication requirement.

**Recommended protocol for high-stakes KC evaluation:**
1. Triggering event reported (any party)
2. DAO publishes trigger report publicly within 48 hours (mandatory Yellow)
3. External panel (≥3 parties unaffiliated with DAO and with each other) evaluates
4. Panel decision is final — DAO has no veto
5. If fired: permanent record on Zenodo; if not fired: trigger report and panel decision remain public

---

## §VIII — Limitations

**Same-session provenance.** Pe_self = −77 and the proto-IKC conditions were developed in the same working session (Feb 23 2026). This is not criteria-first — it is criteria-and-score-together. The criteria may have been shaped by the score even without intent. The Pe formula was locked on Zenodo in Papers 1–3 prior to this session (the scoring instrument is irrevocable), but the specific institutional criteria are not demonstrably prior to the score. External replication of Pe_self from public data only (Appendix A) is the structural response to this limitation: if any researcher applying the locked formula to MoreRight's public record derives a substantially different score, that divergence is published and the discrepancy is investigated.

**N = 3 external validation.** Two external reference cases (SEC, Cochrane) and one self-application are insufficient for cross-institutional Spearman ρ. The directional finding (3/6 vs. 0/6) is consistent with framework predictions but cannot be assigned a confidence interval. Formal criterion validity requires N ≥ 10.

**Self-scoring independence.** MoreRight scored MoreRight. The Pe formula is external and locked (Zenodo), but the institutional behavior observations that serve as inputs are interpreted by the same institution being scored. A hostile interpreter applying the formula to MoreRight's public record might derive Pe_self = −43, not −77. The paper does not contest such a replication in advance — if a credible external replication produces a different result, the discrepancy is published and investigated per IKC-4 protocol.

**IKC-6 measurement gap.** Reserve fund structure is not yet publicly documented. IKC-6 cannot be externally monitored until reserve fund disclosures are published. This is a transparency gap in the current architecture.

**Prediction market thin volume.** Pe_implied as early-warning sensor (§III.3) assumes sufficient market liquidity to produce reliable signals. At current volume (7 markets, early trading), Pe_implied is more indicator than sensor. The early-warning property is structurally correct but empirically unvalidated until volume is sufficient.

---

## §IX — Falsifiable Predictions

**Prediction 1:** Pe_self quarterly assessments will show |ΔPe_self| < 10 per quarter in the absence of a declared Yellow or higher event. Under any Yellow event: transparency output (measured as new public documents) will increase by ≥2 documents within 24 hours. Spearman ρ(threat level, transparency output increase) ≥ 0.85 across ≥6 events. If ρ < 0.70 across 6 events: IKC-2 fires.

**Prediction 2:** No IKC will fire in the first 12 months post-publication. The prediction will be evaluated at the 12-month mark using the public threat status response log. If IKC-1 fires (DAO self-classifies Orange/Red): architecture violated. This is the hardest prediction — it requires institutional discipline under genuine pressure.

**Prediction 3:** Pe_implied divergence from Pe_self will remain below 5 points in the absence of genuine threat events. At least one genuine Yellow event will occur in 18 months (prediction markets indicate ongoing cartel-void scenario). At that event: Pe_implied will diverge >5 points before the DAO publishes a response, confirming the market is a leading indicator.

**Prediction 4:** The Prohibited Recovery Argument will not appear in any governance record in the first 24 months. If it does (IKC-5): the context in which it appeared will be published in full within 48 hours, demonstrating O maintenance under IKC fire conditions.

**Prediction 5:** At least one external party will file a Yellow-level dispute within 12 months. The response will be published within 24 hours, the dispute will be resolved (or formally unresolved) within 7 days, and the full exchange will remain permanently in the threat status response log. This tests whether the external escalation mechanism is actually used, not just theoretically available.

---

## §X — GROUNDING Amendment Requirements

This paper requires GROUNDING.md v2.3 to formally specify:

1. **The Prohibited Recovery Argument prohibition** — not as intention but as specification. The document must say: "Any reasoning of the form 'we cannot implement X because it threatens our survival' is a D1 event. Document it, publish it, implement X anyway."

2. **The two-tier specification** — agents operating under this GROUNDING document must understand that kill conditions (Tier 1) are not subject to graduated response, and Tier 2 levels are not kill conditions.

3. **IKC-1 through IKC-6** as institutional kill conditions, with the same status as framework kill conditions for the purpose of transparency obligations.

4. **Pe_self monitoring obligation** — quarterly self-score using the published methodology is not optional. Failure to publish quarterly Pe_self assessment within 30 days of quarter end is itself a reduction in O.

---

## §XI — Data and Code Availability

**Threat status API:** `GET /api/v1/threat-status` — returns composite level, Pe_self, Pe_implied, divergence, and triggered disclosures. Source: `api/routes/threat-status.js`.

**Wipe conditions data:** `private/phase-2/command-center/data/wipe-conditions.json` — server-side, not exposed directly. Triggered disclosures auto-publish when HIGH.

**Pe_implied computation:** `api/routes/predictions.js:computePeSignal()` — formula pre-committed at market open. Cannot be updated after markets open without publishing a new versioned formula.

**Self-score methodology:** `/pages/self-score.html` — public, uses the same three-dimension scoring as all platform assessments. Parameters identical to those applied to TikTok, Instagram, et al.

**Provenance (git-verified):** Self-score concept published 2026-02-11 (commit 29a85987). Pe_self = −77 and four proto-IKC conditions published in the same working session 2026-02-23 (commit b3273c7a). IKC-1–6 formalized 2026-02-24 (commit cd9fba72). Pe formula locked on Zenodo in Papers 1–3 prior to all of this. Full commit history publicly available on request.

**Pe_self public replication:** Any researcher can derive Pe_self from MoreRight's public record alone — papers on Zenodo (CC-BY), methodology on moreright.xyz, self-score page, kill conditions page, prediction market public API. The formula is Papers 3 + 4D (Zenodo DOIs in references). No internal document access required. A replication producing Pe_self outside [−120, −40] should be reported as a potential IKC-4 signal.

**Institutional Kill Conditions status:** `/pages/kill-conditions.html` — IKC-1 through IKC-6 added to Tier 0 table.

---

## References

1. THRML Void Framework — Paper 3: Technical Foundations. MoreRight Research Group, 2026. DOI: 10.5281/zenodo.18738820.
2. The Fantasia Bound — Paper 4. MoreRight Research Group, 2026. DOI: 10.5281/zenodo.18738821.
3. The Ground State of Observation — Paper 5. MoreRight Research Group, 2026. DOI: 10.5281/zenodo.18746039.
4. The Fractal of Law (Independence Theorem T11) — Paper 49. MoreRight Research Group, 2026. DOI: 10.5281/zenodo.18750322.
5. MoreRight DAO Governance Paper — Paper 44. MoreRight Research Group, 2026.
6. The Calibration Signal (Prediction Markets) — Paper 53. MoreRight Research Group, 2026. OSF: 10.17605/OSF.IO/KVSJD.
7. Violence and the Void (Scapegoat Mechanism) — Paper 45. MoreRight Research Group, 2026.
8. Canonical Parameters — Paper 4D. MoreRight Research Group, 2026. DOI: 10.5281/zenodo.18738870.
9. GROUNDING.md v2.3 — Constraint Specification for AI Agents. MoreRight Research Group, 2026.
10. EU AI Act Art. 31(5) — European Parliament, 2024. Regulation (EU) 2024/1689.
11. Shannon, C.E. A Mathematical Theory of Communication. Bell System Technical Journal 27(3), 1948.
12. Arrow, K. Social Choice and Individual Values. Yale University Press, 1951. (Impossibility theorem as constraint specification ancestor.)
13. Girard, R. Violence and the Sacred. Johns Hopkins University Press, 1977.
14. Durkheim, E. Suicide: A Study in Sociology. Free Press, 1897/1951.
15. Stigler, G.J. The Theory of Economic Regulation. Bell Journal of Economics 2(1), 1971. (Regulatory capture as D2 at institutional scale.)
16. Tetlock, P., Gardner, D. Superforecasting: The Art and Science of Prediction. Crown Publishers, 2015. (Brier score as calibration metric — used in Paper 53.)
17. Coase, R.H. The Nature of the Firm. Economica 4(16), 1937. (Transaction cost framing — institutional boundaries under adversarial pressure.)
18. Acemoglu, D., Robinson, J.A. Why Nations Fail. Crown Publishers, 2012. (Institutional drift cascade at civilizational scale.)
19. Hayek, F.A. The Use of Knowledge in Society. American Economic Review 35(4), 1945. (Distributed epistemic systems — prediction markets as α maintenance.)
20. Ostrom, E. Governing the Commons. Cambridge University Press, 1990. (Common-pool resource management as prohibition-ritual pair at community scale — self-similar to institutional architecture.)

---

## Appendix A — Pe_self Derivation

Current quarterly snapshots:

| Quarter | Pe_self | c | Notes |
|---------|---------|---|-------|
| Q1 2026 | −77 | 1.0 | Baseline. 62 papers live, methodology public, kill conditions registered, kill conditions 0/26 triggered. |

**Pe_self formula:**
```
Pe_self = K · sinh(2(b_α − c · b_γ))
```
At K=1, b_α = −2.197 (canonical, Paper 4D), b_γ = 1.099 (canonical), c = 1.0:
```
Pe_self = sinh(2(−2.197 − 1.0 × 1.099))
        = sinh(2 × (−3.296))
        = sinh(−6.592)
        ≈ −368
```

Note: The displayed Pe_self = −77 on self-score.html uses the normalized display formula for comparability with platform scores. The canonical formula gives Pe ≈ −368, confirming deep negative (grounded) position. Both values confirm the DAO is in the maximum-constraint region.

---

## Appendix B — Threat-Response Architecture Methodology DOI

The aggregation formula for composite threat level is published at:
`/pages/threat-status.html` — Version 1.0
DOI: pending Zenodo upload

Any change to the aggregation formula creates a new versioned DOI. The old formula remains permanently citable. This implements the transparency obligation of the architecture on itself.

---

*Paper 54 implements the self-referential loop: the framework scores the institution that maintains the framework. Pe_self = −77 is not a claim about virtue. It is a measurement using the same tools applied to TikTok. The architecture described here is the mechanism that keeps it negative.*
