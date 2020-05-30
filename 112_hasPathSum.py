"""
112. Path Sum
https://leetcode.com/problems/path-sum/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:
        if not root: return False

        is_leaf = (not root.left) and (not root.right)
        root_leaf_sum = (root.val == sum) and is_leaf
        if root_leaf_sum:
            return root_leaf_sum
        else:
            sum -= root.val
            left_has_path_sum = self.hasPathSum(root.left, sum)
            right_has_path_sum = self.hasPathSum(root.right, sum)
            return max(left_has_path_sum, right_has_path_sum)
