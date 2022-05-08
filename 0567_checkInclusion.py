"""
567. Permutation in String
https://leetcode.com/problems/permutation-in-string/
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window with array hashtable
        # Refactor
        l1 = [0]*26
        l2 = [0]*26

        for x in s1:
            l1[ord(x) - ord('a')] += 1

        for i in range(len(s2)):
            l2[ord(s2[i]) - ord('a')] += 1
            if i >= len(s1):
                l2[ord(s2[i-len(s1)]) - ord('a')] -= 1
            if l1 == l2:
                return True
        return False


        # Sliding Window with hashmap
        # [0] Initialize left window, l = 0, and right window, r = len(s1) - 1
        #.    and hashmap, h = Counter(s1), and subtract count remaining from s2[:r] and hashset
        # [1] while r < len(s2)
        #     a. if sum of values of h == 0 return true
        #.    b. if s2[l] in s2 chars, then h[s2[l]] += 1, and update l += 1
        #.    c. r += 1 and if s2[r] in s2 then h[s2[r]] -= 1
        # return False
        # Complexity
        # if n1 = len(s1) and n2 = len(s2)
        # Time: O(n1 + n2), n1 to create hashset cs and n2 to traverse s2
        # Space: O(n1) = O(1) to store hashtable & hashset if there are at most 26 chars.

        # cs = set(s1)
        # from collections import Counter
        # h = Counter(s1)
        # # print('h', h)
        # for c in s2[:len(s1)]:
        #     if c in cs:
        #         h[c] -= 1
        # l, r = 0, len(s1) - 1
        # while r < len(s2):
        #     if all(x == 0 for x in h.values()):
        #         return True
        #     cl = s2[l]
        #     if cl in cs:
        #         h[cl] += 1
        #     l += 1
        #     r += 1
        #     if r < len(s2):
        #         cr = s2[r]
        #         if cr in cs:
        #             h[cr] -= 1
        # return False
