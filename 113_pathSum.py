"""
113. Path Sum II
https://leetcode.com/problems/path-sum-ii/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode, path_sum: int) -> List[List[int]]:
        paths = []
        if not root: return paths
        self.dfs(root, path_sum, paths, [root.val])
        return paths

    def dfs(self, root, target, paths, cur_path):
        if (not root): return
        hit = (sum(cur_path) == target)
        if hit and (not root.left) and (not root.right):
            paths.append(cur_path)
        if root.left:
            new_path = cur_path + [root.left.val]
            self.dfs(root.left, target, paths, new_path)
        if root.right:
            new_path = cur_path + [root.right.val]
            self.dfs(root.right, target, paths, new_path)
