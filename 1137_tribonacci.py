"""
1137. N-th Tribonacci Number
https://leetcode.com/problems/n-th-tribonacci-number/
"""

class Solution:
    def tribonacci(self, n: int) -> int:
        # O(n) space, O(n) time
        trib = [0, 1, 1]
        if n <= len(trib) - 1: return trib[n]

        while n > len(trib)-1:
            trib.append(trib[-1] + trib[-2] + trib[-3])
        return trib[-1]
