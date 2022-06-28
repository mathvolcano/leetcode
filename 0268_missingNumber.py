"""
268. Missing Number
https://leetcode.com/problems/missing-number/
"""

class Solution:
    def missingNumber(self, nums: List[int]) -> int:

        # Cyclic sort
        # [1] extend nums with new element -1
        # [2] loop i through nums
        # [3] if nums[i] == -1 or i != nums[i], then swap nums[i] and nums[nums[i]], else incrmeent i
        # [4] loop through nums again and return the index of the -1
        # O(n) time and O(1) space
        nums.append(-1)
        i, n = 0, len(nums)
        while i < n:
            j = nums[i]
            if j == -1 or i == j:
                i += 1
            else:
                nums[i], nums[j] = nums[j], nums[i]

        for i, v in enumerate(nums):
            if v == -1:
                return i

        # Array copy
        # [1] Create an array of all integers in order, all_ints
        # [2] For n in nums set, set all_ints[n] = -1
        # [3] Loop through all_ints and return the first element that is not -1
        # O(n) time and O(n) space
#         all_ints = list(range(len(nums)+1))

#         for n in nums:
#             all_ints[n] = -1

#         for n in all_ints:
#             if n >= 0:
#                 return n