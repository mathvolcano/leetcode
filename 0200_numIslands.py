"""
200. Number of Islands
https://leetcode.com/problems/number-of-islands/
"""

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        # DFS
        # [1] Return 0 if trivial grid
        # [2] Iterate through the grid
        #  a. if we encounter a '1' then perform a dfs
        #  b. Update grid entry from '1' to '0'.
        #  b. get all new directions to the current position by adding standard vector directions
        #  c. Perform dfs on each direction
        #  d. increment result counter
        # Time complexity: O(m*n)
        # Space complexity: O(1) additional variable storage, but worst case need O(m*n) memory for stack

        m, n = len(grid), len(grid[0])

        res = 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == "1":
                    self.dfs(grid, r, c)
                    res += 1
        return res

    def dfs(self, grid, r, c):
        directions = [(0,-1), (0,1), (-1,0), (1, 0)]
        grid[r][c] = "0"
        for d in directions:
            new_r = r + d[0]
            new_c = c + d[1]
            is_valid = (new_r >= 0 and new_c >= 0 and new_r < len(grid) and new_c < len(grid[0]))
            if is_valid:
                if grid[new_r][new_c] == "1":
                    self.dfs(grid, new_r, new_c)
