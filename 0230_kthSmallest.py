"""
230. Kth Smallest Element in a BST
https://leetcode.com/problems/kth-smallest-element-in-a-bst/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:

        # Morris traversal
        # use left nodes of the leaf nodes to link to the inorder predecessor
        # O(1) space complexity, O(n) time
        # [1] Initialize current as root
        # while current is not null
        # [2] If current does not have a left child
        #    a. get current's data
        #    b. step right curr -> curr.right
        # [3] Else
        #    a. in current's left subtree make current the right child of the rightmost node
        #    b. Go to this left child, i.e., current = current->left
        curr = root
        while curr:
            if curr.left is None:
                k -= 1
                if k == 0: return curr.val
                curr = curr.right
            else:
                # [1]
                pre = curr.left  # previous
                while pre.right is not None and pre.right is not curr:
                    pre = pre.right
                if pre.right is None:
                    # Make current as right child of its inorder predecessor
                    pre.right = curr
                    curr = curr.left
                else:
                    # Revert the changes made
                    # in the 'if' part to restore the
                    # original tree. i.e., fix
                    # the right child of predecessor
                    pre.right = None
                    k -= 1
                    if k == 0: return curr.val
                    curr = curr.right

        # O(h) space complexity where h ~ log n is the height of the tree of n nodes (because of storing the stack memory)
        # [1] Preorder traverse the BST and increment a counter
        # [2] Once the count reaches k, return the node's value
    #     self.k = k
    #     self.res = None
    #     self.dfs(root)
    #     return self.res
    #
    # def dfs(self, root):
    #     if not root: return
    #     self.dfs(root.left)
    #     self.k -= 1
    #     if self.k == 0:
    #         self.res = root.val
    #         return
    #     self.dfs(root.right)

        # self.count = 0
        # return helper(root.right)

        # Brute Force
        # [1] Preorder traverse the BST and store as list. The resulting list will be ordered
        # by increasing values because of the BST property.
        # [2] return the k-th element
        # O(n) time complexity & O(n) space

        # def preorder(root):
        #     if not root: return []
        #     return preorder(root.left) + [root.val] + preorder(root.right)
        # traversal = preorder(root)
        # return traversal[k-1]
