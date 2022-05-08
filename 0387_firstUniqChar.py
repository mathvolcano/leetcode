"""
387. First Unique Character in a String
https://leetcode.com/problems/first-unique-character-in-a-string/
"""

class Solution:
    def firstUniqChar(self, s: str) -> int:
        # One-pass, use 2 hashmaps
        # O(n) time and O(1) space
        from collections import defaultdict
        h, j = {}, {}
        res = [i for i in range(len(s))]
        for i,v in enumerate(s):
            h[v] = h.get(v, 0) + 1
            if h[v] > 1:
                res[j[v]] = -1
                res[i] = -1
            j[v] = i
        for r in res:
            if r >= 0:
                return r
        return -1


        # Hashmap
        # [1] Initialize hashmap, counts, and count character frequency
        # [2] iterate i,c through enumerate(s)
        # [3] if counts[c] == 1 then return i
        # O(len(s)) time complexity and at most O(m) <= O(n) space, m the unique chars of s, or O(1) space if there are a finite number of chars.
        # from collections import Counter
        # counts = Counter(s)
        # for i,c in enumerate(s):
        #     if counts[c] == 1:
        #         return i
        # return -1
