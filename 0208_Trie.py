"""
208. Implement Trie (Prefix Tree)
https://leetcode.com/problems/implement-trie-prefix-tree/
"""

# https://www.youtube.com/watch?v=KX2GdDZPxQA
# https://en.wikipedia.org/wiki/Trie

class Node:
    def __init__(self):
        self.children = {}  # Store words in the children
        self.word_end = False  # Mark whether or not the end of the word was reached

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = Node()


    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        ptr = self.root  # pointer
        for c in word:  # character
            if c not in ptr.children:
                ptr.children[c] = Node()
            ptr = ptr.children[c]
        ptr.word_end = True


    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        ptr = self.root
        for c in word:  # character
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True if ptr.word_end else False

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        ptr = self.root
        for c in prefix:  # character
            if c not in ptr.children:
                return False
            ptr = ptr.children[c]
        return True


# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
