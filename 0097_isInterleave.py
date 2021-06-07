"""
97. Interleaving String
https://leetcode.com/problems/interleaving-string/
"""

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        # DP
        # Note if s1[:i] and s2[:j] are validedly interleaved into s3[:i+j]
        # then s3[:i+j+1] is also valid if s3[i+j+1] equals either
        # s1[i] or s2[j].
        # [1] Form a matrix of boolean flags whose (i+1, j+1) entry
        # indicates whether or not the s3[:i+j] is a valid interleave of s1[:i]
        # and s2[:j].
        # [2] Instantiate the matrix with the top left square to 1.
        # [3] Update the first row and column by iterating solely through the row or column
        # [4] Check if either the next letter of s3 is from either s1 or s2 and the the previous row or column for s1 or s2 is also true.
        # Time and space complexity: O(n^2)
        n1, n2, n3 = len(s1), len(s2), len(s3)
        if n1 + n2 != n3: return False

        dp = [[0]* (n2+1)] * (n1+1)
        for i in range(n1+1):
            for j in range(n2+1):
                if i == 0 and j == 0:
                    dp[i][j] = 1
                elif i == 0:
                    dp[i][j] = dp[i][j-1] and (s2[j-1] == s3[j-1])
                elif j == 0:
                    dp[i][j] = dp[i-1][j] and s1[i-1] == s3[i-1]
                else:
                    dp[i][j] = ((dp[i][j-1] and s2[j-1] == s3[i+j-1]) or
                                (dp[i-1][j] and s1[i-1] == s3[i+j-1])
                                )
        return dp[-1][-1]
