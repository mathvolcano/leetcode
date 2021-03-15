"""
152. Maximum Product Subarray
https://leetcode.com/problems/maximum-product-subarray/
"""

def maxProduct(nums):
    if len(nums) <= 1:
        return nums[0] if len(nums) == 1 else 0
    
    best = nums[0]
    pos = neg = nums[0]
    for n in nums[1:]:
        pos, neg = max(n, n*pos, n*neg), min(n, n*pos, n*neg)
        best = max(best, pos)
    return best
