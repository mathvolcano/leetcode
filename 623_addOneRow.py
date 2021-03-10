"""
623. Add One Row to Tree
https://leetcode.com/problems/add-one-row-to-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def addOneRow(self, root: TreeNode, v: int, d: int) -> TreeNode:
        if not root: return root
        if d == 1:
            return TreeNode(v, root.left, None)
        elif d == 2:
            root.left = TreeNode(v, root.left, None)
            root.right = TreeNode(v, None, root.right)
        else:
            if root.left:
                root.left = self.addOneRow(root.left, v, d-1)
            if root.right:
                root.right = self.addOneRow(root.right, v, d-1)
        return root


