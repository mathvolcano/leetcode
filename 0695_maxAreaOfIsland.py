"""
695. Max Area of Island
https://leetcode.com/problems/max-area-of-island/
"""

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        # Perform a DFS Search
        # [1] Track the max area nd current area of an island
        # [2] Iterate through the grid skipping 0s
        # [3] When a 1 is found search all 4 directions for other 1s and count
        # the area in a DFS search (updating visited), flipping grid values from 1 to 0,
        # [4] Update the max area based on the current search
        # [5] Return max area
        # O(m*n) time and space complexity because all entries must be tracked and stored

        self.m, self.n = len(grid), len(grid[0])
        self.visited = [[0] * self.n for _ in range(self.m)]
        self.max_area = 0
        self.cur_area = 0
        for r in range(self.m):
            for c in range(self.n):
                self.visited[r][c] = 1
                if grid[r][c] == 1:
                    area = self.dfs(grid, r, c)
                    self.max_area = max(self.max_area, self.cur_area)
                    self.cur_area = 0
        return self.max_area

    def dfs(self, grid, r, c):
        directions = [(0, -1), (-1, 0), (0, 1), (1, 0)]
        self.cur_area += 1
        grid[r][c] = 0
        for d in directions:
            new_r = r + d[0]
            new_c = c + d[1]
            if (0 <= new_r < self.m and 0 <= new_c < self.n):
                if grid[new_r][new_c] == 1:
                    self.dfs(grid, new_r, new_c)