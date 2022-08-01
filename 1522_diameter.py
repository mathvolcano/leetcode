"""
1522. Diameter of N-Ary Tree
https://leetcode.com/problems/diameter-of-n-ary-tree/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        # DFS to get the height of the node
        # [0] define a helper function dfs to return the length of the longest paths
        # [1] DFS: if not node return 0
        # [2] DFS: initialize top 2 maxes max1, max2
        # [2] DFS search the children
        # [3] DFS: update max1 & max2 if heigh is bigger than max1, else check max2 & update
        # [3] DFS: update diameter self.treeDiameter = max(self.treeDiameter, max1 + max2)
        # [4] DFS: return max(max1, max2) + 1 as the length of the longest path up to root
        # [5] dfs(root) and return self.treeDiameter + 1
        # Complexity: n = number of nodes
        # Time: worst case is ll and O(n) because we enter & exit each node once
        # Space: worst case ll, O(n) for recursive call stack.
        self.res = 0
        def dfs(n):  # node
            if not n: return 0
            max1, max2 = 0, 0
            for c in n.children:
                h = dfs(c)
                if h >= max1:
                    max1, max2 = h, max1
                elif max2 <= h < max1:
                    max2 = h
            self.res = max(self.res, max1 + max2) # Update diameter by length of longest path
            return max(max1, max2) + 1  # height is the max height of the subtrees + 1
        dfs(root)
        return self.res
