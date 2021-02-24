"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""


def searchInsert(nums, target):
    n = len(nums)
    for i in range(n):
        val = nums[i]
        if val < target:
            pass
        elif val >= target:
            return i
    return n
