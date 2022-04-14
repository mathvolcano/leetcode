"""
117. Populating Next Right Pointers in Each Node II
https://leetcode.com/problems/populating-next-right-pointers-in-each-node-ii/
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""

class Solution:
    def connect(self, root: 'Node') -> 'Node':

        # BFS/ Level order traversal
        # [1] Initialize a queue, q q = [root]
        # [2] While q
        #  a. set next level to []
        #  b. Updata all nodes' next values in q to point to next node
        #  c. Add children to next level
        #  d. update q to be next level
        # [3] return root
        # O(n) time to traverse all nodes and O(n) space to store bottom level.
        if not root: return None
        q = [root]
        while q:
            lvl = []
            for i, n in enumerate(q[1:], start=1):
                q[i-1].next = n
            for n in q:
                if n.left: lvl.append(n.left)
                if n.right: lvl.append(n.right)
            q = lvl
        return root

