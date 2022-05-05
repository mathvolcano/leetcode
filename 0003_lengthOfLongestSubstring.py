"""
424. Longest Repeating Character Replacement
https://leetcode.com/problems/longest-repeating-character-replacement/
"""

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # Sliding window with hashmap
        # [1] Initialize
        #. a. hashmap, h = {}, to store chars: left most index of the
        #. b. result variable, res = 0, to track result
        #. c. m = 0, max repeat letter count
        #  c. left window pointer l = 0
        # [2] Iterate right window r through range(len(s))
        #  a. Update h with next char
        #. [3] if r - l +1 -m > k then update h and increment l
        #  b. update res = max(res, r - l + 1)
        # O(len(s)) time and O(1) space (if max 26 letters), otherwise O(k) space

        h, l, m, res = {}, 0, 0, 0
        for r in range(len(s)):
            c = s[r]
            h[c] = h.get(c, 0) + 1
            m = max(m, h[c])
            if (r -l + 1 - m) > k:
                c = s[l]
                h[c] -= 1
                if h[c] == 0:
                    del h[c]
                l += 1
            res = max(res, r-l+1)
        return res
