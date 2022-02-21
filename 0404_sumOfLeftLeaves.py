"""
404. Sum of Left Leaves
https://leetcode.com/problems/sum-of-left-leaves/
"""

class Solution:
    def sumOfLeftLeaves(self, root: TreeNode) -> int:

        # Perform a DFS search
        # [1] Check if the root has a left leaf. If so add the value to the total
        # [2] Search the next nodes in the root

        # O(n) time complexity n the number of nodes.
        # O(h) space complexity for the stack memory of the DFS.

        def dfs(root):
            if not root: return
            if root.left and not root.left.left and not root.left.right:
                self.total += root.left.val
            dfs(root.left)
            dfs(root.right)

        self.total = 0
        dfs(root)
        return self.total
