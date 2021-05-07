"""
1446. Consecutive Characters
https://leetcode.com/problems/consecutive-characters/
"""

class Solution:
    def maxPower(self, s: str) -> int:
        # [1] Track left l and right r sides of the unique character runs in s
        # [2] iterate through s. if the right window r is a new char then update l to it
        # and reset run
        # [3] else increment r.

        # Trivial Case
        n = len(s)
        if n <= 1: return n

        l, res = 0, 1
        for r in range(1, n):
            if s[l] != s[r]:
                l = r
            res = max(res, r - l + 1)
        return res
