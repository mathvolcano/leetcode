#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 24 07:47:27 2020

@author: mathvolcano

https://leetcode.com/explore/learn/card/queue-stack/232/practical-application-stack/1380/

Number of Islands
"""

def numIslands(self, grid):
    if not grid or not grid[0]:
        return 0
    
    # grid is mxn
    m = len(grid)
    n = len(grid[0])
    
    count = 0
    for r in range(m):
        for c in range(n):
            if grid[r][c] == "1":
                self.dfs(grid, r, c)
                count += 1
    return count

    def dfs(self, grid, r, c):
        directions = [(0,-1), (0,1), (-1,0), (1, 0)]
        grid[r][c] = "0"
        for direction in directions:
            new_r = r + direction[0]
            new_c = c + direction[1]
            is_valid = (new_r >= 0 and new_c >= 0 and new_r < len(grid) and new_c < len(grid[0]))
            if is_valid:
                if grid[new_r][new_c] == "1":
                    self.dfs(grid, new_r, new_c)
