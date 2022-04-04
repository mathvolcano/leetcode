"""
545. Boundary of Binary Tree
https://leetcode.com/problems/boundary-of-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        # DFS using a preorder traversal
        # [1] Preorder search the tree initialize result res with root
        # [2] Add left boundary to result, then leaves then right
        # [3] To get left boundary check if node is root or leaf and return none
        #  a) else add value to left
        #  b) then recurse on left node if there is one, else recurse on right.
        # [4] get leaves by checking if not left and not right or root and adding to result
        #     else, recurse
        # [4] Right boundary is similar to left
        # O(n) time complexity and O(n) space complexity because # of nodes in leaves is ~ n/2 for binary tree.
        if not root: return []
        res = [root.val]

        def get_l(root):
            if not root or not root.left and not root.right: return
            res.append(root.val)
            if root.left:
                get_l(root.left)
            else:
                get_l(root.right)

        def get_r(root):
            if not root or not root.left and not root.right: return
            if root.right:
                get_r(root.right)
            else:
                get_r(root.left)
            res.append(root.val)

        def leaves(node):
            if not node: return
            if not node.left and not node.right and node != root:
                res.append(node.val)
            leaves(node.left)
            leaves(node.right)

        get_l(root.left)
        leaves(root)
        get_r(root.right)
        return res
