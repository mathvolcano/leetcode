# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class BSTIterator:

    def __init__(self, root: TreeNode):
        self.stack = []
        self.prev = root

    def next(self) -> int:
        """
        @return the next smallest number
        """
        while len(self.stack) > 0 or self.prev:
            while self.prev:
                self.stack.append(self.prev)
                self.prev = self.prev.left
            cur = self.stack.pop()
            self.prev = cur.right
            return cur.val

    def hasNext(self) -> bool:
        """
        @return whether we have a next smallest number
        """
        return len(self.stack) > 0 or self.prev

# Your BSTIterator object will be instantiated and called as such:
# obj = BSTIterator(root)
# param_1 = obj.next()
# param_2 = obj.hasNext()
