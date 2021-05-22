"""
1805. Number of Different Integers in a String
https://leetcode.com/problems/number-of-different-integers-in-a-string/
"""

class Solution:
    def numDifferentIntegers(self, word: str) -> int:
        # [1] Iterate through the string an replace all non numeric text with space ' '
        # [2] split on space
        # [3] Get unique integers in the new list and return length
        # O(len(word)) time complexity and O(word) space
        new_s = ''.join([c if c.isdigit() else ' ' for c in word])
        s_split = new_s.split(' ')
        return len(set(int(s) for s in s_split if len(s) > 0))
