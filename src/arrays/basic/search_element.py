#!/usr/bin/env python3
"""Search Element

Problem: Given an element and a list of integers, search for the
element in the array. Return 1 if found, 0 if not found.

Example:
    search_element(3, [1, 2, 3, 4, 5]) -> 1
    search_element(6, [1, 2, 3, 4, 5]) -> 0

Edge Cases:
    - Empty array: element is not found
    - Single element: match or no match
    - Element at first or last position
    - Negative numbers in the array

Approach (Linear Search):
    1. Iterate through each index of the array
    2. Compare the current element with the target
    3. If a match is found, return 1 immediately
    4. If the loop ends without a match, return 0

This is the simplest search algorithm. For sorted arrays, binary
search (O(log n)) would be more efficient, but linear search works
on any array regardless of order.

Time Complexity:  O(n) - worst case checks every element
Space Complexity: O(1) - no extra space needed
"""


def search_element(element, arr):
    """Search Element.

    Args:
        element: The element being searched for
        arr: List of integers

    Returns:
        1 if element is found, 0 otherwise
    """
    pass
