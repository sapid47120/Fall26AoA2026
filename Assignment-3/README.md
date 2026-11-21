# Assignment 3: Empirical Analysis of Sorting Algorithms

**Student Name:** Arslan Tahir  
**SAP ID:** 47120  
**Course:** Analysis of Algorithms  
**Repository:** [https://github.com/sapid47120/Fall26AoA2026](https://github.com/sapid47120/Fall26AoA2026) (under `Assignment-3/`)

---

## 1. Overview
This project evaluates the execution time and auxiliary space complexity of four fundamental sorting algorithms implemented from scratch in Python:
1. **Selection Sort** ($O(1)$ auxiliary space, in-place)
2. **Bubble Sort** ($O(1)$ auxiliary space, in-place with early-exit flag)
3. **Quick Sort** (Lomuto partition scheme, in-place partitioning, recursive stack space)
4. **Merge Sort** (divide-and-conquer, requires $O(N)$ extra array allocations)

---

## 2. Test Cases (16 Total)
Each algorithm is evaluated across four distinct input configurations:
- **Size 5 — Sorted:** `[1, 2, 3, 4, 5]`
- **Size 5 — Reverse Sorted:** `[5, 4, 3, 2, 1]`
- **Size 100 — Sorted:** `[1, 2, ..., 100]`
- **Size 100 — Reverse Sorted:** `[100, 99, ..., 1]`

Total runs = $4 \text{ algorithms} \times 4 \text{ cases} = 16 \text{ test cases}$.  
Each test case is executed across 3 independent runs and averaged in microseconds ($\mu s$).

---

## 3. Project Files
```text
Assignment-3/
├── sorting_algorithms.py               # Pure Python implementations from scratch
├── data_generator.py                   # Test input generation (N=5, 100 sorted & reverse)
├── benchmark.py                        # Benchmark suite (3 timing runs per case & operation tracking)
├── test_sorting.py                     # Unit tests for correctness & immutability
├── generate_assignment3_pdf.py         # Script generating the finalized Word & PDF reports
├── 47120_ArslanTahir_Assignment3.docx  # Final Word report
├── 47120_ArslanTahir_Assignment3.pdf   # Final submission PDF report
├── README.md                           # Documentation
└── .gitignore                          # Exclusions for virtual environments and cache
```

---

## 4. How to Run

### Run Unit Tests
```bash
python -m unittest test_sorting.py -v
```

### Run Benchmark Suite
```bash
python benchmark.py
```
