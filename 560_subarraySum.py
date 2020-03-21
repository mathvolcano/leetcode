#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 10:34:32 2020

@author: mathvolcano

560. Subarray Sum Equals K

https://leetcode.com/problems/subarray-sum-equals-k/
"""

def subarraySum(nums, k):
    from collections import defaultdict
    n_subarrays = 0
    s = 0
    
    # Count the sums of the arrays from beginning to each index.
    # Store sum in a hash table
    # If the complement is in the hash_table then add 1 to count
    hash_table = defaultdict(int) # sum: counts
    hash_table[0] = 1
    for n in nums:
        s += n
        
        if s-k in hash_table:
            n_subarrays += hash_table[s-k]
            
        hash_table[s] += 1
    
    return n_subarrays

nums = [1,1,1]
k = 2
subarraySum(nums, k)

nums = [-1,-1,1]
k = 0
subarraySum(nums, k)