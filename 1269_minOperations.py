"""
1769. Minimum Number of Operations to Move All Balls to Each Box
https://leetcode.com/problems/minimum-number-of-operations-to-move-all-balls-to-each-box/
"""
class Solution:
    def minOperations(self, boxes: str) -> List[int]:

        # 2 pass
        # [1] initialize
        #     [a] a result array, res of length boxes, res = [0] * len(boxes),
        #     [b] a counter, balls, of the number of balls
        #     [c] a count of the number of operations, ops
        # [2] Left pass – initialize a counter, ops = 0, and add 1 to it if ball else 0
        #     set boxes[i] += ops (subtract 1 if ball already there)
        # [3] Right pass – initialize a counter, ops = 0, and add 1 to it if ball else 0
        #     set boxes[i] += ops (subtract 1 if ball already there)
        # O(len(boxes)) time and space complexity

        # Example 1:
        # res = [0,0,0], balls = 0, ops = 0
        # Left pass
        # i = 0, balls = 1, ops = 0, res = [0+0, 0, 0]
        # i = 1, balls = 2, ops = 1, res = [0, 0+1, 0]
        # i = 2, balls = 2, ops = 3, res = [0, 1, 0+3]
        # Right pass
        # i = 0, balls = 0, ops = 0, res = [0, 1, 3+0]
        # i = 1, balls = 1, ops = 0, res = [0, 1+0, 3]
        # i = 2, balls = 1, ops = 1, res = [0+1, 1, 3]
        # res = [1,1,3]

        res = [0] * len(boxes)
        balls, ops = 0, 0
        # Left pass
        for i, c in enumerate(boxes):
            ops += balls
            res[i] += ops
            balls += 1 if c == '1' else 0
        # Right pass
        balls, ops = 0, 0
        for i, c in reversed(list(enumerate(boxes))):
            # print(i, c)
            ops += balls
            res[i] += ops
            balls += 1 if c == '1' else 0
        return res
