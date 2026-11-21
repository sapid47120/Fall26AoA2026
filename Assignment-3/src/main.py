"""
Master Script to Run the Complete Assignment Workflow.

Steps:
1. Runs correctness checks to verify all algorithms sort properly.
2. Benchmarks all algorithms on ascending inputs (Arr1 to Arr4).
3. Benchmarks all algorithms on descending inputs (worst-case).
4. Saves results to CSV files and prints markdown summary tables.
5. Generates execution-time graphs using Matplotlib.
"""

import os
import sys

# Ensure src directory is accessible
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
if CURRENT_DIR not in sys.path:
    sys.path.insert(0, CURRENT_DIR)

from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort
from data_generator import ASCENDING_ARRAYS, get_descending_input
from benchmark import run_benchmark_suite, save_results_to_csv, ALGORITHMS, SIZES
from plotter import plot_benchmark_results


def validate_correctness():
    """Verifies that all sorting algorithms sort correctly and leave original inputs unchanged."""
    print("Step 1: Checking algorithm correctness and input immutability...")
    for name, sort_fn in ALGORITHMS.items():
        # Check ascending inputs
        for n, original in ASCENDING_ARRAYS.items():
            arr_copy = list(original)
            res = sort_fn(arr_copy)
            if res != sorted(original) or arr_copy != original:
                raise RuntimeError(f"Validation failed for {name} on ascending input N={n}")

        # Check descending inputs
        for n in SIZES:
            desc = get_descending_input(n)
            desc_copy = list(desc)
            res = sort_fn(desc_copy)
            if res != sorted(desc) or desc_copy != desc:
                raise RuntimeError(f"Validation failed for {name} on descending input N={n}")

    print("Result: All algorithms passed correctness tests.\n")


def print_table(title: str, rows: list):
    """Prints a clean markdown table in the terminal."""
    print(f"\n### {title}")
    headers = list(rows[0].keys())
    header_line = "| " + " | ".join(headers) + " |"
    separator = "| " + " | ".join(["---"] * len(headers)) + " |"
    print(header_line)
    print(separator)
    for r in rows:
        row_str = "| " + " | ".join(f"{r[h]}" for h in headers) + " |"
        print(row_str)
    print()


def main():
    validate_correctness()

    project_root = os.path.dirname(CURRENT_DIR)
    results_dir = os.path.join(project_root, "results")
    plots_dir = os.path.join(project_root, "plots")
    os.makedirs(results_dir, exist_ok=True)
    os.makedirs(plots_dir, exist_ok=True)

    # 1. Benchmark on Ascending Arrays (Assignment inputs Arr1 to Arr4)
    asc_summary, _ = run_benchmark_suite("ascending")
    asc_csv = os.path.join(results_dir, "ascending_benchmark_results.csv")
    save_results_to_csv(asc_csv, asc_summary)
    print_table("Ascending Order Execution Times (μs) - Best / Typical Case", asc_summary)

    asc_plot = os.path.join(plots_dir, "execution_time_ascending.png")
    plot_benchmark_results(
        asc_summary,
        title="Execution Time vs Input Size (Ascending Inputs)",
        output_filepath=asc_plot,
    )

    # 2. Benchmark on Descending Arrays (Worst-case inputs)
    desc_summary, _ = run_benchmark_suite("descending")
    desc_csv = os.path.join(results_dir, "descending_benchmark_results.csv")
    save_results_to_csv(desc_csv, desc_summary)
    print_table("Descending Order Execution Times (μs) - Worst Case", desc_summary)

    desc_plot = os.path.join(plots_dir, "execution_time_descending.png")
    plot_benchmark_results(
        desc_summary,
        title="Execution Time vs Input Size (Descending Inputs - Worst Case)",
        output_filepath=desc_plot,
    )

    print("==========================================")
    print("All benchmarks finished successfully!")
    print("CSVs saved in: results/")
    print("Plots saved in: plots/")
    print("==========================================")


if __name__ == "__main__":
    main()
