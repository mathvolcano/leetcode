"""
243. Shortest Word Distance
https://leetcode.com/problems/shortest-word-distance/
"""

class Solution:
    def shortestDistance(self, wordsDict: List[str], word1: str, word2: str) -> int:
        d = {}
        for i, w in enumerate(wordsDict):
            if w in d:
                d[w].append(i)
            else:
                d[w] = [i]
        return min([abs(x-y) for x in d[word1] for y in d[word2]])
