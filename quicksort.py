#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 07:40:53 2020

@author: mathvolcano

Quicksort - O(nlogn) time complexity in best & average cases. Worst case O(n^2)

Divide & conquer strategy for sorting a list

Divide: partition the array into 2 (possibly empty) subarrays A[p...q-1] and
A[q+1..r] such that each element of A[p..q-1] is <= A[q] and is in turn
A[q] <= A[q+1..r]. Compute the index q as part of this partition procedure

Conquer: sort 2 subarrays A[p..q-1] and A[q+1..r] by recursive calls to quicksort.

Why use quicksort over merge sort? Because it's memory optimized, space efficient
O(n) for pointers & buffers, and the algorithm has stability. 

Merge sort has better worst case time complexity with O(nlogn).

https://en.wikipedia.org/wiki/Quicksort#Hoare_partition_scheme
"""

def quicksort(a_list):

    def _quicksort(a_list, low, high):
        # must run partition on sections with 2 elements or more
        if low < high: 
            p = partition(a_list, low, high)
            _quicksort(a_list, low, p)
            _quicksort(a_list, p+1, high)
    
    def partition(a_list, low, high):
        pivot = a_list[low]
        while True:
            while a_list[low] < pivot:
                low += 1
            while a_list[high] > pivot:
                high -= 1
            if low >= high:
                return high
            a_list[low], a_list[high] = a_list[high], a_list[low]
            low += 1
            high -= 1
    _quicksort(a_list, 0, len(a_list)-1)

array = [97, 200, 100, 101, 211, 107]
# array -> [97, 100, 101, 107, 200, 211]