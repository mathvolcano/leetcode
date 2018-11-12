#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 12 05:48:36 2018

@author: mathvolcano

Add two numbers
"""

# Definition for singly-linked list.
class ListNode:
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        l4 = l3 = ListNode(0)
        carry = 0
        while l1 or l2:
            added = (l1.val if l1 else 0) + (l2.val if l2 else 0) + carry
            l4.next = ListNode(added % 10)
            carry = 1 if (added >= 10) else 0

            l4 = l4.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        if carry == 1:
            l4.next = ListNode(1)
        return l3.next