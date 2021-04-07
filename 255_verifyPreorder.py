"""
255. Verify Preorder Sequence in Binary Search Tree
https://leetcode.com/problems/verify-preorder-sequence-in-binary-search-tree/
"""

class Solution:
    def verifyPreorder(self, preorder: List[int]) -> bool:
        # Use a stack to track the lowest values of the left branches
        # If the value is ever less than the lowest value in the stack
        # then the value cannot be in a right branch.
        stack = []
        low = float('-inf')
        for val in preorder:
            if val < low:
                return False
            while stack and val > stack[-1]:
                low = stack.pop()
            stack.append(val)

        return True