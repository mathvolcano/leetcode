"""
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def diameterOfBinaryTree(self, root: TreeNode) -> int:
    if not root: return 0

    def height(node):
        if not node: return 0
        return 1 + max(height(node.left), height(node.right))

    l_height = height(root.left)
    r_height = height(root.right)

    l_diam = diameterOfBinaryTree(root.left)
    r_diam = diameterOfBinaryTree(root.right)

    return max(l_height + r_height, max(l_diam, r_diam))
