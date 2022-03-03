"""
890. Find and Replace Pattern
https://leetcode.com/problems/find-and-replace-pattern/
"""

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:

        # Iterate through the list of words - for each word
        # [1] (surjective) check that the length matches the pattern
        # [2] (injective) check that a mapping of letters is 1-1:
        # [2a] create a dict that maps pattern letters to word letters
        # and a dict that maps word letters to pattern letters
        # Time complexity O(w + p) and space complexity is O(w+p)

        def injective(pattern, word):
            p_dic, w_dic = {}, {}
            for p, w in zip(pattern, word):
                if p not in p_dic:
                    p_dic[p] = w
                elif p_dic[p] != w:
                    return False
                if w not in w_dic:
                    w_dic[w] = p
                elif w_dic[w] != p:
                    return False
            return True

        res = []
        for w in words:
            if len(w) != len(pattern):
                continue
            if injective(pattern, w):
                res.append(w)
        return res
