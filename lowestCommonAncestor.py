#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Feb  2 15:50:33 2020

@author: mathvolcano

https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-search-tree
"""

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not root:
            return None
        if (p.val < root.val) and (q.val < root.val):
            return self.lowestCommonAncestor(root.left, p, q)
        elif (p.val > root.val) and (q.val > root.val):
            return self.lowestCommonAncestor(root.right, p, q)
        else:
            return root