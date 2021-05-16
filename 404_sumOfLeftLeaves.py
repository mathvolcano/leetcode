"""
404. Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        # Perform a DFS search
        # [1] Check if the root has a left leaf. If so add the value to the total
        # [2] Search the next nodes in the root

        def dfs(root):
            if not root: return
            if root.left and not root.left.left and not root.left.right:
                self.total += root.left.val
            dfs(root.left)
            dfs(root.right)

        self.total = 0
        dfs(root)
        return self.total
