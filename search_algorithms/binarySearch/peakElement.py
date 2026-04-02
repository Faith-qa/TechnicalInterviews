#!/usr/bin/env python3
"""
Find Peak Element
A peak element is an element that is strictly greater than its neighbors.
Given a 0-indexed integer array nums,
find a peak element, and return its index.
The array may contain multiple peaks; return any of them.
You may imagine that nums[-1] = nums[n] = -∞.
"""

def binarySearch(nums):
    low = 0
    high = len(nums) - 1
    while low < high:
        mid = low + (high - low) // 2
        if nums[mid] > nums[mid+1]:
            #descending slope
            high = mid
        else:
            #ascending slope
            low = mid + 1

    return low

if __name__ == '__main__':
    print(binarySearch([1,2,3,1]))