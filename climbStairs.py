#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 07:27:30 2018

@author: mathvolcano

Climb Stairs
"""


class Solution:
    def climbStairs(self, n):
        # boundary case
        if n in (0, 1):
            return n
        
        n_ways = [0] * (n + 1)
        n_ways[0] = n_ways[1] = 1
        for i in range(2, n + 1):
            n_ways[i] = n_ways[i - 1] + n_ways[i - 2]
        return n_ways[n]
    