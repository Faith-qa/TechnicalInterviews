#!/usr/bin/env python3
"""
Last Occurrence / Upper Bound - 1
Given a sorted array of integers nums
 (possibly with duplicates) and a target value, return
 the index of the last occurrence
of the target. Return -1 if not found.
"""

def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    results = -1

    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            results = mid
            high = mid - 1
        elif nums[mid] < target:
            low = mid + 1
        else:
            high = mid - 1

    return results

if __name__ == '__main__':
    arr = [ 5,  8, 12, 14,14, 17, 18, 21, 24 ]
    target = 14
    print(binarySearch(arr, target))