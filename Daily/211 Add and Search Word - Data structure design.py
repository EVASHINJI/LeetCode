# Url: https://leetcode.com/problems/add-and-search-word-data-structure-design/
# Related Topics:
# Trie Design Backtracking

# Example:
# addWord("bad")
# addWord("dad")
# addWord("mad")
# search("pad") -> false
# search("bad") -> true
# search(".ad") -> true
# search("b..") -> true


from collections import defaultdict
from functools import reduce

class WordDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        Trie = lambda: defaultdict(Trie)
        self.trie = Trie()
        self.END = True

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        reduce(dict.__getitem__, word, self.trie)[self.END] = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        """
        tries = [self.trie]
        for c in word:
            if not tries:
                return False
            new_tries = []
            for t in tries:
                if c == '.':
                    new_tries.extend([ch for ch in t.values() if ch != self.END])
                elif c in t:
                    new_tries.append(t[c])
            tries = new_tries
        return any([self.END in t for t in tries])


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)