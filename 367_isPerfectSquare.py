"""
367. Valid Perfect Square
https://leetcode.com/problems/valid-perfect-square/
"""

class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        if num == 1: return True

        l, r, = 0, num // 2  # all n > 1 have sqrt(n) < n/2
        while l < r:
            m = l + (r - l) // 2
            if m*m == num:
                return True
            elif m*m < num:
                l = m + 1
            else:  # m*m > num
                r = m - 1
        return l*l == num
