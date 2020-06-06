"""
101. Symmetric Tree
https://leetcode.com/problems/symmetric-tree/submissions/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:

        # check if subtree pairs are symmetric
        def symmetry_helper(sub_tree1, sub_tree2):
            if not sub_tree1 and not sub_tree2:
                return True
            elif sub_tree1 and sub_tree2:
                equal_vals = (sub_tree1.val == sub_tree2.val)
                outer_symmetry = symmetry_helper(sub_tree1.left, sub_tree2.right)
                inner_symmetry = symmetry_helper(sub_tree1.right, sub_tree2.left)
                return (equal_vals and outer_symmetry and inner_symmetry)
            else:
                return False

        return (not root) or symmetry_helper(root.left, root.right)
