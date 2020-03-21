#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar 21 10:17:16 2020

@author: mathvolcano

378. Kth Smallest Element in a Sorted Matrix
https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix/
"""

def kthSmallest(matrix, k):
    n = len(matrix)
    if n == 0: return
    n2 = n**2
    if k > n2: return 
    
    # Use a heap
    from heapq import heapify, heappop
    nums = [e for r in matrix for e in r]
    heapify(nums)
    
    # Get the kth smallest element
    result = 0
    for i in range(k):
        result = heappop(nums)
    return result


matrix = [
   [ 1,  5,  9],
   [10, 11, 13],
   [12, 13, 15]
]
k = 8
kthSmallest(matrix, k)

matrix = [[1,2],[1,3]]
k = 2
kthSmallest(matrix,k) # 1
