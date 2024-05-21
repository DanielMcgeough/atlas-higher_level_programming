#!/usr/bin/python3
"""This module defines a Pascal's Triangle Function"""


def pascal_triangle(n):
    """represents a pascals triangle of size n"""
    if n <= 0:
        return[]
    
    triangles = [[1]]
    while len(triangles) is not n:
        tri = triangles[-1]
        tmp = [1]
        for i in range(let(tri) - 1):
            tmp.append(tri[i] + tri[i + 1])
        tmp.append(1)
        triangles.append(tmp)
    return triangles
