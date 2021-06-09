"""
95. Unique Binary Search Trees II
https://leetcode.com/problems/unique-binary-search-trees-ii/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:

        # Recursion
        # [1] Create a helper function for recursion that generates new tree nodes from list of values.
        # [2] for each value in range(n) set value to root then append to it results of recursing
        # on remaining values
        # Time complexity is O(3^n) because we have 3 branches (left, center, right)
        # and depth n.
        # Space complexity is O(3^n) because we have to store all results.

        def helper(s, e):  # start, end
            return [TreeNode(val=i, left=l, right=r)
                    for i in range(s, e + 1)
                    for l in helper(s, i - 1)
                    for r in helper(i + 1, e)
                    ] or [None]

        return helper(1, n)
