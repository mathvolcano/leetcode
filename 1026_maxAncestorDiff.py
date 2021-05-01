"""
1026. Maximum Difference Between Node and Ancestor
https://leetcode.com/problems/maximum-difference-between-node-and-ancestor/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def maxAncestorDiff(self, root: TreeNode) -> int:
        self.abs_max = 0
        self.helper(root)
        return self.abs_max

    def helper(self, root, imax = -float('inf'), imin = float('inf')):
        if not root: return 0
        imax = max(imax, root.val)
        imin = min(imin, root.val)
        self.abs_max = max(self.abs_max, abs(imax - imin))
        self.helper(root.left, imax, imin)
        self.helper(root.right, imax, imin)
        return self.abs_max
