"""
231. Power of Two
https://leetcode.com/problems/power-of-two/
"""


class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        if n == 1: return True

        while n > 1:
            n /= 2
            if n == 1:
                return True
        return False
