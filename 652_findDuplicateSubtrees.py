"""
652. Find Duplicate Subtrees
https://leetcode.com/problems/find-duplicate-subtrees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: TreeNode) -> List[TreeNode]:

        # Note the postorder traversal a node's children uniquely serializes the tree.
        # [1] Encode each node as node value and Post order traversal each child of node
        # [2] Store encoding in a hash_table
        # O(n) average time and O(log n) worst case
        # O(n) space for hash map O(n^2) worst case

        from collections import Counter
        res = []
        hash_map = Counter()

        def postorder(node):
            if not node:
                return None

            node_key = (node.val, postorder(node.left), postorder(node.right))
            hash_map[node_key] += 1

            if hash_map[node_key] == 2:
                res.append(node)
            return node_key

        postorder(root)
        return res
