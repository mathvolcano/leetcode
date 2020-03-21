#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:17:36 2020

@author: mathvolcano

152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/
"""

def maxProduct(nums):
    if len(nums) <= 1:
        return nums[0] if len(nums) == 1 else 0
    
    best = nums[0]
    pos = neg = nums[0]
    for n in nums[1:]:
        pos, neg = max(n, n*pos, n*neg), min(n, n*pos, n*neg)
        best = max(best, pos)
    return best

nums = [2,3,-2,4]
maxProduct(nums)

nums = [-2,0,-1]
maxProduct(nums)
