"""
844. Backspace String Compare
https://leetcode.com/problems/backspace-string-compare/
"""


def backspaceCompare(S, T):
    def word_from_backspace(word):
        stack = []
        for c in word:
            if (c == '#') and (len(stack) > 0):
                stack.pop()
            elif c != '#':
                stack.append(c)
        return ''.join(stack)

    return word_from_backspace(S) == word_from_backspace(T)
