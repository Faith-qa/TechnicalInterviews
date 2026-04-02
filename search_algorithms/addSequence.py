#!/usr/bin/env python3

def add(n):
    tot = 0
    for i in range(n):
        tot += pairSum(i, i+1)
    return tot

def pairSum(x, y):
    return x + y

if __name__ == "__main__":
    print(add(4))