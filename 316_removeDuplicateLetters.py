"""
316. Remove Duplicate Letters
https://leetcode.com/problems/remove-duplicate-letters/
"""

class Solution:
    def removeDuplicateLetters(self, s: str) -> str:

        # Use a stack to track whether the characters are lexi ordered
        # Use a hash set to track whether characters was seen or not
        # [1] for each character get the last index that a character appears in it
        # [2] For each c in s we look through the stack and pop all chars that
        # come after c lexicographically if there is another occurence of the character
        # after c.
        # [3] Add c to the stack
        # O(n) space for stack and seen, O(n) time complexity to iterate through array
        stack = []  # stack
        seen = set()
        last = {c: i for i, c in enumerate(s)}
        for i, c in enumerate(s):
            if c not in seen:
                while stack and c < stack[-1] and i < last[stack[-1]]:
                    seen.remove(stack.pop())
                seen.add(c)
                stack.append(c)
        return ''.join(stack)

        # Brute Force (Pythonic)
#         # O(n^2) to check for duplicates
#         uniques = list(set(s))
#         uniques.sort()
#         return ''.join(uniques)
