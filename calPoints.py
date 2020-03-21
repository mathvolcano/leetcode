#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan 19 12:20:45 2020

@author:  mathvolcano

Leetcode 682. Baseball Game
"""



def calPoints(ops):
    ops_list = []
    total = 0
    
    for r in ops:
        print('r', r)
        if (r.isdigit()) or (r.startswith('-') and r[1:].isdigit()):
            val = int(r)
            ops_list.append(int(r))
            total += val
        elif r == 'C': # delete the last round
            val = - ops_list[-1]
            ops_list = ops_list[:-1]
            total += val
        elif r == 'D':
            # the points you get in this round are the doubled data of the last valid round's points
            val = ops_list[-1] * 2
            ops_list.append(val)
            total = sum(ops_list)
        elif r == '+':
            val = ops_list[-1] + ops_list[-2]
            ops_list.append(val)
            total = sum(ops_list)
        else:
             print('error')
             pass
        print(ops_list)
        print('total', total)
    return total
