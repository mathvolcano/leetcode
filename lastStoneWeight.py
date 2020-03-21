#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 07:44:19 2020

@author: mathvolcano

https://leetcode.com/problems/last-stone-weight/

1046. Last Stone Weight
"""

from heapq import _heapify_max, _heappop_max, heappush
def lastStoneWeight(stones):
    _heapify_max(stones)
    while len(stones) >= 2:
        largest = _heappop_max(stones)
        largest2 = _heappop_max(stones)
        diff = largest - largest2
        if diff > 0:
            heappush(stones, diff)
            _heapify_max(stones)
    
    if len(stones) == 1:
        return stones[0]
    if len(stones) == 0:
        return 0

stones = [2,7,4,1,8,1]
lastStoneWeight(stones)

stones = [1,3]
lastStoneWeight(stones)