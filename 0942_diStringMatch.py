"""
942. DI String Match
https://leetcode.com/problems/di-string-match/
"""

class Solution:
    def diStringMatch(self, s: str) -> List[int]:
        # only need relative changes in values & not exact
        # So encode each I with a low value and each D with a high value & work inward.
        # O(n) time and space
        l, h = 0, len(s)  # low, high
        ans = []
        for c in s:
            if c == "I":
                ans.append(l)
                l += 1
            else:  # c == 'D'
                ans.append(h)
                h -= 1
        return ans + [l]

#         # Brute Force, O(n!) because we have to form all permutations first
#         from itertools import permutations
#         n = len(s) + 1
#         nums = list(range(n))

#         perms = permutations(nums, n)
#         for p in perms:
#             sp = ''
#             for i in range(1, n):
#                 if p[i] > p[i-1]:
#                     sp += 'I'
#                 else:  # p[i] < p[i-1]
#                     sp += 'D'
#             if sp == s:
#                 return p