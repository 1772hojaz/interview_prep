#!/usr/bin/env python3
"""Sum of Array Elements

Problem: Given a list of integers, compute and return the sum
of all elements.

Example:
    sum_array([1, 2, 3, 4, 5]) -> 15
    sum_array([10, 20, 30]) -> 60
    sum_array([-1, 2, -3]) -> -2

Edge Cases:
    - Empty array: should raise ValueError or IndexError
    - Single element: return that element
    - All zeros: return 0
    - Mix of positive and negative numbers

Approach (Running Total):
    1. Initialize a variable with the first element
    2. Iterate through the remaining elements starting at index 1
    3. Add each element to the running total
    4. Return the total

Alternative: Use Python's built-in sum() function, but this
exercise practices the manual accumulation pattern.

Time Complexity:  O(n) - visit each element once
Space Complexity: O(1) - only one accumulator variable
"""


def sum_array(arr):
    """Sum of Array Elements.

    Args:
        arr: List of integers

    Returns:
        The sum of all elements in the array
    """
    pass
