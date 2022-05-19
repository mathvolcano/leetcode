"""
713. Subarray Product Less Than K
https://leetcode.com/problems/subarray-product-less-than-k/
"""
class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:

        # Note For each j, let opt(j) be the smallest i so that nums[i] * nums[i+1] * ... * nums[j] is less than k. opt is an increasing function.
        #
        # [0] Initialize  product, prod = 1, result, res = 0, left pointer, l = 0, and n = len(arr)
        # [1] Iterate right pointer, r, through range(n):
        # [2] Divide prod by leftmost elements and increment l until prod is < k
        # [3] Once prod < k, increment result by r - l + 1, the number of subarrays of nums[l:r]
        #.    because the product of all elements form l to r < target, so are all subarrays
        # O(n) time complexity for each loo
        # Space is O(1) space to variables.
        res, n = 0, len(nums)
        l, prod = 0, 1
        for r in range(n):
            prod *= nums[r]
            while (prod >= k and l <= r):
                prod /= nums[l]
                l += 1
            res += r - l +1
        return res
