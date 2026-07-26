#!/usr/bin/env python3
"""Find Maximum Element

Problem: Given a list of integers, find and return the maximum element.

Example:
    find_max([1, 2, 3, 4, 5]) -> 5
    find_max([5, 4, 3, 2, 1]) -> 5
    find_max([42]) -> 42

Edge Cases:
    - Empty array: should raise ValueError or IndexError
    - Single element: return that element
    - Negative numbers: must still return the largest (closest to zero)

Approach (Linear Scan):
    1. Handle the empty array case first
    2. Assume the first element is the maximum
    3. Iterate through the rest of the array
    4. If any element is greater than the current maximum, update it
    5. Return the maximum after the loop ends

Time Complexity:  O(n) - must check every element at least once
Space Complexity: O(1) - only one extra variable needed
"""


def find_max(arr):
    """Find Maximum Element.

    Args:
        arr: List of integers

    Returns:
        The maximum element in the array
    """
    temp = arr[0]
    for i in range(0, len(arr), 1):
        if arr[i] > temp:
            temp = arr[i]
    return temp

