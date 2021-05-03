"""
1509. Minimum Difference Between Largest and Smallest Value in Three Moves
https://leetcode.com/problems/minimum-difference-between-largest-and-smallest-value-in-three-moves/
"""

class Solution:
    def minDifference(self, nums: List[int]) -> int:
        # [1]. Sort the array
        # [2]. Track the min 4 elements and the max 4 elements and compute their min difference
        # [3]. Return this min difference because replacing values for 3 of these differences
        # means that we can choose values for them in the moves to set them to 0.

        # Base case – can always change 3 numbers to the 4th, so the difference will be 0.
        if len(nums) <= 4: return 0
        nums.sort()
        mins = nums[:4]
        maxs = nums[-4:]
        return min(maxs[i] - mins[i] for i in range(4))
