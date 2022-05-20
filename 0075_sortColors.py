"""
https://leetcode.com/problems/sort-colors/
75. Sort Colors
"""

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 2 Pointers
        # Goal: Move all 0s before l and all 2s after h.
        # [0] Initialize low & high pointers: Set l, h = 0, len(nums) -1, and a tracking index i= 0
        # [1] while i <= r
        # [2] Case logic
        #  a. if nums[i] == 0, swap nums[i] with nums[l] and increment l & i
        #  b. if nums[i] == 2, swap nums[i] with nums[h] and decrement h
        #  c. if nums[i] == 1, increment i
        # O(n) time and O(1) space

        n = len(nums)
        i, l, h = 0, 0, n - 1
        while i <= h:
            if nums[i] == 0:
                nums[i], nums[l] = nums[l], nums[i]
                i += 1
                l += 1
            elif nums[i] == 1:
                i += 1
            else: # nums[i] == 2
                nums[i], nums[h] = nums[h], nums[i]
                h -= 1
        return
