#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Feb 26 07:33:44 2020

@author: mathvolcano

https://leetcode.com/problems/reverse-linked-list/

206. Reverse Linked List
"""

def reverseList(head) -> ListNode:
        
    # Get reversed values
    n = head
    new_list = []
    while n:
        new_list.insert(0, n.val)
        n = n.next
        
    # Change values in place
    r = head
    for v in new_list:
        r.val = v
        r = r.next
    return head