#!/usr/bin/env python3
"""Sum of Array Elements"""


def sum_array(arr):
    """Sum of Array Elements.
    
    Args:
        arr: List of integers
        
    Returns:
        Result based on problem description
    """
    temp = arr[0]
    for i in range(1, len(arr), 1):
        temp = temp + arr[i]
    return temp

a = [1,2,3,4,5]

print(sum_array(a))
