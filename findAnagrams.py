#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:53:25 2020

@author: mathvolcano

438. Find All Anagrams in a String
"""

def findAnagrams(s, p):
    if (len(s) == 0):
        return None
    if len(p) > len(s):
        return None
    
    p_sorted = ''.join(sorted(p))
    
#    n_len_p_strs = len(s) - len(p) + 1
    grams = [''.join(sorted(s[i:i+len(p)]))
             for i in range(len(s) - len(p) + 1)]
    idx_matches = []
    for i, g in enumerate(grams):
        if g == p_sorted:
            idx_matches.append(i)
    if idx_matches:
        return idx_matches
    return idx_matches if idx_matches else None
    
    

s1 = "cbaebabacd"
p1 = "abc"
assert findAnagrams(s1, p1) == [0, 6]

s2 = "abab"
p2 = "ab"
assert findAnagrams(s2, p2) == [0, 1, 2]
