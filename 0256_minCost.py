"""
256. Paint House
https://leetcode.com/problems/paint-house/
"""

class Solution:
    def minCost(self, costs: List[List[int]]) -> int:
        # DP - Update cost array with the total min cost by iterating through the housts
        # [1] Leave the 1st row alone. Return if n == 1
        # [2] For each row and each index in the row iterate through the previous row and search for the cheapest total cost
        # from the previous row that is not the same index as the current row and sum it.
        # This gives use the dp relation costs[i][j] = costs[i][j] + min([c for k, c in enumerate(costs[i-1]) if k != j])
        # Example: costs = [[17,2,17],[16,16,5],[14,3,19]]
        # dp = []
        # Iteration 1: costs = [[17,2,17],[16,16,5],[14,3,19]]
        # Iteration 2: costs = [[17,2,17],[18,33,7],[14,3,19]]
        # Iteration 3: costs = [[17,2,17],[18,33,7],[21,10,37]]
        # Time complexity: O(n), additional space complexity O(1)

        n = len(costs)
        if n == 1: return min(costs[0])

        for i in range(1, n):
            for j in range(3):
                costs[i][j] = costs[i][j] + min([c for k, c in enumerate(costs[i-1]) if k != j])
        return min(costs[-1])
