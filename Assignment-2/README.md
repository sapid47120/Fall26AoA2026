# Empirical Analysis of Sorting Algorithms

**Student Name:** Arslan Tahir  
**SAP ID:** 47120  
**Subject:** Analysis of Algorithms  
**Project:** Sorting_Algorithm_Analysis (Assignment 2)  
**GitHub Repository:** [https://github.com/sapid47120/Fall26AoA2026](https://github.com/sapid47120/Fall26AoA2026) (under `Assignment-2/`)  

---

## 1. Project Description
This project analyzes the practical execution times of four standard sorting algorithms implemented from scratch in Python:
- **Bubble Sort** (with an early-exit optimization for sorted data)
- **Selection Sort**
- **Insertion Sort**
- **Merge Sort** (divide-and-conquer)

We compare their theoretical time complexities ($O(N)$, $O(N^2)$, and $O(N \log N)$) with actual execution times on different input sizes:
- **Ascending inputs:** The exact arrays from the assignment ($N = 5, 10, 50, 100$).
- **Descending inputs:** Reverse-ordered arrays ($N = 5, 10, 50, 100$) to test worst-case behavior.

---

## 2. Project Layout

```text
Sorting_Algorithm_Analysis/
├── requirements.txt            # Python dependencies (matplotlib, pandas)
├── README.md                   # Project overview and run instructions
├── src/
│   ├── sorting_algorithms.py   # Pure Python sorting implementations
│   ├── data_generator.py       # Assignment arrays (Arr1 to Arr4) and reverse inputs
│   ├── benchmark.py            # High-precision timer and multi-run benchmark logic
│   ├── plotter.py              # Matplotlib code for execution-time graphs
│   └── main.py                 # Main runner script
├── tests/
│   └── test_sorting.py         # Unit tests checking correctness and array immutability
├── results/
│   ├── ascending_benchmark_results.csv   # Measured averages for ascending inputs
│   └── descending_benchmark_results.csv  # Measured averages for descending inputs
└── plots/
    ├── execution_time_ascending.png      # Graph for ascending inputs
    └── execution_time_descending.png     # Graph for descending inputs
```

---

## 3. How Timing is Measured
Because array sizes are relatively small ($N \le 100$), a single sort takes only a few microseconds. To get accurate, repeatable numbers:
1. We use Python's high-precision `time.perf_counter_ns()`.
2. Each benchmark run repeats the sort 500 times on pre-copied inputs (so array creation is not included in the measured time).
3. We perform 5 independent benchmark runs for every algorithm and input size, then calculate the average execution time in microseconds ($\mu s$).
4. We pause Python's garbage collection during the inner loop to prevent random background cleanups from affecting the readings.

---

## 4. Setup and How to Run

### Requirements
- Python 3.8 or newer (tested on Python 3.11)
- Libraries: `matplotlib`, `pandas`

### Install Dependencies
```bash
pip install -r requirements.txt
```

### Run Unit Tests
To verify that all four algorithms sort correctly and leave original inputs untouched:
```bash
python -m unittest discover -s tests -v
```

### Run the Complete Benchmark
To run the benchmarks, update the CSV files, and generate the graphs:
```bash
python src/main.py
```

---

## 5. Theoretical Complexity Comparison

| Algorithm | Best-Case Time | Average-Case Time | Worst-Case Time | Auxiliary Space | Stable? |
| :--- | :---: | :---: | :---: | :---: | :---: |
| **Bubble Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes |
| **Selection Sort** | $O(N^2)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | No |
| **Insertion Sort** | $O(N)$ | $O(N^2)$ | $O(N^2)$ | $O(1)$ | Yes |
| **Merge Sort** | $O(N \log N)$ | $O(N \log N)$ | $O(N \log N)$ | $O(N)$ | Yes |

---

## 6. Key Takeaways from Measured Results
1. **Ascending Inputs (Best Case):**
   - Bubble Sort and Insertion Sort are very fast because they recognize the array is already sorted in $O(N)$ steps.
   - Selection Sort still takes $O(N^2)$ comparisons because it always scans the rest of the array.
2. **Descending Inputs (Worst Case):**
   - Bubble Sort and Insertion Sort slow down significantly due to the maximum number of inversions.
   - For $N=50$ and $N=100$, Merge Sort clearly outperforms all quadratic algorithms, consistent with its $O(N \log N)$ complexity.
3. **Small Array Behavior ($N=5, 10$):**
   - At very small sizes, Merge Sort is slightly slower than simple loops due to recursion and sub-list creation overhead. As $N$ reaches $50$ and $100$, its asymptotic advantage becomes dominant.
