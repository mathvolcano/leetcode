"""
259. 3Sum Smaller
https://leetcode.com/problems/3sum-smaller/
"""

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        # Sort with sliding window
        # [0] initialize res = 0
        # [1] Sort arr
        # [2] iterate i through range(n-2)
        # [3] Define a helper sliding window function, search_pair
        #  a. Set l, r = i+1, n-1
        #  b. while l < r, check the sum < target, if so increment res by r-l (all these indices' values add to < target)
        # and increment l  else decrement r
        # O(n^2) time and O(1) space if the sort is done in-place. Else we'll need O(n) additional space for sort.
        res, n = 0, len(nums)
        nums.sort()
        for i in range(n-2):
            d = target - nums[i]
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] < d:
                    res += r - l
                    l += 1
                else:
                    r -= 1
        return res

        # Brute Force - O(n^3) time and O(1) space
#         n = len(nums)
#         if len(nums) < 3: return 0

#         res = 0
#         for i in range(n):
#             for j in range(i+1, n):
#                 for k in range(j+1, n):
#                     if nums[i] + nums[j] + nums[k] < target:
#                         res += 1
#         return res
