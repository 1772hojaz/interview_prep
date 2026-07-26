#!/usr/bin/env python3
"""Rotate Array"""


def rotate_array(arr):
    """Rotate Array.
    
    Args:
        arr: List of integers
        
    Returns:
        Result based on problem description
    """
    a = []
    for element in arr[::-1]:
        a.append(element)
    return a

array = [1,2,3,4,5]

print(rotate_array(array))
