#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:30:36 2020

@author: mathvolcano

3. Longest Substring Without Repeating Characters

https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

def lengthOfLongestSubstring(s):
    """Sliding window. Move 2 pointers. O(n) complexity"""
    if len(s) <= 1: return len(s)
    
    i = 0 # 2 pointers
    j = 0
    len_longest = 0
    n = len(s)
    hash_set = set()
    
    while j < n:
        if s[j] not in hash_set:
            hash_set.add(s[j])
            j += 1
            len_longest = max(len(hash_set), len_longest)
        else:
            hash_set.remove(s[i])
            i += 1
    return len_longest

s = "abcabcbb"
lengthOfLongestSubstring(s) # 3, 'abc'

s = "bbbbb"
lengthOfLongestSubstring(s) # '1'

s = "pwwkew"
lengthOfLongestSubstring(s)

