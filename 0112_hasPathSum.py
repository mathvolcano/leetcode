"""
112. Path Sum
https://leetcode.com/problems/path-sum/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: TreeNode, sum: int) -> bool:

        # DFS
        # [1] Check if a root is a leaf and has value equal the sum. If so, return True
        # [2] Else, subtract the root value from the sum
        # [3] Recurse on left &/or right nodes.Return logical or of them.
        # O(n) time to because we must check all nodes. O(log n) space complexity for recursive stack.
        if not root: return False
        if (not root.left) and (not root.right) and (root.val == sum):
            return True
        return(self.hasPathSum( root.left, sum-root.val) or
               self.hasPathSum(root.right, sum-root.val)
        )
