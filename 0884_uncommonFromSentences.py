"""
884. Uncommon Words from Two Sentences
https://leetcode.com/problems/uncommon-words-from-two-sentences/
"""

class Solution:
    def uncommonFromSentences(self, A: str, B: str) -> List[str]:
        from collections import Counter
        C = A + ' ' + B
        counts = Counter(C.split(' '))
        return [x for x in counts if counts[x] == 1]
