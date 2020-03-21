#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 15:56:39 2020

@author: mathvolcano

55. Jump Game
https://leetcode.com/problems/jump-game/
"""

def canJump(nums):
    if len(nums) <= 1:
        return True
    
    n = len(nums)
    i = n - 1
    can_win = [False] * i + [True]
    smallest_win_idx = n -1
    while i >= 0:
        len_to_end = smallest_win_idx - i
        if nums[i] >= len_to_end:
            can_win[i] = True
            smallest_win_idx = i
        
        i -= 1  
    return can_win[0]

nums = [2,3,1,1,4]
canJump(nums) # True

canJump([3,2,1,0,4]) # False

nums = [2,0,0]
canJump(nums) # True
