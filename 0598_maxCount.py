"""
598. Range Addition II
https://leetcode.com/problems/range-addition-ii/
"""

class Solution:
    def maxCount(self, m: int, n: int, ops: List[List[int]]) -> int:

        # Note that all operations are performed on the top left submatrix of the mxn matrix
        # Thus the max entry value is always the [1,1] element of the matrix
        # The entries that have the max value are thus those at the intersection of all operations
        # [1] initialize min_a, min_b = m,n values to be the entire matrix
        # [2] iterate through ops and update min_a = min(min_a,a), min_b = min(min_b,b)
        # [3] return the product
        # Time complexity: = O(len(ops))
        # Space complexity: O(1)
        min_a, min_b = m,n
        for a,b in ops:
            min_a = min(min_a, a)
            min_b = min(min_b, b)
        return min_a * min_b

        # Brute Force
        # [1] initialize zero matrix of size mxn
        # [2] increment the matrix by the ops
        # [3] Find the max int value in the resulting matrix
        # [4] count the number of occurrences of the max int
        # Time complexity: O(m*n*len(ops))
        # Space complexity: O(m*n)
        # mat = [[0] * n for _ in range(m)]
        # for a,b in ops:
        #     for i in range(a):
        #         for j in range(b):
        #             mat[i][j] += 1
        # max_int = max(max(r) for r in mat)
        # return sum(sum(x == max_int for x in r) for r in mat)
