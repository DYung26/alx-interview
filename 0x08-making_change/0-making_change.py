#!/usr/bin/python3
"""
Module for solving the coin change problem using dynamic programming.

This module contains the function `makeChange` that calculates the minimum
number of coins required to make a given total using a list of coins
denominations.
The function uses dynamic programming to efficiently find the optimal
solution.
"""


def makeChange(coins, total):
    """
    Returns the minimum number of coins needed to make the total amount.

    Args:
        coins (list): A list of integers representing the available coin
        denominations.
        total (int): The total amount that needs to be made using the given
        coin denominations.

    Returns:
        int: The minimum number of coins required to make the total, or -1 if
        it is not possible to make the total.

    This function utilizes a dynamic programming approach, where a dp array is
    used to store the minimum number of coins required for each amount from 0
    to total.
    The function iterates through each coin and updates the dp array to reflect
    the minimum coins
    required at each step. The result is found at dp[total], and if it is still
    infinity, the total cannot be made with the given coins.
    """
    dp = [float('inf')] * (total + 1)
    dp[0] = 0

    for i in range(len(coins) - 1, -1, -1):
        for j in range(1, total + 1):
            take = float('inf')
            noTake = float('inf')

            if j - coins[i] >= 0 and coins[i] > 0:
                take = dp[j - coins[i]]
                if take != float('inf'):
                    take += 1

            if i + 1 < len(coins):
                noTake = dp[j]

            dp[j] = min(take, noTake)

    return dp[total] if dp[total] != float('inf') else -1
