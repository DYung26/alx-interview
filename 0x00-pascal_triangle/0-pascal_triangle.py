#!/usr/bin/python3
"""
This module contains a function to generate Pascal's Triangle.

Pascal's Triangle is a triangular array of numbers where each number
is the sum of the two numbers directly above it in the previous row.
The module uses a custom factorial function to calculate
the binomial coefficients required to construct each row of Pascal's Triangle.
"""


def factorial(n):
    """
    Calculate the factorial of a number n.

    The factorial of a non-negative integer n is the product of all positive
    integers less than or equal to n. Factorial is represented as n! and
    is defined as:

        n! = n * (n - 1) * (n - 2) * ... * 1

    Args:
        n (int): The number to calculate the factorial for.

    Returns:
        int: The factorial of n.
    """
    result = 1
    for i in range(2, n + 1):
        result *= i
    return result


def pascal_triangle(n):
    """
    Generate Pascal's Triangle up to the nth row.

    Pascal's Triangle is a triangular array of numbers in which
    each number is the sum of the two directly above it in the previous row.
    The function uses binomial coefficients (calculated via the custom
    factorial function) to construct each row.

    Args:
        n (int): The number of rows of Pascal's Triangle to generate.
                 Must be a non-negative integer.

    Returns:
        List[List[int]]: A list of lists where each inner list represents
                         a row of Pascal's Triangle.
                         If n <= 0, returns an empty list.
    """

    if n <= 0:
        return []

    triangle = []
    for i in range(n):
        sub = []
        for j in range(i+1):
            sub.append(factorial(i)//(factorial(j)*factorial(i-j)))
        triangle.append(sub)
    return triangle
