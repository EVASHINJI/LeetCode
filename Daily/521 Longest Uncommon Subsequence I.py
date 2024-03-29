# Url: https://leetcode.com/problems/longest-uncommon-subsequence-i/
# Related Topics:
# String

# Example:
# Input: "aba", "cdc"
# Output: 3


class Solution:
    def findLUSlength(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: int
        """
        if a == b:
            return -1
        return max(len(a), len(b))