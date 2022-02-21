"""
111. Minimum Depth of Binary Tree
https://leetcode.com/problems/minimum-depth-of-binary-tree/
"""

#class TreeNode:
#    def __init__(self, x):
#        self.root = x
#        self.left = None
#        self.right = None
        
def minDepth(root):
    if not root: return 0
    
    min_depth = 1
    levels = [root]
    while levels:
        new_levels = []
        for node in levels:
            if (not node.left) and (not node.right):
                return min_depth
            else:
                if node.left:
                    new_levels.append(node.left)
                if root.right:
                    new_levels.append(node.right)
        min_depth += 1
        levels = [x for x in new_levels if x]
            
    return -1
