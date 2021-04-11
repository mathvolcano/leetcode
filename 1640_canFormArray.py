"""
1640. Check Array Formation Through Concatenation
https://leetcode.com/problems/check-array-formation-through-concatenation/
"""

class Solution:
    def canFormArray(self, arr: List[int], pieces: List[List[int]]) -> bool:

        # O(nm) time O(n+m) space
        piece_start_to_piece = {p[0]: p for p in pieces}
        concat = []
        for a in arr:
            concat += piece_start_to_piece.get(a, [])

        return arr == concat
