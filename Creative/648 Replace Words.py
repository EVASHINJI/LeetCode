# Url: https://leetcode.com/problems/replace-words/
# Related Topics:
# HashTable Trie

# Example:
# Input: dict = ["cat", "bat", "rat"]
# sentence = "the cattle was rattled by the battery"
# Output: "the cat was rat by the bat"

# Creative
# usage of Trie

from collections import defaultdict
from functools import reduce
class Solution:
    def replaceWords(self, dict1: List[str], sentence: str) -> str:
        Trie = lambda: defaultdict(Trie)
        trie = Trie()
        END = True
        for root in dict1:
            reduce(dict.__getitem__, root, trie)[END] = root
        
        def replace(word):
            cur = trie
            for letter in word:
                if letter not in cur or END in cur:
                    break
                cur = cur[letter]
            return cur.get(END, word)
        
        return ' '.join(map(replace, sentence.split()))