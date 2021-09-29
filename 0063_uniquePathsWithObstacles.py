"""
63. Unique Paths II
https://leetcode.com/problems/unique-paths-ii/
"""

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:

        # DP. Needs O(n*m) space and O(n + m + n*m) = O(nm) time.
        m, n = len(obstacleGrid), len(obstacleGrid[0])

        # Trivial cases
        if obstacleGrid[0][0] == 1 or obstacleGrid[-1][-1] == 1:
            return 0
        if m <= 1 or n <= 1:
            return 0 if obstacleGrid[m-1][n-1] == 1 else 1

        # DP. Init first row and column up to a an obstacle with a single path
        dp = [[0] * n for _ in range(m)]
        for i in range(m):
            if obstacleGrid[i][0] == 1:
                dp[i][0] = 0
                break
            dp[i][0] = 1
        for j in range(n):
            if obstacleGrid[0][j] == 1:
                dp[0][j] == 0
                break
            dp[0][j] = 1

        # Update the dp as the sum of up and left dp entries
        for i in range(1,m):
            for j in range(1,n):
                if obstacleGrid[i][j] == 1:
                    dp[i][j] = 0
                else:
                    dp[i][j] = dp[i-1][j] + dp[i][j-1]
        return dp[m-1][n-1]


        # PErform a BFS, O(n*m) time, O(n*m) space (O(1) additional space needed)
        # if dp[-1][-1] == 1 or dp[0][0] == 1: return 0
        # m, n = len(dp), len(dp[0])
#         i,j = m-1, n-1
#         # dp[i][j] = -1
#         q = [[i,j]]
#         while q:
#             i,j = q.pop(0)
#             # print('ij', i, j)
#             # Get the number of paths that end below the position
#             # unless there is an obstacle
#             if i == m - 1:
#                 d = 0
#             else:
#                 d = dp[i+1][j] if dp[i+1][j] != 1 else 0

#             # Get the number of paths that end below the position
#             # unless there is an obstacle
#             if j == n - 1:
#                 r = 0
#             else:
#                 r = dp[i][j+1] if dp[i][j+1] != 1 else 0

#             # Update if not an obstacle
#             dp[i][j] = d + r if dp[i][j] != 1 else 1

#             if i == m-1 and j == n-1:
#                 dp[i][j] = -1

#             # Add next elements to queue
#             if i-1 >= 0:
#                 q.append([i-1, j])
#             if j-1 >= 0:
#                 q.append([i, j-1])
#             # print(dp)

#         return -dp[0][0]
