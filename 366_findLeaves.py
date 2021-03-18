"""
366. Find Leaves of Binary Tree
https://leetcode.com/problems/find-leaves-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: TreeNode) -> List[List[int]]:
        """Perform DFS to find depth of the subtrees. Return children of the same depth.
        O(n) because we have to traverse all elements.
        """
        def dfs(root):
            if not root:
                return -1

            depth = max(dfs(root.left), dfs(root.right)) + 1
            if depth == len(res):
                res.append([])
            res[depth].append(root.val)
            return depth

        res = []
        dfs(root)
        return res

