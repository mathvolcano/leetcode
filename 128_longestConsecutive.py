"""
128. Longest Consecutive Sequence
https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:

        # Hash table
        # [1] create a hash set of of the numbers (drops duplicates)
        # [2] Iterate through nums, check that we start from the leftmost element of the
        # values (v -1 doesn't exit)
        # count the longest run of consecutives.
        # [3] update max result
        # Time complexity: O(n) because hash_table lookup is O(1) and we iterate through
        # nums once.
        # Space complexity is O(n) because of hash_table

        if len(nums) in (0,1): return len(nums)
        res, h = 1, set(nums)  # result, hash_set
        for i, v in enumerate(nums):
            if v - 1 not in h:
                run = 0
                while v + run in h:
                    run += 1
                if run > res:
                    res = run
        return res

        # [1] Sort the array nums
        # [2] Track the runs. Iterate through the array and check if next value matches previous +1
        # if so increment run, else reset run
        # [3] after each iteration check if run exceeds a max run result else pass
        # Example, nums = [100,4,200,1,3,2] -> [1,2,3,4,100, 200]
        # run = [1,2,3,4,1,1]
        # res = [1,2,3,4,4,4]
        # Time complexity O(n log n) space complexity O(1)

#         n = len(nums)
#         if n in (0,1): return n

#         nums.sort()
#         res, run, prev = 1, 1, nums[0]
#         for i in range(1, n):
#             print('prev, nums[i]', prev, nums[i])
#             if nums[i] == prev:
#                 continue
#             if nums[i] == prev + 1:
#                 run += 1
#                 if run > res:
#                     res = run
#                 prev = nums[i]
#             else:
#                 prev, run = nums[i], 1
#         return res
