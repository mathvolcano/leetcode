#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 05:22:59 2018

@author: mathvolcano

Leetcode searchInsert
"""

def searchInsert(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: int
    """
    n = len(nums)
    for i in range(n):
        val = nums[i]
        if val < target:
            pass
        elif val >= target:
            return i
    return n