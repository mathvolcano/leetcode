"""
73. Set Matrix Zeroes
https://leetcode.com/problems/set-matrix-zeroes/
"""

def setZeroes(matrix):
    """
    Do not return anything, modify matrix in-place instead.
    """
    firstRowHasZero = False
    firstColHasZero = False
    n = len(matrix)
    m = len(matrix[0])
    if n==0 or m == 0:
        return
    for col in range(m):
        if matrix[0][col]==0:
            firstRowHasZero = True
            break
    for row in range(n):
        if matrix[row][0]==0:
            firstColHasZero = True
            break
        
    if n > 1 and m > 1:
        for row in range(1, n):
            for col in range(1,m):
                if matrix[row][col] == 0:
                    matrix[0][col] = 0
                    matrix[row][0] = 0
    
    if n > 1 and m > 1:
        for row in range(1, n):
            for col in range(1,m):
                if matrix[row][0] == 0 or matrix[0][col] == 0:
                    matrix[row][col] = 0
    
    if firstRowHasZero:
        for col in range(m):
            matrix[0][col] = 0
    
    if firstColHasZero:
        for row in range(n):
            matrix[row][0] = 0


matrix = [
  [0,1,2,0],
  [3,4,5,2],
  [1,3,1,5]
]
setZeroes(matrix)
#[
#  [0,0,0,0],
#  [0,4,5,0],
#  [0,3,1,0]
#]

matrix = [[1,1,1],[1,0,1],[1,1,1]]
setZeroes(matrix)

matrix = [[0],[1]]
setZeroes(matrix)