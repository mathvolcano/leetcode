"""
599. Minimum Index Sum of Two Lists
https://leetcode.com/problems/minimum-index-sum-of-two-lists/
"""

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:

        # [1] Use a hash_map to track the indices of restaurants in list1
        # [2] Iterate through list2 to get the restaurant with the min list index sum
        # O(max(n1, n2)) time complexity and space complexity for hash_map and iteration.
        hash_map = {r: i for i, r in enumerate(list1)}  # r restaurant
        min_sum = len(list1) + len(list2)
        res = []

        for i, r in enumerate(list2):
            idx_sum = i + hash_map.get(r, min_sum)
            if idx_sum < min_sum:
                min_sum = idx_sum
                res = [r]
            elif idx_sum == min_sum:
                res.append(r)

        return res

        # Brute Force 2
        # [1] Get the intersection of the lists
        # [2] for every restaurant in the intersection compute the list index sum
        # [3] return the restaurants
        # O(n1 * n2) to compute intersection and O(min(n1, n2)) space for hash_map
        hash_set = set(list1).intersection(set(list2))
        hash_map = {}
        min_sum = float('inf')
        for r in hash_set:
            idx_sum = list1.index(r) + list2.index(r)
            hash_map[r] = idx_sum
            min_sum = min(min_sum, idx_sum)

        res = []
        for r,c in hash_map.items():
            if c == min_sum:
                res.append(r)
        return res

        # Brute Force
        # [1] Enumerate the lists and get all cross pairs and index sums
        # [2] Return the smallest matching pair by sum of index
        # O(max(n1, n2)^2) time and space complexity to compute full cartesan product
        # full = [(x1, x2) for x1 in enumerate(list1)
        #                  for x2 in enumerate(list2)]
        # full = [z for z in full if z[0][1] == z[1][1]]
        # full.sort(key = lambda x: x[0][0] + x[1][0])
        # print(full)
        # print(full[0][0][1])
        # return [''.join(full[0][0][1])]