"""
90. Subsets II
https://leetcode.com/problems/subsets-ii/
"""

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:

        # Recursion
        # Time – Recursion C(n) = 2*C(n-1) gives O(2^n). O(n) time within a call and O(2^n)
        # calls yields O(n * 2^n)
        # Space – O(n* 2^n) because there are O(2^n) subsets and average size O(n/2).
        # Similar strategy to 78_subsets.py, but add a sort. Sort does not impact 
        def helper(n, selected):
            if n == len(nums):
                power_set.add(tuple(selected))
                return
            helper(n+1, selected)
            new_list = list(selected) + [nums[n]]
            new_list.sort()
            helper(n+1, new_list)

        power_set = set()
        helper(0, tuple())
        power_set = list(power_set)
        return power_set