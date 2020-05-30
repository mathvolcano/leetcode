"""
64. Minimum Path Sum
https://leetcode.com/problems/minimum-path-sum/
"""


def minPathSum(grid) -> int:
    if (len(grid) == 0) or (len(grid[0]) == 0):
        return 0
    m, n = len(grid), len(grid[0])

    # Initialize dp array
    dp = [[0]*n for x in range(m)]
    dp[0][0] = grid[0][0]
    # go through first row & column
    for c in range(1, n):
        dp[0][c] =  grid[0][c] + dp[0][c-1]
    for r in range(1, m):
        dp[r][0] = grid[r][0] + dp[r-1][0]

    # Fill remaining (m-1)x(n-1) grid
    for r in range(1,m):
        for c in range(1,n):
            dp[r][c] = min(dp[r-1][c], dp[r][c-1]) + grid[r][c]

    return dp[-1][-1]

grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
minPathSum(grid)