"""
958. Check Completeness of a Binary Tree
https://leetcode.com/problems/check-completeness-of-a-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCompleteTree(self, root: TreeNode) -> bool:
        # BFS
        # A complete binary tree has each level filled except the last level.
        # All nodes in the last level has to be as far left as possible.
        # For each level filled with nodes, the number of nodes must be 2^(n-1) with n level.

        if not root: return True

        stack = [[(root, 0)]]  # level[(node, val)]
        level = 0
        while True:
            children = []
            for n, v in stack[-1]:
                if n.left: children.append((n.left, 2 * v))
                if n.right: children.append((n.right, 2 * v + 1))
                if n.right and not n.left: return False
            if not children: break
            if len(stack[-1]) != pow(2, level): return False
            stack.append(children)
            level += 1
        return len(stack[-1]) == stack[-1][-1][1] + 1
