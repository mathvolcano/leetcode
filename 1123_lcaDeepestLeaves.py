"""
1123. Lowest Common Ancestor of Deepest Leaves
https://leetcode.com/problems/lowest-common-ancestor-of-deepest-leaves/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def lcaDeepestLeaves(self, root: TreeNode) -> TreeNode:

        # DFS
        # Observation is that once we have found the deepest depth then recursively
        # tracing their parents gives us the LCA
        # [0] Initialize variables lca & deepest to track depth
        # [1] Create dfs helper that calls node n & depth d
        # [2] Base case if not node return d
        # [3] else get dfs of left & right children with d+1. If both left & right are deepest then set lca to node
        # else: return max of left & right
        # Complexity: let n denote number of nodes & h height of tree (worse case is tree is skewed)
        # Time: O(n) because we traverse each node once
        # Space: O(h) for recursion stack calls (worse case O(n))
        self.lca, self.deepest = None, 0
        def dfs(n, d):
            self.deepest = max(self.deepest, d)
            if not n: return d
            l = dfs( n.left, d + 1)
            r = dfs(n.right, d + 1)
            if l == r == self.deepest:
                self.lca = n
            return max(l, r)
        dfs(root, 0)
        return self.lca
