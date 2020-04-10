"""
287. Find the Duplicate Number
https://leetcode.com/problems/find-the-duplicate-number/
"""


def findDuplicate(nums):
    # Use approach from linked list
    slow = fast = 0
    while True:
        fast = nums[nums[fast]]
        slow = nums[slow]
        # Always terminates because we have duplicates
        if fast == slow:
            break

    dup = 0
    while dup != slow:
        dup = nums[dup]
        slow = nums[slow]
    return dup
