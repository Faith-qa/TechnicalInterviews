#!/usr/bin/env python3
"""
Treat the array as circular (last element connects to first).
Return the smallest index where target appears (considering wrap-around).
If target appears multiple times, return the smallest valid index.
Return -1 if not found.
"""

def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

if __name__ == '__main__':
    nums = [6, 7, 8, 1, 2, 3]
    target = 8
    print(linearSearch(nums, target))