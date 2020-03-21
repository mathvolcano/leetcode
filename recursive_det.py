#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 26 09:01:48 2020

@author: mathvolcano
"""

import numpy as np

A = np.array([[1,2,3],
              [4,5,6],
              [9, 8, 7]])

def recursive_det(mat):
    """Don't use np.linalg"""
    # State assumptions
    assert mat.shape[0] == mat.shape[1]
    assert mat.shape[0] > 0
    
    # Handle cases when dim = 1 and dim =2
    if mat.shape[0] == 1:
        det = mat[0,0]
    if mat.shape[0] == 2:
        det = (mat[1,1] * mat[0,0]) - (mat[0,1] * mat[1,0])
        
    # Define recursion
    if mat.shape[0] > 2:
        det = 0
        for j in range(0,len(mat)):
            sgn = (-1)**(j)
            sub_matrix = np.concatenate([mat[1:,:j], mat[1:,j+1:]], axis=1)
            print(sub_matrix)
            det += sgn * mat[0,j] * recursive_det(sub_matrix)
            print(det)
    return det
    
# Check results
A2 = np.array([[1,2], [3,4]])

A3 = np.array([[1,0,0],
              [0,-1,0],
              [0, 0, 1]])
    
A3_2 = np.array([[2,-3,1],
              [4,2,-1],
              [-5, 3, -2]])