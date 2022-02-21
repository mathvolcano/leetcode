"""
110. Balanced Binary Tree
https://leetcode.com/problems/balanced-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



def isBalanced(root):

    def height(root):
        if root == None:
            return 0
        else:
            return max(height(root.left), height(root.right)) + 1

    if root == None:
        return 1
    else:
        imbalanced = abs(height(root.left) - height(root.right)) > 1
        if imbalanced:
            return 0
        else:
            return isBalanced(root.left) and isBalanced(root.right)


