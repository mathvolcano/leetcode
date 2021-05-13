"""
1267. Count Servers that Communicate
https://leetcode.com/problems/count-servers-that-communicate/
"""

class Solution:
    def countServers(self, grid: List[List[int]]) -> int:

        # Brute Force
        # Note: the number of servers that can communicate with any other server
        # is the total number of servers that are not isolated, e.g., servers that
        # are located solely in their own row and column
        # [1] Get the row sums for each row and column
        # [2] count the total number of servers
        # [3] using the row sums and col sums count the number of isolated servers
        # [4] return the difference of the total number of servers and the isolated servers.

        m, n = len(grid), len(grid[0])
        row_sums = [0 for i in range(m)]
        col_sums = [0 for i in range(n)]
        for r in range(m):
            for c in range(n):
                v = grid[r][c]
                row_sums[r] += v
                col_sums[c] += v

        servers = sum(row_sums)
        isolated_servers = 0
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 1 and row_sums[i] == col_sums[j] == 1:
                    isolated_servers += 1
        return servers - isolated_servers
