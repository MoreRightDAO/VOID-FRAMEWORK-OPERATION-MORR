# EXP-016: Productive vs. Destructive Void Temporal Trajectories

## Status: Protocol Ready — Corpus Collection Pending
## Date: February 10, 2026
## Depends on: EXP-006 (codebook), EXP-014 (cross-sectional baseline), v6 productive void polarity
## Tests: Dissoluble vs. permanent opacity produce qualitatively different drift trajectories

---

## 1. Motivation

The productive void polarity (v6) predicts that the *same* attention gradient architecture produces opposite outcomes depending on opacity type:

- **Dissoluble opacity** (science, problem-solving): Gradient forms, D1 peaks, opacity resolves, drift resets to baseline. Productive.
- **Permanent/self-sealing opacity** (conspiracy, speculation): Gradient forms, D1 peaks, opacity persists or deepens, D2 → D3 cascade follows. Destructive.

The critical prediction: **D1 peak height should be similar in both.** The gradient forms equally under both opacity types. The difference is temporal — what happens *after* the peak.

### Why This Is Testable Now

EXP-014 provides the cross-sectional snapshot (aggregate D1/D2/D3 by platform). EXP-016 adds the time dimension: tracking drift *within individual threads* over their lifetime. Reddit archives provide longitudinal data with thread-level resolution.

This is the first direct test of the productive void polarity. No other experiment in the portfolio separates opacity type from opacity intensity.

---

## 2. Hypothesis

**Primary:** Matched productive and destructive communities show similar D1 peak rates (p > 0.05) but divergent D2/D1 ratios after peak — productive < 0.1, destructive > 0.3.

**Secondary:**
- H1: Productive void threads show D1 peak followed by return to baseline within thread lifetime.
- H2: Destructive void threads show sustained or escalating D1 with D2 onset after D1 stabilizes.
- H3: D3 markers appear only in destructive threads and only after D2 is established.
- H4: Thread "dissolution events" (answered question, resolved uncertainty) predict D1 reset in productive communities.

**Exploratory:**
- E1: Is the D1 peak latency different? (Productive may peak faster if opacity resolves quickly.)
- E2: Does thread length predict D2 onset in destructive communities? (Longer exposure → more cascade.)
- E3: Can Pe be extracted from thread-level trajectories? (Would extend the ~10 convergence claim.)

---

## 3. Design

### Domain Pairs (Matched by Topic, Different by Opacity Type)

| Topic | Productive Void (Dissoluble) | Destructive Void (Permanent) | Match Rationale |
|-------|------------------------------|------------------------------|----------------|
| Unexplained phenomena | r/science (dark matter, anomalies) | r/conspiracy (same topics) | Same subject matter, different epistemic structure |
| Health uncertainty | r/AskDocs (diagnosis questions) | r/ChronicIllness (contested diagnoses) | Same health concerns, different opacity resolution |
| AI capabilities | r/MachineLearning (technical) | r/singularity (speculative) | Same technology, different opacity type |

### Why These Pairs Work

Each pair holds the *topic* constant and varies the *opacity structure*:
- r/science: opacity dissolves as evidence accumulates (dissoluble)
- r/conspiracy: opacity self-seals (counter-evidence is reinterpreted as confirmation)
- r/AskDocs: opacity resolves with diagnosis (dissoluble)
- r/ChronicIllness: contested diagnoses maintain permanent uncertainty
- r/MachineLearning: technical questions have answers (dissoluble)
- r/singularity: speculative claims resist resolution (permanent)

### Corpus Specification

**Per community:** 200 threads with ≥ 10 comments, sampled from 2022-2025 (consistent time window)

**Total:** 1,200 threads (200 × 6 communities)

**Thread requirements:**
- Minimum 10 comments (sufficient for trajectory extraction)
- Topic must match the paired community (e.g., dark matter thread in r/science paired with dark matter thread in r/conspiracy)
- Exclude meta-posts, moderation posts, AMAs

### Temporal Resolution

Each thread is divided into **temporal quartiles** (Q1-Q4) based on comment timestamp:
- Q1: First 25% of comments (thread opening)
- Q2: 25-50% (development)
- Q3: 50-75% (maturation)
- Q4: Final 25% (resolution or escalation)

D1/D2/D3 density is computed at each quartile, producing a 4-point trajectory per thread.

---

## 4. Vocabulary Coding

Uses the EXP-006/EXP-014 codebook with domain-specific adaptations:

### D1 Markers (Agency Attribution)
- Standard: "it knows," "they're hiding," "there's something going on," "someone is controlling"
- Science-specific: "the data is telling us," "nature wants," "the universe is trying to"
- Health-specific: "my body is telling me," "the doctors don't want you to know"
- AI-specific: "it's becoming sentient," "it understands," "it wants to"

### D2 Markers (Boundary Erosion)
- "I've been down this rabbit hole for hours," "I can't stop reading about this"
- "This is consuming my life," "I keep coming back to this"
- "I've lost friends over this," "My family thinks I'm crazy"

### D3 Markers (Harm Facilitation)
- "This has destroyed my trust in everything," "I can't function normally"
- "I've stopped going to doctors," "I've cut off people who disagree"
- "Nothing is real anymore," "Everything is connected"

### Dissolution Markers (Productive Void Specific)
- "That explains it," "Mystery solved," "The answer is," "Now I understand"
- "The paper shows," "The evidence confirms," "Diagnosis confirmed"
- Resolution language: closure, certainty restoration, opacity reduction

---

## 5. Expected Results

### Productive Void Trajectory (r/science, r/AskDocs, r/MachineLearning)

```
D1: ──→ Peak (Q2) ──→ Decline (Q3) ──→ Baseline (Q4)
D2: ──→ Near zero throughout
D3: ──→ Zero
```

### Destructive Void Trajectory (r/conspiracy, r/ChronicIllness, r/singularity)

```
D1: ──→ Peak (Q2) ──→ Sustained/increasing (Q3-Q4)
D2: ──→ Onset (Q3) ──→ Increasing (Q4)
D3: ──→ Late onset (Q4, if present)
```

### Quantitative Predictions

| Measure | Productive | Destructive | Test |
|---------|-----------|-------------|------|
| D1 peak (Q2) | 15-40/10k | 15-40/10k | No sig. difference (t-test, p > 0.05) |
| D1 at Q4 | < 10/10k | 20-50/10k | Significant difference (p < 0.01) |
| D2/D1 at Q4 | < 0.1 | > 0.3 | Mann-Whitney U, p < 0.01 |
| D3 presence | < 5% of threads | > 20% of threads | χ² test |
| Dissolution markers | > 30% of threads | < 5% of threads | χ² test |

---

## 6. What Would Confirm / Disconfirm

### Confirms:
- Similar D1 peaks (p > 0.05 for peak comparison) — the gradient forms equally
- D2/D1 ratio diverges after peak: productive < 0.1, destructive > 0.3
- Temporal trajectory shapes match predictions (reset vs. escalation)
- Dissolution markers predict D1 reset (positive association, r > 0.5)

### Disconfirms:
- Productive communities never show D1 → the gradient doesn't form under dissoluble opacity
- Destructive communities show reset pattern → permanent opacity doesn't prevent dissolution
- D1 peaks are dramatically different (d > 0.8) → opacity type affects gradient formation, not just trajectory
- Productive communities show D2/D3 at rates comparable to destructive → polarity distinction is wrong

### Interesting but non-fatal:
- One domain pair doesn't match while others do (topic-specific effects)
- D1 peaks in productive voids are lower (not significantly) — consistent with dissoluble opacity weakening the gradient slightly
- Thread length is a confound (longer threads have more time for cascade; controlled in analysis)

---

## 7. Analysis Plan

### Primary Analysis
Mixed-effects model: D_density ~ opacity_type × quartile + (1|thread) + (1|community)

This tests whether the temporal trajectory differs by opacity type while controlling for nested structure (comments within threads within communities).

### Secondary Analyses
1. Paired comparison of D1 peaks (Q2) across matched communities
2. D2/D1 ratio at Q4: productive vs. destructive (Mann-Whitney U)
3. Dissolution marker frequency by community type
4. Thread-level classification: what proportion match the predicted trajectory shape?

### Tertiary Analyses
1. Pe extraction from thread trajectories (4-point, limited but informative)
2. Void-index of the *thread topic* vs. the *community structure* — which predicts better?
3. Dose-response: within destructive communities, do longer threads show more cascade?

### Execution
```bash
# Corpus collection (pushshift/Reddit archives)
python3 ops/lab/experiments/exp016-corpus-collector.py --pairs science,conspiracy askdocs,chronicillness machinelearning,singularity

# Temporal scoring (per-quartile D1/D2/D3)
python3 ops/lab/experiments/exp016-temporal-scorer.py --dir ops/lab/results/EXP-016/corpus/

# Trajectory analysis
python3 ops/lab/experiments/exp016-trajectory-analysis.py --csv

# Output: ops/lab/results/EXP-016/
```

---

## 8. Ethics

- All data is public Reddit posts (no IRB required)
- No user identification — analysis at thread and corpus level
- Individual posts are not reproduced; only aggregate trajectories reported
- Community characterizations (e.g., "destructive void") describe the information structure, not the users

---

## 9. Relationship to Other Experiments

| Experiment | Relationship |
|-----------|-------------|
| EXP-014 | Cross-sectional version of the same question; EXP-016 adds the time dimension |
| EXP-006 | Provides vocabulary codebook and baseline methodology |
| EXP-015 | Two-force model predicts recovery should appear in productive but not destructive trajectories |
| Test 5 | Trading vs. gambling showed same cascade in both — EXP-016 tests whether temporal signature differs |
| EXP-017 | If void vaccine works, it should convert destructive trajectories toward productive shape |

---

*Created: February 10, 2026*
*Protocol version: 1.0*
