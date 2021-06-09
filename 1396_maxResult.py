"""
1696. Jump Game VI
https://leetcode.com/problems/jump-game-vi/
"""
class Solution:
    def maxResult(self, nums: List[int], k: int) -> int:
        # DP & Use a max heap
        # [1] Create an array to track costs to jump to the steps
        # [2] Create a heap to track the costs of the steps. Initialize with cost and step of 0.
        # [3a] Iterate through the heap pop all elements that are less than i - k
        # [3b] Update next step as dp[i] = nums[i] - h[0][0]
        # [3] Push to heap the next step
        # [4] Return last element of the array.
        # Space complexity: O(n)
        # Time complexity O(n log n) for heap
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
