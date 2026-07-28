#!/usr/bin/env python3
"""Merge Two Sorted Arrays

Problem: Given two sorted arrays of integers, merge them into
a single sorted array.

Example:
    merge_sorted([1, 3, 5], [2, 4, 6]) -> [1, 2, 3, 4, 5, 6]
    merge_sorted([1, 2, 3], [4, 5, 6]) -> [1, 2, 3, 4, 5, 6]
    merge_sorted([], [1, 2, 3]) -> [1, 2, 3]

Edge Cases:
    - One or both arrays empty
    - Arrays of different lengths
    - Duplicate values across or within arrays
    - Negative numbers

Approach (Two-Pointer Merge):
    1. Initialize two pointers, i and j, both at index 0
    2. Compare arr1[i] and arr2[j]
    3. Append the smaller value to the result and advance that pointer
    4. Repeat until one array is fully consumed
    5. Append all remaining elements from the other array

This is the same merge logic used in the Merge Sort algorithm.

Time Complexity:  O(n + m) where n and m are the lengths of the two arrays
Space Complexity: O(n + m) for the result array
"""


def merge_sorted(arr1, arr2):
    """Merge Two Sorted Arrays.

    Args:
        arr1: First sorted list of integers
        arr2: Second sorted list of integers

    Returns:
        A new sorted list containing all elements from both arrays
    """
    i = 0
    j = 0
    a = []
    while i < len(arr1) and j < len(arr2):
        if arr1[i] < arr2[j]:
            a.append(arr1[i])
            i += 1
        else:
            a.append(arr2[j])
            j+=1

    while i < len(arr1):
        a.append(arr1[i])
        i+=1

    while j < len(arr2):
        a.append(arr2[j])
        j+=1
    return a

