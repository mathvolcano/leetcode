"""
429. N-ary Tree Level Order Traversal
https://leetcode.com/problems/n-ary-tree-level-order-traversal/
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        if not root: return None

        traversal = [[root.val]]
        lvl = root.children
        while lvl:
            traversal += [[c.val for c in lvl]]
            nxt_lvl = []
            for c in lvl:
                nxt_lvl += c.children
            lvl = nxt_lvl
        return traversal
