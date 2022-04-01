"""
199. Binary Tree Right Side View
https://leetcode.com/problems/binary-tree-right-side-view/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:

        # BFS - level order traversal
        # [1] Initialize queue with root node and result object
        # [2] While queue,
        #  a. add right most value to result
        #. b. pop elements from queue and add children to next level
        #  c. add next level to queue
        # O(n) time & O(log n) space where n is the number of nodes in the tree
        from collections import deque  # makes solution faster than using array directly.
        if not root: return []

        res = []
        q = deque([root])
        while q:
            res.append(q[-1].val)
            lvl = []
            while q:
                n = q.popleft()
                if n.left: lvl.append(n.left)
                if n.right: lvl.append(n.right)
            q = deque(lvl)
        return res
