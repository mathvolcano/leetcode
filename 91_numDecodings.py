#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 18 10:00:26 2020

@author: mathvolcano

91. Decode Ways
https://leetcode.com/problems/decode-ways/
"""

def numDecodings(s):
    if len(s) < 1: return len(s)
    valid_substrings = [str(x) for x in range(1,27)]
    
    def is_valid(string):
        return string in valid_substrings
    
    # count the number of ways to decode s[:i]
    dp = [0] * (len(s) + 1)
    dp[0] = 1
    dp[1] = 1 if is_valid(s[0]) else 0
    
    # The number of encodings is equal to  number of encodings of s[:i-1] if 
    # the last character is valid. If the last 2 characters are valid then
    # we must add the number of encodings of s[:i-2]
    for i in range(2, len(s)+1):
        dp[i] += is_valid(s[i-1:i]) * dp[i-1] + is_valid(s[i-2:i]) * dp[i-2]
    
    return dp[-1]


s = "12"
numDecodings(s) # 2

numDecodings("226")

s = "0"
numDecodings(s)