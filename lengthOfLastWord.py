#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 10 08:41:12 2018

@author: kevinschenthal

Length of Last Word
"""

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_lst = s.strip().split(' ')
        return len(word_lst[-1])
    
def lengthOfLastWord(s):
    """
    :type s: str
    :rtype: int
    """
    word_lst = s.strip().split(' ')
    return len(word_lst[-1])