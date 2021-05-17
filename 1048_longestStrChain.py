"""
1048. Longest String Chain
https://leetcode.com/problems/longest-string-chain/
"""

class Solution:
    def longestStrChain(self, words: List[str]) -> int:

        # DP with a hash_map
        # [1] Sort the words in increasing length
        # [2] For a given word compute the subwords by deleting 1 char
        # [3] compute the longest chain for the word by looking up in hash_table and words
        # to confirm a) if subword is valid in words and b) if valid, what is the longest chain up to that word
        # [4] store length of chain in hash_map.
        # Time complexity is O(max(wlog(w), w*len(w))). Space complexity is O(w)
        if not words: return 1

        words.sort(key=len)

        cache = {}
        res = 0
        for w in words:
            longest = 0
            for i in range(len(w)):
                sw = w[0:i] + w[i+1:]  #sub-word
                longest = max(longest, cache.get(sw, 0) + 1)
            cache[w] = longest
            res = max(res, longest)
        return res
