"""
392. Is Subsequence
https://leetcode.com/problems/is-subsequence/
"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        #2 pointers
        # Complexity: n = len(s) and m = len(t)
        # Time: O(n+m) worst case when we must traverse entirety of both strings
        # Space: O(1) for pointers
        if not s: return True
        if not t or (len(s) > len(t)): return False

        p = 0
        for c in t:
            if c == s[p]:
                p += 1
            if p == len(s):
                break
        return p == len(s)
