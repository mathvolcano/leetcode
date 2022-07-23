"""
590. N-ary Tree Postorder Traversal
https://leetcode.com/problems/n-ary-tree-postorder-traversal/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children
"""

class Solution:
    def postorder(self, root: 'Node') -> List[int]:
        traversal = []
        if not root: return traversal

        for c in root.children:
            traversal.extend(self.postorder(c))
        traversal.append(root.val)
        return traversal