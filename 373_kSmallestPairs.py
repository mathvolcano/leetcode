#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb 23 14:27:37 2020

@author: mathvolcano

373. Find K Pairs with Smallest Sums
https://leetcode.com/problems/find-k-pairs-with-smallest-sums/
"""

def kSmallestPairs(nums1, nums2, k):
    from heapq import heapify, heappop
    all_pairs_heap = [(n1+n2, n1, n2)
                      for n1 in nums1
                      for n2 in nums2]
    heapify(all_pairs_heap)
    if k < len(all_pairs_heap):
        return [heappop(all_pairs_heap)[1:] for _ in range(k)]
    else:
        return [[x[1], x[2]] for x in all_pairs_heap]

nums1 = [1,7,11]
nums2 = [2,4,6]
k = 3
kSmallestPairs(nums1, nums2, k) # [1,2],[1,4],[1,6]

nums1 = [1,1,2]
nums2 = [1,2,3]
k = 2
kSmallestPairs(nums1, nums2, k) # [1,1],[1,1]

nums1 = [1,2]
nums2 = [3]
k = 3
kSmallestPairs(nums1, nums2, k) # [1,3],[2,3]

