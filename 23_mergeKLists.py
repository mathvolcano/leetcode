"""
23. Merge k Sorted Lists
https://leetcode.com/problems/merge-k-sorted-lists/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        # Perform a merge-sort on each list

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

        def mergeKListsHelper(lists, begin, end):
            # Stopping conditions
            if begin > end:
                return None
            if begin == end:
                return lists[begin]

            # Merge first list with middle and the middle with last (binary Search)
            return mergeTwoLists(mergeKListsHelper(lists, begin, (begin + end) // 2), \
                                 mergeKListsHelper(lists, (begin + end) // 2 + 1, end))

        return mergeKListsHelper(lists, 0, len(lists) - 1)
        