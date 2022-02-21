"""
133. Clone Graph
https://leetcode.com/problems/clone-graph/
"""

## Definition for a Node.
#class Node:
#    def __init__(self, val = 0, neighbors = []):
#        self.val = val
#        self.neighbors = neighbors

class Solution:
    def __init__(self):
        self.visited = {}

    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return

        new_node = Node(node.val, [])

        if node.val not in self.visited:
            self.visited[node.val] = new_node

        for neighbor in node.neighbors:
            if neighbor.val in self.visited:
                new_node.neighbors.append(self.visited[neighbor.val])
            else:
                new_node.neighbors.append(self.cloneGraph(neighbor))

        return new_node


adjList = [[2,4],[1,3],[2,4],[1,3]]