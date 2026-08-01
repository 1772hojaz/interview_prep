#!/usr/bin/env python3
"""Find All Duplicates"""
"""[1,2,3,4,5"""

def find_duplicates(arr):
    """Find All Duplicates."""
    y = 0
    x = 0
    a = []

    while y < len(arr):
        x =y+1
        while x< len(arr):
            if arr[y] !=arr[x]):
                a.append(arr[y])
            x+=1
        y+=1
        

        
            

a = [1,2,3,4,5,6]
find_duplicates(a)
