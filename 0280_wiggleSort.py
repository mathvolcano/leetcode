"""
280. Wiggle Sort
https://leetcode.com/problems/wiggle-sort/
"""

class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # 1- pointer
        # O(n) time, O(1) space
        check_is_less = 1
        for i in range(len(nums)-1):
            n1, n2 = nums[i], nums[i+1]
            swap_logic = (check_is_less and (n1 > n2)) or ((check_is_less == 0) and (n1 < n2))
            if swap_logic:
                nums[i], nums[i+1] = n2, n1
            check_is_less = 1 - check_is_less
