#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 07:26:53 2020

@author: mathvolcano

191. Number of 1 Bits

https://leetcode.com/problems/number-of-1-bits/
"""

def hammingWeight(n):
    result = n & 1
    while n:
        n = n >> 1
        result += n & 1
    return result
