#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Feb 18 08:02:44 2020

@author: mathvolcano

https://leetcode.com/problems/valid-palindrome-ii/

680. Valid Palindrome II
"""

def validPalindrome(s):
    def is_palindrome(s):
        return s == s[::-1]
    
    if len(s) <= 1:
        return True
    
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] != s[r]:
            return is_palindrome(s[:l] + s[l+1:]) | is_palindrome(s[:r] + s[r+1:])
        l += 1
        r -= 1
    return True

s = "aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga"
