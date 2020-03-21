#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 08:48:55 2020

@author: mathvolcano

62. Unique Paths
https://leetcode.com/problems/unique-paths/
"""

def uniquePaths(m,n):
    from math import factorial
    return factorial(m+n-2) // (factorial(m-1) * factorial(n-1))

uniquePaths(3,2)