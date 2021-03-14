"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        """O(len(s) + len(t))"""
        if not s: return True
        if not t or (len(s) > len(t)): return False

        n_chars = 0
        for c in t:
            if c == s[n_chars]:
                n_chars += 1
            if n_chars == len(s):
                break
        return n_chars == len(s)
