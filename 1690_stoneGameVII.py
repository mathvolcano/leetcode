"""
1690. Stone Game VII
https://leetcode.com/problems/stone-game-vii/
"""

class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:

        # Top-Down DP
        # [0] Track the best scores in a (n+1)*n for i the left-most index and j the right most index of the stones array removed. Need an extra row for DP sum
        # [1] Compute the prefix sums to get the stone totals
        # [2] Iterate through the matrix starting from i is row n-1 and working up
        # and starting from column j = i +1 and working right
        # [3] get the best score for dp[i][j] as the max of total less removning the head and tail of the stones
        # Iterate and return dp[0][-1]
        # O(n^2) time and space complexity

        # n = len(stones)
        # dp = [[0] * n for _ in range(n)]
        # # Get the prefix sums
        # prefix = stones[:] + [0]
        # for i in range(n):
        #     prefix[i] += prefix[i-1]
        #
        # # DP
        # for i in reversed(range(n)):
        #     for j in range(i + 1, n):
        #         removeHead = prefix[j] - prefix[i]
        #         removeTail = prefix[j-1] - prefix[i-1]
        #         dp[i][j] = max(removeHead - dp[i+1][j], removeTail - dp[i][j-1])
        # return dp[0][-1]

        # Improvement - only need to track the current and the previous rows of the dp tracking.
        # This reduces space from O(n^2) to O(n)
        # TODO: add example

        n = len(stones)
        dp_curr, dp_last = [0] * n, [0] * n

        # Get the prefix sums
        prefix = stones[:] + [0]
        for i in range(n):
            prefix[i] += prefix[i-1]

        # DP
        for i in reversed(range(n)):
            dp_last, dp_curr = dp_curr, dp_last
            for j in range(i + 1, n):
                removeHead = prefix[j] - prefix[i]
                removeTail = prefix[j-1] - prefix[i-1]
                dp_curr[j] = max(removeHead - dp_last[j], removeTail - dp_curr[j])
        return dp_curr[-1]
