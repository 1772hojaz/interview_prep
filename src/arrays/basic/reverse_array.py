#!/usr/bin/env python3
"""Reverse Array

Problem: Given a list of integers, return a new list with the
elements in reverse order.

Example:
    reverse_array([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
    reverse_array([10, 20, 30]) -> [30, 20, 10]
    reverse_array([1]) -> [1]

Edge Cases:
    - Empty array: return empty list
    - Single element: return as-is
    - Two elements: swap them
    - Palindrome: result equals original

Approach (Backward Iteration):
    1. Create an empty result list
    2. Start from the last index (len(arr) - 1) down to 0
    3. Append each element to the result
    4. Return the result

Alternative approaches:
    - Use slicing: return arr[::-1]
    - In-place swap: swap elements from both ends toward the center

Time Complexity:  O(n) - visit each element once
Space Complexity: O(n) for a new list, O(1) if done in-place
"""


def reverse_array(arr):
    """Reverse Array.

    Args:
        arr: List of integers

    Returns:
        A new list with elements in reverse order
    """
    pass
