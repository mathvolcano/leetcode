"""
283. Move Zeroes
https://leetcode.com/problems/move-zeroes/
"""


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if len(nums) <= 1: return nums

        n = len(nums)

        # Move the nonzero elements to the front
        n_nonzeros = 0
        for i in range(n):
            if nums[i] != 0:
                nums[n_nonzeros] = nums[i]
                n_nonzeros += 1

        # Assign tail elements to the zero
        n_zeros = n_nonzeros
        while n_zeros < n:
            nums[n_zeros] = 0
            n_zeros += 1
