#!/usr/bin/env python3
"""
Find First Duplicate using Linear Search Only
Given an array containing numbers from 1 to n (with exactly one duplicate),
return the first number (in order of appearance) that appears more than once.
You may only use linear search — no hash set/map allowed.
Example: [1, 5, 3, 4, 6, 2, 4] → return 4
"""

def linear_search(nums):
   n = len(nums)
   for i in range(n):
      for j in range(i + 1, n):
         if nums[i] == nums[j]:
            return nums[i]
   return -1

if __name__ == '__main__':
   print(linear_search([1, 5, 3, 4, 6, 2, 4]))


