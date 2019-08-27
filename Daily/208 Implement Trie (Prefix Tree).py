# Url: https://leetcode.com/problems/implement-trie-prefix-tree/
# Related Topics:
# Trie Design

# Example:
# Trie trie = new Trie();
# trie.insert("apple");
# trie.search("apple");   // returns true
# trie.search("app");     // returns false
# trie.startsWith("app"); // returns true
# trie.insert("app");   
# trie.search("app");     // returns true


from collections import defaultdict
from functools import reduce

class Trie:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        MyTrie = lambda: defaultdict(MyTrie)
        self.trie = MyTrie()
        self.END = True

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        reduce(dict.__getitem__, word, self.trie)[self.END] = True
        
    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        trie = self.trie
        for c in word:
            if c not in trie:
                return False
            trie = trie[c]
        return self.END in trie

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        trie = self.trie
        for c in prefix:
            if c not in trie:
                return False
            trie = trie[c]
        return True
        
# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)