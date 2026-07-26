#!/usr/bin/env python3
"""Search Element"""


def search_element(element,arr):
    """Search Element.
    
    Args:
        element: The element being searched for
        arr: List of integers
        
    Returns:
        Result based on problem description
    """
    for i in range(0,len(arr), 1):
        if element == arr[i]:
            print(f"{element} found")
            return 1
        
    print("element not found")
    return 0


            

a = [1,2,3,4,5]
l = 5
x = 6
print(search_element(l,a))
print(search_element(x,a))

