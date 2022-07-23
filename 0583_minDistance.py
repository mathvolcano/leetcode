"""
583. Delete Operation for Two Strings
https://leetcode.com/problems/delete-operation-for-two-strings/
"""

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # Dynamic Programming
        # Note that the min number of deletes of word1 and word2 equals
        # the number of deletes of word1[:-1] and word2[:-1] when word1[-1] == word2[-1]
        # but requires 1 more if they aren't equal.
        # [1] Create a matrix of size len(word1)+1, len(word2)+1
        # so that the matrix (r,c) track the min number of deletes up to word1[r-1], word2[c-1].
        # We need an extra row & column of 0s so that the lookback works.
        # [2] Iterate through the matrix r row and c col
        # Example1, the DP  atrix becomes
        # 0 1 2 3
        # 1 2 3 4
        # 2 1 2 3
        # 3 2 1 2

        m, n = len(word1)+1, len(word2)+1
        dp = [[0] * n for _ in range(m)]

        for r in range(m):
            for c in range(n):
                if r == 0 or c == 0:
                    dp[r][c] = r + c
                elif word1[r-1] == word2[c-1]:
                    dp[r][c] = dp[r-1][c-1]
                else:  # word1[r-1] != word2[c-1]
                    dp[r][c] = min(dp[r][c-1], dp[r-1][c]) + 1
        return dp[-1][-1]
