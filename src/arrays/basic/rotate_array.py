#!/usr/bin/env python3
"""Rotate Array

Problem: Given a list of integers, rotate (reverse) the array
and return a new list with elements in reversed order.

Example:
    rotate_array([1, 2, 3, 4, 5]) -> [5, 4, 3, 2, 1]
    rotate_array([10, 20, 30]) -> [30, 20, 10]

Edge Cases:
    - Empty array: return empty list
    - Single element: return as-is
    - Two elements: swap them
    - Double rotation returns original array

Approach (Manual Reverse with New List):
    1. Create an empty list
    2. Iterate through the input array in reverse order
    3. Append each element to the new list
    4. Return the new list

Time Complexity:  O(n) - visit each element once
Space Complexity: O(n) for the new list
"""


def rotate_array(arr):
    """Rotate Array.

    Args:
        arr: List of integers

    Returns:
        A new list with elements in reversed order
    """
    a = []
    for element in arr[::-1]:
        a.append(element)

    return a

x = [1,2,3,4,5]
print(rotate_array(x))
