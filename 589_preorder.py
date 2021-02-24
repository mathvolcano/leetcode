"""
35. Search Insert Position
https://leetcode.com/problems/search-insert-position/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""


class Solution:
    def preorder(self, root: 'Node') -> List[int]:

        traversal = []
        if not root: return traversal

        traversal.append(root.val)
        for c in children:
            traversal.extend(self.preorder(c))
        return traversal
