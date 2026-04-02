#!/usr/bin/env python3
"""
Find Second Smallest Element
Return the second smallest element in an array of distinct integers.
If fewer than 2 distinct elements exist → return some sentinel value (e.g. -1 or Integer.MAX_VALUE).
"""

def linearSearch(arr):
    fSmallest = float('inf')
    sSmallest = float('inf')
    for i in range (len(arr)):
        if arr[i] < fSmallest:
            sSmallest = fSmallest
            fSmallest = arr[i]
        elif fSmallest < arr[i] < sSmallest:
            sSmallest = arr[i]
    if sSmallest == float('inf'):
        return -1
    return sSmallest

if __name__ == "__main__":
    arr= [5, 8, 3, 2, 9, 2]
    print(linearSearch(arr))



