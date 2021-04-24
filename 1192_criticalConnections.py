"""
1192. Critical Connections in a Network
https://leetcode.com/problems/critical-connections-in-a-network/
"""

class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        def dfs(node, parent, adjacency, edges):
            self.ts += 1
            dfs_num[node] = self.ts
            lowest_rank[node] = self.ts
            for neighbor in adjacency[node]:
                if neighbor == parent:
                    continue
                if (not dfs_num[neighbor]):
                    dfs(neighbor, node, adjacency, edges)
                # Reset the older reachable if a neighbor cycles back
                lowest_rank[node] = min(lowest_rank[node], lowest_rank[neighbor])

                # if neighbor cannot reach back to self or older then critical connection
                if lowest_rank[neighbor] > dfs_num[node]:
                    print('found cc', [node, neighbor])
                    cc.append([node, neighbor])

        if len(connections) == 1 or (n <= 2): return connections

        adjacency = [[] for _ in range(n)]
        for c in connections:
            adjacency[c[0]].append(c[1])
            adjacency[c[1]].append(c[0])

        dfs_num = [0] * n
        lowest_rank = [0] * n
        self.ts = 0  # Timestamp
        cc = []  # Critical connections
        dfs(0, -1, adjacency, cc)
        return cc
