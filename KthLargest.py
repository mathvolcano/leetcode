#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 19 07:38:08 2020

@author: mathvolcano

https://leetcode.com/problems/kth-largest-element-in-a-stream/

703. Kth Largest Element in a Stream
"""

from heapq import heapify, heappop, heappush, heappushpop
class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        self.k = k
        heapify(self.heap)
        while len(self.heap) > self.k:
            heappop(self.heap)

    def add(self, val: int) -> int:
        if len(self.heap) < self.k:
            heappush(self.heap, val)
        else:
            heappushpop(self.heap, val)
        return self.heap[0]