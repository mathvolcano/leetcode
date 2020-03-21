#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 08:05:44 2020

@author: mathvolcano

56. Merge Intervals
https://leetcode.com/problems/merge-intervals/
"""

def merge(intervals):
    if len(intervals) <= 1: return intervals
    
    intervals.sort(key=lambda x: x[0])
    
    l = 0
    r = 1
    checked = 0
    while checked < len(intervals):
        
        # Get intervals
        l_interval = intervals[l]
        if r < len(intervals):
            r_interval = intervals[r]
        else:
            break
        
        print(l_interval, r_interval)
        
        if l_interval[1] >= r_interval[0]:
            max_r = max(l_interval[1], r_interval[1])
            new_interval = [l_interval[0], max_r]
            del intervals[r]
        else:
            new_interval = r_interval
            l += 1
            r += 1
            checked += 1
        intervals[l] = new_interval
        
    return intervals

intervals = [[1,3],[2,6],[8,10],[15,18]]
merge(intervals) #Output: [[1,6],[8,10],[15,18]]

intervals = [[1,4],[4,5]]
merge(intervals)
#Output: [[1,5]]

intervals = [[1,4],[0,2],[3,5]]
merge(intervals)# [[0,5]]

intervals = [[2,3],[4,5],[6,7],[8,9],[1,10]]
merge(intervals) # [[1,10]]