"""
Unit tests for sorting algorithms.

Verifies:
1. Each algorithm produces correctly sorted output.
2. The original input array is never modified (immutability).
3. Algorithms handle edge cases (empty list, single element, duplicates, negative numbers).
"""

import os
import sys
import unittest

# Ensure src path is in sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))

from sorting_algorithms import bubble_sort, selection_sort, insertion_sort, merge_sort
from data_generator import ASCENDING_ARRAYS, get_descending_input


class TestSortingAlgorithms(unittest.TestCase):
    def setUp(self):
        self.algorithms = {
            "Bubble Sort": bubble_sort,
            "Selection Sort": selection_sort,
            "Insertion Sort": insertion_sort,
            "Merge Sort": merge_sort,
        }

    def test_ascending_inputs_correctness_and_immutability(self):
        """Test on the exact assignment ascending arrays."""
        for name, sort_fn in self.algorithms.items():
            for n, original in ASCENDING_ARRAYS.items():
                input_copy = list(original)
                result = sort_fn(input_copy)

                expected = list(range(1, n + 1))
                self.assertEqual(
                    result, expected, f"{name} failed on ascending array of size {n}"
                )
                self.assertEqual(
                    input_copy, original, f"{name} modified original array of size {n}"
                )

    def test_descending_inputs_correctness_and_immutability(self):
        """Test on descending arrays (worst-case inputs)."""
        for name, sort_fn in self.algorithms.items():
            for n in [5, 10, 50, 100]:
                original = get_descending_input(n)
                input_copy = list(original)
                result = sort_fn(input_copy)

                expected = list(range(1, n + 1))
                self.assertEqual(
                    result, expected, f"{name} failed on descending array of size {n}"
                )
                self.assertEqual(
                    input_copy, original, f"{name} modified original array of size {n}"
                )

    def test_edge_cases(self):
        """Test edge cases such as empty lists, single items, duplicates, and negative numbers."""
        for name, sort_fn in self.algorithms.items():
            # Empty list
            self.assertEqual(sort_fn([]), [])
            # Single element
            self.assertEqual(sort_fn([42]), [42])
            # Already sorted with duplicates
            self.assertEqual(sort_fn([1, 2, 2, 3]), [1, 2, 2, 3])
            # Negative numbers and duplicates
            self.assertEqual(sort_fn([5, -1, 3, -1, 0]), [-1, -1, 0, 3, 5])


if __name__ == "__main__":
    unittest.main()
