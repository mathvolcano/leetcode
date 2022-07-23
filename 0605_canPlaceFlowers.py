#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:21:41 2020

@author: mathvolcano

605. Can Place Flowers
https://leetcode.com/problems/can-place-flowers/
"""




def canPlaceFlowers(flowerbed, n: int) -> bool:
    l = len(flowerbed)
    # Length 0
    if l == 0: return n == 0

    if (l == 1):
        return n <= 1 * (flowerbed[0] == 0)
    if (l == 2):
        return n <= 1 - 1 * (1 in flowerbed)

    i,j = flowerbed[0], flowerbed[1]
    if i == j == 0:
        n -= 1
    cutoff = 2 if j == 0 else 3
    print(cutoff, flowerbed[cutoff:], n)
    return canPlaceFlowers(flowerbed[cutoff:], n)
