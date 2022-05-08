"""
2032. Two Out of Three
https://leetcode.com/problems/two-out-of-three/
"""
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        # Hash table
        # Time complexity = O(n1 + n2 + n3 + m) where ni = len(numsi) and m is the max number of
        # distinct values
        # Space: O(n1 + n2 + n3 + m) to store h and store res.
        from collections import defaultdict
        h = defaultdict(list)
        for i, l in enumerate([nums1, nums2, nums3]):
            for n in l:
                if i not in h[n]:
                    h[n].append(i)
        res = []
        for k,v in h.items():
            if len(v) >= 2:
                res.append(k)
        return res
