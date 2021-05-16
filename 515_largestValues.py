"""
515. Find Largest Value in Each Tree Row
https://leetcode.com/problems/find-largest-value-in-each-tree-row/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: TreeNode) -> List[int]:

        # BFS or level-order traversal
        # [1] Store in a list the nodes in the level
        # [2] Get the max of the nodes on the level
        # [3] Update the list to include the children in the next level.
        # Time complexity O(n) and space complexity O(h) additional space to store max values.

        if not root: return []
        res = []
        level = [root]
        while level:
            new_level = []
            lvl_max = -float('inf')
            for n in level:
                lvl_max = max(lvl_max, n.val)
                if n.left:
                    new_level.append(n.left)
                if n.right:
                    new_level.append(n.right)
            res.append(lvl_max)
            level = new_level

        return res
