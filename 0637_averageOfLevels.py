"""
637. Average of Levels in Binary Tree
https://leetcode.com/problems/average-of-levels-in-binary-tree/
"""

# Helper class that allocates a  
# new node with the given data and  
# None left and right pointers.  
class newNode: 
    def __init__(self, data): 
        self.val = data  
        self.left = self.right = None

def averageOfLevels(root):
    res = []
    if not root:
        return res
    q = [root]
    while q:
        temp = []
        total = 0
        count = 0
        while q:
            node = q.pop()
            if node.left:
                temp.append(node.left)
            if node.right:
                temp.append(node.right)
            total += node.val
            count += 1
        res.append(total*1.0/count)
        q = list(temp)
    return res  
