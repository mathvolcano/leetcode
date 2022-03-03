"""
154. Find Minimum in Rotated Sorted Array II
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array-ii/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:

        # Binary search
        # [1] Get the middle element and compare against the right endpoint
        # [2] if the right endpoint is strictly bigger than the mid then search
        # for min in this range
        # [3] else set right to mid because we also have to check if the mid value
        # itself is the min.
        # O(log n) time complexity, O(1) space
        l, r = 0, len(nums) - 1
        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                l = m + 1
            elif nums[m] < nums[r]:
                r = m
            else:
                r -= 1
        return nums[l]

        # Pythonic O(n) time and O(1) space
        # return min(nums)
