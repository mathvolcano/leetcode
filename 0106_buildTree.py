"""
106. Construct Binary Tree from Inorder and Postorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-inorder-and-postorder-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, inorder: List[int], postorder: List[int]) -> TreeNode:
        # Example
        #                 3
        #               /  \
        #             9     20
        #            / \     / \
        #           6   11   15  7

        #         inorder   = [left, root, right] = [6,9,11,3,15,20,7]
        #         postorder = [left, right, root] = [6,11,9,15,7,20,3]

        # Recursion / DFS
        # [1] Get root index from postorder
        # [2] split inorder to get left & right values for recursing for left & right nodes:
        # l inorder = inorder[:root_idx], r inorder = inorder[root_idx+1:]
        # [3] split postorder: r postorder = postorder[-1-root_idx:-1] and
        # l postorder = postorder[:-1-root_idx]
        # Ex: root_idx = 3,
        # l inorder = [:3] = [6,9,11], r inorder [15, 20, 7]
        # r postorder = [15,7,20], l postorder [6,11,9]
        if not inorder or not postorder: return None
        idx = inorder.index(postorder[-1])
        return TreeNode(
            val   = postorder[-1],
            left  = self.buildTree(inorder=inorder[:idx]  , postorder=postorder[:idx]),
            right = self.buildTree(inorder=inorder[idx+1:], postorder=postorder[idx:-1])
        )
