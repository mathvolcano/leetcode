#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on %(date)s

@author: mathvolcano

529. Minesweeper
https://leetcode.com/problems/minesweeper/
"""

def updateBoard(board, click):
    def get_entry_val(board, click):
        return board[click[0]][click[1]]
    
    def adjacent_entries(board, x, y):
        adjacents = [[x + i, y + j]
                     for i in range(-1,2)
                     for j in range(-1,2)
                     if ((not ((i==0) and (j==0)))
                         and (x+i < len(board))
                         and (x+i >= 0)
                         and (y+j < len(board[0]))
                         and (y+j >= 0))
                    ]
        return adjacents
#    
    def count_adjacent_mines(board, position):
#        adjacents = adjacent_entries(board, position[0], position[1])
        adjacent_values = get_adjacent_values(board, position)
        n_mines = sum([1 if v=='M' else 0
                       for v in adjacent_values])
        return n_mines

    def get_adjacent_values(board, position):
        adjacents = adjacent_entries(board, position[0], position[1])
        return [board[a[0]][a[1]] for a in adjacents]
        
    x, y = click
    
    # If the initial click is a bomb return board
    if board[x][y] == 'M':
        board[x][y] = 'X'
    elif board[x][y] == 'E':
        # Assign count of bombs
        n_adj_mines = count_adjacent_mines(board, click)
        board[x][y] = str(n_adj_mines) if n_adj_mines else 'B'
        
        # Iterate through adjacents
        if not n_adj_mines:
            adjacents = adjacent_entries(board, x, y)
            for adj in adjacents:
                updateBoard(board, adj)
    return board
    
ex1 = [['B', '1', 'E', '1', 'B'],
       ['B', '1', 'M', '1', 'B'],
       ['B', '1', '1', '1', 'B'],
       ['B', 'B', 'B', 'B', 'B']]
click1 = [1,2]
updateBoard(ex1, click1)
#Output: 
#
#[['B', '1', 'E', '1', 'B'],
# ['B', '1', 'X', '1', 'B'],
# ['B', '1', '1', '1', 'B'],
# ['B', 'B', 'B', 'B', 'B']]

ex2 = [['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'M', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E'],
 ['E', 'E', 'E', 'E', 'E']]
click2 = [3,0]
updateBoard(ex2, click2)

ex3 = [["E"]]
click3 = [0,0]
updateBoard(ex3, click3)

#Output: 
#
#[['B', '1', 'E', '1', 'B'],
# ['B', '1', 'M', '1', 'B'],
# ['B', '1', '1', '1', 'B'],
# ['B', 'B', 'B', 'B', 'B']]