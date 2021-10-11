"""
547. Number of Provinces
https://leetcode.com/problems/number-of-provinces/
"""
class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        # Perform a DFS O(n^2) time and O(n) additional space.
        n = len(isConnected)
        self.visited = [0] * n
        provinces = 0

        def dfs(city_row):
            for k in range(n):
                if isConnected[city_row][k] == 1 and self.visited[k] == 0:
                    self.visited[k] = 1
                    dfs(k)

        for r in range(n):  # row
            if isConnected[r][r] == 1 and self.visited[r] == 0:
                self.visited[r] = 1
                dfs(r)
                provinces += 1
        return provinces
