#!/usr/bin/env python3
import math
"""
does lower number of searches than linear search
linear search:- search through an element by passing through all the elements in
comparison to the target
linear search problem:- takes O(n)
how jump start works:- takes an element a with a jump size of n
it divides the array into number of blocks
list is sorted
"""
def jumpSearch(arr, target):
    starr = sorted(arr)
    n = len(arr)

    step = math.sqrt(len(starr)) # find the step size
    start = 0 #starting index
    while starr[int(min(step, n) - 1)] < target:
        start = step
        step += math.sqrt(n)
        if start >= n:
            return -1
    # do a linear search
    while starr[int(start)] < target:
        start +=1
        if start == min(step, n):
            return -1
    if starr[int(start)] == target:
        return start
    return -1

if __name__ == "__main__":
    arr = [ 0, 1, 1, 2, 3, 5, 8, 13, 21,
            34, 55, 89, 144, 233, 377, 610 ]
    x = 39
    print(jumpSearch(arr, x))



    start = 0
    end = 3

