"""
153. Find Minimum in Rotated Sorted Array
https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
"""

class Solution:
    def findMin(self, nums: List[int]) -> int:
        if len(nums) == 0: return -1
        if len(nums) == 1: return nums[0]

        l, r = 0, len(nums)-1

        while l+1 < r:
            m = l + (r - l)//2
            if nums[m] < nums[r]:
                r = m
                continue
            if nums[l] < nums[m]:
                l = m
                continue
        return min(nums[l], nums[r])
