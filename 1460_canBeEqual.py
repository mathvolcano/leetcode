"""
1460. Make Two Arrays Equal by Reversing Sub-arrays
https://leetcode.com/problems/make-two-arrays-equal-by-reversing-sub-arrays/
"""

class Solution:
    def canBeEqual(self, target: List[int], arr: List[int]) -> bool:
        # Note: reversing a pair of integers is a transposition.
        # Because all permutations can be decomposed as compositions of
        # transpositions, target can be achieved if it is a permutation of arr.
        # Thus, we can sort target and arr arrays to check if they are equal.
        # If they are then, the result is true and if not then false.
        target.sort()
        arr.sort()
        return target == arr
