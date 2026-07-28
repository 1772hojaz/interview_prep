#!/usr/bin/env python3
"""Remove Duplicates

Problem: Given a list of integers, return a new list with all
duplicate values removed. The relative order of the remaining
elements should be preserved.

Example:
    remove_duplicates([1, 2, 3, 2, 1]) -> [1, 2, 3]
    remove_duplicates([1, 1, 2, 3, 3, 3]) -> [1, 2, 3]
    remove_duplicates([5, 5, 5, 5]) -> [5]

Edge Cases:
    - Empty array: return empty list
    - Single element: return as-is
    - No duplicates: return a copy of the original
    - All elements the same: return single-element list

Approach (Seen Set / List Scan):
    1. Create an empty result list
    2. Iterate through each element in the input
    3. If the element is NOT already in the result, append it
    4. Return the result

Note: Checking `if item not in result` is O(n) per check, making
this approach O(n^2) overall. A more efficient approach would use
a hash set for O(1) lookups, but the result would need to be
built separately to maintain order.

Time Complexity:  O(n^2) with list check, O(n) with a hash set
Space Complexity: O(n) for the result
"""


def remove_duplicates(arr):
    """Remove Duplicates.

    Args:
        arr: List of integers

    Returns:
        A new list with duplicates removed, preserving order
    """


    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] == arr[j]:
                arr.remove(arr[j])
    return arr

a = [2,5,5,5,5,1]
print(remove_duplicates(a))
