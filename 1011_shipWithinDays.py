"""
1011. Capacity To Ship Packages Within D Days
https://leetcode.com/problems/capacity-to-ship-packages-within-d-days/
"""

class Solution:
    def shipWithinDays(self, weights: List[int], D: int) -> int:

        # Binary search
        # [1] Create the answer space [weights[0], sum(weights)] among which we will search for answer.
        # [2] Create a helper so that for a given capacity we determin if the weights can be shipped in D days.
        # [3] Binary search through the answer space to arrive at answer.
        # [4] for a given capacity sum the elements of weights up to the capacity
        # [3] increment a count when the capacity is reached. Check if count after
        # iterating throught weights exceeds D. If so return False else return true
        # O(1) space, O(w * log(sum(weights) - max(weights))) time complexity.

        # Trivial cases
        total = sum(weights)
        if D == 1: return total
        if len(weights) == 1: return weights[0]

        # Binary search
        l, r = max(weights), total
        while l <= r:
            m = (l + r) // 2

            # Count days to ship
            days = 1
            cargo = 0
            for w in weights:
                if cargo + w > m:
                    days += 1
                    cargo = 0
                cargo += w

            # Update capacity search
            if days <= D:
                r = m - 1
            else:
                l = m + 1
        return l


        # Brute Force
        # [1] iterate through the capacities from 1 to sum(weights)
        # [2] for a given capacity sum the elements of weights up to the capacity
        # [3] increment a count when the capacity is reached. Check if count after
        # iterating throught weights exceeds D. If so return False else return true
        # Return the minimal capacity that returned true.
        # O(w*max(weights)) time and O(w) space for copy of weights
#         if D == 1: return sum(weights)

#         def helper(capacity, max_days, weights):
#             n_days = 1
#             cargo = 0
#             while weights:
#                 # Check if possible
#                 if n_days > max_days:
#                     return False
#                 if cargo == 0 and weights[0] > capacity:
#                     return False

#                 if cargo + weights[0] <= capacity:
#                     cargo += weights.pop(0)
#                 else:
#                     n_days += 1
#                     cargo = 0
#             return True

#         max_capacity = sum(weights)
#         capacities = range(weights[0], max_capacity+1)
#         for c in capacities:
#             weights_copy = weights.copy()
#             possible = helper(c, D, weights_copy)
#             if possible:
#                 return c
#         return max_capacity
