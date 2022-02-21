"""
832. Flipping an Image
https://leetcode.com/problems/flipping-an-image/
"""

class Solution:
    def flipAndInvertImage(self, image: List[List[int]]) -> List[List[int]]:
        return [[1-i for i in r[::-1]] for r in image]
        # O(n) time, O(n) space
        # because we only access each element exactly once.