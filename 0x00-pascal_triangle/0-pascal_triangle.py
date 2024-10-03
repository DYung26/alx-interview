#!/usr/bin/env python3
from math import factorial


def pascal_triangle(n):
    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        sub = []
        for j in range(i+1):
            sub.append(factorial(i)//(factorial(j)*factorial(i-j)))
        triangle.append(sub)
    return triangle
