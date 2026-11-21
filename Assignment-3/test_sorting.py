"""
Unit tests for Assignment 3 sorting algorithms.
Verifies correctness, ground truth matching, and array immutability.
"""

import unittest
from sorting_algorithms import selection_sort, bubble_sort, quick_sort, merge_sort
from data_generator import get_test_cases


class TestAssignment3Sorting(unittest.TestCase):
    def setUp(self):
        self.algorithms = {
            "Selection Sort": selection_sort,
            "Bubble Sort": bubble_sort,
            "Quick Sort": quick_sort,
            "Merge Sort": merge_sort,
        }

    def test_all_16_cases_correctness_and_immutability(self):
        for algo_name, sort_fn in self.algorithms.items():
            for case_id, size, order, data in get_test_cases():
                input_copy = list(data)
                sorted_result, comp, swaps = sort_fn(input_copy)

                expected = list(range(1, size + 1))
                self.assertEqual(
                    sorted_result,
                    expected,
                    f"{algo_name} failed on {case_id} ({size}, {order})",
                )
                self.assertEqual(
                    input_copy,
                    data,
                    f"{algo_name} mutated original input on {case_id} ({size}, {order})",
                )

    def test_edge_cases(self):
        for algo_name, sort_fn in self.algorithms.items():
            # Empty list
            res, _, _ = sort_fn([])
            self.assertEqual(res, [])
            # Single item
            res, _, _ = sort_fn([10])
            self.assertEqual(res, [10])
            # Duplicates
            res, _, _ = sort_fn([4, 2, 4, 1, 3])
            self.assertEqual(res, [1, 2, 3, 4, 4])
            # Negative numbers
            res, _, _ = sort_fn([0, -5, 3, -2, 1])
            self.assertEqual(res, [-5, -2, 0, 1, 3])


if __name__ == "__main__":
    unittest.main()
