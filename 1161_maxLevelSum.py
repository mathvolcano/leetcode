"""
1161. Maximum Level Sum of a Binary Tree
https://leetcode.com/problems/maximum-level-sum-of-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxLevelSum(self, root: TreeNode) -> int:

        # Level-Order Search
        # [1] initialize variables, res & max_sum, store the min level and the max level sum respectively for the search
        # [2] initialize a level containing the root.
        # [3] while there is a level get the sum of the level and update res & max_sum
        # [4] get the level's children and update level
        # Time complexity: O(n) and space complexity O(log n) to store last level

        if not root: return

        res, max_sum = 1, root.val
        level, nodes = 1, [root]
        while nodes:
            total = sum([r.val for r in nodes])
            if total > max_sum:
                res, max_sum = level, total
            next_nodes = []
            for n in nodes:
                if n.left:
                    next_nodes.append(n.left)
                if n.right:
                    next_nodes.append(n.right)
            level, nodes = level + 1, next_nodes
        return res
