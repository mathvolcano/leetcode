"""
696. Count Binary Substrings
https://leetcode.com/problems/count-binary-substrings/
"""
class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        if len(s) <= 1: return 0

        # Count the number of previously occurring characters that are the same
        # Count the current number of characters that are the same
        # Once a character differs from the previous add the smaller of the runs
        res, prev, cur = 0, 0, 1
        for i in range(1, len(s)):
            if s[i] != s[i-1]:
                res += min(prev, cur)
                prev, cur = cur, 1
            else:
                cur += 1
        return res + min(prev, cur)
