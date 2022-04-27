"""
159. Longest Substring with At Most Two Distinct Characters
https://leetcode.com/problems/longest-substring-with-at-most-two-distinct-characters/
"""
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # Sliding window with hashmap
        # [1] initialize variables
        #. a. hashmap, h= {}, to store char: freq
        #. b. res = 0 the length of the longest substring
        #. a. l =0 the left pointer of window start
        # [2] iterate through range(len(s))
        #. a. update h with s[r]
        #. b. while len(h) > 2 increment up l and update h
        #. b. update res = max(res, r - l + 1)
        # if n = len(s) then O(n) time complexity to traverse s twice
        # O(1) worst case to store at most 3 kvs in h.
        k = 2
        l, res = 0, 0
        h = {}
        for r in range(len(s)):
            c = s[r]
            h[c] = h.get(c, 0) + 1

            while len(h) > k:
                c = s[l]
                h[c] -= 1
                if h[c] == 0:
                    del h[c]
                l += 1

            res = max(res, r - l +1)
        return res
