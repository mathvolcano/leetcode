"""
1268. Search Suggestions System
https://leetcode.com/problems/search-suggestions-system/
"""

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:

        # Binary search
        # [1] Sort the products lexicographically
        # [2] For each prefix of searchWord Perform a binary search on each prefix
        # to find a match
        # [3] Once a match is found then backtrack to the left until no match is found.
        # [4] Check that the next 3 products have matches and append to results
        # Time complexity is O(p log p + len(searchWord) * log(p)) = O(max(p, len(searchWord)) log p)
        # Space complexity is O(searchWord * max(len(p)))
        def prefix_suggestion(products, prefix):
            l, r, found = 0, len(products) - 1, -1
            while l <= r:
                m = (l + r) // 2
                m_word = products[m]
                if m_word.startswith(prefix):
                    found = m
                    break
                elif m_word[:len(prefix)] > prefix:
                    r = m - 1
                else:  # m_word[:len_prefix] < prefix
                    l = m + 1
            if found < 0:
                return []
            else:
                while found > 0 and products[found-1].startswith(prefix):
                    found -= 1
            res = [products[found]]
            for i in range(1,3):
                if found + i < len(products) and products[found+i].startswith(prefix):
                    res.append(products[found+i])
            return res

        products.sort()
        res = []
        for i in range(len(searchWord)):
            res.append(prefix_suggestion(products, searchWord[:i+1]))
        return res

        # Brute Force
        # Sort the products lexicographically
        # Iterate through each prefix of the searchword and match with top 3 products
        # O(p*s) time and O(s*max(len(p))) space
        # products.sort()
        # res = []
        # for i in range(1, len(searchWord)+1):
        #     prefix = searchWord[:i]
        #     matches = []
        #     for p in products:
        #         if p[:i] == prefix:
        #             matches.append(p)
        #         if len(matches) == 3:
        #             break
        #     res.append(matches)
        # return res
