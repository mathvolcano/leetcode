"""
1430. Check If a String Is a Valid Sequence from Root to Leaves Path in a Binary Tree
https://leetcode.com/problems/check-if-a-string-is-a-valid-sequence-from-root-to-leaves-path-in-a-binary-tree/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidSequence(self, root: Optional[TreeNode], s: List[int]) -> bool:
        # DFS preorder
        # [1] define helper function dfs(i, node)
        # [2] if not node or i == n or s[i] != node.val: return False
        # [3] if node is leaf and i == n-1 and and node.val == s[i] then return true
        # [4] return recursion of dfs(i+1, node.left) or dfs(i+1, node.right)
        # [5] Return dfs(0, root)
        # Complexity: n = number of nodes of tree, m = length of s
        # Space: O(n) for recursive call stack with worse case a linear tree
        # Time worst case O(min(2^m, n)) because each element of s corresponds with 2 leaf options and n to traverse whole tree.
        n = len(s)
        def dfs(i, node):
            if not node or i == n or s[i] != node.val:
                return False
            if i == n - 1 and not (node.left or node.right):
                return True
            return dfs(i+1, node.left) or dfs(i+1, node.right)
        return dfs(0, root)
