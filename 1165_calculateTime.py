"""
1165. Single-Row Keyboard
https://leetcode.com/problems/single-row-keyboard/
"""

class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        hash_map = {x[1]: x[0] for x in enumerate(keyboard)}
        res = hash_map[word[0]]
        for i in range(0, len(word)-1):
            res += abs(hash_map[word[i]] - hash_map[word[i+1]])
        return res
