"""
408. Valid Word Abbreviation
https://leetcode.com/problems/valid-word-abbreviation/
"""
class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:

        # 2 pointer – Cleaner
        # O(max(n,m)) time and O(1) space
        i, j = 0, 0
        n, m = len(word), len(abbr)

        while i < n and j < m:
            # Case 1: equals
            if word[i] == abbr[j]:
                i += 1
                j += 1
                continue

            # Case 2: abbr[j] is a letter and != word[i] or abbr[j] is leading 0
            if not abbr[j].isnumeric() or abbr[j] == '0':
                return False

            # Case 3: get the full number & increase pointer by that amount
            start = j
            while j < m and abbr[j].isnumeric():
                j += 1
            num = int(abbr[start:j])
            i += num

        # Check that lengths are equal.
        return i == n and j == m

        # [1] Convert abbr to a list of letters & abbr numbers, lst
        # [2] Set pointer p = 0 to check value of word
        # [2] Iterate through range(len(lst)):
        # [3] for each letter of lst, check if equals to current pointer of word and increment p
        # [4] for number, increase p by that number
        # O(max(len(word), len(abbr))) time and O(len(abbr)) space worst case
#         lst = []
#         prev = ''
#         for a in abbr:
#             if a.isdigit():
#                 prev += a
#             elif a.isalpha() and prev:
#                 # Remove invalids
#                 if prev[0] == '0':
#                     return False
#                 lst.append(int(prev))
#                 lst.append(a)
#                 prev = ''
#             else:  # isalpha & no prev
#                 lst.append(a)
#         if prev:
#             if prev[0] == '0':
#                 return False
#             lst.append(int(prev))
#         # print(lst)

#         p = 0
#         for i in range(len(lst)):
#             if p >= len(word):
#                 return False
#             v = lst[i]
#             # print('i, v', i, v)
#             if str(v).isalpha():
#                 if v != word[p]:
#                     return False
#                 p +=1
#             else: # v is vlaue
#                 p += v
#                 if p > len(word):
#                     return False
#         return p == len(word)
