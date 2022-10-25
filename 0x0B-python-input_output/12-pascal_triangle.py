#!/usr/bin/python3
"""Defines a Pascal's Triangle function."""


def pascal_triangle(n):
    """Represent Pascal's Triangle of size n.

    Returns a list of lists of integers representing the triangle.
    """
    if n <= 0:
        return []

    triangles = [[1]]
    while len(triangles) != n:
        tri = triangles[-1]
        hol = [1]
        for x in range(len(tri) - 1):
            hol.append(tri[x] + tri[x + 1])
        hol.append(1)
        triangles.append(tmp)
    return triangles
