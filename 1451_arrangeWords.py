"""
1451. Rearrange Words in a Sentence
https://leetcode.com/problems/rearrange-words-in-a-sentence/
"""
class Solution:
    def arrangeWords(self, text: str) -> str:

        # [1] Split sentence into a list of lowercase words
        #     "Leetcode is cool" -> ['leetcode', 'is', 'cool']
        # [2] Store relative positions of words - If two words have the same length, arrange them in their original order.
        #     ['leetcode', 'is', 'cool'] -> [('leetcode',0), ('is',1), ('cool',2)]
        # [3] Count lengths of words
        #     [('leetcode', 8), ('is', 2), ('cool', 4)]
        # [4] Sort by length ascending [('is', 2), ('cool', 4), ('leetcode', 8)]
        # [5] Concatenate and titlize: 'Is cool leetcode'
        # If s = len(text), then O(s) space worst case and O(slogs) worst case time complexity

        words = [(x[1], len(x[1]), x[0]) for x in enumerate(text.lower().split())]
        words.sort(key=lambda x: (x[1], x[2]))
        return ' '.join([w[0] for w in words]).capitalize()
