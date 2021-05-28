"""
1695. Maximum Erasure Value
https://leetcode.com/problems/maximum-erasure-value/
"""

class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:

        # 2 pointer technique
        # [0] Create a hash map to track counts of elements that appear in the
        # subarrays.
        # [1] Create variables to store best total, result and the current total, cur.
        # [2] Iterate through nums. Increment next value of r in the hash_map and the current total,
        # [3] If the count newly added number is == 1 then check if new total exceeds best
        # [4] If the count newly added number is > 1 then increase l and decrement values in hash_map until hash_map[r] == 1. At each step track current sum and check if its the best result.
        # O(n) time and space
        n = len(nums)
        if n == 1: return nums[0]

        hash_map = {}
        l, cur, res = 0, 0, 0
        for r in range(n):
            v = nums[r]
            hash_map[v] = hash_map.get(v, 0) + 1
            cur += v
            while hash_map[v] > 1:
                l_val = nums[l]
                hash_map[l_val] = hash_map.get(l_val, 0) - 1
                cur -= l_val
                l += 1
            res = max(res, cur)
        return res
