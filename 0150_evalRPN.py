"""
150. Evaluate Reverse Polish Notation
https://leetcode.com/problems/evaluate-reverse-polish-notation/
"""

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Stack
        # [1] For any integer append to stack
        # [2] If we encounter a token that is an operation pop the last 2 values in the
        # stack and reduce according to operation
        # [3] append resulting value to stack
        # [4] return last value of stack.

        stack = []
        ops = ['+', '-', '*', '/']

        for idx, token in enumerate(tokens):
            if token not in ops:
                stack.append(int(token))
            else:
                r = stack.pop()  # right
                l = stack.pop()  # left
                if token == '+':
                    stack.append(l + r)
                if token == '-':
                    stack.append(l - r)
                if token == '*':
                    stack.append(l * r)
                if token == '/':
                    if l * r < 0:
                        stack.append(-((-l)//r))
                    else:
                        stack.append(l//r)
        return stack.pop()