"""
538. Convert BST to Greater Tree
https://leetcode.com/problems/convert-bst-to-greater-tree/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def __init__(self):
        self._sum = 0

    def convertBST(self, root: TreeNode) -> TreeNode:
        if not root: return None

        if root.right:
            root.right = self.convertBST(root.right)
        self._sum += root.val
        root.val = self._sum
        if root.left:
            root.left = self.convertBST(root.left)
        return root

