#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 17:55:55 2020

@author: mathvolcano

268. Missing Number
https://leetcode.com/problems/missing-number/
"""

def missingNumber(nums):
    all_ints = list(range(len(nums)+1))
    
    for n in nums:
        all_ints[n] = -1
        
    for n in all_ints:
        if n >= 0:
            return n

nums = [3,0,1]
missingNumber(nums) # 2

nums = [9,6,4,2,3,5,7,0,1]
missingNumber(nums) # 8

nums = [1]
missingNumber(nums) # 0