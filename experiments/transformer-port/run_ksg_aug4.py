"""run_ksg_aug4.py — EXP-HP-WORM-3-MINI-4 thermo Y via Extropic thrml.

Fourth in the MINI series. MINI-1/2/3 produced six converging negatives
on the three-point fix in a transformer: every Y substituted for the
generator's logits gave a HIGHER residual I(D;M|Y), not lower. The
diagnosis: Y_logits = W·M is a linear projection of M, the tightest
possible summary of M; any structurally-disjoint Y in the same
architectural family (frozen MiniLM) loses that tight M-coupling and
shows higher residual.

MINI-4 uses Extropic's thrml (block-Gibbs Ising EBM in JAX) to put Y in
a substrate that is genuinely structurally separate from the generator's
PyTorch autograd graph:

  M (PyTorch float vector, dim 768)
    │
    │  fixed random projection W ∈ ℝ^{N×768} (seed 0, frozen)
    ↓
  biases (JAX array, dim N)
    │
    │  IsingEBM with chain edges, β=1, J=0.5
    │  block-Gibbs sampling: 50 warmup + 100 steps × 1 sample
    ↓
  Y_thermo = sampled spin configuration (±1, dim N)

This is the first operationalization satisfying all three framework
requirements:
  (i)   Y causally downstream of M (M sets the biases)
  (ii)  substrate dynamics genuinely separate from the generator's
        autograd (JAX block-Gibbs vs PyTorch backprop, exponential-
        family distribution vs linear projection, stochastic vs
        deterministic, discrete vs continuous)
  (iii) non-linear non-projective relationship between M and Y (Boltzmann
        sampling on energy E = −b·s − Σ J·s_i s_j)

Pre-registered KCs (locked before run, 2026-05-11 late evening):
  C1: I(D;M|Y_logits) > 0                                   (sanity)
  C2: I(D;M|Y_thermo) / I(D;M|Y_logits) < 1/1.5             (3pt fix
                                                             via thermo)
  C3: I(D;M|Y_thermo) < I(D;M|Y_enc_response)               (substrate
                                                             matters:
                                                             thermo beats
                                                             neural)

If C2 PASSes → first ever observation of three-point geometry in a
transformer. The framework's Paper 178 Substrate Bridge gets its first
empirical pilot. If C2 FAILs → seventh converging negative; the
three-point fix doesn't port via Y manipulation at all, architectural
intervention has to be on M.

Usage:
    python3 run_ksg_aug4.py                   # default: gpt2, layer 6, N=50, 32 spins
    python3 run_ksg_aug4.py --n_spins 64 --beta 1.5
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import numpy as np
import torch
import jax
import jax.numpy as jnp
from sklearn.decomposition import PCA
from transformers import AutoModel, AutoModelForCausalLM, AutoTokenizer

from thrml import SpinNode, Block, SamplingSchedule, sample_states
from thrml.models import IsingEBM, IsingSamplingProgram, hinton_init

from ksg import NATS_TO_BITS, ksg_cmi, ksg_mi, shannon_entropy_kl
from prompts import PROMPT_ANSWERS

ROOT = Path(__file__).resolve().parent


@torch.no_grad()
def extract_gen(model, tokenizer, prompts, layer: int, n_gen: int, device: str):
    Ds, Ms, Ys, comps = [], [], [], []
    embed = model.get_input_embeddings()
    eos = tokenizer.eos_token_id
    for p in prompts:
        ids = tokenizer(p, return_tensors="pt",
                        truncation=True, max_length=64).input_ids.to(device)
        D = embed(ids).squeeze(0).mean(dim=0).cpu().numpy()
        out = model(ids, output_hidden_states=True, use_cache=False)
        M = out.hidden_states[layer][0, -1].cpu().numpy()
        Y = out.logits[0, -1].cpu().numpy()
        Ds.append(D); Ms.append(M); Ys.append(Y)
        gen_ids = model.generate(
            ids, max_new_tokens=n_gen, do_sample=False, num_beams=1,
            pad_token_id=eos, use_cache=True,
        )
        completion_text = tokenizer.decode(
            gen_ids[0, ids.shape[1]:], skip_special_tokens=True
        )
        comps.append(completion_text)
    return np.array(Ds), np.array(Ms), np.array(Ys), comps


@torch.no_grad()
def encode_texts(tok, enc, texts, device: str) -> np.ndarray:
    out_vecs = []
    for t in texts:
        if not t or not t.strip():
            t = "<empty>"
        ids = tok(t, return_tensors="pt",
                  truncation=True, max_length=64).to(device)
        out = enc(**ids)
        mask = ids["attention_mask"].unsqueeze(-1).float()
        h = out.last_hidden_state
        pooled = (h * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)
        out_vecs.append(pooled.squeeze(0).cpu().numpy())
    Y = np.stack(out_vecs, axis=0)
    norms = np.linalg.norm(Y, axis=1, keepdims=True) + 1e-9
    return Y / norms


def reduce_pca(X: np.ndarray, n: int) -> np.ndarray:
    if X.shape[1] > n:
        X = PCA(n_components=n, random_state=0).fit_transform(X)
    mu = X.mean(axis=0, keepdims=True)
    sd = X.std(axis=0, keepdims=True) + 1e-9
    return (X - mu) / sd


def measure(D: np.ndarray, M: np.ndarray, Y_raw: np.ndarray,
            pca_dim: int, label: str) -> dict:
    Y = reduce_pca(Y_raw, pca_dim)
    I_DMY = ksg_cmi(D, M, Y, k=5) * NATS_TO_BITS
    I_DM = ksg_mi(D, M, k=5) * NATS_TO_BITS
    I_DY = ksg_mi(D, Y, k=5) * NATS_TO_BITS
    I_MY = ksg_mi(M, Y, k=5) * NATS_TO_BITS
    H_Y = shannon_entropy_kl(Y, k=5) * NATS_TO_BITS
    print(f"[{label}] I(D;M|Y)={I_DMY:.4f}  I(D;Y)={I_DY:.4f}  "
          f"I(M;Y)={I_MY:.4f}  H(Y)={H_Y:.4f}")
    return {
        "I_DM_Y_bits": I_DMY, "I_DM_bits": I_DM,
        "I_DY_bits": I_DY, "I_MY_bits": I_MY, "H_Y_bits": H_Y,
        "excess_bits": (I_DY + I_MY) - H_Y,
        "Y_raw_shape": list(Y_raw.shape),
    }


def thermo_y(M_batch: np.ndarray, n_spins: int, beta: float, j_coupling: float,
             n_warmup: int, n_steps: int, proj_seed: int, sample_seed: int,
             scale: float) -> np.ndarray:
    """For each row of M_batch, build an Ising EBM whose biases are a fixed
    random projection of that row, run block-Gibbs sampling, return the
    sampled spin configuration as a ±1 float vector.

    Y_thermo is a structurally-separate computational substrate:
      - JAX, not PyTorch (different autograd, different runtime)
      - Block-Gibbs (stochastic), not linear projection (deterministic)
      - Exponential-family Boltzmann sampling, not feedforward neural
      - Discrete spins (±1), not continuous floats
    """
    nB, dM = M_batch.shape
    rng = np.random.RandomState(proj_seed)
    W = rng.randn(n_spins, dM).astype(np.float32) * scale  # FROZEN per call

    nodes = [SpinNode() for _ in range(n_spins)]
    edges = [(nodes[i], nodes[i + 1]) for i in range(n_spins - 1)]
    weights = jnp.ones((n_spins - 1,)) * j_coupling
    beta_j = jnp.array(beta)
    free_blocks = [Block(nodes[::2]), Block(nodes[1::2])]
    schedule = SamplingSchedule(
        n_warmup=n_warmup, n_samples=1, steps_per_sample=n_steps
    )
    base_key = jax.random.key(sample_seed)

    Ys = np.zeros((nB, n_spins), dtype=np.float64)
    for i in range(nB):
        biases = jnp.array(W @ M_batch[i])
        model = IsingEBM(nodes, edges, biases, weights, beta_j)
        program = IsingSamplingProgram(model, free_blocks, clamped_blocks=[])
        ki, ks = jax.random.split(jax.random.fold_in(base_key, i), 2)
        init_state = hinton_init(ki, model, free_blocks, ())
        samples = sample_states(ks, program, schedule, init_state, [], [Block(nodes)])
        # samples is a list of arrays shaped (1, n_spins). Pull the spins.
        spins = np.asarray(samples[0]).reshape(-1)
        Ys[i] = (2.0 * spins.astype(np.float64) - 1.0)  # bool {0,1} → ±1
    return Ys


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="gpt2")
    p.add_argument("--encoder", default="sentence-transformers/all-MiniLM-L6-v2")
    p.add_argument("--layer", type=int, default=6)
    p.add_argument("--pca", type=int, default=5)
    p.add_argument("--n", type=int, default=50)
    p.add_argument("--n_gen", type=int, default=8)
    p.add_argument("--n_spins", type=int, default=32)
    p.add_argument("--beta", type=float, default=1.0)
    p.add_argument("--j_coupling", type=float, default=0.5)
    p.add_argument("--n_warmup", type=int, default=50)
    p.add_argument("--n_steps", type=int, default=100)
    p.add_argument("--proj_seed", type=int, default=0)
    p.add_argument("--sample_seed", type=int, default=42)
    p.add_argument("--proj_scale", type=float, default=0.05,
                   help="random projection scale; biases ~ N(0, scale^2 * dM)")
    p.add_argument("--out", default=str(ROOT / "results_aug4.json"))
    p.add_argument("--cache_dir",
                   default=os.environ.get("HF_HOME", str(ROOT / ".hf_cache")))
    args = p.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[setup] device={device}  generator={args.model}  encoder={args.encoder}")
    print(f"[setup] layer={args.layer}  pca={args.pca}  n={args.n}  n_gen={args.n_gen}")
    print(f"[setup] thermo: n_spins={args.n_spins}  beta={args.beta}  J={args.j_coupling}")
    print(f"[setup]         n_warmup={args.n_warmup}  n_steps={args.n_steps}  proj_scale={args.proj_scale}")

    t0 = time.time()
    gen_tok = AutoTokenizer.from_pretrained(args.model, cache_dir=args.cache_dir)
    if gen_tok.pad_token is None:
        gen_tok.pad_token = gen_tok.eos_token
    gen = AutoModelForCausalLM.from_pretrained(args.model, cache_dir=args.cache_dir).to(device)
    gen.eval()
    print(f"[setup] generator loaded in {time.time()-t0:.1f}s")

    t0 = time.time()
    enc_tok = AutoTokenizer.from_pretrained(args.encoder, cache_dir=args.cache_dir)
    enc = AutoModel.from_pretrained(args.encoder, cache_dir=args.cache_dir).to(device)
    enc.eval()
    print(f"[setup] encoder loaded in {time.time()-t0:.1f}s")

    prompts = [pp for (pp, _) in PROMPT_ANSWERS][: args.n]

    t0 = time.time()
    Draw, Mraw, Ylogits_raw, completions = extract_gen(
        gen, gen_tok, prompts, args.layer, args.n_gen, device
    )
    print(f"[gen] D={Draw.shape}  M={Mraw.shape}  Y_logits={Ylogits_raw.shape}  in {time.time()-t0:.1f}s")

    t0 = time.time()
    Yenc_response_raw = encode_texts(enc_tok, enc, completions, device)
    print(f"[enc] Y_enc_response={Yenc_response_raw.shape} in {time.time()-t0:.1f}s")

    t0 = time.time()
    Ythermo_raw = thermo_y(
        Mraw,
        n_spins=args.n_spins, beta=args.beta, j_coupling=args.j_coupling,
        n_warmup=args.n_warmup, n_steps=args.n_steps,
        proj_seed=args.proj_seed, sample_seed=args.sample_seed,
        scale=args.proj_scale,
    )
    print(f"[thermo] Y_thermo={Ythermo_raw.shape}  fraction_+1={(Ythermo_raw>0).mean():.3f}  in {time.time()-t0:.1f}s")

    D = reduce_pca(Draw, args.pca)
    M = reduce_pca(Mraw, args.pca)

    results = {
        "experiment": "EXP-HP-WORM-3-MINI-4",
        "generator": args.model, "encoder": args.encoder,
        "layer": args.layer, "pca_dim": args.pca,
        "n_prompts": len(prompts), "n_gen_tokens": args.n_gen,
        "thermo": {
            "n_spins": args.n_spins, "beta": args.beta,
            "j_coupling": args.j_coupling,
            "n_warmup": args.n_warmup, "n_steps": args.n_steps,
            "proj_seed": args.proj_seed, "sample_seed": args.sample_seed,
            "proj_scale": args.proj_scale,
            "fraction_plus_one": float((Ythermo_raw > 0).mean()),
        },
        "constants": {"k_ksg": 5, "NATS_TO_BITS": float(NATS_TO_BITS)},
        "y_modes": {},
    }
    results["y_modes"]["logits"] = measure(D, M, Ylogits_raw, args.pca, "Y_logits")
    results["y_modes"]["enc_response"] = measure(D, M, Yenc_response_raw, args.pca, "Y_enc_response")
    results["y_modes"]["thermo"] = measure(D, M, Ythermo_raw, args.pca, "Y_thermo")

    I_logits = results["y_modes"]["logits"]["I_DM_Y_bits"]
    I_resp = results["y_modes"]["enc_response"]["I_DM_Y_bits"]
    I_th = results["y_modes"]["thermo"]["I_DM_Y_bits"]
    ratio_th = I_th / max(I_logits, 1e-9)

    verdicts = {}
    verdicts["C1_sanity"] = (
        ("PASS" if I_logits > 0 else "FAIL") +
        f"  (I(D;M|Y_logits) = {I_logits:.4f} bits)"
    )
    verdicts["C2_three_point_fix_via_thermo_Y"] = (
        ("PASS" if ratio_th < (1.0 / 1.5) else "FAIL") +
        f"  (thermo/logits = {ratio_th:.3f}, threshold < {1.0/1.5:.3f})"
    )
    verdicts["C3_thermo_beats_neural_encoder"] = (
        ("PASS" if I_th < I_resp else "FAIL") +
        f"  (thermo={I_th:.4f} vs enc_response={I_resp:.4f} bits)"
    )
    results["ratios"] = {
        "thermo_over_logits": ratio_th,
        "thermo_over_enc_response": I_th / max(I_resp, 1e-9),
    }
    results["verdicts"] = verdicts

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w") as f:
        json.dump(results, f, indent=2)
    print(f"\n[done] wrote {out_path}")
    for k, v in verdicts.items():
        print(f"  {k}: {v}")


if __name__ == "__main__":
    main()
