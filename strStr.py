#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 06:57:27 2018

@author: mathvolcano

strStr
"""

class Solution:
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """
        ln = len(needle)
        
        # Null Case
        if ln == 0:
            return 0
        
        # Get number of attempts
        n_tries = len(haystack) - ln + 1
        
        idx = -1  # case not found
        for i in range(n_tries):
            sub_str = haystack[i: i + ln]
            if sub_str == needle:
                idx = i
                break
        return idx
    