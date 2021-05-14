"""
98. Validate Binary Search Tree
https://leetcode.com/problems/validate-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode) -> bool:
        # [1] Get a list of root values via an inorder traversal
        # [2] Check the BST condition holds: that the inorder traversal is ascending.
        # O(n) time and space to perform and store the traversal

        if not root: return False

        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        traversal = inorder(root)
        for i,t in enumerate(traversal[1:], start=1):
            if t <= traversal[i-1]:
                return False
        return True
