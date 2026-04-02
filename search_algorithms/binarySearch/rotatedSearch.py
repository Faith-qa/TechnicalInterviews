#!/usr/bin/env python3
"""
There is an integer array nums sorted in ascending order (with no duplicates),
 rotated at some pivot unknown to you
  beforehand.
Given the array nums and an integer
target, return the index of
target if it exists, else return -1.
"""

def binarySearch(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low +(high-low)//2
        if nums[mid] == target:
            return mid
        # check left side sorted
        if nums [low] <= nums[mid]:
            if nums[low] <= target <= nums[mid]:
                high = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1

    return -1

if __name__ == '__main__':
    nums = [4,5,6,7,0,1,2]
    target = 0
    print(binarySearch(nums, target))