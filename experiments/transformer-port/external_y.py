"""external_y.py — structurally-separate Y channel for KC-(iii) (Paper 186 §10.2).

The smoke run's KC-(iii) failed because a text-prefix "system message" is NOT
three-point geometry — D, M, and the supposed Y reference all share the same
input channel of the same model. The framework predicts the penalty only drops
when Y is **structurally separate** from (D, M): produced by a disjoint
computational path with its own weights, vocabulary, and graph.

Two flavors of structurally-separate Y, both encoding the ground-truth answer
from prompts.py::PROMPT_ANSWERS:

  external_hash:
      Char-trigram random-feature hashing of the answer string. Zero extra
      models, no downloads, deterministic. Tests **pure structural separation**:
      Y carries the answer identity but no semantic dependency on the
      generator. If KC-(iii) PASSes here, the three-point fix is a property
      of channel separation per se, not of having a "smart" reference.

  external_encoder:
      Sentence/CLS embedding from a separately-loaded small encoder
      (default: sentence-transformers/all-MiniLM-L6-v2, ≈80MB, or
      distilbert-base-uncased via plain transformers, ≈250MB). Tests
      **semantically-meaningful structural separation**: Y carries both the
      answer identity AND a real semantic representation, but the encoder's
      weights and architecture are disjoint from the generator. Closest
      analog to "external classifier head" in the framework's apparatus.

Internal-Y baseline (the falsified single-channel form) is just the model's
own last-token logits, kept in run_ksg_transformer.py as `y_mode=logits`.
"""

from __future__ import annotations

import hashlib
import numpy as np
import torch
from transformers import AutoModel, AutoTokenizer


# --------------------------------------------------------------------------- #
# Variant A — char-trigram random-feature hash                                #
# --------------------------------------------------------------------------- #

def _trigrams(s: str) -> list[str]:
    s = s.lower().strip()
    s = f"^^{s}$$"
    return [s[i:i+3] for i in range(len(s) - 2)]


def hash_to_index(token: str, dim: int) -> int:
    h = hashlib.md5(token.encode("utf-8")).digest()
    return int.from_bytes(h[:4], "big") % dim


def hash_to_sign(token: str) -> int:
    h = hashlib.md5(token.encode("utf-8")).digest()
    return 1 if h[4] & 1 else -1


def y_external_hash(answers: list[str], dim: int = 32) -> np.ndarray:
    """Char-trigram random-feature hash, signed, L2-normalized.

    Each answer string → trigram bag → hashed to `dim`-dim sparse vector
    with random signs (Charikar 2002 sketch). Same answer → same vector
    deterministically. Different answers → near-orthogonal with high
    probability for `dim` ≥ vocabulary_size / 4.
    """
    out = np.zeros((len(answers), dim), dtype=np.float64)
    for r, ans in enumerate(answers):
        for tri in _trigrams(ans):
            j = hash_to_index(tri, dim)
            s = hash_to_sign(tri)
            out[r, j] += s
    # L2 normalize
    norms = np.linalg.norm(out, axis=1, keepdims=True) + 1e-9
    return out / norms


# --------------------------------------------------------------------------- #
# Variant B — frozen separate encoder                                         #
# --------------------------------------------------------------------------- #

@torch.no_grad()
def y_external_encoder(
    answers: list[str],
    encoder_name: str = "sentence-transformers/all-MiniLM-L6-v2",
    cache_dir: str | None = None,
    device: str = "cpu",
) -> np.ndarray:
    """Embed each answer via a separately-loaded encoder.

    Default is all-MiniLM-L6-v2 (≈80MB, 384-dim). Fall back to
    distilbert-base-uncased (≈250MB, 768-dim) via the plain transformers
    package if MiniLM isn't reachable. Whatever the encoder, its weights
    and vocabulary are disjoint from the generator under measurement,
    which is what "structurally separate" means.
    """
    tok = AutoTokenizer.from_pretrained(encoder_name, cache_dir=cache_dir)
    enc = AutoModel.from_pretrained(encoder_name, cache_dir=cache_dir).to(device)
    enc.eval()
    embs = []
    for a in answers:
        ids = tok(a, return_tensors="pt", truncation=True, max_length=32).to(device)
        out = enc(**ids)
        # Mean-pool over tokens, attention-masked
        mask = ids["attention_mask"].unsqueeze(-1).float()
        h = out.last_hidden_state
        pooled = (h * mask).sum(dim=1) / mask.sum(dim=1).clamp(min=1)
        embs.append(pooled.squeeze(0).cpu().numpy())
    Y = np.stack(embs, axis=0)
    # L2 normalize (so KSG sees scale-comparable Y across modes)
    norms = np.linalg.norm(Y, axis=1, keepdims=True) + 1e-9
    return Y / norms
