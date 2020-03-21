#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 12:29:43 2020

@author: mathvolcano

https://leetcode.com/problems/coin-change/

322. Coin Change
"""

def coinChange(coins, amount):
    if amount == 0:
        return 0
    
    toCheck = set([amount])
    level = 0
    while toCheck:
        level += 1
        temp = set()
        for x in toCheck:
            for c in coins:
                if x > c:
                    temp.add(x-c)
                elif x == c:
                    return level
        toCheck = temp
    return -1

coins = [1, 2, 5]
amount = 11
coinChange(coins, amount) # 3

coins = [474,83,404,3]
amount = 264
coinChange(coins, amount) # 8

coins = [2]
amount = 3
coinChange(coins, amount) # -1

coins = [1, 2, 5]
amount = 100
coinChange(coins, amount) # 20
