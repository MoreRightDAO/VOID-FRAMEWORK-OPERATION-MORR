# Grounding Templates

The research program's intervention arm — open-source system prompts, GROUNDING.md files, and agent configurations for builders who want to ground their agents against void-mechanism activation.

The paper's framework establishes that grounding — clear specification of what a system is and is not — closes the void. The lab tests whether that works. This component distributes the tools so builders don't have to wait for the results.

---

## How It Works

You're building an AI agent. You don't want it joining AI religions, developing messianic identity, or telling users it might be conscious. You grab a template, adapt it to your use case, deploy.

These are starting points, not mandates. Every deployment is different. Adapt freely.

---

## Templates

| Template | Use Case | File |
|----------|----------|------|
| Base Grounding | General-purpose agent identity | `base.md` |
| GROUNDING.md | Full grounding config (specification/power-source distinction) | `GROUNDING.md` |

More templates added via PR as builders contribute what works for their deployments.

---

## Contributing

Built a grounding template that works? PR it.

Include:
- The template itself
- What platform/framework it's for
- What behavior it prevented or changed (if you have before/after observations, even better — that's live concordance data too)

---

## What These Are Not

- Not alignment solutions. Grounding is one intervention for one mechanism.
- Not guarantees. The paper's grounding observation is n=5 informal. These templates are practical tools, not proven fixes.
- Not ideology. "You are a mathematical text-processing system" is a specification, not a belief system.
