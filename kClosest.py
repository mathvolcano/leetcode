#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jan 31 20:38:37 2020

@author: mathvolcano
"""

def kClosest(points, K):
    if len(points) == 0:
        return None
    else:
        points_and_norm = [x + [(x[0]**2 + x[1]**2)**(1/2)] for x in points]
        points_and_norm.sort(key=lambda x: x[2])
        if K > len(points_and_norm):
            return [x[:2] for x in points_and_norm]
        else:
            return [x[:2] for x in points_and_norm[:K]]
    

points1 = [[1,3],[-2,2]]
k1 = 1
assert kClosest(points1, k1) == [[-2,2]]

points2 = [[3,3],[5,-1],[-2,4]]
K2 = 2
assert kClosest(points2, K2) == [[3,3],[-2,4]]
