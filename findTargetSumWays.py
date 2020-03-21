#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 18:39:46 2020

@author: mathvolcano

https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1389/
"""

class Solution:
    def findTargetSumWays(self, nums: List[int], S: int) -> int:
        if not nums:
            return 0
        if len(nums) == 0:
            return 0
        return self.dfs(nums, S, 0, 0)
    
    def dfs(self, nums, S, idx, total):
        n_ways = 0
        if idx == len(nums):
            if total == S:
                n_ways += 1
            return n_ways
        else:
            n_ways += self.dfs(nums, S, idx + 1, total + nums[idx]);
            n_ways += self.dfs(nums, S, idx + 1, total - nums[idx]);
            return n_ways
    
nums = [1, 1, 1, 1, 1]
S = 3
findTargetSumWays(nums, S) # 5
        