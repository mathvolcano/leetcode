"""
103. Binary Tree Zigzag Level Order Traversal
https://leetcode.com/problems/binary-tree-zigzag-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:

        # Perform a level-order traversal
        # [1] create a flip bool to flip the orders and create a result list
        # [2] Create a queue and add current level's nodes (first root)
        # [3] for all nodes in queue add children to a new list
        # [4] If flip, then reverse order of nodes. If not keep order same. Append nodes to result

        # Time & space complexity is O(n) to traverse and store the whole tree.

        res = []
        if not root: return res

        q, flip = [root], 0
        while q:
            vals, nxt = [], []
            for r in q:
                vals.append(r.val)
                if r.left:
                    nxt.append(r.left)
                if r.right:
                    nxt.append(r.right)
            if flip:
                vals = vals[::-1]
            flip ^= 1
            res.append(vals)
            q = nxt
        return res
