"""
370. Range Addition
https://leetcode.com/problems/range-addition/
"""

class Solution:
    def getModifiedArray(self, length: int, updates: List[List[int]]) -> List[int]:

        # [0] initialize empty array of length, l.
        # [1] Iterate through the updates and increment the first position of the update by the value
        # and decrement by the value in the last position + 1
        # [2] prefix sum the elements in the array
        # O(l + len(updates)) time and O(l) space
        # Example: 5, 5[[1,3,2],[2,4,3],[0,2,-2]]
        # [0] res = [0,0,0,0,0]
        # [1]
        # res [0, 2, 0, 0, -2]
        # res [0, 2, 3, 0, -2]
        # res [-2, 2, 3, 2, -2]
        # [2]
        # res [-2, 0, 3, 2, -2]
        # res [-2, 0, 3, 2, -2]
        # res [-2, 0, 3, 5, -2]
        # res [-2, 0, 3, 5, 3]

        res = [0] * length  # [0]
        for i, j, v in updates:  # [1]
            res[i] += v
            j += 1
            if j < len(res):
                res[j] -= v

        for i in range(1, len(res)):  # [2]
            res[i] += res[i-1]

        return res
