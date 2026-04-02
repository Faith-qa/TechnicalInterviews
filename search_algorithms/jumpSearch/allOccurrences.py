#!/usr/bin/env python3
import math
from operator import index

"""
eturn All Occurrences
Modify jump search to return a list of all indices where the target appears (in ascending order).
If the element is not found → return empty list []
"""

def jumpSearch(arr, target):
    n = len(arr)
    if n == 0:
        return []
    # keep original indices in sorted array
    indexedArr = sorted([(value, index) for index, value in enumerate(arr)])

    step = int(math.sqrt(n))
    prev = 0

    #find block with a posibility of arget
    while prev < n and indexedArr[min(step, n) - 1][0] < target:
        prev = step
        step += int(math.sqrt(n))
        if prev >= n:
            return []

    # perform linear search
    while prev < min(step, n) and indexedArr[min(step, n) - 1][0] < target:
        prev += 1

    if prev >= n or indexedArr[prev][0] != target:
        return []

    result = []
    i = prev
    while i < n and indexedArr[i][0] == target:
        result.append(indexedArr[i][1])
        i += 1

    return sorted(result)


if __name__ == '__main__':
    arr = [4, 2, 7, 2, 9, 2, 5]
    target = 2

    print(jumpSearch(arr, target))





