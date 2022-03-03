"""
342. Power of Four
https://leetcode.com/problems/power-of-four/
"""


class Solution:
    def isPowerOfFour(self, num: int) -> bool:
        if num == 1: return True

        while num > 1:
            num /= 4
            if num == 1:
                return True
        return False
