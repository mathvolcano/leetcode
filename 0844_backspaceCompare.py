"""
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/
"""

class Solution:
    def backspaceCompare(self, str1: str, str2: str) -> bool:
        # 2 pointer, work backwards from string ends
        # [1] Initialize
        # . a. n1, n2 = len(str1), len(str2)
        # . b. i1, i2 = n1-1, n2 - 1
        # [2] while i1 >= 0 or i2 >= 0
        #  a. get the next valid indices of the strings (will define in [3])
        #  b. Case 1: if both indices are < 0, then we reached end of strings and return TRue
        #  c. Case 2: if only one of the indices < 0 then return False (strings are of unequal length)
        # . d. Case 3: str1[j1] != str2[j2], so return False
        # . f. decrement indices, i1 = j1-1, i2 = j2-2
        # [3] Define helper next_valid_char_index(s: String, i: int) -> int
        #  a.  initialize backspaces = 0
        #  b. while i >= 0, if s[i] == '#' then increment backspaces
        #  c. elif backspaces > 0 then decrement backspaces
        # . d. else: break
        # . f. decrement i
        # Time complexity O(n1 + n2) to traverse strings
        # Space O(1)
        n1, n2 = len(str1), len(str2)
        i1, i2 = n1 - 1, n2 - 1
        while i1 >= 0 or i2 >= 0:
            j1 = self.next_valid_char_index(str1, i1)
            j2 = self.next_valid_char_index(str2, i2)
            if j1 < 0 and j2 < 0:  # reached the end of both the strings
                return True
            if j1 < 0 or j2 < 0:  # reached the end of one of the strings, but not the other
                return False
            if str1[j1] != str2[j2]:  # check if the characters are equal
                return False
            i1 = j1 - 1
            i2 = j2 - 1
        return True

    def next_valid_char_index(self, s: str, i: int) -> int:
        backspaces = 0
        while i >= 0:
            if s[i] == '#':  # found a backspace character
                backspaces += 1
            elif backspaces > 0:  # a non-backspace character
                backspaces -= 1
            else:
                break
            i -= 1
        return i

    # def backspaceCompare(self, S: str, T: str) -> bool:
    # Stack helper method to construct word without backspaces and compare if they are equal
    # [1] Initialize stack s = []
    # [2] for c in word:
    # [3] if c = '#' and there is a stack: then pop last element of stack
    # [4] else, append to stack
    # [5] join characters in stack
    # [6] apply helper to both strings and compare equality
    # O(len(S) + len(T)) time complexity
    # O(len(S) + len(T)) space complexity worse case when no backspaces

    # def word_from_backspace(word):
    #     s = []  # stack
    #     for c in word:
    #         if (c == '#') and s:
    #             s.pop()
    #         elif c != '#':
    #             s.append(c)
    #     return ''.join(s)
    #
    # return word_from_backspace(S) == word_from_backspace(T)

