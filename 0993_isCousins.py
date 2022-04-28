"""
993. Cousins in Binary Tree
https://leetcode.com/problems/cousins-in-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        # BFS, level-wise traversal
        # [1] Initialize queue, q = []
        # [2] Iterate through q
        #. b. check if any node has x & y as children values. if so return false
        #. a. else if x & y are already in the queue, return true (because they have the same depth)
        #. c. else, add children to next level and update queue
        # n = # nodes in tree
        # O(n) time complexity and O(n) space (worst case) to store all leaf nodes in a balanced binary tree
        # Can do early stopping to improve code speed.
        # TODO: perform DFS
        if not root: return False
        q = [root]
        t = (x,y)  # targets
        while q:
            lvl = []
            # uses uniqueness of tree node values
            if sum(1 if z.val in t else 0 for z in q) == 2:
                return True
            for n in q:
                # print('n', n.val)
                if n.left and (n.left.val in t) and n.right and (n.right.val in t):
                    return False
                if n.left:
                    lvl.append(n.left)
                if n.right:
                    lvl.append(n.right)
            q = lvl
        return False
