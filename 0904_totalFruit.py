"""
904. Fruit Into Baskets
https://leetcode.com/problems/fruit-into-baskets/
"""
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        # Sliding window with hashmap
        # [0] Initialize: result variable, res = 0, to track longest run, left pointer, l =0, h = {} to track fruit: freq
        # [1] For r in range(n))
        #  a. add next fruit to hashmap, h[f] = h.get(f, 0) + 1
        #  b. while len(h) > 2: decrement h[fruits[l]] -= 1 and pop if 0
        #. c. update result
        # Time complexity: O(n) worst case to traverse fruits at most 2x
        # Space compleixty: O(1) to store hashmap of at most 3 kv pairs
        n = len(fruits)
        l, res, h = 0, 0, {}
        for r in range(n):
            f = fruits[r]
            h[f] = h.get(f, 0) + 1
            while len(h) > 2:
                c = fruits[l]
                h[c] -= 1
                if h[c] == 0:
                    del h[c]
                l += 1
            res = max(res, r - l + 1)
        return res
