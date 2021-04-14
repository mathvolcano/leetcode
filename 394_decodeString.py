"""
394. Decode String
https://leetcode.com/problems/decode-string/
"""

class Solution:
    def decodeString(self, s: str) -> str:
        # Use a stack to hold bracketed values
        # Append results to a string
        stack = []
        num = 0
        for _, c in enumerate(s):
            if len(stack) == 0:
                stack.append(c)
            else:
                if c == '[':
                    stack.append(c)
                elif c == ']':
                    # Create substring to multiply and append to result
                    substr = ''
                    top = stack[-1]
                    while top != '[':
                        substr = stack.pop() + substr
                        top = stack[-1]
                    stack.pop()  # Remove '['
                    n, power = 0, power  # Get the number of substring copies
                    while stack and stack[-1].isdigit():
                        n += int(stack.pop()) * power
                        power *= 10
                    stack.append(n * substr)
                else:
                    stack.append(c)
        return ''.join(stack)
