"""
496. Next Greater Element I
https://leetcode.com/problems/next-greater-element-i/
"""

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # Monotone Stack
        # [1] Initialize an res boject res = [-1] * len(nums1) and stack s
        # [2] Create a hash map, h = {} that maps the values of nums 2 to the next largest value.
        #  a. Initialize a decreasing monotone stack, s =[]
        #  b. for each element n in nums2
        #  b1. if no element in stack or if n < s[-1], then append to stack s
        #  b2. else pop stack until b1 is true and for each element popped add element to hash_table key with value n.
        # [3] Iterate through nums1 and perform lookup in hash_map
        # O(n1 + n2) time complexity to create hashmap and perform lookup. If nums1 is always a subset of nums2 then time complexity is O(n2)
        # O(n2) space for creating hashmap (do not count saving the result)
        h, s = {}, []
        for n in nums2:
            if len(s) == 0 or n < s[-1]:
                s.append(n)
            else:
                while len(s) > 0 and n >= s[-1]:
                    h[s.pop()] = n
                s.append(n)
        return [h[n] if n in h else -1 for n in nums1]
