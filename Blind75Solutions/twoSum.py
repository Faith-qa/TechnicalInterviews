#!/usr/bin/env python3

class Solution:


    def hashmap_twosum(self, nums, target):
        """ most optimal solution:-
    - leverages on hashmaps and dictionaries
    - loops the array only once
    - has a time complexity of O(n) and space complexity of O(1)
    """
        hmaps = {}
        for i in range(len(nums)):
            curr = nums[i]
            x = target - curr
            if x in hmaps:
                return([i, hmaps.get(x)])
            hmaps[curr] = x
        return

    def bruteforce_twosum(self, nums, target):
        """
        - loops through the entire array one at a time
        - slow as it goes through the array multiple times
        - has a time complexity of O(n2) and a space complexity of O(n)
        """

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[j] == target - nums[i]:
                    return [i, j]

        return []





