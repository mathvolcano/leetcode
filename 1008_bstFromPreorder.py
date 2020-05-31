"""
1008. Construct Binary Search Tree from Preorder Traversal
https://leetcode.com/problems/construct-binary-search-tree-from-preorder-traversal/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:

    def bstFromPreorder(self, preorder: List[int]) -> TreeNode:

        if not preorder: return None

        root = preorder[0]
        tree = TreeNode(root)
        i = 1
        while i < len(preorder):
            if preorder[i] > root:
                break
            i += 1

        tree.left = self.bstFromPreorder(preorder[1:i])
        tree.right = self.bstFromPreorder(preorder[i:])
        return tree

