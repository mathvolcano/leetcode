"""
267. Palindrome Permutation II
https://leetcode.com/problems/palindrome-permutation-ii/
"""
class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        # See 47 Permutation
        def helper(arr, current, result):
            # Terminating case
            if len(arr) == 0 and len(current) > 0:
                result.add(tuple(current))
            else:
                for i in range(len(arr)):
                    newArr = arr[:i] + arr[i+1:]
                    newCur = current + [arr[i]]
                    helper(newArr, newCur, result)

            return -1

        result = set()
        helper(nums, [], result)
        return list(result)

    def generatePalindromes(self, s: str) -> List[str]:
        # [1] Check if s can be a palindrome by counting elements of s. If not return False.
        # [2] If a palindromic permutation exists, generate the first half of the string.
        # [3] Check for all unique palindromes using permutation 2
        # O(n!) Time and space complexity for calculating & storing permutations

        # [0] Base or Trivial cases
        if len(s) == 0: return []
        if len(s) == 1: return [s]

        # [1] Check palindrome permutation. Get any odd-one-out letter if they exist
        from collections import Counter
        counts = Counter(s)
        odd_char = ''
        odds = 0
        for l,c in counts.items():
            if c % 2 == 1:
                odd_char = l
                odds += 1

        if odds > 1:
            return []
        else:
            counts[odd_char] -= 1

        # Get permutations of first half of permutation
        first_half = []
        for l, c in counts.items():
            if c % 2 == 0:
                first_half += [l] * (c // 2)
        print('first_half', first_half)

        # Get the permutations of the first half
        first_half_perms = self.permuteUnique(first_half)
        print('first_half_perms', first_half_perms)

        # Build palindromes
        return [''.join(list(h) + [odd_char] + list(h[::-1])) for h in first_half_perms]

        # Brute Force / Pythonic
        # Get all permutations and check if the permutation is palindrome
        # O(2^n) time and space to generate all permutations
        # import itertools
        # perms = list(itertools.permutations(s, len(s)))
        # return list(set(''.join(p) for p in perms if p == p[::-1]))
