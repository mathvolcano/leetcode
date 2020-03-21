#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb 22 15:15:26 2020

@author: mathvolcano

https://leetcode.com/problems/reorganize-string/

767. Reorganize String
"""



def reorganizeString(S):
    from collections import Counter
    from heapq import heapify, heappop
    counts = Counter(S)
    heap = [(-counts[n], n) for n in counts]
    heapify(heap)  # Compares the first attribute of the tuple
    S2 = ''
    previous_char = ''
    while heap:
        top1 = heappop(heap)
        if (previous_char != top1[1]):
            S2 = S2 + top1[1]
            top1 = (top1[0] +1, top1[1])
            previous_char = top1[1]
            if top1[0] < 0:
                heap = heap + [top1]
        elif (previous_char == top1[1]) and (len(heap) > 0):
            top2 = heappop(heap)
            S2 = S2 + top2[1]
            previous_char = top2[1]
            top2 = (top2[0] + 1, top2[1])
            if top2[0] < 0:
                heap = heap + [top1] + [top2]
            elif top2[0] == 0:
                heap = heap + [top1]
        else:
            return ''
        heapify(heap)
    return S2

S = 'aab'
reorganizeString(S) # 'aba'

S = 'aaab'
reorganizeString(S) # ''