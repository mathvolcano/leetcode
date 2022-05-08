"""
44. Wildcard Matching
https://leetcode.com/problems/wildcard-matching/
"""

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        # Tabular DP
        # [1] Define state dp[i][j] as a binary value indicating whether or not
        # the ith character of s matches the jth character pattern of p.
        # [3] Then the following relation holds:
        # If p[j] == '?' then dp[i][j] = dp[i-1][j-1]
        # If s[i-1] == p[j-1] then dp[i][j] = dp[i-1][j-1]
        # If p[*] == '*' then dp[i][j] = dp[i-1][j] or dp[i][j-1]
        # [2] Initialize dp[0][0] = True, dp[i][0] is True unless p is empty
        # and dp[0][j] is True unless p[j-1] = '*'
        # Return dp[-1][-1]
        # Time & Space complexity is O(len(s) * len(p)) to create and populate dp matrix.

        ns, np = len(s), len(p)

        #Initialize DP
        dp = [[False] * (np+1) for _ in range(ns + 1)]
        dp[0][0] = True
        #Initialize dp[0][j]
        for j in range(1, np+1):
            if p[j-1] != "*":
                break
            dp[0][j] = True

        for i in range(1, ns+1):
            for j in range(1, np+1):
                #Substituting transfer equation
                if p[j-1] == s[i-1] or p[j-1] == "?":
                    dp[i][j] = dp[i-1][j-1]
                elif p[j-1] == "*":
                    dp[i][j] = dp[i-1][j] or dp[i][j-1]

        return dp[-1][-1]
