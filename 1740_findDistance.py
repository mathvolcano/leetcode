"""
1740. Find Distance in a Binary Tree
https://leetcode.com/problems/find-distance-in-a-binary-tree/
"""
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        # 1-pass DFS
        # [0] initialize result self.res = -1
        # [1] Define a helper funcition, dfs(root, p,q) to get sum of distances from root to p & q.
        #  a. if not root: return -1
        #. b. Call dfs on left & right children, set to l & r resp.
        #  c. If root.val in (p,q):
        #. [Case 1] target found if either l or r < 0 then p or q == root. So one of them is distance 0 and we set res to l+1 or r+1 & return -1
        #  [Case 2] target found both l & r > 0 so set result to l + r + 2 and return -1
        #. [Case 3&4] No target found yet l >= 0 so so return l + 1. Similarly return r >= 0
        # return -1
        # [2] return self.res
        # Complexity: n = number of nodes of root, h height of tree
        # Time: O(n) worst case to traverse skewed tree
        # Space: O(h) for recursion call stack, worst case O(n)
        def dfs(root, p, q):
            if not root: return -1
            l = dfs( root.left, p, q)
            r = dfs(root.right, p, q)
            if root.val in (p,q):
                if l < 0 and r < 0: return 0
                self.res = l+1 if l >= 0 else r+1
                return -1
            if l >= 0 and r >= 0:
                self.res = l + r + 2
                return -1
            if l >= 0: return l + 1
            if r >= 0: return r + 1
            return -1

        if p == q: return 0
        self.res = -1
        dfs(root, p, q)
        return self.res

        # [1] Find the LCA using a dfs
        #  a. if root.val == p or q then return root
        # b. Recurse for LCA on left & right.
        # c. if left and right, then return root
        # d. else return left if not none, or return right
        # [2] Calculate the distance from LCA to p & q.
        #. a. Initialize a queue q of the node and the distance to LCA, q = deque([(root, 0)])
        #. b. if node equals value of target node then return distance
        #. c. else, add children to queue with +1 distance
        # [3] Return sum of distances
        # Complexity: n = # of nodes of root and h the height of tree
        # Time: worst case O(n) to search full tree for nodes to find LCA for skewed tree case & to traverse 2 more times to calculate distances to target nodes
        # Space: O(h) recursion call stack, worst case O(n) for skewed tree

        # def lca(root):
        #     if not root: return None
        #     if root.val in (p,q): return root
        #     l = lca(root.left)
        #     r = lca(root.right)
        #     if l and r:
        #         return root
        #     return l or r

        # def dist(root, val):
        #     q = collections.deque()
        #     q.append((root, 0))
        #     while q:
        #         c, d = q.popleft()  # current, distance
        #         if c.val == val:
        #             return d
        #         if c.left: q.append((c.left, d+1))
        #         if c.right: q.append((c.right, d+1))

#         def dist(n, v):  # node, value
#             if not n: return float('inf')
#             if n.val == v: return 0
#             return 1 + min(dist(n.left, v), dist(n.right, v))

#         node = lca(root)
#         return dist(node, p) + dist(node,q)
