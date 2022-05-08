"""
438. Find All Anagrams in a String
https://leetcode.com/problems/find-all-anagrams-in-a-string/
"""

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        # Sliding window with array hashtable
        # [0] Initialize
        #.    a) Initialize 26 char zero arrays, ls & lp
        #.    b) populate lp's char counts by counts in p
        #.    c) initialize result array res = []
        # [1] Traverse enumerate(s)
        #.    a) add char counts of s to ls
        #.    b) if i >= len(p) then subtract last char's count s[i-np] from ls's char position
        #.    c) check if lp == ls and if so then append index of s (i - np + 1) to res
        # Complexity: let ns = len(s) and np = len(p)
        # Time: O(ns + np) to create hashtable lp and traverse s
        # Space: O(1) if there are 26 chars.
        ls = [0]*26
        lp = [0]*26

        for x in p:
            lp[ord(x) - ord('a')] += 1

        res = []
        np = len(p)
        for i, v in enumerate(s):
            ls[ord(v) - ord('a')] += 1
            if i >= np:
                ls[ord(s[i-np]) - ord('a')] -= 1
            if lp == ls:
                res.append(i-np+1)
        return res
