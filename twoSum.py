#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 16:14:57 2018

@author: mathvolcano

Two Sum
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        num_idx_pairs = [(x[1], x[0]) for x in enumerate(nums)]

        for i in range(len(nums)):
            num = nums[i]
            diff = target - num
            num_to_idx = dict(num_idx_pairs[i+1:])
            if diff in num_to_idx:
                return [i, num_to_idx[diff]]
        return(-1)