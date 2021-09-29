"""
94. Binary Tree Inorder Traversal
https://leetcode.com/problems/binary-tree-inorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        l, r = [], []
        if root.left:
            l = self.inorderTraversal(root.left)
        if root.right:
            r = self.inorderTraversal(root.right)
        return l + [root.val] + r