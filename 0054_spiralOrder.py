#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 20:21:41 2020

@author: mathvolcano

54. Spiral Matrix
https://leetcode.com/problems/spiral-matrix/
"""

def spiralOrder(matrix):
    # Set variables and return edge cases
    m = len(matrix)
    if m == 0: return matrix
    if m == 1: return matrix[0]
    n = len(matrix[0])
    if n == 0: return matrix
    if n == 1: return [x[0] for x in matrix]
    
    result = []
    # Loop around the matrix
    while matrix:
        # remove top row
        top_row = matrix.pop(0)
        result += top_row
        
        # Remove right column
        if matrix and matrix[-1]:
            right_column = [r.pop() for r in matrix]
            result += right_column
                
        # Remove bottom row
        if matrix:
            bottom_row = matrix.pop()
            result += bottom_row[::-1] # Reverse order bottom row
            
        if matrix and matrix[0]:
            left_column = [r.pop(0) for r in matrix]
            result += left_column[::-1]

    return result
    

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
spiralOrder(matrix)
# [1,2,3,6,9,8,7,4,5]

matrix =[
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
]
spiralOrder(matrix)
#Output: [1,2,3,4,8,12,11,10,9,5,6,7]

matrix = [[7],[9],[6]]
spiralOrder(matrix)

matrix = []
spiralOrder(matrix)

matrix = [[]]
spiralOrder(matrix)