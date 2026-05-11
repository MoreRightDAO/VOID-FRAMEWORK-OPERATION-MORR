"""ksg.py — KSG mutual-information and conditional-MI estimators.

Direct port of the substrate-agnostic estimators from
`ops/lab/worm-sim/sim_v3_5_synapse.py`. Same algorithm (Kraskov-Stögbauer-
Grassberger 2004 for MI; Frenzel-Pompe 2007 for CMI), same Chebyshev metric,
same kth-nearest-neighbor procedure. The methodological deliverable of
Paper 186 §10.3.

ksg_cmi(D, M, Y, k=5)  →  I(D;M|Y) in nats; multiply by NATS_TO_BITS for bits.
"""

from __future__ import annotations

import numpy as np
from scipy.spatial import cKDTree
from scipy.special import digamma

NATS_TO_BITS = 1.0 / np.log(2)


def _to_2d(a: np.ndarray) -> np.ndarray:
    a = np.asarray(a, dtype=np.float64)
    return a.reshape(-1, 1) if a.ndim == 1 else a


def ksg_mi(x: np.ndarray, y: np.ndarray, k: int = 5) -> float:
    """I(X;Y) via KSG algorithm 1 (Chebyshev metric)."""
    x = _to_2d(x); y = _to_2d(y); n = len(x)
    xy = np.hstack([x, y])
    tree_xy = cKDTree(xy)
    dist, _ = tree_xy.query(xy, k=k + 1, p=np.inf)
    eps = dist[:, k] - 1e-10
    tx = cKDTree(x); ty = cKDTree(y)
    nx = np.array(tx.query_ball_point(x, r=eps, p=np.inf, return_length=True)) - 1
    ny = np.array(ty.query_ball_point(y, r=eps, p=np.inf, return_length=True)) - 1
    mi = digamma(k) + digamma(n) - float(np.mean(digamma(nx + 1) + digamma(ny + 1)))
    return float(max(mi, 0.0))


def ksg_cmi(x: np.ndarray, y: np.ndarray, z: np.ndarray, k: int = 5) -> float:
    """I(X;Y|Z) via Frenzel-Pompe.
       I(X;Y|Z) = ψ(k) − <ψ(n_xz+1) + ψ(n_yz+1) − ψ(n_z+1)>"""
    x = _to_2d(x); y = _to_2d(y); z = _to_2d(z); n = len(x)
    xyz = np.hstack([x, y, z])
    tree = cKDTree(xyz)
    dist, _ = tree.query(xyz, k=k + 1, p=np.inf)
    eps = dist[:, k] - 1e-10
    xz = np.hstack([x, z]); yz = np.hstack([y, z])
    n_xz = np.array(cKDTree(xz).query_ball_point(xz, r=eps, p=np.inf, return_length=True)) - 1
    n_yz = np.array(cKDTree(yz).query_ball_point(yz, r=eps, p=np.inf, return_length=True)) - 1
    n_z = np.array(cKDTree(z).query_ball_point(z, r=eps, p=np.inf, return_length=True)) - 1
    cmi = digamma(k) - float(np.mean(digamma(n_xz + 1) + digamma(n_yz + 1) - digamma(n_z + 1)))
    return float(max(cmi, 0.0))


def shannon_entropy_kl(x: np.ndarray, k: int = 5) -> float:
    """Kozachenko-Leonenko entropy estimator (nats).
    H(X) = ψ(n) − ψ(k) + log(c_d) + (d/n) · Σ log(2·ε_i)
    Chebyshev metric → c_d = 1 (unit ℓ∞ ball volume)."""
    x = _to_2d(x); n, d = x.shape
    tree = cKDTree(x)
    dist, _ = tree.query(x, k=k + 1, p=np.inf)
    eps = dist[:, k]
    eps = np.where(eps == 0, 1e-10, eps)
    h = digamma(n) - digamma(k) + (d / n) * float(np.sum(np.log(2 * eps)))
    return float(h)
