"""
1650. Lowest Common Ancestor of a Binary Tree III
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-iii/
"""

"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        # [1]. Check the base cases.
        # [2]. Traverse the path from q to the root.
        # [3]. Traverse the path from p to root.
        # [4]. Take the first common point of p's path that is in q's
        # Time and space complexity O(h)

        # Base cases
        if p == q: return p

        q_path = [q]
        while q.parent:
            q_path.append(q.parent)
            q = q.parent

        p_path = [p]
        while p.parent:
            p_path.append(p.parent)
            p = p.parent

        while p_path:
            pn = p_path.pop(0)
            if pn in q_path:
                return pn

        # Return root
        return q.path[-1]


