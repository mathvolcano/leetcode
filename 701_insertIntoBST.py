"""
701. Insert into a Binary Search Tree
https://leetcode.com/problems/insert-into-a-binary-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        if not root:
            return TreeNode(val=val)

        head = root

        while root:
            # End conditions
            if val < root.val and not root.left:
                root.left = TreeNode(val=val)
                break
            if val > root.val and not root.right:
                root.right = TreeNode(val=val)
                break

            # Traverse
            if val > root.val:
                root = root.right
            elif val < root.val:
                root = root.left
        return head
