"""
1564. Put Boxes Into the Warehouse I
https://leetcode.com/problems/put-boxes-into-the-warehouse-i/
"""
class Solution:
    def maxBoxesInWarehouse(self, boxes: List[int], warehouse: List[int]) -> int:

        # Greedy
        # [1] Sort boxes in descending order
        # [2] check if the height of the box exceeds the height of the room
        # if not continue
        # [3] else increment count up to length of the warehouse.
        # O(1) space, O(b log b) time to sort boxes.
        boxes.sort(reverse=True)
        res = 0
        for h in boxes:
            if h > warehouse[res]:
                continue
            res += 1
            if res == len(warehouse):
                break
        return res
