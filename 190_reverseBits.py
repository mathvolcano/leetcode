#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Mar 10 18:13:41 2020

@author: mathvolcano

190. Reverse Bits
https://leetcode.com/problems/reverse-bits/
"""

def reverseBits(n):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        if bit:
            result += bit << (31 - i)
    return result

#Input: 00000010100101000001111010011100
#Output: 00111001011110000010100101000000
#Explanation: The input binary string 00000010100101000001111010011100 represents the unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.

reverseBits(43261596)