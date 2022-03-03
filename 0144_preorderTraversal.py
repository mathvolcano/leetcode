"""
144. Binary Tree Preorder Traversal
https://leetcode.com/problems/binary-tree-preorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: TreeNode) -> List[int]:
        if not root: return []

        l, r = [], []
        if root.left:
            l = self.preorderTraversal(root.left)
        if root.right:
            r = self.preorderTraversal(root.right)
        return [root.val] + l + r
