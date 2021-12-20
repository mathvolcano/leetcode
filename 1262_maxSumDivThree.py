"""
1262. Greatest Sum Divisible by Three
https://leetcode.com/problems/greatest-sum-divisible-by-three/
"""

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:

        # DP - Tabulation
        # [1] Initialize an array, dp = [0,0,0]
        # [2] Make a copy of dp
        # [3] 2 loops : Iterate through nums to get it's values, v,
        #     iterate through a copy of dp, p, and add v to its values % 3
        # [4] set new index dp[(p+v)%3] to be max of dp[(p+v)%3] and p + v
        # Return dp[0]
        # O(1) space complexity, O(n) time complexity

        # Example 1
        # nums = [3,6,5,1,8]
        # dp = [0,0,0]
        # p = 0
        # dp = [3,0,0]
        # p = 1
        # dp = [9,0,0]
        # p = 2
        # dp = [9,0,14]
        # p = 3
        # dp = [15,10,14]
        # p = 4
        # dp = [18,22,23]

        dp = [0,0,0]
        for v in nums:
            for p in dp.copy():
                p2 = (p+v) % 3
                dp[p2] = max(dp[p2], p + v)
        return dp[0]
