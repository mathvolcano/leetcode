"""
1150. Check If a Number Is Majority Element in a Sorted Array
https://leetcode.com/problems/check-if-a-number-is-majority-element-in-a-sorted-array/description/
"""

class Solution:
    def isMajorityElement(self, nums: List[int], target: int) -> bool:
        # Binary search - Built
        # Same as below but we build the binary search helper
        # Complexity: O(log n) time and O(1) space
        def bs(a, t):  # array, target, get the right-most endpoint if it exists
            l, r = 0, len(a)
            while l < r:
                m = (l + r) // 2
                if a[m] < t:
                    l = m + 1
                else:
                    r = m
            return l

        l = bs(nums, target)
        r = bs(nums, target + 1)
        return r - l > len(nums) // 2

        # Binary search - Pythonic
        # Idea: binary search to find the first and last occurrences of target (l, r)
        # return true if r - l > n//2, where n = len(nums)
        # Complexity: O(log n) time and O(1) space
        # l = bisect.bisect_left(nums, target)
        # r = bisect.bisect_right(nums, target)
        # return r - l > len(nums) // 2

        # Brute force – does not use sorted
        # [1] Count the number of occurrences of target in nums
        # [2] return true if > len(nums) // 2
        # Complexity: O(len(nums)) time and O(1) space
        # return nums.count(target) > len(nums) // 2
