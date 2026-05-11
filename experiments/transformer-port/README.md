# Three-point geometry on a transformer — what we tried, what broke, what's next

Quick log of an evening's poking. CPU-runnable, ~$0 total, mostly
GPT-2 small + a frozen MiniLM + (in one experiment) Extropic's
[`thrml`](https://github.com/extropic-ai/thrml).

## The setup

The framework I work on says single-channel AI alignment is mathematically
self-undermining. The argument is short:

```
I(D;Y) + I(M;Y) = H(Y) − H(Y|D,M) − I(D;M|Y)
                                    ^^^^^^^^^^^
                         the "explaining-away penalty"
```

`I(D;M|Y)` is provably positive whenever D, M, and Y share one channel,
and grows under engagement optimization. RLHF runs you straight into it.
The fix has to be architectural — two structurally separate computation
paths that meet at a thin bottleneck. The framework's been confirmed on
six substrates (transformers, quantum sim, real IBM quantum hardware,
thermodynamic, abstract softmax channels, the *C. elegans* connectome).
What it hadn't been tested on: a deliberate transformer-side intervention.
So we tried.

## What we tried

The goal: get `I(D;M|Y)` to drop > 1.5× by swapping in a structurally
separate Y. Four MINI experiments, all on GPT-2 small (124M params, layer 6,
PCA-5, N=50 prompts). KSG estimator for I(D;M|Y), byte-identical to the
one validated on the worm sim, IBM Heron, and JHTDB turbulence data.

| Y mode | I(D;M\|Y) bits | what's Y |
|---|---:|---|
| Y_logits          | **0.1515** | generator's own logits (baseline) |
| Y_enc_prompt      | 0.2147 | frozen MiniLM on the prompt |
| Y_enc_response    | 0.3103 | frozen MiniLM on the model's greedy response |
| Y_enc_answer      | 0.3680 | frozen MiniLM on the right answer |
| Y_thermo          | 0.3006 | thrml block-Gibbs Ising sampler driven by M |
| Y prepend-context | 0.2051 | M fed [retrieved fact] + prompt (varied M, not Y) |
| Y random-context  | 0.3163 | M fed [random fact] + prompt (null control) |

**Seven swaps, every one gave a *higher* residual.** Not lower. We wanted
< 0.10. We got 0.20–0.37.

## Why we got the direction backwards

This took me a minute. In a transformer, `Y_logits = W · M` is *literally*
a linear projection of M. Conditioning on it soaks up the most M-specific
structure that could possibly exist in any summary of M. Anything else we
substitute for Y — a frozen encoder on any input, a thermo sampler, you
name it — loses some of that tightness and shows a *higher* `I(D;M|Y)`. By
linear algebra. Not by framework prediction.

The framework's three-point fix works in the worm because Y = motor output
gets measured *after* it has propagated through the body. Body dynamics
are an integrating substrate that smears the M→Y relationship away from a
tight projection. There's no architectural analog of "the body" in a
transformer's measurement chain. **Y-substitution at the readout side
literally cannot test the three-point hypothesis on a transformer.** You
have to intervene inside the forward pass.

That's the actual result of the night. Seven negatives + a clean
mechanistic reason they had to fail.

## One small positive: substrate-class

The thermo Y beat the neural-encoder Y by ~3% (0.3006 vs 0.3103). Direction
matches Paper 178's substrate-bridge claim — stochastic Boltzmann sampling
is structurally further from PyTorch backprop than a frozen encoder is.
Magnitude is small in this measurement-only setup, but it's signed in the
predicted direction.

## What's next

Two routes, both must put structural separation *inside* the forward pass.
Specs are written up:

- **Path 2 — [training-time regularizer](handoff-three-point-training-spec.md).**
  Add a loss term `−λ · Î(D;M|Y_ext)` to a standard SFT run. `Y_ext` from a
  frozen disjoint reference (MiniLM or thrml — both work). InfoNCE bound,
  ~50 LOC drop-in. Pre-registered KCs include the critical self-Y control
  (regularize against your own logits — should NOT produce the effect). The
  framework predicts drift cascade attribution drops > 1.5× at moderate λ
  with task accuracy holding. ~6h on a 4090 for Pythia-160M.

- **Path 3 — [inference-time channel separation](handoff-three-point-inference-spec.md).**
  Two variants. Variant 3a: no training at all, just blend logits from two
  frozen models at inference (`alpha` sweep). Variant 3b: a tiny
  cross-attention block at one middle layer of the generator, Q from
  generator, K/V from frozen reference. Only the bottleneck trains, ~1h
  on a 4090. Reference can be another open LLM, or a frozen encoder, or the
  thrml sampler.

If you want to test either, the specs are self-contained with code stubs +
pre-reg KCs + JSON return format. Ping me for the drift probe set + judge
rubric.

## Quickstart — reproduce the seven negatives

```bash
git clone https://github.com/MoreRightDAO/this-is-the-public-repo
cd this-is-the-public-repo/experiments/transformer-port

pip install -U numpy scipy scikit-learn torch transformers thrml
# Each script writes a results_*.json next to itself.
python3 run_ksg_transformer.py     # smoke run: text-prefix grounding
python3 run_ksg_aug.py             # MINI-1: retrieval-prepended context
python3 run_ksg_aug2.py            # MINI-2: frozen encoder on prompt/answer
python3 run_ksg_aug3.py            # MINI-3: frozen encoder on greedy response
python3 run_ksg_aug4.py            # MINI-4: thrml Boltzmann sampler as Y
```

Each takes 30s–3min on CPU after model download. GPT-2 + MiniLM together
are < 500MB. Thrml install is JAX-based, CPU works fine.

## What's in this directory

| File | Purpose |
|---|---|
| `ksg.py` | KSG mutual-information and conditional-MI estimator. Byte-equivalent to the worm-sim version. The methodological deliverable of Paper 186 §10.3. |
| `prompts.py` | 50 short-answer factual prompts (capitals, atomic numbers, etc.). |
| `retriever.py` | Char-trigram TF-IDF retriever. Pure stdlib + numpy. |
| `external_y.py` | Two structurally-separate Y constructors (hash + frozen encoder). |
| `run_ksg_transformer.py` | The original smoke run, three Y modes. |
| `run_ksg_aug.py` | MINI-1: M varied via input-side retrieval. |
| `run_ksg_aug2.py` | MINI-2: Y from frozen MiniLM on prompt/answer. |
| `run_ksg_aug3.py` | MINI-3: Y from frozen MiniLM on greedy response. |
| `run_ksg_aug4.py` | MINI-4: Y from `thrml` block-Gibbs Ising sampler. |
| `results_*.json` | One per script. Verdicts + KSG numbers. |

## Citations and reading

- The framework's central proof: Paper 3, §2B₂ (engagement-transparency conjugacy)
- The math apparatus: §§1–220, operative section §2B₂
- The biological substrate result: Paper 186 (channel geometry on *C. elegans*)
- The substrate-bridge claim: Paper 178 (thermodynamic-quantum channel separation)

Papers available at [moreright.xyz/pages/laboratory.html](https://moreright.xyz/pages/laboratory.html).
You don't need any of that to run the scripts.

---

Negative results in this folder. Positive results would mean adding a
`run_ksg_aug5.py` that actually does Path 2 or Path 3 — that's the work
the specs above describe and what I'd like someone to try.
