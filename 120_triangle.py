"""
120. Triangle
https://leetcode.com/problems/triangle/
"""

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        if len(triangle) == 1: return triangle[0][0]

        # DP – track the min sum paths
        r = 1  # row
        while r < len(triangle):

            # Endpoints only have 1 path
            triangle[r][0]  += triangle[r-1][0]
            triangle[r][-1] += triangle[r-1][-1]

            if len(triangle) == 2:
                return min(triangle[r])

            for i in range(1, r):
                triangle[r][i] += min(triangle[r-1][i-1], triangle[r-1][i])

            r += 1

        return min(triangle[-1])
