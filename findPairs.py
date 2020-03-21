#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Jan 25 10:39:12 2020

@author: mathvolcano
"""

#https://leetcode.com/problems/k-diff-pairs-in-an-array/

#class Solution:
#    def findPairs(self, nums: List[int], k: int) -> int:
#            if k < 0:
#                return 0
#            n_total = 0
#            count_dict = {}
#            for n in nums:
#                if n in count_dict:
#                    if k == 0 and count_dict[n] == 1:
#                        n_total += 1
#                    # Ensure n won't be double counted
#                    count_dict[n] = -1
#                else:
#                    #won't duplicate since only new val can check existed val, no val can check twice.
#                    if (n + k in count_dict):
#                        n_total += 1
#                    if (n - k in count_dict):
#                        n_total += 1
#                    count_dict[n] = 1
#            return n_total

def findPairs(nums, k):
    if k < 0:
        return 0
    n_total = 0
    count_dict = {}
    for n in nums:
        if n in count_dict:
            if k == 0 and count_dict[n] == 1:
                n_total += 1
            # Ensure n won't be double counted
            count_dict[n] = -1
        else:
        	#won't duplicate since only new val can check existed val, no val can check twice.
            if (n + k in count_dict):
                n_total += 1
            if (n - k in count_dict):
                n_total += 1
            count_dict[n] = 1
    return n_total
    
ex_list1 = [3, 1, 4, 1, 5]
k1 = 2

assert findPairs(ex_list1, k1) == 2

ex_list2 = [1, 2, 3, 4, 5]
k2 = 1

assert findPairs(ex_list2, k2) == 4

ex_list3 = [1, 3, 1, 5, 4]
k3 = 0
assert findPairs(ex_list3, k3) == 1

ex_list4 = [6,3,5,7,2,3,3,8,2,4]
k4 = 2
