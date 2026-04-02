#!/usr/bin/env python3
"""
Find the Insertion Point
Given a sorted array of distinct
integers nums and a target value target,
 return the index where target would be inserted to keep the array sorted (same behavior as lower_bound in C++). If target already exists, return its index.
"""

def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low +(high - low)// 2
        if nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return low

if __name__ == '__main__':
    arr = [ 5,  8, 12, 14,14, 17, 18, 21, 24 ]
    target = 26
    print(binarySearch(arr, target))
