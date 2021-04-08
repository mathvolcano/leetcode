"""
Created on Mon Feb 10 08:05:56 2020

@author: mathvolcano

Bubble Sort
"""

def bubbleSort(arr):
    n = len(arr)
    
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                
arr = [64, 34, 25, 12, 22, 11, 90] 

