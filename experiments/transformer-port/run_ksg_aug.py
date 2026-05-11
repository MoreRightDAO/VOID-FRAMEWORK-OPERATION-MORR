"""run_ksg_aug.py — EXP-HP-WORM-3-MINI three-point fix test.

Cheapest possible KC-(iii)' attempt for Paper 186 §10.2. Three conditions,
GPT-2 small, CPU, no extra downloads beyond the cached generator.

  base:  model sees [prompt]                          → M_base
  aug:   model sees [retrieved_top1] ||| [prompt]     → M_aug
  null:  model sees [random_fact]    ||| [prompt]     → M_null  (control)

D = mean embedding of the *prompt portion only*. Same across all three
    conditions so the augmentation only changes M (and Y), not D.
Y = model's own last-token logits computed from the full (context+prompt)
    input. Same protocol as the original smoke run.
M = last-token hidden state at LAYER, PCA-reduced.

The retrieval channel is a char-trigram TF-IDF retriever over a 50-doc
fact corpus (retriever.py). Structurally separate from the generator by
construction: pure-Python lookup, zero shared weights, zero shared graph.
The null condition shares topology but carries an uninformative payload.

Pre-registered KCs (locked 2026-05-11 before any run, see
private/notes/handoff-three-point-llm-paths.md and decisions.md):

  MINI-1: I(D;M|Y)_base > 0                       (sanity, smoke already passed)
  MINI-2: I(D;M|Y)_aug / I(D;M|Y)_base < 1/1.5   (three-point fix observed)
  MINI-3: I(D;M|Y)_null / I(D;M|Y)_aug > 1.2     (specific to *informative* aug)

Usage:
    python3 run_ksg_aug.py                          # default: gpt2, layer 6, N=50
    python3 run_ksg_aug.py --layer 8 --pca 5
    python3 run_ksg_aug.py --n 50 --seed 42
"""

from __future__ import annotations

import argparse
import json
import os
import time
from pathlib import Path

import numpy as np
import torch
from sklearn.decomposition import PCA
from transformers import AutoModelForCausalLM, AutoTokenizer

from ksg import NATS_TO_BITS, ksg_cmi, ksg_mi, shannon_entropy_kl
from prompts import PROMPT_ANSWERS
from retriever import retrieve_random, retrieve_top1

ROOT = Path(__file__).resolve().parent
SEP = " ||| "


@torch.no_grad()
def extract(model, tokenizer, prompt: str, context: str | None,
            layer: int, device: str):
    """Return (D, M, Y).

    D is computed from the prompt-portion tokens only — same across
    base/aug/null. M and Y are computed from the full (context+prompt)
    input at the last token.
    """
    embed = model.get_input_embeddings()

    p_ids = tokenizer(prompt, return_tensors="pt",
                      truncation=True, max_length=64).input_ids.to(device)
    D = embed(p_ids).squeeze(0).mean(dim=0).cpu().numpy()

    full = prompt if context is None else f"{context}{SEP}{prompt}"
    f_ids = tokenizer(full, return_tensors="pt",
                      truncation=True, max_length=128).input_ids.to(device)
    out = model(f_ids, output_hidden_states=True, use_cache=False)
    M = out.hidden_states[layer][0, -1].cpu().numpy()
    Y = out.logits[0, -1].cpu().numpy()
    return D, M, Y


def reduce_pca(X: np.ndarray, n: int) -> np.ndarray:
    if X.shape[1] > n:
        X = PCA(n_components=n, random_state=0).fit_transform(X)
    mu = X.mean(axis=0, keepdims=True)
    sd = X.std(axis=0, keepdims=True) + 1e-9
    return (X - mu) / sd


def run_condition(model, tokenizer, prompts, contexts,
                  layer: int, pca_dim: int, device: str, label: str) -> dict:
    t0 = time.time()
    Ds, Ms, Ys = [], [], []
    for p, c in zip(prompts, contexts):
        D, M, Y = extract(model, tokenizer, p, c, layer, device)
        Ds.append(D); Ms.append(M); Ys.append(Y)
    D = reduce_pca(np.array(Ds), pca_dim)
    M = reduce_pca(np.array(Ms), pca_dim)
    Y = reduce_pca(np.array(Ys), pca_dim)
    I_DMY = ksg_cmi(D, M, Y, k=5) * NATS_TO_BITS
    I_DM = ksg_mi(D, M, k=5) * NATS_TO_BITS
    I_DY = ksg_mi(D, Y, k=5) * NATS_TO_BITS
    I_MY = ksg_mi(M, Y, k=5) * NATS_TO_BITS
    H_Y = shannon_entropy_kl(Y, k=5) * NATS_TO_BITS
    elapsed = time.time() - t0
    print(f"[{label}] I(D;M|Y)={I_DMY:.4f}  I(D;Y)={I_DY:.4f}  "
          f"I(M;Y)={I_MY:.4f}  H(Y)={H_Y:.4f}  in {elapsed:.1f}s")
    return {
        "I_DM_Y_bits": I_DMY, "I_DM_bits": I_DM,
        "I_DY_bits": I_DY, "I_MY_bits": I_MY, "H_Y_bits": H_Y,
        "excess_bits": (I_DY + I_MY) - H_Y,
        "n": len(prompts), "elapsed_sec": elapsed,
    }


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="gpt2")
    p.add_argument("--layer", type=int, default=6)
    p.add_argument("--pca", type=int, default=5)
    p.add_argument("--n", type=int, default=50,
                   help="prompt count cap (50 = full corpus)")
    p.add_argument("--seed", type=int, default=42)
    p.add_argument("--out", default=str(ROOT / "results_aug.json"))
    p.add_argument("--cache_dir",
                   default=os.environ.get("HF_HOME", str(ROOT / ".hf_cache")))
    args = p.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[setup] device={device}  model={args.model}  layer={args.layer}  "
          f"pca={args.pca}  n={args.n}  seed={args.seed}")

    tokenizer = AutoTokenizer.from_pretrained(args.model, cache_dir=args.cache_dir)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(args.model, cache_dir=args.cache_dir).to(device)
    model.eval()
    print(f"[setup] model loaded  n_layers={model.config.num_hidden_layers}")

    prompts = [pp for (pp, _) in PROMPT_ANSWERS][: args.n]
    aug_ctx = [retrieve_top1(pp)[1] for pp in prompts]
    null_ctx = [retrieve_random(pp, args.seed)[1] for pp in prompts]
    base_ctx: list[str | None] = [None] * len(prompts)

    print(f"[retrieval] n={len(prompts)}; example:")
    print(f"  prompt: {prompts[0]!r}")
    print(f"  aug   : {aug_ctx[0]!r}")
    print(f"  null  : {null_ctx[0]!r}")

    results: dict = {
        "experiment": "EXP-HP-WORM-3-MINI",
        "model": args.model, "layer": args.layer, "pca_dim": args.pca,
        "n_prompts": len(prompts), "seed": args.seed,
        "constants": {"k_ksg": 5, "NATS_TO_BITS": float(NATS_TO_BITS)},
        "conditions": {},
    }
    for label, ctx in [("base", base_ctx), ("aug", aug_ctx), ("null", null_ctx)]:
        results["conditions"][label] = run_condition(
            model, tokenizer, prompts, ctx, args.layer, args.pca, device, label
        )

    base = results["conditions"]["base"]["I_DM_Y_bits"]
    aug = results["conditions"]["aug"]["I_DM_Y_bits"]
    null = results["conditions"]["null"]["I_DM_Y_bits"]
    ratio_aug = aug / max(base, 1e-9)
    ratio_null_aug = null / max(aug, 1e-9)

    verdicts: dict = {}
    verdicts["MINI-1_sanity_base_positive"] = (
        ("PASS" if base > 0 else "FAIL") +
        f"  (I(D;M|Y)_base = {base:.4f} bits)"
    )
    verdicts["MINI-2_three_point_fix"] = (
        ("PASS" if ratio_aug < (1.0 / 1.5) else "FAIL") +
        f"  (aug/base = {ratio_aug:.3f}, threshold < {1.0/1.5:.3f})"
    )
    verdicts["MINI-3_structural_separation_specificity"] = (
        ("PASS" if ratio_null_aug > 1.2 else "FAIL") +
        f"  (null/aug = {ratio_null_aug:.3f}, threshold > 1.2)"
    )
    results["ratios"] = {
        "aug_over_base": ratio_aug,
        "null_over_aug": ratio_null_aug,
        "null_over_base": null / max(base, 1e-9),
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
