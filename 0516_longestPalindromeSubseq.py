"""
516. Longest Palindromic Subsequence
https://leetcode.com/problems/longest-palindromic-subsequence/
"""

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)

        # Trivial cases
        if n <= 0: return n

        t = s[::-1]
        dp = [[0]*(n+1) for r in range(n+1)]
        for r in range(1, n+1):
            for c in range(1, n+1):
                if s[r-1] == t[c-1]:
                    dp[r][c] = dp[r-1][c-1] + 1
                else:
                    dp[r][c] = max(dp[r][c-1], dp[r-1][c])
        return dp[-1][-1]

        # Idea: reverse s and perform the same procedure as longest common subsequences for
        # 2 texts using dynamic programming.
        # 2 pointer solution, 1 for s and the other for s[::-1]
        # DP – count the number of characters of common text2 up to pointer i in text1
        # Store results in a matrix
        # If the next character of both s and

        # Add an extra row and column for 0s for DP


        # r (row) iterates over s and represents s[:r]
        # c (col) iterates over t and represents t[:c]
        # dp[r][c] == longest subsequences in s[:r] and t[:c]
        # Then if s[r+1] = t[c+1] we have the relation
        # dp[r][c] = dp[r-1][c-1] + 1
        # Else then the longest subsequence is unchanged from either s[:r-1] and t[:c] or s[:r] and t[:c-1]
        # so dp[r][c] = max(dp[r-1][c], dp[r][c-1])

#         # Brute force - O(2^n) time and space to get and store all subsequences
#         t = ''.join(reversed(s))

#         def subsequences(s):
#             if len(s) == 0: return ['']
#             if len(s) == 1: return [s[0]]
#             temp = subsequences(s[:-1])
#             return temp + [t + s[-1] for t in temp]

#         subsequence_lengs = [len(ss)
#                              for ss in subsequences(s)
#                              for ts in subsequences(t)
#                              if ss == ts]
#         return max(subsequence_pairs)
