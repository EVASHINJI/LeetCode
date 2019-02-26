# Url: https://leetcode.com/problems/longest-word-in-dictionary/
# Related Topics:
# HashTable Trie

# Example 1:
# Input: 
# words = ["w","wo","wor","worl", "world"]
# Output: "world"
# Explanation: 
# The word "world" can be built one character at a time by "w", "wo", "wor", and "worl".
# Example 2:
# Input: 
# words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
# Output: "apple"
# Explanation: 
# Both "apply" and "apple" can be built from other words in the dictionary. However, "apple" is lexicographically smaller than "apply".


class Solution:
    def longestWord(self, words: List[str]) -> str:
        ans = None
        words.sort(key=lambda x: (len(x), x), reverse=True)
        vocab = set(words)
        for w in words:
            if ans and len(w) < len(ans):
                break
            tmp = w[:-1]
            while tmp:
                if tmp not in vocab:
                    break
                tmp = tmp[:-1]
            if not tmp:
                ans = w
        return ans