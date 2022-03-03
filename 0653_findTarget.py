"""
653. Two Sum IV - Input is a BST
https://leetcode.com/problems/two-sum-iv-input-is-a-bst/
"""


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: TreeNode, k: int) -> bool:

        # Use a queue and hash_set
        # O(n) time and space
        if not root: return False
        hash_set = set()
        q = [root]  # queue
        while q:
            r = q.pop(0)
            diff = k - r.val
            if diff in hash_set:
                return True
            else:
                hash_set.add(r.val)
                if r.left:
                    q.append(r.left)
                if r.right:
                    q.append(r.right)

        # O(n) time and space
        # In order traversal
        def inorder(root):
            if not root: return []
            return inorder(root.left) + [root.val] + inorder(root.right)

        traversal = inorder(root)
        l, r, = 0, len(traversal) - 1
        while l < r:
            cur = traversal[l] + traversal[r]
            if cur == k:
                return True
            elif cur > k:
                r -= 1
            else:
                l += 1
        return False
