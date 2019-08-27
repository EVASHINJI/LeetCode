# Url: https://leetcode.com/problems/map-sum-pairs/
# Related Topics:
# Trie

# Example 1:
# Input: insert("apple", 3), Output: Null
# Input: sum("ap"), Output: 3
# Input: insert("app", 2), Output: Null
# Input: sum("ap"), Output: 5


from collections import defaultdict
from functools import reduce

class MapSum:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        Trie = lambda: defaultdict(Trie)
        self.trie = Trie()
        self.END = True

    def insert(self, key: str, val: int) -> None:
        reduce(dict.__getitem__, key, self.trie)[self.END] = val

    def sum(self, prefix: str) -> int:
        trie = self.trie
        for c in prefix:
            trie = trie[c]
        ans = 0
        stack = [trie]
        while stack:
            cur = stack.pop()
            stack.extend([cur[letter] for letter in cur if letter != self.END])
            if self.END in cur:
                ans += cur[self.END]
        return ans


# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)