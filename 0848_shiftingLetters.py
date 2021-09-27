"""
848. Shifting Letters
https://leetcode.com/problems/shifting-letters/
"""

class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:

        # 1 Get cumulative sum of shifts: [3,5,9] -> cumsum = [17, 14, 9]
        # 2 modulo shifts by 26: cumsum = [17 % 26, 14 % 26, 9 %26] -> [17, 14, 9]
        # 3 Cast string s characters to alphanumeric positions: s => s_nums = [1,2,3]
        #   using a alpha to nums dict (need to create that)
        # 4 Add shifts to string numeric positions: s_nums = [18, 16, 12]
        # 5 Modulo sum by 26: s_nums = [18 % 26, 16 % 26, 12 %26] = [18, 16, 12]
        # 5 cast the resulting array of numerals back to alpha letters: s_nums = ['r', 'p', 'l']
        # 6 Concat: => 'rpl'

        # O(len(s)) time complexity, O(1) additional space complexity

        # 1 & 2
        shifts = shifts[::-1]
        prev = 0
        for i, v in enumerate(shifts):
            shifts[i] += prev
            prev += v
        shifts = shifts[::-1]
        shifts = [x % 26 for x in shifts]

        # Dicts
        import string
        nums_to_chars = dict(enumerate(string.ascii_lowercase, 1))
        nums_to_chars.pop(26, None)
        nums_to_chars[0] = 'z'
        chars_to_nums = {v:k for k,v in nums_to_chars.items()}

        return ''.join([nums_to_chars[(chars_to_nums[s[i]] + shifts[i]) % 26]
                        for i in range(len(s))])
