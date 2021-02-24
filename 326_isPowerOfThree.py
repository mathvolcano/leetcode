"""
326. Power of Three
https://leetcode.com/problems/power-of-three/
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n == 1: return True

        while n > 1:
            n /= 3
            if n == 1:
                return True
        return False
