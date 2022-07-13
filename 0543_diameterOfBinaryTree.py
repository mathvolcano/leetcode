"""
543. Diameter of Binary Tree
https://leetcode.com/problems/diameter-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

def diameterOfBinaryTree(self, root: TreeNode) -> int:
    # DFS to get the height of the node
    # [0] define a helper function dfs to return the length of the longest paths
    # [1] if not node return 0
    # [2] DFS search the left then the right children
    # [3] update diameter self.treeDiameter = max(self.treeDiameter, l + r)
    # [4] return max(l,r) + 1 as the length of the longest path up to root
    # [5] dfs(root) and return self.treeDiameter + 1
    # Complexity: n = number of nodes
    # Time: worst case is ll and O(n) because we enter & exit each node once
    # Space: worst case ll, O(n) for recursive call stack.
    self.res = 0
    def dfs(n):  # node
        if not n: return 0
        l = dfs( n.left)
        r = dfs(n.right)
        self.res = max(self.res, l + r) # Update diameter by length of longest path
        return max(l,r) + 1  # height is the max height of the subtrees + 1
    dfs(root)
    return self.res

    # Recrusion
    # if not root: return 0
    #
    # def height(node):
    #     if not node: return 0
    #     return 1 + max(height(node.left), height(node.right))
    #
    # l_height = height(root.left)
    # r_height = height(root.right)
    #
    # l_diam = diameterOfBinaryTree(root.left)
    # r_diam = diameterOfBinaryTree(root.right)
    #
    # return max(l_height + r_height, max(l_diam, r_diam))
