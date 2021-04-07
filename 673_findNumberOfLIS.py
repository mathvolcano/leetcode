"""
673. Number of Longest Increasing Subsequence
https://leetcode.com/problems/number-of-longest-increasing-subsequence/
"""

class Solution:
    def findNumberOfLIS(self, nums: List[int]) -> int:
        # DP. Encode in an array the length of the longest subsequence
        # And encode the counts of subsequences that end at nums[i]
        n = len(nums)
        if n <= 1: return n
        lengths = [1] * n  #lengths[i] = longest ending in nums[i]
        counts  = [1] * n  #count[i] = number of longest ending in nums[i]

        for i, num in enumerate(nums):
            for j in range(i):
                if nums[j] < nums[i]:
                    if lengths[j] >= lengths[i]:
                        lengths[i] = max(lengths[i],lengths[j]+1)
                        counts[i] = counts[j]
                    elif lengths[i] == lengths[j] + 1:
                        counts[i] += counts[j]
        longest = max(lengths)
        return sum(c for j, c in enumerate(counts) if lengths[j] == longest)
