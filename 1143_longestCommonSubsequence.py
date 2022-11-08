fe"""
1143. Longest Common Subsequence
https://leetcode.com/problems/longest-common-subsequence/
"""

class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:

        # DP - space optimized bottom-up
        # [0] Make text1 the shorter string
        # [1] Create arrays of length n1 = len(text1) + 1 to track previous row & current row, starting with all 0s representing longest subsequence up to text1[r] and text2[c] in reverse
        # [1] iterate: for r in reversed rows for c in reversed columns
        # [2] if text1[r-1] == text2[c-1] then increment cur[r] array by 1 + prev(r+1)
        # [3] else, update it to be the max of cur[r] = max(cur[r+1], pre[r-1])
        # return pre[0]
        # Complexity: n1 = len(text1) and n2 = len(text2)
        # Time: O(n1* n2) to traverse entire matrix
        # Space: O(min(n1, n2)) to store matrix
        if len(text2) < len(text1):
            text1, text2 = text2, text1
        n1, n2 = len(text1), len(text2)

        # The previous and current column starts with all 0's and like
        # before is 1 more than the length of the first word.
        pre = [0] * (n1 + 1)
        cur = [0] * (n1 + 1)
        for c in reversed(range(n2)):
            for r in reversed(range(n1)):
                if text2[c] == text1[r]:
                    cur[r] = 1 + pre[r + 1]
                else:
                    cur[r] = max(pre[r], cur[r + 1])
            # The current column becomes the previous one, and vice versa.
            pre, cur = cur, pre
        return pre[0]

        # DP
        # [0] Create a n1 xn2 matrix to store results
        # [1] iterate: for r in rows for c in columns
        # [2] if text1[r-1] == text2[c-1] then increment dp matrix from r-1xc-1 entry
        # [3] else, update it to be the max of r x c-1 or r-1 x c entry
        # retu dp[-1][-1]
        # Complexity: n1 = len(text1) and n2 = len(text2)
        # Time: O(n1* n2) to traverse entire matrix
        # Space: O(n1*n2) to store matrix
#         n1, n2 = len(text1), len(text2)
#         dp = [[0]*(n2+1) for r in range(n1+1)]

#         for r in range(1, n1+1):
#             for c in range(1, n2+1):
#                 if text1[r-1] == text2[c-1]:
#                     dp[r][c] = dp[r-1][c-1] + 1
#                 else:
#                     dp[r][c] = max(dp[r][c-1], dp[r-1][c])

#         return dp[-1][-1]
