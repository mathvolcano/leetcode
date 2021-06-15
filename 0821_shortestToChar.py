"""
821. Shortest Distance to a Character
https://leetcode.com/problems/shortest-distance-to-a-character/
"""

class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:

        # [1] Iterate from the left and track the distance from the character to the leftmost index of the
        # last target characters - store in array
        # [2] Iterate from the right and track the distance from the character to the rightmost index of the
        # last target characters - store in array
        # [3] Set each index to be the min value of the corresponding indexes

        n = len(s)
        res = [None] * n

        # Left
        last_idx = float('inf')
        for i, l in enumerate(s):
            if l == c: last_idx = i
            res[i] = abs(last_idx - i)

        # Right
        last_idx = float('inf')
        for i, l in reversed(list(enumerate(s))):
            if l == c: last_idx = i
            res[i] = min(res[i], abs(last_idx - i))

        return res
