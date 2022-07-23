"""
236. Lowest Common Ancestor of a Binary Tree
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # Recursion
        # [1] Base case: if not root or p = root or q = root then return root
        # [2] Recursive call to left & right subtree
        # [3] if left and right return root, then root is the LCA and return root
        # [4] Return left if left else right
        # Complexity: n = number of nodes and h the height of the tree
        # Time: worst case O(n) to traverse entire tree with nodes on the right
        # Space: O(h) storage for recursive stack calls, worst case is O(n) with skewed tree and ll
        if not root or p == root or q == root:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left and right:
            return root
        return left if left else right
