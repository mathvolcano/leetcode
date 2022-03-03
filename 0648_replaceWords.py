"""
648. Replace Words
https://leetcode.com/problems/replace-words/
"""

class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:

        # Brute Force and use a cache
        # [1] Split the sentence into words
        # [2] Order dictionary lexicographically
        # [2] For each word search cache (hash_map) if found replace, else search sorted dictionary.
        # [3] Replace word with shortest length word
        # [4] if no matches found return same word
        # [5] Concatenate words to end
        # Example 1: but ["cat",'b', "bat","rat"]
        # [1] [-->'the', 'cattle', 'was', 'rattled', 'by', 'the', 'battery',]
        # [2] & [4] ['the', -->'cattle', 'was', 'rattled', 'by', 'the', 'battery',]
        # [3] ['the', 'cat', -->'was', 'rattled', 'by', 'the', 'battery',]
        # [2] ['the', 'cat', 'was', 'rat', 'b', 'the', 'b',]
        # [5] "the cat was rat b the b"
        # Time complexity: O(min(w log(w), n)) for w in dictionary, n words in sentence
        # Space complexity: O(n) additional space for n words in sentence

        cache = {}
        dictionary.sort()
        arr = sentence.split(' ')
        for i, w in enumerate(arr):
            if w in cache:
                arr[i] = cache[w]
            # Match a word to a prefix
            matched = None
            for root in dictionary:
                if w.startswith(root):
                    matched = root
                    break
            if matched:
                arr[i] = matched
                cache[w] = matched
        return ' '.join(arr)
