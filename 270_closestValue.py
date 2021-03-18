"""
270. Closest Binary Search Tree Value
https://leetcode.com/problems/closest-binary-search-tree-value/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        if not root: return

        best = root.val
        smallest_diff = abs(target - best)
        if not root.left and not root.right:
            return best
        if target < best and root.left:
            l_best = self.closestValue(root.left, target)
            if abs(target - l_best) < smallest_diff:
                best = l_best
        if target > best and root.right:
            r_best = self.closestValue(root.right, target)
            if abs(target - r_best) < smallest_diff:
                best = r_best

        return best
