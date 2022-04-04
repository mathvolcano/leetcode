"""
938. Range Sum of BST
https://leetcode.com/problems/range-sum-of-bst/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rangeSumBST(self, root: Optional[TreeNode], low: int, high: int) -> int:
        # DFS
        # O(n) time complexity (worst case) and O(n) space (worst case with a single line for call stack)
        self.res = 0
        def dfs(root):
            if not root: return
            v = root.val
            if low <= v <= high:
                self.res += v
            if low < v:
                dfs(root.left)
            if v < high:
                dfs(root.right)

        dfs(root)
        return self.res

        # Recursion Preorder traversal
        # O(n) time to search all nodes and O(n) space for recursion call stack of depth tree height of size log n
        # Does not use BST property so can do better.
        # res = 0
        # if not root: return res
        # v = root.val
        # if low <= v <= high:
        #     res += v
        # return res + self.rangeSumBST(root.left, low, high) + self.rangeSumBST(root.right, low, high)
