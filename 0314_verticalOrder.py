"""
314. Binary Tree Vertical Order Traversal
https://leetcode.com/problems/binary-tree-vertical-order-traversal/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def verticalOrder(self, root: TreeNode) -> List[List[int]]:
        # BFS
        # [1] Initialize a queue q with element node, pos = (root, 0)
        # [2] Initialize a cols hashmap that maps cols to node
        # [3] While q
        #. a.  pop first tuple of q and set to node, pos
        #. b.  if left child then subtract 1 from pos and add left node to queue. If right add 1 to pos and add right child to queue
        #. c.  add node to cols hashmap
        # [4] sort res by pos
        # [5] return the nodes of res
        import collections
        cols = collections.defaultdict(list)
        q = [(root,0)]  # queue

        for node, col in q:
            if node:
                cols[col].append(node.val)
                q += (node.left, col - 1), (node.right, col + 1)

        return [cols[col] for col in sorted(cols)]
