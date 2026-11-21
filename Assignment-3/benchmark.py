"""
Benchmark execution script for Assignment 3.
Runs all 4 algorithms on all 4 input cases (16 cases total).
Performs 3 timing runs per case, averages them, and tracks auxiliary space & operation counts.
"""

import time
import gc
from typing import Dict, List, Tuple
from sorting_algorithms import selection_sort, bubble_sort, quick_sort, merge_sort
from data_generator import get_test_cases

ALGORITHMS = [
    ("Selection Sort", selection_sort, "O(1)", "In-place"),
    ("Bubble Sort", bubble_sort, "O(1)", "In-place"),
    ("Quick Sort", quick_sort, "O(log N) avg / O(N) worst", "In-place partitioning"),
    ("Merge Sort", merge_sort, "O(N)", "Needs extra arrays"),
]

RUNS = 3
# Internal repetitions per run to ensure precise microsecond measurement
REPETITIONS = 500


def measure_case(sort_fn, input_data: List[int]) -> Tuple[List[float], float, int, int]:
    """Measures 3 runs of execution time in microseconds, taking the average."""
    run_times_us = []
    
    # Warm-up run
    _ = sort_fn(list(input_data))

    comp_count = 0
    swap_count = 0

    for r in range(RUNS):
        copies = [list(input_data) for _ in range(REPETITIONS)]
        gc.collect()
        gc.disable()
        t0 = time.perf_counter_ns()
        for i in range(REPETITIONS):
            res, comp_count, swap_count = sort_fn(copies[i])
        t1 = time.perf_counter_ns()
        gc.enable()
        del copies

        total_ns = t1 - t0
        avg_ns = total_ns / REPETITIONS
        avg_us = avg_ns / 1000.0
        run_times_us.append(round(avg_us, 4))

    mean_us = round(sum(run_times_us) / len(run_times_us), 4)
    return run_times_us, mean_us, comp_count, swap_count


def execute_all_benchmarks():
    """Executes all 16 test cases and organizes results into 4 tables."""
    test_cases = get_test_cases()
    # 4 Tables (one per algorithm)
    tables_by_algo = {}

    for name, fn, aux_space, place_type in ALGORITHMS:
        rows = []
        for case_id, size, order, data in test_cases:
            runs_us, avg_us, comps, swaps = measure_case(fn, data)
            rows.append({
                "Case": f"Size {size} - {order}",
                "Size": size,
                "Order": order,
                "Run 1 (μs)": runs_us[0],
                "Run 2 (μs)": runs_us[1],
                "Run 3 (μs)": runs_us[2],
                "Average (μs)": avg_us,
                "Aux Space": aux_space,
                "In-Place?": place_type,
                "Comparisons": comps,
                "Swaps/Moves": swaps,
            })
        tables_by_algo[name] = rows

    return tables_by_algo
