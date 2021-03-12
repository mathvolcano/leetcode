"""
Created on Mon Feb  3 07:52:51 2020

@author: mathvolcano

Recursive polish notation
"""

def evalRPN(tokens):
    
    stack = []
    ops = ['+', '-', '*', '/']
    
    for idx, token in enumerate(tokens):
        if token not in ops:
            stack.append(int(token))
        else:
            right = stack.pop()
            left = stack.pop()
            if token == '+':
                stack.append(left + right)
            if token == '-':
                stack.append(left - right)
            if token == '*':
                stack.append(left * right)
            if token == '/':
                if left* right < 0:
                    stack.append(-((-left)//right))
                else:
                    stack.append(left//right)
    return stack.pop()
        

a1 = ["4","3","-"]
evalRPN(a1)
# expected 1

a = ["2", "1", "+", "3", "*"]
evalRPN(a)
#Output: 9
#Explanation: ((2 + 1) * 3) = 9

b = ["4", "13", "5", "/", "+"]
evalRPN(b)
#Explanation: (4 + (13 / 5)) = 6

c = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]
evalRPN(c)
#Output: 22
#Explanation: 
#  ((10 * (6 / ((9 + 3) * -11))) + 17) + 5
#= ((10 * (6 / (12 * -11))) + 17) + 5
#= ((10 * (6 / -132)) + 17) + 5
#= ((10 * 0) + 17) + 5
#= (0 + 17) + 5
#= 17 + 5
#= 22