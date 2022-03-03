"""
290. Word Pattern
https://leetcode.com/problems/word-pattern/
"""

class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split(' ')
        surjective = len(pattern) == len(words)
        if not surjective:
            return False

        # Test for injective
        p_dic, w_dic = {}, {}
        for p, w in zip(pattern, words):
            if p not in p_dic:
                p_dic[p] = w
            elif p_dic[p] != w:
                return False
            if w not in w_dic:
                w_dic[w] = p
            elif w_dic[w] != p:
                return False

        return True
