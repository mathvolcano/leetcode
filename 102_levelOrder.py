"""
102. Binary Tree Level Order Traversal
https://leetcode.com/problems/binary-tree-level-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def levelOrder(root):
    if not root: return []
    
    res = [[root.val]]
    levels = [x for x in [root.left, root.right] if x]
    while levels:
        new_vals = []
        new_levels = []
        for x in levels:
            new_vals.append(x.val)
            if x.left:
                new_levels.append(x.left)
            if x.right:
                new_levels.append(x.right)
        res.append(new_vals)
        levels = new_levels
            
    return res