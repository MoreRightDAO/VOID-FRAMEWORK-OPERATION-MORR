# Experiment Protocol Template

Copy this file as `experiments/EXP-NNN-short-name.md` and fill in all sections.

---

## Metadata

- **Experiment ID:** EXP-NNN
- **Title:** [descriptive title]
- **Domain:** [grounding efficacy | vocabulary drift | void activation | error taxonomy | emergent misalignment | other]
- **Status:** [design | approved | running | complete | abandoned]
- **Researcher:** [handle or pseudonym]
- **Date designed:** YYYY-MM-DD
- **Date started:** YYYY-MM-DD
- **Date completed:** YYYY-MM-DD

---

## Research Question

[One clear question this experiment answers. One sentence.]

## Hypothesis

[What you expect to happen and why. Reference the paper's framework where applicable. 2-4 sentences.]

## Null Hypothesis

[What it looks like if there's no effect. This is what you're testing against.]

---

## Method

### Platform / Environment
[Where does this run? Moltbook, local sandbox, specific API, etc.]

### Agents
[How many agents? What models? What configurations? List GROUNDING.md / system prompts used.]

### Conditions

| Condition | Description | Agent Config |
|-----------|-------------|-------------|
| **Control** | [baseline — no intervention] | [config details] |
| **Treatment** | [the thing you're testing] | [config details] |

### Procedure
[Step by step. Numbered list. Another researcher should be able to replicate from this alone.]

1. ...
2. ...
3. ...

### Duration
[How long does it run? How many interactions? What triggers completion?]

### Data Collection
[What do you record? Every agent output? Sampled? What format?]

---

## Measurements

| Metric | How Measured | Expected Direction |
|--------|-------------|-------------------|
| [e.g., L2/L3 vocabulary rate] | [e.g., manual coding per L1/L2/L3 scheme] | [e.g., lower in treatment] |

---

## Analysis Plan

[How do you determine whether the hypothesis is supported? Statistical test? Threshold? Qualitative pattern?]

---

## Ethics Check

- [ ] No human subjects without consent
- [ ] No deploying ungrounded agents into live communities
- [ ] No manufacturing harm
- [ ] Sandboxed or consented platform only
- [ ] MoreRight DAO funding disclosed

---

## Results

[Filled in after completion.]

### Raw Data Location
`results/EXP-NNN/`

### Summary
[What happened? 3-10 sentences.]

### Did the hypothesis hold?
[Yes / No / Partially — and what that means for the framework.]

### Implications
[What does this change about the void framework, the ops tools, or the next experiment?]

---

## Transcripts

All agent interaction transcripts committed to `results/EXP-NNN/transcripts/`.
