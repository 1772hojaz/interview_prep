#!/usr/bin/env python3
"""Second Largest Element

Problem: Given a list of integers, find and return the second
largest distinct element.

Example:
    second_largest([1, 2, 3, 4, 5]) -> 4
    second_largest([5, 5, 4, 3]) -> 4
    second_largest([1, 2]) -> 1

Edge Cases:
    - Empty array: should raise ValueError
    - Single element: should raise ValueError
    - Two elements: return the smaller one
    - Duplicates of the max: skip them to find true second
    - All elements the same: no valid second largest

Approach (Single-Pass with Two Variables):
    1. Handle arrays with fewer than 2 elements
    2. Initialize `first` and `second` to negative infinity
    3. For each number in the array:
       a. If num > first: shift first down to second, update first
       b. Else if num > second AND num != first: update second
    4. Return second

Why not sort? Sorting would be O(n log n). This approach finds
the answer in a single pass with O(n) time and O(1) space.

Time Complexity:  O(n) - single pass through the array
Space Complexity: O(1) - only two extra variables
"""


def second_largest(arr):
    """Second Largest Element.

    Args:
        arr: List of integers

    Returns:
        The second largest distinct element
    """
    #Todo:
        # make a temp variable that stores the first element
        # If the next element in the array is > than the temp, then store temp in the sec_ond variable 

    temp = arr[0]
    second = 0
    x = len(arr)
    if x == 0:
        raise ValueError("Empty array")
    elif x ==1:
        raise ValueError("Single element")

    for i in range(1, x, 1):
        #If the current number is greater than temp. Temp is replaced and the current number is put to be the second number
        if arr[i] > temp:
            second = temp
            temp = arr[i]

        # if the second number is less than the current and is not equal to temp then it should be the second number
        elif arr[i] > second and arr[i] != temp:
            second = arr[i]
        

 
    
    return second

a = [5, 1, 4, 2, 3]
print(second_largest(a))
