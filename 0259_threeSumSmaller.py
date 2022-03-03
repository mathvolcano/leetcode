"""
259. 3Sum Smaller
https://leetcode.com/problems/3sum-smaller/
"""

class Solution:
    def threeSumSmaller(self, nums: List[int], target: int) -> int:

        # 2-pointer solution
        # [1] sort nums
        # Ex target = 2, nums = [-1,2,1,-4, 5, -2] -> [-3, -2, -1, 1, 2, 5]
        # [2] For each index perform twoSumLessThanK –  perform a 2-pointer search to count the number of sums of nums[j] + nums[k] < target - nums[i]
        # [2] set left l and right r pointers to the endpoints
        # [3] compute sum of the three values nums[i] + nums[l] + nums[r]
        # if the sum < target then add (r-l) to result because w can set r to be all numbers between r & l.
        # [4] increase l if sum is < target, otherwise decrease r if sum is >= target
        # O(n^2) time and O(1) space
        n = len(nums)
        if n < 3: return 0

        nums.sort()
        res = 0
        for i in range(n-2):
            diff = target - nums[i]
            l, r = i + 1, n - 1
            while l < r:
                if nums[l] + nums[r] < diff:
                    res += (r - l)
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
