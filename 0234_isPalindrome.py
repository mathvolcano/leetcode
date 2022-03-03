"""
234. Palindrome Linked List
https://leetcode.com/problems/palindrome-linked-list/
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        # approach: O(n) time O(1) space because we modify in place
        #    1. use walker/runner pointers for find mid node
        #    2. reverse the second half list
        #    3. match each element in the first haf list and
        #       reversed second half list

        # iteratively reverse
        def reverse(head):
            if head == None or head.next == None:
                return head

            cur = head
            while cur.next:
                n = cur.next
                cur.next = n.next
                n.next = head
                head = n
            return head

        fast = slow = head

        # slow will point to the middle node
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        # if amount of nodes is odd, slow move one more step
        if fast:
            slow = slow.next

        seek = head
        slow = reverse(slow)
        while seek and slow and seek.val == slow.val:
            seek = seek.next
            slow = slow.next

        return slow == None

#         # Pythonic - O(n) time and space
#         # Get reversed values
#         n = head
#         vals = []
#         while n:
#             vals.append(n.val)
#             n = n.next

#         l = len(vals)
#         return all(vals[i] == vals[l-i-1] for i, _ in enumerate(vals))
