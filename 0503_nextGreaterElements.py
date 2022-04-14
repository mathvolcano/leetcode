"""
503. Next Greater Element II
https://leetcode.com/problems/next-greater-element-ii/
"""

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:

        # Monotone stack with Brute Force
        # [1] concat nums with itself, nums2 = nums + nums
        # [2] Use a decreasing monotone stack, s, to get the next largest element
        #. for each element, m, in nums *2:
        #. b. if m is larger than the last value in the stack (if it exists) then pop last index and assign the res[i] = m
        #  c. else: append tuple i to the stack.
        # O(n) time complexity
        # O(n) space complexity
        n = len(nums)
        res = [-1] * n
        s = []
        for i, m in enumerate(nums*2):
            while s and (m > nums[s[-1]]):
                res[s.pop()] = m
            if i < n:
                s.append(i)
        return res
