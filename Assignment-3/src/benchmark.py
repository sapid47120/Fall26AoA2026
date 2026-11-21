"""
Timing and Benchmarking Module.

Measures the execution time of each sorting algorithm using time.perf_counter_ns().
Runs 5 independent runs per size, with 500 repetitions per run to ensure reliable,
consistent timing for small arrays.
"""

import time
import gc
import csv
from typing import Callable, Dict, List, Tuple
from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort
from data_generator import ASCENDING_ARRAYS, get_descending_input

ALGORITHMS: Dict[str, Callable[[List[int]], List[int]]] = {
    "Bubble Sort": bubble_sort,
    "Selection Sort": selection_sort,
    "Insertion Sort": insertion_sort,
    "Merge Sort": merge_sort,
}

SIZES = [5, 10, 50, 100]
RUNS = 5
REPETITIONS = 500


def benchmark_single(
    sort_fn: Callable[[List[int]], List[int]],
    input_data: List[int],
    repetitions: int = REPETITIONS,
) -> float:
    """Measures the average execution time of a sorting function in microseconds (us).

    Methodology:
    1. Pre-copies the input arrays before timing starts so that array creation
       time is not included in the measurement.
    2. Runs one warm-up sort to initialize Python bytecode and CPU cache.
    3. Pauses Python garbage collection during the timed loop so background
       memory cleanups do not distort the measured sort time.
    4. Divides total elapsed time by the number of repetitions and converts to us.
    """
    # Pre-allocate inputs outside the timed block
    test_copies = [list(input_data) for _ in range(repetitions)]

    # Warm-up run
    _ = sort_fn(list(input_data))

    gc.collect()
    gc.disable()
    try:
        start_ns = time.perf_counter_ns()
        for i in range(repetitions):
            _ = sort_fn(test_copies[i])
        end_ns = time.perf_counter_ns()
    finally:
        gc.enable()

    del test_copies

    total_ns = end_ns - start_ns
    avg_ns_per_op = total_ns / repetitions
    avg_us_per_op = avg_ns_per_op / 1000.0  # Convert nanoseconds to microseconds
    return avg_us_per_op


def run_benchmark_suite(
    input_type: str,
) -> Tuple[List[Dict[str, float]], Dict[str, Dict[int, List[float]]]]:
    """Runs the benchmark across all algorithms and input sizes for one input type.

    Args:
        input_type: 'ascending' or 'descending'

    Returns:
        summary_rows: Average times formatted for CSV and table display.
        raw_runs: Individual run timings for each algorithm and size.
    """
    print(f"\n==========================================")
    print(f"Running Benchmarks for: {input_type.upper()} inputs")
    print(f"Settings: {RUNS} runs per size, {REPETITIONS} repetitions per run")
    print(f"==========================================")

    raw_runs: Dict[str, Dict[int, List[float]]] = {
        name: {size: [] for size in SIZES} for name in ALGORITHMS
    }
    summary_rows: List[Dict[str, float]] = []

    for size in SIZES:
        if input_type == "ascending":
            base_array = list(ASCENDING_ARRAYS[size])
        else:
            base_array = get_descending_input(size)

        row: Dict[str, float] = {"Input Size (N)": size}

        for name, sort_fn in ALGORITHMS.items():
            run_times = []
            for _ in range(RUNS):
                t_us = benchmark_single(sort_fn, base_array, REPETITIONS)
                run_times.append(t_us)

            raw_runs[name][size] = run_times
            avg_time_us = sum(run_times) / len(run_times)
            row[name] = round(avg_time_us, 4)

        summary_rows.append(row)

    return summary_rows, raw_runs


def save_results_to_csv(filepath: str, rows: List[Dict[str, float]]):
    """Saves benchmark results to a CSV file."""
    if not rows:
        return
    headers = list(rows[0].keys())
    with open(filepath, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=headers)
        writer.writeheader()
        writer.writerows(rows)
    print(f"Saved results to: {filepath}")
