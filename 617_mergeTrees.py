"""
617. Merge Two Binary Trees
https://leetcode.com/problems/merge-two-binary-trees/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def mergeTrees(self, t1: TreeNode, t2: TreeNode) -> TreeNode:
        if not t1: return t2
        if not t2: return t1

        t3 = TreeNode()
        t3.val = t1.val + t2.val
        t3.left = self.mergeTrees(t1.left, t2.left)
        t3.right = self.mergeTrees(t1.right, t2.right)
        return t3
