#!/usr/bin/env python3
"""ARC-AGI-3 Ensemble Solver — dispatches best solver per game from probe diagnostics.

Three solvers crack three different games:
  packet_solver     → tn36-L0  (ClickScan on CLICK-ONLY)
  recursive_solver  → lp85-L0  (GF(2) grammar on LOCKED)
  instanton_planner → r11l-L0  (macro replay on CLICK-ONLY)

Ensemble probes once, dispatches all viable solvers, takes best result.

Usage:
  python3 ensemble_solver.py --all              # Eval mode: all solvers per game
  python3 ensemble_solver.py --all --compete    # Competition: best-guess solver per game
  python3 ensemble_solver.py cd82-xxx           # Single game
  python3 ensemble_solver.py --all --save r.json # Save results
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

import arc_agi
from packet_probe import probe_game, GameProfile
import packet_solver
import recursive_solver
import instanton_planner
import spectral_engine
import aaa_solver
import eckert_simulator
from eckert_win_detector import EckertWinDetector


# ═══════════════════════════════════════════════════════════════════
#  DISPATCH TABLE — profile-based solver selection
# ═══════════════════════════════════════════════════════════════════

def dispatch_solvers(profile: GameProfile) -> list[str]:
    """Return solver priority list based on probe diagnostics.

    First solver in the list is the best guess for competition mode.
    Eval mode runs all of them.
    """
    gt = profile.game_type
    det = profile.is_deterministic
    vocab_size = len(profile.nibble_vocab)
    n_templates = profile.n_unique_templates
    has_click = 6 in profile.available_actions
    has_move = any(a in profile.available_actions for a in [1, 2, 3, 4])

    if gt == 'CLICK-ONLY':
        if det and n_templates > 8:
            return ['instanton', 'eckert', 'aaa', 'packet', 'recursive']
        elif profile.clickable_colors:
            return ['packet', 'eckert', 'instanton', 'aaa', 'recursive']
        else:
            return ['instanton', 'eckert', 'aaa', 'packet', 'recursive']

    elif gt == 'LOCKED':
        return ['recursive', 'eckert', 'aaa', 'instanton', 'packet']

    elif gt == 'AGENT-KB':
        # Eckert shines on deterministic agent games — manifold coords
        # locate the agent and plan geodesic paths
        if det:
            return ['eckert', 'aaa', 'instanton', 'recursive', 'packet']
        else:
            return ['aaa', 'eckert', 'recursive', 'instanton', 'packet']

    elif gt == 'FIELD':
        return ['eckert', 'aaa', 'packet', 'recursive', 'instanton']

    elif gt == 'MIXED':
        return ['eckert', 'aaa', 'instanton', 'recursive', 'packet']

    # Unknown type — eckert is the most general
    return ['eckert', 'aaa', 'recursive', 'instanton', 'packet']


# ═══════════════════════════════════════════════════════════════════
#  SOLVER RUNNERS — unified interface over different APIs
# ═══════════════════════════════════════════════════════════════════

@dataclass
class SolverResult:
    solver_name: str
    game_id: str
    levels_solved: int = 0
    win_levels: int = 0
    total_actions: int = 0
    error: Optional[str] = None
    raw: dict = field(default_factory=dict)


def _run_one(solver_name: str, game_id: str, probe_budget: int,
             verbose: bool) -> SolverResult:
    """Run a single solver on a fresh game instance, catching all errors."""
    try:
        if solver_name == 'packet':
            result = packet_solver.solve_game(
                game_id, probe_budget=probe_budget, verbose=verbose)
        elif solver_name == 'recursive':
            result = recursive_solver.solve(
                game_id, probe_budget=probe_budget, verbose=verbose)
        elif solver_name == 'instanton':
            result = instanton_planner.solve(
                game_id, probe_budget=probe_budget, verbose=verbose)
        elif solver_name == 'spectral':
            result = spectral_engine.solve(
                game_id, probe_budget=probe_budget, verbose=verbose)
        elif solver_name == 'aaa':
            result = aaa_solver.solve(
                game_id, probe_budget=probe_budget, verbose=verbose)
        elif solver_name == 'eckert':
            result = eckert_simulator.solve(
                game_id, probe_budget=probe_budget, verbose=verbose)
        else:
            return SolverResult(solver_name, game_id,
                                error=f"Unknown solver: {solver_name}")

        return SolverResult(
            solver_name=solver_name,
            game_id=game_id,
            levels_solved=result.get('levels_solved', 0),
            win_levels=result.get('win_levels', 0),
            total_actions=result.get('total_actions', 0),
            raw=result,
        )
    except Exception as e:
        if verbose:
            traceback.print_exc()
        return SolverResult(
            solver_name=solver_name,
            game_id=game_id,
            error=f"{type(e).__name__}: {e}",
        )


# ═══════════════════════════════════════════════════════════════════
#  ENSEMBLE CORE
# ═══════════════════════════════════════════════════════════════════

def solve_ensemble(game_id: str, probe_budget: int = 30, verbose: bool = True,
                   compete: bool = False, max_solvers: int = 3) -> dict:
    """Run ensemble on a single game.

    compete=True  → run only the top-dispatched solver (fast, one scorecard)
    compete=False → run up to max_solvers, compare results (eval mode)
    """
    short_id = game_id.split('-')[0]

    if verbose:
        print(f"\n{'='*60}")
        print(f"  ENSEMBLE: {game_id}")
        print(f"{'='*60}")

    # Phase 1: Probe (free — separate arcade instance)
    profile = probe_game(game_id, budget=probe_budget, verbose=False)

    if verbose:
        print(f"  Type: {profile.game_type} | Det: {profile.is_deterministic} | "
              f"Vocab: {len(profile.nibble_vocab)} | "
              f"Tmpl: {profile.n_unique_templates} | "
              f"Actions: {profile.available_actions}")

    # Phase 2: Dispatch
    solver_order = dispatch_solvers(profile)
    run_list = solver_order[:1] if compete else solver_order[:max_solvers]

    if verbose:
        mode = "COMPETE" if compete else "EVAL"
        print(f"  [{mode}] dispatch: {' > '.join(run_list)}")

    # Phase 3: Run with φ-based progress tracking
    results = []
    best_phi = 0.0

    for name in run_list:
        if verbose:
            print(f"\n  ── {name} {'─'*(45-len(name))}")

        r = _run_one(name, game_id, probe_budget=probe_budget, verbose=verbose)
        results.append(r)

        # Track φ from solver if available
        solver_phi = r.raw.get('final_phi', 0.0)
        if solver_phi > best_phi:
            best_phi = solver_phi

        if verbose:
            if r.error:
                print(f"  {name}: ERROR {r.error[:70]}")
            else:
                phi_str = f" φ={solver_phi:.3f}" if solver_phi > 0 else ""
                print(f"  {name}: {r.levels_solved}/{r.win_levels} levels "
                      f"({r.total_actions} actions){phi_str}")

        # Early exit if all levels solved
        if r.levels_solved > 0 and r.levels_solved >= r.win_levels:
            if verbose:
                print(f"  * ALL LEVELS SOLVED by {name} *")
            break

    # Phase 4: Pick best (most levels solved, then fewest actions)
    best = max(results, key=lambda r: (r.levels_solved, -r.total_actions))

    return {
        'game_id': game_id,
        'profile': {
            'game_type': profile.game_type,
            'is_deterministic': profile.is_deterministic,
            'vocab_size': len(profile.nibble_vocab),
            'n_templates': profile.n_unique_templates,
            'available_actions': profile.available_actions,
        },
        'best_solver': best.solver_name,
        'levels_solved': best.levels_solved,
        'win_levels': best.win_levels,
        'total_actions': best.total_actions,
        'all_results': [
            {
                'solver': r.solver_name,
                'levels_solved': r.levels_solved,
                'win_levels': r.win_levels,
                'actions': r.total_actions,
                'error': r.error,
            }
            for r in results
        ],
    }


# ═══════════════════════════════════════════════════════════════════
#  MAIN
# ═══════════════════════════════════════════════════════════════════

def main():
    parser = argparse.ArgumentParser(description='ARC-AGI-3 Ensemble Solver')
    parser.add_argument('game_id', nargs='?', help='Game ID (e.g., cd82-xxx)')
    parser.add_argument('--all', action='store_true', help='Run on all games')
    parser.add_argument('-b', '--probe-budget', type=int, default=30)
    parser.add_argument('-v', '--verbose', action='store_true', default=True)
    parser.add_argument('-q', '--quiet', action='store_true')
    parser.add_argument('--compete', action='store_true',
                        help='Competition mode: one solver per game')
    parser.add_argument('--max-solvers', type=int, default=3,
                        help='Max solvers per game in eval mode (default: 3)')
    parser.add_argument('--save', type=str, help='Save results JSON')
    args = parser.parse_args()

    if args.quiet:
        args.verbose = False

    # Resolve game list
    if args.all or args.game_id is None:
        arcade = arc_agi.Arcade()
        envs = arcade.get_environments()
        game_ids = [e.game_id for e in envs]
    else:
        game_ids = [args.game_id]

    all_results = []
    total_solved = 0
    total_possible = 0
    solver_wins = {}   # solver -> [game_ids]
    solver_errors = {} # solver -> [(game_id, error)]

    t0 = time.time()

    for gid in game_ids:
        result = solve_ensemble(
            gid,
            probe_budget=args.probe_budget,
            verbose=args.verbose,
            compete=args.compete,
            max_solvers=args.max_solvers,
        )
        all_results.append(result)
        total_solved += result['levels_solved']
        total_possible += result['win_levels']

        if result['levels_solved'] > 0:
            solver_wins.setdefault(result['best_solver'], []).append(
                result['game_id'])

        for r in result['all_results']:
            if r['error']:
                solver_errors.setdefault(r['solver'], []).append(
                    (result['game_id'], r['error']))

    elapsed = time.time() - t0

    # ── Summary ──────────────────────────────────────────────────
    print(f"\n{'='*60}")
    print(f"  ENSEMBLE RESULTS")
    print(f"{'='*60}")
    mode = 'Competition (1 solver/game)' if args.compete else \
           f'Evaluation (up to {args.max_solvers} solvers/game)'
    print(f"  Games: {len(game_ids)} | Solved: {total_solved}/{total_possible} | "
          f"Time: {elapsed:.1f}s")
    print(f"  Mode: {mode}")

    # Solver wins
    if solver_wins:
        print(f"\n  Solver wins:")
        for solver, games in sorted(solver_wins.items()):
            short = [g.split('-')[0] for g in games]
            print(f"    {solver}: {len(games)} — {', '.join(short)}")

    # Solved games detail
    solved = [r for r in all_results if r['levels_solved'] > 0]
    if solved:
        print(f"\n  Solved games:")
        for r in solved:
            short = r['game_id'].split('-')[0]
            print(f"    {short}: {r['levels_solved']}/{r['win_levels']} "
                  f"by {r['best_solver']} ({r['total_actions']} actions)")

    # Errors summary
    if solver_errors:
        print(f"\n  Errors:")
        for solver, errs in sorted(solver_errors.items()):
            print(f"    {solver}: {len(errs)} errors")
            for gid, err in errs[:3]:
                print(f"      {gid.split('-')[0]}: {err[:70]}")
            if len(errs) > 3:
                print(f"      ... and {len(errs) - 3} more")

    # Dispatch table (eval mode, multi-game)
    if not args.compete and len(game_ids) > 1:
        print(f"\n  Dispatch table (profile → best solver):")
        for r in all_results:
            # Find which solver(s) actually solved levels
            winners = [sr for sr in r['all_results'] if sr['levels_solved'] > 0]
            if winners:
                best = max(winners, key=lambda s: s['levels_solved'])
                p = r['profile']
                print(f"    {r['game_id'].split('-')[0]}: {best['solver']} "
                      f"[{p['game_type']}, det={p['is_deterministic']}, "
                      f"v={p['vocab_size']}, t={p['n_templates']}]")

    # Save
    if args.save:
        with open(args.save, 'w') as f:
            json.dump({
                'timestamp': time.strftime('%Y-%m-%d %H:%M:%S'),
                'mode': 'compete' if args.compete else 'eval',
                'total_solved': total_solved,
                'total_possible': total_possible,
                'elapsed_seconds': round(elapsed, 1),
                'results': all_results,
            }, f, indent=2)
        print(f"\n  Results saved to {args.save}")


if __name__ == '__main__':
    main()
