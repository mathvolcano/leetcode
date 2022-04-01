"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:

        # BFS
        # [1] Initialize result object to track the levels and a levels queue to
        #     record the children of root
        # [2] While levels
        #  a. pop nodes
        #  b. append nodes to result
        #  c. append the children of each node to a new level and update level
        # Time complexity: O(n), with n the number of nodes in root
        # Space complexity: O(log n) ~ the number of nodes in the last level
        if not root: return []

        res = [[root.val]]
        levels = [x for x in [root.left, root.right] if x]
        while levels:
            new_vals = []
            new_levels = []
            for x in levels:
                new_vals.append(x.val)
                if x.left:
                    new_levels.append(x.left)
                if x.right:
                    new_levels.append(x.right)
            res.append(new_vals)
            levels = new_levels

        return res
