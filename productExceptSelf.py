#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 07:39:20 2020

@author: mathvolcano

238. Product of Array Except Self

https://leetcode.com/problems/product-of-array-except-self/
"""

def productExceptSelf(nums):
    
    n = len(nums)
    
    # 1. Calculate cumulative product of all nums to left of the index
    prod = 1
    result = []
    for i in range(n):
        result.append(prod)
        prod *= nums[i]
    
    # 2. Multiple result by cumulative product of all nums to right of the index
    prod = 1
    for i in range(n-1, -1, -1):
        result[i] = result[i] * prod
        prod *= nums[i]
    
    return result

productExceptSelf([1,2,3,4])

productExceptSelf([0,0])