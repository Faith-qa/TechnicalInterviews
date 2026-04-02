#!/usr/bin/env python3
"""
binarySearch:- only works in sorted list
    - involves spliting the list into two halves and finds a target value
    by starting from the middle of a sorted array eliminating the half
    of the remaining elements in each stop

"""

def binarySearch(arr, target):
    low = 0 # lowest pointer
    high = len(arr) - 1 # high pointer

    while low <= high:
        mid = low + (high - low) // 2 # define the mid pointer
        # checks target is present at mid
        if arr[mid] == target:
            return mid
        elif arr[mid] < target: #if target is greater, ignote the left half
            low = mid + 1
        else: # if target is smaller, ignore the right half
            high = mid - 1

    return -1


if __name__ == '__main__':
    arr = [ 5,  8, 12, 14, 17, 18, 21, 24 ]
    target = 14
    print(binarySearch(arr, target))

