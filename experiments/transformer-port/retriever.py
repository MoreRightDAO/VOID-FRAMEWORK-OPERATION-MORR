"""retriever.py — char-trigram TF-IDF retriever for EXP-HP-WORM-3-MINI.

Pure-Python (numpy only). The retrieval channel for the lightest possible
KC-(iii)' attempt: a structurally-separate computational path that produces
context to be prepended to a prompt before the generator sees it. No
embedding model, no neural net, zero downloads.

The corpus is built from `prompts.PROMPT_ANSWERS` at import time as
natural-language fact statements ('{prompt} {answer}.'). The retriever
returns the top-1 fact for a query via cosine over char-trigram TF-IDF
vectors. `retrieve_random` returns a deterministic-random different fact
for the structural-separation specificity control.

Trigram conventions match `external_y.py::_trigrams` so this stays
substitutable into the existing port if we want.
"""

from __future__ import annotations

import hashlib
import numpy as np

from prompts import PROMPT_ANSWERS


def _trigrams(s: str) -> list[str]:
    s = s.lower().strip()
    s = f"^^{s}$$"
    return [s[i:i+3] for i in range(len(s) - 2)]


def _build_corpus() -> list[str]:
    return [f"{p.strip()} {a.strip()}." for (p, a) in PROMPT_ANSWERS]


CORPUS = _build_corpus()


def _doc_freqs(corpus: list[str]) -> dict[str, int]:
    df: dict[str, int] = {}
    for doc in corpus:
        for tri in set(_trigrams(doc)):
            df[tri] = df.get(tri, 0) + 1
    return df


def _tfidf_vec(text: str, df: dict[str, int], n_docs: int) -> dict[str, float]:
    tris = _trigrams(text)
    tf: dict[str, int] = {}
    for tri in tris:
        tf[tri] = tf.get(tri, 0) + 1
    vec: dict[str, float] = {}
    for tri, count in tf.items():
        idf = np.log((1.0 + n_docs) / (1.0 + df.get(tri, 0))) + 1.0
        vec[tri] = count * idf
    norm = np.sqrt(sum(v * v for v in vec.values())) + 1e-9
    return {t: v / norm for t, v in vec.items()}


def _cosine(a: dict[str, float], b: dict[str, float]) -> float:
    keys = set(a) & set(b)
    return float(sum(a[k] * b[k] for k in keys))


_DF = _doc_freqs(CORPUS)
_N = len(CORPUS)
_CORPUS_VECS = [_tfidf_vec(d, _DF, _N) for d in CORPUS]


def retrieve_top1(query: str) -> tuple[int, str, float]:
    """Return (index, fact, score) of the highest-scoring fact for query.

    On this corpus the query is typically a prefix of its matching fact, so
    top-1 will reliably be the correct answer fact. That is fine: the
    framework's prediction is about *structural separation* between the
    retrieval channel and the generator, not about retrieval cleverness.
    """
    qv = _tfidf_vec(query, _DF, _N)
    scores = [_cosine(qv, dv) for dv in _CORPUS_VECS]
    j = int(np.argmax(scores))
    return j, CORPUS[j], scores[j]


def retrieve_random(query: str, seed: int) -> tuple[int, str, float]:
    """Return a deterministically-random fact other than top-1.

    Structural-separation specificity control: same channel topology as
    top-1 retrieval, but the channel carries an uninformative payload.
    """
    j_top, _, _ = retrieve_top1(query)
    h = hashlib.md5((query + "|" + str(seed)).encode("utf-8")).digest()
    j = int.from_bytes(h[:4], "big") % _N
    if j == j_top:
        j = (j + 1) % _N
    return j, CORPUS[j], 0.0


if __name__ == "__main__":
    # Smoke print
    for p, _ in PROMPT_ANSWERS[:5]:
        j, fact, s = retrieve_top1(p)
        jr, factr, _ = retrieve_random(p, seed=42)
        print(f"prompt: {p!r}")
        print(f"  top1[{j}] (s={s:.3f}): {fact}")
        print(f"  rand[{jr}]: {factr}")
