# Url: https://leetcode.com/problems/find-and-replace-in-string/
# Related Topics:
# String

# Example:
# Input: S = "abcd", indexes = [0,2], sources = ["a","cd"], targets = ["eee","ffff"]
# Output: "eeebffff"


class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        info = [(i, s, t) for i, s, t in zip(indexes, sources, targets)]
        info.sort(key=lambda x: -x[0])
        for i, s, t in info:
            l = len(s)
            if S[i: i + l] == s:
                S = S[:i] + t + S[i+l:]
        return S