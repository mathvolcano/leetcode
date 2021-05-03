"""
1122. Relative Sort Array
https://leetcode.com/problems/relative-sort-array/
"""

class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        # [1]. create a hash map of the values in arr2 to their indices
        # Note: this requires the values in arr2 to be distinct.
        # [2]. Create a stack for elements in arr1 not in arr2.
        # [3]. Iterate through arr1. If an element is not in arr2 then pop to stack.
        # [4]. Sort remaining elements of arr1 by the arr2 hashmap and sort elements of stack
        # in ascending order.
        # [5] Concatenate arr1 and stack and return
        # O(n) additional space for hashmap and O(n log n) time complexity for sort
        n_to_val = {v:i for i,v in enumerate(arr2)}
        stack, i = [], 0
        while i < len(arr1):
            if arr1[i] not in n_to_val:
                stack.append(arr1.pop(i))
            else:
                i += 1

        arr1.sort(key=lambda x: n_to_val[x])
        stack.sort()
        return arr1 + stack
