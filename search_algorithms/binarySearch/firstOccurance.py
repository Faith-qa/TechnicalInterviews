#!/usr/bin/env python3
"""
First Occurrence / Lower Bound
Given a sorted array of integers nums that may contain
duplicates and a target value target, return the index of the
first occurrence of target. If target is not found, return -1.
"""

def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    result = -1
    while low <= high:
        mid = low + (high - low) // 2 # define the mid pointer
        # checks target is present at mid
        if nums[mid] == target:
            result = mid
            low = mid + 1
        elif nums[mid] < target: #if target is greater, ignote the left half
            low = mid + 1
        else: # if target is smaller, ignore the right half
            high = mid - 1
    return result

if __name__ == '__main__':
    arr = [ 5,  8, 12, 14,14, 17, 18, 21, 24 ]
    target = 14
    print(binarySearch(arr, target))