"""
746. Min Cost Climbing Stairs
https://leetcode.com/problems/min-cost-climbing-stairs/
"""

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        dp = cost
        dp[:2] = cost[:2]
        if n == 2: return min(cost)

        for i in range(2,len(cost)):
            cost[i] += min(cost[i-1], cost[i-2])
        return min(cost[-1], cost[-2])
