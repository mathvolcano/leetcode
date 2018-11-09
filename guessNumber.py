#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 08:12:32 2018

@author: mathvolcano
"""

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        # Perform a binary search
        left = 1
        right = n
        while left <= right:
            mid = int((right+left)/2)
            high_or_low_or_right = guess(mid)
            if high_or_low_or_right == 1:
                left = mid + 1
            elif high_or_low_or_right == -1:
                right = mid - 1
            else:
                return mid
        return left 
