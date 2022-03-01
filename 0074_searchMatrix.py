"""
74. Search a 2D Matrix
https://leetcode.com/problems/search-a-2d-matrix/
"""

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        # Note that if we flattened the matrix and then did a binary search
        # that the time complexity would be O(log(nm)) < O(log n * log m)
        # O(1) space complexity.
        n, m = len(matrix), len(matrix[0])
        l, r = 0, n*m - 1
        while l <= r:
            mid = l + (r - l) // 2
            val = matrix[mid//m][mid%m]
            if target == val:
                return True
            elif target < val:
                r = mid - 1
            else:
                l = mid + 1
        return False

#         # Binary search the rows and columns
#         # [1] Given a row, binary search to find target
#         # [2] Binary search across rows to see if the row contains the target
#         # O(log n * log m) time complexity, O(1) space complexity.
#         n, m = len(matrix)-1, len(matrix[0]) - 1
#         l, r = 0, len(matrix) - 1
#         while l <= r:
#             mid = (l+r) // 2
#             row = matrix[mid]
#             found = self.binary_search_row(row, target)
#             if found == True:
#                 return True
#             elif target < row[0]:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return False

#     # Binary search row
#     def binary_search_row(self, row, target):
#         if (target < row[0]) or (target > row[-1]): return False
#         l, r = 0, len(row) - 1
#         while l <= r:
#             mid = (l + r) // 2
#             val = row[mid]
#             if target == val:
#                 return True
#             elif target < val:
#                 r = mid - 1
#             else:
#                 l = mid + 1
#         return False

# Brute Force – Flatten the matrix and search all values
# O(n * m) time complexity with n rows and m cols
# vals = [x for row in matrix for x in row]
# return target in vals
