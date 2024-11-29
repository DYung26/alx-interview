#!/usr/bin/python3

def makeChange(coins, total):
    if total <= 0:
        return 0

    dp = [float('inf')] * (total + 1)
    dp[0] = 0
    for coin in coins:
        for i in range(coin, total + 1):
            dp[i] = min(dp[i], dp[i - coin] + 1)

    return dp[total] if dp[total] != float('inf') else -1

'''
def makeChange(coins, total):
    if total <= 0:
        return 0
    coins.sort(reverse=True)
    t_coin = 0
    counter = 0
    for coin in coins:
        while coin + t_coin <= total:
            t_coin += coin
            counter += 1
        if t_coin == total:
            return counter
    return -1
'''
