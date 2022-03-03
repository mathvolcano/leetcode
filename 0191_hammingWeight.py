"""
191. Number of 1 Bits
https://leetcode.com/problems/number-of-1-bits/
"""

def hammingWeight(n):
    # [1] Check last bit of n and 1 and add to a result counter (initialized at 0)
    # [2] shift bits to the right by 1, loop until n == 0
    # Time complexity the number of bits in n, or O(lg n)
    # Space complexity: O(1)
    res = 0
    while n:
        res += n & 1
        n = n >> 1
    return res
