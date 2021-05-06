"""
1590. Make Sum Divisible by P
https://leetcode.com/problems/make-sum-divisible-by-p/
"""

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:

        # [1] Use a map to keep track of the rightmost index for every prefix sum % p.
        # [2] The result is the smallest number such that the remaining subarry equals the complement

        # Base case
        r = sum(nums) % p  # remainder
        if r == 0: return 0

        hash_table = {0: -1}
        res = len(nums)
        s = 0  # sum
        for i, n in enumerate(nums):
            s = (s + n) % p
            t = (s + p - r) % p  # target
            if t in hash_table:
                res = min(res, i - hash_table[t])
            hash_table[s] = i
        return -1 if res == len(nums) else res
