"""
1010. Pairs of Songs With Total Durations Divisible by 60
https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/
"""

class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        # Hash table O(1) space, O(n) time
        hash_map, count = {}, 0
        for i, t in enumerate(time):
            modulus = t % 60
            diff = (60 - modulus) % 60
            pairs = hash_map.get(diff, 0)
            if pairs > 0:
                count += pairs
            hash_map[modulus] = hash_map.get(modulus, 0) + 1
        # print(hash_map)
        return count

        # # Pythonic – Brute Force O(n^2)
        # pairs = [(time[i], time[j]) for i in range(len(time))
        #          for j in range(len(time)) if i < j and (time[i] + time[j]) % 60 == 0]
        # return len(pairs)
