"""
501. Find Mode in Binary Search Tree
https://leetcode.com/problems/find-mode-in-binary-search-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findMode(self, root: TreeNode) -> List[int]:

        self.prev = None
        self.max_count = 0
        self.modes = []
        self.cur_count = 0

        # Perform an inorder recursion
        # [1] track the previous node, the modes, max_count and the count of mode
        # [2] If the current node has the same value as the last node then increment current count
        #     else reset count
        # [3] Update the modes and max count tracking based on the current count and value
        # [4] Recurse in order.
        # Time Complexity – O(n) for traversing full tree
        # Space Complexity – Space O(1) space (best) and O(n) worst (all modes the same)

        def traverse(root):
            """Perform an inorder traversal to get the modes."""
            if not root: return

            traverse(root.left)

            ### Process the current node

            # Set previous and update the current count
            if self.prev and self.prev.val == root.val:
                self.cur_count += 1
            else:
                self.cur_count = 0
            self.prev = root

            # Update the max counts and modes
            if self.cur_count > self.max_count:
                self.max_count = self.cur_count
                self.modes = [root.val]
            elif self.cur_count == self.max_count:
                self.modes.append(root.val)

            traverse(root.right)
        traverse(root)
        return self.modes

        # Brute Force – Doesn't use BST property
        # [1] Perform in-order traversal
        # [2] count the elements in the traversal
        # [3] return the largest
        # def inorder(root):
        #     if not root: return []
        #     return inorder(root.left) + [root.val] + inorder(root.right)
        # from collections import Counter
        # traversal = inorder(root)
        # counts = Counter(traversal)
        # max_count = max(v for _, v in counts.items())
        # return [k for k,v in counts.items() if v == max_count]
