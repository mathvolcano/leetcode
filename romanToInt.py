#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 26 17:22:52 2018

@author: mathvolcano

Roman Numerals
"""

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        symbol_to_val = {'I': 1,
                         'V': 5,
                         'X': 10,
                         'L': 50,
                         'C': 100,
                         'D': 500,
                         'M': 1000}
        symbol_pairs_to_vals = [('IV', -2),
                                ('IX', -2),
                                ('XL', -20),
                                ('XC', -20),
                                ('CD', -200),
                                ('CM', -200)]
        pairs_to_val_dict = dict(symbol_pairs_to_vals)
        int_total = 0
        for letter in s:
            int_total += symbol_to_val[letter]
            
        for symbol_pair in [x[0] for x in symbol_pairs_to_vals]:
            if symbol_pair in s:
                int_total += pairs_to_val_dict[symbol_pair]
                
        return int_total
            

