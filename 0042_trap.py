"""
42. Trapping Rain Water
https://leetcode.com/problems/trapping-rain-water/
"""
import heapq
def trap(self, heightMap: List[int]) -> int:
    # O(mn) space complexity, O(mn) time complexity
    # Perform a BFS stepping from visited to non-visited entries
    # Use a min heap to store the smallest height
    # stepping from visited to nonvisited
    if len(height) <= 1: return 0
    m, n = len(heightMap), len(heightMap and heightMap[0])
    heap, vol = [], 0
    for i in range(m):
        for j in range(n):
            if i in {0, m - 1} or j in {0, n - 1}:
                heapq.heappush(heap, (heightMap[i][j], i, j))
                heightMap[i][j] = -1
    while heap:
        h, i, j = heapq.heappop(heap)
        steps = ((i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1))
        for x, y in steps:
            if 0 < x < m - 1 and 0 < y < n - 1 and heightMap[x][y] != -1:
                vol += max(h - heightMap[x][y], 0)
                heapq.heappush(heap, (max(heightMap[x][y], h), x, y))
                heightMap[x][y] = -1
    return vol
