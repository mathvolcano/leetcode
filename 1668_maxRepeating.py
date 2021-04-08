"""
1668. Maximum Repeating Substring
https://leetcode.com/problems/maximum-repeating-substring/
"""

class Solution:
    def maxRepeating(self, sequence: str, word: str) -> int:
        # O(n) space, O(n) time because we only have to iterate through seq once.
        k = 0
        n = len(word)
        if n > len(sequence): return 0

        l, r = 0, n
        pattern = word
        while r <= len(sequence):
            subseq = sequence[l:r]
            if subseq == pattern:
                pattern += word
                r += n
                k += 1
            else:
                l += 1
                r += 1
        return k
