"""
3. Longest Substring Without Repeating Characters
https://leetcode.com/problems/longest-substring-without-repeating-characters/
"""

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:

        # 2 pointer / Sliding Window

        # 0. Handle trivial cases when len(s) <= 1 to ensure pointers set
        # 1. Initialize 2 pointers, left l=0 & right r = 1, and a result counter res to track longest
        #    substring length
        # 2. Initialize a hash set of characters in the longest substring found
        # 3a. Iterating through s if the r is a new char not in the hash set then add 1 to r
        #     and add char to hash set.
        # 3b. Else, increase l and pop the s[l] from the hash set

        # O(len(s)) time complexity because we must iterate through the whole string s
        # O(len(s)) space complexity (worst case) for storing at most all s in the hash set.

        if len(s) <= 1: return len(s)

        l, r, res = 0, 0, 0
        hs = set()
        while r < len(s):
            if s[r] not in hs:
                hs.add(s[r])
                r += 1
            else:
                hs.remove(s[l])
                l += 1
            res = max(res, len(hs))
        return res
