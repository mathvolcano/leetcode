#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Feb 21 08:38:37 2020

@author: mathvolcano

347. Top K Frequent Elements

https://leetcode.com/problems/top-k-frequent-elements/
"""



#def topKFrequent(nums, k):
#    # Get a sorted list of counts
#    from collections import Counter
#    hash_counter = Counter(nums)
#    count_array = [(k, hash_counter[k]) for k in hash_counter]
#    count_array.sort(key=lambda x: x[1], reverse=True)
#    
#    # Return counts
#    if len(count_array) <= k:
#        return [x[0] for x in count_array]
#    else:
#        return [x[0] for x in count_array[:k]]


# Do again with a heap
def topKFrequent(nums, k):
    from collections import Counter
    from heapq import heapify, heappop
    counts = Counter(nums)
    heap = [(-counts[n], n) for n in counts]
    heapify(heap)  # Compares the first attribute of the tuple
    return [heappop(heap)[1] for _ in range(k)]


topKFrequent([1,1,1,2,2,3], 2)
# [1,2]