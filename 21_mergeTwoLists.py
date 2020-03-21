#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 11 17:41:53 2020

@author: mathvolcano
21. Merge Two Sorted Lists
https://leetcode.com/problems/merge-two-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def mergeTwoLists(l1, l2):
    # Trivial edge cases
    if not l1: return l2
    if not l2: return l1
    
    head = tail = ListNode(0)
    
    while l1 and l2:
        if (l1.val < l2.val):
            tail.next = l1
            l1 = l1.next
        else:
            tail.next = l2
            l2 = l2.next
        tail = tail.next
    tail.next = l1 or l2
            
    return head.next