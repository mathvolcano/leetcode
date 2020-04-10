"""
1047. Remove All Adjacent Duplicates In String
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string/
"""


class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        l = len(stack)
        for s in S:
            if (l > 0) and (stack[-1] == s):
                stack.pop()
                l -= 1
            else:
                stack.append(s)
                l += 1
        return ''.join(stack)
