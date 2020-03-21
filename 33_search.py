#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:09:40 2020

@author: mathvolcano

https://leetcode.com/problems/search-in-rotated-sorted-array/

33. Search in Rotated Sorted Array
"""

def search(nums, target):
    if len(nums) == 0:
        return -1
    
    n = len(nums)
    left = 0
    right = n-1
    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        if nums[left] == target:
            return left
        if nums[right] == target:
            return right
        if nums[mid] <= nums[right]:
            if (nums[mid] < target < nums[right]):
                left = mid + 1
                right -= 1
            else:
                right = mid - 1
                left += 1
        else:
            if (nums[left] < target < nums[mid]):
                right = mid - 1
                left += 1
            else:
                left = mid + 1
                right -= 1
    
    return -1

nums = [4,5,6,7,0,1,2]
search(nums, 0) # 4

search([], 0) # -1

search([1], 0) # -1

search([1], 1) # 0
