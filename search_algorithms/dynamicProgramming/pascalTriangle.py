#!/usr/bin/env python3
"""

"""

def pascal_triangle(n):
    if n == 0:
        return
    triangle = []
    for i in range(n):
        row = [1] * (i + 1)
        # fill middle values
        for j in range(1, i):
            row[j] = triangle[i-1][j-1] + triangle[i-1][j]
        triangle.append(row)

        print(row)






if __name__ == '__main__':
    print(pascal_triangle(5))
