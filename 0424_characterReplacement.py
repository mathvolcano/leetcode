#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  8 10:59:10 2020

@author: mathvolcano

424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/
"""

def characterReplacement(s, k):
    """sliding window."""
    from collections import Counter
    n = len(s)
    if n <= 1: return n
    
    # Keep a running count of character frequencies
    char_counts = Counter()
    longest = 0
    l = r = 0
    while r < n:
        char_counts[s[r]] += 1
        r += 1
        count_most_common_char = max(char_counts.values())
        while r - l - count_most_common_char > k:
            char_counts[s[l]] -= 1
            l += 1
        longest = max(longest, r - l)
    return longest

s = "AABABBA"
k = 1
characterReplacement(s, k)