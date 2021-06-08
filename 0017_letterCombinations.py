"""
17. Letter Combinations of a Phone Number
https://leetcode.com/problems/letter-combinations-of-a-phone-number/
"""


def letterCombinations(digits):
    """Compute O(n*4^n) complexity solution"""
    if len(digits) == 0: return []

    MAPPING = ['0', '1', 'abc', 'def', 'ghi', 'jkl', 'mno', 'pqrs', 'tuv', 'wxyz']
    lcs = []
    letters_list = [0] * len(digits)

    def recurse(pointer):
        # Exit the recursion by combining  all valid letters to join
        if pointer == len(digits):
            valid_combos = ''.join(letters_list)
            lcs.append(valid_combos)
        # Recurse
        else:
            letters = MAPPING[int(digits[pointer])]
            print(letters, letters_list, lcs)
            for c in letters:
                letters_list[pointer] = c
                recurse(pointer + 1)

    recurse(0)
    return lcs

letterCombinations('23')
# ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]