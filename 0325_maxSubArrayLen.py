"""
325. Maximum Size Subarray Sum Equals k
https://leetcode.com/problems/maximum-size-subarray-sum-equals-k/
"""

class Solution:
    def maxSubArrayLen(self, nums: List[int], k: int) -> int:

        # [1] Compute the prefix sum
        # [2] Two sum solution
        # [2] Iterate through nums and use a hashmap that maps sum to index initialized at hm = {0: -1}
        #     a) if running sum, s, has diff, s-k in the dict then return max of result and i - hm[s-k]
        #     b) if s not in hm then add hm[s] = 9
        # O(len(nums)) time and space complexity

        hm = {0:-1}
        s, res = 0, 0
        for i, n in enumerate(nums):
            s += n
            diff = s-k
            if diff in hm:
                res = max(res, (i - hm[diff]))
            if s not in hm:
                hm[s] = i
        return res
