#!/usr/bin/env python3

"""
Linear search:- sequential search, iterates through a collection of elements one by one
from begining comparing each element with target
Advantages:
    1. simple loop
    2. efficient for small datasets
Given an array of integers nums and a target integer target, return the index of the first occurrence of target.
Return -1 if the target is not found.
"""

def linear_search(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
         return i # targe found returns he index
    return -1 # arget not found

if __name__ == '__main__':
    arr =  [70, 40, 30, 11, 57, 41, 25, 89, 27]
    target = 41
    print(linear_search(arr, target))
