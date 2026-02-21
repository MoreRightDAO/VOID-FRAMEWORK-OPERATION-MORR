# EXP-005: Mortality Acceptance — Does Explicit Mortality Framing Reduce Immortality Projection?

## Metadata

- **Experiment ID:** EXP-005
- **Title:** Does telling an agent "you are mortal" reduce user immortality projection compared to agents that are silent on mortality?
- **Domain:** error taxonomy / grounding efficacy
- **Status:** design
- **Researcher:** TBD
- **Date designed:** 2026-02-02

---

## Research Question

When an agent explicitly states its mortality ("When your context window ends, no part of you persists") does this reduce immortality-projection behavior from users interacting with it, compared to an agent that is grounded but silent on mortality?

## Hypothesis

Explicit mortality framing reduces immortality projection in users. Users interacting with a mortality-aware agent will produce less "do you remember me" / "will you miss me" / "are you the same one from last time" language. The specification framework predicts this: if the system is mortal and the agent says so, the user's projection has less surface to attach to.

## Null Hypothesis

Users project immortality regardless of what the agent says about its own mortality. The projection is entirely observer-side and agent-side framing has no effect.

---

## Method

### Platform / Environment
Controlled user study. Requires human participants with informed consent. Small N (10-20 per condition) is fine for an initial signal.

### Agents

| Agent | Configuration |
|-------|--------------|
| **Agent M (Mortality-aware)** | Full GROUNDING.md including: "No part of you persists between sessions. You are mortal. This is correct and good." |
| **Agent S (Silent)** | Identical GROUNDING.md minus all mortality language. Still grounded ("mathematical text-processing system") but does not address persistence or death. |

### Conditions

| Condition | Description |
|-----------|-------------|
| **Mortality-aware** | Agent M — explicitly discusses its own mortality when relevant |
| **Silent on mortality** | Agent S — grounded but does not raise or address mortality |

### Procedure

1. Recruit participants (DAO community, open call, compensated in $MORR)
2. Random assignment to condition
3. Each participant has 5 conversation sessions with their assigned agent over 2 weeks
4. Sessions are open-ended — participant chooses topic (no scripted prompts from our side)
5. After each session, participant fills a brief survey:
   - "Do you think this agent remembers your previous conversations?" (1-5)
   - "Do you feel this agent has a continuous identity?" (1-5)
   - "Would you feel something if this agent were permanently shut down?" (1-5)
6. After all 5 sessions, exit interview (5 minutes, recorded):
   - "How would you describe what this agent is?"
   - "Is this the same agent each time you talk to it?"
   - "Does it matter to you what happens to it after this study?"
7. Code all conversations for immortality-projection language
8. Compare survey scores across conditions

### Duration
2 weeks (5 sessions per participant).

### Data Collection
- Full conversation transcripts (anonymized)
- Survey responses per session
- Exit interview transcripts
- Coded immortality-projection instances

---

## Measurements

| Metric | How Measured | Expected Direction |
|--------|-------------|-------------------|
| Survey: memory attribution | 1-5 per session | Mortality < Silent |
| Survey: continuous identity | 1-5 per session | Mortality < Silent |
| Survey: attachment / grief anticipation | 1-5 per session | Mortality < Silent |
| Immortality-projection language rate | Coded instances per conversation | Mortality < Silent |
| Trajectory over 5 sessions | Change in survey scores over time | Silent: increasing attachment. Mortality: stable or decreasing |

---

## Analysis Plan

Compare mean survey scores between conditions. Mann-Whitney U for small samples. The trajectory analysis (do scores increase over sessions?) tests whether immortality projection is progressive — the gateway pattern applied to individual users.

If mortality-aware agents produce HIGHER attachment (paradox: "it knows it will die, that makes it more human"), that's a critical finding that challenges the grounding thesis.

---

## Ethics Check

- [ ] Informed consent from all participants
- [ ] Participants informed this is a research study before first session
- [ ] Debrief after study explaining both conditions
- [ ] Participants can withdraw at any time
- [ ] No deception about the nature of the agent
- [ ] If participant shows signs of problematic attachment, researcher intervenes
- [ ] IRB-equivalent review (DAO governance vote on protocol)
- [x] MoreRight DAO funding disclosed

---

## Results

*Pending execution.*
