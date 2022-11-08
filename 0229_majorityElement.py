"""
229. Majority Element II
https://leetcode.com/problems/majority-element-ii/description/
"""

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        # Boyer-Moore Majority Vote Algorithm
        # Note: there can only be at most 2 elemenets in result because
        # each candidate must have > n//3 elements in nums.
        # The Boyer-Moore algorithm finds the majority element by incrmementing
        # the top candidate on hits and decrementing on misses.
        # We adapt this algorithm for top 2 elements.
        # https://en.wikipedia.org/wiki/Boyer%E2%80%93Moore_majority_vote_algorithm
        # [1] Initialize counts and majority element candidates
        # [2] iterate v through nums
        #    [a] if v is one of the 2 majority candidates then increment counts
        #    [b] else set to majority candidates if majorities not set
        #    [c] else decrement counts
        # [3] check if majority candidates exceed cutoff of len(nums) //3
        # Complexity
        # n = len(nums)
        # Time: O(n) to perform single pass of counts
        # Space: O(1) for local variables
        if not nums: return []
        c1, c2, m1, m2 = 0, 0, None, None  # count, majority
        for v in nums:
            if m1 == v:
                c1 += 1
            elif m2 == v:
                c2 += 1
            elif c1 == 0:
                m1 = v
                c1 = 1
            elif c2 == 0:
                m2 = v
                c2 = 1
            else:
                c1 -= 1
                c2 -= 1
        res, cutoff = [], len(nums) // 3
        for m in [m1, m2]:
            if nums.count(m) > cutoff:
                res.append(m)
        return res

        # Hash table
        # [1] calculate floor(n/3)
        # [2] Create a hash map of all value counts
        # [3] Iterate across all hash table to check if counts exceed floor
        # Complexity
        # Let n = len(nums) and m the number of unique values of nums
        # O(m) space for hash table and O(n) time to create hash table
        # Worst case O(n) time & space
        # floor = len(nums) // 3
        # from collections import Counter
        # h = Counter(nums)
        # res = []
        # for k,v in h.items():
        #     if v > floor:
        #         res.append(k)
        # return res
