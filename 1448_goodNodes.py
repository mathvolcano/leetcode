"""
1448. Count Good Nodes in Binary Tree
https://leetcode.com/problems/count-good-nodes-in-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:

        # Perform a Depth First Search
        # [1] if root is at least as big as max_val then increment count
        # [2] update the max_value on the path
        # [3] Perform goodNodes on root.left and root.right
        # [4] return count

        def dfs(root, max_val):
            if not root: return
            if root.val >= max_val:
                self.total += 1
                max_val = max(max_val, root.val)
            if root.left:
                dfs(root.left, max_val)
            if root.right:
                dfs(root.right, max_val)

        if not root: return 0
        self.total = 0
        dfs(root, -float('inf'))
        return self.total
