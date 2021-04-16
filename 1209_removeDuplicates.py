"""
1209. Remove All Adjacent Duplicates in String II
https://leetcode.com/problems/remove-all-adjacent-duplicates-in-string-ii/
"""

class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for _, c in enumerate(s):
            if not stack:
                stack.append((c, 1))  # Append character and count
            else:
                top_c, top_count = stack[-1]
                if c == top_c and top_count + 1 == k:
                    stack = stack[:len(stack) - (k - 1)]
                elif c == top_c and top_count + 1 < k:
                    stack.append((c, top_count + 1))
                else:  # c != top_c:
                    stack.append((c,1))
        return ''.join([c for c, _ in stack])
