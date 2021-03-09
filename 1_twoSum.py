"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        n_to_index = {}
        for i, n in enumerate(nums):
            if target - n in n_to_index:
                return [i, n_to_index[target-n]]
            else:
                n_to_index[n] = i
        return 