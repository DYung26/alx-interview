#!/usr/bin/python3

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
