"""
120. Triangle
https://leetcode.com/problems/triangle/
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]

        # DP – track the min sum paths
        # O(n^2) time, O(n^2) space (no additional space required)
        n = len(triangle)
        for i in range(1, n):
            triangle[i][0]  += triangle[i-1][0]
            triangle[i][-1] += triangle[i-1][-1]
        for i in range(2, n):
            for j in range(1, i):
                triangle[i][j] += min(triangle[i-1][j-1], triangle[i-1][j])

        return min(triangle[-1])
