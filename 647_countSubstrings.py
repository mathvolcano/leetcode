#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 17:48:21 2020

@author: mathvolcano

647. Palindromic Substrings

https://leetcode.com/problems/palindromic-substrings/
"""

def countSubstrings(s):
    n = len(s)
    if n <= 1: return n
    
    count = 0
    for i in range(n):
        count += 1
        
        # count odd length palindroms
        l = i-1
        r = i+1
        while l >= 0 and r <= n-1 and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
        
        # Count even length palindromes
        l = i
        r = i+1
        while l >= 0 and r <= n-1 and s[l] == s[r]:
            count += 1
            l -= 1
            r += 1
    return count
    
s = 'aaa'
countSubstrings(s) # 6

s = 'abc'
countSubstrings(s) # 3
