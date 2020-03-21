#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Feb  8 19:16:08 2020

@author: mathvolcano
"""

def isValid(s):
    if len(s) < 1:
        return True
    
    stack = []
    for p in s:
        print(p)
        if len(stack) == 0:
            stack.append(p)
        else:
            top = stack[-1]
            if (top == '{') and (p == '}'):
                stack.pop()
            elif (top == '(') and (p == ')'):
                stack.pop()
            elif (top == '[') and (p == ']'):
                stack.pop()
            else:
                stack.append(p)
#        print(stack)
#    print(stack)
    return len(stack) == 0

assert isValid("()[]{}") == True

assert isValid("(]") == False
            