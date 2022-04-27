"""
53. Maximum Subarray
https://leetcode.com/problems/maximum-subarray/
"""
class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # TODO: divide & conquer

        # Kadane's Algorithm (DP)
        # [0] Initialize variables cur for the current subarray sum and res to track
        # the largest subarray sum. Set both to be nums[0]
        # [1] Iterate n through nums[1:]
        #  a. Set cur to the max of cur + n or n (if n > cur then discard cur)
        #  b. Update res to be the max of res and cur
        # O(n) time and O(1) space
        cur = res = nums[0]  # [0]
        for n in nums[1:]:
            cur = max(n, cur + n)  # a
            res = max(res, cur)    # b
        return res

        # Brute Force
        # O(n^2) time and O(1) space
        # res = -float('inf')
        # for i in range(len(nums)):
        #     for j in range(i+1, len(nums)):
        #         s = sum(nums[i:j])
        #         res = max(res, s)
        # return res
