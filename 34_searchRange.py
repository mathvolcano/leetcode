"""
34. Find First and Last Position of Element in Sorted Array
https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
"""



def searchRange(nums, target):
    if (not nums) or (target > nums[len(nums)-1]) or (target < nums[0]):
        return [-1, -1]

    # Perform a binary search
    l = 0
    r = len(nums) - 1
    count = 0
    while (nums[l] < target) or (nums[r] > target):
        mid = int((r + l) / 2)
        val = nums[mid]
        if val < target:
            l = mid + 1
        elif val > target:
            r = mid - 1

        if nums[l] < target:
            l += 1
        if nums[r] > target:
            r -= 1
        if l >= r:
            break
    return [l, r] if nums[l] == target else [-1, -1]
