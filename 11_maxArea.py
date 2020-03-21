#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 28 17:28:09 2020

@author: mathvolcano

https://leetcode.com/problems/container-with-most-water/

11. Container With Most Water
"""

def maxArea(height):
    """Brute force O(n^2)"""
    most_water = 0
    if len(height) <= 1:
        return most_water
    
    def water(l, r):
        return min(height[l], height[r]) * (r - l)
    
    n = len(height)    
    left_right_width = [(i,j, j-i) for i in range(n)
                                   for j in range(n)
                                   if i<j]
    left_right_width.sort(key=lambda x: x[2], reverse=True)
    for lrw in left_right_width:
        l, r, w = lrw
        most_water = max(most_water, water(l, r))
    return most_water


def maxArea(height):
    """Better. O(n)"""
    most_water = 0
    if len(height) <= 1:
        return most_water
    
    def water(l, r):
        return min(height[l], height[r]) * (r - l)
    
    n = len(height)
  
    l, r = 0, n-1
    best_water = water(l, r)
    while l < r:
#        print(l, r, best_water)
        new_water = water(l,r)
        best_water = max(best_water, new_water)
        if height[l] < height[r]:
            l += 1
        else:
            r -= 1
    return best_water


        

nums = [1,8,6,2,5,4,8,3,7]
maxArea(nums) # 49

nums = [2,3,10,5,7,8,9]
maxArea(nums) # 36

nums = [1,3,2,5,25,24,5]
maxArea(nums) # 24