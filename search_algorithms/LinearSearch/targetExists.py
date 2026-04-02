#!/usr/bin/env python3
"""
Exists or Not (Boolean)
Return true if target exists in the array, false otherwise.
(No index needed — just presence check)
"""

def linearSearch(arr, target):
   for i in range(len(arr)):
       if arr[i] == target:
           return True

   return False
if __name__ == "__main__":
    nums = [1, 3, 3, 4, 3, 5]
    target = 9
    print(linearSearch(nums, target))