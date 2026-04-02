#!/usr/bin/env python3
"""
Find Minimum Element using Linear Search
Without using any built-in min() function, find and return the smallest element in the array.
Assume the array is non-empty.
"""

def linearSearch(arr):
    minVal = arr[0]
    for i in range (1, len(arr)):
        if arr[i] < minVal:
            minVal = arr[i]
    return minVal

if __name__ == "__main__":
    nums = [4, 2, 7, 2, 9, 2]
    print(linearSearch(nums))
