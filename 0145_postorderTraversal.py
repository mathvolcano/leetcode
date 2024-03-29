# 145. Binary Tree Postorder Traversal
# https://leetcode.com/problems/binary-tree-postorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        traversal = []
        if not root: return traversal

        if root.left:
            traversal.extend(self.postorderTraversal(root.left))
        if root.right:
            traversal.extend(self.postorderTraversal(root.right))
        traversal.append(root.val)
        return traversal