"""
536. Construct Binary Tree from String
https://leetcode.com/problems/construct-binary-tree-from-string/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def str2tree(self, s: str) -> TreeNode:
        # Trivial cases
        if len(s) == 0: return None
        if '(' not in s: return TreeNode(int(s))

        def paren_pair_idx(s):
            """Find the outermost pair of parentheses."""
            paren_count = 0
            for i, c in enumerate(s):
                if c == '(':
                    paren_count += 1
                elif c == ')':
                    paren_count -= 1
                if paren_count == 0 and i > s.find('('):
                    return (s.find('('), i)

        # Construct tree by preorder traversal
        root = TreeNode(int(s[:s.find('(')]))

        # Left
        l, r = paren_pair_idx(s)
        root.left = self.str2tree(s[l+1:r])

        # Right
        if r < len(s) - 1:
            root.right = self.str2tree(s[r+2: -1])  # Exclude ')(' and ')'
        else:
            root.right = None

        return root


