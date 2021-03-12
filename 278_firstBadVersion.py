"""
278. First Bad Version
https://leetcode.com/problems/first-bad-version/
"""

class Solution:
    def firstBadVersion(self, n):
        # Perform a binary search
        l, r = 0, n
        while (l + 1) < r:
            m = l + (r - l) // 2
            if isBadVersion(m):
                r = m
            else:
                l = m
        return r
