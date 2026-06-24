#!/usr/bin/env python3

"""

Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.

"""
class solution:

    def hashSet_containsDup(self, nums):
        """
        optimal solution that leverages the power of hashsets
        and on the fact that hashsets dont contain duplicate
        has a time complexity of O(n)
        has a space complexity of O(n)
        """

        hSet = set()

        for i in nums:
            if i in hSet:
                return True
            hSet.add(i)
        return False



    def prev_buySellStock(self, prices):
        """optimal solution was dynamic programming"""
        minBp = prices[0]
        maxPr = 0

        for i in range(1, len(prices)):
            maxPr = max(maxPr, prices[i] - minBp)
            minBp = min(minBp, prices[i])

        return maxPr


    def prev_twoSum(self, nums, target):
        """
        optimal solution was hashmap
        time complexity: O(n)
        space Complexity: O(n)
        """
        hmap = {}
        for i in range(len(nums)):
            curr = nums[i]
            x = target - nums[i]
            if x in hmap:
                return [i, hmap.get(x)]
            hmap[curr] = i

        return
