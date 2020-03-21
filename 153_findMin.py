#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 29 09:19:19 2020

@author: mathvolcano

153. Find Minimum in Rotated Sorted Array

https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

def findMin(nums):
    if len(nums) == 0: return -1
    if len(nums) == 1: return nums[0]
    
    l, r = 0, len(nums)-1
    
    while l+1 < r:
        mid = l + (r - l)//2
        if nums[mid] < nums[r]:
            r = mid
            continue
        if nums[l] < nums[mid]:
            l = mid
            continue
    return min(nums[l], nums[r])

nums = [3,4,5,1,2] 
findMin(nums) # 1

nums = [4,5,6,7,0,1,2]
findMin(nums) # 0

nums = [1,2]
findMin(nums)

nums = [1,2,3]
findMin(nums)