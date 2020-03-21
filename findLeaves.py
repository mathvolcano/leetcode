#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb  3 10:26:08 2020

@author: mathvolcano

http://buttercola.blogspot.com/2018/09/leetcode-366-find-leaves-of-binary-tree.html
"""

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def findLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        hash_map = {} # height: nodes
        
        max_height = self.dfs(root, hash_map)
        
        ans = []
        for i in range(max_height+1):
            ans.append(hash_map[i])
        return ans
        
    def dfs(self, node, hash_map):
        if not node:
            return -1
        leftLayer, rightLayer = -1, -1
        if node.left:
            leftLayer = self.dfs(node.left,hash_map)
        if node.right:
            rightLayer = self.dfs(node.right,hash_map)
        curLayer = max(leftLayer, rightLayer) + 1
        if curLayer not in hash_map:
            hash_map[curLayer] = []
        hash_map[curLayer].append(node.val)
        return curLayer
