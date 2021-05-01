"""
222. Count Complete Tree Nodes
https://leetcode.com/problems/count-complete-tree-nodes/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        """BF – O(n) complexity because have to if nodes exist."""
        n = 0
        if not root: return n
        n += 1

        if root.right:
            n += self.countNodes(root.right)
        if root.left:
            n += self.countNodes(root.left)
        return n

