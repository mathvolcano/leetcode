"""
905. Sort Array By Parity
https://leetcode.com/problems/sort-array-by-parity/
"""
class Solution:
    def sortArrayByParity(self, A: List[int]) -> List[int]:

        # 1 pass through A, O(n) time & space.
        even, odd = [], []
        while len(A)!= 0:
            if A[-1] % 2 == 0:
                even.append(A.pop())
            else:
                odd.append(A.pop())
        return even + odd

        # Pythonic
        # return sorted(A, key = lambda x : x % 2)
        # return [a for a in A if a % 2 == 0] + [a for a in A if a % 2 == 1]
