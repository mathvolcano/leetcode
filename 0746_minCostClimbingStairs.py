"""
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:

        # DP
        # Note the cost of reaching step i is the min of the cost of
        # reaching step i-1 or step i-2.
        # Time complexity O(n), space complexity O(1) additional space
        for i in range(2, len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
