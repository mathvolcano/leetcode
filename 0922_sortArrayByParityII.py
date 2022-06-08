"""
922. Sort Array By Parity II
https://leetcode.com/problems/sort-array-by-parity-ii/
"""
class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        # 2 pointer
        # [1] Set initial pointers e, o = 0,1
        # [2] while e & o < len(nums)
        # [3] Get the first even index where nums[e] % 2 != 0, increment by 2 as needed
        # [3] Get the first  odd index where nums[o] % 2 != 1, increment by 2 as needed
        # [5] swap indices
        # O(n) time and O(1) space
        n = len(nums)
        e, o = 0, 1
        while e < n and o < n:
            if nums[e] % 2 == 0:
                e += 2
            elif nums[o] % 2 == 1:
                o += 2
            else:
                nums[e], nums[o] = nums[o], nums[e]
                e += 2
                o += 2
        return nums
