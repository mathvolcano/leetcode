"""
1044. Longest Duplicate Substring
https://leetcode.com/problems/longest-duplicate-substring/
"""

class Solution:
    def longestDupSubstring(self, s: str) -> str:


        # Binary Search + Rabin-Karp (rolling hash)
        # [1] binary search on the length of the substring
        # [2] use Rabin-Karp rolling has to  search for substring matches of length k
        # Time complexity: Average case O(n log n), worst case O(n^2 log n)
        # Space complexity: O(n^2)

        def RabinKarp(text, M, q):
            if M == 0: return True
            h, t, d = (1<<(8*M-8))%q, 0, 256

            dic = defaultdict(list)
            for i in range(M):
                t = (d * t + ord(text[i]))% q
            dic[t].append(i-M+1)

            for i in range(len(text) - M):
                t = (d*(t-ord(text[i])*h) + ord(text[i + M]))% q
                for j in dic[t]:
                    if text[i+1:i+M+1] == text[j:j+M]:
                        return (True, text[j:j+M])
                dic[t].append(i+1)
            return (False, "")

        l, r = 1, len(s)
        q = (1<<31) - 1
        res = ""
        while l <= r:
            m = (l + r)//2
            isFound, candidate = RabinKarp(s, m, q)
            if isFound:
                l, res = m + 1, candidate
            else:
                r = m - 1
        return res

        # Binary Search & Hash map
        # [1] binary search on the length of the substring
        # [2] to search for substring matches of length k use a hash_map
        # to iterate through the string and count the appearances of the substrings
        # Time complexity: O(n^2 log n)
        # Space complexity: O(n^2)

        # n = len(s)
        # l, r = 0, n
        # res = ''
        # while l <= r:
        #     # Count substrings of length m
        #     m = (l + r) // 2
        #     hm = {}  # hash_map
        #     for i in range(0, n - m + 1):
        #         hm[s[i:i+m]] = hm.get(s[i:i+m], 0) + 1
        #     count = 0
        #     for ss in hm:
        #         if hm[ss] > 1:
        #             count = max(count, hm[ss])
        #             if len(ss) > len(res):
        #                 res = ss
        #     if count > 1:
        #         l = m + 1
        #     else:  # count <= 1, no duplicate substrings found
        #         r = m - 1
        # return res

        # Brute Force
        # [1] Get all substrings of different lengths
        # [2] Search the longest among those substrings
        # O(n^3) time complexity and O(n^2) space complexity
        # n = len(s)
        # substrings = [(s[i:j], j-i) for i in range(n) for j in range(n) if i < j]
        # res = ''
        # for ss, l in substrings:
        #     if len(res) >= l:
        #         continue
        #     count = 0
        #     for k in range(0, n-l+1):
        #         if ss == s[k:k+l]:
        #             count += 1
        #         if count >= 2:
        #             res = ss
        #             break
        # return res
