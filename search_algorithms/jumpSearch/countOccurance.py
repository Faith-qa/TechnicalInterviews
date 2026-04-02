#!/usr/bin/env python3
import math
"""
ount Occurrences Efficiently
Given a sorted array, find how many times a number x appears using jump search as the main searching strategy.
Goal: try to avoid scanning the whole array even when there are many duplicates.
"""

def jumpSearch(arr, target):
    n = len(arr)
    step = int(math.sqrt(n))
    start = 0
    run = 0
    if n == 0:
        return -1

    while arr[min(step, n) - 1] < target:
        start = step
        step += int(math.sqrt(n))
        if start >= n:
            return -1

    # linear search
    while arr[start] < target:
        start += 1
        if start == min(step, n):
            return -1

    if arr[start] == target:
        run += 1

    return run


