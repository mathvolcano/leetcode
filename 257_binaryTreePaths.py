"""
257. Binary Tree Paths
https://leetcode.com/problems/binary-tree-paths/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: TreeNode) -> List[str]:

        paths = []
        joiner = '->'
        if not root: return paths

        if (not root.left) and (not root.right):
            return [str(root.val)]
        else:
            if root.left:
                left_paths = [str(root.val) + joiner + x
                              for x in self.binaryTreePaths(root.left)]
                paths = paths + left_paths
            if root.right:
                right_paths = [str(root.val) + joiner + x
                               for x in self.binaryTreePaths(root.right)]
                paths = paths + right_paths
            return paths
