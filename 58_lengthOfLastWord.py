"""
58. Length of Last Word
https://leetcode.com/problems/length-of-last-word/
"""


class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        word_lst = s.strip().split(' ')
        return len(word_lst[-1])
