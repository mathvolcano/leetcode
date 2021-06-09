"""
487. Max Consecutive Ones II
https://leetcode.com/problems/max-consecutive-ones-ii/
"""

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        # Example1 – iterate through nums and track the index of the last flip
        # Track the longest run. Update the left window to the right of the last
        # flip when a new flip is encountered
        # [-->1,0,1,1,0,1,1], l = 0, r = 0, best = 1, q = -1
        # [1,-->0,1,1,0,1,1], l = 0, r = 1, best = 2, q = 1
        # [1,0,-->1,1,0,1,1], l = 0, r = 2, best = 3, q = 1
        # [1,0,1,-->1,0,1,1], l = 0, r = 3, best = 4, q = 1
        # [1,0,1,1,-->0,1,1], l = 2, r = 4, best = 4, q = 4
        # [1,0,1,1,0,-->1,1], l = 2, r = 5, best = 4, q = 4
        # [1,0,1,1,0,1,-->1], l = 2, r = 6, best = 5, q = 4

        q, res = -1, 0  # trivial queue of last indices, result
        l = 0  # left side of window
        for r in range(len(nums)):
            if nums[r] == 0:
                l = q + 1
                q = r
            res = max(res, r - l + 1)

        return res
