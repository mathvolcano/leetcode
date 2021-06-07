"""
797. All Paths From Source to Target
https://leetcode.com/problems/all-paths-from-source-to-target/
"""

class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:

        # DFS
        # [0] start at 0
        # [1] For a given path if the path ends at n-1 then append to results
        # [2] Else, for the current position fetch the next nodes and append to path
        # [3] repeat in graph
        # Assumes all edges of graph has a terminal state of n-1
        # Time & space complexity is O(len(graph) * max([len(x) for x in graph]))


        def dfs(cur, path, graph, res):
            if cur == len(graph) - 1:
                res.append(path)
                return
            else:
                for n in graph[cur]:
                    dfs(n, path+[n], graph, res)

        res = []
        dfs(0, [0], graph, res)
        return res
