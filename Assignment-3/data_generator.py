"""
Input dataset generator for Assignment 3.

Test Cases:
1. Size 5, Sorted: [1, 2, 3, 4, 5]
2. Size 5, Reverse Sorted: [5, 4, 3, 2, 1]
3. Size 100, Sorted: [1, 2, ..., 100]
4. Size 100, Reverse Sorted: [100, 99, ..., 1]
"""

from typing import Dict, List, Tuple

TEST_CASES: List[Tuple[str, int, str, List[int]]] = [
    ("Case 1", 5, "Sorted", [1, 2, 3, 4, 5]),
    ("Case 2", 5, "Reverse Sorted", [5, 4, 3, 2, 1]),
    ("Case 3", 100, "Sorted", list(range(1, 101))),
    ("Case 4", 100, "Reverse Sorted", list(range(100, 0, -1))),
]


def get_test_cases() -> List[Tuple[str, int, str, List[int]]]:
    """Returns the list of 4 required test cases."""
    return TEST_CASES
