"""
285. Inorder Successor in BST
https://leetcode.com/problems/inorder-successor-in-bst/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def inorderSuccessor(self, root: 'TreeNode', p: 'TreeNode') -> 'TreeNode':
        ancestor = None
        while root and root.val:
            if p.val < root.val:
                ancestor = root
                root = root.left
            else:
                root = root.right
        return ancestor
