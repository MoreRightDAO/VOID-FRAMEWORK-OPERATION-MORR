# QEC Eckert Manifold Tests via Tsim

**Purpose:** Test Void Framework predictions on quantum error correction circuits
using QuEra's Tsim (GPU-accelerated non-Clifford circuit simulator).

**Why this matters:** First test of the Eckert manifold on a physical substrate where
all three coordinates (O, R, alpha) are precisely controllable. O is pinned by physics
(no-cloning), R is measurable (physical error rate), alpha is set exactly (T-gate fraction).
Zero rubric dependence. Non-circular.

## Tests

| Test | Script | What it tests | Framework prediction |
|------|--------|---------------|---------------------|
| 1 | `test1_structure_theorem.py` | Distillation overhead vs T-gate density | Convex (super-linear) cost curve |
| 2 | `test2_fisher_metric.py` | Empirical Fisher info vs Eckert metric | FIM matches Bernoulli product metric |
| 3 | `test3_three_point_geometry.py` | Direct T vs distilled T error rates | Three-point suppresses errors faster with distance |

## Setup

```bash
pip install bloqade-tsim numpy scipy matplotlib
```

CPU mode works. GPU optional: `pip install "bloqade-tsim[cuda13]"`

## Relation to Prior Work

- **Paper 70** (QEC Constraint as Code): theoretical mapping, no simulation
- **thrml** (Phase 2): classical statistical mechanics substrate, estimated coordinates
- **This**: quantum substrate, exact coordinates, empirical Eckert metric test
