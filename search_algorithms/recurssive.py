#!/usr/bin/env python3

#recurssive function for addition
def add (n):
    if n <= 0:
        return 0
    return n + add(n - 1)

if __name__== "__main__":
    print(add(4))