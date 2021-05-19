"""
453. Minimum Moves to Equal Array Elements
https://leetcode.com/problems/minimum-moves-to-equal-array-elements/
"""

class Solution:
    def minMoves(self, nums: List[int]) -> int:
        # Note that a single move adds n-1 elements to the sum
        # Let x denote the final values of the array and min the initial
        # min element in the array.
        # Then after m increments we have the equation
        # sum(nums) + (n-1) * m = x * n.
        # Further note that we want to increase the min element m times to equal x.
        # Thus, min + m = x
        # Substituting yields sum(nums) = m + min * n
        # or m = sum(nums) - min * n
        # O(n) time and O(1) space
        return sum(nums) - min(nums) * len(nums)
