#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 08:35:27 2020

@author: mathvolcano

104. Maximum Depth of Binary Tree
https://leetcode.com/problems/maximum-depth-of-binary-tree/
"""

def maxDepth(root):
    """Fine."""
    if not root: return 0
    
    depth = 0
    levels = [root]
    while levels:
        new_levels = []
        for node in levels:
            if node.left:
                new_levels.append(node.left)
            if root.right:
                new_levels.append(node.right)
        depth += 1
        levels = [x for x in new_levels if x]
            
    return depth

def maxDepth(root):
    """Uses recursion."""
    if root == None:
        return 0
    return 1 + max(maxDepth(root.left), maxDepth(root.right))