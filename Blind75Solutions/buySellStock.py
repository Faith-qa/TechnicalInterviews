#!/usr/bin/env python3
class Solution:

    """
    You are given an array prices where prices[i] is the price of a given stock on the ith day.

You want to maximize your profit by choosing a single day to buy one stock and choosing a different day in the future to sell that stock.

Return the maximum profit you can achieve from this transaction. If you cannot achieve any profit, return 0.

    """

    def previus_two_sum_practice(self, nums, target):
        """
        practice for two sum done yesterday

        """

        hmap = {}

        for i in range(len(nums)):
            curr = nums[i]
            x = target - curr
            if x in hmap:
                return [i, hmap.get(x)]
            hmap[curr] = i
        return


    def dp_buysellstock(self, prices):


        """
        leverages on dynamic programming, this sollution:
        - has a time complexity of O(n) given we are traversing the array only once
        - it equally has a space complexity of O(1) as w are not taking any more space in memeory

        """

        bp = prices[0]
        profit = 0

        for i in range(1, len(prices)):
            if prices[i] < bp:
                bp = prices[i] #update the buying price to the smallest value

            else:
                currP = prices[i] - bp # find the current profit
                profit = max(currP, profit)

        return profit
