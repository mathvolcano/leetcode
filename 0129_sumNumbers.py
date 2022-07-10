"""
129. Sum Root to Leaf Numbers
https://leetcode.com/problems/sum-root-to-leaf-numbers/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:

        # Morris Preorder Traversal
        # O(n) time and O(1) space
        r = c = 0  # root_to_leaf, current number
        while root:
            # if there is a leaf child then compute its predecessor p
            # If there is no link p.right = too --> set it
            # if there is a link p.right = root --> break it
            if root.left:
                # predecessor node is 1 step to the left and then to the right till you can't.
                p = root.left
                steps = 1
                while p.right and p.right is not root:
                    p = p.right
                    steps += 1

                # Set link p.right = root and go to explore the left subtree
                if not p.right:
                    c = c *10 + root.val
                    p.right = root
                    root = root.left
                # Break the link predecessor.right = root
                # Once the link is broken,
                # it's time to change subtree and go to the right
                else:
                    if not p.left:
                        r += c
                    # This part of the tree is explored: backtrack
                    for _ in range(steps):
                        c //= 10
                    p.right = None
                    root = root.right
            else:  # if there is no left child just go right
                c = c*10 + root.val
                if not root.right:
                    r += c
                root = root.right
        return r

        # DFS
        # [1] Initialize sums res = []. # path_sums. Define a helper helper(root, ps)
        # [2] In helper: multiply ps by 10 and add root.val
        # [3] If root is leaf append path sum to result
        # [3] Recurse on children if children
        # [4] return sum(res)
        # Complexity: n = number of nodes of root
        # Time: O(n) for at most n/2 paths, space O(lg n) = O(n) for recursive call stack & storing paths
        # if not root: return 0
        # self.res = 0
        # def helper(root, ps):
        #     if not root: return
        #     ps = 10*ps + root.val
        #     if not root.left and not root.right:
        #         self.res += ps
        #     if root.left : helper(root.left , ps)
        #     if root.right: helper(root.right, ps)
        # helper(root, 0)
        # return self.res