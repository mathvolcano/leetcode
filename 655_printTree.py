"""
655. Print Binary Tree
https://leetcode.com/problems/print-binary-tree/
"""

class Solution:
    def printTree(self, root):

        # Recursion
        # [1] calculate height of tree, h
        # [2] Note that the width is 2^h - 1. Set to width, w
        # [3] construct empty output for us to fill
        # [4] Set root       val to mid, m1, of 1st row x1 = 0, y1 = (l1 + r1) / 2 = (w-1)//2
        # [4] Set l child val to mid of l half of 2nd row x2 = 1, y2 = (l1 + (y1-1)) / 2
        # [4] Set r child val to mid of r half of 2nd row x2 = 1, y2 = ((y1+1) + r1) / 2
        # Time and space complexity is O(h*w) = O(h*2^h)

        def height(root):
            if not root: return 0
            return max(height(root.left), height(root.right)) + 1

        def fill(root, h, l, r):
            if not root: return
            m = (l + r) // 2  # mid
            res[h][m] = str(root.val)
            if root.left:
                fill(root.left , h + 1, l    , m - 1)
            if root.right:
                fill(root.right, h + 1, m + 1, r    )

        h = height(root)
        w = 2**h - 1
        res = [[""] * w for _ in range(h)]
        fill(root, 0, 0, w - 1)
        return res