"""
1302. Deepest Leaves Sum
https://leetcode.com/problems/deepest-leaves-sum/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def deepestLeavesSum(self, root: TreeNode) -> int:

        def maxDepth(root):
            if root == None:
                return 0
            return 1 + max(maxDepth(root.left), maxDepth(root.right))

        # 1. Traverse tree to find max depth
        # 2. Traverse tree again to compute the sum

        max_depth = maxDepth(root)
        cur_depth, level = 1, [root]
        while level:
            if cur_depth == max_depth:
                return sum(r.val for r in level)
            # Get next level
            next_level = []
            for n in level:
                if n.left:
                    next_level.append(n.left)
                if n.right:
                    next_level.append(n.right)
            cur_depth += 1
            level = next_level
