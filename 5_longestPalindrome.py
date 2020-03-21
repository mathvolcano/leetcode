#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Mar  7 16:43:41 2020

@author: mathvolcano

5. Longest Palindromic Substring
https://leetcode.com/problems/longest-palindromic-substring/
"""

#def longestPalindrome(s):
#    """Brute force."""
#    if len(s) <= 0:
#        return len(s)
#    
#    pointer_pairs = [(i,j) for i in range(len(s))
#                           for j in range(len(s)) if j>= i]
#    palindrome_len = [(s[x[0]:x[1]] == s[x[0]:x[1]][::-1], x[1]-x[0])
#                      for x in pointer_pairs]
#    palindrome_len = [x for x in palindrome_len if x[0]]
#    palindrome_len.sort(key=lambda x: x[1], reverse=True)
#    return palindrome_len[0][1]
    
def longestPalindrome(s):
    """Expanding window. O(n^2)"""
    
    n = len(s)
    if n <= 1: return len(s)
    
    def expand_window(s, l, r):
        """Get the longest length palindrome centered at l=r"""
        if len(s) == 0 or (l > r): return 0
        
        while l >= 0 and (r < n) and s[l] == s[r]:
            l -= 1
            r += 1
        return r-l-1
    
    start = 0
    end = 0
    
    for i in range(n):
        len_odd = expand_window(s, i, i)
        len_even = expand_window(s, i, i+1)
        longer_len = max(len_odd, len_even)
        
        if longer_len > end - start:
            start = i - (longer_len -1 ) // 2
            end = i + longer_len // 2


    return s[start: end+1]


s = "babad"
longestPalindrome(s)

s = "cbbd"
longestPalindrome(s)