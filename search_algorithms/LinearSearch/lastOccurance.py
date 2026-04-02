#!/usr/bin/env python3
"""
Given an array of integers nums and a target integer target, return the index of the last occurrence of target.
Return -1 if the target is not found.
"""

def linear_search(arr, target):
    tempHold = []
    for i in range(len(arr)):
        if arr[i] == target:
            tempHold.append(i)

    if len(tempHold) != 0:
        return tempHold[-1]
    return -1

if __name__ == "__main__":
    nums = [4, 2, 7, 2, 9, 2]
    target = 2
    print(linear_search(nums, target))
