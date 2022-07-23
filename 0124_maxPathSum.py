"""
124. Binary Tree Maximum Path Sum
https://leetcode.com/problems/binary-tree-maximum-path-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxPathSum(self, root: Optional[TreeNode]) -> int:
        # DFS to get the sum of the longest path
        # [0] define a helper function dfs to return the sum of the max sum paths
        # [1] if not node return 0
        # [2] DFS search the left then the right children
        # [3] update max sum with self.res = max(self.res, l + r)
        # [4] return max(l,r) + node.val as the max sum path up to & including root
        # [5] dfs(root) and return self.treeDiameter + 1
        # Complexity: n = number of nodes
        # Time: worst case is ll and O(n) because we enter & exit each node once
        # Space: worst case ll, O(n) for recursive call stack.
        res = -float('inf')
        def dfs(n):  # node
            if not n: return 0
            l = max(dfs( n.left), 0)  # ignore paths with negative sums,
            r = max(dfs(n.right), 0)
            nonlocal res
            res = max(res, l + r + n.val)
            return max(l,r) + n.val
        dfs(root)
        return res
