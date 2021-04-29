"""
114. Flatten Binary Tree to Linked List
https://leetcode.com/problems/flatten-binary-tree-to-linked-list/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode) -> None:
        """
        Do not return anything, modify root in-place instead.
        """

        # Perform a DFS, us a stack to store the current node in a post order traversal
        def dfs(root, stack):
            if root is None: return
            dfs(root.right, stack)
            dfs(root.left, stack)
            root.right = stack.pop()
            root.left = None
            stack.append(root)
            return root

        dfs(root, [None])
