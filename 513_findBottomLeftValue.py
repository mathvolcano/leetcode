"""
513. Find Bottom Left Tree Value
https://leetcode.com/problems/find-bottom-left-tree-value/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findBottomLeftValue(self, root: TreeNode) -> int:

        # Level-wise traversal
        # [1] Add root to a queue
        # [2] for each element in the queue get it's check children (starting from left)
        # [3] if no children are found return head of queue, else repeat
        # Time complexity is O(n) because we must traverse all elements
        # Space complexity is O(n) because in worst case scenario the binary tree could be a
        # balanced BST and n/2 entries could be kept in the last row.

        if not root: return
        level = [root]
        while level:
            next_level = []
            for r in level:
                if r.left:
                    next_level.append(r.left)
                if r.right:
                    next_level.append(r.right)
            if not len(next_level):
                return level[0].val
            else:
                level = next_level
        return -1
