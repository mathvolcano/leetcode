"""
1160. Find Words That Can Be Formed by Characters
https://leetcode.com/problems/find-words-that-can-be-formed-by-characters/
"""

class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        from collections import Counter
        counts = Counter(chars)
        res = 0
        for w in words:
            w_counts = Counter(w)
            if counts & w_counts == w_counts:
                res += len(w)
        return res