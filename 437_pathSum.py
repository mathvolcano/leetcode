"""
437. Path Sum III
https://leetcode.com/problems/path-sum-iii/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, path_sum: int) -> int:
        n_paths = 0
        if not root: return n_paths
        n_paths += self.n_continued_paths(root, path_sum)

        # Start over from lower nodes
        if root.left:
            n_paths += self.pathSum(root.left, path_sum)
        if root.right:
            n_paths += self.pathSum(root.right, path_sum)

        return n_paths

    def n_continued_paths(self, root, target):
        if (not root): return 0

        n_paths = 1 if root.val == target else 0
        remainder = target - root.val
        if root.left:
            n_paths += self.n_continued_paths(root.left, remainder)
        if root.right:
            n_paths += self.n_continued_paths(root.right, remainder)
        return n_paths
