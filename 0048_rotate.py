#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar 15 20:14:29 2020

@author: mathvolcano

48. Rotate Image
https://leetcode.com/problems/rotate-image/
"""

def rotate(matrix):
    n = len(matrix)
    if n <= 1: return matrix
    
    # Transpose
    for i in range(n):
        for j in range(0, i+1):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
            
    # Exchange cols
    for j in range(n // 2):
        for i in range(n):
            matrix[i][j], matrix[i][n-1-j] = matrix[i][n-1-j], matrix[i][j]
    
    return
            
matrix = [
  [1,2,3],
  [4,5,6],
  [7,8,9]
]
rotate(matrix)
#[
#  [7,4,1],
#  [8,5,2],
#  [9,6,3]
#]

matrix = [
  [ 5, 1, 9,11],
  [ 2, 4, 8,10],
  [13, 3, 6, 7],
  [15,14,12,16]
]
rotate(matrix)
matrix = [
  [15,13, 2, 5],
  [14, 3, 4, 1],
  [12, 6, 8, 9],
  [16, 7,10,11]
]