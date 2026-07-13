#!/usr/bin/env python3
"""
Given an array of integers nums, find the subarray with the largest sum and return the sum.

A subarray is a contiguous non-empty sequence of elements within an array.

Example 1:

Input: nums = [2,-3,4,-2,2,1,-1,4]

Output: 8
"""

class Solution:

    def kadAlgoMaxSubArray(self, nums):
        """the Kadenes Algorthm:- works on the assumption that if a running sum is negative, keeping
        it will only reduce the sum of future sub arrays so whenever the current sum
        drops below zero, it resets to zero and we start a new subarray
        time Complexity :- O(n)
        space complexity :- O(1)
        """
        currSum = 0
        maxSum = nums[0]
        for i in nums:
            if currSum < 0:
                currSum = 0
            currSum += i
            maxSum = max(currSum, maxSum)
        return maxSum

    def dpMaxSubArray(self, nums):
        """
        works by declaring a dp table where dp[i]:- represents the maximum subarray ending at index i
        at every position we have a simple choice:_
        - start a new subarray at the current element
        - extend the subarray that ended at the previous index

        therefore if the sum upto to the previous index is negative, extending it would only make
        things worse, so we start a fresh at the current element

        time complexity :- O(n)
        spaceComplexity :- O(n) because of the dp arrat
        """
        dp = [*nums]

        for i in range(1, len(nums)):
            dp[i] = max(nums[i], nums[i] + dp[i-1])
        return max(dp)

    def bruteForceMaxSubArray(self, nums):
        """
        involves trying every possible subarray, calculating it's sum and keeping track of the max sum
        time Complexity:- O(n2)
        not very effective
        """

        n, res = len(nums), nums[0]
        for i in range(n):
            curr = 0
            for j in range(1, n):
                curr += nums[j]
                res = max(res, curr)

        return res

    def practice_prodExceptSelf(self, nums):
        """
        best approach rakes on a timecomplexity of O(n) and a space complexity ob o(1)
        involves multipllying the left and right returning the array
        create a prod from the begining left side and right end
        """
        res = [1] * len(nums)
        leftProd = 1
        for i in range(len(nums)):
            res[i] = leftProd
            leftProd *= nums[i]
        rightProd = 1
        for i in range(len(nums)-1, -1,-1):
            res[i] *= rightProd
            rightProd *= nums[i]
        return res

    def practice_containsDup(self, nums):
        """
        best approach is leveraging the concepts of a hashset i.e a data structure that takes no
        duplicate
        because of the hashset the space complexity will be O(n)
        """
        hSet = set()

        for i in nums:
            if i in hSet:
                return True
            hSet.add(i)
        return False

    def practice_buySellStock(self, prices):
        """leverages on a dynamic programming approach
        where as we traverse the array we update the maxprfit and have a running minimum bp

        """
        maxP = 0
        minBp = prices[0]

        for i in range(1, len(prices)):
            maxP = max(maxP, prices[i] - minBp)
            minBp = min(minBp, prices[i])
        return maxP


    def practice_twoSum(self, nums, target):
        """leverage on the concept of hashmaps to track sum of two values in the array"""
        hmaps = {}
        for i in range(len(nums)):
            curr = nums[i]
            x = target - curr
            if x in hmaps:
                return[i, hmaps.get(x)]
            hmaps[curr] = i
        return 0






