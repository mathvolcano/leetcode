"""
1. Two Sum
https://leetcode.com/problems/two-sum/
"""

class Solution:
    def twoSum(self, nums, target):
        # Use a hash table
        # For each num in nums stores num: index.
        # If following num in nums are in the values then return the indicies of the key & value
        # O(n) time and space (worst case)
        h = {}
        for i,v in enumerate(nums):
            c = target - v
            if c in h:
                return [i, h[c]]
            h[v] = i
