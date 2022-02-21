"""
684. Redundant Connection
https://leetcode.com/problems/redundant-connection/
"""

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:

        # DFS
        # For each edge (a,b) check use DFS search to check if a & b are already connected
        # earlier in the edges list
        # [1] Construct a graph of the edges as an array, connected, where the the index i
        # corresponds with the integer in the edge [i,j] and the value is j.
        # [2] Iterate through edges. For each edge e = [n1, n2] in edges get the largest node visited value in the connections that n1 and n2 are connected to. Call it n3, n4.
        # [3] if n3 == n4 then return n1 and n2 because they were already connected.
        # [4] else, update connections with n1 and n2.
        # Time complexity is O(n^2) worst case, and O(n) space complexity for the connected array.

        connected = [0] * (len(edges) + 1)

        def dfs(node):
            if connected[node] == 0:
                return node
            return dfs(connected[node])

        for n1, n2 in edges:
            n3 = dfs(n1)
            n4 = dfs(n2)
            if n3 == n4:
                return [n1, n2]
            connected[n3] = n4
