#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 07:40:55 2020

@author: mathvolcano
"""

def thirdMax(nums):
    if len(nums) <= 0:
        return None
    nums_unique = list(set(nums))
    nums_unique.sort(reverse=True)
    if len(nums_unique) < 3:
        return nums_unique[0]
    return nums_unique[2]


ex1 = [3,2,1]
assert thirdMax(ex1) == 1

ex2 = [1, 2]
assert thirdMax(ex2) == 2

ex3 = [2, 2, 3, 1]
assert thirdMax(ex3) == 1
