"""
665. Non-decreasing Array
https://leetcode.com/problems/non-decreasing-array/
"""

def checkPossibility(nums):
    count, n = 0, len(nums)
    if n <= 1: return True

    for i in range(1, n):
        if nums[i] < nums[i - 1]:
            count += 1
            if i == 1 or nums[i] >= nums[i - 2]:
                nums[i - 1] = nums[i]
            else:
                nums[i] = nums[i - 1]
    return count <= 1



