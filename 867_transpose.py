"""
867. Transpose Matrix
https://leetcode.com/problems/transpose-matrix/
"""

class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:

    # Pythonic
    # O(n*m) time and space.
    # return list(map(list, zip(*matrix)))

    # Brute Force
    # [1] Construct a matrix of the transposed form
    # [2] Populate elements of ans
    # O(n*m) time and space.
    #         m, n = len(matrix), len(matrix[0])
    #         ans = [[0] * m for _ in range(n)]
    #         # print(ans)

    #         for i in range(m):
    #             for j in range(n):
    #                 ans[j][i] = matrix[i][j]
    #         return ans
