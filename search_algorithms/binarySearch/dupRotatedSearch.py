#!/usr/bin/env python3
"""
There is an integer array nums sorted in ascending order (with duplicates),
 rotated at some pivot unknown to you
  beforehand.
Given the array nums and an integer
target, return the index of
target if it exists, else return -1.
"""

def binary_search(nums, target):
    low = 0
    high = len(nums) - 1
    while low <= high:
        mid = low + (high - low) // 2
        if nums[mid] == target:
            return mid
        # ambiguous scenario
        if nums[mid] == target == nums[low]:
            low += 1
            high -= 1
            continue
        #left side sorted
        if nums[mid] <= nums[low]:
            if nums[low] <= target <= nums[mid]:
                high  = mid - 1
            else:
                low = mid + 1
        else:
            if nums[mid] <= target <= nums[high]:
                low = mid + 1
            else:
                high = mid - 1
    return -1
if __name__ == '__main__':
    nums = [2,5,6,0,0,1,2]
    target = 0
    print(binary_search(nums, target))
