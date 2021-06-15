"""
965. Univalued Binary Tree
https://leetcode.com/problems/univalued-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        # [0] return true if no root
        # [1] Check if root's value equals the value of the children and return false if not
        # [2] Return isUnivalTree of left and right
        # Time and space complexity O(n) (space for the tail recursion)

        if not root: return True
        if root.left and root.val != root.left.val:
            return False
        if root.right and root.val != root.right.val:
            return False
        return self.isUnivalTree(root.left) and self.isUnivalTree(root.right)
