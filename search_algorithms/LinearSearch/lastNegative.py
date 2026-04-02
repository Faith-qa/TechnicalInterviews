#!/usr/bin/env python3

"""
Find Last Negative Number
Return the index of the rightmost negative number.
Return -1 if none found.
Example: [1, -4, 7, -2, -8, 3] → 4
"""

def linearSearch(arr):
    lastNeg = float('inf')
    for i in range(len(arr)):
        if arr[i] < 0:
            if arr[i] < lastNeg:
                lastNeg = arr[i]
    if lastNeg  == float('inf'):
        return -1
    else:
        return arr.index(lastNeg)


if __name__ == '__main__':
    arr = [1, -4, 7, -2, -8, 3]
    print(linearSearch(arr))