"""
116. Populating Next Right Pointers in Each Node
https://leetcode.com/problems/populating-next-right-pointers-in-each-node/
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
        if not root: return

        # Recursion
        if root is None or root.left is None:
            return root
        root.left.next = root.right
        if root.next:
            root.right.next = root.next.left
        self.connect(root.left)
        self.connect(root.right)
        return root

        # # BFS – traverses all elements of tree so O(n) time and O(n) space
        # lvl = [root]
        # while lvl:
        #     n = len(lvl)
        #     nxt_lvl = []
        #     for i,r in enumerate(lvl):
        #         if i + 1 == n:
        #             r.next = None
        #         else:
        #             r.next = lvl[i+1]
        #         if r.left:
        #             nxt_lvl.append(r.left)
        #         if r.right:
        #             nxt_lvl.append(r.right)
        #     lvl = nxt_lvl
        # return root