"""
326. Power of Three
https://leetcode.com/problems/power-of-three/
"""


class Solution:
    def isPowerOfThree(self, n: int) -> bool:

        # Iterative approach
        # O(log n) time and O(1) space
        if n == 1: return True

        while n > 1:
            n /= 3
            if n == 1:
                return True
        return False

        # Recursive approach
        if n == 1: return True
        if n < 1: return False
        if n > 1: return self.isPowerOfThree(n/3)
