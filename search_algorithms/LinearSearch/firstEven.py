#!/usr/bin/env python3
"""
ind First Even Number
Return the index of the first even number in the array.
Return -1 if no even number exists.
"""
def linearSearch(arr):
    for i in range(len(arr)):
        if arr[i] % 2 == 0:
            return i
    return -1


if __name__ == '__main__':
    arr = [5, 8, 3, 2, 9, 2]
    print(linearSearch(arr))