"""
324. Wiggle Sort II
https://leetcode.com/problems/wiggle-sort-ii/
"""
class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        # Sort solution - Not optimal
        # [1] Sort array
        # [2] Create copies of the smaller & larger entries
        # [3] assign all odd index values of nums the small values in descending order
        # [4] assign all odd index values of nums the larger values in descending order
        # We need to reverse the order because of equality ties
        # Time: O(n log n) for sort, Space O(n) space

        # Ex: [1,3,2,2,3,1]
        # [1]: [1,1,2,2,3,3]
        # [2]: l = [1,1,2], r= [2,3,3]
        # [3 & 4]: l[::-1] = [2,1,1], r[::-1] = [3,3,2] nums = [2,3,1,3,1,2]
        nums.sort()
        m = (len(nums) + 1) // 2
        l, r = nums[:m], nums[m:]
        nums[0::2] = l[::-1]
        nums[1::2] = r[::-1]
