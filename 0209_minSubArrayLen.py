"""
209. Minimum Size Subarray Sum
https://leetcode.com/problems/minimum-size-subarray-sum/
"""

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:

        # Sliding window, 2 pointers
        # [1] initialize 2 points, l & r at 0
        # [2] Initialize result variable to inf and running sum to 0
        # [3] loop through the array, and increment sum
        # [4] while sum exceeds target,
        #     a) update res against min of itself and new window length
        #     b) subtract nums[l] from sums, S
        #     c) increment l
        # [4] update result res if finite
        # O(n) time complexity
        # O(1) space complexity
        n = len(nums)
        if n == 0: return 0
        res, l, S = float('inf'), 0, 0
        for r in range(n):
            S += nums[r]
            while S >= target:
                res = min(res, r-l+1)
                S -= nums[l]
                l += 1
        return res if res < float('inf') else 0
