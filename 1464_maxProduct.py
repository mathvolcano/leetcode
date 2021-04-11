"""
1464. Maximum Product of Two Elements in an Array
https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
"""

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        # Sort then multiply.  O(n log n) time, O(n) space
        nums.sort()
        return max((nums[-1] - 1) * (nums[-2] - 1),
                   (nums[0] - 1) * (nums[1] - 1)  # Need for negative nums
                   )

        # # Pythonic, Brute force O(n^2)
        # return max((nums[i] - 1) * (nums[j] - 1)
        #            for i in range(len(nums))
        #            for j in range(len(nums))
        #            if i != j)
