"""
240. Search a 2D Matrix II
https://leetcode.com/problems/search-a-2d-matrix-ii/
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:

        # [1] Start from the top right corner and set to val
        # [2] Note that if target > val then eliminate row and increase row count
        # if equal target, return true, and if target < val, then search row.
        # Repeat until cursor is out of bounds.
        # Space complexity is O(1)
        # Time complexity is O(m+n) < O(min(m,n) * log(max(m,n)))
        r, c = 0, len(matrix[0]) - 1
        while c >= 0 and r < len(matrix):
            val = matrix[r][c]
            if val > target:
                c -= 1
            elif val < target:
                r += 1
            else:
                return True
        return False


#         # Binary search the rows and columns
#         # [1] Condition on whether or not the matrix is vertically-stretched or horizontally-stretched
#         # [2] Perform a binary search
#         # Time complexity = O(min(m,n) * log(max(m,n)))
#         # Space complexity: O(1)
#         if not matrix: return False

#         for i in range(min(len(matrix), len(matrix[0]))):
#             vertical_found = self.binary_search(matrix, target, i, True)
#             horizontal_found = self.binary_search(matrix, target, i, False)
#             if vertical_found or horizontal_found:
#                 return True
#         return False


#     def binary_search(self, matrix, target, start, vertical):
#         l = start
#         r = len(matrix[0]) - 1 if vertical else len(matrix) - 1
#         while l <= r:
#             m = (l + r) // 2
#             if vertical: # search col
#                 v = matrix[start][m]
#                 if v < target:
#                     l = m + 1
#                 elif v > target:
#                     r = m - 1
#                 else:
#                     return True
#             else:  # search row
#                 v = matrix[m][start]
#                 if v < target:
#                     l = m + 1
#                 elif v > target:
#                     r = m - 1
#                 else:
#                     return True
