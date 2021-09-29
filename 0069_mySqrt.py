"""
69. Sqrt(x)
https://leetcode.com/problems/sqrtx/
"""
class Solution:
    def mySqrt(self, x: int) -> int:
        # Trivial cases
        if x == 0: return 0
        if x == 1: return 1

        # Binary search on range [0,x]
        l, r = 0, x
        while l <= r:
            m = l + (r - l) // 2
            if m*m > x:
                r = m - 1
            elif (m*m < x):
                l = m + 1
            else:
                return m
        return r

        # Pythonic
        # from math import floor, sqrt
        # return int(floor(sqrt(x)))