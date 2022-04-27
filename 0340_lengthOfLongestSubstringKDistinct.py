"""
340. Longest Substring with At Most K Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-k-distinct-characters/
"""
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # Sliding window with hashmap
        # [0] Initialize result variable res = 0 , left window end, l = 0
        #     and hashmap, h = {}, of char: freq
        # [1] Iterate right window r through range(len(s)):
        #  a. increase letter count
        # [2] while len(h) > k
        #  a. increase
        #  b. & update h counts
        #  b. update res = max(res, r - l + 1)

        # O(n) time complexity
        # O(k) space complexity (worst case)
        if k == 0: return 0
        l, res = 0, 0
        h = {}
        for r in range(len(s)):
            c = s[r]
            h[c] = h.get(c, 0) + 1

            while len(h) > k:
                c = s[l]
                l += 1
                h[c] -= 1
                if h[c] == 0:
                    del h[c]
            res = max(res, r - l + 1)
        return res