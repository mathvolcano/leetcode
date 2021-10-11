"""
575. Distribute Candies
https://leetcode.com/problems/distribute-candies/
"""

class Solution:
    def distributeCandies(self, candyType: List[int]) -> int:
        n = len(candyType)
        types = set(candyType)
        return min(n // 2, len(types))
