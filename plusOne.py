#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Nov  9 12:19:08 2018

@author: mathvolcano

66. Plus One
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        i = len(digits) - 1
        while i >= 0:
            if digits[i] == 9:
                digits[i] = 0
                i = i - 1
            else:
                digits[i] = digits[i] + 1
                break
        # i == -1 when all prior digits are 9 so that digits[1] == 9
        if i == -1:
            digits = [1] + digits
        return digits
