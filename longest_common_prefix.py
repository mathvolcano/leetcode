#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 04:47:01 2018

@author: mathvolcano
"""

def longestCommonPrefix(strs):
    """
    :type strs: List[str]
    :rtype: str
    """
    
    longest_prefix = ''
    l = 1
    while l > 0:
        prefixes = [x[:l] for x in strs]
        if len(set(prefixes)) == 1:
            if longest_prefix == prefixes[0]:  # Handle null input ['']
                break
            longest_prefix = prefixes[0]
            l += 1
        else:
            l = -1
    return longest_prefix