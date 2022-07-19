"""
107. Binary Tree Level Order Traversal II
https://leetcode.com/problems/binary-tree-level-order-traversal-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrderBottom(self, root: TreeNode) -> List[List[int]]:
        # BFS
        # [1] initialize a queue, q = [root], of the level's nodes and a result, res = [], object
        # [2] while q: create a new level by adding the children
        # [3] append level to result
        # return result reversed from the last non-empty element
        # Complexity: let n be the number of nodes in the ree
        # Time: O(n) to traverse tree
        # Space: O(n) to store results
        res, q = [], [root]
        while q:
            res.append([n.val for n in q if n])
            q = [child for n in q if n for child in (n.left, n.right)]
        return res[-2::-1]
