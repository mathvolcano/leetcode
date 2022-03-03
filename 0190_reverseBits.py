"""
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
