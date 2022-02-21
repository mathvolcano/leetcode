"""
399. Evaluate Division
https://leetcode.com/problems/evaluate-division/
"""

class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:

        # Graph Traversal & DFS
        # [1] construct the graph as an adjacency matrix of division operations
        # [2] Iterate through queries and perform a DFS search for each entry
        # [3] Build our DFS search
        # Time and space complexity is O(e^2) where e is the number of unique variables in equations
        # Needed because we may have to search all node paths and to store full graph.

        from collections import defaultdict
        gr = defaultdict(dict)
        for (x,y), v in zip(equations, values):
            gr[x][y] = v
            gr[y][x] = 1. / v

        def dfs(x, y, visited):
            if x not in gr or y not in gr:
                return -1.

            if y in gr[x]:
                return gr[x][y]

            for i in gr[x]:
                if i not in visited:
                    visited.add(i)
                    tmp = dfs(i, y, visited)
                    if tmp == -1:
                        continue
                    else:
                        return gr[x][i] * tmp  # a/b * b/c
            return -1

        res = []
        for q in queries:
            q_res = dfs(q[0], q[1], set())
            res.append(q_res)
        return res
