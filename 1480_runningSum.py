"""
1480. Running Sum of 1d Array
https://leetcode.com/problems/running-sum-of-1d-array/
"""

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        if len(nums) <= 1: return nums

        # Keep a running sum and replace values of nums in place with the sum
        # O(n) time complexity and O(1) additional space complexity
        tot = 0
        for i, v in enumerate(nums):
            tot += v
            nums[i] = tot
        return nums

        # Pythonic – Brute Force
        # return [sum(nums[:i+1]) for i in range(len(nums))]