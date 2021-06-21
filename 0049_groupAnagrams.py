#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Mar  1 11:47:02 2020

@author: mathvolcano

49. Group Anagrams

https://leetcode.com/problems/group-anagrams/
"""

def groupAnagrams(strs):
#    from collections import Counter
    if len(strs) <= 1: return [strs]
    
    strs_to_counts = [(s, tuple(sorted(s))) for s in strs]
    reverse_dict = {}
    for kv in strs_to_counts:
        k, v = kv
        if v in reverse_dict:
            reverse_dict[v].append(k)
        else:
            reverse_dict[v] = [k]
    
    return list(reverse_dict.values())

ls = ["eat", "tea", "tan", "ate", "nat", "bat"]

groupAnagrams(ls)
#[
#  ["ate","eat","tea"],
#  ["nat","tan"],
#  ["bat"]
#]

l2 = ["",""]
groupAnagrams(l2)
