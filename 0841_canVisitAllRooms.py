"""
841. Keys and Rooms
https://leetcode.com/problems/keys-and-rooms/
"""

class Solution:
    def canVisitAllRooms(self, rooms: List[List[int]]) -> bool:

        # Brute Force
        # O(n) time to check each room. Worst case to O(n^2). Space O(n)
        n = len(rooms)
        visited = set()
        stack = [0]
        while stack:
            r = stack.pop()
            visited.add(r)
            for u in rooms[r]:
                if u not in visited:
                    stack.append(u)
        return len(visited) == n
