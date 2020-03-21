#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Feb 10 07:27:09 2020

@author: mathvolcano

Daily Temperatures
https://leetcode.com/explore/learn/card/queue-stack/230/usage-stack/1363/
"""

def dailyTemperatures(T):
    result = [0] * len(T)
    stack = [] #indexes from hottest to coldest
    for i in range(len(T) - 1, -1, -1):
        while stack and T[i] >= T[stack[-1]]:
            stack.pop() #remove lower and not soonest 
        if stack:
            result[i] = stack[-1] - i
        stack.append(i)
    return result  

T = [73, 74, 75, 71, 69, 72, 76, 73]
#Output [1, 1, 4, 2, 1, 1, 0, 0]
