#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 08:05:56 2020

@author: mathvolcano

Bubble Sort

Best case time complexity is O(n) when the array is already sorted.
Average & worst case both are O(n^2). 

Obama famously said "I think the bubble sort would be the wrong way to go." in
interview with Eric Schmidt.
"""

def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
arr = [64, 34, 25, 12, 22, 11, 90] 

