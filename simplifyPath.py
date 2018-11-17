#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 08:59:22 2018

@author: mathvolcano

Simplify Unix Path
"""

class Solution:
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        # already in top directory
        if path in ['/../', '/.']:
            return '/'
        if path[:4] == '/../':
            path = '/' + path[4:]
        
        # replace multiple slashes
        while ('//' in path) or ('/./' in path):
            path = (path.replace('//', '/').replace('/./', '/'))
            
        # Move up one directory
        directory_moves = path.split('/')
        while '..' in directory_moves:
            # Get index of last occurrence in liast and remove it
            dotdot_idx = directory_moves.index('..')
            # Already in top directory
            if dotdot_idx == 0:
                directory_moves = directory_moves[1:]
            
            # Move out of previous directory
            if dotdot_idx >= 1:
                directory_moves \
                    = directory_moves[:dotdot_idx-1] + directory_moves[dotdot_idx+1:]
        path = '/'*(len(directory_moves) == 0) + '/'.join(directory_moves)
            
        # Return "/home//foo/" -> "/home/foo"
        if len(path) > 1 and (path[-1] == '/'):
            path = path[:-1]
            
        # Catch edge cases
        
        # End
        if path[-2:] == '/.':
            path = path[:-2]
            
        if len(path) == 0:
            path = '/'
            
        if path[0] != '/':
            path = '/' + path
            
        return path
