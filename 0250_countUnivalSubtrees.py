"""
250. Count Univalue Subtrees
https://leetcode.com/problems/count-univalue-subtrees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countUnivalSubtrees(self, root: TreeNode) -> int:
        self.count = 0
        self.dfs(root)
        return self.count

        # DFS - Postorder Traversal
        # If at least one child is "True" and root.val is equal to that child's value,
        # then root node is uniValue subtree node.
        # O(n) time complexity to traverse all roots
        # O(1) space complexity with recursion stack depth O(n)
    def dfs(self, root):
        if not root: return True
        l, r = self.dfs(root.left), self.dfs(root.right)
        l_match = (not root.left)  or (root.left.val == root.val)
        r_match = (not root.right) or (root.right.val == root.val)
        if l and r and l_match and r_match:
            self.count += 1
            return True
        return False
