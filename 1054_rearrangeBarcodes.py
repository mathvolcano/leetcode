#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:48:27 2020

@author: mathvolcano

1054. Distant Barcodes

https://leetcode.com/problems/distant-barcodes/
"""

def rearrangeBarcodes(barcodes):
    from collections import Counter
    from heapq import heapify, heappop, heappush
    counts = Counter(barcodes)
    heap = [(-counts[n], n) for n in counts]
    heapify(heap)  # Compares the first attribute of the tuple
    # print pq
    result = []
    while len(heap) >= 2:
        count1, barcode1 = heappop(heap)
        count2, barcode2 = heappop(heap)
        result.extend([barcode1, barcode2])
        
        if count1 + 1: 
            heappush(heap, (count1 + 1, barcode1))
        if count2 + 1: 
            heappush(heap, (count2 + 1, barcode2))

    if heap:
        result.append(heap[0][1])
    
    return result

bc = [1,1,1,2,2,2]
rearrangeBarcodes(bc) # [2,1,2,1,2,1]

bc = [1,1,1,1,2,2,3,3]
rearrangeBarcodes(bc) # [1,3,1,3,2,1,2,1]

