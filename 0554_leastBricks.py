"""
554. Brick Wall
https://leetcode.com/problems/brick-wall/
"""

class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:

        # Get the candidates for the cut locations
        # Count the number of levels whose total brick length
        # ends at these points

        # O(1) space, O(n*m) time
        height, width = len(wall), sum(wall[0])
        hash_map, min_cut = {}, height
        for i, lvl in enumerate(wall):
            length = 0
            for b in lvl:
                length += b
                if length != width:  # Exclude endpoints
                    new_height = hash_map.get(length, height) - 1
                    hash_map[length] = new_height
                    min_cut = min(min_cut, new_height)
        return min_cut
