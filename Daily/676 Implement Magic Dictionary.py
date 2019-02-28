# Url: https://leetcode.com/problems/implement-magic-dictionary/
# Related Topics:
# HashTable Trie

# Example:
# Input: buildDict(["hello", "leetcode"]), Output: Null
# Input: search("hello"), Output: False
# Input: search("hhllo"), Output: True
# Input: search("hell"), Output: False
# Input: search("leetcoded"), Output: False


class MagicDictionary:

    def __init__(self):
        """
        Initialize your data structure here.
        """

    def buildDict(self, dict1: List[str]) -> None:
        """
        Build a dictionary through a list of words
        """
        self.build_set = set(dict1)

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for w in self.build_set:
            if self.isEditDistanceOne(w, word):
                return True
        return False
    
    def isEditDistanceOne(self, w1, w2):
        if len(w1) != len(w2):
            return False
        for i in range(len(w1)):
            if w1[i] != w2[i]:
                return w1[i+1:] == w2[i+1:]
        return False


# Your MagicDictionary object will be instantiated and called as such:
# obj = MagicDictionary()
# obj.buildDict(dict)
# param_2 = obj.search(word)