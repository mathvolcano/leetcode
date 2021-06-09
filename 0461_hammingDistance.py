"""
461. Hamming Distance
https://leetcode.com/problems/hamming-distance/
"""

class Solution:
    def hammingDistance(self, x: int, y: int) -> int:
        res = 0
        while x or y:
            res += 1 if (x & 1) != (y & 1) else 0
            x >>= 1
            y >>= 1
        return res