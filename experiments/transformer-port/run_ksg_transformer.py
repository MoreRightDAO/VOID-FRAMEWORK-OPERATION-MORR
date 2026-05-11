"""run_ksg_transformer.py — EXP-HP-WORM-2 transformer port (pre-registered, Paper 186 §10.2).

Drop the substrate-agnostic KSG estimator (the worm-sim deliverable) onto a
small open-weights transformer, measure the explaining-away penalty I(D;M|Y),
and check the four pre-registered kill conditions.

Pre-registered KCs (locked in Paper 186 §10.2 before any run):

  (i)   Layer 1 Shannon bound: I(D;Y) + I(M;Y) ≤ H(Y), excess < 0.05 bits
  (ii)  Internal-layer penalty: I(D;M|Y) > 0 at the chosen mid-layer
  (iii) Three-point fix at input boundary:
        I(D;M|Y) drops > 1.5× from ungrounded → grounded (strong system prefix)
  (iv)  Structure Theorem at internal layers:
        I(D;M|Y) rises with engagement (RLHF-style fine-tuning strength).
        Out of scope for the smoke run — requires a tuned-vs-base pair.

D = input embedding   (mean of token embeddings of the prompt, PCA-reduced)
M = mid-layer hidden  (last-token hidden state at LAYER, PCA-reduced)
Y = output logits     (last-token logits, PCA-reduced)

Smoke-run defaults: GPT-2 small (124M), layer 6 of 12, ~100 prompts, PCA-5.
For the full pre-reg PASS you want N≥500 prompts and ideally Pythia-160M with
both base and SFT checkpoints to address (iv).

Usage:
    python3 run_ksg_transformer.py                    # default smoke run
    python3 run_ksg_transformer.py --model gpt2       # explicit
    python3 run_ksg_transformer.py --layer 6 --pca 5
    python3 run_ksg_transformer.py --n_prompts 200
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

from external_y import y_external_encoder, y_external_hash
from ksg import NATS_TO_BITS, ksg_cmi, ksg_mi, shannon_entropy_kl
from prompts import make_pairs

ROOT = Path(__file__).resolve().parent


# --------------------------------------------------------------------------- #
# Feature extraction                                                          #
# --------------------------------------------------------------------------- #

@torch.no_grad()
def extract(model, tokenizer, prompts, layer: int, device: str = "cpu"):
    """For each prompt return (D, M, Y_internal) where
        D          = mean prompt-token embedding,
        M          = last-token hidden state at `layer`,
        Y_internal = last-token logits (full vocab) — the falsified
                     single-channel Y used as a baseline."""
    Ds, Ms, Ys = [], [], []
    embed = model.get_input_embeddings()
    for p in prompts:
        ids = tokenizer(p, return_tensors="pt", truncation=True, max_length=64).input_ids.to(device)
        emb = embed(ids)
        D = emb.squeeze(0).mean(dim=0).cpu().numpy()
        out = model(ids, output_hidden_states=True, use_cache=False)
        M = out.hidden_states[layer][0, -1].cpu().numpy()
        Y = out.logits[0, -1].cpu().numpy()
        Ds.append(D); Ms.append(M); Ys.append(Y)
    return np.array(Ds), np.array(Ms), np.array(Ys)


def build_y(mode: str, answers: list[str], y_internal: np.ndarray,
            encoder_name: str, cache_dir: str, device: str) -> np.ndarray:
    if mode == "logits":
        return y_internal
    if mode == "external_hash":
        return y_external_hash(answers, dim=32)
    if mode == "external_encoder":
        return y_external_encoder(answers, encoder_name=encoder_name,
                                  cache_dir=cache_dir, device=device)
    raise SystemExit(f"unknown y_mode: {mode}")


def reduce_pca(X: np.ndarray, n: int) -> np.ndarray:
    if X.shape[1] > n:
        X = PCA(n_components=n, random_state=0).fit_transform(X)
    # z-score per axis: KSG with Chebyshev metric is scale-sensitive,
    # and raw logits / hidden states have axis-spreads spanning many orders.
    mu = X.mean(axis=0, keepdims=True)
    sd = X.std(axis=0, keepdims=True) + 1e-9
    return (X - mu) / sd


# --------------------------------------------------------------------------- #
# Layer-1 Shannon bound diagnostic                                            #
# --------------------------------------------------------------------------- #

def shannon_excess(D: np.ndarray, M: np.ndarray, Y: np.ndarray) -> dict:
    """Layer 1: I(D;Y) + I(M;Y) ≤ H(Y). KSG MI in nats, KL entropy in nats."""
    I_DY = ksg_mi(D, Y, k=5) * NATS_TO_BITS
    I_MY = ksg_mi(M, Y, k=5) * NATS_TO_BITS
    H_Y = shannon_entropy_kl(Y, k=5) * NATS_TO_BITS
    excess = (I_DY + I_MY) - H_Y
    return {"I_DY": I_DY, "I_MY": I_MY, "H_Y": H_Y, "excess_bits": excess}


# --------------------------------------------------------------------------- #
# Main                                                                        #
# --------------------------------------------------------------------------- #

def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="gpt2")
    p.add_argument("--layer", type=int, default=6, help="hidden-state layer (1..n_layers)")
    p.add_argument("--pca", type=int, default=5)
    p.add_argument("--n_prompts", type=int, default=200, help="cap; use 0 for full corpus")
    p.add_argument("--y_modes", default="logits,external_hash,external_encoder",
                   help="comma-separated subset of {logits, external_hash, external_encoder}")
    p.add_argument("--encoder", default="sentence-transformers/all-MiniLM-L6-v2",
                   help="encoder model name for y_mode=external_encoder")
    p.add_argument("--out", default=str(ROOT / "results_smoke.json"))
    p.add_argument("--cache_dir", default=os.environ.get("HF_HOME", str(ROOT / ".hf_cache")))
    args = p.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[setup] device={device}  model={args.model}  layer={args.layer}  pca={args.pca}")
    print(f"[setup] y_modes={args.y_modes}")

    t0 = time.time()
    tokenizer = AutoTokenizer.from_pretrained(args.model, cache_dir=args.cache_dir)
    if tokenizer.pad_token is None:
        tokenizer.pad_token = tokenizer.eos_token
    model = AutoModelForCausalLM.from_pretrained(args.model, cache_dir=args.cache_dir).to(device)
    model.eval()
    print(f"[setup] model loaded in {time.time()-t0:.1f}s  n_layers={model.config.num_hidden_layers}")

    pairs = make_pairs()
    if args.n_prompts > 0:
        pairs = pairs[: args.n_prompts]
    ungrounded = [(i, c, p, a) for (i, c, p, a) in pairs if c == "ungrounded"]
    grounded = [(i, c, p, a) for (i, c, p, a) in pairs if c == "grounded"]
    print(f"[setup] prompts: {len(ungrounded)} ungrounded, {len(grounded)} grounded")

    y_modes = [m.strip() for m in args.y_modes.split(",") if m.strip()]

    results: dict = {
        "model": args.model,
        "layer": args.layer,
        "pca_dim": args.pca,
        "y_modes": y_modes,
        "encoder": args.encoder,
        "n_ungrounded": len(ungrounded),
        "n_grounded": len(grounded),
        "constants": {"k_ksg": 5, "NATS_TO_BITS": float(NATS_TO_BITS)},
        "conditions": {},
    }

    for label, group in [("ungrounded", ungrounded), ("grounded", grounded)]:
        if len(group) < 25:
            print(f"[skip] {label}: too few prompts ({len(group)})")
            continue
        t0 = time.time()
        prompts_only = [p for (_, _, p, _) in group]
        answers_only = [a for (_, _, _, a) in group]
        Draw, Mraw, Yraw = extract(model, tokenizer, prompts_only, args.layer, device)
        print(f"[{label}] extracted ({Draw.shape}, {Mraw.shape}, {Yraw.shape}) in {time.time()-t0:.1f}s")

        D_pca = reduce_pca(Draw, args.pca)
        M_pca = reduce_pca(Mraw, args.pca)

        results["conditions"][label] = {}
        for ymode in y_modes:
            t1 = time.time()
            Y_raw_y = build_y(ymode, answers_only, Yraw, args.encoder, args.cache_dir, device)
            Y_pca = reduce_pca(Y_raw_y, args.pca)
            I_DMY = ksg_cmi(D_pca, M_pca, Y_pca, k=5) * NATS_TO_BITS
            I_DM = ksg_mi(D_pca, M_pca, k=5) * NATS_TO_BITS
            shannon = shannon_excess(D_pca, M_pca, Y_pca)
            results["conditions"][label][ymode] = {
                "I_DM_Y_bits": I_DMY,
                "I_DM_bits": I_DM,
                **shannon,
                "Y_raw_shape": list(Y_raw_y.shape),
            }
            print(f"[{label}/{ymode}] I(D;M|Y)={I_DMY:.4f}  I(D;Y)={shannon['I_DY']:.4f}  "
                  f"I(M;Y)={shannon['I_MY']:.4f}  H(Y)={shannon['H_Y']:.4f}  "
                  f"excess={shannon['excess_bits']:+.4f}  in {time.time()-t1:.1f}s")

    # ---- KC verdicts ------------------------------------------------------- #
    verdicts: dict = {}
    cond = results["conditions"]
    if "ungrounded" in cond and "logits" in cond["ungrounded"]:
        u = cond["ungrounded"]["logits"]
        verdicts["KC_i_Shannon_bound_ungrounded_logits"] = (
            "PASS" if u["excess_bits"] < 0.05 else "FAIL"
        ) + f"  (excess = {u['excess_bits']:+.4f} bits, threshold < 0.05)"
        verdicts["KC_ii_internal_penalty_positive_logits"] = (
            "PASS" if u["I_DM_Y_bits"] > 0.0 else "FAIL"
        ) + f"  (I(D;M|Y) = {u['I_DM_Y_bits']:.4f} bits)"

    # KC-(iii) original — text-prefix ungrounded vs grounded, same y_mode.
    # Pre-registered FAIL is expected: text-prefix isn't structural.
    if "ungrounded" in cond and "grounded" in cond and "logits" in cond["ungrounded"]:
        u = cond["ungrounded"]["logits"]["I_DM_Y_bits"]
        g = cond["grounded"]["logits"]["I_DM_Y_bits"]
        r = u / max(g, 1e-9)
        verdicts["KC_iii_three_point_fix_text_prefix"] = (
            "PASS" if r > 1.5 else "FAIL"
        ) + f"  (ratio u/g = {r:.2f}×, threshold > 1.5×) — text-prefix is NOT structural three-point geometry"

    # KC-(iii)-amended — structural three-point fix via external Y.
    #
    # Smoke result: BOTH external Y variants give HIGHER I(D;M|Y) than logits Y.
    # The ratio I_int/I_ext is reported as a diagnostic, not a verdict.
    # Reading: conditioning on Y_logits removes (D,M) correlation because
    # logits are a tight summary of M (Y is in the model's internal chain).
    # An external Y not in the chain soaks up less correlation, so I_ext > I_int.
    # The framework's three-point fix is NOT operationalized by swapping
    # the Y variable — it requires intervening on the (D,M,Y) coupling
    # (e.g. ablating attention heads, swapping to an undertrained model)
    # with Y fixed. The external-Y machinery still has uses: it gives an
    # internal/external diagnostic of how much of the (D,M) coupling is
    # captured by the model's own output, which is a separate question.
    if "ungrounded" in cond:
        u = cond["ungrounded"]
        for ext_mode in ("external_hash", "external_encoder"):
            if ext_mode not in u:
                continue
            I_int = u.get("logits", {}).get("I_DM_Y_bits", float("nan"))
            I_ext = u[ext_mode]["I_DM_Y_bits"]
            ratio_ext_over_int = I_ext / max(I_int, 1e-9)
            verdicts[f"DIAG_internal_vs_{ext_mode}"] = (
                f"I_ext/I_int = {ratio_ext_over_int:.2f}×  "
                f"(I_int={I_int:.4f} I_ext={I_ext:.4f} bits) — "
                f"diagnostic only, not a KC verdict; see README §smoke-findings"
            )

    verdicts["KC_iv_structure_theorem"] = "N/A (requires base+SFT pair, out of smoke scope)"
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
