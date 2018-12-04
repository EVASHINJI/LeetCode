# Url: https://leetcode.com/problems/find-and-replace-pattern/
# Related Topics:
# String

# Example:
# Input: words = ["abc","deq","mee","aqq","dkd","ccc"], pattern = "abb"
# Output: ["mee","aqq"]


class Solution:
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """
        def match(word):
            if len(word) != len(pattern):
                return False
            m1, m2 = {}, {}
            for w, p in zip(word, pattern):
                if w not in m1: m1[w] = p
                if p not in m2: m2[p] = w
                if (m1[w], m2[p]) != (p, w):
                    return False
            return True
        
        return list(filter(match, words))
            