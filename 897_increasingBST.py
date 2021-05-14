"""
897. Increasing Order Search Tree
https://leetcode.com/problems/increasing-order-search-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def increasingBST(self, root: TreeNode) -> TreeNode:

        # Create a new tree using a depth-first search storing left nodes (decreasing in values) in a stack tracking the traversal with trav
        # [1] If there's a left node traverse left adding the nodes to stack
        # [2] Once we reach a node without a left node, pop stack and set head and tail to the node
        # [3] Append root to the right of tail and update tail to next right
        # [4] Append root.right to the right of tail
        # [5] return head
        # O(n) time to traverse tree, O(h) additional space to store nodes in stack
        if not root: return

        stack = []
        trav = root
        head, tail = None, None
        while trav or stack:
            # [1]
            if trav:  # [1]
                stack.append(trav)
                trav = trav.left
            else:
                cur = stack.pop()
                if not tail:  # [2]
                    head = TreeNode(cur.val)
                    head.left = None
                    tail = head
                else:  # [3]
                    nxt = TreeNode(val=cur.val)
                    tail.right = nxt
                    tail.left = None
                    tail = tail.right
                trav = cur.right  # [4]
        return head  # [5]

        # Brute Force
        # [1] Get in order traversal array
        # [2] Construct a new tree with all nodes to the right
        # O(n) time and space complexity
#         def inorder(root):
#             if not root: return []
#             return inorder(root.left) + [root.val] + inorder(root.right)

#         traversal = inorder(root)
#         head = res = TreeNode(val=None)
#         for t in traversal:
#             res.right = TreeNode(val=t)
#             res = res.right
#         return head.right
