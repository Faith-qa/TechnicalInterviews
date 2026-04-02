#!/usr/bin/env python3
"""
Given a rod of length n inches and an array price[].
price[i] denotes the value of a piece of length i.
The task is to determine the maximum value obtainable by cutting
up the rod and selling the pieces.
Input: price[] =  [1, 5, 8, 9, 10, 17, 17, 20]
Output: 22
"""

def dynamic_programming(price, n):
    memo = [-1] * (n + 1)
    def best(l):
        if l == 0:
            return 0
        if memo[l] != -1:
            return memo[l]
        ans = 0
        for cut in range(1, l + 1):
            valOfCut = price[cut - 1]
            ans = max(ans, valOfCut + best(l - cut))
        memo[l] = ans
        return ans
    return best(n)


if __name__ == "__main__":
    price = [1, 5, 8, 9, 10, 17, 17, 20]
    print(dynamic_programming(price, 8))
