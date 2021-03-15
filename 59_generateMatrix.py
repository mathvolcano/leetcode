"""
59. Spiral Matrix II
https://leetcode.com/problems/spiral-matrix-ii/
"""

def generateMatrix(n):
    if n == 0: return []
    if n == 1: return [[1]]
    
    min_x, max_x, min_y, max_y = 0, n-1, 0, n-1
    
    x, y = 0, 0
    result = [[0]* n for i in range(n)]
    values = [i for i in range(1,n**2 + 1)]
    directions = [(0,1), (1,0), (0,-1), (-1,0)]
    current_dir = 0
    while values:
        result[x][y] = values.pop(0)
        
        # 1. After traversing right the top row update direction & bounds
        if current_dir == 0 and y == max_y:
            current_dir = 1
            min_x += 1
        # 2. Update after traversing down the right column
        elif current_dir == 1 and x == max_x:
            current_dir = 2
            max_y -= 1
        # 3. After traversing left the bottom row update direction & bounds
        elif current_dir == 2 and y == min_y:
            current_dir = 3
            max_x -= 1
        # 4. After traversing up the left update direction & bounds
        elif current_dir == 3 and x == min_x:
            current_dir = 0
            min_y += 1
            
        # Update
        x += directions[current_dir][0]
        y += directions[current_dir][1]
            
    return result


generateMatrix(3)
#[
# [ 1, 2, 3 ],
# [ 8, 9, 4 ],
# [ 7, 6, 5 ]
#]
