"""
Sorting Algorithms Implementation from scratch for Assignment 3.

Algorithms:
1. Selection Sort
2. Bubble Sort
3. Quick Sort (Lomuto partition scheme)
4. Merge Sort (Divide-and-Conquer)

Includes tracking of comparisons, swaps, and auxiliary space analysis.
All functions take an input list and return a sorted list copy.
"""

from typing import List, Tuple, TypeVar

T = TypeVar("T")


def selection_sort(arr: List[T]) -> Tuple[List[T], int, int]:
    """Sorts a list using Selection Sort.
    
    Time Complexity:
        - Best Case: O(N^2)
        - Average Case: O(N^2)
        - Worst Case: O(N^2)
    Space Complexity:
        - Auxiliary Space: O(1) in-place (no extra arrays needed).
    
    Returns:
        (sorted_list, comparisons_count, swaps_count)
    """
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0

    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            comparisons += 1
            if a[j] < a[min_idx]:
                min_idx = j
        if min_idx != i:
            a[i], a[min_idx] = a[min_idx], a[i]
            swaps += 1

    return a, comparisons, swaps


def bubble_sort(arr: List[T]) -> Tuple[List[T], int, int]:
    """Sorts a list using Bubble Sort (with early-exit optimization).
    
    Time Complexity:
        - Best Case: O(N) (when already sorted)
        - Average Case: O(N^2)
        - Worst Case: O(N^2) (reverse sorted)
    Space Complexity:
        - Auxiliary Space: O(1) in-place (no extra arrays needed).
        
    Returns:
        (sorted_list, comparisons_count, swaps_count)
    """
    a = list(arr)
    n = len(a)
    comparisons = 0
    swaps = 0

    for i in range(n):
        swapped = False
        for j in range(0, n - i - 1):
            comparisons += 1
            if a[j] > a[j + 1]:
                a[j], a[j + 1] = a[j + 1], a[j]
                swaps += 1
                swapped = True
        if not swapped:
            break

    return a, comparisons, swaps


def quick_sort(arr: List[T]) -> Tuple[List[T], int, int]:
    """Sorts a list using Quick Sort (in-place partitioning with recursion).
    
    Time Complexity:
        - Best Case: O(N log N)
        - Average Case: O(N log N)
        - Worst Case: O(N^2) (sorted or reverse-sorted inputs with standard last-element pivot)
    Space Complexity:
        - Auxiliary Space: O(log N) average call stack; O(N) worst-case call stack.
          In-place data partitioning (no full extra copy arrays created).
        
    Returns:
        (sorted_list, comparisons_count, swaps_count)
    """
    a = list(arr)
    comparisons = [0]
    swaps = [0]

    def _partition(low: int, high: int) -> int:
        pivot = a[high]
        i = low - 1
        for j in range(low, high):
            comparisons[0] += 1
            if a[j] <= pivot:
                i += 1
                if i != j:
                    a[i], a[j] = a[j], a[i]
                    swaps[0] += 1
        # Place pivot at i + 1
        if i + 1 != high:
            a[i + 1], a[high] = a[high], a[i + 1]
            swaps[0] += 1
        return i + 1

    def _quick_sort_recursive(low: int, high: int):
        if low < high:
            pi = _partition(low, high)
            _quick_sort_recursive(low, pi - 1)
            _quick_sort_recursive(pi + 1, high)

    if len(a) > 1:
        _quick_sort_recursive(0, len(a) - 1)

    return a, comparisons[0], swaps[0]


def merge_sort(arr: List[T]) -> Tuple[List[T], int, int]:
    """Sorts a list using Merge Sort (divide-and-conquer).
    
    Time Complexity:
        - Best Case: O(N log N)
        - Average Case: O(N log N)
        - Worst Case: O(N log N)
    Space Complexity:
        - Auxiliary Space: O(N) requires extra arrays during merging + O(log N) call stack.
          Not an in-place sort.
        
    Returns:
        (sorted_list, comparisons_count, swaps_count)
    """
    comparisons = [0]
    swaps = [0]  # Counts element assignments during merging

    def _merge_sort_recursive(lst: List[T]) -> List[T]:
        if len(lst) <= 1:
            return lst

        mid = len(lst) // 2
        left = _merge_sort_recursive(lst[:mid])
        right = _merge_sort_recursive(lst[mid:])

        merged = []
        i = 0
        j = 0
        len_l = len(left)
        len_r = len(right)

        while i < len_l and j < len_r:
            comparisons[0] += 1
            if left[i] <= right[j]:
                merged.append(left[i])
                swaps[0] += 1
                i += 1
            else:
                merged.append(right[j])
                swaps[0] += 1
                j += 1

        while i < len_l:
            merged.append(left[i])
            swaps[0] += 1
            i += 1

        while j < len_r:
            merged.append(right[j])
            swaps[0] += 1
            j += 1

        return merged

    result = _merge_sort_recursive(list(arr))
    return result, comparisons[0], swaps[0]
