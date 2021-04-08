"""
611. Valid Triangle Number
https://leetcode.com/problems/valid-triangle-number/
"""

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        n = len(nums)
        if n < 3 : return 0

        # Sort array, use 3 pointers. When longest side is longer than shorter 2 sides then increase shortest side
        # Double for loop => O(n^2) time complexity, O(1) space complexity.
        res = 0
        nums.sort()
        for k in range(n-1, 1, -1):
            i, j = 0, k-1
            while i < j:
                if nums[i] + nums[j] > nums[k]:
                    res += j - i  # increasing i up to j will always satisfy the constraint
                    j -= 1  # to break
                else:
                    i += 1  # to satisfy
        return res

        # # Brute force – O(n!)
        # from itertools import combinations
        # triplets = list(combinations(nums, 3))
        # res = 0
        # for t in triplets:
        #     s1 = t[0] + t[1] > t[2]
        #     s2 = t[0] + t[2] > t[1]
        #     s3 = t[2] + t[0] > t[1]
        #     if s1 and s2:
        #         res += 1
        # return res