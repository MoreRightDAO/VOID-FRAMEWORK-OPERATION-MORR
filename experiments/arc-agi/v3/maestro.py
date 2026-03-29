#!/usr/bin/env python3
"""ARC-AGI-3 Maestro — The Conductor.

Meta-orchestrator that conducts the solver ensemble using Eckert manifold
geometry. Replaces ensemble_solver.py as the top-level entry point.

What the Maestro does that the ensemble doesn't:
  1. SHARED STATE: All solvers read/write the same knowledge pool
  2. BARRIER-CALIBRATED BUDGETS: π/√2 × N_mechanisms per exploration phase
  3. φ GRADIENT CONDUCTING: picks solver with steepest thermodynamic descent
  4. KILL SWITCHES: Fantasia saturation, φ stall, holonomy novelty
  5. PERSISTENT LEARNING: GameLedger (per-game) + CrossGameLedger (transfer)
  6. MULTI-ATTEMPT: evolves strategy order across attempts
  7. PADÉ EXTRAPOLATION: predicts solver convergence from early trajectory

Math apparatus:
  HP203  JKO gradient flow — F(Pe) monotonically decreasing
  HP204  PID decomposition — unique/redundant/synergistic per solver
  §136D2 Barrier universality — exploration budget per mechanism
  §2B    Fantasia Bound — saturation gate
  §101   Holonomy — geometric novelty tracking
  §177   Padé — convergence prediction

Usage:
  python3 maestro.py --all -q --compete     # Competition mode
  python3 maestro.py --all -q               # Full eval mode
  python3 maestro.py cd82 -v                # Single game, verbose
  python3 maestro.py --all --attempts 3     # Multi-attempt learning
  python3 maestro.py --all --resume         # Load ledgers, continue learning
"""

import sys
import os
import time
import json
import argparse
import traceback
from dataclasses import dataclass, field
from typing import Optional

# Ensure v3 modules importable
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import numpy as np
import arc_agi
from arcengine import GameState

from packet_probe import probe_game, GameProfile, frame_hash
from packet_analyzer import shannon_entropy
from ensemble_solver import dispatch_solvers
from spectral_engine import estimate_mechanisms, coordination_barrier, ChebyshevGrammar
from shared_state import SharedState, GameLedger, CrossGameLedger
from eckert_math import (
    jko_gradient, pade_extrapolate, holonomy_deficit,
    pid_decompose, chebyshev_fingerprint, game_similarity,
)

# Solver imports
import packet_solver
import recursive_solver
import instanton_planner
import aaa_solver
import eckert_simulator

# LLM hybrid — the pro gamer brain
try:
    from llm_hybrid import HybridSolver as LLMHybridSolver
    from llm_solver import BACKEND as LLM_BACKEND
    HAS_LLM = LLM_BACKEND != 'none'
except Exception:
    HAS_LLM = False



def _solve_one_level_on_env(solver_name: str, profile: GameProfile,
                            env, obs, shared: SharedState,
                            budget: int = 300) -> tuple:
    """Solve ONE level using the specified solver. Returns (result, new_obs).

    Each solver's solve_level() attempts the current level only.
    If it succeeds, obs.levels_completed increments.
    If it fails, obs is still valid for another solver to retry.
    """
    start_level = obs.levels_completed if hasattr(obs, 'levels_completed') else 0

    if solver_name == 'packet':
        gt = profile.game_type
        solver_class = {
            "AGENT-KB": packet_solver.GreedyNavSolver,
            "AGENT-HYBRID": packet_solver.GreedyNavSolver,
            "CLICK-ONLY": packet_solver.ClickScanSolver,
            "FIELD": packet_solver.FieldSolver,
            "LOCKED": packet_solver.DeepScanSolver,
        }.get(gt, packet_solver.ClickScanSolver)

        solver = solver_class(profile, env, obs)
        solver.max_actions = budget
        solved = solver.solve_level()
        acts = solver.actions_taken
        return {
            'level_solved': solved,
            'total_actions': acts,
            'final_phi': 0.0,
        }, solver.obs

    elif solver_name == 'instanton':
        solver = instanton_planner.InstantonPlanner(
            profile, env, obs, shared_state=shared)
        solved = solver.solve_level()
        acts = solver.total_actions
        phi = 0.0
        det = getattr(solver, '_detector', None)
        if det and hasattr(det, 'snapshots') and det.snapshots:
            phi = max(s.phi for s in det.snapshots)
        shared.absorb_from_solver(solver_name, solver)
        return {
            'level_solved': solved,
            'total_actions': acts,
            'final_phi': phi,
        }, solver.obs

    elif solver_name == 'aaa':
        solver = aaa_solver.AAASolver(
            profile, env, obs, shared_state=shared)
        solved = solver.solve_level()
        acts = solver.total_actions
        phi = 0.0
        det = getattr(solver.eckert, 'detector', None)
        if det and hasattr(det, 'snapshots') and det.snapshots:
            phi = max(s.phi for s in det.snapshots)
        shared.absorb_from_solver(solver_name, solver)
        return {
            'level_solved': solved,
            'total_actions': acts,
            'final_phi': phi,
        }, solver.obs

    elif solver_name == 'recursive':
        solver = recursive_solver.RecursiveSolver(
            profile, env, obs, budget_per_level=budget,
            shared_state=shared)
        solved = solver.solve_level()
        acts = solver.total_actions
        shared.absorb_from_solver(solver_name, solver)
        return {
            'level_solved': solved,
            'total_actions': acts,
            'final_phi': 0.0,
        }, solver.obs

    elif solver_name == 'eckert':
        sim = eckert_simulator.EckertSimulator(
            profile, shared_state=shared)
        solved, new_obs, acts = sim.solve_level(env, obs, budget=budget)
        phi = 0.0
        det_summary = sim.detector.summary() if hasattr(sim.detector, 'summary') else {}
        phi = det_summary.get('phi', 0.0)
        shared.absorb_from_solver(solver_name, sim)
        return {
            'level_solved': solved,
            'total_actions': acts,
            'final_phi': phi,
        }, new_obs

    elif solver_name == 'llm' and HAS_LLM:
        solver = LLMHybridSolver(profile, env, obs)
        # Seed with shared knowledge
        shared.seed_into_solver(solver)
        level_num = obs.levels_completed if hasattr(obs, 'levels_completed') else 0
        solved = solver.solve_level(level=level_num, max_actions=budget,
                                    max_llm_calls=6)
        acts = solver.total_actions
        phi = 0.0
        if hasattr(solver, 'detector') and hasattr(solver.detector, 'snapshots'):
            snaps = solver.detector.snapshots
            if snaps:
                phi = max(s.phi for s in snaps)
        shared.absorb_from_solver(solver_name, solver)
        return {
            'level_solved': solved,
            'total_actions': acts,
            'final_phi': phi,
        }, solver.obs

    return {'level_solved': False, 'total_actions': 0, 'final_phi': 0.0}, obs


# ═══════════════════════════════════════════════════════════════════
#  THE MAESTRO
# ═══════════════════════════════════════════════════════════════════

class Maestro:
    """Meta-orchestrator. Conducts solvers using Eckert manifold geometry.

    The manifold IS the conducting surface.
    The φ oracle IS the baton.
    The barrier constant IS the score.
    """

    def __init__(self, game_id: str, budget: int = 500,
                 max_attempts: int = 3, resume: bool = True,
                 verbose: bool = True, compete: bool = False):
        self.game_id = game_id
        self.budget = budget
        self.max_attempts = max_attempts
        self.verbose = verbose
        self.compete = compete

        # Persistent learning
        self.game_ledger = GameLedger()
        self.cross_ledger = CrossGameLedger()

        # Initialize or resume shared state
        if resume:
            loaded = self.game_ledger.load(game_id)
            self.shared = loaded if loaded else SharedState()
            if loaded and verbose:
                s = self.shared.summary()
                print(f"  RESUMED: {s['transitions']} transitions, "
                      f"{s['macros']} macros, {s['atoms']} atoms, "
                      f"φ_best={s['best_phi']:.3f}")
        else:
            self.shared = SharedState()

        # Conducting state
        self.temperature = 1.0
        self.solver_results: dict[str, dict] = {}
        self._attempt_num = 0

    def conduct(self) -> dict:
        """Main entry point. Returns result dict compatible with ensemble."""
        t0 = time.time()

        if self.verbose:
            print(f"\n{'═'*65}")
            print(f"  MAESTRO: {self.game_id}")
            print(f"{'═'*65}")

        # ─── PHASE 1: PROBE (5% budget) ───
        profile = probe_game(self.game_id, budget=30, verbose=False)

        if self.verbose:
            print(f"  Profile: {profile.solver_hint()}")

        # Estimate barriers
        n_mechs = estimate_mechanisms(profile)
        barrier = coordination_barrier(n_mechs)
        self.shared.detector.set_barrier_estimate(n_mechs)

        # Game fingerprint for transfer learning
        first_frame = profile.probe_frames[-1] if profile.probe_frames else np.zeros((64, 64))
        fingerprint = chebyshev_fingerprint(first_frame)

        # Cross-game recommendations
        recommended = self.cross_ledger.recommend_strategy(profile, fingerprint)
        base_order = dispatch_solvers(profile)
        solver_order = recommended if recommended else base_order

        # LLM leads for keyboard_click games (needs both action types)
        if HAS_LLM:
            gt = profile.game_type
            has_click = 6 in profile.available_actions
            has_keys = any(a in profile.available_actions for a in [1, 2, 3, 4])
            if has_click and has_keys:
                # Hybrid game — LLM is the pro gamer brain
                solver_order = ['llm'] + [s for s in solver_order if s != 'llm']
            elif gt in ('MIXED', 'FIELD', 'AGENT-HYBRID'):
                solver_order = ['llm'] + [s for s in solver_order if s != 'llm']

        if self.verbose:
            print(f"  Mechanisms: {n_mechs} | Barrier: {barrier:.1f} | "
                  f"Budget: {self.budget}")
            src = "transfer" if recommended else "dispatch"
            print(f"  Solver order ({src}): {' > '.join(solver_order)}")

            # Show resumed knowledge
            if self.shared.total_sessions > 0:
                s = self.shared.summary()
                print(f"  Prior knowledge: {s['transitions']} trans, "
                      f"{s['macros']} macros, {s['atoms']} atoms")

        # ─── PHASE 2: CONDUCT (multi-attempt) ───
        best_result = {'levels_solved': 0, 'total_actions': 0,
                       'win_levels': profile.win_levels}

        for attempt in range(self.max_attempts):
            self._attempt_num = attempt

            if self.verbose and self.max_attempts > 1:
                print(f"\n  ── Attempt {attempt + 1}/{self.max_attempts} "
                      f"{'─'*40}")

            result = self._conduct_attempt(
                profile, solver_order, barrier, attempt)

            if result['levels_solved'] > best_result['levels_solved']:
                best_result = result

            if result['levels_solved'] >= profile.win_levels:
                if self.verbose:
                    print(f"  ★ SOLVED in attempt {attempt + 1} ★")
                break

            # Evolve strategy order for next attempt
            solver_order = self._evolve_order(solver_order)
            self.temperature *= 1.3  # Increase exploration diversity

        # ─── PHASE 3: PERSIST ───
        self.shared.total_sessions += 1
        profile_hint = profile.solver_hint() if hasattr(profile, 'solver_hint') else ''
        self.game_ledger.save(
            self.game_id, self.shared, self.solver_results, profile_hint)
        self.cross_ledger.update(
            self.game_id, profile, fingerprint,
            self.solver_results, self.shared)

        elapsed = time.time() - t0

        # ─── PHASE 4: REPORT ───
        if self.verbose:
            print(f"\n{'─'*65}")
            s = self.shared.summary()
            total_acts = sum(
                r.get('total_actions', 0) for r in self.solver_results.values()
            )
            print(f"  Result: {best_result['levels_solved']}/"
                  f"{profile.win_levels} levels | "
                  f"{total_acts} total actions | "
                  f"φ_best={s['best_phi']:.3f} | "
                  f"{elapsed:.1f}s")
            print(f"  Knowledge: {s['transitions']} trans, "
                  f"{s['macros']} macros, {s['atoms']} atoms, "
                  f"{s['states_visited']} states")
            print(f"  Saved to: ledger/{self.game_id}.json")

        return {
            'game_id': self.game_id,
            'levels_solved': best_result['levels_solved'],
            'win_levels': profile.win_levels,
            'total_actions': sum(
                r.get('total_actions', 0)
                for r in self.solver_results.values()
            ),
            'best_solver': best_result.get('solver_name', ''),
            'best_phi': self.shared.best_phi_ever,
            'attempts': self._attempt_num + 1,
            'elapsed': elapsed,
            'shared_state': self.shared.summary(),
            'profile': {
                'game_type': profile.game_type,
                'is_deterministic': profile.is_deterministic,
                'vocab_size': len(profile.nibble_vocab),
                'n_templates': profile.n_unique_templates,
            },
        }

    def _conduct_attempt(self, profile: GameProfile, solver_order: list,
                         barrier: float, attempt_num: int) -> dict:
        """One attempt: Maestro manages the level loop.

        Key insight: each solver solves ONE level at a time. If solver A
        fails a level, solver B tries the SAME level on the SAME env.
        When a level is solved, move to the next level with the best solver.
        """
        arcade = arc_agi.Arcade()
        env = arcade.make(self.game_id)
        obs = env.reset()

        total_levels_solved = 0
        total_actions = 0
        remaining_budget = self.budget
        per_level_budget = max(50, self.budget // profile.win_levels)

        if self.verbose:
            print(f"  Budget: {self.budget} total, "
                  f"~{per_level_budget}/level, "
                  f"{profile.win_levels} levels")

        # Track which solvers solved which levels (for fast-tracking)
        proven_solvers: dict[int, str] = {}  # level_idx → solver_name
        failed_solvers: dict[int, set] = {}  # level_idx → set of failed solvers

        # ─── LEVEL LOOP: Maestro conducts one level at a time ───
        for level_idx in range(profile.win_levels):
            if obs.state == GameState.WIN:
                break
            if remaining_budget <= 0:
                break

            level_solved = False
            level_budget = min(per_level_budget, remaining_budget)
            failed_this_level = failed_solvers.get(level_idx, set())

            # Build solver priority: proven solver first, skip known failures
            if level_idx in proven_solvers:
                # Fast-track: put the proven solver first
                proven = proven_solvers[level_idx]
                level_order = [proven] + [s for s in solver_order
                                          if s != proven and s not in failed_this_level]
            else:
                level_order = [s for s in solver_order if s not in failed_this_level]

            for solver_name in level_order:
                if level_budget <= 0:
                    break

                # If env is dead, create a fresh one
                if obs.state == GameState.GAME_OVER:
                    env = arcade.make(self.game_id)
                    obs = env.reset()
                    if self.verbose:
                        print(f"    (env reset)")

                    # Fast-replay previously solved levels
                    replay_ok = True
                    for prev_lvl in range(level_idx):
                        if prev_lvl in proven_solvers:
                            rr, obs = self._run_one_level(
                                proven_solvers[prev_lvl], profile, env, obs,
                                budget=per_level_budget)
                            acts = rr.get('total_actions', 0)
                            total_actions += acts
                            remaining_budget -= acts
                            level_budget -= acts
                            if not rr.get('level_solved', False):
                                replay_ok = False
                                break
                        else:
                            replay_ok = False
                            break
                    if not replay_ok:
                        break

                result, obs = self._run_one_level(
                    solver_name, profile, env, obs,
                    budget=level_budget)

                acts = result.get('total_actions', 0)
                total_actions += acts
                remaining_budget -= acts
                level_budget -= acts

                if result.get('level_solved', False):
                    total_levels_solved += 1
                    level_solved = True
                    proven_solvers[level_idx] = solver_name
                    if self.verbose:
                        print(f"    → L{level_idx} SOLVED by {solver_name}")
                    break
                else:
                    failed_this_level.add(solver_name)
                    failed_solvers[level_idx] = failed_this_level

            if not level_solved:
                if self.verbose:
                    print(f"    → L{level_idx} FAILED (all solvers)")
                break

        best = {'levels_solved': total_levels_solved,
                'total_actions': total_actions,
                'win_levels': profile.win_levels}

        self.shared.attempts.append({
            'attempt': attempt_num,
            'levels_solved': total_levels_solved,
            'total_actions': total_actions,
            'solvers': list(self.shared.budget_spent.keys()),
            'best_phi': self.shared.best_phi_ever,
            'temperature': round(self.temperature, 2),
        })

        return best

    def _run_one_level(self, solver_name: str, profile: GameProfile,
                       env, obs, budget: int) -> tuple:
        """Run solver for ONE level on the shared env. Returns (result, obs).

        The solver attempts to solve the current level only. If it succeeds,
        obs advances to the next level. If it fails, obs is still valid
        for another solver to try.
        """
        key = f"{solver_name}_a{self._attempt_num}"
        start_levels = obs.levels_completed if hasattr(obs, 'levels_completed') else 0

        if self.verbose:
            print(f"    {solver_name} (L={start_levels}, "
                  f"budget={budget})...", end=' ', flush=True)

        try:
            result, new_obs = _solve_one_level_on_env(
                solver_name, profile, env, obs,
                self.shared, budget=budget)
        except Exception as e:
            if self.verbose:
                print(f"ERROR: {e}")
            return {'total_actions': 0, 'level_solved': False,
                    'error': str(e)}, obs

        result['solver_name'] = solver_name
        self.solver_results[key] = result

        # Update tracking
        phi = result.get('final_phi', 0.0)
        if phi > self.shared.best_phi_ever:
            self.shared.best_phi_ever = phi

        actions = result.get('total_actions', 0)
        self.shared.budget_spent[solver_name] = (
            self.shared.budget_spent.get(solver_name, 0) + actions
        )

        if self.verbose:
            solved = result.get('level_solved', False)
            acts = result.get('total_actions', 0)
            status = "SOLVED" if solved else f"no solve"
            phi_str = f" φ={phi:.3f}" if phi > 0 else ""
            print(f"{status}, {acts} acts{phi_str}")

        return result, new_obs

    # ─── CONDUCTING DECISIONS ─────────────────────────────────────

    def _pick_steepest_phi(self, solver_order: list) -> str:
        """JKO gradient conducting: pick solver with steepest φ descent."""
        best_name = solver_order[0]
        best_grad = -float('inf')

        for name, traj in self.shared.phi_trajectories.items():
            grad = jko_gradient(traj)
            if grad > best_grad:
                best_grad = grad
                best_name = name

        # If no trajectories yet, use dispatch order
        return best_name

    def _best_phi_gradient(self) -> float:
        """Current best φ gradient across all solvers."""
        best = 0.0
        for traj in self.shared.phi_trajectories.values():
            grad = jko_gradient(traj)
            if grad > best:
                best = grad
        return best

    def _should_kill(self, solver_name: str) -> tuple:
        """Kill switch check. Returns (should_kill, reason)."""
        # 1. Fantasia saturation
        sat = self.shared.detector.barrier_progress()
        if sat > 0.95:
            return True, "fantasia_saturated"

        # 2. φ stall
        traj = self.shared.phi_trajectories.get(solver_name, [])
        if len(traj) >= 5:
            recent = traj[-5:]
            if max(recent) - min(recent) < 0.01:
                return True, "phi_stalled"

        # 3. Holonomy novelty (only if we have paths)
        paths = self.shared.holonomy_paths.get(solver_name, [])
        if len(paths) > 5:
            try:
                O_path = [p[0] for p in paths]
                R_path = [p[1] for p in paths]
                a_path = [p[2] for p in paths]
                novelty = holonomy_deficit(O_path, R_path, a_path)
                if novelty < 0.01:
                    return True, "redundant_exploration"
            except (IndexError, ValueError):
                pass

        return False, ""

    def _evolve_order(self, current_order: list) -> list:
        """Replicator dynamics on solver fitness across attempts."""
        fitness = {}
        for key, result in self.solver_results.items():
            solver_name = key.split('_a')[0]
            solved = 1.0 if result.get('level_solved', False) else 0.0
            phi = result.get('final_phi', 0.0)
            acts = max(1, result.get('total_actions', 1))
            # Reward: SOLVING is king (1000×), φ secondary, budget waste minor
            score = solved * 1000.0 + phi * 10.0 - acts * 0.01
            if solver_name not in fitness:
                fitness[solver_name] = []
            fitness[solver_name].append(score)

        # Average fitness per solver
        avg_fitness = {
            s: sum(scores) / len(scores)
            for s, scores in fitness.items()
        }

        # Sort by fitness, keep all solvers (unlisted ones at end)
        all_solvers = list(dict.fromkeys(current_order))
        for s in avg_fitness:
            if s not in all_solvers:
                all_solvers.append(s)

        evolved = sorted(all_solvers,
                         key=lambda s: avg_fitness.get(s, 0.0),
                         reverse=True)

        if self.verbose and evolved != current_order:
            print(f"  Evolved order: {' > '.join(evolved)}")

        return evolved


# ═══════════════════════════════════════════════════════════════════
#  CLI
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(
        description='ARC-AGI-3 Maestro — The Conductor')
    parser.add_argument('game_id', nargs='?', help='Game ID (e.g., cd82-xxx)')
    parser.add_argument('--all', action='store_true', help='Run all games')
    parser.add_argument('-v', '--verbose', action='store_true', default=True)
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('--compete', action='store_true',
                        help='Competition mode: one solver per game')
    parser.add_argument('--attempts', type=int, default=3,
                        help='Max attempts per game (default: 3)')
    parser.add_argument('--budget', type=int, default=500,
                        help='Action budget per attempt (default: 500)')
    parser.add_argument('--resume', action='store_true', default=True,
                        help='Resume from ledger (default: True)')
    parser.add_argument('--fresh', action='store_true',
                        help='Ignore ledger, start fresh')
    parser.add_argument('--save', type=str, help='Save results JSON')
    args = parser.parse_args()

    if args.quiet:
        args.verbose = False

    resume = not args.fresh

    # Resolve game list
    if args.all or args.game_id is None:
        arcade = arc_agi.Arcade()
        game_ids = [e.game_id for e in arcade.get_environments()]
    else:
        game_ids = [args.game_id]

    # Run
    all_results = []
    total_solved = 0
    total_levels = 0
    t_start = time.time()

    for i, gid in enumerate(game_ids):
        if args.verbose:
            print(f"\n{'▓'*65}")
            print(f"  Game {i+1}/{len(game_ids)}: {gid}")
            print(f"{'▓'*65}")

        maestro = Maestro(
            game_id=gid,
            budget=args.budget,
            max_attempts=args.attempts,
            resume=resume,
            verbose=args.verbose,
            compete=args.compete,
        )
        result = maestro.conduct()
        all_results.append(result)
        total_solved += result['levels_solved']
        total_levels += result['win_levels']

    # Summary
    elapsed = time.time() - t_start
    n_games = len(game_ids)
    games_with_progress = sum(1 for r in all_results if r['levels_solved'] > 0)

    print(f"\n{'═'*65}")
    print(f"  MAESTRO SUMMARY")
    print(f"{'═'*65}")
    print(f"  Games: {n_games} | Levels: {total_solved}/{total_levels} | "
          f"Time: {elapsed:.1f}s")
    print(f"  Games with progress: {games_with_progress}/{n_games}")

    # Per-game results
    if args.verbose or total_solved > 0:
        print(f"\n  {'Game':<20} {'Solved':>8} {'φ_best':>8} "
              f"{'Actions':>8} {'Solver':<15}")
        print(f"  {'─'*60}")
        for r in sorted(all_results,
                         key=lambda x: x['levels_solved'], reverse=True):
            gid = r['game_id'].split('-')[0]
            print(f"  {gid:<20} {r['levels_solved']:>3}/"
                  f"{r['win_levels']:<4} "
                  f"{r.get('best_phi', 0):.3f}    "
                  f"{r['total_actions']:>6}   "
                  f"{r.get('best_solver', ''):<15}")

    # Save
    if args.save:
        with open(args.save, 'w') as f:
            json.dump(all_results, f, indent=2, default=str)
        print(f"\n  Saved to: {args.save}")

    print()


if __name__ == '__main__':
    main()
