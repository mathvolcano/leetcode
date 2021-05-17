"""
463. Island Perimeter
https://leetcode.com/problems/island-perimeter/
"""

class Solution:
    def islandPerimeter(self, grid: List[List[int]]) -> int:

        # Brute Force - iterate through the grid
        # Note that the perimeter is equal to 4 * the number of land cells
        # minus 2 times the number of internal edges
        # [1] When land is found increment land
        # [2] If the grid cell is a land increment the edges if the previous cell to the left is a land
        # [4] If the grid cell is a land increment the edges if the cell above it is a land
        # [3] return 4*land - 2*edges
        # O(m*n) time complexity and O(1) space.

        m, n = len(grid), len(grid[0])
        land, edges = 0, 0
        for r in range(m):
            for c in range(n):
                if grid[r][c] == 1:
                    land += 1
                    if r > 0 and grid[r-1][c] == 1:
                        edges += 1
                    if c > 0 and grid[r][c-1] == 1:
                        edges += 1
        return 4 * land - 2 * edges
