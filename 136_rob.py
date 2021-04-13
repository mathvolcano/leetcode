"""
198. House Robber
https://leetcode.com/problems/house-robber/
"""

class Solution:
    def rob(self, nums: List[int]) -> int:
        dp = nums  # DP

        # Trivial
        if len(nums) == 1: return nums[0]
        dp[1] = max(nums[:2])
        if len(nums) == 2: return dp[1]

        for i, n in enumerate(nums[2:], start=2):
            dp[i] = max(nums[i] + dp[i-2], dp[i-1])
        return max(dp[-1], dp[-2])