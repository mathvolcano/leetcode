"""
921. Minimum Add to Make Parentheses Valid
https://leetcode.com/problems/minimum-add-to-make-parentheses-valid/
"""

class Solution:
    def minAddToMakeValid(self, S: str) -> int:
        # Use a stack. O(n) time and space
        if len(S) == 0: return 0
        stack = []
        arr, prev = list(S), ''
        while arr:
            p = arr.pop(0)
            if prev == '(' and p == ')':
                stack.pop()
                prev = stack[-1] if stack else ''
            else:
                prev = p
                stack.append(p)
        return len(stack)
