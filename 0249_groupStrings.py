"""
249. Group Shifted Strings
https://leetcode.com/problems/group-shifted-strings/
"""

class Solution:
    def groupStrings(self, strings: List[str]) -> List[List[str]]:
        # Hash map
        # Idea is to create a hash table with a key the encoded differences
        # between the letters in the strings and the values the list of strings
        # with this encoding
        # Example hash map
        # h = {
        #      (1, 1): ['abc', 'bcd', 'xyz'],
        #   (2, 2, 1): ['acef'],
        #       (25,): ['az', 'ba'],
        #          (): ['a', 'z']
        # }
        # [0] initialize h = {}
        # [1] for s in strings: k = []
        # [2] for i in range(0, len(s) -1)
        # [3] get d = ord(s[i+1]) - ord(s[i]) % 26 and append to k
        # [4] h[tuple(k)] = s
        # [5] Return list(h.values())
        # Complexity: S = len(strings) and C the length of the longest string
        # Time: Worst case: O(SC)
        # Space: O(SC) to store hashtable.

        h = {}
        for s in strings:
            k = []
            for i in range(len(s)-1):
                k.append((ord(s[i+1]) - ord(s[i])) % 26)
            k = tuple(k)
            h[k] = h.get(k, []) + [s]
        return list(h.values())
