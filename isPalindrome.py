#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Feb  6 07:25:26 2020

@author: mathvolcano
"""

def isPalindrome(x):
    if x < 0:
        return False
    
    x_reversed = 0
    x2 = x
    
    # Build a reversed integer
    while x2 >= 1:
        x_reversed = x_reversed*10 + (int(x2) % 10)
        x2 = x2 / 10
        print(x_reversed, x2)
        
    return x_reversed == x

isPalindrome(1)
isPalindrome(121)