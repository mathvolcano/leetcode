#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 06:01:02 2018

@author: mathvolcano

283 Move Zeros
Input: [0,1,0,3,12]
Output: [1,3,12,0,0]
https://leetcode.com/problems/move-zeroes/description/
"""

class Solution:
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        n_zeros_moved = 0
        counter = 0
        while counter < (n - n_zeros_moved):
            if nums[counter] == 0:
                nums.remove(nums[counter])
                nums.append(0)
                n_zeros_moved += 1
            else:
                counter += 1
        print(nums)