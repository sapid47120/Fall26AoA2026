"""
Input data setup for the sorting assignment.

Contains:
1. Exact ascending input arrays specified in the assignment sheet (Arr1 to Arr4).
2. Helper to generate descending (reverse-ordered) arrays for worst-case analysis.
"""

from typing import Dict, List

# Exact ascending arrays from the assignment specification:
# Arr1: N=5   {1, 2, 3, 4, 5}
# Arr2: N=10  {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
# Arr3: N=50  {1, 2, ..., 50}
# Arr4: N=100 {1, 2, ..., 100}
ASCENDING_ARRAYS: Dict[int, List[int]] = {
    5: [1, 2, 3, 4, 5],
    10: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    50: list(range(1, 51)),
    100: list(range(1, 101)),
}


def get_ascending_input(n: int) -> List[int]:
    """Returns a copy of the ascending input array for size N."""
    if n in ASCENDING_ARRAYS:
        return list(ASCENDING_ARRAYS[n])
    return list(range(1, n + 1))


def get_descending_input(n: int) -> List[int]:
    """Generates a descending list [N, N-1, ..., 1] for size N.

    Reverse order creates maximum inversions, which triggers the worst-case
    behavior for Bubble Sort and Insertion Sort.
    """
    return list(range(n, 0, -1))
