"""
462. Minimum Moves to Equal Array Elements II
https://leetcode.com/problems/minimum-moves-to-equal-array-elements-ii/
"""
class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        # [1] Sort the array
        # [2] get the midpoint
        # [3] calculate the abs diff from each num to the midpoint
        m = sorted(nums) [len(nums) // 2]
        return sum(abs(i - m) for i in nums)
