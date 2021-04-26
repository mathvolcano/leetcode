"""
https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/
323. Number of Connected Components in an Undirected Graph
"""

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        # O(n) time and O(n) space.
        # Perform a dfs
        self.visited = [0] * n

        def dfs(node):
            # print('running dfs for ', node)
            for e in edges:
                n1, n2 = e
                if   n1 == node and self.visited[n2] == 0:
                    self.visited[n2] = 1
                    dfs(n2)
                elif n2 == node and self.visited[n1] == 0:
                    self.visited[n1] = 1
                    dfs(n1)

        res = 0
        for k in range(n):
            if self.visited[k] == 0:
                self.visited[k] = 1
                dfs(k)
                res += 1
        return res