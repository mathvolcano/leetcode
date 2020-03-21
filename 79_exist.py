#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Mar 16 07:54:01 2020

@author: mathvolcano

79. Word Search
https://leetcode.com/problems/word-search/
"""

def exist(board, word):
    if len(word) == 0: return 0

    def dfs(board, r,c, count, word):
        if count == len(word):
            return True
        
        char = word[count]
        if (r < 0 or c < 0 or r >= len(board) or c >= len(board[0]) or board[r][c] != char):
            return False
        temp = board[r][c] # needed to prevent backtracking
        board[r][c] = ' '
        found = (dfs(board, r-1,c, count+1, word)
                 or dfs(board, r+1,c, count+1, word)
                 or dfs(board, r,c-1, count+1, word)
                 or dfs(board, r,c+1, count+1, word))
        board[r][c] = temp
        return found
        
    # board is nxm
    n = len(board)
    m = len(board[0])
    
    for r in range(n):
        for c in range(m):
            if board[r][c] == word[0] and dfs(board, r,c, 0, word):
                return True
    return False

        

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

word = "ABCCED"
exist(board, word) # True

word = "SEE"
exist(board, word) # True

word = 'ABCD'
exist(board, word) # False

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCB"
exist(board, word)