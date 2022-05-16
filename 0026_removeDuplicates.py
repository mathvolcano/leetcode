"""
26. Remove Duplicates from Sorted Array
https://leetcode.com/problems/remove-duplicates-from-sorted-array/
"""
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # Two Pointer
        # [1] initialize a result index, i = 1 and a current index, c = 0
        # [2] Traverse nums while c < len(nums)
        #     [3] if nums[i-1] < nums[c], then assign nums[i] = nums[c] and increment i
        #     [4] increment c
        # Complexity: O(len(nums)) time & O(1) space

        i = 1 # index of last non-duplicate
        c = 0 # current
        while c < len(nums):
            ac = nums[c]
            if nums[i-1] < ac:
                nums[i] = ac
                i += 1
            c += 1
        return i
