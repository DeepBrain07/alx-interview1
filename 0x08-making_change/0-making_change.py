#!/usr/bin/python3
""" This module defines a function that
    determines the fewest number of coins
    needed to meet a given amount 'total'
"""


def makeChange(coins, total):
    """ Determines  the fewest number of coins
        needed to meet a given amount 'total'
    """
    if total <= 0:
        return 0

    sum = 0
    count = 0
    while True:
        if not coins or coins == []:
            return -1
        num = max(coins)
        count += 1
        if sum + num == total:
            return count
        elif sum + num > total:
            coins.remove(num)
            count -= 1
        else:
            sum += num
