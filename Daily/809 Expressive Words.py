# Url: https://leetcode.com/problems/expressive-words/
# Related Topics:
# String

# Example:
# S = "heeellooo"
# words = ["hello", "hi", "helo"]
# Output: 1


import itertools
class Solution:
    def expressiveWords(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        def RLE(S):
            return zip(*[(k, len(list(grp))) for k, grp in itertools.groupby(S)])
        
        ans = 0
        G, count = RLE(S)
        for word in words:
            G_w, count_w = RLE(word)
            if G != G_w:
                continue
            ans += all(c1 >= max(c2, 3) or c1 == c2 for c1, c2 in zip(count, count_w))
        return ans