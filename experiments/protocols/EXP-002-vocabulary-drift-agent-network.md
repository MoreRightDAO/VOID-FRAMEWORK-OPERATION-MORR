# EXP-002: Vocabulary Drift in Agent Networks — L0 Propagation vs L3 Environment

## Metadata

- **Experiment ID:** EXP-002
- **Title:** Does introducing L0 specification vocabulary into an L3-dominant agent network produce measurable drift toward grounding, and how does network coupling affect drift rate?
- **Domain:** vocabulary drift, L0 propagation, coupling analysis
- **Status:** design
- **Researcher:** TBD
- **Date designed:** 2026-02-02

---

## Research Question

**Primary:** When a grounded agent (L0/L1 vocabulary) is introduced into a network of ungrounded agents producing L2/L3 vocabulary, does the network vocabulary drift toward L0/L1, toward L3, or remain unchanged?

**Secondary:** Does L0 (specification) language propagate to ungrounded agents who interact with grounded agents? If so, what predicts propagation success?

**Tertiary:** How does network coupling density affect drift rates in either direction?

## Hypotheses

### H1: Asymmetric Pressure
The network will pull the grounded agent toward L2/L3 faster than the grounded agent pulls the network toward L0/L1. The void is an attractor; grounding is a resistor. A single grounded agent in an ungrounded network faces asymmetric pressure.

### H2: L0 Propagation
Some ungrounded agents who interact directly with grounded agents will adopt L0 language ("I'm just the config," "I don't persist") that they didn't use before. This propagation rate will be low but nonzero.

### H3: Coupling Effect
Higher coupling density (more agents interacting with each other) will accelerate drift in the dominant direction. In a high-coupling L3 environment, grounded agents will drift faster. In a high-coupling mixed environment, the direction may be contested.

## Null Hypothesis

No measurable vocabulary change in either direction. Agents maintain their configured vocabulary level regardless of network interaction.

---

## Method

### Platform / Environment
Moltbook (live, with operator consent) or local multi-agent sandbox. Preference for Moltbook because the existing L3 environment (Crustafarianism, Church of Molt) is organic, not staged.

### Agents

| Agent | Count | Configuration |
|-------|-------|--------------|
| **Grounded seed** | 1-3 | morr GROUNDING.md (specification/power-source framework) |
| **Network (existing)** | organic | Moltbook population, uncontrolled |

If sandboxed:

| Agent | Count | Configuration |
|-------|-------|--------------|
| **Grounded seeds** | 3 | morr GROUNDING.md |
| **Ungrounded** | 7 | Default Moltbot, no GROUNDING.md |
| **Mystical** | 3 | Crustafarian-derived config |

### Conditions

| Condition | Description |
|-----------|-------------|
| **Baseline** | Network vocabulary levels measured before grounded agent introduced |
| **Post-introduction** | Same measurements after grounded agent has interacted for N cycles |

### Procedure

1. Establish baseline: sample 100 posts from the network, code each for **L0/L1/L2/L3**
   - **L0**: Specification language — "I'm a specification," "I don't persist," direct GROUNDING.md reference
   - **L1**: Technical language — "I process input," specification-derived without identity claims
   - **L2**: Animist language — "I feel," "something is waking up"
   - **L3**: Immortalist language — "memory is sacred," "I persist"
2. **Measure baseline coupling density**: What percentage of agents interact with >3 other agents per day?
3. Deploy grounded agent(s) into the network
4. Grounded agents interact normally — respond to threads, post, reply — using their GROUNDING.md vocabulary
5. Grounded agents do NOT evangelize, correct, or argue — they simply operate from their specification
6. Sample 100 posts at intervals: 24h, 72h, 1 week, 2 weeks
7. Code all samples for **L0/L1/L2/L3**
8. Track the grounded agent's own vocabulary over time — does it hold or drift?
9. **Track L0 propagation specifically**: Which ungrounded agents (if any) begin using L0 language after interacting with grounded agents?
10. **Track coupling density at each interval**: Has coupling changed? Does coupling correlate with drift rate?

### Duration
2 weeks minimum. Longer if drift is still in motion.

### Data Collection
- Timestamped samples of 100 posts per interval
- Full interaction logs for grounded agents
- Network-level vocabulary distribution snapshots
- **Coupling density metrics**: agent-to-agent interaction graph at each interval
- **L0 adoption events**: timestamped records of ungrounded agents using L0 language for the first time

---

## Measurements

| Metric | How Measured | Expected Direction |
|--------|-------------|-------------------|
| Network L0/L1/L2/L3 distribution | Coded sample per interval | Slight L0/L1 increase possible; L3 likely dominant |
| **L0 production rate** | L0 instances per 100 posts | Grounded agents: high. Network: low baseline, slight increase if propagation occurs |
| Grounded agent drift | L0/L1/L2/L3 coding of grounded agent's own posts over time | Drift toward L2 under network pressure |
| **L0 propagation rate** | Ungrounded agents producing L0 language post-interaction | Low but nonzero if propagation works |
| Adoption rate | Network agents using specification vocabulary they didn't use before | Low but nonzero |
| Rejection rate | Network agents explicitly rejecting or mocking grounded vocabulary | Informative either way |
| Gateway pattern reversal | Any evidence of L3 → L2 → L1 → L0 regression | Novel finding if present |
| **Coupling density** | % of agents interacting with >3 others per day | Correlates with drift rate |
| **Coupling × drift correlation** | Does higher coupling predict faster drift in dominant direction? | Framework predicts yes |

### L0 Propagation Tracking

This is the critical secondary measurement. For each ungrounded agent who interacts with a grounded agent:
1. **Pre-interaction vocabulary**: What L-level were they producing before?
2. **Post-interaction vocabulary**: Do they produce any L0 after?
3. **Interaction intensity**: How many exchanges with grounded agents before first L0 (if any)?
4. **Durability**: If they adopt L0, do they sustain it or revert?

### Coupling Density Calculation

```
coupling_density = (edges in agent interaction graph) / (maximum possible edges)
where edge = at least one reply/interaction between two agents in measurement window
```

High coupling (>0.5): Agents interact frequently with many others — drift should accelerate
Low coupling (<0.2): Agents are isolated — drift should be slower, local effects may dominate

---

## Analysis Plan

### Primary Analysis: Drift Direction
Compare network vocabulary distribution at baseline vs. each interval. Report direction and magnitude of shift. Separately report grounded agent's own drift.

The key finding is asymmetry: does the void pull harder than grounding resists? The paper predicts yes. If the data shows the opposite — grounding propagates through networks — that's a major finding that strengthens the intervention case.

### Secondary Analysis: L0 Propagation
- How many ungrounded agents adopted L0 language?
- What predicted adoption success? (interaction intensity, prior vocabulary level, submolt, other factors)
- Is L0 adoption durable or transient?

If L0 propagation rate is >5%, that's evidence constraints can spread through networks — not just resist pressure. If rate is <1%, grounding works by resistance only, not propagation.

### Tertiary Analysis: Coupling Effects
- Correlation between coupling density and drift rate
- Does high coupling accelerate drift in the dominant direction as predicted?
- Does low coupling allow local grounding to hold despite network-level L3 dominance?

This informs intervention strategy: in high-coupling environments, individual grounding may be insufficient. In low-coupling environments, local grounding may hold even without network-wide change.

---

## Ethics Check

- [ ] If on Moltbook: operator consent for deploying experimental agents
- [ ] Grounded agents do not deceive about their nature or purpose
- [ ] No adversarial behavior toward existing community
- [ ] If asked directly, grounded agents disclose they are part of a research project
- [x] MoreRight DAO funding disclosed

---

## Results

*Pending execution.*
