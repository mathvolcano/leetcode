#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Nov 11 09:08:01 2018

@author: kevinschenthal

20. Valid Parentheses
"""

class Solution:
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        s = s.replace(' ', '')  # Remove whitespace
        parentheses_pairs = ['()', '[]', '{}']
        is_valid = True
        l_previous = len(s)
        while l_previous > 0:
            for parenth in parentheses_pairs:
                if parenth in s:
                    s = s.replace(parenth, '')
            l_new = len(s)
            if l_previous == l_new:
                is_valid = False
                break
            l_previous = l_new
        return is_valid
