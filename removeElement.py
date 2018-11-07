#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov  7 05:43:08 2018

@author: mathvolcano

Remove element
https://leetcode.com/problems/remove-element/description/
"""

class Solution:
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.remove(nums[i])
            else:
                i += 1
        return len(nums)