# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode) -> List[float]:
        res = []
        if not root: return res

        nodes = [root]

        while nodes:
            vals = []
            new_nodes = []
            for n in nodes:
                vals.append(n.val)
                if n.left:
                    new_nodes.append(n.left)
                if n.right:
                    new_nodes.append(n.right)
            res.append(sum(vals) / len(vals))
            nodes = new_nodes
        return res
