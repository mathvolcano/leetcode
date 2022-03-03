#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 11:17:45 2020

@author: mathvolcano

724. Find Pivot Index
https://leetcode.com/problems/find-pivot-index/
"""

def pivotIndex(nums):
    left_sum = 0
    right_sum = sum(nums)
    
    for i in range(len(nums)):
        right_sum -= nums[i]
        if left_sum == right_sum:
            return i
        left_sum += nums[i]
    
    return -1

nums = [1, 7, 3, 6, 5, 6]
pivotIndex(nums)

nums = [1, 2, 3]
pivotIndex(nums)

nums = [-1,-1,-1,0,1,1]
pivotIndex(nums)