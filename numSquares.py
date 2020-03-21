#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 19:32:02 2020

@author: mathvolcano

https://leetcode.com/explore/learn/card/queue-stack/231/practical-application-queue/1371/

Perfect Squares
Given a positive integer n, find the least number of perfect square numbers (for example, 1, 4, 9, 16, ...) which sum to n.
"""

def numSquares(n):
    if n < 3:
        return n
    squares = []
    i = 1
    while i * i <= n:
        squares.append( i * i )
        i += 1
    depth = 0
    toCheck = {n}
    while toCheck:
        depth += 1
        temp = set()
        for x in toCheck:
            for s in squares:
                if x == s:
                    return depth
                if x < s:
                    break
                temp.add(x-s)
        toCheck = temp

    return depth

assert numSquares(13) == 2
#Explanation: 13 = 4 + 9

assert numSquares(12) == 3
#Input: n = 12
#Output: 3 
#Explanation: 12 = 4 + 4 + 4.