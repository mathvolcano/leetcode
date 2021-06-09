"""
1624. Largest Substring Between Two Equal Characters
https://leetcode.com/problems/largest-substring-between-two-equal-characters/
"""

class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:

        # Hash Table
        # [1] Iterate through the list and store the positions in a hash map
        # [2] when the hash_map has value of length 1 get the length between the current and the previous positions and update result.
        # [3] Add current position to hash_map and continue
        # Time & space complexity O(len(s))

        from collections import defaultdict
        res, h = -1, defaultdict(list)
        for i, c in enumerate(s):
            if len(h[c]) == 0:
                h[c].append(i)
                continue
            elif len(h[c]) == 1:
                h[c].append(i)
            else:  # len(h[c]) == 2
                h[c][1] = i
            res = max(res, h[c][1] - h[c][0] - 1)
        return res
