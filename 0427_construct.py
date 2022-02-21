"""
427. Construct Quad Tree
https://leetcode.com/problems/construct-quad-tree/
"""

"""
# Definition for a QuadTree node.
class Node:
    def __init__(self, val, isLeaf, topLeft, topRight, bottomLeft, bottomRight):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight
"""

class Solution:
    def construct(self, grid: List[List[int]]) -> 'Node':
        
        # Recursion
        # [1] Define a helper function on which we recurse
        # [2] Base case: if all values the same then set leaf to true
        # and val to 1
        # [3] Else, set leaf to false and partition range by midpoints
        # [4] recurse on 4 children
        # Time and space complexity: O(n^2)

        def helper(x, y, length):
            val = grid[x][y]
            flag = True
            root = Node(False, False, None, None, None, None)
            for i in range(length):
                for j in range(length):
                    if grid[x+i][y+j] != val:
                        flag = False
                        break
            if flag:
                root.isLeaf = True
                root.val = True if val == 1 else False
            else:
                root.isLeaf = False
                m = length // 2  # mid
                root.topLeft = helper(x, y, m)
                root.topRight = helper(x, y+m, m)
                root.bottomLeft = helper(x+m, y, m)
                root.bottomRight = helper(x+m, y+m, m)
            return root

        length = len(grid)
        return helper(0, 0, length)
