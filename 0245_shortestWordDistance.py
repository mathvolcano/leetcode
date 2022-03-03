"""
245. Shortest Word Distance III
https://leetcode.com/problems/shortest-word-distance-iii/
"""

class Solution:
    def shortestWordDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d = {}
        for i, w in enumerate(wordsDict):
            if w in d:
                d[w].append(i)
            else:
                d[w] = [i]
        diffs = [abs(x-y) for x in d[word1] for y in d[word2]]
        return min([x for x in diffs if x != 0])