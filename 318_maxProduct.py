"""
318. Maximum Product of Word Lengths
https://leetcode.com/problems/maximum-product-of-word-lengths/
"""

class Solution:
    def maxProduct(self, words: List[str]) -> int:

        # Hash table of bitwise encoding of words
        # [1] Create a hash table of each word to its bitwise encoding of letters
        # [2] Iterate through all pairs of words and check that the bitwise and &
        # is 0
        # [3] If so then update a result variable and return it.
        # O(n^2 + n*w) time for n the number of words and w the max length of words
        # O(1) space
        import itertools
        from collections import defaultdict

        if len(words) <= 1: return 0

        word_to_bits = defaultdict(int)
        for w in words:
            for c in w:
                word_to_bits[w] |= 1 << ord(c) - ord('a')

        res = 0
        for w1, w2 in itertools.combinations(words, 2):
            prod = len(w1) * len(w2)
            if (word_to_bits[w1] & word_to_bits[w2] == 0) and res < prod:
                res = prod
        return res

        # Brute Force O(n^2*w) where n = len(words) and w is the max word length
        # Space O(1)
        # res = 0
        # n = len(words)
        # for i in range(n):
        #     for j in range(i+1, n):
        #         if not set(words[i]).intersection(set(words[j])):
        #             res = max(res, len(words[i]) * len(words[j]))
        # return res