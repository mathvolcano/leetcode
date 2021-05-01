"""
1249. Minimum Remove to Make Valid Parentheses
https://leetcode.com/problems/minimum-remove-to-make-valid-parentheses/
"""

class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        # Iterate through s, add parentheses indices to stack. pop when valid
        # Store deletes in a list
        # Remove deletes
        stack, deletes = [], []
        for i, c in enumerate(s):
            if c.isalpha():
                continue
            if c == '(':
                stack.append(i)
            elif not stack:
                deletes.append(i)
            else:  # c == ')'
                stack.pop()
        deletes += stack
        return ''.join([c for i,c in enumerate(s) if i not in deletes])

        # Use a stack - hoping to get an O(n) time and space complexity
        arr = list(s)
        # track count of parentheses were '(' we +1 and ')' -1.
        # When count goes negative we pop ')'
        # If count is positive after we traverse string we pop last count of '('
        stack, count = [], 0
        for c in s:
            if c == '(':
                count += 1
                stack.append(c)
            elif c == ')':
                if count == 0:  # Skip adding ')'
                    continue
                else:
                    count -= 1
                    stack.append(c)
            elif c.isalpha():
                stack.append(c)

        # Delete extra left parentheses
        m = len(stack)
        deletes = []
        if count > 0:
            for j in range(m-1, -1, -1):
                if count == 0: break
                if stack[j] == '(':
                    deletes.append(j)
                    count -= 1

        res = [c for i,c in enumerate(stack) if i not in deletes]
        return ''.join(res)

