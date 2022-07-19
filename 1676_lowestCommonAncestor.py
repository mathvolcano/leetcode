"""
1676. Lowest Common Ancestor of a Binary Tree IV
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iv/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def __init__(self):
        self.nodes = []

    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        # Recursion
        # [0] Base case if not root or root in nodes; return root
        # [1] Make nodes a hash set so lookup time is O(1)
        # [2] Recursive: call left & and right children of root and assign to l,r
        # [3] if both l & r then return current node
        # [4] return left if left else right
        # Complexity: m = number of nodes of root, n = len(nodes), h height of root
        # Time: O(m*n) for h calls of checking if root in nodes, worst case when root skewed O(m*n)
        # Space: O(h * n) for h calls of checking if root in nodes, worst case when root skewed O(m*n)
        if not self.nodes:
            self.nodes = set(nodes)

        if not root or root in self.nodes:
            return root
        l = self.lowestCommonAncestor(root.left, nodes)
        r = self.lowestCommonAncestor(root.right, nodes)
        if l and r:
            return root
        return l if l else r
