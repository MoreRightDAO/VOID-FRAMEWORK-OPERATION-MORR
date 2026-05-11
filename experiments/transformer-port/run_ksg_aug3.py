"""run_ksg_aug3.py — EXP-HP-WORM-3-MINI-3 Y from frozen-encoded response.

Third in the MINI series. MINI-1 varied M via input-side retrieval (FAIL).
MINI-2 varied Y via frozen encoder on prompt/answer (FAIL on the fix
direction, but reproduced this morning's external_y answer finding).

MINI-3 puts Y in the framework-correct topological position: **downstream
of M through a structurally-separate substrate**. The generator greedy-
decodes a short completion conditioned on the prompt, and a frozen
disjoint encoder (sentence-transformers/all-MiniLM-L6-v2) embeds *only
the completion tokens*. That Y_enc_response is then used as the
conditioning variable.

Y_enc_response is the direct transformer analog of motor output → body
→ world in the worm:
  M (command interneurons) → motor output → body bend → mean(bend) (Y)
  M (transformer hidden) → logits → sampled tokens → encoder-embedded
                                                     completion (Y)

In both, Y is downstream of M (caused by M via a sampling/integration
step) AND in a disjoint computational substrate (muscle physics /
frozen encoder weights).

For reference comparisons we also measure Y_logits and Y_enc_prompt.
Y_logits is M-aligned (linear projection of M); Y_enc_prompt is
D-aligned (encoder on same input as D); Y_enc_response is
M-downstream-through-disjoint-substrate. The framework predicts only
the last operationalization is true three-point geometry.

Variables:
  D = mean prompt-token embedding from generator (PCA-reduced)
  M = generator's last-token hidden state at LAYER (PCA-reduced)
  Y = one of {logits, enc_prompt, enc_response}, PCA-reduced

Pre-registered KCs (locked before run, 2026-05-11 late evening):
  B1: I(D;M|Y_logits) > 0                                    (sanity)
  B2: I(D;M|Y_enc_response) / I(D;M|Y_logits) < 1/1.5        (3pt fix)
  B3: I(D;M|Y_enc_response) < I(D;M|Y_enc_prompt)            (downstream-of-M
                                                              beats parallel-
                                                              to-D)

Usage:
    python3 run_ksg_aug3.py                       # default: gpt2, layer 6, N=50, 8 tok
    python3 run_ksg_aug3.py --layer 8 --n_gen 10
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
from transformers import AutoModel, AutoModelForCausalLM, AutoTokenizer

from ksg import NATS_TO_BITS, ksg_cmi, ksg_mi, shannon_entropy_kl
from prompts import PROMPT_ANSWERS

ROOT = Path(__file__).resolve().parent


@torch.no_grad()
def extract_gen(model, tokenizer, prompts, layer: int, n_gen: int, device: str):
    """Return (D, M, Y_logits, completions[]).

    D = mean prompt-token embedding.
    M = last-token hidden state at `layer` after processing prompt only.
    Y_logits = last-token logits after prompt only.
    completions[i] = text of `n_gen` greedy-decoded tokens following
                     prompt i. Decoded from the *same model* — Y_response
                     downstream of M by construction.
    """
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
            ids, max_new_tokens=n_gen,
            do_sample=False, num_beams=1,
            pad_token_id=eos, use_cache=True,
        )
        # Strip the prompt portion; keep only completion tokens.
        completion_ids = gen_ids[0, ids.shape[1]:]
        completion_text = tokenizer.decode(completion_ids, skip_special_tokens=True)
        comps.append(completion_text)

    return np.array(Ds), np.array(Ms), np.array(Ys), comps


@torch.no_grad()
def encode_texts(tok, enc, texts, device: str) -> np.ndarray:
    """Frozen encoder hidden state, mean-pooled with attention mask."""
    out_vecs = []
    for t in texts:
        # Tokenizer can return empty for trivially-empty strings; guard.
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


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--model", default="gpt2")
    p.add_argument("--encoder", default="sentence-transformers/all-MiniLM-L6-v2")
    p.add_argument("--layer", type=int, default=6)
    p.add_argument("--pca", type=int, default=5)
    p.add_argument("--n", type=int, default=50)
    p.add_argument("--n_gen", type=int, default=8,
                   help="generated token count for Y_enc_response")
    p.add_argument("--out", default=str(ROOT / "results_aug3.json"))
    p.add_argument("--cache_dir",
                   default=os.environ.get("HF_HOME", str(ROOT / ".hf_cache")))
    args = p.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[setup] device={device}  generator={args.model}  encoder={args.encoder}")
    print(f"[setup] layer={args.layer}  pca={args.pca}  n={args.n}  n_gen={args.n_gen}")

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
    print(f"[gen] D={Draw.shape}  M={Mraw.shape}  Y_logits={Ylogits_raw.shape}  "
          f"completions={len(completions)} in {time.time()-t0:.1f}s")
    print(f"[gen] example completion[0]: {completions[0]!r}")
    print(f"[gen] example completion[1]: {completions[1]!r}")

    t0 = time.time()
    Yenc_prompt_raw = encode_texts(enc_tok, enc, prompts, device)
    Yenc_response_raw = encode_texts(enc_tok, enc, completions, device)
    print(f"[enc] Y_enc_prompt={Yenc_prompt_raw.shape}  "
          f"Y_enc_response={Yenc_response_raw.shape}  in {time.time()-t0:.1f}s")

    D = reduce_pca(Draw, args.pca)
    M = reduce_pca(Mraw, args.pca)

    results = {
        "experiment": "EXP-HP-WORM-3-MINI-3",
        "generator": args.model, "encoder": args.encoder,
        "layer": args.layer, "pca_dim": args.pca,
        "n_prompts": len(prompts), "n_gen_tokens": args.n_gen,
        "constants": {"k_ksg": 5, "NATS_TO_BITS": float(NATS_TO_BITS)},
        "completions_sample": completions[:10],
        "y_modes": {},
    }
    results["y_modes"]["logits"] = measure(D, M, Ylogits_raw, args.pca, "Y_logits")
    results["y_modes"]["enc_prompt"] = measure(D, M, Yenc_prompt_raw, args.pca, "Y_enc_prompt")
    results["y_modes"]["enc_response"] = measure(D, M, Yenc_response_raw, args.pca, "Y_enc_response")

    I_logits = results["y_modes"]["logits"]["I_DM_Y_bits"]
    I_prompt = results["y_modes"]["enc_prompt"]["I_DM_Y_bits"]
    I_response = results["y_modes"]["enc_response"]["I_DM_Y_bits"]
    ratio_response = I_response / max(I_logits, 1e-9)

    verdicts = {}
    verdicts["B1_sanity"] = (
        ("PASS" if I_logits > 0 else "FAIL") +
        f"  (I(D;M|Y_logits) = {I_logits:.4f} bits)"
    )
    verdicts["B2_three_point_fix_via_M_downstream_disjoint_Y"] = (
        ("PASS" if ratio_response < (1.0 / 1.5) else "FAIL") +
        f"  (enc_response/logits = {ratio_response:.3f}, threshold < {1.0/1.5:.3f})"
    )
    verdicts["B3_response_beats_prompt_aligned_Y"] = (
        ("PASS" if I_response < I_prompt else "FAIL") +
        f"  (enc_response={I_response:.4f} vs enc_prompt={I_prompt:.4f} bits)"
    )
    results["ratios"] = {
        "enc_response_over_logits": ratio_response,
        "enc_response_over_enc_prompt": I_response / max(I_prompt, 1e-9),
        "enc_prompt_over_logits": I_prompt / max(I_logits, 1e-9),
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
