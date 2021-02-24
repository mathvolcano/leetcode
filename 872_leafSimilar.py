"""
872. Leaf-Similar Trees
https://leetcode.com/problems/leaf-similar-trees/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getLeafList(self, root):
        leaves = []
        if not root: return leaves

        if not root.left and not root.right:
            leaves.append(root.val)

        if root.left:
            leaves.extend(self.getLeafList(root.left))
        if root.right:
            leaves.extend(self.getLeafList(root.right))
        return leaves

    def leafSimilar(self, root1: TreeNode, root2: TreeNode) -> bool:
        leaves1 = self.getLeafList(root1)
        leaves2 = self.getLeafList(root2)
        print(leaves1)
        print(leaves2)
        return leaves1 == leaves2
