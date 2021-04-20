"""
1696. Jump Game VI
https://leetcode.com/problems/jump-game-vi/
"""
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # DP & Use a max heap
        n = len(nums)
        dp = [-float(inf)] * n
        dp[0] = nums[0]
        from heapq import heappop, heappush
        h = []
        heappush(h, (-nums[0], 0))
        for i in range(1, n):
            while h[0][1] < i - k:
                heappop(h)
            dp[i] = nums[i] - h[0][0]
            heappush(h, (-dp[i], i))
        return dp[-1]
