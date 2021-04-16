"""
1151. Minimum Swaps to Group All 1's Together
https://leetcode.com/problems/minimum-swaps-to-group-all-1s-together/
"""

class Solution:
    def minSwaps(self, data: List[int]) -> int:
        ones = sum(data)
        # Iterate through each subarray of len ones
        # Count the number of swaps it needs, ie, the # of zeroes
        # Brute force O(n*k) time, O(n-k) space
        # Note: we don't need to recount the number of zeroes each time.
        min_swaps = float('inf')
        zeros = None
        subarr = []
        for i in range(0, len(data) - ones + 1):
            if not subarr:
                subarr = data[i:ones + i]

            if not zeros:
                zeros = ones - sum(subarr)
            else:
                zeros = zeros + (data[i-1] - data[ones+i-1])
            min_swaps = min(min_swaps, zeros)
        return min_swaps
