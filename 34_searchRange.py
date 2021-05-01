"""
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""



def searchRange(nums, target):
    # Binary searches to find leftmost and rightmost occurences
    # O(log n) time O(1) space
    l, r = 0, len(nums) - 1
    l_most = -1
    while l <= r:
        m = (r + l) // 2
        if nums[m] >= target:
            r = m - 1
        else:
            l = m + 1
        if nums[m] == target:
            l_most = m

    l, r = 0, len(nums) - 1
    r_most = -1
    while l <= r:
        m = (r + l) // 2
        if nums[m] <= target:
            l = m + 1
        else:
            r = m - 1
        if nums[m] == target:
            r_most = m
    return [l_most, r_most]
