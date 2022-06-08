"""
80. Remove Duplicates from Sorted Array II
https://leetcode.com/problems/remove-duplicates-from-sorted-array-ii/
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        # 2 pointer
        # [0] Use a flag boolean to indicate the number of duplicates in nums[l:r+1]
        # [1] If nums[l] == nums[r]
        # a. if not flag then there are 0 or 1 of the same number between nums[l:r+1] and we first increment l & swap nums[l] & nums[r] & increase count
        # b. If flag then there are >= 2 duplicates and we do nothing and increase r
        # [2] If nums[l] != nums[r] then set flag to False, increment l and swap nums[l] & nums[r], increment count
        # [3] return count
        # O(n) time complexity and O(1) space
        n = len(nums)
        if not nums: return 0
        l = 0
        count = 1
        flag = False
        for r in range(1, n):
            if nums[r] == nums[l]:
                if not flag:
                    flag = True
                    l += 1
                    nums[l], nums[r] = nums[r], nums[l]
                    count += 1
            else:
                flag = False
                l += 1
                nums[l], nums[r] = nums[r], nums[l]
                count += 1
        return count
