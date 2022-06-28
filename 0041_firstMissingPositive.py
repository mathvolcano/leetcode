"""
41. First Missing Positive
https://leetcode.com/problems/first-missing-positive/
"""

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        # Cyclic Sort
        # [1] Initialize i = 0, n = len(nums) for loop: while i < n
        # [2] Set j = nums[i] - 1. If j is negative then increment i
        # [3] If 0 < nums[i] <= n and nums[i] != nums[j] then swap values of i & j.
        # [4] else increment i
        # [5] Loop through nums again and return index of entry whose value does not equal the index
        # [6] If loop did not return a value then return nums[-1] + 1
        # Complexity: time O(n) and space O(1)
        i, n = 0, len(nums)
        while i < n:
            j = nums[i] - 1
            if 0 < nums[i] <= n and nums[i] != nums[j]:
                nums[i], nums[j] = nums[j], nums[i]
            else:
                i += 1

        for i,v in enumerate(nums, start=1):
            if i != v:
                return i
        return nums[-1] + 1
