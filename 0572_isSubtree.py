"""
572. Subtree of Another Tree
https://leetcode.com/problems/subtree-of-another-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

# DFS
# [1] Define a function isSameTree to test whether 2 trees are the same
# [a] Test if roots are empty, return True
# [b] if only 1 tree is empty then return False
# [c] Recurse on left & right children
# [2] Iterate through the tree t checking if s equals t
# [a] if not, then check children of t.

# O(max(n_s, n_t)) time complexity to traverse each of the n nodes of s & t.
# O(max(n_s, n_t)) space complexity because the tail recursion requires storing all nodes in memory
class Solution:
    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False
        if s.val != t.val:
            return False
        else:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)

    def isSubtree(self, s: TreeNode, t: TreeNode) -> bool:
        if not s and not t:
            return True
        if not s or not t:
            return False
        return self.isSameTree(s, t) or self.isSubtree(s.left, t) or self.isSubtree(s.right, t)
