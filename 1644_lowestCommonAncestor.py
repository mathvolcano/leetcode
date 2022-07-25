"""
1644. Lowest Common Ancestor of a Binary Tree II
https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        # [1] Perform a dfs
        # [2] Return a null and count 0 in leaf and chiled & count 1 if found.
        # O(n) time complexity, O(1) space complexity
        self.res = None

        def dfs(root, p, q):
            if not root: return 0

            l_res = dfs(root.left , p, q)
            r_res = dfs(root.right, p, q)
            cur = root == p or root == q  # 1 if root is p or q
            if cur + l_res + r_res >= 2:
                self.res = root
            return cur or l_res or r_res

        dfs(root, p, q)
        return self.res

#         # [1] check if p and q are in root by doing an inorder traversal
#         # [2] if so then perform an lca from binary tree 1
#         # [2.5] lca by starting from root to see if root is p or q. Perform on root.left and root.right
#         # if root.left and root.right are an ancestor to p or q
#         # O(n) time complexity for full traversal, O(n) space complexity for storing the inorder list.

#         def inorder(r):
#             if not r: return []
#             return inorder(r.left) + [r] + inorder(r.right)

#         traversal = inorder(root)
#         pi, qi = -1, -1
#         for i, r in enumerate(traversal):
#             # print('i pi qi', i, pi, qi)
#             if r.val == p.val:
#                 pi = i
#             if r.val == q.val:
#                 qi = i
#             if qi >= 0 and pi >= 0:
#                 return self.lca1(root, p, q)
#         # print('pi qi', pi, qi)

#     def lca1(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
#         if not root or p == root or q == root:
#             return root
#         left = self.lca1(root.left, p, q)
#         right = self.lca1(root.right, p, q)
#         if left and right:
#             return root
#         return left if left else right