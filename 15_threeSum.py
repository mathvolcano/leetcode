#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar  2 07:52:10 2020

@author: mathvolcano

15. 3Sum

https://leetcode.com/problems/3sum/
"""

def threeSum(nums):
    """find sets of unique  abc such that a+b+c = 0."""
    n = len(nums)
    solution_set = []
    
    for i in range(n):
        target = - nums[i]
        hash_set = set()
        for j in range(i+1, n):
            diff = target - nums[j]
            if diff not in hash_set:
                hash_set.add(nums[j])
            else:
                solution = [nums[i], nums[j], diff]
                solution.sort()
                solution_set.append(tuple(solution))
    
    unique_solutions = list(set(solution_set))
    return [list(x) for x in unique_solutions]


nums = [-1, 0, 1, 2, -1, -4]

threeSum(nums)
#[
#  [-1, 0, 1],
#  [-1, -1, 2]
#]