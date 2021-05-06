"""
1248. Count Number of Nice Subarrays
https://leetcode.com/problems/count-number-of-nice-subarrays/
"""

class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:

        # Prefix Sum solution in a hash_map
        # [1] For each index in the array get the rolling count of odds in the nums
        # [2] Store counts in a hash_map. Check to see if the complement has k odds.
        # Ex: nums = [1,1,2,1,1], k=3
        hash_map = {0:1}
        res, cur = 0, 0  # result, current count
        for i, v in enumerate(nums):
            cur += 1 if v % 2 ==1 else 0
            res += hash_map.get(cur - k, 0)
            hash_map[cur] = hash_map.get(cur, 0) + 1
        # i = 4, v = 1
        # cur = 4, res = 2
        # hash_map = {0:1, 1:1, 2:2, 3:1}
        return res

        # Brute Force  –
        #[1] get all continuous subarrays
        #[2] count the number of odds in each subarray
        # O(n^3) time complexity to iterate through all subarray sums
        # O(n^2) space complexity to store pairs
        # n = len(nums)
        # pairs = [(i,j) for i in range(n) for j in range(n) if i <= j]
        # res = 0
        # for i,j in pairs:
        #     subarr = nums[i:j+1]
        #     odds = sum(1 for x in subarr if x % 2 == 1)
        #     if odds == k:
        #         res += 1
        # return res
