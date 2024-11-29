#!/usr/bin/python3

def makeChange(coins, total):
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
