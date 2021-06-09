"""
494. Target Sum
https://leetcode.com/problems/target-sum/
"""


class Solution(object):
    def findTargetSumWays(self, nums, target):
        # dp with hashmap
        from collections import defaultdict
        count = defaultdict(int)
        count[0] = 1
        for n in nums:
            tmp = defaultdict(int)
            for k, v in count.items():
                tmp[k + n] += v
                tmp[k - n] += v
            count = tmp
        return count[target]

    # DFS – O(2^n) time complexity - TLE
    # def findTargetSumWays(self, nums, S):
    #     self.result = 0
    #     self.dfs(0, 0, S, nums)
    #     return self.result
    #
    # def dfs(self, idx, count, S, nums):
    #     if idx == len(nums):
    #         if count == S:
    #             self.result += 1
    #         return
    #     else:
    #         for flag in [1, -1]:
    #             self.dfs(idx+1, count+flag*nums[idx], S, nums)
    