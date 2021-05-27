"""
105. Construct Binary Tree from Preorder and Inorder Traversal
https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        #                 3                          
        #               /  \                       
        #             9     20                     
        #            / \     / \                      
        #           6   11   15  7         

        #         preorder = [3,9,6,11,20,15,7]
        #         inorder  = [6,9,11,3,15,20,7]

        # Recursion / DFS
        # Know root is 3 from preorder
        # Know from inorder that everyting before 3 is left of root
        # and everything right of 3 is right node.
        # [1] So pop 3 from preorder
        # For values l of 3 in inorder, get the l values from preorder in the same order
        # For values r of 3 in inorder, get the r values from preorder in the same order
        # assign left node to be buildTree of these values and right node to be buildTree of these values
        # preorder = [root, left, right] so split preorder to the left side with [1:idx+1]
        # and right to [idx+1:]
        # print('preorder', preorder)
        # print('inorder', inorder)
        # Time complexity is O(n) because we have to traverse all nodes
        # Space complexity is O(n) for stack memory and storing result
        if not preorder or not inorder: return None
        idx = inorder.index(preorder[0])
        return TreeNode(
            val   = preorder[0],
            left  = self.buildTree(preorder[1:idx+1], inorder[:idx]),
            right = self.buildTree(preorder[idx+1: ], inorder[idx+1:])
        )
