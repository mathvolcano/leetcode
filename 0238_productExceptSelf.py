"""
238. Product of Array Except Self
https://leetcode.com/problems/product-of-array-except-self/
"""

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        # Hash map – O(1) space except for result
        # [0] Initialize a result array res = [1] + [0] * (n-1)
        # [1] Left product: Get product of elements to the left of each i: for eac i in range(1,n): res[i] = nums[i-1] * res[i-1]
        # [2] right product: for i in reversed(range(n)): have a product of all elemnts of right
        # p and set res[i] *= p and multiply p by nums[i]
        # O(n) time and O(1) space except for result
        n = len(nums)
        res = [1] + [0] * (n-1)
        for i in range(1, n):
            res[i] = nums[i-1] * res[i-1]
        p = 1
        for i in reversed(range(n)):
            res[i] *= p
            p *= nums[i]
        return res

        # Hash map
        # [1] Construct 2 arrays that are the products of all elements to the left (and right resp)
        # of the element.
        # [2] for each i multiply these the ith entry of l and r to get the result
        # O(n) time and O(n) space
        n = len(nums)
        l, r = [0]*n, [0] *n
        l[0] = 1
        p = 1
        for i in range(1, n):
            p *= nums[i-1]
            l[i] = p
        p = 1
        for i in range(n-1, 0, -1):
            r[i] = p
            p *= nums[i]
        r[0] = p
        return [l[i] * r[i] for i in range(n)]
