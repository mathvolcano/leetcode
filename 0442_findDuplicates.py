"""
442. Find All Duplicates in an Array
https://leetcode.com/problems/find-all-duplicates-in-an-array/
"""

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:

        # Cyclic Sort
        # [1] initialize coutner i = 0 and loop while i < len(nums):
        # [2] set j = nums[i]-1. if j is negative increment i
        # [3] else if nums[j] > 0 then swap & assign nums[i], nums[j] = nums[j], -1
        # [4] else if nums[j] == -1 then swap & decrement nums[i], nums[j] = nums[j], -2
        # return list of indices of nums where the value is -2
        # O(n) time and O(1) space for variables, up to O(n) space worst case to build result

        i, n = 0, len(nums)
        while i < n:
            j = nums[i]-1
            if j < 0:
                i += 1
            elif nums[j] == -1:
                nums[j] = -2
                nums[i] = -float('inf')
                i += 1
            else:
                nums[i], nums[j] = nums[j], -1
        return [i+1 for i,v in enumerate(nums) if v == -2]