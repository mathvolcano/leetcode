"""
244. Shortest Word Distance II
https://leetcode.com/problems/shortest-word-distance-ii/
"""

class WordDistance:

    def __init__(self, wordsDict: List[str]):
        self.query = wordsDict
        self.word_to_indices = self.get_word_indices()

    def get_word_indices(self):
        d = {}
        for i, w in enumerate(self.query):
            if w in d:
                d[w].append(i)
            else:
                d[w] = [i]
        return d

    def shortest(self, word1: str, word2: str) -> int:
        indices1 = self.word_to_indices[word1]
        indices2 = self.word_to_indices[word2]
        return min([abs(x-y) for x in indices1 for y in indices2])



# Your WordDistance object will be instantiated and called as such:
# obj = WordDistance(wordsDict)
# param_1 = obj.shortest(word1,word2)