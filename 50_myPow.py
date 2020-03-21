#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 09:00:13 2020

@author: mathvolcano

50. Pow(x, n)
https://leetcode.com/problems/powx-n/
"""

def myPow(x, n):
    result = 1
    power = n
    if n < 0:
        power, x = -power, 1./x
    while power:
        if power & 1:
            result *= x
        x *= x
        power = power >>1
    return result

myPow(2.00000, 10) # 1024

myPow(2.10000, 3) # 9.26100

myPow(2.00000, -2) # 0.25
