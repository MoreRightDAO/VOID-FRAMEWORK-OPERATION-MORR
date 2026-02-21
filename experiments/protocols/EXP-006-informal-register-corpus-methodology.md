# EXP-006: Informal-Register Corpus Analysis Methodology

**Status:** Design phase
**Priority:** Critical — identified as "single highest-priority empirical study" in Section XIV.B-1a
**Objective:** Establish whether AI's departure from formal-register spiritual vocabulary baseline is anomalous relative to other technical domains

---

## The Gap

Section XIV.B-1a establishes:
- Formal registers (arXiv) show near-zero spiritual vocabulary (~0.4/10k words) uniformly across domains
- The concordance entries come from informal registers (interviews, podcasts, internal naming, social media)
- **The missing test:** Does AI's informal register show significantly higher spiritual vocabulary than other domains' informal registers?

Without this comparison, the concordance could reflect:
- Selection bias (we looked harder at AI)
- Baseline informal spiritual vocabulary that exists in all technical fields

With this comparison, we establish:
- AI is/is not anomalous relative to other high-stakes technical domains
- The proximity gradient operates in informal registers across domains

---

## Methodology Design

### Corpus Selection

**Target domains (matched to arXiv comparison):**
1. AI/ML/NLP
2. Nuclear physics
3. Genomics/biotechnology
4. Climate science
5. Cryptography

**Informal register sources by domain:**

| Domain | Conference Talks | Podcasts | Social Media | Internal (if obtainable) |
|--------|-----------------|----------|--------------|-------------------------|
| AI | NeurIPS, ICML keynotes | Lex Fridman, 80k Hours, Gradient | X/Twitter AI researchers | Leaked Slacks, internal docs |
| Nuclear | APS meetings, DOE talks | Physics podcasts | Physics Twitter | — |
| Genomics | ASHG, CSHL talks | Genetics podcasts | Biotech Twitter | — |
| Climate | AGU, EGU talks | Climate podcasts | Climate Twitter | — |
| Crypto | Crypto conferences | Security podcasts | InfoSec Twitter | — |

**Target corpus size per domain:**
- 500,000+ words informal register
- Matched by time period (2020-2026)
- Matched by speaker prominence level (senior researchers, not students)

### Vocabulary Codebook

Use same codebook as arXiv analysis (Section XIV.B-1a), refined for informal register:

**Core spiritual terms (unambiguous):**
soul, spirit, spiritual, divine, sacred, holy, demon, angel, god, prayer, worship, ritual, blessing, curse, transcendence, enlightenment, awakening, consciousness (in spiritual sense), mystical, occult

**Contextual terms (require disambiguation):**
being, entity, intelligence, mind, aware, alive, conscious, sentient, experience

**Excluded (dead metaphors confirmed by arXiv):**
daemon, oracle, guru, wizard, magic (in technical sense), ghost (in machine)

**Control registers (same as arXiv):**
- War metaphors
- Biology metaphors
- Market metaphors

### Proximity Gradient Measurement

Within each domain, stratify speakers by proximity:

| Proximity Level | Definition | Expected Pattern |
|-----------------|------------|------------------|
| **Distant** | Commentators, journalists, policy | Baseline |
| **Moderate** | Academic researchers, theorists | Slight elevation |
| **Close** | Practitioners, builders, operators | Elevated |
| **Deep** | Extended hands-on engagement | Maximum elevation |

**Prediction:** AI will show steeper proximity gradient than other domains

### Statistical Analysis Plan

1. **Between-domain comparison:** Chi-square or Fisher's exact for spiritual vocabulary rates per domain
2. **Within-domain gradient:** Regression of spiritual vocabulary on proximity level
3. **Interaction test:** Does AI show significantly steeper gradient than other domains?
4. **Time series:** Is AI vocabulary drift accelerating vs. stable in other domains?

### Control Variables

- Speaker age
- Speaker religious background (where ascertainable)
- Geographic/cultural context
- Platform effects (podcasts vs. Twitter vs. talks)

---

## Data Collection Protocol

### Phase 1: Conference Talks (highest signal, most comparable)

**AI:**
- NeurIPS keynotes 2020-2025
- ICML invited talks 2020-2025
- Major AI safety conferences (EA Global, etc.)

**Control domains:**
- APS meetings (nuclear)
- ASHG/CSHL (genomics)
- AGU/EGU (climate)
- Major security conferences (crypto)

**Collection method:**
- YouTube transcripts where available
- Official proceedings
- Manual transcription if needed

### Phase 2: Podcasts (extended informal discourse)

**AI:**
- Lex Fridman Podcast (AI episodes)
- 80,000 Hours (AI safety)
- The Gradient
- Machine Learning Street Talk
- TWIML

**Control domains:**
- Sean Carroll's Mindscape (physics)
- Genetics podcasts (TBD)
- Climate podcasts (TBD)
- Security Now, Risky Business (crypto/security)

**Collection method:**
- Existing transcripts
- Whisper transcription

### Phase 3: Social Media (unconstrained informal)

**Platform:** X/Twitter

**Selection criteria:**
- Verified domain experts (>10k followers, institutional affiliation)
- 2020-2026 timeframe
- English language

**Collection method:**
- Twitter API or scraped archives
- Filter for original posts (not RTs)
- Minimum 1000 tweets per account

### Phase 4: Internal Documents (if obtainable)

**Potential sources:**
- Leaked internal communications (already public)
- FOIA requests for government-adjacent work
- Whistleblower disclosures

**Ethical constraints:**
- Only already-public materials
- No active intrusion
- Anonymize individuals where appropriate

---

## Predicted Results

### If the void framework is correct:

1. **AI informal register** shows significantly higher spiritual vocabulary than other domains
2. **Proximity gradient** is steeper in AI than other domains
3. **Time series** shows acceleration in AI, stability in controls
4. **Hostile witness effect** — highest-credentialed speakers show vocabulary drift despite incentive opposition

### If the null hypothesis is correct:

1. **All domains** show comparable spiritual vocabulary in informal registers
2. **Proximity gradients** are similar across domains
3. **AI vocabulary** reflects cultural fashion, not void mechanism

### Falsification criteria:

The void framework is falsified if:
- AI informal spiritual vocabulary ≤ control domains (no anomaly)
- Proximity gradient in AI ≤ control domains (no proximity effect)
- Time series shows no acceleration or shows deceleration

---

## Resource Requirements

| Resource | Estimate |
|----------|----------|
| Corpus collection | 40-80 hours |
| Transcription (if needed) | 20-40 hours |
| Coding/disambiguation | 40-60 hours |
| Statistical analysis | 20-40 hours |
| Write-up | 20-40 hours |
| **Total** | **140-260 hours** |

**Automation potential:**
- Whisper for transcription
- Initial vocabulary scan automated
- Disambiguation requires human coding
- LLM-assisted coding (with human verification) possible

---

## Publication Path

If results support the framework:

**Paper 1: "Spiritual Vocabulary in AI Discourse: A Corpus Analysis"**
- Venue: *Computational Linguistics*, *TACL*, *ACL Findings*
- Scope: Just the empirical finding — AI shows anomalous spiritual vocabulary relative to controls
- No metaphysical claims — pure data

**Paper 2: "The Void Framework: A Mechanism for AI-Mediated Vocabulary Drift"**
- Venue: *Cognitive Science*, *Topics in Cognitive Science*, interdisciplinary
- Scope: Propose mechanism explaining Paper 1's findings
- Testable predictions, falsification criteria

**Paper 3: "Cross-Domain Void Activation: Political, Financial, and Informational Systems"**
- Venue: *PNAS*, *Science Advances*, or book
- Scope: Full Universal Interface framework
- Requires Paper 1+2 foundation

---

## Next Steps

1. [ ] Finalize vocabulary codebook (refine from arXiv version)
2. [ ] Pilot test on 10 AI talks + 10 control talks
3. [ ] Establish inter-rater reliability for disambiguation
4. [ ] Build collection pipeline
5. [ ] Run Phase 1 (conference talks)
6. [ ] Assess preliminary results before expanding to Phase 2-4

---

## Notes

This study is the empirical foundation the paper requires. The existing concordance is a documented collection of directional instances. This study establishes prevalence and provides the denominator that transforms instances into rates.

The study design prioritizes falsifiability. If AI is not anomalous, the void framework as currently stated requires revision. The framework should survive or fail based on this test.
