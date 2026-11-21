"""
Plotting module using Matplotlib.

Generates execution-time line graphs showing Average Time (us) vs Input Size (N).
"""

from typing import Dict, List
import matplotlib.pyplot as plt


def plot_benchmark_results(
    summary_rows: List[Dict[str, float]],
    title: str,
    output_filepath: str,
    algorithms: List[str] = None,
):
    """Generates and saves a clean line graph of sorting execution times."""
    if algorithms is None:
        algorithms = ["Bubble Sort", "Selection Sort", "Insertion Sort", "Merge Sort"]

    sizes = [row["Input Size (N)"] for row in summary_rows]

    plt.figure(figsize=(9, 5.5), dpi=300)
    plt.style.use("seaborn-v0_8-whitegrid" if "seaborn-v0_8-whitegrid" in plt.style.available else "default")

    markers = ["o", "s", "^", "D"]
    colors = ["#e74c3c", "#3498db", "#2ecc71", "#9b59b6"]

    for idx, algo in enumerate(algorithms):
        times = [row[algo] for row in summary_rows]
        plt.plot(
            sizes,
            times,
            marker=markers[idx % len(markers)],
            color=colors[idx % len(colors)],
            linewidth=2,
            markersize=6,
            label=algo,
        )

    plt.title(title, fontsize=13, fontweight="bold", pad=12)
    plt.xlabel("Input Size (N)", fontsize=11, labelpad=8)
    plt.ylabel("Average Execution Time (μs)", fontsize=11, labelpad=8)
    plt.xticks(sizes, [str(s) for s in sizes], fontsize=10)
    plt.yticks(fontsize=10)
    plt.grid(True, linestyle="--", alpha=0.6)
    plt.legend(loc="upper left", fontsize=10, frameon=True)
    plt.tight_layout()

    plt.savefig(output_filepath)
    plt.close()
    print(f"Saved plot: {output_filepath}")
