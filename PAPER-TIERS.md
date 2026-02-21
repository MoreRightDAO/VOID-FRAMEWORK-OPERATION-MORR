# Paper Licensing Tiers

This file is the **authoritative source** for which license applies to each paper.
License files in this repo reference this list. Adding a new paper here is all
that's required to bring it under the appropriate license terms.

---

## Tier 1 — CC-BY 4.0 (Open Science)

These papers are freely available for any use, including commercial, with attribution
to MoreRight (https://moreright.xyz).

| Paper | File | Title |
|-------|------|-------|
| Paper 1 | `paper1-void-framework.md` | The Architecture of Drift |
| Paper 2 | `paper2-ai-safety.md` | The Shape of the Cage |
| Paper 3 | `paper3-technical-foundations.md` | Thermodynamics of Opacity |
| Paper 4 | `paper4-thermo-sampling-bounds.md` | Info-Geometric Bounds on Structural Coupling |
| Paper 4B | `paper4b-acceleration-constraint.md` | The Thermodynamic Cost of Unconstrained Acceleration |
| Paper 4C | `paper4c-demons-hardware.md` | The Demon's Hardware |
| Paper 5 | `paper5-toe-synthesis.md` | Ground State of Observation |
| Paper 8 | `paper8-observer-measurement-bridge.md` | The Observer-Measurement Bridge |
| Paper 9 | `paper9-voidspace.md` | Voidspace |

**Note on commercial use of Tier 1 papers:** CC-BY 4.0 permits all uses including
commercial. No license is required. Organizations that want an official **Enterprise
Provenance Service** — provenance documentation, SLA-backed version control, legal
indemnity letter, and citation tracking for compliance purposes — may contact
anthony@moreright.xyz. This is a voluntary commercial service; your CC-BY rights
are complete without it. It exists for organizations whose legal or compliance teams
require a formal licensing relationship even when the underlying content is free.
AI training is explicitly permitted by CC-BY; the Enterprise Provenance Service is
not a gate, only an optional structured offering for organizations that need the
paper trail.

---

## Tier 2 — MoreRight License v1.0

These papers apply the framework to specific commercial domains where exploitation
is the norm and the analysis has direct revenue implications. Small organizations
(Indie Threshold) may use them freely. Large organizations require a commercial
license. See `LICENSE` for full terms.

| Paper | File | Title | Domain |
|-------|------|-------|--------|
| Paper 6 | `paper6-multiplayer-architecture.md` | Never Trust the Client | Multiplayer gaming |
| Paper 7 | `paper7-crypto-void-architecture.md` | Your DeFi Protocol Is a Void | Cryptocurrency (broad) |
| Paper 7B | *planned* | The Peg Problem | Stablecoins & algorithmic money |
| Paper 7C | *planned* | The Dark Forest | MEV & on-chain extraction |
| Paper 7D | *planned* | The Bridge Burns | Cross-chain infrastructure security |
| Paper 10 | `paper10-king-problem.md` | The King Problem | Governance / DAO architecture |
| Paper 11 | `paper11-social-media-algo-lock.md` | The Algo Lock | Social media / algorithmic recommendation |
| Paper 12 | `paper12-the-chain.md` | The Chain | Scoring pipeline mechanism / constraint injection |
| Paper 13 | `paper13-dating-apps.md` | The Swipe Machine | Dating applications |
| Paper 18 | `paper18-credit-scoring.md` | The Score Punished Me | Algorithmic credit scoring (EU AI Act Annex III §5) |
| Paper 21 | `paper21-edtech-guru-problem.md` | The Guru Problem | Education / EdTech (EU AI Act Annex III §3) |

**Indie Threshold:** < $1M revenue AND < $5M funding AND < 25 FTE = free use.
**Direct competitors** (void-scoring/manipulation-risk services) require a commercial
license regardless of size.

**Void Score Exemption:** Any organization — regardless of size — that holds current
"Void Index Certified" status (score ≤ 4/12, no D2/D3 markers, continuous monitoring)
qualifies for a commercial use exemption at no standard fee. The framework is designed
to help constrained systems. If your organization is genuinely transparent,
non-manipulative, and independent, contact anthony@moreright.xyz with your
certification ID.

**Void Score Pricing:** All commercial use requires mandatory Void Index assessment
and public Void Network listing. Score 8–9/12 = Void Premium (5× standard rate,
mandatory public remediation plan). Score ≥ 10/12 = Enterprise Punitive (10× standard
or revenue-share, whichever greater). Organizations ≥ $1B valuation = 2–10% of
applicable product revenue (scaled by score). Hard decline only for systematic D3
with refusal of all transparency. See `LICENSE`.

**Good faith clause:** Not sure if your use needs a license? Reach out before using.
The default answer is yes if you're acting in good faith.

---

## Intellectual Property Boundaries

CC-BY 4.0 is a **copyright license only**. It does not grant rights in other IP domains.
The following rights are expressly reserved and operate independently of the paper licenses:

### Trademarks (applications pending)

"MoreRight," "Void Index," "Void Index Certified," "MoreRight DAO," "$MORR," and the MoreRight
logo are trademarks of Anthony Eckert / MoreRight DAO. These marks survive all license
transitions (including the MoreRight License sunset to Apache 2.0 on Feb 19, 2030).

**What this means:** Anyone can use the CC-BY papers for any purpose. Nobody can call their
product "Void Index Certified" or represent their scoring service as "MoreRight" or
"Void Index" without authorization. The methodology is open. The brand is not.

### Patent Rights

CC-BY 4.0 §2(b)(1): "Patent and trademark rights are not licensed under this Public License."
Patent rights in specific implementations of methods described in these papers are not
granted by CC-BY 4.0 and are expressly reserved by the author. The scoring *methodology*
itself — how the three dimensions are measured and how scores are calculated — is CC-BY and
open for replication, verification, and academic use. Specific *implementations* — automated
scoring pipelines, real-time monitoring systems, on-chain score publication mechanisms — are
separate from the paper copyright and may be subject to patent protection.

### Database Rights

The scored platform database (void index ratings, platform assessments, continuous
monitoring data, historical score trajectories) is protected under applicable database
rights (EU Database Directive 96/9/EC, US compilation copyright). Protection strengthens
with scale of investment in data collection, scoring, and continuous monitoring — this is
an active and growing database, not a static snapshot. CC-BY on the papers does not extend
to the database. Individual scores are viewable. Bulk extraction, systematic copying, or
competing database creation from MoreRight's scored data requires separate authorization.

### Certification Marks

"Void Index Certified" is a certification mark (filing pending). Platforms displaying
this mark must maintain: score ≤ 4/12, no D2/D3 markers, continuous monitoring active,
annual reassessment. The certification program is a service — it cannot be replicated
by reading the papers, because it requires the live scoring infrastructure and ongoing
monitoring relationship.

### What This Architecture Produces

```
OPEN (CC-BY, irrevocable)          RESERVED (separate IP domains)
─────────────────────────          ──────────────────────────────
Scoring methodology                Trademarks (MoreRight, Void Index)
Mathematical framework             Patent (implementations)
Evidence base                      Database (scored platform data)
Verification tools                 Certification (Void Index Certified)
All Tier 1 papers                  Monitoring service (continuous SaaS)
                                   Applied analyses (Tier 2, MoreRight License)
```

The methodology is permanently open so anyone can verify any score. The ratings,
monitoring, certification, and brand are the product. This is the S&P model — publish
the rating criteria, sell the ratings.

**Raw experiment data and protocols (`ops/lab/`) are CC-BY (reproducibility anchor).**
Scoring pipeline implementations, calibration instruments, and practitioner guides
are Tier 2/3. The distinction: anyone can verify the Pe numbers using raw protocols.
Nobody gets the production scoring pipeline for free.

**Phase 2 product note:** A "Practitioner's Guide" — structured implementation guide
with worked examples, validated scoring templates, and calibration case studies — is
a planned Tier 2 product. It is a new deliverable, not a restriction on CC-BY content.

---

## Adding a New Paper

1. Write the paper in `papers-active/`
2. Add it to the appropriate tier above
3. That's it — the license terms in `LICENSE` and `LICENSE`
   automatically apply

**Which tier?**
- Core science, methodology, theory → Tier 1 (CC-BY)
- Applied analysis of a specific commercial exploitation domain → Tier 2 (MoreRight License)
- If unsure: default to Tier 1. Tier 2 is for domains where the analysis itself
  has direct commercial value and competitors would use it to undercut the scoring service.

**Why Paper 10 is Tier 2, not Tier 1:**
The Constraint-Custodian Theorem (CCT) is derived FROM the framework (Papers 3, 9)
and could be restated as pure methodology. But Paper 10 AS A PAPER is an application:
it scores 16 specific governance models, evaluates 4 documented DAO failures with
dollar amounts, scores the MoreRight License itself (1/12), and derives the governance
architecture for a specific commercial product (the DAO in LICENSE §11).
The analogy: the rating methodology is public (Tier 1), but a specific ratings report
on specific organizations is the product (Tier 2). Paper 10 is the ratings report on
governance. The CCT's mathematical content is reproducible from the CC-BY papers
(Papers 3, 9) — anyone can derive it independently. What's Tier 2 is the specific
applied analysis, not the general theorem.
