"""
1099. Two Sum Less Than K
https://leetcode.com/problems/two-sum-less-than-k/
"""

class Solution:
    def twoSumLessThanK(self, nums: List[int], k: int) -> int:
        nums.sort()
        nums = [n for n in nums if n < k]
        if len(nums) <= 1: return -1
        max_sum = 0
        l, r = 0, len(nums) - 1
        while l < r:
            val = nums[l] + nums[r]
            if val < k:
                max_sum = max(max_sum, val)
                l += 1
            else:  # val >= k
                r -= 1
        return max_sum
