"""
426. Convert Binary Search Tree to Sorted Doubly Linked List
https://leetcode.com/problems/convert-binary-search-tree-to-sorted-doubly-linked-list/
"""
"""
# Definition for a Node.
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution:
    def treeToDoublyList(self, root: 'Optional[Node]') -> 'Optional[Node]':
        # O(1) memory
        # [0] Initialize a a previous node and set to a dummy node
        # [1] Inorder traverse the tree
        #. a. set left to previous and right of previous to node
        #  b. update previous to node
        # [2] Link last element with first element
        #.    (self.prev is now last so set right to dummy.right)
        # return dummy.right
        # O(n) time and O(1) space.
        def inorder(root):
            if not root: return
            inorder(root.left)
            self.prev.right = root
            root.left = self.prev
            self.prev = root
            inorder(root.right)

        if not root: return
        self.prev = dummy = Node(-1)
        inorder(root)
        # Link 1st & last elements
        self.prev.right = dummy.right
        dummy.right.left = self.prev
        return dummy.right


        # [1] get a list, l=[] of the nodes via an inorder traversal
        # [2] iterate through list: updated each node's right to be the next element
        # and each node's left to be the prior node
        # [3] link l[-1].right = l[0] and l[0].left = l[-1]
        # Return root
        # O(n) time for inorder traversal & iterating through list
        # O(n) additional space to store root as a list
#         if not root: return

#         def inorder(root):
#             if not root: return []
#             return inorder(root.left) + [root] + inorder(root.right)

#         l = inorder(root)
#         for i, n in enumerate(l):
#             if i == 0:
#                 n.left = l[-1]
#                 n.right = l[0] if len(l) == 1 else l[1]
#             elif i == len(l) - 1:
#                 n.right = l[0]
#                 n.left = l[-2]
#             else:
#                 n.left = l[i-1]
#                 n.right = l[i+1]
#         return l[0]
