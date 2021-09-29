"""
83. Remove Duplicates from Sorted List
https://leetcode.com/problems/remove-duplicates-from-sorted-list/
"""


def deleteDuplicates(head):
    if head == None: return head

    current = head
    while current:
        if current.next and (current.val == current.next.val):
            current.next = current.next.next
        else:
            current = current.next
    return head
