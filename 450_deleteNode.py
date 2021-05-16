"""
450. Delete Node in a BST
https://leetcode.com/problems/delete-node-in-a-bst/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deleteNode(self, root: TreeNode, key: int) -> TreeNode:

        # Recursion
        # [1] Root does not have eky
        # [1a] if key is less than the root value then recurse on left
        # [1a] if key is > the root value then recurse on right
        # [2] Root has key, but not both children. Set the root value to child
        # [3] If both left and right nodes exist
        # then get the next larger value than the root and give it to the root value
        # [4] Recurse on right there could be duplicates.

        if not root:
            return root
        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)
        else:
            if not root.left:
                return root.right
            if not root.right:
                return root.left
            tmp = root.right
            while tmp.left:
                tmp = tmp.left
            root.val = tmp.val
            root.right = self.deleteNode(root.right, tmp.val)
        return root
