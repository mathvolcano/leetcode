"""
646. Maximum Length of Pair Chain
https://leetcode.com/problems/maximum-length-of-pair-chain/
"""

class Solution:
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        # Use DP and store lengths of all chains that may
        # come before a given link O(n^2)
        dp = [1] * len(pairs)
        if len(pairs) <= 1: return len(pairs)

        pairs.sort(key=lambda x: x[0])  # O(n log n)

        for i, p in enumerate(pairs):
            longest = dp[0]
            for c, v in enumerate(pairs[:i]):
                if v[1] < p[0]:
                    longest = max(longest, dp[c] + 1)
            dp[i] = longest
        return max(dp)
