"""
160. Intersection of Two Linked Lists
https://leetcode.com/problems/intersection-of-two-linked-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None


def getIntersectionNode(headA, headB):
    if (not headA) or (not headB): return None

    def length(ll):
        val = 0
        while ll:
            val += 1
            ll = ll.next
        return val

    newA, newB = headA, headB
    lenA, lenB = length(newA), length(newB)

    # Iterate through longer linked list up to same length
    curA, curB = headA, headB
    for _ in range(abs(lenA - lenB)):
        if lenA >= lenB:
            curA = curA.next
        else:
            curB = curB.next

    while curB != curA:
        curA = curA.next
        curB = curB.next
    return curA
