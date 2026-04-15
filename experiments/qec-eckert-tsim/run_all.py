#!/usr/bin/env python3
"""
Run all QEC Eckert manifold tests.

Usage:
    python run_all.py          # run all tests
    python run_all.py 1        # run test 1 only
    python run_all.py 1 3      # run tests 1 and 3
"""

import sys
import importlib


def main():
    tests = {
        "1": ("test1_structure_theorem", "Structure Theorem (convexity)"),
        "2": ("test2_fisher_metric", "Fisher Metric vs Eckert Manifold"),
        "3": ("test3_three_point_geometry", "Three-Point Geometry"),
    }

    # Which tests to run
    if len(sys.argv) > 1:
        selected = sys.argv[1:]
    else:
        selected = list(tests.keys())

    print("QEC Eckert Manifold Test Suite")
    print("Using QuEra Tsim (CPU mode)")
    print("=" * 70)

    for test_id in selected:
        if test_id not in tests:
            print(f"Unknown test: {test_id}. Available: {list(tests.keys())}")
            continue

        module_name, description = tests[test_id]
        print(f"\n{'#' * 70}")
        print(f"# TEST {test_id}: {description}")
        print(f"{'#' * 70}\n")

        try:
            module = importlib.import_module(module_name)
            if test_id == "1":
                module.run_structure_theorem_test()
            elif test_id == "2":
                module.run_fisher_metric_test()
            elif test_id == "3":
                module.run_three_point_test()
        except Exception as e:
            print(f"TEST {test_id} FAILED: {e}")
            import traceback
            traceback.print_exc()

    print("\n" + "=" * 70)
    print("All selected tests complete. Results in results_*.json files.")


if __name__ == "__main__":
    main()
