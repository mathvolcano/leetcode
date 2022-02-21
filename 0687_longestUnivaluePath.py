"""
687. Longest Univalue Path
https://leetcode.com/problems/longest-univalue-path/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:

        # DFS - Postorder traversal DFS
        # [1] Check if the left child value or right child value equals the root value
        # [2] Add 1 to the longest path of either the left or right children's edge.
        # [3] If the the number of the total edge (left + right) is greater than the max number of edges
        # then we update the max number of edges.

        # O(n) time to traverse all nodes
        # O(h) space to store the stack memory

        def dfs(root):
            if not root: return 0
            l_len, r_len = dfs(root.left), dfs(root.right)
            l = l_len + 1 if root.left  and  root.left.val == root.val else 0
            r = r_len + 1 if root.right and root.right.val == root.val else 0
            self.longest.append(max(self.longest.pop(), l+r))
            print(root.val, self.longest)
            return max(l,r)

        self.longest = [0]
        dfs(root)
        return self.longest[0]
