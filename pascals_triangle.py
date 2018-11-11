#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 17:29:02 2018

@author: mathvolcano

118. Pascal's Triangle
"""

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """
        if numRows == 0:
            return []
        pascal = [[1]]
        if numRows == 1:
            return pascal
        # Case 2 
        pascal = pascal + [[1,1]]
        if numRows == 2:
            return pascal
    
        else:
            for j in range(numRows-2):
                t = pascal[-1]
                mid_vals = [t[i] + t[i+1] for i in range(len(t)-1)]
                new_row = [1] + mid_vals + [1]
                pascal.append(new_row)
            return pascal
