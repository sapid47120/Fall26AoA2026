"""
Sorting Algorithms Implementation from Scratch.

Implemented algorithms:
1. Bubble Sort (includes early-exit flag for sorted inputs)
2. Selection Sort (finds the minimum element and places it in front)
3. Insertion Sort (builds the sorted list one item at a time)
4. Merge Sort (standard divide-and-conquer approach)

All functions return a sorted copy and do not modify the original input array.
"""

from typing import List, TypeVar

T = TypeVar("T")


def bubble_sort(arr: List[T]) -> List[T]:
    """Sorts a list using Bubble Sort.

    How it works:
        Compares adjacent elements and swaps them if they are in the wrong order.
        An early-exit flag stops the algorithm if no swaps occur during a pass.

    Time Complexity:
        - Best Case (already sorted): O(N)
        - Average Case: O(N^2)
        - Worst Case (reverse sorted): O(N^2)
    Space Complexity: O(1) auxiliary space (excluding the output copy).
    """
    a = list(arr)
    n = len(a)
    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swapped = True
        # If no elements were swapped, the list is already sorted
        if not swapped:
            break
    return a


def selection_sort(arr: List[T]) -> List[T]:
    """Sorts a list using Selection Sort.

    How it works:
        Repeatedly finds the smallest item in the unsorted portion
        and swaps it into its correct position at the front.

    Time Complexity:
        - Best Case: O(N^2)
        - Average Case: O(N^2)
        - Worst Case: O(N^2)
    Space Complexity: O(1) auxiliary space (excluding the output copy).
    """
    a = list(arr)
    n = len(a)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if a[j] < a[min_idx]:
                min_idx = j
        # Swap the found minimum element with the current position
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
    return a


def insertion_sort(arr: List[T]) -> List[T]:
    """Sorts a list using Insertion Sort.

    How it works:
        Takes each element one by one and inserts it into its correct
        position among the previously sorted elements by shifting larger items.

    Time Complexity:
        - Best Case (already sorted): O(N)
        - Average Case: O(N^2)
        - Worst Case (reverse sorted): O(N^2)
    Space Complexity: O(1) auxiliary space (excluding the output copy).
    """
    a = list(arr)
    n = len(a)
    for i in range(1, n):
        key = a[i]
        j = i - 1
        # Shift elements that are greater than key to one position ahead
        while j >= 0 and a[j] > key:
            a[j + 1] = a[j]
            j -= 1
        a[j + 1] = key
    return a


def merge_sort(arr: List[T]) -> List[T]:
    """Sorts a list using Merge Sort (divide-and-conquer).

    How it works:
        Recursively splits the list into two halves until single-element lists remain,
        then merges the sorted halves back together in ascending order.

    Time Complexity:
        - Best Case: O(N log N)
        - Average Case: O(N log N)
        - Worst Case: O(N log N)
    Space Complexity: O(N) auxiliary space for sub-arrays during merging.
    """
    a = list(arr)
    if len(a) <= 1:
        return a

    mid = len(a) // 2
    left = merge_sort(a[:mid])
    right = merge_sort(a[mid:])

    return _merge(left, right)


def _merge(left: List[T], right: List[T]) -> List[T]:
    """Helper function to merge two sorted lists into one sorted list."""
    merged = []
    i = 0
    j = 0
    len_l = len(left)
    len_r = len(right)

    while i < len_l and j < len_r:
        if left[i] <= right[j]:
            merged.append(left[i])
            i += 1
        else:
            merged.append(right[j])
            j += 1

    # Append any remaining items
    while i < len_l:
        merged.append(left[i])
        i += 1

    while j < len_r:
        merged.append(right[j])
        j += 1

    return merged
