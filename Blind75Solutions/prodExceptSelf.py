#!/usr/bin/env python3

"""
Given an integer array nums, return an array output where output[i] is the product of all the elements of nums except nums[i].

Each product is guaranteed to fit in a 32-bit integer.

Follow-up: Could you solve it in
O(n)
O(n) time without using the division operation?

"""

class Solution:
    """
    optimal solution returns a time complexity of O(n) and a space complexity of o(n)
    involves a running prod on the left and right
    """

    def opt_productExceptSelf(self, nums):
        res = [1] * len(nums)
        leftProd = 1
        for i in range(len(nums)):
            res[i] = leftProd
            leftProd *= nums[i]
        rightProd = 1
        for i in range(len(nums) - 1, -1, -1):
            res[i] *= rightProd
            rightProd *= nums[i]
        return res

    """
    secondOptimal solution sacrifices for space complexity hence still attains an O(n) time
    complexity and O(n) space complexity
    it uses the prefic and suffix approach by creating two lists
    """

    def prefSuff_productExceptSelf(self, nums):
        n = len(nums)
        res = [1] * n
        pref = [1] * n
        suff = [1] * n

        for i in range(1, n):
            pref[i] = nums[i-1] * pref[i-1]
        for i in range(n - 2, -1, -1):
            suff[i] = nums[i+1] * suff[i+1]

        for i in range(n):
            res[i] = pref[i] * suff[i]
        return res


    """Practice for contains dup"""
    def practice_containsDup(self, nums):
        hashset = set()

        for i in nums:
            if i in hashset:
                return True
            hashset.add(i)
        return False

    """practice for buy and sell stalk:- optimal sollution"""

    def practice_buySellStalk(self, prices):

        minBp = prices[0]
        maxProfit = 0

        for i in range(1, len(prices)):
            if prices[i] < minBp:
                minBp = prices[i]
            else:
                currPr = prices[i] - minBp
                maxProfit = max(maxProfit, currPr)

        return maxProfit

    """Practice fot twoSum problem"""
    def practice_twoSum(self, nums, target):
        hmap = {}

        for i in range(len(nums)):
            curr = nums[i]
            x = nums[i] - curr
            if x in hmap:
                return[i, hmap.get(x)]
            hmap[curr] = i
        return 0
