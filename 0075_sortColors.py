"""
https://leetcode.com/problems/sort-colors/
75. Sort Colors
"""

def sortColors(nums):
    if len(nums) <= 1: return nums
    
    # smaller, middle, larger division mark the points that we know are 0, 1, 2
    s, m, l = 0, 0, len(nums)
    while m < l:
        if nums[m] == 0:
            nums[s], nums[m] = nums[m], nums[s]
            s += 1
            m += 1
        elif nums[m] == 1:
            m += 1
        else:
            nums[l-1], nums[m] = nums[m], nums[l-1]
            l -= 1


nums = [2,0,2,1,1,0]
sortColors(nums)
nums # [0,0,1,1,2,2]

nums = [2,0,1]
sortColors(nums)