"""

"""

class Solution(object):
    def numSubmatrixSumTarget(self, matrix, target):

        # DP
        # Brute force is O(m^2 * n^2)
        # Can do in
        # import collections

        # Sum over columns
        m, n = len(matrix), len(matrix[0])
        for row in matrix:
            for i in range(n - 1):
                row[i + 1] += row[i]
        # 1 1 1 1 -> 1 2 3 4
        # 1 1 1 1 -> 1 2 3 4
        # 1 1 1 1 -> 1 2 3 4
        # 1 1 1 1 -> 1 2 3 4
        ans = 0
        for i in range(n):
            for j in range(i, n):
                c = collections.defaultdict(int)
                cur, c[0] = 0, 1
                for k in range(m):
                    cur += matrix[k][j] - (matrix[k][i - 1] if i > 0 else 0)
                    ans += c[cur - target]
                    c[cur] += 1
        return ans