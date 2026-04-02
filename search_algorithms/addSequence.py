#!/usr/bin/env python3
# resources:
"""
video Playlist:- https://savanna.alxafrica.com/rltoken/_4-JUPlg6lfKZO2YPHCA7g
space complexty: https://savanna.alxafrica.com/rltoken/QK9ENdoTyqGs0d4_M3XE3g
search algorithm:- https://savanna.alxafrica.com/rltoken/ap2kuRv8qrUMyQ0-MY3EXw
"""
def add(n):
    tot = 0
    for i in range(n):
        tot += pairSum(i, i+1)
    return tot

def pairSum(x, y):
    return x + y

if __name__ == "__main__":
    print(add(4))