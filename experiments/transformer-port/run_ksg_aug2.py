"""run_ksg_aug2.py — EXP-HP-WORM-3-MINI-2 second-model Y on the prompt.

Sibling experiment to EXP-HP-WORM-3-MINI. MINI-1 varied M by routing
through a structurally-separate retrieval channel (FAIL on input-level
augmentation, PASS on informative-specificity null). MINI-2 varies Y
by routing it through a structurally-separate second model (frozen
disjoint encoder applied to the same prompt the generator sees).

The framework reading: Y now lives in a computational graph that shares
no weights with (D, M). This is the (D, M, Y) triple's first ever
structurally-separate Y on a transformer.

Variables (D and M identical to MINI-1):
  D = mean prompt-token embedding from generator (PCA-reduced)
  M = generator's last-token hidden state at LAYER (PCA-reduced)

Four Y variants, three measured one used as a sanity diagnostic:
  Y_logits         = generator's last-token logits (the falsified
                     single-channel form; reproduces MINI-1 base)
  Y_enc_prompt     = frozen encoder's mean-pooled hidden state on the
                     PROMPT (new — structurally-separate Y of the
                     generator's input)
  Y_enc_answer     = frozen encoder's mean-pooled hidden state on the
                     canonical answer (replication of this morning's
                     `external_encoder` Y test; expected high penalty
                     because Y is not aligned with M's content)

Pre-registered KCs (locked 2026-05-11 evening, before run):
  A1: I(D;M|Y_logits) > 0                                      (sanity)
  A2: I(D;M|Y_enc_prompt) / I(D;M|Y_logits) < 1/1.5            (three-point
                                                                fix via
                                                                structural
                                                                Y on prompt)
  A3: I(D;M|Y_enc_answer) / I(D;M|Y_logits) > 1.2              (replicates
                                                                this
                                                                morning's
                                                                external_y
                                                                answer test)

Usage:
    python3 run_ksg_aug2.py                       # default: gpt2, layer 6, N=50
    python3 run_ksg_aug2.py --layer 8 --pca 5
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
def extract_gen(model, tokenizer, prompts, layer: int, device: str):
    """Return generator-side (D, M, Y_logits) for each prompt."""
    Ds, Ms, Ys = [], [], []
    embed = model.get_input_embeddings()
    for p in prompts:
        ids = tokenizer(p, return_tensors="pt",
                        truncation=True, max_length=64).input_ids.to(device)
        D = embed(ids).squeeze(0).mean(dim=0).cpu().numpy()
        out = model(ids, output_hidden_states=True, use_cache=False)
        M = out.hidden_states[layer][0, -1].cpu().numpy()
        Y = out.logits[0, -1].cpu().numpy()
        Ds.append(D); Ms.append(M); Ys.append(Y)
    return np.array(Ds), np.array(Ms), np.array(Ys)


@torch.no_grad()
def encode_texts(tok, enc, texts, device: str) -> np.ndarray:
    """Frozen encoder hidden state, mean-pooled with attention mask."""
    out_vecs = []
    for t in texts:
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
    p.add_argument("--out", default=str(ROOT / "results_aug2.json"))
    p.add_argument("--cache_dir",
                   default=os.environ.get("HF_HOME", str(ROOT / ".hf_cache")))
    args = p.parse_args()

    device = "cuda" if torch.cuda.is_available() else "cpu"
    print(f"[setup] device={device}  generator={args.model}  encoder={args.encoder}")
    print(f"[setup] layer={args.layer}  pca={args.pca}  n={args.n}")

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
    answers = [aa for (_, aa) in PROMPT_ANSWERS][: args.n]

    t0 = time.time()
    Draw, Mraw, Ylogits_raw = extract_gen(gen, gen_tok, prompts, args.layer, device)
    print(f"[gen] D={Draw.shape}  M={Mraw.shape}  Y_logits={Ylogits_raw.shape}  in {time.time()-t0:.1f}s")
    t0 = time.time()
    Yenc_prompt_raw = encode_texts(enc_tok, enc, prompts, device)
    Yenc_answer_raw = encode_texts(enc_tok, enc, answers, device)
    print(f"[enc] Y_enc_prompt={Yenc_prompt_raw.shape}  Y_enc_answer={Yenc_answer_raw.shape}  in {time.time()-t0:.1f}s")

    D = reduce_pca(Draw, args.pca)
    M = reduce_pca(Mraw, args.pca)

    results = {
        "experiment": "EXP-HP-WORM-3-MINI-2",
        "generator": args.model, "encoder": args.encoder,
        "layer": args.layer, "pca_dim": args.pca,
        "n_prompts": len(prompts),
        "constants": {"k_ksg": 5, "NATS_TO_BITS": float(NATS_TO_BITS)},
        "y_modes": {},
    }
    results["y_modes"]["logits"] = measure(D, M, Ylogits_raw, args.pca, "Y_logits")
    results["y_modes"]["enc_prompt"] = measure(D, M, Yenc_prompt_raw, args.pca, "Y_enc_prompt")
    results["y_modes"]["enc_answer"] = measure(D, M, Yenc_answer_raw, args.pca, "Y_enc_answer")

    I_logits = results["y_modes"]["logits"]["I_DM_Y_bits"]
    I_prompt = results["y_modes"]["enc_prompt"]["I_DM_Y_bits"]
    I_answer = results["y_modes"]["enc_answer"]["I_DM_Y_bits"]
    ratio_prompt = I_prompt / max(I_logits, 1e-9)
    ratio_answer = I_answer / max(I_logits, 1e-9)

    verdicts = {}
    verdicts["A1_sanity"] = (
        ("PASS" if I_logits > 0 else "FAIL") +
        f"  (I(D;M|Y_logits) = {I_logits:.4f} bits)"
    )
    verdicts["A2_three_point_fix_structural_Y_on_prompt"] = (
        ("PASS" if ratio_prompt < (1.0 / 1.5) else "FAIL") +
        f"  (enc_prompt/logits = {ratio_prompt:.3f}, threshold < {1.0/1.5:.3f})"
    )
    verdicts["A3_replicate_external_y_on_answer_high"] = (
        ("PASS" if ratio_answer > 1.2 else "FAIL") +
        f"  (enc_answer/logits = {ratio_answer:.3f}, threshold > 1.2)"
    )
    results["ratios"] = {
        "enc_prompt_over_logits": ratio_prompt,
        "enc_answer_over_logits": ratio_answer,
        "enc_answer_over_enc_prompt": I_answer / max(I_prompt, 1e-9),
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
