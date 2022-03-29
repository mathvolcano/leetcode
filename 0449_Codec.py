"""
449. Serialize and Deserialize BST
https://leetcode.com/problems/serialize-and-deserialize-bst/
"""

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:


    def serialize(self, root: TreeNode) -> str:
        """Encodes a tree to a single string.
        """
        # O(n) time and space to traverse tree and store (needed for stack memory recursion)
        if not root: return '*'
        return str(root.val) + ',' + self.serialize(root.left) + ',' + self.serialize(root.right)


    def deserialize(self, data: str) -> TreeNode:
        """Decodes your encoded data to tree.
        """
        # O(n) time and space to traverse tree and store (needed for stack memory recursion)
        def helper(data):
            v = data.popleft()
            if v == '*': return None
            root = TreeNode(int(v))
            root.left = helper(data)
            root.right = helper(data)
            return root

        data = deque(data.split(','))
        return helper(data)


# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans