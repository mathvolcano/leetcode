"""
674. Longest Continuous Increasing Subsequence
https://leetcode.com/problems/longest-continuous-increasing-subsequence/
"""

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        n = len(nums)
        if n <= 1: return n

        best_run, curr_run = 1, 1
        for i in range(1,n):
            if nums[i] - nums[i-1] > 0:
                curr_run += 1
                best_run = max(best_run, curr_run)
            else:
                curr_run = 1
        return best_run
