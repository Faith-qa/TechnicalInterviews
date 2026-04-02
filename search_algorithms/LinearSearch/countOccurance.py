#!/usr/bin/env python3
"""
Return how many times target appears in the array.
"""

def linear_search(arr, target):
    count = 0
    for i in range(len(arr)):
        if arr[i] == target:
            count += 1

    if count > 0:
        return count
    else:
        return -1

if __name__ == '__main__':
    nums = [1, 3, 3, 4, 3, 5]
    target = 3
    print(linear_search(nums, target))