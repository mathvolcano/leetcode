#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jan 29 07:29:00 2020

@author: mathvolcano
"""

def frequencySort(s):
    
    if len(s) <= 0:
        return s
    
    # Count dict
    count_dict = {}
    for i in s:
        if i in count_dict:
            count_dict[i] = count_dict[i] + 1
        else:
            count_dict[i] = 1
    print(count_dict)
    # Convert counts to array
    count_array = [(k,count_dict[k]) for k in count_dict]
    count_array.sort(key=lambda x: x[1])
    str_order = [x[0] * x[1] for x in count_array[::-1]]
    new_str = ''.join(str_order)
    return new_str

ex1 = 'tree'
assert frequencySort(ex1) == 'eert'