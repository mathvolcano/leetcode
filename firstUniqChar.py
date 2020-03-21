#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Jan 30 07:24:05 2020

@author: mathvolcano

387. First Unique Character in a String
"""

def firstUniqChar(s):
    if len(s) == 0:
        return -1
    else:
        # 0. Count the number of occurences in a dict – can use collections Counter
        count_dict = {}
        for c in s:
            if c in count_dict:
                count_dict[c] += 1
            else:
                count_dict[c] = 1
        # 1. Iterate through string and look up count in dict. If 1 then return.
        for idx, c2 in enumerate(s):
            if count_dict[c2] == 1:
                return idx
        return -1

s = "leetcode"
assert firstUniqChar(s) == 0
#return 0.
#
s2 = "loveleetcode"
assert firstUniqChar(s2) == 2
#return 2.

