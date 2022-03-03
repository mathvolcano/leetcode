"""
693. Binary Number with Alternating Bits
https://leetcode.com/problems/binary-number-with-alternating-bits/
"""

class Solution:
    def hasAlternatingBits(self, n: int) -> bool:
        # Iterate through n and check if current bit ever equals the previous bit
        # Time complexity O(log n), the number of bits. Note that the number of bits < 32,
        # so we can take this to be O(1)
        # Space complexity is O(1)
        cur, pre = 0, -1
        while n != 0:
            cur = n & 1
            if cur == pre: return False
            n = n >> 1
            pre = cur
        return True
