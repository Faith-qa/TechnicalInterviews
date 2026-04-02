#!/usr/bin/env python3
"""
Find Minimum in Rotated Sorted Array
Suppose an array of length n sorted in ascending order
is rotated between 1 and n times.
Find the minimum element in
this rotated sorted array.
(Assume no duplicates for this version.)
"""

def binarySearch(arr):
    low = 0
    high = len(arr) - 1
    while low < high:
        mid = low + (high - low) // 2
        #if minimum is in the right half
        if arr[mid] > arr[high]:
            low = mid + 1
        # minimum is on the left
        else:
            high = mid
    return arr[low]

if __name__ == '__main__':
    arr = [3,4,5,1,2]
    print(binarySearch(arr))
