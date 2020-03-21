#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 19:23:44 2020

@author: mathvolcano

338. Counting Bits
https://leetcode.com/problems/counting-bits/
"""

def countBits(num):
    dp = [0]
    i = 0
    while True:
        # Partition the range dyadically
        subrange = range(1<<i, 1<<(i+1))
        for j in subrange:
            if j > num:
                return dp
            # count bits in this range – dyadic so the results are 1 + start of previous range
            val = 1 + dp[j - (1<<i)]
            dp.append(val)
        i += 1
    return dp

num = 12
countBits(num)