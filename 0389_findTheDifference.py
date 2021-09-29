"""
389. Find the Difference
https://leetcode.com/problems/find-the-difference/
"""

class Solution:
    def findTheDifference(self, s: str, t: str) -> str:

        # 1 Create a hashmap of the counts of each letter in s
        # 2 Check for each char in t if it is in the hashmap. If not return
        # 3 If the char is in the dic then decrement the count in hm
        # 4 Iterate through the hm and return the char that has nonzero value.
        # O(len(s)) time and space because len(t) = len(s) + 1.

        from collections import defaultdict
        hm = defaultdict(int)
        for c in s:
            hm[c] += 1
        for c in t:
            if c not in hm:
                return c
            hm[c] -= 1
        for k,v in hm.items():
            if v != 0:
                return k
