#!/usr/bin/env python3
"""
Given an integer array nums, find a subarray that has the largest product, and return the product.

A subarray is a contiguous non-empty sequence of elements within an array.

You can assume the output will fit into a 32-bit integer.

Note that the product of an array with a single element is the value of that element.
"""

class Solution:
    """Kadenes Algorithm approach:-
    works on two facts:-
     - a negative * negative = positive
     meaning a small negative can change the dymanics and suddenly become the max product
     therefore at every index, their is need to track currMax, currMin
    - time complexity :- O(n) , space Complecity O(1)
    """

    def kadenMaxProd(self, nums):
        currMin, currMax = 1, 1
        res = max(nums)

        for n in nums:
            if n == 0:
                currMax, currMin = 1,1
                continue
            tmp = n * currMax
            currMax = max(currMax * n, n, currMin * n)
            currMin = min(tmp, currMin * n, n)
            res = max(currMax, res)
        return res

    def practice_maxSubArray(self, nums):
        """kadenes algorithm:- O(n), O(1)"""
        maxSum = nums[0]
        currSum = 0
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSum = max(currSum, maxSum)
        return maxSum

    def practice_productExceptSelf(self, nums):
        res = [1] * len(nums)
        leftProd = 1
        for i in range(len(nums)):
            res[i] = leftProd
            leftProd *= nums[i]

        rightProd = 1
        for i in range(len(nums)-1,-1,-1):
            res[i] *= rightProd
            rightProd *= nums[i]
        return res

    def practice_contDuplicates(self, nums):
        hset = set()

        for i in nums:
            if i in hset:
                return True
            hset.add(i)
        return False

    def practice_buySellStock(self, prices):
        maxProf = 0
        minBp = prices[0]

        for i in range(1, len(prices)):
            maxProf = max(maxProf, prices[i] - minBp)
            minBp = min(prices[i], minBp)
        return maxProf

    def practice_twoSum(self, nums, target):
        hmap = {}
        for i in range(len(nums)):
            x = target - nums[i]
            if x in hmap:
                return [i, hmap.get(x)]
            hmap[nums[i]] = i
        return 0

