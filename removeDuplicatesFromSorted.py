#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Oct 27 11:18:12 2018

@author: kevinschenthal

Remove Duplicates from Sorted Array

https://leetcode.com/explore/interview/card/top-interview-questions-easy/92/array/727/
"""

class Solution:
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) <2:
            return len(nums)

        i = 0
        j = 0
        n_unique = 1

        while i < len(nums):
            if nums[i] == nums[j]:
                i += 1
            else:
                n_unique += 1
                j += 1
                nums[j] = nums[i]
                i += 1
        return n_unique