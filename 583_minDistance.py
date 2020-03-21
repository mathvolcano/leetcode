#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 14:24:58 2020

@author: mathvolcano

583. Delete Operation for Two Strings
https://leetcode.com/problems/delete-operation-for-two-strings/
"""

def minDistance(word1, word2):
    rows = len(word1) +1
    cols = len(word2) + 1
    if rows == 1 or cols == 1:
        return max(rows, cols)
    
    matrix = [[0] * (cols) for i in range(rows)]
    
    for r in range(rows):
        for c in range(cols):
            if r == 0 or c == 0:
                matrix[r][c] = r + c
            elif word1[r-1] == word2[c-1]:
                matrix[r][c] = matrix[r-1][c-1]
            else:
                matrix[r][c] = min(matrix[r-1][c], matrix[r][c-1]) + 1

    return matrix[-1][-1]

minDistance("sea", "eat") # 2

minDistance('meet', 'greet') # 3