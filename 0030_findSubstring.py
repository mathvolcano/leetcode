"""
30. Substring with Concatenation of All Words
https://leetcode.com/problems/substring-with-concatenation-of-all-words/
"""
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        # [1] Initialize
        #. a. Keep the frequency of words in a HashMap, hw = {} word: frequency
        #. b. count = sum(v for v in h.values())
        #. c. res = [], to track the indices
        #. d. l = len(words[0])
        # [2] Starting from every index in the string, try to match all the words.
        # [3] In each iteration i in range (ns - count*l + 1, keep track of all the words that we have already seen in another HashMap, v = {} visited
        # [4] Iterate through the remaining word count j in range(count)
        # [5] Get next word, k = i + j*l, w = s[k:k+l] and update frequency in visited v[w] += 1
        # [4] If a word is not found or has a higher frequency than required, we can move on to the next character in the string, v[w] > h.get(w,0).
        # [5] Store the index if we have found all the words. If j+1 == count
        # Complexity: let W = len(words), S = len(s), L = len(words[0])
        # Time complexity: O(W*S*L) for the 2 for loops and getting the word to check
        # Space complexity: O(W + S) worst case to store hashmaps

        if len(words) == 0 or len(words[0]) == 0: return []
        h = {}
        for w in words:
            h[w] = h.get(w, 0) + 1
        count = sum(v for v in h.values())
        res = []
        l, ns = len(words[0]), len(s)

        for i in range(ns - count*l + 1):
            v = {} # visited words
            for j in range(count):
                k = i + j*l
                w = s[k: k+l]
                v[w] = v.get(w, 0) + 1
                if v[w] > h.get(w,0):
                    break
                if j + 1 == count:
                    res.append(i)
        return res
