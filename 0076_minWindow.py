"""
76. Minimum Window Substring
https://leetcode.com/problems/minimum-window-substring/
"""

class Solution:
    def minWindow(self, s: str, t: str) -> str:
        # Filtered Sliding Window
        # Same as sliding window but remove non-t elements of s
        # Example
        #S = "ABCDDDDDDEEAFFBC" T = "ABC"
        # fs = [(0, 'A'), (1, 'B'), (2, 'C'), (11, 'A'), (14, 'B'), (15, 'C')]
        # Here (0, 'A') means in string S character A is at index 0.
        if not t or not s: return ""
        ht = Counter(t)
        nt = len(ht)
        ns = len(s)

        # Filter all the characters from s into a new list along with their index.
        # The filtering criteria is that the character should be present in t.
        fs = []
        for i, c in enumerate(s):
            if c in ht:
                fs.append((i, c))
        l, r = 0, 0
        count = 0
        hs = {}

        res = float("inf"), None, None

        # Look for the characters only in the filtered list instead of entire s. This helps to reduce our search.
        # Hence, we follow the sliding window approach on as small list.
        while r < len(fs):
            c = fs[r][1]
            hs[c] = hs.get(c, 0) + 1

            if hs[c] == ht[c]:
                count += 1

            # If the current window has all the characters in desired frequencies i.e. t is present in the window
            while l <= r and count == nt:
                c = fs[l][1]
                # Save the smallest window until now.
                start, end = fs[l][0], fs[r][0]
                if end - start + 1 < res[0]:
                    res = (end - start + 1, start, end)
                hs[c] -= 1
                if hs[c] < ht[c]:
                    count -= 1
                l += 1
            r += 1
        return "" if res[0] == float("inf") else s[res[1] : res[2] + 1]

        # Sliding Window
        # [0] Initialize
        #. a. hashmaps, ht = Counter(t), and hs = {}
        #. b. left & right window ends, l = r = 0
        #. c. res = 0, res_len = float('inf') to track updates to the result string
        #  d. count = 0 and nt = len(t) to use for checking if we need to update result
        # [1] While r < len(s):
        #  a. Increase r and update hs with char freq if the char is in ht
        #. b. Update count: if hs[c] < hs[t] and c in ht then increment count
        #.    [2] While count == nt and l <= r we contain a substring:
        #.     a. Check if substring is minimum (res_len > length) and update res_len and result
        #      b. c = s[l], decrement hs[c] and count (if necessary when c in ht and hs[c] < ht[c])
        #. c. increment r
        # Complexity: let ns = len(s) and nt = len(t)
        # Space complexity: O(ns + nt) to store hs & ht
        # Time: O(ns + nt) to create hs & ht and traverse hs
#         from collections import Counter
#         hs, ht = {}, Counter(t)
#         l = r = 0
#         res, res_len = '', float('inf')
#         count, nt = 0, len(t)

#         while r < len(s):
#             c = s[r]
#             hs[c] = hs.get(c,0) + 1
#             if c in ht and hs[c] <= ht[c]:
#                 count += 1
#             while l <= r and count == nt:
#                 length = r - l + 1
#                 if length < res_len:
#                     res_len = min(res_len, length)
#                     res = s[l:r+1]

#                 c = s[l]
#                 hs[c] -= 1
#                 if c in ht and hs[c] < ht[c]:
#                     count -= 1
#                 l += 1
#             r += 1
#         return res
Hey, Charlie 👋! It’s been a while since we studied at UCD math together! I hope that you are doing well after grad school. It would be fun to catch up with you at some point!
I wanted to connect you with my friend & one of our fellow UCD math grads, Yoni, because of your mutual interest in environmental science & agriculture and just being cool people. I think that you both would have a lot to talk about and be interested in each other’s perspective on things!
https://www.linkedin.com/in/jonathandackerman/
